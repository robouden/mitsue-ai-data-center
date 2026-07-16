#!/bin/bash

# Update all document dates to 2026-06-10

CURRENT_DIR="/home/rob/Documents/Mitsue/Mitsue Village Project AI data center"
cd "$CURRENT_DIR"

# Files that need version/date updates
files=(
  "mitsue_founding_charter.md"
  "Mitsue_Research_Brief_jp.md"
  "mitsue_qa_briefing.md"
  "mitsue_project_overview_pellegrom.md"
  "mitsue_revenue_model_jp.md"
  "mitsue_project_founding_story.md"
  "mitsue_email_highreso_intro.md"
  "mitsue_stakeholders.md"
  "mitsue_introduction_a4.md"
  "mitsue_quantum_mesh_outreach.md"
  "mitsue_revenue_model.md"
  "SONNET_TASK_village_re_plan_alignment.md"
  "mitsue_village_re_plan_alignment_jp.md"
  "mitsue_project_founding_story_jp.md"
  "mitsue_village_government_onepager_jp.md"
  "degraded_forests_paper_summary_and_application.md"
  "degraded_forests_paper_summary_and_application_JP.md"
  "docs/extra/mitsue_files from Village hall/mitsue_village_re_plan_clean_translation_en.md"
  "mitsue_wbs.md"
  "PDF_CONVERSION_GUIDE.md"
  "SONNET_TASK_budget_revenue_dependency.md"
  "mitsue_business_case.md"
  "mitsue_quantum_mesh_outreach_jp.md"
  "mitsue_founder_agreement_template.md"
  "mitsue_business_case_jp.md"
  "mitsue_evm_plan.md"
)

# Update version headers and last modified dates
for file in "${files[@]}"; do
  # Docs moved into docs/<theme>/ — resolve by basename if not at the listed path.
  [[ -f "$file" ]] || file=$(find . -path ./.git -prune -o -name "$(basename "$file")" -print | head -1)
  if [[ -f "$file" ]]; then
    echo "Updating: $file"
    # Update version headers that contain "Last modified: YYYY-MM-DD"
    sed -i 's/Last modified: 2026-06-05/Last modified: 2026-06-10/g' "$file"
    sed -i 's/Last modified: 2026-06-07/Last modified: 2026-06-10/g' "$file"
    sed -i 's/Last modified: 2026-06-02/Last modified: 2026-06-10/g' "$file"
    sed -i 's/Last modified: 2026-05-29/Last modified: 2026-06-10/g' "$file"
    sed -i 's/Last modified: 2026-05-30/Last modified: 2026-06-10/g' "$file"
  else
    echo "File not found: $file"
  fi
done

# Also update the specific version headers in their respective locations
# This is a catch-all for files that might have specific patterns
cd "$CURRENT_DIR"

# Update specific version patterns
for file in "${files[@]}"; do
  # Docs moved into docs/<theme>/ — resolve by basename if not at the listed path.
  [[ -f "$file" ]] || file=$(find . -path ./.git -prune -o -name "$(basename "$file")" -print | head -1)
  if [[ -f "$file" ]]; then
    # Look for patterns like "Version: vX.Y &nbsp;|&nbsp; Last modified: YYYY-MM-DD"
    # and update the date part
    sed -i -E 's/Last modified: 20(26-[0-9]{2}-[0-9]{2})/Last modified: 2026-06-10/' "$file"
    
    # Also look for "Version: vX.Y &nbsp;|&nbsp; Last modified: YYYY-MM-DD" patterns
    # specifically for the right-aligned headers
    sed -i -E 's/Version: v[0-9.]+ &nbsp;\|&nbsp; Last modified: 20(26-[0-9]{2}-[0-9]{2})/Version: v2.7 &nbsp;|&nbsp; Last modified: 2026-06-10/' "$file"
  fi
done

echo "Date update completed for all documents"
