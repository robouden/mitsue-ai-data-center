#!/bin/bash
# Sets up OpenProject on a fresh Ubuntu/Debian VPS and restores the Mitsue project data.
#
# Usage:
#   git clone https://codeberg.org/YR-Design/mitsue-ai-data-center
#   cd mitsue-ai-data-center
#   bash vps_setup.sh                          # HTTP only (port 8080)
#   bash vps_setup.sh openproject.example.com  # HTTPS via Caddy (recommended)
#
# Requirements:
#   - Ubuntu 22.04 / 24.04 or Debian 12
#   - Run as a user with sudo access (not root)
#   - Port 80, 443, 8080 open in your VPS firewall

set -euo pipefail

DOMAIN="${1:-}"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OP_DIR="$HOME/openproject"
COMPOSE="$OP_DIR/docker-compose.yml"
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'

log()  { echo -e "\n${GREEN}==>${NC} $1"; }
warn() { echo -e "${YELLOW}WARN:${NC} $1"; }
die()  { echo -e "${RED}ERROR:${NC} $1"; exit 1; }

# ── 1. Checks ─────────────────────────────────────────────────────────────────

log "Checking system..."
[[ "$EUID" -eq 0 ]] && die "Do not run as root. Use a sudo-capable user."
command -v curl &>/dev/null || sudo apt-get install -y curl

if [[ -f /etc/os-release ]]; then
    . /etc/os-release
    [[ "$ID" =~ ^(ubuntu|debian)$ ]] || warn "Untested OS: $PRETTY_NAME. Proceeding anyway."
fi

# ── 2. Docker ─────────────────────────────────────────────────────────────────

if command -v docker &>/dev/null; then
    log "Docker already installed: $(docker --version)"
else
    log "Installing Docker..."
    curl -fsSL https://get.docker.com | sh
    sudo usermod -aG docker "$USER"
    log "Docker installed. NOTE: You may need to log out and back in for group membership."
    # Use newgrp to apply group in this session
    exec newgrp docker <<'NEWGRP'
NEWGRP
fi

# ── 3. OpenProject docker-compose ─────────────────────────────────────────────

log "Setting up OpenProject directory at $OP_DIR..."
mkdir -p "$OP_DIR"

# Copy the pinned docker-compose from this repo
cp "$REPO_DIR/openproject_docker-compose.yml" "$COMPOSE"

# Patch host/HTTPS settings based on whether a domain was given
if [[ -n "$DOMAIN" ]]; then
    log "Configuring for domain: $DOMAIN (HTTPS via Caddy reverse proxy)"
    # OpenProject listens on 8080 (HTTP), Caddy handles TLS termination
    sed -i "s|OPENPROJECT_HOST__NAME: \"localhost:8080\"|OPENPROJECT_HOST__NAME: \"$DOMAIN\"|g" "$COMPOSE"
    sed -i 's|OPENPROJECT_HTTPS: "false"|OPENPROJECT_HTTPS: "true"|g'  "$COMPOSE"
    sed -i 's|OPENPROJECT_HSTS: "false"|OPENPROJECT_HSTS: "true"|g'    "$COMPOSE"
else
    log "No domain given — OpenProject will be accessible on port 8080 (HTTP only)"
fi

# ── 4. Start OpenProject ──────────────────────────────────────────────────────

log "Starting OpenProject containers..."
docker compose -f "$COMPOSE" up -d

log "Waiting for database to be ready..."
until docker exec openproject-db-1 pg_isready -U postgres &>/dev/null; do
    sleep 3
done
echo "  Database ready."

log "Waiting for web to be ready (this takes ~90 seconds on first start)..."
until curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/ | grep -qE "^[23]"; do
    sleep 5
done
echo "  Web ready."

# ── 5. Restore from backup ────────────────────────────────────────────────────

SQL="$REPO_DIR/openproject_backup.sql"
if [[ -f "$SQL" ]]; then
    log "Restoring OpenProject database from backup..."
    echo ""
    echo "  The restore script will ask you to type YES to confirm."
    echo "  This is destructive — it replaces any existing OpenProject data."
    echo ""
    bash "$REPO_DIR/openproject_restore.sh"
else
    warn "No openproject_backup.sql found. Skipping restore — OpenProject starts empty."
    warn "Run 'git pull' to fetch the latest backup, then run: bash openproject_restore.sh"
fi

# ── 6. Caddy reverse proxy + auto-HTTPS ───────────────────────────────────────

if [[ -n "$DOMAIN" ]]; then
    log "Installing Caddy for HTTPS ($DOMAIN → localhost:8080)..."

    # Install Caddy
    if ! command -v caddy &>/dev/null; then
        sudo apt-get install -y debian-keyring debian-archive-keyring apt-transport-https
        curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' \
            | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
        curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' \
            | sudo tee /etc/apt/sources.list.d/caddy-stable.list
        sudo apt-get update && sudo apt-get install -y caddy
    fi

    # Write Caddyfile
    sudo tee /etc/caddy/Caddyfile > /dev/null << EOF
$DOMAIN {
    reverse_proxy localhost:8080
}
EOF

    sudo systemctl reload caddy
    log "Caddy configured. SSL certificate will be issued automatically by Let's Encrypt."
fi

# ── 7. Firewall ───────────────────────────────────────────────────────────────

if command -v ufw &>/dev/null; then
    log "Configuring UFW firewall..."
    sudo ufw allow OpenSSH
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp
    [[ -z "$DOMAIN" ]] && sudo ufw allow 8080/tcp
    sudo ufw --force enable
    echo "  Firewall rules applied."
fi

# ── Done ──────────────────────────────────────────────────────────────────────

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  OpenProject is up and running!${NC}"
echo -e "${GREEN}========================================${NC}"
if [[ -n "$DOMAIN" ]]; then
    echo "  URL:      https://$DOMAIN"
else
    echo "  URL:      http://$(curl -s ifconfig.me 2>/dev/null || echo '<your-vps-ip>'):8080"
fi
echo "  Login:    admin / (set during first restore, or use the welcome email)"
echo ""
echo "  To back up and push:  bash $REPO_DIR/openproject_backup.sh"
echo "  To restore:           bash $REPO_DIR/openproject_restore.sh"
echo ""
