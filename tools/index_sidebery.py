#!/usr/bin/env python3
"""Index the 5 most recent Sidebery tab-snapshot JSON files into DuckDB (deduped by URL)."""
import json
import glob
import os
import duckdb

SRC_DIR = "/home/rob/Sidebery"
DB_PATH = os.path.join(os.path.dirname(__file__), "sidebery_index.duckdb")
N_LATEST = 5


def flatten_tabs(node):
    """tabs nesting depth varies (window->tabs or window->group->tabs); walk until dicts."""
    if isinstance(node, dict):
        if node.get("url"):
            yield node
        return
    if isinstance(node, list):
        for child in node:
            yield from flatten_tabs(child)


def iter_snapshots(path):
    d = json.load(open(path))
    if "snapshots" in d:
        for snap in d["snapshots"]:
            yield snap.get("id"), snap.get("time"), snap.get("tabs", [])
    else:
        yield d.get("id"), d.get("time"), d.get("tabs", [])


def main():
    paths = sorted(glob.glob(os.path.join(SRC_DIR, "*.json")), key=os.path.getmtime, reverse=True)[:N_LATEST]

    rows = []
    for path in paths:
        fname = os.path.basename(path)
        for snap_id, snap_time, tabs in iter_snapshots(path):
            for win_idx, window in enumerate(tabs):
                for tab_idx, tab in enumerate(flatten_tabs(window)):
                    rows.append((
                        fname, snap_id, snap_time, win_idx, tab_idx,
                        tab.get("url"), tab.get("title"),
                        tab.get("panelId"), bool(tab.get("pinned")),
                    ))

    con = duckdb.connect(DB_PATH)
    con.execute("""
        CREATE OR REPLACE TABLE tabs_raw (
            source_file TEXT, snapshot_id TEXT, snapshot_time BIGINT,
            window_idx INT, tab_idx INT,
            url TEXT, title TEXT, panel_id TEXT, pinned BOOLEAN
        )
    """)
    con.executemany("INSERT INTO tabs_raw VALUES (?,?,?,?,?,?,?,?,?)", rows)

    # Dedup: keep one row per URL, the most recent snapshot_time
    con.execute("""
        CREATE OR REPLACE TABLE tabs AS
        SELECT * FROM (
            SELECT *, ROW_NUMBER() OVER (PARTITION BY url ORDER BY snapshot_time DESC) AS rn
            FROM tabs_raw
        ) WHERE rn = 1
    """)
    con.execute("ALTER TABLE tabs DROP COLUMN rn")
    con.execute("""
        CREATE OR REPLACE VIEW tabs_dated AS
        SELECT *, to_timestamp(snapshot_time / 1000) AS snapshot_date FROM tabs
    """)

    total = con.execute("SELECT COUNT(*) FROM tabs_raw").fetchone()[0]
    deduped = con.execute("SELECT COUNT(*) FROM tabs").fetchone()[0]
    print(f"Files used ({len(paths)}): {[os.path.basename(p) for p in paths]}")
    print(f"{total} raw tab rows -> {deduped} unique URLs indexed into {DB_PATH}")
    con.close()


if __name__ == "__main__":
    main()
