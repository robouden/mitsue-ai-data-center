#!/usr/bin/env python3
"""Replace old front pages with new HTML design across all project docs."""
import re, os

DOCS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root (script in tools/)

SKIP_FILES = {
    'mitsue_frontpage.md', 'mitsue_implementation_plan.md',
    'AGENTS.md', 'HEARTBEAT.md', 'IDENTITY.md', 'OPENPROJECT.md',
    'PDF_CONVERSION_GUIDE.md', 'README.md', 'README_jp.md',
    'README_daily_reporting.md', 'SOUL.md', 'TOOLS.md', 'USER.md',
}
SKIP_DIRS  = {'memory', 'chat-exports', 'skills', 'node_modules', '.git'}
SKIP_SUBDIR_FILES = {
    # poems / cards / gifts
    'kaya_seed_poem.md', 'kaya_seed_poem-2.md', 'mayor-meeting-card.md',
    # fairytales
    'tsuemi_hime_and_the_seven_dwarfs.md', 'Fairy Tale Two-Page Summary.md',
    'つえみ姫と七人の森の精.md', 'つえみ姫と七人の森の精_2ページ要約.md',
    # internal notes / chat fragments
    'Meeting attendance group of 1 june..md',
    'This powerful triad—forest restoration, distributed energy, and community-owned data centers—is a highly innovative mode.md',
}

def logo_path(file_path):
    return os.path.relpath(
        os.path.join(DOCS_DIR, 'assets', 'logo_go.png'),
        os.path.dirname(file_path)
    )

def build_frontpage(subtitle, version, date, logo):
    return f"""<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;">
<p style="font-size:7.5pt; font-weight:600; letter-spacing:0.25em; color:#3a7a5a; margin:0 0 4mm;">PROJECT DOCUMENT</p>
<h1 style="font-size:28pt; font-weight:700; margin:0 0 2mm; border-bottom:1px solid #eee; padding-bottom:2mm;">Mitsue Project</h1>
<p style="font-style:italic; color:#666; margin:2mm 0 8mm;">{subtitle}</p>
<img src="{logo}" alt="御" width="50%" style="display:block;margin:0 auto;">
<div style="height:105mm;"></div>
<table style="width:100%; border-collapse:collapse; font-size:9pt;">
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold; width:30%;">Version</td><td style="padding:3mm 4mm; border:1px solid #ccc;">{version}</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Date</td><td style="padding:3mm 4mm; border:1px solid #ccc;">{date}</td></tr>
<tr><td style="padding:3mm 4mm; border:1px solid #ccc; font-weight:bold;">Author</td><td style="padding:3mm 4mm; border:1px solid #ccc;">Rob Oudendijk</td></tr>
</table>
</div>

<div style="page-break-after:always; break-after:page; height:0; margin:0; padding:0;"></div>

"""

def strip_title_prefix(text):
    """Remove 'Mitsue Project — ' / '御杖プロジェクト — ' prefix from first H1."""
    return re.sub(
        r'^(# )(?:Mitsue (?:Project|Village[^—\n]*)[—–\-]\s*|御杖プロジェクト\s*[—–\-]\s*)',
        r'\1', text, count=1, flags=re.MULTILINE
    )

def extract_subtitle_from_old(content):
    m = re.search(r'<p style="font-style:italic[^>]*>([^<]+)</p>', content)
    if m: return m.group(1).strip()
    m = re.search(r'\*([^*\n]+)\*', content[:600])
    return m.group(1).strip() if m else ''

def extract_meta(text):
    vm = re.search(r'Version:\s*(v[\d.]+)', text) or re.search(r'["\'> ](v\d+\.\d+[\d.]*)[<"\' ]', text)
    dm = re.search(r'Last modified:\s*([\d-]+)', text) or re.search(r'["\'> ](\d{4}-\d{2}-\d{2})[<"\' ]', text)
    version = vm.group(1) if vm else 'v1.0'
    date    = dm.group(1) if dm else '2026-06-14'
    return version, date

def extract_h1(text):
    m = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
    if not m: return ''
    title = m.group(1).strip()
    title = re.sub(r'^(?:Mitsue (?:Project|Village[^—\n]*)[—–\-]\s*|御杖プロジェクト\s*[—–\-]\s*)', '', title)
    title = re.sub(r'\*\*', '', title)
    return title.strip()

def process_old_frontpage(path, content):
    """Replace old markdown-based front page."""
    subtitle = extract_subtitle_from_old(content)
    version, date = extract_meta(content)

    # Body starts after:  | Rob Oudendijk |  \n\n---\n\n
    end = re.search(r'\| Rob Oudendijk \|\s*\n\n---\n\n', content)
    if not end:
        # fallback: after last --- that follows the table
        end = re.search(r'\*\*Author\*\*.*?Rob Oudendijk.*?\n\n---\n\n', content, re.DOTALL)
    if not end:
        print(f"  WARN: can't find old front page end — skipping")
        return

    body = strip_title_prefix(content[end.end():])
    new = build_frontpage(subtitle, version, date, logo_path(path)) + body
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)
    print(f"  UPDATED (old→new): subtitle={subtitle!r}  {version} | {date}")

def process_no_frontpage(path, content):
    """Add brand-new front page to a doc that has none."""
    # Strip leading <style> block if present
    content = re.sub(r'^\s*<style>.*?</style>\s*', '', content, flags=re.DOTALL)
    # Strip old <p align="right"> version header
    content = re.sub(r'<p align="right">Version:.*?</p>\s*\n?', '', content)
    version, date = extract_meta(content)
    subtitle = extract_h1(content)
    if not subtitle:
        print(f"  SKIP (no title found)")
        return
    body = strip_title_prefix(content.lstrip())
    new = build_frontpage(subtitle, version, date, logo_path(path)) + body
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)
    print(f"  ADDED: subtitle={subtitle!r}  {version} | {date}")

def should_skip(path):
    fname = os.path.basename(path)
    if fname in SKIP_FILES: return True
    if fname in SKIP_SUBDIR_FILES: return True
    if fname.startswith('SONNET_TASK'): return True
    if fname.startswith('convert_'): return True
    if fname.startswith('update_') or fname.startswith('add_'): return True
    return False

def find_files():
    results = []
    for root, dirs, files in os.walk(DOCS_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for fname in sorted(files):
            if not fname.endswith('.md'): continue
            fp = os.path.join(root, fname)
            if not should_skip(fp):
                results.append(fp)
    return results

files = find_files()
print(f"Scanning {len(files)} files...\n")
for path in files:
    rel = os.path.relpath(path, DOCS_DIR)
    print(f"{rel}")
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.startswith('<div style="font-family:-apple-system'):
        print(f"  SKIP (already new format)")
    elif 'PROJECT DOCUMENT' in content and ('<div align="center">' in content or '| **Author** | Rob Oudendijk |' in content):
        process_old_frontpage(path, content)
    else:
        process_no_frontpage(path, content)

print("\nDone.")
