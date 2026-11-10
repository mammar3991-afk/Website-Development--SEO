#!/usr/bin/env bash
# Deploy the static site to a Contabo (or any Linux) VPS over SSH, with instant rollback.
# Usage:  HOST=203.0.113.10 SSH_USER=deploy ./deploy/deploy-contabo.sh [--staging]
# Nothing here runs unless you run it. It never touches DNS.
set -euo pipefail
: "${HOST:?set HOST to the server IP or name}"
: "${SSH_USER:?set SSH_USER}"
REMOTE_BASE="${REMOTE_BASE:-/var/www/octavebytes}"
cd "$(dirname "$0")/.."

if [[ "${1:-}" == "--staging" ]]; then
  python3 build.py --staging
else
  python3 build.py --launch          # refuses to build while any review flag is open
fi
python3 tools/check.py               # refuses to deploy if any check fails

REL="release-$(date +%Y%m%d-%H%M%S)"
echo "Uploading to $SSH_USER@$HOST:$REMOTE_BASE/releases/$REL"
ssh "$SSH_USER@$HOST" "mkdir -p '$REMOTE_BASE/releases/$REL'"
rsync -az --delete dist/ "$SSH_USER@$HOST:$REMOTE_BASE/releases/$REL/"
# Switch the 'current' symlink atomically; keep the last 5 releases for rollback
ssh "$SSH_USER@$HOST" "ln -sfn '$REMOTE_BASE/releases/$REL' '$REMOTE_BASE/current' && cd '$REMOTE_BASE/releases' && ls -1dt release-* | tail -n +6 | xargs -r rm -rf"
echo "Live: $REL"
echo "Rollback: ssh $SSH_USER@$HOST \"ln -sfn $REMOTE_BASE/releases/<previous-release> $REMOTE_BASE/current\""
