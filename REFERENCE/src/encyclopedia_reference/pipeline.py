from __future__ import annotations

from pathlib import Path
from typing import Any

from .references import ReferenceResolver
from .storage import FileStorage
from .validator import ValidationResult, Validator


class ReferencePipeline:
    """Минимальный pipeline первого вертикального среза."""

    def __init__(self, schema_path: Path, storage_root: Path):
        self.validator = Validator(schema_path)
        self.storage = FileStorage(storage_root)
        self.references = ReferenceResolver(self.storage)

    def validate(self, record: dict[str, Any]) -> ValidationResult:
        return self.validator.validate(record)

    def create(self, record: dict[str, Any]) -> ValidationResult:
        result = self.validate(record)
        if not result.passed:
            return result

        reference_findings = self.references.validate(record)
        if reference_findings:
            return ValidationResult(
                status="fail",
                findings=result.findings + tuple(reference_findings),
                metadata=result.metadata,
                coverage={**result.coverage, "L3": "executed"},
            )

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

        reference_findings = self.references.validate(record)
        if reference_findings:
            return ValidationResult(
                status="fail",
                findings=result.findings + tuple(reference_findings),
                metadata=result.metadata,
                coverage={**result.coverage, "L3": "executed"},
            )

        self.storage.update(record, expected_version)
        return result
