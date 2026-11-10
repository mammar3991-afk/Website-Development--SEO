#!/usr/bin/env python3
"""Static site builder for octavebytes.com (v2 prototype). Standard library only.

    python3 build.py            build into ./dist
    python3 build.py --serve    build, then serve dist at http://localhost:4321
    python3 build.py --staging  build with noindex + robots Disallow (for a preview host)
    python3 build.py --launch   production build; FAILS while any [[FLAG]] is still open, and strips the review bar

Page sources live in src/pages/*.html. Each starts with a front-matter block:

    ---
    url: /products/hubspot/
    title: Amazon Connect HubSpot Integration | Octavebytes
    description: ...
    product: HubSpot connector        (optional: adds SoftwareApplication schema)
    robots: noindex                   (optional)
    ---

Markup helpers used in page sources:
    {{var:core}}                      value from site.json "vars"
    [[CONFIRM: text]]                 review flag (also PROOF NEEDED, OWNER DECISION,
                                      ASSET NEEDED, DATA NEEDED). Hidden when review mode is off.
    <details class="faq">             turned into FAQPage JSON-LD automatically
"""
import csv, hashlib, html, json, os, re, shutil, sys

from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "tools"))
import contrast
SRC, DIST = ROOT / "src", ROOT / "dist"
CFG = json.loads((ROOT / "site.json").read_text())
VARS = CFG["vars"]
ORIGIN = CFG["origin"]
FLAG_KINDS = ["CONFIRM", "PROOF NEEDED", "OWNER DECISION", "ASSET NEEDED", "DATA NEEDED"]
TODAY = date.today().isoformat()
STAGING = "--staging" in sys.argv  # noindex everything; for preview hosts
LAUNCH = "--launch" in sys.argv    # production: refuses to build while any review flag is open


def parse_page(path):
    raw = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
    if not m:
        raise SystemExit(f"{path}: missing front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def render_includes(text):
    def sub(m):
        f = SRC / "partials" / (m.group(1) + ".html")
        if not f.exists():
            raise SystemExit(f"missing partial {m.group(1)}")
        return render_includes(f.read_text())
    return re.sub(r"\{\{include:([a-z0-9-]+)\}\}", sub, text)


def render_vars(text):
    def sub(m):
        key = m.group(1)
        if key not in VARS:
            raise SystemExit(f"unknown var {key}")
        return VARS[key]
    return re.sub(r"\{\{var:([a-z_]+)\}\}", sub, text)


def render_flags(text):
    pat = re.compile(r"\[\[(" + "|".join(FLAG_KINDS) + r")(?::\s*(.*?))?\]\]", re.S)

    def sub(m):
        kind, body = m.group(1), (m.group(2) or "").strip()
        cls = kind.lower().replace(" ", "-")
        label = f"{kind}: {body}" if body else kind
        return f'<span class="flag flag--{cls}" data-flag>{label}</span>'
    return pat.sub(sub, text)


def strip_tags(s):
    s = re.sub(r"<span class=\"flag[^>]*>.*?</span>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", html.unescape(s)).strip()
    return re.sub(r"\s+([.,;:!?])", r"\1", s)  # no stray space where a link was stripped


def faq_schema(body):
    items = []
    for m in re.finditer(r'<details class="faq"[^>]*>\s*<summary>(.*?)</summary>(.*?)</details>', body, re.S):
        q, a = strip_tags(m.group(1)), strip_tags(m.group(2))
        if q and a:
            items.append({"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a}})
    if not items:
        return None
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}


def build_nav(current):
    out = []
    for i, top in enumerate(CFG["nav"]):
        if "items" in top:
            active = any(current.startswith(it["url"].rstrip("/")) for it in top["items"])
            items = "".join(
                f'<li><a href="{it["url"]}" role="menuitem"><span class="nav__item-label">{it["label"]}</span>'
                f'<span class="nav__item-desc">{it["desc"]}</span></a></li>' for it in top["items"])
            out.append(
                f'<li class="nav__group{" is-active" if active else ""}">'
                f'<button class="nav__toggle" aria-expanded="false" aria-controls="menu-{i}">{top["label"]}'
                f'<svg aria-hidden="true" width="12" height="12" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>'
                f'<ul class="nav__menu" id="menu-{i}" role="menu">{items}</ul></li>')
        else:
            active = current.startswith(top["url"].rstrip("/"))
            cur = ' aria-current="page"' if current == top["url"] else ""
            cls = " is-active" if active else ""
            out.append(f'<li class="nav__group{cls}"><a class="nav__link" href="{top["url"]}"{cur}>{top["label"]}</a></li>')
    return "".join(out)


def build_crumbs(url, titles, existing=frozenset()):
    parts = [p for p in url.strip("/").split("/") if p]
    if not parts:
        return "", None
    crumbs, ld, acc = [("Home", "/")], [], ""
    for p in parts:
        acc += f"/{p}"
        u = acc + "/"
        label = titles.get(u) or p.replace("-", " ").title()
        crumbs.append((label, u))
    def li(i, l, u):
        if i == len(crumbs) - 1:
            return f'<li><span aria-current="page">{l}</span></li>'
        if u in existing or u == "/":
            return f'<li><a href="{u}">{l}</a></li>'
        return f"<li><span>{l}</span></li>"  # section has no page of its own: label only
    lis = "".join(li(i, l, u) for i, (l, u) in enumerate(crumbs))
    linkable = [(l, u) for i, (l, u) in enumerate(crumbs) if u in existing or u == "/" or i == len(crumbs) - 1]
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": l, "item": ORIGIN + u}
                              for i, (l, u) in enumerate(linkable)]}
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>', ld


def product_schema(meta):
    offers = [{"@type": "Offer", "name": "Octave Connector subscription", "price": VARS["price"], "priceCurrency": "USD",
               "priceSpecification": {"@type": "UnitPriceSpecification", "price": VARS["price"], "priceCurrency": "USD",
                                      "unitText": "per agent per month", "billingDuration": 1, "billingIncrement": 1}}]
    return {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": meta["product"],
            "applicationCategory": "BusinessApplication", "operatingSystem": "Web browser",
            "publisher": {"@id": ORIGIN + "/#organization"}, "url": ORIGIN + meta["url"],
            "description": render_vars(meta["description"]), "image": ORIGIN + OG_IMAGE,
            **({} if meta.get("offer") == "none" else {"offers": offers})}


OG_IMAGE = "/assets/img/og-contact-center.png"


def org_schema():
    def addr(street, city, region, code, country):
        a = {"@type": "PostalAddress", "streetAddress": street, "addressLocality": city, "postalCode": code, "addressCountry": country}
        if region:
            a["addressRegion"] = region
        return {k: v for k, v in a.items() if v}
    return {"@context": "https://schema.org", "@type": "Organization", "@id": ORIGIN + "/#organization",
            "name": "Octavebytes", "url": ORIGIN + "/",
            "logo": ORIGIN + "/assets/img/logo.png", "image": ORIGIN + OG_IMAGE,
            "description": "Amazon Connect partner: migration, custom builds, bots and AI, and CRM connectors for HubSpot and Dynamics 365.",
            "email": VARS["sales_email"], "telephone": VARS["phone_us"],
            "address": [addr("10808 Capri Dr", "McKinney", "TX", "75072", "US"),
                        addr("128 City Road", "London", "", "EC1V 2NX", "GB"),
                        addr("Office 2, 4th Floor, 36 Civic Centre, Garden Town", "Lahore", "", "", "PK")],
            "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": VARS["sales_email"], "telephone": VARS["phone_us"], "availableLanguage": ["English"]},
                             {"@type": "ContactPoint", "contactType": "customer support", "email": VARS["support_email"]}],
            "sameAs": ["https://www.linkedin.com/company/octavebytes", VARS["aws_marketplace_url"], VARS["hubspot_marketplace_url"]],
            "knowsAbout": ["Amazon Connect", "Contact center migration", "CTI integration", "HubSpot", "Microsoft Dynamics 365"]}


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": ORIGIN + "/#website", "name": "Octavebytes",
            "url": ORIGIN + "/", "publisher": {"@id": ORIGIN + "/#organization"}, "inLanguage": "en"}


def article_schema(meta, body):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    a = {"@context": "https://schema.org", "@type": "Article",
         "headline": strip_tags(m.group(1)) if m else meta["title"].split("|")[0].strip(),
         "description": render_vars(meta["description"]), "image": ORIGIN + OG_IMAGE,
         "mainEntityOfPage": ORIGIN + meta["url"], "inLanguage": "en",
         "author": {"@type": "Organization", "name": "Octavebytes", "url": ORIGIN + "/"},
         "publisher": {"@id": ORIGIN + "/#organization"}}
    if meta.get("updated"):
        a["dateModified"] = meta["updated"]
    return a


THEME_LOGO = {"a": "logo.png", "b": "logo.png", "c": "logo-c.png", "d": "logo-d.png"}


def logos(theme, footer=False):
    """Prototype: one <img> per look (CSS shows the active one). Launch: only the chosen theme's logo."""
    def img(key, fname):
        cls = f"logo logo--{key}" + (" footer__logo" if footer else "")
        return f'<img class="{cls}" src="/assets/img/{fname}" width="181" height="32" alt="Octavebytes">'
    if LAUNCH or CFG.get("theme_locked"):
        k = theme if theme in "cd" else "a"
        return img(k, THEME_LOGO[theme])
    return "".join(img(k, f) for k, f in (("a", "logo.png"), ("c", "logo-c.png"), ("d", "logo-d.png")))


def contrast_html(key):
    rows = contrast.report()[key]
    ok = sum(1 for r in rows if r[5])
    body = "".join(
        f'<tr><td>{html.escape(l)}</td><td class="mono"><span class="sw" style="background:{bg}"><span style="color:{fg}">Aa</span></span> {fg} on {bg}</td>'
        f'<td>{r:.2f}:1</td><td>{need}:1</td><td>{"Pass" if good else "FAIL"}</td></tr>' for l, fg, bg, r, need, good in rows)
    low = min(r[3] for r in rows)
    return (f'<summary>Measured contrast: {ok} of {len(rows)} pairs pass; lowest {low:.2f}:1</summary>'
            f'<div class="table-wrap"><table><thead><tr><th scope="col">Pair</th><th scope="col">Colours</th><th scope="col">Ratio</th><th scope="col">Needs</th><th scope="col">Result</th></tr></thead><tbody>{body}</tbody></table></div>')


THEME_INFO = {
    "a": ("Current blue", "The live site's blue, kept as it is. Matches the existing logo and marketplace listings, so it is the safest choice."),
    "b": ("Indigo and amber", "A deeper indigo for trust and focus, with an amber accent for warmth. The existing blue logo still fits, so nothing else changes."),
    "c": ("Teal", "A calm teal on a deep green-black. Feels different from every competitor's blue. Uses a recoloured logo."),
    "d": ("Graphite and orange", "Neutral graphite with a burnt-orange accent. The most distinct and the most energetic. Uses a recoloured logo."),
}


def theme_panels():
    tpl = (SRC / "partials" / "theme-panel.html").read_text()
    out = []
    for key, (name, desc) in THEME_INFO.items():
        out.append(tpl.replace("@@KEY@@", key).replace("@@UP@@", key.upper()).replace("@@NAME@@", name)
                   .replace("@@DESC@@", desc).replace("@@LOGOS@@", logos_for_panel()).replace("@@CONTRAST@@", contrast_html(key)))
    return "\n".join(out)


def logos_for_panel():
    return "".join(f'<img class="logo logo--{k}" src="/assets/img/{f}" width="181" height="32" alt="Octavebytes">' for k, f in (("a", "logo.png"), ("c", "logo-c.png"), ("d", "logo-d.png")))


def main():
    layout = (SRC / "layout.html").read_text()
    pages = []
    for p in sorted((SRC / "pages").glob("*.html")):
        meta, body = parse_page(p)
        if meta.get("hidden") == "true":
            continue  # hidden in this release: not built, not in the sitemap, no launch flags
        pages.append((p.name, meta, body))
    titles = {}
    for _, meta, _ in pages:
        titles[meta["url"]] = meta.get("crumb") or meta["title"].split("|")[0].strip()
    existing = {m["url"] for _, m, _ in pages}
    titles["/products/"] = "Products"; titles["/solutions/"] = "Solutions"; titles["/resources/"] = "Resources"
    titles["/company/"] = "Company"; titles["/legal/"] = "Legal"

    sitemap, report = [], []
    open_flags = {}
    flag_pat = re.compile(r"\[\[(" + "|".join(FLAG_KINDS) + r")(?::\s*(.*?))?\]\]", re.S)
    for fname, meta, body in pages:
        found = [(m.group(1), re.sub(r"\s+", " ", (m.group(2) or "").strip())) for m in flag_pat.finditer(render_vars(render_includes(body)))]
        if found:
            open_flags[meta["url"]] = found
    if LAUNCH and open_flags:
        n = sum(len(v) for v in open_flags.values())
        lines = [f"LAUNCH BLOCKED: {n} review flags are still open on {len(open_flags)} pages:"]
        for u, v in open_flags.items():
            lines.append(f"  {u}: {len(v)}")
        lines.append("Resolve each flag (confirm the fact, get the proof, or remove the claim), then rebuild. See FLAGS.md.")
        write_flags(open_flags, CFG)
        raise SystemExit("\n".join(lines))
    write_flags(open_flags, CFG)
    # only now touch dist/, so a blocked launch build leaves the previous build intact
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(SRC / "assets", DIST / "assets")
    if (SRC / "static").is_dir():  # root-level files that must keep their exact URL (e.g. Search Console verification)
        for f in (SRC / "static").iterdir():
            shutil.copy(f, DIST / f.name)
    for fname, meta, body in pages:
        url = meta["url"]
        if (LAUNCH or CFG.get("theme_locked")) and meta.get("prototype"):
            continue  # prototype-only pages (theme comparison) never ship
        body = render_includes(body)
        if "{{themepanels}}" in body:
            body = body.replace("{{themepanels}}", theme_panels())
        body = render_flags(render_vars(body))
        crumbs_html, crumbs_ld = build_crumbs(url, titles, existing) if url != "/404.html" else ("", None)
        ld = []
        if url == "/":
            ld += [org_schema(), website_schema()]
        if meta.get("schema") == "organization":
            ld.append(org_schema())
        if meta.get("schema") == "article":
            ld.append(article_schema(meta, body))
        if meta.get("product"):
            ld.append(product_schema(meta))
        fq = faq_schema(body)
        if fq:
            ld.append(fq)
        if crumbs_ld:
            ld.append(crumbs_ld)
        jsonld = "".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in ld)
        canonical = ORIGIN + (url if url != "/404.html" else "/")
        page = layout
        repl = {
            "title": html.escape(render_vars(meta["title"])),
            "description": html.escape(render_vars(meta["description"])),
            "canonical": canonical,
            "robots": "noindex, nofollow" if STAGING else meta.get("robots", "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"),
            "og_type": "article" if meta.get("schema") == "article" else "website",
            "body_class": "page-" + (url.strip("/").replace("/", "-") or "home"),
            "nav": build_nav(url),
            "crumbs": crumbs_html if not meta.get("nocrumbs") else "",
            "jsonld": jsonld,
            "content": body,
            "hs_config": json.dumps({"portalId": CFG["hubspot"]["portalId"], "formGuids": CFG["hubspot"]["formGuids"], "formDefaults": CFG["hubspot"].get("formDefaults", {}), "ga4Id": "" if STAGING else CFG.get("ga4Id", ""), "clarityId": "" if STAGING else CFG.get("clarityId", "")}),
            "year": str(date.today().year),
            "css_v": hashlib.md5((SRC / "assets/css/site.css").read_bytes()).hexdigest()[:8],
            "js_v": hashlib.md5((SRC / "assets/js/site.js").read_bytes()).hexdigest()[:8],
            "theme": CFG.get("theme", "a"),
            "logo": logos(CFG.get("theme", "a")),
            "logo_footer": logos(CFG.get("theme", "a"), footer=True),
            "aws_marketplace_url": VARS["aws_marketplace_url"],
            "hubspot_marketplace_url": VARS["hubspot_marketplace_url"],
            "sales_email": VARS["sales_email"], "support_email": VARS["support_email"],
            "phone_us": VARS["phone_us"], "phone_pk": VARS["phone_pk"],
        }
        for k, v in repl.items():
            page = page.replace("{{" + k + "}}", v)
        page = render_flags(page)
        if CFG.get("theme_locked"):
            page = re.sub(r"<!--THEME-->.*?<!--/THEME-->", "", page, flags=re.S)
        else:
            page = page.replace("<!--THEME-->", "").replace("<!--/THEME-->", "")
        if LAUNCH:
            page = re.sub(r"<!--REVIEW-->.*?<!--/REVIEW-->", "", page, flags=re.S)
        left = re.findall(r"\{\{[a-z_:]+\}\}", page)
        if left:
            raise SystemExit(f"{fname}: unresolved placeholders {left}")
        out = DIST / "404.html" if url == "/404.html" else DIST / url.strip("/") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page)
        if "noindex" not in meta.get("robots", "") and url != "/404.html":
            sitemap.append((url, meta.get("updated")))
        report.append((url, meta["title"], meta["description"]))

    # sitemap, robots
    urls = "".join(f"<url><loc>{ORIGIN}{u}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>" for u, d in sorted(sitemap, key=lambda x: x[0]))
    (DIST / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    if STAGING:
        (DIST / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
    else:
        (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n")

    write_redirects()
    (DIST / "BUILD-INFO.txt").write_text(f"Built {TODAY}. {len(pages)} pages.\n")
    print(f"built {len(pages)} pages -> {DIST}")
    return report


def write_flags(open_flags, cfg):
    """Write FLAGS.md: the owner's punch list of everything that must be confirmed before launch."""
    order = {k: i for i, k in enumerate(FLAG_KINDS)}
    total = sum(len(v) for v in open_flags.values())
    kinds = {}
    for v in open_flags.values():
        for k, _ in v:
            kinds[k] = kinds.get(k, 0) + 1
    out = ["# Open review flags", "",
           "Generated by `build.py`. Every item is a fact, promise, price, proof point or asset that must be resolved before launch.",
           "`python3 build.py --launch` refuses to build while any of these remain.", "",
           f"**{total} open flags on {len(open_flags)} pages.** " + ", ".join(f"{k}: {n}" for k, n in sorted(kinds.items(), key=lambda x: order[x[0]])), ""]
    for url, items in sorted(open_flags.items()):
        out.append(f"## `{url}` ({len(items)})")
        for k, t in sorted(items, key=lambda x: order[x[0]]):
            out.append(f"- **{k}**" + (f": {t}" if t else ""))
        out.append("")
    (ROOT / "FLAGS.md").write_text("\n".join(out))


def write_redirects():
    """Parse the redirect map in design/05-seo-and-migration-plan.md and emit server configs."""
    md = (ROOT.parent / "design" / "05-seo-and-migration-plan.md").read_text()
    rows = []
    for m in re.finditer(r"^\| `(/[^`]*)` \| (?:`(/[^`]*)`|—) \| (301|410)[^|]*\|", md, re.M):
        old, new, code = m.group(1), m.group(2), m.group(3)
        if old == "/":
            continue
        rows.append((old, new, code))
    extra = [("/category/case-study/", "/customers/", "301"),
             ("/category/chatbots/", "/resources/guides/", "301"),
             ("/category/cti/", "/resources/guides/", "301"),
             ("/category/cloud-cc-technologies/", "/resources/guides/", "301"),
             ("/category/wallboard/", "/resources/guides/", "301"),
             ("/category/uncategorized/", "/resources/guides/", "301"),
             ("/elementor-hf/about/", None, "410"), ("/elementor-hf/footer-2/", None, "410"),
             ("/feed/", None, "410"), ("/comments/feed/", None, "410"), ("/author/admin/", None, "410")]
    seen = {r[0] for r in rows}
    rows += [e for e in extra if e[0] not in seen]
    dep = ROOT / "deploy"
    dep.mkdir(exist_ok=True)
    with open(dep / "redirects.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["old", "new", "code"]); w.writerows(rows)
    # Apache (.htaccess), typical of GoDaddy shared hosting
    ap = ["# Generated by build.py from design/05-seo-and-migration-plan.md. Do not edit by hand.",
          "RewriteEngine On", "RewriteBase /", ""]
    for old, new, code in rows:
        pat = re.escape(old.strip("/")).replace("\\/", "/")
        if code == "301":
            ap.append(f"RewriteRule ^{pat}/?$ {new} [R=301,L]")
        else:
            ap.append(f"RewriteRule ^{pat}/?$ - [G,L]")
    htaccess_head = (DEPLOY_HEAD)
    (DIST / ".htaccess").write_text(htaccess_head + "\n".join(ap) + "\n" + HTACCESS_TAIL)
    # nginx (Contabo VPS)
    ng = ["# Generated by build.py. Include inside the server {} block.", ""]
    for old, new, code in rows:
        if code == "301":
            ng.append(f"location = {old.rstrip('/')} {{ return 301 {new}; }}")
            ng.append(f"location = {old} {{ return 301 {new}; }}")
        else:
            ng.append(f"location = {old.rstrip('/')} {{ return 410; }}")
            ng.append(f"location = {old} {{ return 410; }}")
    (dep / "nginx-redirects.conf").write_text("\n".join(ng) + "\n")


DEPLOY_HEAD = """# Octavebytes static site: Apache config (GoDaddy shared hosting / any Apache).
# Generated by build.py.
Options -Indexes
ErrorDocument 404 /404.html
DirectoryIndex index.html

<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml
</IfModule>

<IfModule mod_rewrite.c>
# Force HTTPS and the bare domain
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
RewriteRule ^ https://%1%{REQUEST_URI} [R=301,L]
"""
HTACCESS_TAIL = "</IfModule>\n"


def serve():
    """Dev server. Resolves dist/ on every request, so rebuilding while serving is safe."""
    import http.server, socketserver

    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(DIST), **kw)

        def send_error(self, code, message=None, explain=None):
            page = DIST / "404.html"
            if code == 404 and page.exists():
                data = page.read_bytes()
                self.send_response(404); self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(data))); self.end_headers()
                if self.command != "HEAD": self.wfile.write(data)
                return
            super().send_error(code, message, explain)

        def end_headers(self):
            self.send_header("Cache-Control", "no-store")  # dev only
            super().end_headers()

        def log_message(self, *a):
            pass
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", 4321), H) as httpd:
        print("serving http://localhost:4321  (Ctrl+C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
    if "--serve" in sys.argv:
        serve()
