from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any

def _canonical(record: dict[str, Any]) -> str:
    return json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def build_offline_edition(records: list[dict[str, Any]], output_dir: Path, edition_id: str = "encyclopedia-offline") -> dict[str, Any]:
    """Build deterministic static/offline and durable local representations."""
    output_dir.mkdir(parents=True, exist_ok=True)
    records_sorted = sorted(records, key=lambda r: (r["record_id"], r["record_version"]))
    data = output_dir / "records.json"
    data.write_text(json.dumps(records_sorted, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    jsonl = output_dir / "records.jsonl"
    jsonl.write_text("".join(_canonical(r) + "\n" for r in records_sorted), encoding="utf-8")
    md = output_dir / "README.md"
    md.write_text("# Энциклопедия цивилизации — offline edition\n\nEdition: " + edition_id + "\n\nRecords: " + str(len(records_sorted)) + "\n\nrecords.json is canonical; derived views are not a new normative source.\n", encoding="utf-8")
    html = output_dir / "index.html"
    rows = []
    for r in records_sorted:
        rows.append("<article><h2>" + r["record_id"] + "</h2><p><b>type:</b> " + r["record_type"] + " <b>version:</b> " + r["record_version"] + "</p><pre>" + json.dumps(r["content"], ensure_ascii=False, indent=2, sort_keys=True) + "</pre></article>")
    html.write_text("<!doctype html><meta charset='utf-8'><title>Энциклопедия цивилизации — offline</title><style>body{font-family:system-ui;max-width:1100px;margin:40px auto;padding:0 24px}article{break-inside:avoid-page;margin:0 0 40px}pre{white-space:pre-wrap}@media print{article{page-break-inside:avoid}body{max-width:none}}</style><h1>Энциклопедия цивилизации</h1><p>Offline edition: " + edition_id + "</p>" + "".join(rows), encoding="utf-8")
    db = output_dir / "records.sqlite3"
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE records(record_id TEXT NOT NULL, record_version TEXT NOT NULL, record_type TEXT NOT NULL, canonical_json TEXT NOT NULL, PRIMARY KEY(record_id, record_version))")
    con.executemany("INSERT INTO records VALUES(?,?,?,?)", [(r["record_id"], r["record_version"], r["record_type"], _canonical(r)) for r in records_sorted])
    con.commit(); con.close()
    files = [data, jsonl, md, html, db]
    manifest = {"edition_id": edition_id, "edition_version": "1.0", "network_required": False, "record_count": len(records_sorted), "canonical_source": "records.json", "durable_formats": ["json", "jsonl", "sqlite3"], "static_site": "index.html", "print_surface": "index.html", "files": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in files}, "epistemic_boundary": "offline packaging and integrity do not establish truth"}
    (output_dir / "edition-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest
