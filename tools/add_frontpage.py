#!/usr/bin/env python3
import re, os, sys

DOCS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root (script in tools/)

def _resolve(filename):
    """Docs moved into docs/<theme>/ — find by basename if not at repo root."""
    direct = os.path.join(DOCS_DIR, filename)
    if os.path.exists(direct):
        return direct
    for root, _dirs, files in os.walk(os.path.join(DOCS_DIR, 'docs')):
        if filename in files:
            return os.path.join(root, filename)
    return direct

TARGETS = [
    "mitsue_business_case.md", "mitsue_business_case_jp.md",
    "mitsue_evm_plan.md", "mitsue_evm_plan_jp.md",
    "mitsue_founder_agreement_template.md",
    "mitsue_founding_charter.md",
    "mitsue_implementation_plan_jp.md",
    "mitsue_introduction_a4.md", "mitsue_introduction_a4_jp.md",
    "mitsue_phases_funding_flowchart.md", "mitsue_phases_funding_flowchart_jp.md",
    "mitsue_project_founding_story.md", "mitsue_project_founding_story_jp.md",
    "mitsue_project_overview_pellegrom.md",
    "mitsue_qa_briefing.md",
    "mitsue_quantum_mesh_outreach.md", "mitsue_quantum_mesh_outreach_jp.md",
    "Mitsue_Research_Brief.md", "Mitsue_Research_Brief_jp.md",
    "mitsue_revenue_model.md", "mitsue_revenue_model_jp.md",
    "mitsue_stakeholders.md", "mitsue_stakeholders_jp.md",
    "mitsue_village_government_onepager.md", "mitsue_village_government_onepager_jp.md",
    "mitsue_village_re_plan_alignment.md", "mitsue_village_re_plan_alignment_jp.md",
    "mitsue_wbs.md", "mitsue_wbs_jp.md",
]

FRONTPAGE_MARKER = "PROJECT DOCUMENT"

def extract_meta(content):
    # Version and date from header line
    m = re.search(r'Version:\s*(v[\d.]+).*?Last modified:\s*([\d-]+)', content)
    version = m.group(1) if m else "v1.0"
    date = m.group(2) if m else "2026-06-14"
    return version, date

def extract_subtitle(content, filename):
    # Find first H1
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if not m:
        return os.path.splitext(filename)[0].replace('_', ' ').title()
    title = m.group(1).strip()
    # Strip common prefixes like "Mitsue Project —" or "御杖村"
    title = re.sub(r'^Mitsue Project\s*[—–-]\s*', '', title)
    title = re.sub(r'^御杖村[：:]\s*', '', title)
    title = re.sub(r'^Mitsue Village.*?[—–-]\s*', '', title)
    return title.strip()

def strip_style_block(content):
    # Remove leading <style>...</style> blocks
    return re.sub(r'^\s*<style>.*?</style>\s*', '', content, flags=re.DOTALL)

def build_frontpage(filename, version, date, subtitle):
    return f"""<p align="right">{filename} &nbsp;|&nbsp; Version: {version} &nbsp;|&nbsp; Last modified: {date}</p>

---

<div align="center">

PROJECT DOCUMENT

# Mitsue Village AI Data Center

*{subtitle}*

<img src="assets/logo_go.png" alt="御" width="75%" style="display:block;margin:0 auto;">

</div>

---

| | |
|---|---|
| **Version** | {version} |
| **Date** | {date} |
| **Author** | Rob Oudendijk |

---

"""

for filename in TARGETS:
    path = _resolve(filename)
    if not os.path.exists(path):
        print(f"SKIP (not found): {filename}")
        continue

    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    if FRONTPAGE_MARKER in original:
        print(f"SKIP (already has frontpage): {filename}")
        continue

    content = strip_style_block(original)
    version, date = extract_meta(content)
    subtitle = extract_subtitle(content, filename)
    frontpage = build_frontpage(filename, version, date, subtitle)

    # Strip existing version header line so it doesn't duplicate
    content = re.sub(r'<p align="right">Version:.*?</p>\s*\n?', '', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(frontpage + content.lstrip())

    print(f"OK: {filename}  [{version} | {date}]  subtitle: {subtitle}")
