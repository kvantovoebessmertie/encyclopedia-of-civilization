from __future__ import annotations

from pathlib import Path
from typing import Any

from .storage import FileStorage
from .validator import ValidationResult, Validator


class ReferencePipeline:
    """Минимальный pipeline первого вертикального среза."""

    def __init__(self, schema_path: Path, storage_root: Path):
        self.validator = Validator(schema_path)
        self.storage = FileStorage(storage_root)

    def validate(self, record: dict[str, Any]) -> ValidationResult:
        return self.validator.validate(record)

    def create(self, record: dict[str, Any]) -> ValidationResult:
        result = self.validate(record)
        if not result.passed:
            return result
        self.storage.create(record)
        return result

    def edit(
        self,
        record: dict[str, Any],
        expected_version: str,
    ) -> ValidationResult:
        result = self.validate(record)
        if not result.passed:
            return result
        self.storage.update(record, expected_version)
        return result
