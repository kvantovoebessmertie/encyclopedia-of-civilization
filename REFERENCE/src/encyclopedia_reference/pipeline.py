from __future__ import annotations

from pathlib import Path
from typing import Any

from .references import ReferenceResolver
from .storage import FileStorage
from .validator import ValidationResult, Validator
from .semantic_rules import validate_semantic_dataset


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
        reference_findings = self.references.validate(record)
        semantic_findings = validate_semantic_dataset(self.storage.export_all() + [record])
        findings = result.findings + tuple(reference_findings) + tuple(semantic_findings)
        coverage = {**result.coverage, "L3": "executed", "semantic_registry": "executed"}

        if result.status != "pass" or any(f.severity == "error" for f in findings):
            return ValidationResult(
                status="fail" if any(f.severity == "error" for f in findings) else "indeterminate",
                findings=findings,
                metadata=result.metadata,
                coverage=coverage,
            )

        self.storage.create(record)
        return ValidationResult(
            status="pass",
            findings=findings,
            metadata=result.metadata,
            coverage=coverage,
        )

    def edit(
        self,
        record: dict[str, Any],
        expected_version: str,
    ) -> ValidationResult:
        result = self.validate(record)
        reference_findings = self.references.validate(record)
        semantic_findings = validate_semantic_dataset(self.storage.export_all() + [record])
        findings = result.findings + tuple(reference_findings) + tuple(semantic_findings)
        coverage = {**result.coverage, "L3": "executed", "semantic_registry": "executed"}

        if result.status != "pass" or any(f.severity == "error" for f in findings):
            return ValidationResult(
                status="fail" if any(f.severity == "error" for f in findings) else "indeterminate",
                findings=findings,
                metadata=result.metadata,
                coverage=coverage,
            )

        self.storage.update(record, expected_version)
        return ValidationResult(
            status="pass",
            findings=findings,
            metadata=result.metadata,
            coverage=coverage,
        )
