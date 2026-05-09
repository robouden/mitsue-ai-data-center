# Skill: Document Headers & Footers

After editing any project `.md` file, run this to update the header and footer:

```bash
cd "/home/rob/Documents/Mitsue/Mitsue Village Project AI data center"
python3 update_doc_headers.py <filename.md>   # single file
python3 update_doc_headers.py                 # all 15 project docs
```

## What it does

- **First run:** adds `v1.0` + today's date + estimated page count
- **Subsequent runs:** increments minor version (`v1.0 → v1.1`), updates date and page count

## Markers used

The script uses HTML comment markers so it can find and replace existing blocks:

```
<!-- doc-header version=v1.0 date=2026-05-09 -->
> **Title** &nbsp;|&nbsp; **Version:** v1.0 &nbsp;|&nbsp; **Last modified:** 2026-05-09
---
<!-- /doc-header -->

<!-- doc-footer -->
---
> *v1.0 &nbsp;·&nbsp; Last modified: 2026-05-09 &nbsp;·&nbsp; ~4 pages*
<!-- /doc-footer -->
```

## Managed documents

The 15 project docs listed in `PROJECT_DOCS` inside `update_doc_headers.py`.
System/agent files (`AGENTS.md`, `OPENPROJECT.md`, `CLAUDE.md`, etc.) are intentionally excluded.
