#!/bin/bash
# Restores OpenProject database from the latest backup in this repo.
# Run this after a git pull if you need to restore OpenProject data.
#
# Usage: bash openproject_restore.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SQL="$SCRIPT_DIR/openproject_backup.sql"

if [ ! -f "$SQL" ]; then
  echo "ERROR: $SQL not found. Run 'git pull' first."
  exit 1
fi

echo "==> This will REPLACE the current OpenProject database with the backup."
echo "    Backup file: $SQL ($(du -sh "$SQL" | cut -f1))"
echo ""
read -p "Are you sure? Type YES to continue: " CONFIRM
if [ "$CONFIRM" != "YES" ]; then
  echo "Aborted."
  exit 0
fi

echo ""
echo "==> Making sure OpenProject containers are running..."
docker compose -f ~/openproject/docker-compose.yml up -d
sleep 5

echo "==> Stopping web and worker to prevent DB writes during restore..."
docker compose -f ~/openproject/docker-compose.yml stop web worker cron proxy

echo "==> Dropping and recreating the database..."
docker exec openproject-db-1 psql -U postgres -c "DROP DATABASE IF EXISTS openproject;"
docker exec openproject-db-1 psql -U postgres -c "CREATE DATABASE openproject;"

echo "==> Restoring from backup..."
docker exec -i openproject-db-1 psql -U postgres openproject < "$SQL"

echo "==> Restarting all containers..."
docker compose -f ~/openproject/docker-compose.yml start web worker cron proxy

echo ""
echo "==> Waiting for web to be ready..."
until curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/ | grep -q "30[0-9]"; do
  sleep 3
done

echo "==> Done. OpenProject is restored and running at http://localhost:8080"
