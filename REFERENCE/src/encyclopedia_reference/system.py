from __future__ import annotations

from pathlib import Path
from typing import Any

from .pipeline import ReferencePipeline
from .publication import build_publication
from .query import QueryInterface
from .recovery import make_package


class ReferenceSystem:
    """End-to-end фасад первого вертикального среза."""

    def __init__(self, schema_path: Path, storage_root: Path):
        self.pipeline = ReferencePipeline(schema_path, storage_root)
        self.query = QueryInterface(self.pipeline.storage)

    def create(self, record: dict[str, Any]):
        return self.pipeline.create(record)

    def edit(self, record: dict[str, Any], expected_version: str):
        return self.pipeline.edit(record, expected_version)

    def publish(self) -> dict[str, Any]:
        records = self.query.query()
        return build_publication(records)

    def package(self, target: Path) -> Path:
        return make_package(self.query.query(), target)
