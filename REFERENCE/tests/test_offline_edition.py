from __future__ import annotations

import importlib.util
import json
import re
import sqlite3
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest

from encyclopedia_reference.offline_edition import build_offline_edition, validate_edition_id

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"


class _GeneratedHTMLStructure(HTMLParser):
    """Reject unexpected markup, attributes, comments and malformed nesting."""

    ALLOWED_TAGS = {"meta", "title", "style", "h1", "p", "article", "h2", "b", "pre"}
    VOID_TAGS = {"meta"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in self.ALLOWED_TAGS:
            self.errors.append(f"unexpected start tag: {tag}")
        if tag == "meta":
            if attrs != [("charset", "utf-8")]:
                self.errors.append(f"unexpected meta attributes: {attrs!r}")
        elif attrs:
            self.errors.append(f"attributes are not allowed on {tag}: {attrs!r}")
        if tag not in self.VOID_TAGS:
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID_TAGS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag not in self.ALLOWED_TAGS or tag in self.VOID_TAGS:
            self.errors.append(f"unexpected end tag: {tag}")
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"unbalanced end tag: {tag}")
            return
        self.stack.pop()

    def handle_comment(self, data: str) -> None:
        self.errors.append("HTML comments are not allowed")

    def handle_decl(self, decl: str) -> None:
        if decl.lower() != "doctype html":
            self.errors.append(f"unexpected declaration: {decl}")

    def unknown_decl(self, data: str) -> None:
        self.errors.append(f"unexpected declaration: {data}")


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*/records/*.json"))]


def _assert_safe_generated_html(html: str) -> None:
    parser = _GeneratedHTMLStructure()
    parser.feed(html)
    parser.close()
    assert parser.errors == []
    assert parser.stack == []


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
    _assert_safe_generated_html(html)
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


def test_offline_html_rejects_structural_injection_and_preserves_canonical_data(tmp_path):
    hostile_key = '</pre><ScRiPt>alert("key")</ScRiPt><!-- key -->'
    hostile_value = (
        '</pre><script>alert("content")</script><pre><!-- comment -->'
        '</style><img src=x onerror="alert(1)"><svg onload="alert(2)">'
        '</svg><iframe src="https://example.invalid"></iframe></title>'
    )
    records = [{
        "record_id": 'claim-<ScRiPt>alert("id")</ScRiPt>',
        "record_version": 7,
        "record_type": 'claim"><img src=x onerror="alert(3)">',
        "publication_status": "draft",
        "content": {
            hostile_key: hostile_value,
            "unicode": "Жизнь & знание — 東京",
            "quote": '"quoted" & apostrophe \'',
            "non_string_values": [1, False, None, {"nested": 3.5}],
        },
    }]
    out = tmp_path / "safe"
    build_offline_edition(records, out, "safe-edition_1.0")
    html = (out / "index.html").read_text(encoding="utf-8")
    _assert_safe_generated_html(html)
    assert "<script" not in html.lower()
    assert "<img" not in html.lower()
    assert "<svg" not in html.lower()
    assert "<iframe" not in html.lower()
    assert "<!--" not in html
    assert "Жизнь &amp; знание — 東京" in html
    assert "&lt;/style&gt;" in html
    assert "&lt;/title&gt;" in html

    # Presentation escaping must never mutate the canonical machine-readable records.
    assert json.loads((out / "records.json").read_text(encoding="utf-8")) == records
    jsonl_rows = [json.loads(line) for line in (out / "records.jsonl").read_text(encoding="utf-8").splitlines()]
    assert jsonl_rows == records
    con = sqlite3.connect(out / "records.sqlite3")
    stored = con.execute("SELECT canonical_json FROM records").fetchone()[0]
    con.close()
    assert json.loads(stored) == records[0]
    assert json.loads(stored)["content"][hostile_key] == hostile_value


@pytest.mark.parametrize(
    "edition_id",
    ["encyclopedia-offline", "encyclopedia-4686-09", "full-corpus-offline-v1", "same", "A", "a._-9", "A" * 128],
)
def test_validate_edition_id_accepts_compatible_identifiers(edition_id):
    assert validate_edition_id(edition_id) == edition_id


@pytest.mark.parametrize(
    "edition_id",
    ["", " leading", "has space", "<script>", "a/b", "a\\b", "éclair", "١", "_starts-wrong", ".starts-wrong", "-starts-wrong", "A" * 129, None, 7, True],
)
def test_validate_edition_id_rejects_invalid_identifiers(edition_id):
    with pytest.raises(ValueError, match="edition_id must be"):
        validate_edition_id(edition_id)


def test_invalid_edition_id_fails_before_creating_output_directory(tmp_path):
    out = tmp_path / "not-created" / "offline"
    with pytest.raises(ValueError, match="edition_id must be"):
        build_offline_edition([], out, "../unsafe")
    assert not out.exists()
    assert not out.parent.exists()


def test_cli_reports_invalid_edition_id_before_loading_records_or_writing(tmp_path, monkeypatch, capsys):
    cli_path = ROOT / "REFERENCE" / "build_offline_edition.py"
    spec = importlib.util.spec_from_file_location("build_offline_edition", cli_path)
    assert spec is not None and spec.loader is not None
    cli_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli_module)
    monkeypatch.setattr(sys, "argv", ["build_offline_edition.py", "--output", str(tmp_path / "not-created"), "--edition-id", "bad id"])
    with pytest.raises(SystemExit) as exc:
        cli_module.main()
    assert exc.value.code == 2
    assert "edition_id must be" in capsys.readouterr().err
    assert not (tmp_path / "not-created").exists()
