from __future__ import annotations

from typing import Any


def build_publication(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Создаёт производное представление, не изменяя канонические Record."""

    entries = []
    for record in records:
        entries.append(
            {
                "record_id": record["record_id"],
                "record_version": record["record_version"],
                "record_type": record["record_type"],
                "publication_status": record["publication_status"],
                "content": record["content"],
            }
        )

    return {
        "publication_version": "0.1",
        "entries": entries,
        "derived": True,
        "source_records_unchanged": True,
    }
