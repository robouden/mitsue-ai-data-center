#!/usr/bin/env python3
"""Download Uda City pages + attachments listed in inventory.json, extract text. Resumable. Polite (0.3s)."""
import json,os,re,sys,time,html,subprocess,hashlib,urllib.request,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__))
BASE="https://www.city.uda.lg.jp"
UA="Mozilla/5.0 (compatible; MitsueResearch/1.0; contact rob@mitsue.it)"
inv=json.load(open(f"{HERE}/inventory.json"))
def get(u):
    req=urllib.request.Request(u,headers={"User-Agent":UA})
    with urllib.request.urlopen(req,timeout=60) as r: return r.read()
def fn(path): return re.sub(r'[^A-Za-z0-9._-]','_',path.strip('/'))
# pages
for p,v in inv["pages"].items():
    out=f"{HERE}/pages/{fn(p) or 'index'}.html"
    if os.path.exists(out) or "err" in v: continue
    try: open(out,"wb").write(get(BASE+p))
    except Exception as e: print("page err",p,e)
    time.sleep(0.3)
# attachments
n=0
for path,src in inv["atts"].items():
    out=f"{HERE}/files/{fn(path)}"
    if not os.path.exists(out):
        try: open(out,"wb").write(get(BASE+urllib.parse.quote(path)))
        except Exception as e: print("att err",path,e); continue
        time.sleep(0.3); n+=1
        if n%50==0: print("downloaded",n,flush=True)
    txt=f"{HERE}/text/{fn(path)}.txt"
    if os.path.exists(txt): continue
    ext=path.rsplit('.',1)[-1].lower()
    try:
        if ext=="pdf": subprocess.run(["pdftotext","-layout",out,txt],timeout=120,check=True)
        elif ext=="docx": subprocess.run(["pandoc","-t","plain",out,"-o",txt],timeout=60,check=True)
        elif ext=="xlsx":
            import openpyxl
            wb=openpyxl.load_workbook(out,read_only=True,data_only=True); L=[]
            for ws in wb: 
                L.append(f"## {ws.title}")
                for row in ws.iter_rows(values_only=True):
                    if any(c is not None for c in row): L.append("\t".join("" if c is None else str(c) for c in row))
            open(txt,"w").write("\n".join(L))
        else: open(txt,"w").write("")  # .doc/.xls not extracted
    except Exception as e: print("extract err",path,e); open(txt,"w").write("")
print("done")
