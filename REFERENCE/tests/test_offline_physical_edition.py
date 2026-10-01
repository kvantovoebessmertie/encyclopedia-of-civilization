from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.offline_edition import build_offline_edition

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"

def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*/records/*.json"))]

def test_full_corpus_offline_edition_is_static_and_durable(tmp_path):
    records = _records()
    m = build_offline_edition(records, tmp_path / "edition", "encyclopedia-4686-09")
    assert m["network_required"] is False
    assert m["record_count"] == len(records) == 1782
    assert set(m["durable_formats"]) == {"json", "jsonl", "sqlite3"}
    assert (tmp_path / "edition" / "index.html").is_file()
    db = sqlite3.connect(tmp_path / "edition" / "records.sqlite3")
    assert db.execute("select count(*) from records").fetchone()[0] == 1782
    db.close()

def test_offline_edition_recovers_canonical_identity_and_versions(tmp_path):
    records = _records()
    out = tmp_path / "edition"
    build_offline_edition(records, out)
    recovered = json.loads((out / "records.json").read_text(encoding="utf-8"))
    assert [(r["record_id"], r["record_version"]) for r in recovered] == sorted((r["record_id"], r["record_version"]) for r in records)
    assert all(r.get("provenance") is not None for r in recovered)

def test_content_package_and_offline_edition_are_complementary(tmp_path):
    records = _records()
    report = build_content_package(records, package_dir=tmp_path / "package", schema_path=SCHEMA, package_id="full-corpus-1782")
    edition = build_offline_edition(records, tmp_path / "edition")
    assert report["integrity_and_validation"] == "PASS"
    assert report["network_required"] is False
    assert edition["network_required"] is False
    assert report["recovered_record_count"] == edition["record_count"] == 1782
