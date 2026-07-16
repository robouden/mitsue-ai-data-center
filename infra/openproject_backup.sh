#!/bin/bash
# Backs up OpenProject work packages (JSON) and database (SQL), then commits and pushes.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
API="https://openproject.mitsue.it/api/v3"
TOKEN="d7df8157865c3e15a0c08e6f856afcceadc7c15709684a29766976c82e742c75"
VPS="root@80.208.225.44"
SQL_OUT="$SCRIPT_DIR/openproject_backup.sql"

export_project_json() {
  local PROJECT_ID="$1"
  local JSON_OUT="$2"
  local PAGE_SIZE=500
  local ALL="[]"
  local OFFSET=1

  while true; do
    RESP=$(curl -s -u "apikey:$TOKEN" \
      "$API/projects/$PROJECT_ID/work_packages?pageSize=$PAGE_SIZE&offset=$OFFSET")
    COUNT=$(echo "$RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(len(d.get('_embedded',{}).get('elements',[])))")
    ALL=$(echo "$ALL $RESP" | python3 -c "
import sys, json
parts = sys.stdin.read().split(None, 1)
combined = json.loads(parts[0])
new = json.loads(parts[1]).get('_embedded',{}).get('elements',[])
combined += new
print(json.dumps(combined, indent=2, ensure_ascii=False))
")
    if [ "$COUNT" -lt "$PAGE_SIZE" ]; then break; fi
    OFFSET=$((OFFSET + PAGE_SIZE))
  done

  echo "$ALL" > "$JSON_OUT"
  TOTAL=$(echo "$ALL" | python3 -c "import sys,json; print(len(json.load(sys.stdin)))")
  echo "    $TOTAL work packages saved to $(basename $JSON_OUT)"
}

echo "==> Exporting work packages to JSON (English project)..."
export_project_json "3" "$SCRIPT_DIR/openproject_backup.json"

echo "==> Exporting work packages to JSON (Japanese project)..."
export_project_json "4" "$SCRIPT_DIR/openproject_backup_jp.json"

echo "==> Dumping PostgreSQL database from VPS..."
ssh "$VPS" "docker exec openproject-db-1 pg_dump -U postgres openproject" > "$SQL_OUT"
echo "    Database saved to openproject_backup.sql ($(du -sh "$SQL_OUT" | cut -f1))"

echo "==> Committing and pushing..."
cd "$SCRIPT_DIR"
git add openproject_backup.json openproject_backup_jp.json openproject_backup.sql
git commit -m "backup: OpenProject snapshot $(date '+%Y-%m-%d %H:%M')"
git push origin main
git push github main

echo ""
echo "Done. Both Codeberg and GitHub are up to date."
