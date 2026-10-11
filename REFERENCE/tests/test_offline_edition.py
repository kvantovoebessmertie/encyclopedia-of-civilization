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
    assert manifest["record_count"] == len(records)
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

def test_offline_html_escapes_record_controlled_content(tmp_path):
    records = [{
        "record_id": 'claim-<script>alert("id")</script>',
        "record_version": '1&<img src=x onerror="alert(1)">',
        "record_type": 'claim"><script>alert("type")</script>',
        "publication_status": "draft",
        "content": {
            "statement": '</pre><script>alert("content")</script><pre>',
            "unicode": "Жизнь & знание — 東京",
            "quote": '"quoted" & apostrophe \'',
        },
    }]
    build_offline_edition(records, tmp_path / "safe", 'edition"><script>alert("edition")</script>')
    html = (tmp_path / "safe" / "index.html").read_text(encoding="utf-8")

    assert "<script>" not in html
    assert "</pre><script" not in html
    assert "<img src=x" not in html
    assert "&lt;script&gt;" in html
    assert "&lt;/pre&gt;" in html
    assert "&lt;img" in html
    assert "Жизнь &amp; знание — 東京" in html
    assert "alert(\\&quot;content\\&quot;)" in html

