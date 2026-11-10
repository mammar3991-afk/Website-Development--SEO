import re,csv,urllib.request,urllib.parse,urllib.error,html,time,sys
B="https://octavebytes.com"
UA={"User-Agent":"Mozilla/5.0 (baseline crawl)"}
import subprocess
def get(u):
    try:
        o=subprocess.run(["curl","-sL","-m","12","-A",UA["User-Agent"],"-w","\n%{http_code} %{url_effective}",u],capture_output=True,text=True).stdout
        body,last=o.rsplit("\n",1);code,fin=last.split(" ",1)
        return int(code),body,fin
    except Exception: return 0,"",u
seeds=["/","/sitemap_index.xml","/sitemap.xml","/wp-sitemap.xml"]
urls=set();q=["/"]
# sitemaps
for s in seeds[1:]:
    st,h,_=get(B+s)
    if st==200:
        for loc in re.findall(r"<loc>([^<]+)</loc>",h):
            if loc.endswith(".xml"):
                st2,h2,_=get(loc)
                for l2 in re.findall(r"<loc>([^<]+)</loc>",h2): q.append(urllib.parse.urlparse(l2).path or "/")
            else: q.append(urllib.parse.urlparse(loc).path or "/")
# GSC pages too
for r in csv.DictReader(open("gsc/Pages.csv")): q.append(urllib.parse.urlparse(r["Top pages"]).path or "/")
rows={}
while q:
    p=q.pop()
    if len(rows)>=250: break
    if p in rows or p.startswith("/wp-") and not p.startswith("/wp-content/uploads"): continue
    if re.search(r"\.(png|jpe?g|gif|svg|webp|css|js|pdf|ico|woff2?)$",p,re.I): continue
    st,h,fin=get(B+p)
    t=re.search(r"<title[^>]*>(.*?)</title>",h,re.S);h1=re.findall(r"<h1[^>]*>(.*?)</h1>",h,re.S)
    clean=lambda s:re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>","",s))).strip()
    md=re.search(r'<meta name="description" content="([^"]*)"',h)
    can=re.search(r'<link rel="canonical" href="([^"]*)"',h)
    robots=re.search(r'<meta name="robots" content="([^"]*)"',h)
    words=len(clean(re.sub(r"<(script|style)[^>]*>.*?</\1>","",h,flags=re.S)).split())
    comments=len(re.findall(r'id="comment-\d+"',h))
    rows[p]=[p,st,fin.replace(B,""),clean(t.group(1)) if t else "",clean(h1[0]) if h1 else "",len(h1),clean(md.group(1)) if md else "",can.group(1) if can else "",robots.group(1)[:40] if robots else "",words,comments]
    if st==200:
        for l in re.findall(r'href="([^"#?]*)',h):
            l=urllib.parse.urljoin(B+p,l)
            if l.startswith(B) and not l.startswith(B+"/wp-"):
                lp=urllib.parse.urlparse(l).path or "/"
                if lp not in rows: q.append(lp)
    print(len(rows),p,st,flush=True)
with open("old-site-crawl.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(["path","status","final_path","title","h1","h1_count","meta_description","canonical","robots","words","comments_on_page"])
    for p in sorted(rows): w.writerow(rows[p])
print(len(rows),"urls")
