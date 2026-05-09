#!/usr/bin/env python3
"""
Add or update header (version, date) and footer (page count)
in Mitsue project markdown documents using simple right-aligned HTML.

Usage:
  python3 update_doc_headers.py              # update all project docs
  python3 update_doc_headers.py file.md      # update a single file
"""

import sys, re
from pathlib import Path
from datetime import date


PROJECT_DOCS = [
    "mitsue_founding_charter.md",
    "mitsue_implementation_plan.md",
    "mitsue_implementation_plan_jp.md",
    "mitsue_founder_agreement_template.md",
    "mitsue_letter_pellegrom_support_request.md",
    "mitsue_mayor_meeting_talking_points.md",
    "mitsue_phases_funding_flowchart.md",
    "mitsue_project_founding_story.md",
    "mitsue_project_founding_story_jp.md",
    "mitsue_project_overview_pellegrom.md",
    "mitsue_qa_briefing.md",
    "mitsue_stakeholders.md",
    "mitsue_stakeholders_jp.md",
    "mitsue_village_government_onepager.md",
    "mitsue_village_government_onepager_jp.md",
]

WORDS_PER_PAGE = 400

# Detect the right-aligned HTML header/footer lines (with or without spaces after colons)
HEADER_RE = re.compile(r'^<p align="right">Version:\s*([\d.v]+)[^\n]*</p>\n?', re.MULTILINE)
FOOTER_RE = re.compile(r'\n?<p align="right">Page \d+[^\n]*</p>\n?$')




def next_version(current: str) -> str:
    try:
        major, minor = current.strip().lstrip('v').split('.')
        return f"v{major}.{int(minor) + 1}"
    except Exception:
        return "v1.1"


def make_header(version: str, mod_date: str) -> str:
    return f'<p align="right">Version: {version} &nbsp;|&nbsp; Last modified: {mod_date}</p>\n'


def process(filepath: Path):
    text = filepath.read_text(encoding='utf-8')
    today = date.today().isoformat()

    m = HEADER_RE.search(text)
    has_header = bool(m)

    version = next_version(m.group(1)) if m else "v1.0"

    # Strip existing header and any leftover footer
    text = HEADER_RE.sub('', text, count=1)
    text = FOOTER_RE.sub('', text)
    text = text.strip()

    new_text = make_header(version, today) + "\n" + text + "\n"
    filepath.write_text(new_text, encoding='utf-8')

    action = "updated" if has_header else "added"
    print(f"  ✓ {filepath.name}  {version}  {today}  ({action})")


# ── Main ──────────────────────────────────────────────────────────────────────
base = Path(__file__).parent

if len(sys.argv) > 1:
    targets = [Path(a) for a in sys.argv[1:]]
else:
    targets = [base / doc for doc in PROJECT_DOCS]

for path in targets:
    if not path.is_absolute():
        path = base / path
    if path.exists():
        process(path)
    else:
        print(f"  ~ {path.name} not found, skipping")
