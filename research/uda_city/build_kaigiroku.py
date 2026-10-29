#!/usr/bin/env python3
"""Add council minutes (kaigiroku/*.txt, from scrape_kaigiroku.py) to uda_city.duckdb: days, speeches, keyword hits. Re-runnable. Run AFTER build_db.py."""
import os,re,json,glob,duckdb,unicodedata,datetime
HERE=os.path.dirname(os.path.abspath(__file__)); KD=f"{HERE}/kaigiroku"
idx=json.load(open(f"{KD}/index.json")) if os.path.exists(f"{KD}/index.json") else {}
con=duckdb.connect(f"{HERE}/uda_city.duckdb")
for t in ("kaigiroku_days","kaigiroku_speeches","kaigiroku_hits"): con.execute(f"drop table if exists {t}")
con.execute("create table kaigiroku_days(file varchar primary key,meeting_date date,fiscal_year int,session varchar,label varchar,n_chars int,n_speeches int)")
con.execute("create table kaigiroku_speeches(file varchar,meeting_date date,session varchar,seq int,role varchar,speaker varchar,text varchar)")
con.execute("create table kaigiroku_hits(file varchar,meeting_date date,session varchar,seq int,role varchar,speaker varchar,keyword varchar,context varchar)")
KW=["森林組合","森林環境譲与税","施業放置林","林業","森林","木質バイオマス","バイオマス","木材","内牧","廃校","学校統合","公共施設","入札","データセンター","再生可能","発電","協力隊","ナラ枯れ","鳥獣","補助金","榛原東","室生","御杖","企業誘致","空き家"]
mark=re.compile(r'^○(.+?)[（(](.+?)(?:君|さん|氏)[）)]\s*$')
def dt(fn):
    m=re.match(r'([RH])(\d{2})(\d{2})(\d{2})',fn)
    e,y,mo,d=m.group(1),int(m.group(2)),int(m.group(3)),int(m.group(4))
    y=(2018 if e=="R" else 1988)+y
    return datetime.date(y,mo,d)
days=[];sp=[];hits=[]
for f in sorted(glob.glob(f"{KD}/*A.txt")):
    fn=os.path.basename(f)[:-4]; d=dt(fn); t=open(f,encoding="utf-8").read()
    fy=d.year if d.month>=4 else d.year-1
    cur=None; seq=0; rows=[]
    def flush():
        if cur: rows.append((cur[0],cur[1],"\n".join(cur[2]).strip()))
    for line in t.splitlines():
        m=mark.match(line.strip())
        if m: flush(); cur=(m.group(1).strip(),m.group(2).strip(),[])
        elif cur: cur[2].append(line.strip())
    flush()
    meta=idx.get(fn,{}); sess=meta.get("session","")
    days.append([fn,d,fy,sess,meta.get("label",""),len(t),len(rows)])
    for i,(role,name,body) in enumerate(rows,1):
        sp.append([fn,d,sess,i,role,name,body])
        s=unicodedata.normalize("NFKC",body)
        for k in KW:
            if k in s:
                j=s.index(k); hits.append([fn,d,sess,i,role,name,k,re.sub(r'\s+',' ',s[max(0,j-60):j+120])])
con.executemany("insert into kaigiroku_days values (?,?,?,?,?,?,?)",days)
con.executemany("insert into kaigiroku_speeches values (?,?,?,?,?,?,?)",sp)
con.executemany("insert into kaigiroku_hits values (?,?,?,?,?,?,?,?)",hits)
print(len(days),"days",len(sp),"speeches",len(hits),"hits")
