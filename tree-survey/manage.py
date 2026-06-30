"""Admin CLI for the Mitsue tree-survey app.

Usage (inside the venv):
  python manage.py adduser  <username> <password> ["Display Name"] [--admin]
  python manage.py listusers
  python manage.py deluser  <username>
  python manage.py stats
  python manage.py export   <out.csv|out.parquet|out.geojson>
"""
import sys
import app  # reuses the same DuckDB connection + helpers


def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    cmd = sys.argv[1]

    if cmd == "adduser":
        username, password = sys.argv[2], sys.argv[3]
        display = sys.argv[4] if len(sys.argv) > 4 and not sys.argv[4].startswith("--") else username
        is_admin = "--admin" in sys.argv
        app.add_user(username, password, display, is_admin)
        print(f"OK: user '{username}' (admin={is_admin})")

    elif cmd == "deluser":
        with app._lock:
            app.con.execute("DELETE FROM users WHERE username=?", [sys.argv[2]])
        print(f"Deleted '{sys.argv[2]}'")

    elif cmd == "listusers":
        with app._lock:
            for u in app.con.execute("SELECT username, display_name, is_admin, created_at FROM users ORDER BY username").fetchall():
                print(f"  {u[0]:<16} {u[1]:<20} admin={u[2]}  {u[3]}")

    elif cmd == "stats":
        with app._lock:
            n = app.con.execute("SELECT count(*) FROM trees").fetchone()[0]
            m = app.con.execute("SELECT count(*) FROM trees WHERE mother_tree").fetchone()[0]
            g = app.con.execute("SELECT count(*) FROM trees WHERE lat IS NOT NULL").fetchone()[0]
        print(f"Records: {n}   Mother trees: {m}   With GPS: {g}")

    elif cmd == "export":
        out = sys.argv[2]
        fmt = "PARQUET" if out.endswith(".parquet") else None
        with app._lock:
            if out.endswith(".geojson"):
                import json
                cur = app.con.execute("SELECT * FROM trees WHERE lat IS NOT NULL ORDER BY created_at")
                cols = [c[0] for c in cur.description]
                feats = []
                for row in cur.fetchall():
                    r = dict(zip(cols, row))
                    feats.append({"type": "Feature",
                                  "geometry": {"type": "Point", "coordinates": [float(r["lon"]), float(r["lat"])]},
                                  "properties": {k: (v.isoformat() if hasattr(v, "isoformat") else v)
                                                 for k, v in r.items() if k not in ("lat", "lon")}})
                open(out, "w").write(json.dumps({"type": "FeatureCollection", "features": feats}, ensure_ascii=False, indent=2))
            elif fmt:
                app.con.execute(f"COPY (SELECT * FROM trees ORDER BY created_at) TO '{out}' (FORMAT PARQUET)")
            else:
                app.con.execute(f"COPY (SELECT * FROM trees ORDER BY created_at) TO '{out}' (HEADER, DELIMITER ',')")
        print(f"Wrote {out}")

    else:
        print(__doc__)


if __name__ == "__main__":
    main()
