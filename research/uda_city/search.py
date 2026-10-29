#!/usr/bin/env python3
"""Search the Uda City DB.  Usage: search.py 'keyword' [--fy 2024] [--limit 20] [--docs]
Prints matching lines (document, fiscal year, page, context). --docs lists documents instead."""
import sys,os,re,argparse,duckdb,unicodedata
ap=argparse.ArgumentParser(); ap.add_argument("q"); ap.add_argument("--fy",type=int); ap.add_argument("--limit",type=int,default=20); ap.add_argument("--docs",action="store_true")
a=ap.parse_args()
c=duckdb.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),"uda_city.duckdb"),read_only=True)
fy=" and fiscal_year=?" if a.fy else ""; args=[f"%{a.q}%"]+([a.fy] if a.fy else [])
if a.docs:
    for r in c.execute(f"select fiscal_year,source_title,doc_title,url from documents where text like ?{fy} order by fiscal_year desc nulls last limit {a.limit}",args).fetchall():
        print(r[0],"|",(r[1] or "")[:40],"|",(r[2] or "")[:50],"|",r[3])
else:
    for p,y,pg,t,u in c.execute(f"select d.path,d.fiscal_year,p.page,p.text,d.url from doc_pages p join documents d using(path) where p.text like ?{fy.replace('fiscal_year','d.fiscal_year')} limit {a.limit}",args).fetchall():
        for line in t.splitlines():
            if a.q in line:
                print(f"[{y}] p{pg} {re.sub(chr(32)+'+',' ',line).strip()[:160]}\n     {u}"); break
