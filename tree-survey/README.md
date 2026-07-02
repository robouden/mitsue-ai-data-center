# Mitsue Mother Tree Survey 🌳 / 御杖村 母樹調査アプリ

A tablet/phone web app for cataloguing Mitsue's native **"mother trees"** — old,
seed-bearing broadleaf trees that feed wildlife and seed the next forest.
Volunteers log in, the browser captures **GPS automatically**, they snap
**photos**, and each record is stored in a **DuckDB** file. Fully bilingual
EN / 日本語. Live at **https://trees.mitsue.it**.

Designed to double as a **school activity** and a **nature-tourism experience**:
go into the forest and catalogue the trees.

---

## 1. For volunteers / 調査ボランティア向け

### Getting an account
1. Open **https://trees.mitsue.it** on your phone or tablet.
2. Tap **Register / 登録**, enter a username, your display name, email and a password.
3. Open the confirmation email and tap the link (or ask an admin to confirm you).
4. Log in. Every record you save is attributed to your **display name**.

> 📍 GPS and 📷 camera only work over **HTTPS** — always use the
> `https://trees.mitsue.it` address, not a raw IP.

### Recording a tree (the **Record / 記録** page)
Fill the form top to bottom. **Hover/long-press any field label to see a bilingual
tooltip** explaining it.

1. **Species / 樹種** — pick from the 12 native species (leaf, bark and fruit help
   you identify; choose *Other* if unsure and type the name).
2. **Location / 位置** — tap **📍 Get GPS** to auto-fill latitude, longitude and
   elevation. Add slope/aspect if you can.
3. **Measurements / 計測** — DBH (trunk diameter at ~1.3 m), height, rough age,
   habitat, and overall health.
4. **Assessment / 評価** — tick the boxes that apply: ⭐ Mother tree, seeds present,
   seeds collected, saplings nearby, hollow, tagged, wildlife seen, sacred.
5. **Photos & notes / 写真とメモ** — take several photos (whole tree, bark, leaf,
   fruit — you can select more than one) and add any notes.
6. Tap **💾 Save record / 記録を保存**.

### Other pages
- **Guide / 図鑑** — reference photos and notes for each species.
- **List / 一覧** — the records logged so far.
- **Account / 設定** — change your display name, email or password.
- Tap the **🌳 header** any time to return to the Record page.

📖 A printable **Heritage Tree Field Guide** (identification + paper backup form)
lives in the project docs (`mitsue_heritage_tree_field_guide.md`).

---

## 2. For admins / 管理者向け

Admins see three extra menu items: **Data / データ**, **Users / 利用者**,
**Photos / 写真**.

### Data / データ — manage records
- **Global search** box filters across every column as you type.
- Click any **column header** to sort (↕ → ↑/↓); numbers sort numerically.
- The **header checkbox** selects all visible (filtered) rows.
- **✏️ Edit/編集** on any row to fix a mistake (all fields incl. species, GPS,
  measurements, checkboxes); **🗑 Delete/削除** to remove a record.
- **Export**: CSV, GeoJSON (for the map), Parquet.

### Users / 利用者 — manage volunteers
Each row has:
- **Edit/編集** — change a user's display name, email, or **reset their password**.
- **Disable/無効 · Enable/有効** — block or restore login without deleting.
- **+admin / −admin** — grant or revoke admin rights (this is how you add other admins).
- **Confirm** — manually confirm an account that didn't get the email.
- **Delete/削除** — remove the account.

You can also act on **your own** account (edit / disable / demote / delete) — each
asks for confirmation and logs you out afterward. **Safety guard:** the app refuses
to delete, disable or demote the **last active admin**, so you can never lock
everyone out.

> ⚠️ Renaming a user changes only future records — existing records keep the old
> display name, because records are attributed by name.

### Photos / 写真 — species guide
Upload a reference photo and bilingual caption for each species shown in the Guide.

---

## 3. Run locally / ローカル起動
```bash
cd tree-survey
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
./venv/bin/python manage.py adduser rob 'a-strong-password' 'Rob Oudendijk' --admin
./venv/bin/uvicorn app:app --host 0.0.0.0 --port 8009
```
Open `http://<your-laptop-ip>:8009` on a tablet on the same Wi-Fi.
> Browsers only allow GPS/camera over **HTTPS** (or `localhost`). For real field
> use over Wi-Fi/internet, use the HTTPS deploy below.

## 4. Manage volunteers / data from the CLI
```bash
./venv/bin/python manage.py adduser <user> <pass> "Name"       # add volunteer
./venv/bin/python manage.py adduser <user> <pass> "Name" --admin
./venv/bin/python manage.py listusers
./venv/bin/python manage.py deluser <user>
./venv/bin/python manage.py stats
./venv/bin/python manage.py export mitsue_trees.geojson        # or .csv / .parquet
```
> DuckDB is single-writer: **stop the server** before running `manage.py` write
> commands (adduser/deluser/export), or do it during a quiet moment. Admins can
> always export live from the web while the server runs.

## 5. Data layout (all git-ignored)
```
data/trees.duckdb        # the database
data/photos/<record_id>/ # uploaded photos
data/session_secret.txt  # auto-generated cookie secret
```
Query it any time with DuckDB:
```sql
SELECT species_ja, count(*) FROM trees GROUP BY species_ja;
SELECT * FROM trees WHERE mother_tree;
```

---

## 6. Deploy on the VPS (trees.mitsue.it, HTTPS)

**1. DNS** — A record `trees.mitsue.it → 80.208.225.44`.

**2. Copy & install** (on the VPS):
```bash
rsync -a tree-survey/ root@80.208.225.44:/opt/tree-survey/ --exclude venv --exclude data
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
    LimitRequestBody 26214400
</VirtualHost>
```
```bash
a2enmod proxy proxy_http && a2ensite trees-mitsue
systemctl reload apache2
certbot --apache -d trees.mitsue.it     # HTTPS — required for GPS & camera
```

### Deploy an update
Templates only — sync and restart:
```bash
rsync -a templates/ root@80.208.225.44:/opt/tree-survey/templates/
ssh root@80.208.225.44 "systemctl restart tree-survey"
```
If `app.py` changed, validate before restarting (DuckDB is single-writer, so stop
the service to let the import check open the DB):
```bash
rsync -a app.py root@80.208.225.44:/opt/tree-survey/app.py
ssh root@80.208.225.44 "cd /opt/tree-survey && systemctl stop tree-survey \
  && ./venv/bin/python -c 'import app' && systemctl start tree-survey"
```

Back up `/opt/tree-survey/data/` regularly (DB + photos).

> nginx instead of Apache? `proxy_pass http://127.0.0.1:8009;` plus
> `client_max_body_size 25m;`, then `certbot --nginx -d trees.mitsue.it`.
