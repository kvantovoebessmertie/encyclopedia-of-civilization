from __future__ import annotations

from typing import Any


FIRST_EDITION_CHAPTER_IDS = tuple(f"chapter-{number}" for number in range(1, 20))


def validate_first_edition_chapter_map(
    selected_records: list[dict[str, Any]],
    chapter_map: dict[str, Any],
) -> dict[tuple[str, str], str]:
    """Validate one exact chapter assignment for every selected Claim.

    The chapter map is editorial navigation metadata. It cannot approve records,
    add dependencies, or make unselected records visible.
    """
    if not isinstance(chapter_map, dict) or chapter_map.get("schema_version") != "1.0":
        raise ValueError("Unsupported or missing first-edition chapter-map schema_version (expected 1.0)")

    chapters = chapter_map.get("chapters")
    if not isinstance(chapters, list) or len(chapters) != len(FIRST_EDITION_CHAPTER_IDS):
        raise ValueError("Chapter map must contain exactly 19 chapters")

    chapter_ids: list[str] = []
    for chapter in chapters:
        if not isinstance(chapter, dict):
            raise ValueError("Every chapter-map entry must be an object")
        chapter_id = chapter.get("chapter_id")
        if not isinstance(chapter_id, str) or not chapter_id.strip():
            raise ValueError("Every chapter requires a non-empty chapter_id")
        chapter_ids.append(chapter_id)

    if tuple(chapter_ids) != FIRST_EDITION_CHAPTER_IDS:
        raise ValueError("Chapter map must contain chapter-1 through chapter-19 exactly once and in order")

    selected_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for record in selected_records:
        if not isinstance(record, dict):
            raise ValueError("Every selected record must be an object")
        record_id = record.get("record_id")
        version = record.get("record_version")
        if not isinstance(record_id, str) or not record_id.strip():
            raise ValueError("Selected record has invalid record_id")
        if not isinstance(version, (str, int)) or not str(version).strip():
            raise ValueError("Selected record has invalid record_version")
        key = (record_id, str(version))
        if key in selected_by_key:
            raise ValueError(f"Duplicate selected record identity: {key}")
        selected_by_key[key] = record

    assignments: dict[tuple[str, str], str] = {}
    for chapter in chapters:
        chapter_id = chapter["chapter_id"]
        claim_refs = chapter.get("claim_refs")
        if not isinstance(claim_refs, list):
            raise ValueError(f"claim_refs must be a list for {chapter_id}")
        for ref in claim_refs:
            if not isinstance(ref, dict):
                raise ValueError(f"Claim reference must be an object in {chapter_id}")
            record_id = ref.get("record_id")
            version = ref.get("record_version")
            if not isinstance(record_id, str) or not record_id.strip():
                raise ValueError(f"Claim reference has invalid record_id in {chapter_id}")
            if not isinstance(version, (str, int)) or not str(version).strip():
                raise ValueError(f"Claim reference has invalid record_version in {chapter_id}")
            key = (record_id, str(version))
            if key in assignments:
                raise ValueError(f"Claim is assigned more than once: {key}")
            record = selected_by_key.get(key)
            if record is None:
                raise ValueError(f"Chapter references an unselected or stale record: {key}")
            if record.get("record_type") != "claim":
                raise ValueError(f"Chapter map may assign only selected Claim records: {key}")
            assignments[key] = chapter_id

    selected_claims = {
        key for key, record in selected_by_key.items()
        if record.get("record_type") == "claim"
    }
    missing = selected_claims - set(assignments)
    if missing:
        raise ValueError(f"Selected Claims are not assigned to a chapter: {sorted(missing)}")

    return assignments
