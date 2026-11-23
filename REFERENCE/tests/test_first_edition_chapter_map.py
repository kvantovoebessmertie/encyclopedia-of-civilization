from __future__ import annotations

import copy

import pytest

from encyclopedia_reference.first_edition import (
    FIRST_EDITION_CHAPTER_IDS,
    validate_first_edition_chapter_map,
)


def _records():
    return [
        {"record_id": "CLM-A", "record_version": "1", "record_type": "claim"},
        {"record_id": "CLM-B", "record_version": "2", "record_type": "claim"},
        {"record_id": "EU-A", "record_version": "1", "record_type": "evidence_use"},
        {"record_id": "SRC-A", "record_version": "1", "record_type": "source"},
    ]


def _map():
    chapters = [
        {"chapter_id": chapter_id, "claim_refs": []}
        for chapter_id in FIRST_EDITION_CHAPTER_IDS
    ]
    chapters[0]["claim_refs"] = [{"record_id": "CLM-A", "record_version": "1"}]
    chapters[15]["claim_refs"] = [{"record_id": "CLM-B", "record_version": "2"}]
    return {"schema_version": "1.0", "chapters": chapters}


def test_assigns_every_selected_claim_once_and_only_to_selected_claims():
    result = validate_first_edition_chapter_map(_records(), _map())
    assert result == {
        ("CLM-A", "1"): "chapter-1",
        ("CLM-B", "2"): "chapter-16",
    }


def test_requires_exactly_nineteen_chapters_in_order():
    chapter_map = _map()
    chapter_map["chapters"].pop()
    with pytest.raises(ValueError, match="exactly 19"):
        validate_first_edition_chapter_map(_records(), chapter_map)

    chapter_map = _map()
    chapter_map["chapters"][0], chapter_map["chapters"][1] = (
        chapter_map["chapters"][1], chapter_map["chapters"][0]
    )
    with pytest.raises(ValueError, match="chapter-1 through chapter-19"):
        validate_first_edition_chapter_map(_records(), chapter_map)


def test_rejects_unselected_or_stale_claim_reference():
    chapter_map = _map()
    chapter_map["chapters"][2]["claim_refs"] = [
        {"record_id": "CLM-NOT-SELECTED", "record_version": "1"}
    ]
    with pytest.raises(ValueError, match="unselected or stale"):
        validate_first_edition_chapter_map(_records(), chapter_map)


def test_rejects_non_claim_dependencies_in_chapter_map():
    chapter_map = _map()
    chapter_map["chapters"][2]["claim_refs"] = [
        {"record_id": "EU-A", "record_version": "1"}
    ]
    with pytest.raises(ValueError, match="only selected Claim"):
        validate_first_edition_chapter_map(_records(), chapter_map)


def test_rejects_claim_assigned_to_multiple_chapters():
    chapter_map = _map()
    chapter_map["chapters"][1]["claim_refs"] = [
        {"record_id": "CLM-A", "record_version": "1"}
    ]
    with pytest.raises(ValueError, match="more than once"):
        validate_first_edition_chapter_map(_records(), chapter_map)


def test_rejects_selected_claim_without_chapter_assignment():
    records = _records()
    records[1] = copy.deepcopy(records[1])
    chapter_map = _map()
    chapter_map["chapters"][15]["claim_refs"] = []
    with pytest.raises(ValueError, match="not assigned"):
        validate_first_edition_chapter_map(records, chapter_map)


def test_rejects_invalid_chapter_map_schema():
    chapter_map = _map()
    chapter_map["schema_version"] = "0.9"
    with pytest.raises(ValueError, match="schema_version"):
        validate_first_edition_chapter_map(_records(), chapter_map)
