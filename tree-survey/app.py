"""Mitsue Mother Tree field-survey app.

FastAPI + DuckDB. Volunteers self-register (email-confirmed), log in, and submit
tree records from a tablet (auto GPS + photo). Admins manage users, edit the data
table, and curate a photo reference guide. Bilingual EN / 日本語.
御杖村 母樹プロジェクト 野外調査アプリ
"""
import os, io, re, json, time, hmac, hashlib, secrets, smtplib, threading, datetime as dt
from pathlib import Path
from email.message import EmailMessage

import duckdb
from fastapi import FastAPI, Request, Form, UploadFile, File, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse, Response, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

BASE = Path(__file__).resolve().parent
DATA = Path(os.environ.get("TREE_DATA_DIR", BASE / "data"))
PHOTOS = DATA / "photos"
GUIDE = DATA / "guide"
DB_PATH = str(DATA / "trees.duckdb")
for d in (DATA, PHOTOS, GUIDE):
    d.mkdir(parents=True, exist_ok=True)

# ---- site / email config ----
BASE_URL = os.environ.get("TREE_BASE_URL", "https://trees.mitsue.it").rstrip("/")
MAIL_FROM = os.environ.get("TREE_MAIL_FROM", "Mitsue Mother Trees <noreply@mitsue.it>")
SMTP_HOST = os.environ.get("TREE_SMTP_HOST", "127.0.0.1")
SMTP_PORT = int(os.environ.get("TREE_SMTP_PORT", "25"))
TOKEN_TTL_H = 24
HTTPS = BASE_URL.startswith("https")

_secret_file = DATA / "session_secret.txt"
if not _secret_file.exists():
    _secret_file.write_text(secrets.token_hex(32))
SECRET = _secret_file.read_text().strip()

SPECIES = [  # (en, ja, latin)
    ("Japanese beech", "ブナ", "Fagus crenata"),
    ("Mizunara oak", "ミズナラ", "Quercus crispula"),
    ("Konara oak", "コナラ", "Quercus serrata"),
    ("Sawtooth oak", "クヌギ", "Quercus acutissima"),
    ("Horse chestnut", "トチノキ", "Aesculus turbinata"),
    ("Japanese nutmeg-yew", "カヤ", "Torreya nucifera"),
    ("Wild mountain cherry", "ヤマザクラ", "Cerasus jamasakura"),
    ("Japanese maple", "イロハモミジ", "Acer palmatum"),
    ("Bigleaf magnolia", "ホオノキ", "Magnolia obovata"),
    ("Japanese zelkova", "ケヤキ", "Zelkova serrata"),
    ("Japanese chestnut", "クリ", "Castanea crenata"),
    ("Katsura", "カツラ", "Cercidiphyllum japonicum"),
]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# ---- DuckDB (single connection guarded by a lock) ----
_lock = threading.Lock()
con = duckdb.connect(DB_PATH)
con.execute("""
CREATE TABLE IF NOT EXISTS users (
  username     TEXT PRIMARY KEY,
  display_name TEXT,
  salt         TEXT,
  pw_hash      TEXT,
  is_admin     BOOLEAN DEFAULT FALSE,
  created_at   TIMESTAMP
)""")
# migration: add account columns to any pre-existing users table, then backfill
for col, ddl in [("email", "TEXT"), ("confirmed", "BOOLEAN"), ("active", "BOOLEAN"),
                 ("confirm_token", "TEXT"), ("confirm_expires", "TIMESTAMP"),
                 ("pending_email", "TEXT")]:
    con.execute(f"ALTER TABLE users ADD COLUMN IF NOT EXISTS {col} {ddl}")
con.execute("UPDATE users SET confirmed=TRUE WHERE confirmed IS NULL")
con.execute("UPDATE users SET active=TRUE WHERE active IS NULL")

con.execute("""
CREATE TABLE IF NOT EXISTS trees (
  record_id        TEXT PRIMARY KEY,
  created_at       TIMESTAMP,
  surveyor         TEXT,
  species_en       TEXT,
  species_ja       TEXT,
  latin            TEXT,
  lat              DOUBLE,
  lon              DOUBLE,
  gps_accuracy_m   DOUBLE,
  elevation_m      DOUBLE,
  slope_aspect     TEXT,
  dbh_cm           DOUBLE,
  height_m         DOUBLE,
  est_age_yr       INTEGER,
  habitat          TEXT,
  health           TEXT,
  hollow           BOOLEAN,
  mother_tree      BOOLEAN,
  seeds_present    BOOLEAN,
  seeds_collected  BOOLEAN,
  saplings_nearby  BOOLEAN,
  tagged           BOOLEAN,
  wildlife_obs     BOOLEAN,
  cultural_sacred  BOOLEAN,
  wildlife_text    TEXT,
  notes            TEXT,
  photo_paths      TEXT
)""")
con.execute("""
CREATE TABLE IF NOT EXISTS guide (
  species_key  TEXT PRIMARY KEY,
  species_en   TEXT,
  species_ja   TEXT,
  latin        TEXT,
  photo_path   TEXT,
  caption_en   TEXT,
  caption_ja   TEXT,
  updated_at   TIMESTAMP,
  updated_by   TEXT
)""")
# seed guide rows from SPECIES (idempotent)
for en, ja, lat in SPECIES:
    k = slug(en)
    if not con.execute("SELECT 1 FROM guide WHERE species_key=?", [k]).fetchone():
        con.execute("INSERT INTO guide (species_key,species_en,species_ja,latin) VALUES (?,?,?,?)",
                    [k, en, ja, lat])


# -------------------- helpers --------------------
def hash_pw(pw, salt=None):
    salt = salt or secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac("sha256", pw.encode(), bytes.fromhex(salt), 200_000).hex()
    return salt, h


def verify_pw(pw, salt, h):
    calc = hashlib.pbkdf2_hmac("sha256", pw.encode(), bytes.fromhex(salt), 200_000).hex()
    return hmac.compare_digest(calc, h)


def add_user(username, password, display_name="", is_admin=False, email=None,
             confirmed=True, active=True):
    salt, h = hash_pw(password)
    with _lock:
        con.execute("DELETE FROM users WHERE username=?", [username])
        con.execute("""INSERT INTO users
            (username,display_name,salt,pw_hash,is_admin,created_at,email,confirmed,active)
            VALUES (?,?,?,?,?,?,?,?,?)""",
            [username, display_name or username, salt, h, is_admin, dt.datetime.now(),
             email, confirmed, active])


USER_COLS = ["username", "display_name", "salt", "pw_hash", "is_admin",
             "email", "confirmed", "active", "pending_email"]


def get_user(username):
    with _lock:
        r = con.execute(f"SELECT {','.join(USER_COLS)} FROM users WHERE username=?",
                        [username]).fetchone()
    return dict(zip(USER_COLS, r)) if r else None


def email_valid(e):
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", e or ""))


def set_confirm_token(username, pending_email=None):
    tok = secrets.token_urlsafe(32)
    exp = dt.datetime.now() + dt.timedelta(hours=TOKEN_TTL_H)
    with _lock:
        con.execute("UPDATE users SET confirm_token=?, confirm_expires=?, pending_email=? WHERE username=?",
                    [tok, exp, pending_email, username])
    return tok


def send_email(to, subject, body):
    try:
        m = EmailMessage()
        m["From"], m["To"], m["Subject"] = MAIL_FROM, to, subject
        m.set_content(body)
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as s:
            s.send_message(m)
        return True
    except Exception as e:  # noqa
        print("EMAIL FAIL ->", to, ":", e)
        return False


def send_confirmation(to, username, tok):
    link = f"{BASE_URL}/confirm?token={tok}"
    send_email(to, "メール確認 / Confirm your Mitsue tree-survey account",
               f"こんにちは / Hello {username},\n\n"
               f"Confirm your account for the Mitsue Mother Tree survey by opening this link:\n"
               f"下記リンクを開いてアカウントを確認してください:\n\n{link}\n\n"
               f"リンクは{TOKEN_TTL_H}時間で失効します。 / This link expires in {TOKEN_TTL_H} hours.\n\n"
               f"心当たりがない場合は無視してください。 / If you didn't request this, ignore this email.\n\n"
               f"御杖村 母樹プロジェクト / Mitsue Mother Tree Project")


# simple in-memory rate limiter
_rl_lock = threading.Lock()
_rl = {}


def rate_ok(key, limit, window_s):
    now = time.time()
    with _rl_lock:
        hist = [t for t in _rl.get(key, []) if now - t < window_s]
        if len(hist) >= limit:
            _rl[key] = hist
            return False
        hist.append(now)
        _rl[key] = hist
        return True


def client_ip(request: Request):
    xff = request.headers.get("x-forwarded-for")
    return xff.split(",")[0].strip() if xff else (request.client.host if request.client else "?")


# -------------------- app --------------------
app = FastAPI(title="Mitsue Mother Tree Survey")
app.add_middleware(SessionMiddleware, secret_key=SECRET, https_only=HTTPS,
                   same_site="lax", max_age=60 * 60 * 24 * 30)
app.mount("/photos", StaticFiles(directory=str(PHOTOS)), name="photos")
app.mount("/guideimg", StaticFiles(directory=str(GUIDE)), name="guideimg")
templates = Jinja2Templates(directory=str(BASE / "templates"))


@app.middleware("http")
async def security_headers(request: Request, call_next):
    resp = await call_next(request)
    if HTTPS:
        resp.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "SAMEORIGIN"
    resp.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return resp


def current_user(request: Request):
    u = request.session.get("user")
    if not u:
        raise HTTPException(status_code=303, headers={"Location": "/login"})
    rec = get_user(u)
    if not rec or not rec.get("active"):
        request.session.clear()
        raise HTTPException(status_code=303, headers={"Location": "/login"})
    return u


def require_admin(request: Request):
    if not request.session.get("is_admin"):
        raise HTTPException(status_code=403, detail="管理者のみ / Admin only")
    return request.session.get("user")


def msg_page(request, title, body, link="/login", link_text="続ける / Continue", status=200):
    return templates.TemplateResponse(request, "message.html",
                                      {"title": title, "body": body, "link": link,
                                       "link_text": link_text}, status_code=status)


def _login_session(request, u):
    request.session["user"] = u["username"]
    request.session["display_name"] = u["display_name"]
    request.session["is_admin"] = bool(u["is_admin"])


# -------------------- auth --------------------
@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse(request, "login.html", {"error": None})


@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    u = get_user(username.strip().lower())
    if not u or not verify_pw(password, u["salt"], u["pw_hash"]):
        return templates.TemplateResponse(request, "login.html",
            {"error": "ユーザー名かパスワードが違います / Wrong username or password"}, status_code=401)
    if not u["active"]:
        return templates.TemplateResponse(request, "login.html",
            {"error": "アカウントは無効です。担当者にご連絡ください。 / Account disabled. Contact the coordinator."},
            status_code=403)
    if not u["confirmed"]:
        return templates.TemplateResponse(request, "login.html",
            {"error": "先にメール確認をしてください。 / Please confirm your email first.",
             "show_resend": True}, status_code=403)
    _login_session(request, u)
    return RedirectResponse("/", status_code=303)


@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=303)


@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse(request, "register.html", {"error": None})


@app.post("/register")
def register(request: Request, display_name: str = Form(...), username: str = Form(...),
             email: str = Form(...), password: str = Form(...)):
    ip = client_ip(request)
    username = username.strip().lower()
    email = email.strip()
    err = None
    if not (rate_ok("reg-ip:" + ip, 6, 3600) and rate_ok("reg-em:" + email.lower(), 3, 86400)):
        err = "試行回数が多すぎます。後でお試しください。 / Too many attempts. Please try again later."
    elif len(username) < 3 or not username.isascii() or not username.replace("_", "").replace("-", "").isalnum():
        err = "ユーザー名は3文字以上の英数字。 / Username: 3+ letters/numbers, no spaces."
    elif not email_valid(email):
        err = "正しいメールアドレスを入力してください。 / Please enter a valid email."
    elif len(password) < 6:
        err = "パスワードは6文字以上。 / Password must be at least 6 characters."
    elif get_user(username):
        err = "そのユーザー名は使われています。 / That username is taken."
    if err:
        return templates.TemplateResponse(request, "register.html",
                                          {"error": err, "display_name": display_name,
                                           "username": username, "email": email}, status_code=400)
    # write the unconfirmed user, then (outside the lock) send the email
    add_user(username, password, display_name.strip() or username,
             is_admin=False, email=email, confirmed=False, active=True)
    tok = set_confirm_token(username)
    send_confirmation(email, username, tok)
    return msg_page(request, "メールを確認 / Check your email",
                    f"確認リンクを <b>{email}</b> に送信しました。リンクを開いて有効化し、ログインしてください。<br>"
                    f"We sent a confirmation link to <b>{email}</b>. Open it to activate your account, then sign in.",
                    link="/login", link_text="ログインへ / Go to sign in")


@app.get("/confirm", response_class=HTMLResponse)
def confirm(request: Request, token: str = ""):
    with _lock:
        r = con.execute("SELECT username, confirm_expires, pending_email FROM users WHERE confirm_token=?",
                        [token]).fetchone()
    if not token or not r:
        return msg_page(request, "無効なリンク / Invalid link",
                        "このリンクは無効か使用済みです。 / This confirmation link is invalid or already used.",
                        status=400)
    username, expires, pending = r
    if expires and dt.datetime.now() > expires:
        return msg_page(request, "リンク失効 / Link expired",
                        "リンクは失効しました。再送してください。 / This link has expired. Request a new one.",
                        link="/resend", link_text="再送 / Resend link", status=400)
    with _lock:
        if pending:  # email-change confirmation
            con.execute("UPDATE users SET email=?, pending_email=NULL, confirmed=TRUE, confirm_token=NULL, confirm_expires=NULL WHERE username=?",
                        [pending, username])
        else:
            con.execute("UPDATE users SET confirmed=TRUE, confirm_token=NULL, confirm_expires=NULL WHERE username=?",
                        [username])
    u = get_user(username)
    _login_session(request, u)
    return msg_page(request, "確認完了 / Confirmed!",
                    "メール確認が完了しました。調査を始めましょう！ / Your email is confirmed and you're signed in. Happy surveying!",
                    link="/", link_text="はじめる / Start")


@app.get("/resend", response_class=HTMLResponse)
def resend_form(request: Request):
    return templates.TemplateResponse(request, "resend.html", {"error": None})


@app.post("/resend")
def resend(request: Request, email: str = Form(...)):
    email = email.strip()
    if rate_ok("resend-ip:" + client_ip(request), 6, 3600):
        with _lock:
            r = con.execute("SELECT username, email FROM users WHERE lower(email)=lower(?) AND confirmed=FALSE",
                            [email]).fetchone()
        if r:
            tok = set_confirm_token(r[0])
            send_confirmation(r[1], r[0], tok)
    # always generic (no account enumeration)
    return msg_page(request, "メールを確認 / Check your email",
                    f"未確認のアカウントがあれば、新しいリンクを送信しました。<br>"
                    f"If an unconfirmed account uses <b>{email}</b>, a new link is on its way.",
                    link="/login", link_text="ログインへ / Go to sign in")


# -------------------- account self-edit --------------------
@app.get("/account", response_class=HTMLResponse)
def account_form(request: Request, user: str = Depends(current_user), ok: str = ""):
    u = get_user(user)
    return templates.TemplateResponse(request, "account.html", {"u": u, "ok": ok, "error": None})


@app.post("/account")
def account_save(request: Request, user: str = Depends(current_user),
                 display_name: str = Form(...), email: str = Form(...),
                 current_password: str = Form(""), new_password: str = Form("")):
    u = get_user(user)
    error = ok = None
    new_email = email.strip()
    with _lock:
        con.execute("UPDATE users SET display_name=? WHERE username=?", [display_name.strip() or user, user])
    request.session["display_name"] = display_name.strip() or user

    if new_password:
        if not verify_pw(current_password, u["salt"], u["pw_hash"]):
            error = "現在のパスワードが違います。 / Current password is wrong."
        elif len(new_password) < 6:
            error = "新しいパスワードは6文字以上。 / New password must be 6+ characters."
        else:
            salt, h = hash_pw(new_password)
            with _lock:
                con.execute("UPDATE users SET salt=?, pw_hash=? WHERE username=?", [salt, h, user])
            ok = "保存しました。 / Saved."

    if not error and new_email and new_email.lower() != (u["email"] or "").lower():
        if not email_valid(new_email):
            error = "メールアドレスが不正です。 / Invalid email."
        else:
            tok = set_confirm_token(user, pending_email=new_email)
            send_confirmation(new_email, user, tok)
            ok = "保存しました。新しいメールに確認リンクを送りました。 / Saved. Check your new email to confirm the change."
    elif not error:
        ok = ok or "保存しました。 / Saved."

    u = get_user(user)
    return templates.TemplateResponse(request, "account.html", {"u": u, "ok": ok, "error": error},
                                      status_code=200 if not error else 400)


# -------------------- survey form + submit --------------------
@app.get("/", response_class=HTMLResponse)
def form(request: Request, user: str = Depends(current_user), saved: str = ""):
    return templates.TemplateResponse(request, "form.html", {
        "species": [(en, ja, lat) for en, ja, lat in SPECIES] + [("その他 / Other", "", "")],
        "display_name": request.session.get("display_name", user),
        "is_admin": request.session.get("is_admin", False),
        "saved": saved,
    })


def _b(v):
    return v is not None and v != ""


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _inum(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


@app.post("/submit")
async def submit(request: Request, user: str = Depends(current_user),
                 species: str = Form(""), species_other_en: str = Form(""),
                 species_other_ja: str = Form(""), latin: str = Form(""),
                 lat: str = Form(""), lon: str = Form(""), gps_accuracy_m: str = Form(""),
                 elevation_m: str = Form(""), slope_aspect: str = Form(""),
                 dbh_cm: str = Form(""), height_m: str = Form(""), est_age_yr: str = Form(""),
                 habitat: str = Form(""), health: str = Form(""),
                 hollow: str = Form(None), mother_tree: str = Form(None),
                 seeds_present: str = Form(None), seeds_collected: str = Form(None),
                 saplings_nearby: str = Form(None), tagged: str = Form(None),
                 wildlife_obs: str = Form(None), cultural_sacred: str = Form(None),
                 wildlife_text: str = Form(""), notes: str = Form(""),
                 photos: list[UploadFile] = File(default=[])):
    rid = "T-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + secrets.token_hex(2)
    if species == "__other__":
        sp_en, sp_ja = species_other_en, species_other_ja
    else:
        parts = (species or "||").split("|")
        sp_en, sp_ja = parts[0], (parts[1] if len(parts) > 1 else "")
        if len(parts) > 2 and not latin:
            latin = parts[2]

    saved_paths = []
    pdir = PHOTOS / rid
    for i, up in enumerate(photos or []):
        if not up or not up.filename:
            continue
        pdir.mkdir(parents=True, exist_ok=True)
        ext = os.path.splitext(up.filename)[1].lower() or ".jpg"
        if ext not in (".jpg", ".jpeg", ".png", ".webp", ".heic"):
            ext = ".jpg"
        dest = pdir / f"{i+1}{ext}"
        dest.write_bytes(await up.read())
        saved_paths.append(f"{rid}/{dest.name}")

    row = [
        rid, dt.datetime.now(), request.session.get("display_name", user),
        sp_en, sp_ja, latin,
        _num(lat), _num(lon), _num(gps_accuracy_m), _num(elevation_m), slope_aspect,
        _num(dbh_cm), _num(height_m), _inum(est_age_yr), habitat, health,
        _b(hollow), _b(mother_tree), _b(seeds_present), _b(seeds_collected),
        _b(saplings_nearby), _b(tagged), _b(wildlife_obs), _b(cultural_sacred),
        wildlife_text, notes, ",".join(saved_paths),
    ]
    with _lock:
        con.execute("INSERT INTO trees VALUES (" + ",".join(["?"] * len(row)) + ")", row)
    return RedirectResponse(f"/?saved={rid}", status_code=303)


# -------------------- records list --------------------
@app.get("/records", response_class=HTMLResponse)
def records(request: Request, _: str = Depends(current_user)):
    with _lock:
        rows = con.execute("""SELECT record_id, created_at, surveyor, species_en, species_ja,
                              lat, lon, mother_tree, photo_paths
                              FROM trees ORDER BY created_at DESC LIMIT 500""").fetchall()
    cols = ["record_id", "created_at", "surveyor", "species_en", "species_ja",
            "lat", "lon", "mother_tree", "photo_paths"]
    data = [dict(zip(cols, r)) for r in rows]
    return templates.TemplateResponse(request, "records.html", {
        "rows": data, "is_admin": request.session.get("is_admin", False), "total": len(data)})


# -------------------- reference guide (gallery) --------------------
GUIDE_COLS = ["species_key", "species_en", "species_ja", "latin", "photo_path",
              "caption_en", "caption_ja", "updated_at", "updated_by"]


def guide_rows():
    with _lock:
        rows = con.execute(f"SELECT {','.join(GUIDE_COLS)} FROM guide ORDER BY species_en").fetchall()
    return [dict(zip(GUIDE_COLS, r)) for r in rows]


@app.get("/guide", response_class=HTMLResponse)
def guide_view(request: Request, _: str = Depends(current_user)):
    return templates.TemplateResponse(request, "guide.html", {
        "rows": guide_rows(), "is_admin": request.session.get("is_admin", False)})


@app.get("/admin/guide", response_class=HTMLResponse)
def admin_guide(request: Request, _: str = Depends(require_admin)):
    return templates.TemplateResponse(request, "admin_guide.html", {"rows": guide_rows()})


@app.post("/admin/guide/{species_key}")
async def admin_guide_save(request: Request, species_key: str, _: str = Depends(require_admin),
                           caption_en: str = Form(""), caption_ja: str = Form(""),
                           photo: UploadFile = File(default=None)):
    photo_path = None
    if photo and photo.filename:
        ext = os.path.splitext(photo.filename)[1].lower()
        if ext not in (".jpg", ".jpeg", ".png", ".webp"):
            ext = ".jpg"
        dest = GUIDE / f"{species_key}{ext}"
        dest.write_bytes(await photo.read())
        photo_path = dest.name
    with _lock:
        if photo_path:
            con.execute("UPDATE guide SET photo_path=?, caption_en=?, caption_ja=?, updated_at=?, updated_by=? WHERE species_key=?",
                        [photo_path, caption_en, caption_ja, dt.datetime.now(), request.session.get("user"), species_key])
        else:
            con.execute("UPDATE guide SET caption_en=?, caption_ja=?, updated_at=?, updated_by=? WHERE species_key=?",
                        [caption_en, caption_ja, dt.datetime.now(), request.session.get("user"), species_key])
    return RedirectResponse("/admin/guide", status_code=303)


# -------------------- admin: users --------------------
@app.get("/admin/users", response_class=HTMLResponse)
def admin_users(request: Request, me: str = Depends(require_admin)):
    with _lock:
        rows = con.execute("""SELECT u.username,u.display_name,u.email,u.is_admin,u.confirmed,u.active,
            u.created_at, (SELECT count(*) FROM trees t WHERE t.surveyor=u.display_name) AS n
            FROM users u ORDER BY u.created_at""").fetchall()
    cols = ["username", "display_name", "email", "is_admin", "confirmed", "active", "created_at", "n"]
    return templates.TemplateResponse(request, "admin_users.html",
                                      {"rows": [dict(zip(cols, r)) for r in rows], "me": me})


def _active_admin_count():
    with _lock:
        return con.execute("SELECT count(*) FROM users WHERE is_admin AND active").fetchone()[0]


# NOTE: the literal /edit routes must be registered BEFORE the /{action}
# catch-all below, otherwise "edit" is swallowed as an (unknown) action.
@app.get("/admin/users/{username}/edit", response_class=HTMLResponse)
def admin_user_edit(request: Request, username: str, me: str = Depends(require_admin)):
    u = get_user(username)
    if not u:
        raise HTTPException(status_code=404, detail="該当ユーザーなし / No such user")
    return templates.TemplateResponse(request, "user_edit.html", {"u": u, "me": me})


@app.post("/admin/users/{username}/edit")
def admin_user_edit_save(request: Request, username: str,
                         display_name: str = Form(""), email: str = Form(""),
                         new_password: str = Form(""), me: str = Depends(require_admin)):
    u = get_user(username)
    if not u:
        raise HTTPException(status_code=404, detail="該当ユーザーなし / No such user")
    if email and not email_valid(email):
        raise HTTPException(status_code=400, detail="メール形式が不正 / Invalid email")
    with _lock:
        con.execute("UPDATE users SET display_name=?, email=? WHERE username=?",
                    [display_name or username, email or None, username])
        if new_password:
            salt, h = hash_pw(new_password)
            con.execute("UPDATE users SET salt=?, pw_hash=? WHERE username=?", [salt, h, username])
    if username == me:
        request.session["display_name"] = display_name or username
    return RedirectResponse("/admin/users", status_code=303)


@app.post("/admin/users/{username}/{action}")
def admin_user_action(request: Request, username: str, action: str, me: str = Depends(require_admin)):
    tgt = get_user(username)
    if not tgt:
        raise HTTPException(status_code=404, detail="該当ユーザーなし / No such user")
    if action not in ("delete", "disable", "enable", "promote", "demote", "confirm"):
        raise HTTPException(status_code=404, detail="Unknown action")
    # never let the last active admin lock everyone out (applies to self too)
    if tgt["is_admin"] and tgt["active"] and action in ("delete", "disable", "demote") \
            and _active_admin_count() <= 1:
        raise HTTPException(status_code=400,
                            detail="最後の有効な管理者は削除できません。 / Cannot remove the last active admin.")
    with _lock:
        if action == "delete":
            con.execute("DELETE FROM users WHERE username=?", [username])
        elif action == "disable":
            con.execute("UPDATE users SET active=FALSE WHERE username=?", [username])
        elif action == "enable":
            con.execute("UPDATE users SET active=TRUE WHERE username=?", [username])
        elif action == "promote":
            con.execute("UPDATE users SET is_admin=TRUE WHERE username=?", [username])
        elif action == "demote":
            con.execute("UPDATE users SET is_admin=FALSE WHERE username=?", [username])
        elif action == "confirm":
            con.execute("UPDATE users SET confirmed=TRUE WHERE username=?", [username])
    # if you just revoked your own access, end the session
    if username == me and action in ("delete", "disable", "demote"):
        request.session.clear()
        return RedirectResponse("/login", status_code=303)
    return RedirectResponse("/admin/users", status_code=303)


# -------------------- admin: data table (view / edit / delete) --------------------
TREE_COLS = ["record_id", "created_at", "surveyor", "species_en", "species_ja", "latin",
             "lat", "lon", "gps_accuracy_m", "elevation_m", "slope_aspect", "dbh_cm",
             "height_m", "est_age_yr", "habitat", "health", "hollow", "mother_tree",
             "seeds_present", "seeds_collected", "saplings_nearby", "tagged",
             "wildlife_obs", "cultural_sacred", "wildlife_text", "notes", "photo_paths"]
EDIT_TEXT = ["species_en", "species_ja", "latin", "slope_aspect", "habitat", "health",
             "wildlife_text", "notes", "surveyor"]
EDIT_NUM = ["lat", "lon", "gps_accuracy_m", "elevation_m", "dbh_cm", "height_m"]
EDIT_INT = ["est_age_yr"]
EDIT_BOOL = ["hollow", "mother_tree", "seeds_present", "seeds_collected", "saplings_nearby",
             "tagged", "wildlife_obs", "cultural_sacred"]


@app.get("/admin/data", response_class=HTMLResponse)
def admin_data(request: Request, _: str = Depends(require_admin)):
    with _lock:
        rows = con.execute(f"SELECT {','.join(TREE_COLS)} FROM trees ORDER BY created_at DESC").fetchall()
    data = [dict(zip(TREE_COLS, r)) for r in rows]
    return templates.TemplateResponse(request, "data_table.html", {"rows": data, "total": len(data)})


@app.get("/admin/data/{rid}/edit", response_class=HTMLResponse)
def admin_data_edit(request: Request, rid: str, _: str = Depends(require_admin)):
    with _lock:
        r = con.execute(f"SELECT {','.join(TREE_COLS)} FROM trees WHERE record_id=?", [rid]).fetchone()
    if not r:
        raise HTTPException(status_code=404, detail="Not found")
    rec = dict(zip(TREE_COLS, r))
    return templates.TemplateResponse(request, "data_edit.html",
                                      {"r": rec, "text": EDIT_TEXT, "num": EDIT_NUM,
                                       "intf": EDIT_INT, "boolf": EDIT_BOOL})


@app.post("/admin/data/{rid}/edit")
async def admin_data_save(request: Request, rid: str, _: str = Depends(require_admin)):
    form = await request.form()
    sets, vals = [], []
    for f in EDIT_TEXT:
        sets.append(f"{f}=?"); vals.append(form.get(f, "") or None)
    for f in EDIT_NUM:
        sets.append(f"{f}=?"); vals.append(_num(form.get(f)))
    for f in EDIT_INT:
        sets.append(f"{f}=?"); vals.append(_inum(form.get(f)))
    for f in EDIT_BOOL:
        sets.append(f"{f}=?"); vals.append(form.get(f) is not None)
    vals.append(rid)
    with _lock:
        con.execute(f"UPDATE trees SET {','.join(sets)} WHERE record_id=?", vals)
    return RedirectResponse("/admin/data", status_code=303)


@app.post("/admin/data/{rid}/delete")
def admin_data_delete(request: Request, rid: str, _: str = Depends(require_admin)):
    import shutil
    with _lock:
        con.execute("DELETE FROM trees WHERE record_id=?", [rid])
    pdir = PHOTOS / rid
    if pdir.exists():
        shutil.rmtree(pdir, ignore_errors=True)
    return RedirectResponse("/admin/data", status_code=303)


# -------------------- exports --------------------
@app.get("/export.csv")
def export_csv(request: Request, _: str = Depends(require_admin)):
    out = DATA / "export.csv"
    with _lock:
        con.execute(f"COPY (SELECT * FROM trees ORDER BY created_at) TO '{out}' (HEADER, DELIMITER ',')")
    return FileResponse(out, filename="mitsue_trees.csv", media_type="text/csv")


@app.get("/export.parquet")
def export_parquet(request: Request, _: str = Depends(require_admin)):
    out = DATA / "export.parquet"
    with _lock:
        con.execute(f"COPY (SELECT * FROM trees ORDER BY created_at) TO '{out}' (FORMAT PARQUET)")
    return FileResponse(out, filename="mitsue_trees.parquet", media_type="application/octet-stream")


@app.get("/export.geojson")
def export_geojson(request: Request, _: str = Depends(require_admin)):
    with _lock:
        cur = con.execute("SELECT * FROM trees WHERE lat IS NOT NULL AND lon IS NOT NULL ORDER BY created_at")
        cols = [c[0] for c in cur.description]
        rows = cur.fetchall()
    feats = []
    for row in rows:
        r = dict(zip(cols, row))
        props = {k: (v.isoformat() if hasattr(v, "isoformat") else v)
                 for k, v in r.items() if k not in ("lat", "lon")}
        feats.append({"type": "Feature",
                      "geometry": {"type": "Point", "coordinates": [float(r["lon"]), float(r["lat"])]},
                      "properties": props})
    return JSONResponse({"type": "FeatureCollection", "features": feats},
                        headers={"Content-Disposition": 'attachment; filename="mitsue_trees.geojson"'})


@app.get("/export.gpkg")
def export_gpkg(request: Request, _: str = Depends(require_admin)):
    """GeoPackage (OGC .gpkg) — the native QGIS format: one file, typed fields,
    EPSG:4326 point layer 'mitsue_trees'. Built via DuckDB's spatial extension."""
    out = DATA / "mitsue_trees.gpkg"  # filename → QGIS layer name
    with _lock:
        con.execute("INSTALL spatial"); con.execute("LOAD spatial")
        try:
            out.unlink()
        except FileNotFoundError:
            pass
        con.execute("CREATE OR REPLACE TEMP TABLE mitsue_trees AS "
                    "SELECT *, ST_Point(lon, lat) AS geom FROM trees "
                    "WHERE lat IS NOT NULL AND lon IS NOT NULL ORDER BY created_at")
        con.execute(f"COPY mitsue_trees TO '{out}' "
                    "WITH (FORMAT GDAL, DRIVER 'GPKG', SRS 'EPSG:4326')")
    return FileResponse(out, filename="mitsue_trees.gpkg",
                        media_type="application/geopackage+sqlite3")


@app.get("/healthz")
def healthz():
    return {"ok": True}
