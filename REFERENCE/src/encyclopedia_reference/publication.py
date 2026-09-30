from __future__ import annotations

from typing import Any


def build_publication(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Создаёт производное представление с явными ссылками на Evidence Use."""
    evidence_by_claim: dict[tuple[str, str | None], list[dict[str, Any]]] = {}
    for record in records:
        if record.get("record_type") != "evidence_use":
            continue
        content = record.get("content", {})
        if not isinstance(content, dict):
            continue
        ref = content.get("claim_ref")
        if not isinstance(ref, dict) or not isinstance(ref.get("record_id"), str):
            continue
        key = (ref["record_id"], ref.get("version"))
        evidence_by_claim.setdefault(key, []).append({
            "evidence_use_ref": {
                "record_id": record["record_id"],
                "version": record["record_version"],
            },
            "source_ref": content.get("source_ref"),
            "evidence_role": content.get("evidence_role"),
            "material": content.get("material"),
        })

    entries = []
    for record in records:
        entry = {
            "record_id": record["record_id"],
            "record_version": record["record_version"],
            "record_type": record["record_type"],
            "publication_status": record["publication_status"],
            "content": record["content"],
        }
        if record.get("record_type") == "claim":
            key = (record["record_id"], record["record_version"])
            entry["evidence"] = evidence_by_claim.get(key, [])
        entries.append(entry)

    return {
        "publication_version": "0.2",
        "entries": entries,
        "derived": True,
        "source_records_unchanged": True,
        "citations_preserved": True,
    }
