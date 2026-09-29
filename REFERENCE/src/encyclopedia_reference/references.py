from __future__ import annotations

from typing import Any

from .storage import FileStorage, StorageError
from .validator import Finding


class ReferenceResolver:
    """Проверяет локальные versioned references без молчаливого fallback."""

    def __init__(self, storage: FileStorage):
        self.storage = storage

    def validate(self, record: dict[str, Any]) -> list[Finding]:
        findings: list[Finding] = []

        def check(ref: Any, path: str) -> None:
            if not isinstance(ref, dict):
                return
            record_id = ref.get("record_id")
            version = ref.get("version")
            if not isinstance(record_id, str):
                return
            try:
                if version is None:
                    self.storage.latest(record_id)
                else:
                    self.storage.read_version(record_id, version)
            except StorageError as exc:
                findings.append(
                    Finding(
                        code="VAL-L3-REFERENCE-VERSION",
                        severity="error",
                        layer="L3",
                        message=f"{path}: ссылка не разрешается: {exc}",
                        subject=path,
                        rule="VAL-L3-REFERENCE-VERSION",
                    )
                )

        def walk(value: Any, path: str) -> None:
            if isinstance(value, dict):
                # A canonical record_ref is identified by record_id. Extension
                # payloads are intentionally opaque to the canonical graph.
                if isinstance(value.get("record_id"), str):
                    check(value, path)
                    return
                for key, child in value.items():
                    if key == "extensions":
                        continue
                    walk(child, f"{path}.{key}")
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    walk(child, f"{path}[{index}]")

        walk(record.get("provenance", {}), "provenance")
        for key in ("scope", "context"):
            if key in record:
                walk(record[key], key)
        walk(record.get("content", {}), "content")

        return findings