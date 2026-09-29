from __future__ import annotations

from pathlib import Path
from typing import Any
import json


class StorageError(Exception):
    """Ошибка Storage Adapter."""


class ConcurrentUpdateError(StorageError):
    """Версия Record изменилась между чтением и редактированием."""


class FileStorage:
    """Минимальный offline Storage Adapter.

    Канонической единицей хранения является версия Record.
    """

    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def _record_dir(self, record_id: str) -> Path:
        # Идентификатор никогда не используется как произвольный путь.
        safe = record_id.replace("/", "_").replace("\\", "_")
        if safe in {"", ".", ".."} or ".." in safe:
            raise StorageError("STORAGE-PATH-TRAVERSAL")
        return self.root / safe

    def _version_path(self, record_id: str, version: str) -> Path:
        safe_version = version.replace("/", "_").replace("\\", "_")
        if safe_version in {"", ".", ".."} or ".." in safe_version:
            raise StorageError("STORAGE-PATH-TRAVERSAL")
        return self._record_dir(record_id) / f"{safe_version}.json"

    def create(self, record: dict[str, Any]) -> None:
        record_id = record["record_id"]
        version = record["record_version"]
        path = self._version_path(record_id, version)
        if path.exists():
            raise StorageError("STORAGE-VERSION-EXISTS")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def read_version(self, record_id: str, version: str) -> dict[str, Any]:
        path = self._version_path(record_id, version)
        if not path.exists():
            raise StorageError("STORAGE-VERSION-NOT-FOUND")
        return json.loads(path.read_text(encoding="utf-8"))

    def list_versions(self, record_id: str) -> list[str]:
        directory = self._record_dir(record_id)
        if not directory.exists():
            return []
        return sorted(p.stem for p in directory.glob("*.json"))

    def latest(self, record_id: str) -> dict[str, Any]:
        versions = self.list_versions(record_id)
        if not versions:
            raise StorageError("STORAGE-RECORD-NOT-FOUND")
        return self.read_version(record_id, versions[-1])

    def update(
        self,
        record: dict[str, Any],
        expected_version: str,
    ) -> None:
        current = self.latest(record["record_id"])
        if current["record_version"] != expected_version:
            raise ConcurrentUpdateError("STORAGE-CONCURRENT-UPDATE")
        self.create(record)

    def export_all(self) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for directory in sorted(self.root.iterdir()):
            if directory.is_dir():
                for path in sorted(directory.glob("*.json")):
                    result.append(json.loads(path.read_text(encoding="utf-8")))
        return result
