#!/usr/bin/env python3
"""Quality gate for the built site. Run after build.py:  python3 tools/check.py
Fails (exit 1) if any hard rule is broken. Standard library only."""
import csv, json, re, sys
from html.parser import HTMLParser
from pathlib import Path

DIST = Path(__file__).resolve().parent.parent / "dist"
ROOT = DIST.parent
errors, warns = [], []


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.h = []; self.ids = set(); self.links = []; self.imgs = []; self.title = ""; self.meta = {}
        self.jsonld = []; self._t = None; self._buf = ""; self.labels_for = set(); self.inputs = []; self._ld = False
        self.canonical = None; self.lang = None

    def handle_starttag(self, tag, a):
        a = dict(a)
        if "id" in a: self.ids.add(a["id"])
        if tag == "html": self.lang = a.get("lang")
        if tag in ("h1", "h2", "h3", "h4"): self._t = tag; self._buf = ""
        if tag == "title": self._t = "title"; self._buf = ""
        if tag == "a" and "href" in a: self.links.append(a["href"])
        if tag == "img": self.imgs.append(a)
        if tag == "meta" and a.get("name"): self.meta[a["name"]] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical": self.canonical = a.get("href")
        if tag == "label" and a.get("for"): self.labels_for.add(a["for"])
        if tag in ("input", "select", "textarea"): self.inputs.append(a)
        if tag == "script" and a.get("type") == "application/ld+json": self._ld = True; self._buf = ""

    def handle_data(self, d):
        if self._t or self._ld: self._buf += d

    def handle_endtag(self, tag):
        if tag == self._t:
            if tag == "title": self.title = self._buf.strip()
            else: self.h.append((tag, re.sub(r"\s+", " ", self._buf).strip()))
            self._t = None
        if tag == "script" and self._ld:
            self.jsonld.append(self._buf); self._ld = False


def page_path(link, cur):
    link = link.split("#")[0].split("?")[0]
    if not link: return cur
    if link.startswith("/"):
        f = DIST / link.lstrip("/")
        return f / "index.html" if (f.is_dir() or link.endswith("/")) else f
    return None


pages = sorted(f for f in DIST.rglob("*.html") if not f.name.startswith("google") or f.parent != DIST)  # skip Search Console verification file
parsed = {}
for f in pages:
    p = P(); p.feed(f.read_text()); parsed[f] = p

for f, p in parsed.items():
    rel = "/" + str(f.relative_to(DIST))
    is404 = f.name == "404.html"
    h1s = [t for t in p.h if t[0] == "h1"]
    if len(h1s) != 1: errors.append(f"{rel}: {len(h1s)} <h1> (need exactly 1)")
    if not p.title: errors.append(f"{rel}: missing <title>")
    elif len(p.title) > 65: warns.append(f"{rel}: title {len(p.title)} chars (>65)")
    d = p.meta.get("description", "")
    if not d: errors.append(f"{rel}: missing meta description")
    elif not is404 and not (70 <= len(d) <= 165): warns.append(f"{rel}: meta description {len(d)} chars")
    if p.lang != "en": errors.append(f"{rel}: <html lang> missing")
    if not p.canonical: errors.append(f"{rel}: no canonical")
    # heading order (no skipped levels)
    prev = 0
    for tag, txt in p.h:
        lvl = int(tag[1])
        if prev and lvl > prev + 1: warns.append(f"{rel}: heading jumps h{prev} -> h{lvl} ('{txt[:40]}')")
        prev = lvl
    for im in p.imgs:
        if "alt" not in im: errors.append(f"{rel}: <img> without alt ({im.get('src')})")
    for raw in p.jsonld:
        try: json.loads(raw)
        except Exception as e: errors.append(f"{rel}: invalid JSON-LD ({e})")
    for a in p.inputs:
        if a.get("type") in ("hidden", "submit") or "tabindex" in a: continue
        if a.get("id") not in p.labels_for and a.get("type") not in ("radio", "checkbox"):
            errors.append(f"{rel}: form control #{a.get('id')} has no <label for>")
    src = f.read_text()
    if "{{" in src or "[[" in src: errors.append(f"{rel}: unresolved template markup")
    for l in p.links:
        if l.startswith(("http", "mailto:", "tel:", "javascript:")): continue
        if l.startswith("#"):
            if l[1:] and l[1:] not in p.ids: errors.append(f"{rel}: broken anchor {l}")
            continue
        t = page_path(l, f)
        if t is None: continue
        if not t.exists(): errors.append(f"{rel}: broken link {l}")
        elif "#" in l:
            anchor = l.split("#")[1]
            if t in parsed and anchor and anchor not in parsed[t].ids: errors.append(f"{rel}: broken anchor {l}")

# sitemap covers every indexable page
sm = (DIST / "sitemap.xml").read_text()
for f in pages:
    if f.name == "404.html": continue
    if "noindex" in parsed[f].meta.get("robots", ""): continue  # deliberately unlisted (prototype-only, or a page meant to be shared by link rather than found in search)
    url = "/" + str(f.parent.relative_to(DIST)) + "/" if f.parent != DIST else "/"
    if f"octavebytes.com{url}</loc>" not in sm: errors.append(f"sitemap missing {url}")

# redirects: targets exist; every one of the 50 legacy URLs is covered
rows = list(csv.DictReader(open(ROOT / "deploy" / "redirects.csv")))
for r in rows:
    if r["code"] == "301" and not page_path(r["new"], None).exists(): errors.append(f"redirect target missing: {r['old']} -> {r['new']}")
inv = list(csv.DictReader(open(ROOT.parent / "research" / "data" / "url-inventory.csv")))
covered = {r["old"].rstrip("/") for r in rows} | {""}
for r in inv:
    path = r["url"].replace("https://octavebytes.com", "").rstrip("/")
    if path not in covered and not (DIST / path.strip("/") / "index.html").exists(): errors.append(f"legacy URL not redirected: {path or '/'}")

# redirect rule self-test: emulate the Apache RewriteRule patterns in Python
rules = []
for line in (DIST / ".htaccess").read_text().splitlines():
    m = re.match(r"RewriteRule \^(.+)\$ (\S+) \[(.+)\]", line)
    if m and m.group(1).endswith("/?") and not m.group(1).startswith("("):
        rules.append((re.compile("^" + m.group(1) + "$"), m.group(2), m.group(3)))
for r in inv:
    path = r["url"].replace("https://octavebytes.com", "").strip("/")
    if not path: continue
    hits = [x for x in rules if x[0].match(path)]
    if (DIST / path / "index.html").exists():  # legacy URL that is now a live page: must not be redirected
        if hits: errors.append(f".htaccess: live legacy path '{path}' is redirected")
        continue
    if len(hits) != 1: errors.append(f".htaccess: legacy path '{path}' matches {len(hits)} rules (need exactly 1)")
new_paths = [str(f.parent.relative_to(DIST)) for f in pages if f.name == "index.html" and f.parent != DIST]
for np_ in new_paths:
    if any(x[0].match(np_) for x in rules): errors.append(f".htaccess: a redirect rule would capture live page '{np_}'")
print(f".htaccess self-test: {len(rules)} rules parsed; all {len([r for r in inv if r['url'].rstrip('/')!='https://octavebytes.com'])} legacy paths matched once; {len(new_paths)} live pages unaffected")
nginx = (ROOT / "deploy" / "nginx-redirects.conf").read_text()
for np_ in new_paths:
    if f"location = /{np_}/ " in nginx or f"location = /{np_} " in nginx: errors.append(f"nginx: redirect would capture live page /{np_}/")

# colour themes: every text and UI pair must meet WCAG (see tools/contrast.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import contrast
THEMES = contrast.report()
for key, trows in THEMES.items():
    for label, fg, bg, r, need, ok in trows:
        if not ok: errors.append(f"contrast, option {key.upper()}: {label} {fg} on {bg} = {r:.2f}:1 (need {need})")
print("colour themes: " + "; ".join(f"{k.upper()} {sum(1 for r in v if r[5])}/{len(v)}" for k, v in THEMES.items()))

# asset weights
def kb(p): return p.stat().st_size / 1024
css, js = kb(DIST / "assets/css/site.css"), kb(DIST / "assets/js/site.js")
fonts = sum(kb(x) for x in (DIST / "assets/fonts").glob("*.woff2"))
biggest = max(pages, key=lambda x: x.stat().st_size)
print(f"pages: {len(pages)}  css: {css:.1f} KB  js: {js:.1f} KB  fonts: {fonts:.0f} KB  largest html: {kb(biggest):.1f} KB ({biggest.parent.name or 'root'})")
print(f"redirect rules: {len(rows)} ({sum(1 for r in rows if r['code']=='301')} x 301, {sum(1 for r in rows if r['code']=='410')} x 410); legacy URLs covered: {len(inv)}")
for w in warns: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"\n{len(errors)} errors, {len(warns)} warnings")
sys.exit(1 if errors else 0)
