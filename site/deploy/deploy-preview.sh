#!/usr/bin/env bash
# Deploy a NON-INDEXED preview build (noindex + robots Disallow) to the server in deploy/.env.
# Usage: ./deploy/deploy-preview.sh      Never touches DNS. Review flags stay visible in preview.
set -euo pipefail
cd "$(dirname "$0")"
[[ -f .env ]] || { echo "Missing deploy/.env (copy .env.example)"; exit 1; }
set -a; source .env; set +a
: "${SERVER_HOST:?fill SERVER_HOST in deploy/.env}"; : "${SERVER_USER:?fill SERVER_USER}"
PORT="${SERVER_PORT:-22}"; BASE="${REMOTE_BASE:-/var/www/octavebytes-preview}"
SSH_OPTS=(-p "$PORT" -o StrictHostKeyChecking=accept-new)
[[ -n "${SSH_KEY:-}" ]] && SSH_OPTS+=(-i "$SSH_KEY")
RUN=()
if [[ -z "${SSH_KEY:-}" && -n "${SERVER_PASSWORD:-}" ]]; then
  command -v sshpass >/dev/null || { echo "Password login needs sshpass (brew install sshpass)"; exit 1; }
  export SSHPASS="$SERVER_PASSWORD"; RUN=(sshpass -e)
fi
cd ..
python3 build.py --staging
python3 tools/check.py
REL="release-$(date +%Y%m%d-%H%M%S)"; T="$SERVER_USER@$SERVER_HOST"
"${RUN[@]}" ssh "${SSH_OPTS[@]}" "$T" "mkdir -p '$BASE/releases/$REL'"
tar -C dist -czf - . | "${RUN[@]}" ssh "${SSH_OPTS[@]}" "$T" "tar -xzf - -C '$BASE/releases/$REL'"
"${RUN[@]}" ssh "${SSH_OPTS[@]}" "$T" "ln -sfn '$BASE/releases/$REL' '$BASE/current' && cd '$BASE/releases' && ls -1dt release-* | tail -n +6 | xargs -r rm -rf"
# Keep the legacy-URL redirect rules in sync (included by /opt/ob-preview/nginx.conf), then reload only this preview nginx
"${RUN[@]}" scp -P "$PORT" "${SSH_OPTS[@]:2}" deploy/nginx-redirects.conf "$T:$BASE/redirects.conf"
"${RUN[@]}" ssh "${SSH_OPTS[@]}" "$T" "nginx -t -c '$BASE/nginx.conf' && kill -HUP \$(cat '$BASE/nginx.pid')"
echo "Preview live: $REL  (serve $BASE/current with nginx; see deploy/README.md)"
