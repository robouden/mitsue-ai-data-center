# Mitsue Mother Tree Survey 🌳 / 御杖村 母樹調査アプリ

A tiny tablet/phone web app for cataloguing Mitsue's native "mother trees" in the
field. Volunteers log in, the browser captures **GPS automatically**, they snap
**photos**, and each record is stored in a **DuckDB** file. Bilingual EN / 日本語.

Designed to double as a **school activity** and a **nature-tourism experience** —
go into the forest and catalogue the trees.

## What it does
- 🔐 Per-volunteer login (named accounts → every record is attributed)
- 📍 One-tap GPS (lat/lon/accuracy + altitude where available)
- 📷 Multiple photos per tree (whole tree, bark, leaf, fruit)
- 🌳 12 native species preset + "Other", DBH/height/age, habitat, health
- ⭐ "Mother tree?" + seeds/saplings/wildlife/sacred checkboxes
- 🗂 Admin list view + export to **CSV / GeoJSON / Parquet** for the OSM/DuckDB map

## Run locally
```bash
cd tree-survey
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
./venv/bin/python manage.py adduser rob 'a-strong-password' 'Rob Oudendijk' --admin
./venv/bin/uvicorn app:app --host 0.0.0.0 --port 8009
```
Open `http://<your-laptop-ip>:8009` on a tablet on the same Wi-Fi.
> ⚠️ Browsers only allow GPS/camera over **HTTPS** (or `localhost`). For real field
> use over Wi-Fi/internet you need the HTTPS deploy below.

## Manage volunteers / data
```bash
./venv/bin/python manage.py adduser <user> <pass> "Name"      # add volunteer
./venv/bin/python manage.py adduser <user> <pass> "Name" --admin
./venv/bin/python manage.py listusers
./venv/bin/python manage.py deluser <user>
./venv/bin/python manage.py stats
./venv/bin/python manage.py export mitsue_trees.geojson       # or .csv / .parquet
```
> DuckDB is single-writer: **stop the server** before running `manage.py` write
> commands (adduser/deluser/export), or do user management during a quiet moment.
> Admins can always export live from the web `/records` page while the server runs.

## Data layout (all git-ignored)
```
data/trees.duckdb        # the database
data/photos/<record_id>/ # uploaded photos
data/session_secret.txt  # auto-generated cookie secret
```
Query it any time with DuckDB:
```sql
SELECT species_ja, count(*) FROM 'data/trees.duckdb' ... ;   -- or: duckdb data/trees.duckdb
SELECT * FROM trees WHERE mother_tree;
```

---

## Deploy on the VPS (trees.mitsue.it, HTTPS)

**1. DNS** — add an A record `trees.mitsue.it → 80.208.225.44`.

**2. Copy the app & install** (on the VPS):
```bash
mkdir -p /opt/tree-survey && rsync -a tree-survey/ root@80.208.225.44:/opt/tree-survey/ \
  --exclude venv --exclude data
ssh root@80.208.225.44
cd /opt/tree-survey
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
./venv/bin/python manage.py adduser rob 'STRONG-PASS' 'Rob Oudendijk' --admin
```

**3. systemd service** — `/etc/systemd/system/tree-survey.service`:
```ini
[Unit]
Description=Mitsue Mother Tree Survey
After=network.target

[Service]
WorkingDirectory=/opt/tree-survey
Environment=TREE_DATA_DIR=/opt/tree-survey/data
ExecStart=/opt/tree-survey/venv/bin/uvicorn app:app --host 127.0.0.1 --port 8009
Restart=always
User=www-data
Group=www-data

[Install]
WantedBy=multi-user.target
```
```bash
chown -R www-data:www-data /opt/tree-survey/data
systemctl daemon-reload && systemctl enable --now tree-survey
```

**4. Apache reverse proxy** — vhost for `trees.mitsue.it`:
```apache
<VirtualHost *:80>
    ServerName trees.mitsue.it
    ProxyPreserveHost On
    ProxyPass        / http://127.0.0.1:8009/
    ProxyPassReverse / http://127.0.0.1:8009/
    # allow large photo uploads
    LimitRequestBody 26214400
</VirtualHost>
```
```bash
a2enmod proxy proxy_http
a2ensite trees-mitsue   # after saving the vhost
systemctl reload apache2
certbot --apache -d trees.mitsue.it     # HTTPS — required for GPS & camera
```

**5. Done.** Volunteers visit `https://trees.mitsue.it`, log in, and survey.
Back up `/opt/tree-survey/data/` regularly (DB + photos).

> nginx instead of Apache? Same idea: `proxy_pass http://127.0.0.1:8009;` plus
> `client_max_body_size 25m;`, then `certbot --nginx -d trees.mitsue.it`.
