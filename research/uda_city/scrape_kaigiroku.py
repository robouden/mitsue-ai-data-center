#!/usr/bin/env python3
"""Scrape Uda City council minutes (会議録) from https://www.kensakusystem.jp/uda/ . Resumable, polite (0.5s).
Writes kaigiroku/<fileName>.txt (full text of each meeting day) and kaigiroku/index.json."""
import urllib.request,urllib.parse,http.cookiejar,re,time,html,json,os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); OUT=f"{HERE}/kaigiroku"; os.makedirs(OUT,exist_ok=True)
B="https://www.kensakusystem.jp"; CODE="0qtnybv42thvl8a0j3"
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders=[("User-Agent","Mitsue-research/1.0 (contact rob@mitsue.it)")]
def req(url,fields=None,tries=3):
    for i in range(tries):
        try:
            time.sleep(0.5)
            d=urllib.parse.urlencode(fields,encoding="shift_jis").encode() if fields else None
            return op.open(B+url,d,timeout=60).read().decode("shift_jis","ignore")
        except Exception as e:
            if i==tries-1: raise
            time.sleep(3)
def txt(h): return re.sub(r'[ \t　]+',' ',re.sub(r'\n\s*\n+','\n',html.unescape(re.sub(r'<[^>]+>','\n',h)))).strip()
tabs=[f"令和 {n}年" for n in range(8,1,-1)]+["令和 元年","令和元年","平成31年","平成30年","平成29年","平成28年","平成27年"]
idx={}
for tab in tabs:
    h=req("/uda/cgi-bin3/See.exe",{"Code":CODE,"treedepth":tab,"page":"","fileName":""})
    sessions=[s for s in re.findall(r"treedepth\.value='([^']*回[^']*)'",h)]
    for s in dict.fromkeys(sessions):
        h2=req("/uda/cgi-bin3/See.exe",{"Code":CODE,"treedepth":s,"page":"","fileName":""})
        for fn,label in re.findall(r'ResultFrame\.exe\?Code=\w+&fileName=(\w+)&startPos=0">\s*(?:<[^>]*>)*\s*([^<]*)',h2):
            if fn in idx: continue
            idx[fn]={"session":s.strip(),"label":label.strip()}
print(len(idx),"meeting days found",flush=True)
for n,(fn,v) in enumerate(sorted(idx.items()),1):
    out=f"{OUT}/{fn}.txt"
    if os.path.exists(out) and os.path.getsize(out)>500: continue
    try:
        t=req(f"/uda/cgi-bin3/GetText3.exe?{CODE}/{fn}/0/10/1/PRINT_ALL/0/0")
        open(out,"w",encoding="utf-8").write(txt(t))
    except Exception as e: print("ERR",fn,e,flush=True)
    if n%25==0: print(n,fn,flush=True)
json.dump(idx,open(f"{OUT}/index.json","w"),ensure_ascii=False,indent=1)
print("done")
