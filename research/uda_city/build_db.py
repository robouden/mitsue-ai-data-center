#!/usr/bin/env python3
"""Build uda_city.duckdb from inventory.json + pages/ + text/. Re-runnable."""
import json,os,re,html,duckdb,unicodedata
HERE=os.path.dirname(os.path.abspath(__file__))
BASE="https://www.city.uda.lg.jp"
inv=json.load(open(f"{HERE}/inventory.json"))
fn=lambda p: re.sub(r'[^A-Za-z0-9._-]','_',p.strip('/'))
def fy(s):
    s=unicodedata.normalize("NFKC",s or "")
    m=re.search(r'令和\s*(\d+|元)\s*年度',s)
    if m: return 2018+(1 if m.group(1)=="元" else int(m.group(1)))
    m=re.search(r'平成\s*(\d+)\s*年度',s)
    if m: return 1988+int(m.group(1))
    m=re.search(r'R\s*(\d+)年度',s)
    return 2018+int(m.group(1)) if m else None
KW=["森林環境譲与税","森林組合","施業放置林","境界明確化","林業","森林","木質バイオマス","バイオマス","木材","内牧","廃校","公共施設","入札","契約","補助金","協力隊","データセンター","再生可能","発電","財産","榛原","室生","御杖","御杖村"]
if os.path.exists(f"{HERE}/uda_city.duckdb"): os.remove(f"{HERE}/uda_city.duckdb")
con=duckdb.connect(f"{HERE}/uda_city.duckdb")
con.execute("create table pages(path varchar primary key,url varchar,title varchar,section varchar,depth int,text varchar)")
con.execute("""create table documents(path varchar primary key,url varchar,filename varchar,ext varchar,bytes bigint,source_page varchar,source_title varchar,
  doc_title varchar,fiscal_year int,n_pages int,n_chars int,text_extracted boolean,text varchar)""")
con.execute("create table doc_pages(path varchar,page int,text varchar)")
con.execute("create table keyword_hits(path varchar,source_title varchar,fiscal_year int,page int,line_no int,keyword varchar,context varchar)")
titles={p:v.get("title","") for p,v in inv["pages"].items()}
for p,v in inv["pages"].items():
    f=f"{HERE}/pages/{fn(p) or 'index'}.html"
    if not os.path.exists(f): continue
    t=open(f,encoding="utf-8",errors="ignore").read()
    t=re.sub(r'(?is)<(script|style|noscript|header|nav|footer)[^>]*>.*?</\1>',' ',t)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'[ \t　]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t).strip()
    title=v.get("title",""); sect=title.split(" - ")[-2] if title.count(" - ")>=2 else (title.split(" - ")[-1] if " - " in title else "")
    con.execute("insert into pages values (?,?,?,?,?,?)",[p,BASE+p,title,sect,v.get("depth"),t])
docs=[];hits=[];dp=[]
for path,src in inv["atts"].items():
    f=f"{HERE}/files/{fn(path)}"; tx=f"{HERE}/text/{fn(path)}.txt"
    raw=open(tx,encoding="utf-8",errors="ignore").read() if os.path.exists(tx) else ""
    ext=path.rsplit('.',1)[-1].lower()
    pgs=raw.split("\f") if ext=="pdf" else [raw]
    if pgs and not pgs[-1].strip(): pgs=pgs[:-1]
    first=next((l.strip() for l in raw.splitlines() if l.strip()),"")[:120]
    st=titles.get(src,"")
    y=fy(first) or fy(os.path.basename(path)) or fy(st) or fy(raw[:600])
    docs.append([path,BASE+path,os.path.basename(path),ext,os.path.getsize(f) if os.path.exists(f) else None,src,st,first,y,len(pgs),len(raw),bool(raw.strip()),raw])
    for i,pg in enumerate(pgs,1):
        dp.append([path,i,pg])
        for ln,line in enumerate(pg.splitlines(),1):
            s=unicodedata.normalize("NFKC",line)
            for k in KW:
                if k in s:
                    hits.append([path,st,y,i,ln,k,re.sub(r'\s+',' ',line).strip()[:300]])
con.executemany("insert into documents values (?,?,?,?,?,?,?,?,?,?,?,?,?)",docs)
con.executemany("insert into doc_pages values (?,?,?)",dp)
con.executemany("insert into keyword_hits values (?,?,?,?,?,?,?)",hits)
con.execute("create view v_forestry_docs as select * from documents where source_title ~ '(林業|森林|農林)' or text like '%森林組合%' or text like '%森林環境譲与税%'")
for t in ["pages","documents","doc_pages","keyword_hits"]: print(t,con.execute(f"select count(*) from {t}").fetchone()[0])
print(con.execute("select count(*) from documents where not text_extracted").fetchone())
