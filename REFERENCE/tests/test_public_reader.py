from __future__ import annotations

import json

import pytest

from encyclopedia_reference.public_reader import build_public_preview


def _manifest():
    return {
        "edition_id": "private-demo",
        "edition_state": "preview",
        "source_revision": "synthetic-fixture-only",
        "builder_version": "test",
        "selection_policy_version": "preview-only-v1",
        "records": [
            {
                "record_id": "CLAIM-DEMO-1",
                "record_version": "1",
                "review_state": "preview_only",
                "preview_note": "Synthetic; not approved for publication.",
            }
        ],
    }


def _records():
    return [
        {
            "record_id": "CLAIM-DEMO-1",
            "record_version": "1",
            "record_type": "claim",
            "publication_status": "draft",
            "content": {
                "statement": '</pre><script>alert("x")</script>',
                "unicode": "Знание & проверка — 東京",
            },
        },
        {
            "record_id": "UNSELECTED-SECRET",
            "record_version": "9",
            "record_type": "claim",
            "publication_status": "draft",
            "content": {"statement": "must not appear"},
        },
    ]


def test_preview_includes_only_exact_manifest_allowlist(tmp_path):
    manifest = build_public_preview(_records(), _manifest(), tmp_path / "preview")
    page = (tmp_path / "preview" / "index.html").read_text(encoding="utf-8")
    assert manifest["record_count"] == 1
    assert manifest["selected_records"] == [
        {"record_id": "CLAIM-DEMO-1", "record_version": "1"}
    ]
    assert "UNSELECTED-SECRET" not in page
    assert "must not appear" not in page
    assert "CLAIM-DEMO-1" in page


def test_reader_renders_claim_statement_separately_from_technical_json(tmp_path):
    records = _records()
    records[0]["content"]["claim_type"] = "documented_fact"
    build_public_preview(records, _manifest(), tmp_path / "preview")
    page = (tmp_path / "preview" / "index.html").read_text(encoding="utf-8")
    assert '<section class="semantic"><h3>Reader view</h3>' in page
    assert '<p class="statement">&lt;/pre&gt;&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;</p>' in page
    assert "<b>Claim type:</b> documented_fact" in page
    assert "Record content (technical view)" in page


def test_preview_escapes_untrusted_record_content(tmp_path):
    build_public_preview(_records(), _manifest(), tmp_path / "preview")
    page = (tmp_path / "preview" / "index.html").read_text(encoding="utf-8")
    assert '</pre><script>alert("x")</script>' not in page
    assert "&lt;/pre&gt;&lt;script&gt;" in page
    assert "Знание &amp; проверка — 東京" in page
    assert "not a truth rating" in page
    assert "not a public edition" in page
    assert "script-src \'self\'" in page
    assert '<script src="search.js" defer></script>' in page
    assert "<script>const q=" not in page
    search_script = (tmp_path / "preview" / "search.js").read_text(encoding="utf-8")
    assert "innerHTML" not in search_script
    assert "alert" not in search_script


def test_preview_refuses_released_state(tmp_path):
    manifest = _manifest()
    manifest["edition_state"] = "released"
    with pytest.raises(ValueError, match="preview state only"):
        build_public_preview(_records(), manifest, tmp_path / "preview")


def test_preview_refuses_missing_selected_version(tmp_path):
    manifest = _manifest()
    manifest["records"][0]["record_version"] = "missing"
    with pytest.raises(ValueError, match="not found"):
        build_public_preview(_records(), manifest, tmp_path / "preview")


def test_preview_manifest_is_written_and_deterministic(tmp_path):
    first = build_public_preview(_records(), _manifest(), tmp_path / "a")
    second = build_public_preview(_records(), _manifest(), tmp_path / "b")
    assert first == second
    assert json.loads((tmp_path / "a" / "preview-manifest.json").read_text()) == first
    assert (tmp_path / "a" / "index.html").read_bytes() == (tmp_path / "b" / "index.html").read_bytes()
    assert (tmp_path / "a" / "search.js").read_bytes() == (tmp_path / "b" / "search.js").read_bytes()
    assert first["search_js_sha256"]
