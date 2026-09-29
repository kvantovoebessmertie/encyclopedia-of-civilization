from __future__ import annotations

from typing import Any

from .storage import FileStorage


class QueryInterface:
    """Минимальный read-only Query интерфейс."""

    def __init__(self, storage: FileStorage):
        self.storage = storage

    def query(
        self,
        *,
        record_type: str | None = None,
        publication_status: str | None = None,
    ) -> list[dict[str, Any]]:
        records = self.storage.export_all()
        result = []
        for record in records:
            if record_type is not None and record.get("record_type") != record_type:
                continue
            if (
                publication_status is not None
                and record.get("publication_status") != publication_status
            ):
                continue
            result.append(record)
        return sorted(
            result,
            key=lambda r: (r["record_id"], r["record_version"]),
        )
