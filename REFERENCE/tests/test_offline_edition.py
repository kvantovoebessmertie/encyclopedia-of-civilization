from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path

from encyclopedia_reference.offline_edition import build_offline_edition

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*/records/*.json"))]


def test_full_corpus_offline_edition_is_self_contained(tmp_path):
    records = _records()
    out = tmp_path / "offline"
    manifest = build_offline_edition(records, out, "full-corpus-offline-v1")
    assert manifest["network_required"] is False
    assert manifest["record_count"] == 2547
    for name in ("index.html", "records.json", "records.jsonl", "records.sqlite3", "edition-manifest.json"):
        assert (out / name).is_file()
    html = (out / "index.html").read_text(encoding="utf-8")
    external_resources = re.findall(r"(?i)\b(?:src|href)\s*=\s*['\"]https?://", html)
    assert external_resources == []
    con = sqlite3.connect(out / "records.sqlite3")
    assert con.execute("SELECT COUNT(*) FROM records").fetchone()[0] == len(records)
    con.close()
    built = json.loads((out / "records.json").read_text(encoding="utf-8"))
    assert len(built) == len(records)


def test_offline_edition_manifest_is_deterministic(tmp_path):
    records = _records()
    a = build_offline_edition(records, tmp_path / "a", "same")
    b = build_offline_edition(records, tmp_path / "b", "same")
    assert a == b
    assert (tmp_path / "a" / "records.json").read_bytes() == (tmp_path / "b" / "records.json").read_bytes()
    assert (tmp_path / "a" / "records.jsonl").read_bytes() == (tmp_path / "b" / "records.jsonl").read_bytes()
