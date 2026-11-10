# Deploying the static site

The build output (`dist/`) is plain files: HTML, CSS, one small JS file and two fonts. It needs **no PHP, database or Node** on the server. Forms post from the visitor's browser straight to HubSpot, so nothing runs server-side.

> **Nothing here has been run against a live server.** The Apache and nginx redirect rules were checked with a local self-test (all 49 legacy URLs match exactly one rule; no live page is captured), but not on a real Apache or nginx. Test on a staging host first.

## Before any deploy

```bash
python3 build.py --launch   # production build. FAILS while any review flag is open (see FLAGS.md)
python3 tools/check.py      # 0 errors required
```

For a preview that search engines must not index, use `python3 build.py --staging` (adds `noindex` and `Disallow: /`).

## Option A: Contabo VPS (recommended if you are comfortable with a server)

A Contabo VPS is unmanaged: you own updates and security. Set up once:

1. Create a non-root user (for example `deploy`) with your SSH key; disable password login.
2. `sudo apt install nginx certbot python3-certbot-nginx rsync ufw fail2ban unattended-upgrades`
3. Allow only SSH, HTTP, HTTPS: `sudo ufw allow OpenSSH && sudo ufw allow 'Nginx Full' && sudo ufw enable`
4. `sudo mkdir -p /var/www/octavebytes && sudo chown deploy: /var/www/octavebytes`
5. Copy `nginx-redirects.conf` to `/etc/nginx/snippets/octavebytes-redirects.conf`, and `nginx-site.conf` to `/etc/nginx/sites-available/octavebytes`. Symlink it into `sites-enabled`.
6. Point a **staging** name (for example `new.octavebytes.com`) at the server, get a certificate with `certbot --nginx`, and run `sudo nginx -t && sudo systemctl reload nginx`.

Then each deploy is one command, with atomic switch and instant rollback:

```bash
HOST=<server-ip> SSH_USER=deploy ./deploy/deploy-contabo.sh --staging   # staging
HOST=<server-ip> SSH_USER=deploy ./deploy/deploy-contabo.sh             # production (launch build)
```

## Option B: GoDaddy (Linux/cPanel hosting)

1. Confirm the plan is **Linux hosting with cPanel** (Apache). Windows or Plesk plans ignore `.htaccess` and would need a `web.config`; tell me if that is your case and I will generate it.
2. Run `python3 build.py --launch` and zip the **contents** of `dist/` (not the folder). The file `.htaccess` is hidden on macOS; make sure it is in the zip (`cd dist && zip -r ../site.zip . -x '.DS_Store'`).
3. In cPanel, open File Manager, enable "Show hidden files", and upload the zip into `public_html` (for staging, into the staging subdomain's folder). Extract it.
4. Turn on SSL for the domain in cPanel (AutoSSL or GoDaddy's SSL). The `.htaccess` forces HTTPS and the bare domain.
5. Open a few old URLs (for example `/hubspot-cti-connector/`) and confirm they redirect.

**Take a full backup of the current WordPress site first** (files and database) and keep it for at least 30 days.

## Cut-over checklist (from `design/05-seo-and-migration-plan.md`)

1. Search Console, GA4 and a backlink export are captured *before* anything changes (baseline).
2. The new site is live on a staging host, reviewed, and `python3 build.py --launch` succeeds.
3. In HubSpot, create the six forms and put their GUIDs in `site.json` (see `../README.md`), then submit a test trial request and confirm a contact and deal appear.
4. Lower the DNS TTL 24 hours ahead. Switch DNS (or replace the WordPress files) in one step. **Do not run the old and new sites under the same domain at once.**
5. Confirm the redirects, the sitemap, `robots.txt` and forms. Submit the sitemap in Search Console.
6. Watch 404s and Search Console daily for the first week. Keep redirects for at least 12 months.

## Files

| File | For |
|---|---|
| `nginx-site.conf` | nginx server blocks (Contabo) |
| `nginx-redirects.conf` | generated redirects for nginx |
| `deploy-contabo.sh` | build, check, upload, switch, rollback |
| `redirects.csv` | the same redirect map as data (60 rows) |
| `../dist/.htaccess` | generated Apache rules: HTTPS, redirects, security headers, caching (GoDaddy) |
