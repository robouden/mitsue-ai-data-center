#!/usr/bin/env python3
"""
Add or update header (version, date) and footer (page N of M) to Mitsue project PDFs.
Overlays text on existing pages without touching content, fonts, or layout.

Usage:
  python3 update_pdf_headers.py              # update all project PDFs
  python3 update_pdf_headers.py file.pdf     # update a single file
"""

import sys, re
from pathlib import Path
from datetime import date
import fitz  # pymupdf

FONT       = "Helvetica"
FONT_SIZE  = 8
MARGIN     = 36
LINE_COLOR = (0.4, 0.4, 0.4)
TEXT_COLOR = (0.0, 0.0, 0.0)
LINE_WIDTH = 0.5

HEADER_RE = re.compile(r'Version:\s*([\d.v]+)', re.IGNORECASE)


def read_version(md_path: Path) -> str:
    """Read version from the first line of the matching .md file."""
    if md_path.exists():
        first = md_path.read_text(encoding='utf-8').split('\n')[0]
        m = HEADER_RE.search(first)
        if m:
            return m.group(1).strip()
    return "v1.0"


def apply_envelope(pdf_path: Path):
    today = date.today().isoformat()
    md_path = pdf_path.with_suffix('.md')
    version = read_version(md_path)
    header_text = f"Version: {version}  |  Last modified: {today}"

    font = fitz.Font(FONT)
    doc = fitz.open(str(pdf_path))
    total = len(doc)

    for i, page in enumerate(doc):
        w = page.rect.width
        h = page.rect.height
        footer_text = f"Page {i + 1} of {total}"

        hw = font.text_length(header_text, fontsize=FONT_SIZE)
        fw = font.text_length(footer_text, fontsize=FONT_SIZE)

        # Header line + text
        page.draw_line(fitz.Point(MARGIN, 28), fitz.Point(w - MARGIN, 28),
                       color=LINE_COLOR, width=LINE_WIDTH)
        page.insert_text(fitz.Point(w - MARGIN - hw, 22), header_text,
                         fontname=FONT, fontsize=FONT_SIZE, color=TEXT_COLOR)

        # Footer line + text
        page.draw_line(fitz.Point(MARGIN, h - 22), fitz.Point(w - MARGIN, h - 22),
                       color=LINE_COLOR, width=LINE_WIDTH)
        page.insert_text(fitz.Point(w - MARGIN - fw, h - 12), footer_text,
                         fontname=FONT, fontsize=FONT_SIZE, color=TEXT_COLOR)

    tmp = pdf_path.with_suffix('.tmp.pdf')
    doc.save(str(tmp))
    doc.close()
    tmp.replace(pdf_path)
    print(f"  ✓ {pdf_path.name}  {version}  {today}  {total}p")


# ── Main ──────────────────────────────────────────────────────────────────────
base = Path(__file__).parent

if len(sys.argv) > 1:
    targets = [Path(a) for a in sys.argv[1:]]
else:
    targets = sorted(base.glob('*.pdf'))

for path in targets:
    if not path.is_absolute():
        path = base / path
    if path.exists():
        apply_envelope(path)
    else:
        print(f"  ~ {path.name} not found, skipping")
