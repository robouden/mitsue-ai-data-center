#!/bin/bash
# Start OpenProject and open it in the browser.

echo "==> Starting OpenProject..."
docker compose -f ~/openproject/docker-compose.yml up -d

echo "==> Waiting for web to be ready..."
until curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/ | grep -q "30[0-9]"; do
  sleep 2
done

echo "==> OpenProject is up at http://localhost:8080"
xdg-open http://localhost:8080 2>/dev/null &
