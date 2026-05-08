#!/bin/bash
# Regenerates PDFs for all Mitsue project documents.
# Header: title (left) + last modified date (right)
# Footer: Page X of Y (centered)

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

HEADER_TEX="$SCRIPT_DIR/pandoc_header.tex"

# Project documents to convert (skip system/agent files)
DOCS=(
  mitsue_founding_charter.md
  mitsue_implementation_plan.md
  mitsue_implementation_plan_jp.md
  mitsue_founder_agreement_template.md
  mitsue_letter_pellegrom_support_request.md
  mitsue_mayor_meeting_talking_points.md
  mitsue_phases_funding_flowchart.md
  mitsue_project_founding_story.md
  mitsue_project_founding_story_jp.md
  mitsue_project_overview_pellegrom.md
  mitsue_qa_briefing.md
  mitsue_stakeholders.md
  mitsue_stakeholders_jp.md
  mitsue_village_government_onepager.md
  mitsue_village_government_onepager_jp.md
)

ok=0
err=0

for MD in "${DOCS[@]}"; do
  if [ ! -f "$MD" ]; then
    echo "  ~ Skipping $MD (not found)"
    continue
  fi

  PDF="${MD%.md}.pdf"

  # Last modified date: prefer git log, fall back to file mtime
  GIT_DATE=$(git log -1 --format="%ai" -- "$MD" 2>/dev/null | cut -c1-10)
  MOD_DATE="${GIT_DATE:-$(date -r "$MD" '+%Y-%m-%d')}"

  # Detect Japanese documents (filename contains _jp or has CJK content)
  if echo "$MD" | grep -q "_jp"; then
    FONT_ARGS="-V mainfont='Noto Sans CJK JP' -V CJKmainfont='Noto Sans CJK JP'"
  else
    FONT_ARGS="-V mainfont='Liberation Serif'"
  fi

  echo -n "  → $MD  ($MOD_DATE) ... "

  if pandoc "$MD" \
    --pdf-engine=xelatex \
    --include-in-header="$HEADER_TEX" \
    -V date="$MOD_DATE" \
    -V geometry="margin=2.5cm" \
    -V fontsize=11pt \
    -V linkcolor=blue \
    $FONT_ARGS \
    -o "$PDF" 2>/dev/null; then
    echo "✓ $PDF"
    ok=$((ok + 1))
  else
    # Retry without custom font (fallback)
    if pandoc "$MD" \
      --pdf-engine=xelatex \
      --include-in-header="$HEADER_TEX" \
      -V date="$MOD_DATE" \
      -V geometry="margin=2.5cm" \
      -V fontsize=11pt \
      -V linkcolor=blue \
      -o "$PDF" 2>/dev/null; then
      echo "✓ $PDF (default font)"
      ok=$((ok + 1))
    else
      echo "✗ FAILED"
      err=$((err + 1))
    fi
  fi
done

echo ""
echo "Done: $ok PDFs generated, $err errors."
