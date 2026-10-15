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


def test_reader_links_evidence_references_only_to_selected_records(tmp_path):
    records = [
        {
            "record_id": "CLAIM-DEMO-1",
            "record_version": "1",
            "record_type": "claim",
            "publication_status": "draft",
            "content": {"statement": "A safe demonstration claim.", "claim_type": "documented_fact"},
        },
        {
            "record_id": "EU-DEMO-1",
            "record_version": "1",
            "record_type": "evidence_use",
            "publication_status": "draft",
            "content": {
                "claim_ref": {"record_id": "CLAIM-DEMO-1", "version": "1"},
                "source_ref": {"record_id": "SRC-DEMO-1", "version": "1"},
                "evidence_role": "supports",
                "material": {"description": "Synthetic evidence note."},
            },
        },
        {
            "record_id": "SRC-DEMO-1",
            "record_version": "1",
            "record_type": "source",
            "publication_status": "draft",
            "content": {
                "source_identity": "Synthetic source",
                "external_ref": {"uri": "https://example.org/source"},
            },
        },
    ]
    manifest = _manifest()
    manifest["records"] = [
        {"record_id": record["record_id"], "record_version": "1",
         "review_state": "preview_only", "preview_note": "Synthetic test fixture only."}
        for record in records
    ]
    build_public_preview(records, manifest, tmp_path / "preview")
    page = (tmp_path / "preview" / "index.html").read_text(encoding="utf-8")
    assert 'href="#record-0">CLAIM-DEMO-1 @ 1</a>' in page
    assert 'href="#record-2">SRC-DEMO-1 @ 1</a>' in page
    assert 'href="https://example.org/source"' in page



def test_reader_renders_context_and_scope_limits(tmp_path):
    records = [
        {
            "record_id": "CTX-DEMO-1",
            "record_version": "1",
            "record_type": "context",
            "publication_status": "draft",
            "content": {
                "context_content": "Applies only to the stated context.",
                "target_ref": {"record_id": "CLAIM-DEMO-1", "version": "1"},
                "epistemic_status": "known",
            },
        },
        {
            "record_id": "SCP-DEMO-1",
            "record_version": "1",
            "record_type": "scope",
            "publication_status": "draft",
            "content": {
                "scope_content": "Not a complete reference or universal rule.",
                "target_ref": {"record_id": "CLAIM-DEMO-1", "version": "1"},
            },
        },
    ]
    manifest = _manifest()
    manifest["records"] = [
        {
            "record_id": record["record_id"],
            "record_version": record["record_version"],
            "review_state": "preview_only",
            "preview_note": "Synthetic test fixture only.",
        }
        for record in records
    ]
    build_public_preview(records, manifest, tmp_path / "preview")
    page = (tmp_path / "preview" / "index.html").read_text(encoding="utf-8")
    assert "<b>Context:</b> Applies only to the stated context." in page
    assert "<b>Scope:</b> Not a complete reference or universal rule." in page
    assert "<b>Epistemic status:</b> known" in page
    assert "CLAIM-DEMO-1 @ 1" in page

def test_preview_escapes_untrusted_record_content(tmp_path):
    build_public_preview(_records(), _manifest(), tmp_path / "preview")
    page = (tmp_path / "preview" / "index.html").read_text(encoding="utf-8")
    assert '</pre><script>alert("x")</script>' not in page
    assert "&lt;/pre&gt;&lt;script&gt;" in page
    assert "Знание &amp; проверка — 東京" in page
    assert "not a truth rating" in page
    assert "<b>Review state:</b> preview_only" in page
    assert "preview-only; not editorial approval" in page
    assert '<html lang="ru">' in page
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

def test_reader_never_turns_non_http_source_uris_into_links(tmp_path):
    records = [
        {
            "record_id": "SRC-UNTRUSTED-1",
            "record_version": "1",
            "record_type": "source",
            "publication_status": "draft",
            "content": {
                "source_identity": "Synthetic untrusted URI",
                "external_ref": {"uri": "javascript:alert(1)"},
            },
        },
        {
            "record_id": "SRC-UNTRUSTED-2",
            "record_version": "1",
            "record_type": "source",
            "publication_status": "draft",
            "content": {
                "source_identity": "Synthetic protocol-relative URI",
                "external_ref": {"uri": "//example.org/unsafe"},
            },
        },
    ]
    manifest = _manifest()
    manifest["records"] = [
        {
            "record_id": record["record_id"],
            "record_version": record["record_version"],
            "review_state": "preview_only",
            "preview_note": "Synthetic security test only.",
        }
        for record in records
    ]
    build_public_preview(records, manifest, tmp_path / "preview")
    page = (tmp_path / "preview" / "index.html").read_text(encoding="utf-8")
    assert 'href="javascript:alert(1)"' not in page
    assert 'href="//example.org/unsafe"' not in page
    assert "javascript:alert(1)" in page
    assert "//example.org/unsafe" in page
