#!/usr/bin/env python3
"""Crawl Uda City /soshiki/ (org tree: 部課, 担当業務, 連絡先) + 市長/議会/審議会 pages. Polite, resumable."""
import re,os,sys,time,json,html,urllib.request,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=f"{HERE}/org"; BASE="https://www.city.uda.lg.jp"
UA="Mozilla/5.0 (compatible; MitsueResearch/1.0; contact rob@mitsue.it)"
SEEDS=["/soshiki/","/soshiki/list.html"]
PRE=("/soshiki/",)
seen=set(); q=[(s,0) for s in SEEDS]; idx={}
def get(u):
    r=urllib.request.Request(BASE+u,headers={"User-Agent":UA})
    with urllib.request.urlopen(r,timeout=40) as f: return f.read().decode("utf-8","ignore")
def txt(h):
    h=re.sub(r'(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>','',h)
    h=re.sub(r'(?i)<br\s*/?>|</(p|div|li|tr|h\d|dd|dt)>','\n',h); h=re.sub(r'(?s)<[^>]+>','',h)
    return re.sub(r'\n\s*\n+','\n',html.unescape(h)).strip()
while q:
    u,d=q.pop(0)
    if u in seen or d>5: continue
    seen.add(u)
    try: h=get(u)
    except Exception as e: print("err",u,e); continue
    t=re.search(r'<title>(.*?)</title>',h,re.S); title=html.unescape(t.group(1)).strip() if t else ""
    fn=re.sub(r'[^A-Za-z0-9._-]','_',u.strip('/')) or 'index'
    open(f"{OUT}/{fn}.txt","w").write(f"URL: {BASE}{u}\nTITLE: {title}\n\n{txt(h)}\n")
    idx[u]=title
    for l in re.findall(r'href="([^"#]+)"',h):
        l=urllib.parse.urljoin(BASE+u,l)
        if not l.startswith(BASE): continue
        p=l[len(BASE):].split('?')[0]
        if p.startswith(PRE) and p.endswith(('/','.html')) and p not in seen: q.append((p,d+1))
    time.sleep(0.4)
json.dump(idx,open(f"{OUT}/_index.json","w"),ensure_ascii=False,indent=1)
print("pages",len(idx))
