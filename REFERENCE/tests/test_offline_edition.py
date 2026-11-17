from __future__ import annotations

import json
import os
import re
import sqlite3
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest

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


class _Structure(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags, self.attrs, self.comments, self.other = [], [], [], []
        self.stack, self.text = [], {}

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.attrs.extend((tag, name, value) for name, value in attrs)
        self.stack.append(tag)

    handle_startendtag = handle_starttag

    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack.pop() != tag:
                pass

    def handle_comment(self, data):
        self.comments.append(data)

    def handle_decl(self, decl):
        self.other.append(decl)

    def handle_pi(self, data):
        self.other.append(data)

    def handle_data(self, data):
        if self.stack:
            self.text.setdefault(self.stack[-1], []).append(data)


ALLOWED_TAGS = {"meta", "title", "style", "h1", "p", "article", "h2", "b", "pre"}

HOSTILE_STRINGS = [
    '<script>alert("s")</script>', "<SCRIPT SRC=//x>", "<ScRiPt>x</sCrIpT>",
    "<img src=x onerror=alert(1)>", "<IMG SRC=x ONERROR=alert(1)>", "<iMg/OnLoAd=1>",
    "<svg onload=alert(1)>", "<SVG/ONLOAD=1>", "<iframe src=javascript:alert(1)>", "<IFRAME SRCDOC='x'>",
    "</pre><script>x</script><pre>", "</style><script>x</script>", "</STYLE ><b>x", "</title><script>x</script>",
    "</TITLE><img src=x>", "<!-- c --><!--", "-->", "<![CDATA[x]]>", "<?php x ?>", "<!DOCTYPE x>",
    "it's \" & ' `", "' onmouseover='alert(1)", '" autofocus onfocus="alert(1)',
    "&lt;script&gt; &amp;amp; &#60;img&#62;", "Жизнь & знание — 東京",
]


def _hostile_records():
    records = []
    for n, payload in enumerate(HOSTILE_STRINGS):
        records.append({
            "record_id": f"id{n:02d}-{payload}",
            "record_version": payload if n % 2 else n,
            "record_type": f"type-{payload}",
            "content": {
                payload: payload,
                "list": [payload, None, True, 1.5, {payload: [payload]}],
                "none": None, "bool": False, "int": n, "float": 0.5,
            },
        })
    return records


def test_offline_html_escapes_record_controlled_content(tmp_path):
    records = _hostile_records()
    build_offline_edition(records, tmp_path / "safe", "edition-1.0_x")
    html = (tmp_path / "safe" / "index.html").read_text(encoding="utf-8")

    parsed = _Structure()
    parsed.feed(html)
    parsed.close()

    assert set(parsed.tags) <= ALLOWED_TAGS, sorted(set(parsed.tags) - ALLOWED_TAGS)
    assert not {"script", "img", "svg", "iframe", "a", "link", "base", "object", "embed"} & set(parsed.tags)
    assert parsed.attrs == [("meta", "charset", "utf-8")]
    assert not [a for a in parsed.attrs if a[1].lower().startswith("on")]
    assert parsed.comments == [] and parsed.other == ["doctype html"]
    assert parsed.tags.count("article") == len(records)
    assert parsed.tags.count("h2") == len(records)
    assert parsed.tags.count("pre") == len(records)
    assert parsed.tags.count("style") == 1 and parsed.tags.count("title") == 1
    assert "".join(parsed.text["title"]) == "Энциклопедия цивилизации — offline"
    assert "<" not in "".join(parsed.text["style"])

    # Round trip: parsed text equals the original record-controlled values.
    expected = sorted(records, key=lambda r: (r["record_id"], r["record_version"]))
    assert parsed.text["h2"] == [r["record_id"] for r in expected]
    assert [json.loads(t) for t in parsed.text["pre"]] == [r["content"] for r in expected]
    p_text = "".join(parsed.text["p"])
    for r in records:
        assert r["record_type"] in p_text
        assert str(r["record_version"]) in p_text
    assert "edition-1.0_x" in p_text


def test_canonical_outputs_remain_unescaped_by_html_handling(tmp_path):
    records = _hostile_records()
    out = tmp_path / "canon"
    build_offline_edition(records, out, "canon-1")
    expected = sorted(records, key=lambda r: (r["record_id"], r["record_version"]))

    assert json.loads((out / "records.json").read_text(encoding="utf-8")) == expected
    lines = (out / "records.jsonl").read_text(encoding="utf-8").splitlines()
    assert [json.loads(line) for line in lines] == expected
    con = sqlite3.connect(out / "records.sqlite3")
    rows = con.execute("SELECT record_id, record_version, record_type, canonical_json FROM records ORDER BY record_id, record_version").fetchall()
    con.close()
    assert [json.loads(row[3]) for row in rows] == expected
    assert sorted(row[0] for row in rows) == sorted(r["record_id"] for r in records)
    for name in ("records.json", "records.jsonl"):
        raw = (out / name).read_text(encoding="utf-8")
        assert "<script>" in raw and "&lt;" in raw  # literal hostile input is preserved, not HTML-escaped
        assert "&lt;script&gt; &amp;amp;" in raw  # literal text, not double-escaped


def test_canonical_outputs_do_not_depend_on_html_rendering(tmp_path):
    records = _hostile_records()
    build_offline_edition(records, tmp_path / "a", "same-1")
    build_offline_edition(records, tmp_path / "b", "other-2")
    for name in ("records.json", "records.jsonl", "records.sqlite3"):
        assert (tmp_path / "a" / name).read_bytes() == (tmp_path / "b" / name).read_bytes()


@pytest.mark.parametrize("edition_id", [
    "encyclopedia-offline", "encyclopedia-4686-09", "full-corpus-offline-v1", "same", "a", "A.b_c-9", "x" * 128,
])
def test_edition_id_accepts_documented_identifiers(tmp_path, edition_id):
    manifest = build_offline_edition(_records()[:1], tmp_path / "ok", edition_id)
    assert manifest["edition_id"] == edition_id
    assert f"\nEdition: {edition_id}\n" in (tmp_path / "ok" / "README.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("edition_id", [
    "", " ", "x" * 129, "-leading", ".leading", "_leading", "with space", "tab\t", "new\nline", "trail\n",
    "a\r\nb", 'ed"><script>alert(1)</script>', "<img src=x onerror=alert(1)>", "[x](javascript:alert(1))",
    "![i](http://x)", "<!-- c -->", "a&b", "a'b", "a`b", "a/b", "a\\b", "../x", "a:b", "a|b", "a#b",
    "Энциклопедия", "ａbc", "a\u202eb", "a\u2028b", "a\x00b", None, 1, b"bytes", ["a"],
])
def test_edition_id_rejects_unsafe_values_before_writing(tmp_path, edition_id):
    out = tmp_path / "rejected"
    with pytest.raises(ValueError, match="invalid edition_id"):
        build_offline_edition(_records()[:1], out, edition_id)
    assert not out.exists()


def test_cli_rejects_invalid_edition_id(tmp_path):
    script = ROOT / "REFERENCE" / "build_offline_edition.py"
    env = {**os.environ, "PYTHONPATH": str(ROOT / "REFERENCE" / "src")}
    bad = subprocess.run(
        [sys.executable, str(script), "--output", str(tmp_path / "o"), "--edition-id", "<script>"],
        capture_output=True, text=True, env=env,
    )
    assert bad.returncode == 2 and "invalid edition_id" in bad.stderr
    assert not (tmp_path / "o").exists()
