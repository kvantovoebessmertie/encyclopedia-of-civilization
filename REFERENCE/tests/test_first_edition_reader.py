from __future__ import annotations

import json

import pytest

from encyclopedia_reference.first_edition import FIRST_EDITION_CHAPTER_IDS
from encyclopedia_reference.first_edition_reader import build_first_edition_reader


def record(record_id, record_type, content, provenance=None):
    return {
        "record_id": record_id,
        "record_version": "1",
        "record_type": record_type,
        "type_version": "1.0",
        "schema": "record/0.1",
        "content": content,
        "provenance": provenance or {},
        "publication_status": "published",
        "completion_status": "complete",
    }


def pin(record_id, record_type):
    return {
        "record_id": record_id,
        "record_version": "1",
        "record_type": record_type,
        "type_version": "1.0",
        "schema": "record/0.1",
    }


def entry(record_id, record_type, dependencies=()):
    return {
        **pin(record_id, record_type),
        "decision": "INCLUDE",
        "approval": {
            "status": "APPROVED",
            "approver": "SYNTHETIC-TEST-OWNER",
            "reference": "SYNTHETIC-TEST-DECISION",
        },
        "dependencies": list(dependencies),
    }


def fixtures():
    source = record(
        "SRC-A",
        "source",
        {
            "source_identity": "Synthetic source",
            "external_ref": {"uri": "https://example.invalid/source"},
        },
    )
    claim = record(
        "CLM-A",
        "claim",
        {"statement": "A selected synthetic claim."},
        {"created_from": [{"record_id": "SRC-A", "version": "1"}]},
    )
    evidence = record(
        "EU-A",
        "evidence_use",
        {
            "claim_ref": {"record_id": "CLM-A", "version": "1"},
            "source_ref": {"record_id": "SRC-A", "version": "1"},
            "evidence_role": "supports",
            "material": {
                "description": "A bounded synthetic evidence description.",
                "locator": "Section 1",
            },
        },
        {"created_from": [{"record_id": "SRC-A", "version": "1"}]},
    )
    unselected = record(
        "CLM-NOT-SELECTED",
        "claim",
        {"statement": "This claim must never render."},
    )
    records = [claim, evidence, source, unselected]
    selection = {
        "schema_version": "1.1",
        "records": [
            entry("CLM-A", "claim", [pin("SRC-A", "source")]),
            entry("SRC-A", "source"),
            entry("EU-A", "evidence_use", [pin("CLM-A", "claim"), pin("SRC-A", "source")]),
        ],
    }
    chapters = [
        {"chapter_id": chapter_id, "title": f"Chapter {index}", "claim_refs": []}
        for index, chapter_id in enumerate(FIRST_EDITION_CHAPTER_IDS, start=1)
    ]
    chapters[0]["claim_refs"] = [{"record_id": "CLM-A", "record_version": "1"}]
    chapter_map = {
        "schema_version": "1.0",
        "status": "approved",
        "approval": {
            "status": "APPROVED",
            "approver": "SYNTHETIC-TEST-EDITOR",
            "reference": "SYNTHETIC-CHAPTER-MAP-DECISION",
        },
        "chapters": chapters,
    }
    return records, selection, chapter_map


def test_builds_chapter_reader_from_exact_approved_selection(tmp_path):
    records, selection, chapter_map = fixtures()
    manifest = build_first_edition_reader(
        records, selection, chapter_map, tmp_path / "reader",
        source_commit="a" * 40,
    )
    page = (tmp_path / "reader" / "index.html").read_text(encoding="utf-8")
    assert manifest["article_count"] == 1
    assert manifest["chapter_count"] == 19
    assert manifest["selected_record_count"] == 3
    assert "A selected synthetic claim." in page
    assert "A bounded synthetic evidence description." in page
    assert "Synthetic source" in page
    assert "This claim must never render." not in page
    assert page.count("<article ") == 1
    saved = json.loads((tmp_path / "reader" / "reader-manifest.json").read_text(encoding="utf-8"))
    assert saved == manifest


def test_rejects_unapproved_template_before_writing(tmp_path):
    records, selection, chapter_map = fixtures()
    chapter_map["status"] = "template_not_approved"
    output = tmp_path / "reader"
    with pytest.raises(ValueError, match="status 'approved'"):
        build_first_edition_reader(records, selection, chapter_map, output, source_commit="b" * 40)
    assert not output.exists()


def test_rejects_missing_chapter_map_attestation(tmp_path):
    records, selection, chapter_map = fixtures()
    chapter_map.pop("approval")
    with pytest.raises(ValueError, match="approval attestation"):
        build_first_edition_reader(records, selection, chapter_map, tmp_path / "reader", source_commit="c" * 40)


def test_rejects_hold_even_if_chapter_map_assigns_claim(tmp_path):
    records, selection, chapter_map = fixtures()
    selection["records"][0]["decision"] = "HOLD"
    with pytest.raises(ValueError, match="not approved"):
        build_first_edition_reader(records, selection, chapter_map, tmp_path / "reader", source_commit="d" * 40)


def test_rejects_non_claim_article_assignment(tmp_path):
    records, selection, chapter_map = fixtures()
    chapter_map["chapters"][1]["claim_refs"] = [{"record_id": "EU-A", "record_version": "1"}]
    with pytest.raises(ValueError, match="only selected Claim"):
        build_first_edition_reader(records, selection, chapter_map, tmp_path / "reader", source_commit="e" * 40)


def test_rejects_nonempty_output_directory(tmp_path):
    records, selection, chapter_map = fixtures()
    output = tmp_path / "reader"
    output.mkdir()
    (output / "stale.txt").write_text("stale", encoding="utf-8")
    with pytest.raises(ValueError, match="must be empty"):
        build_first_edition_reader(records, selection, chapter_map, output, source_commit="f" * 40)
    assert (output / "stale.txt").read_text(encoding="utf-8") == "stale"
