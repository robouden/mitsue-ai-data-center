<!-- File: README.md | Version: v1.0 | Last modified: 2026-08-20 -->
# Inochi Forum — Action Plans Reference Database

Source: `Action Plans.pdf` ("Action Plans to Realize the *Inochi* Declaration", *Inochi* Forum, Oct 11, 2025), originally in `~/Downloads/Action.pdf` / `Action Plans.pdf`. Copied here at `pdf/Action Plans.pdf`.

103 draft action plans (135 contributors), organized into 5 perspectives ("Feel", "Protect", "Nurture", "Bond", "Understand" *Inochi*) and 22 numbered Declarations (1-1 … 5-4). Each plan cites a real-world initiative, org, references/URLs, an "Action Platform" tag, and SDG alignment.

Not written for the Mitsue project, but kept as a general reference library — precedents on community/forest/energy ethics, art-for-cause framing, disability & inclusion design, and funding/partnership models that may be useful to cite or borrow language from.

## Files

- `inochi_action_plans.duckdb` — DuckDB database, tables below, with a full-text search (FTS) index on `pages.text`.
- `pages.csv`, `sections.csv`, `declarations.csv`, `items.csv`, `urls.csv` — source CSVs loaded into the db (kept for re-import if needed).
- `text/page_NNN.txt` — raw per-page extracted text (149 files; `pdftotext -raw`).
- `pdf/Action Plans.pdf` — original source PDF.

## DB schema

- `pages(page INT, text VARCHAR)` — full text per PDF page, with FTS index.
- `sections(num, name, first_page)` — the 5 top-level perspectives.
- `declarations(code, section, title, first_page)` — the 22 Declarations (e.g. `4-6`).
- `items(id, section, declaration, first_page, title)` — the 103 numbered action items (e.g. `4-6-2`). `title` is the item's bold statement (sometimes with a trailing image caption picked up by the text layer — noise, not corruption of the statement itself).
- `urls(page, near_item, url)` — every URL found in the doc with the item it was nearest to (312 total; approximate association since some page layouts interleave columns).

## Caveats

The source PDF uses a floating-text-frame layout (captions, reference boxes, pull-quotes as separate objects). `pdftotext` reading order mostly tracks the two-column body text correctly, but item boundaries can bleed 1 item forward/back and reference/SDG blocks aren't reliably separable from body text — so there's no clean per-item `body`/`references`/`sdgs` split in this DB. For anything you plan to quote verbatim, verify against `text/page_NNN.txt` or the PDF page image.

## Example queries

```sql
-- Full-text search
LOAD fts;
SELECT page, score, substr(text,1,150) AS snippet
FROM (SELECT *, fts_main_pages.match_bm25(page, 'forest biomass renewable energy') AS score FROM pages)
WHERE score IS NOT NULL ORDER BY score DESC LIMIT 10;

-- Browse an item and jump to its page
SELECT * FROM items WHERE id = '4-6-2';
SELECT text FROM pages WHERE page = (SELECT first_page FROM items WHERE id = '4-6-2');

-- All URLs cited near a given item
SELECT * FROM urls WHERE near_item = '4-6-2';
```

CLI: `duckdb "research/inochi_action_plans/inochi_action_plans.duckdb"`

Built 2026-07-11.
