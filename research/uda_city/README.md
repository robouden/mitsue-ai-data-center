<!-- File: README.md | Version: v1.1 | Last modified: 2026-10-29 -->
# Uda City (宇陀市) forestry / finance / council research DB

Source: https://www.city.uda.lg.jp (forestry 林業, bidding 入札, budget/settlement 予算・決算, council 市議会, audit 監査, 農林課, 財政課). Crawled 2026-10-29, 0.3-0.4s delay, identifiable User-Agent, no robots.txt present.

## Files
- `uda_city.duckdb` — the database (gitignored, rebuild with the scripts).
- `inventory.json` — crawl result: 200 pages, 1,157 attachments (1,097 PDF, 19 docx, 19 doc, 14 xlsx, 8 xls).
- `fetch_extract.py` — download pages + attachments, extract text (pdftotext -layout; docx via pandoc; xlsx via openpyxl). Resumable.
- `build_db.py` — builds the DB. `search.py` — quick search helper.
- `files/`, `text/`, `pages/` — raw downloads (gitignored, ~830 MB).

## Tables
- `pages(path,url,title,section,depth,text)` — 200 HTML pages.
- `documents(path,url,filename,ext,bytes,source_page,source_title,doc_title,fiscal_year,n_pages,n_chars,text_extracted,text)` — 1,157 attachments. `fiscal_year` is parsed from the document (令和/平成年度) and can be NULL (258) or a planning horizon (2034/2035).
- `doc_pages(path,page,text)` — per-PDF-page text (14,105 pages).
- `keyword_hits(path,source_title,fiscal_year,page,line_no,keyword,context)` — 20,545 lines matching 24 keywords (森林環境譲与税, 森林組合, 施業放置林, 境界明確化, 林業, 森林, バイオマス, 木材, 内牧, 廃校, 公共施設, 入札, 契約, 補助金, 協力隊, データセンター, 再生可能, 発電, 財産, 榛原, 室生, 御杖…).
- View `v_forestry_docs`.

## Usage
```bash
python3 search.py 森林環境譲与税 --fy 2024 --limit 10
python3 search.py 廃校 --docs
python3 -c "import duckdb;c=duckdb.connect('uda_city.duckdb',read_only=True);print(c.execute(\"select keyword,count(*) from keyword_hits group by 1 order by 2 desc\").fetchall())"
```

## Limitations
- 96 documents have no extracted text: 69 PDFs (probably scanned images; OCR not run), 19 .doc and 8 .xls (not converted).
- Council minutes are in the `kaigiroku_*` tables (phase 2, see below). Pages/attachments from the city site have only 審議結果, 議会日程, 一般質問通告一覧 and 議会だより.
- Crawl depth 2 from the seed pages; later years' sub-pages may exist beyond it.
- Japanese text from multi-column PDFs (議会だより) is interleaved, so lines can mix articles.

## Phase 2: council minutes (会議録), added 2026-10-29
Source: https://www.kensakusystem.jp/uda/ (POST-form tree; full text via `GetText3.exe?...&PRINT_ALL`). Scraped with `scrape_kaigiroku.py` (0.5s delay, resumable) into `kaigiroku/*.txt`; loaded with `build_kaigiroku.py` (run after `build_db.py`).
- Coverage: **255 meeting days, H27 (2015) to R8 (2026-06-23)**, 13 years of 定例会/臨時会.
- `kaigiroku_days(file,meeting_date,fiscal_year,session,label,n_chars,n_speeches)`
- `kaigiroku_speeches(file,meeting_date,session,seq,role,speaker,text)` — 57,165 speeches, split on the ○役職（氏名君）markers.
- `kaigiroku_hits(file,meeting_date,session,seq,role,speaker,keyword,context)` — 4,489 keyword hits (25 keywords incl. 森林組合, 林業, 木質バイオマス, 内牧, 廃校, 学校統合, 企業誘致, データセンター, 発電, 空き家).
- Not included: committee minutes (委員会) — the system only publishes plenary 定例会・臨時会.
- Speaker names come from the minutes; some are shown with a truncated given name (e.g. 上田 ｺ) because of font/character issues in the source.

### Notable findings (2026-10-29)
- 2024-03-22: councillor 上田 states the 内牧小学校 site (closed 2006) was leased **free of charge** to 宇陀市森林組合 as its forestry base; city 農林商工部長 東 says the city will cooperate if the Uda and Muro coops decide to restructure. Forest area 18,273 ha (13,931 ha plantation); >half of owners hold <5 ha.
- 2021-06-21: councillor 八木 勝光 (still sitting 2026, vice-chair) asked for woody-biomass power in Uda; dept head: ~2,400 m3/yr of Uda wood already goes to a biomass plant; mayor 金剛 一智: merits, but haul/transport costs.
- 2024-03-22: city plan to attract Estonian firms (Cleveron factory and **data centers**) was raised by 上田.
- 2026-06-23: Haibara elementary school consolidation (3 → 1) debated; reuse of closed school sites "not yet decided" (教育委員会事務局長 鈴木).
