from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import json

from jsonschema import Draft202012Validator, FormatChecker

from . import SCHEMA_VERSION, SUPPORTED_TYPES, VALIDATOR_VERSION


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    layer: str
    message: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    findings: tuple[Finding, ...]
    metadata: dict[str, str]

    @property
    def passed(self) -> bool:
        return self.status == "pass"


def _finding(code: str, severity: str, layer: str, message: str) -> Finding:
    return Finding(code, severity, layer, message)


class Validator:
    """Детерминированный read-only Validator."""

    def __init__(self, schema_path: Path):
        self.schema_path = schema_path
        self.schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self._schema_validator = Draft202012Validator(
            self.schema,
            format_checker=FormatChecker(),
        )

    def validate(self, record: dict[str, Any]) -> ValidationResult:
        findings: list[Finding] = []

        # L1: структурная проверка.
        for error in sorted(
            self._schema_validator.iter_errors(record),
            key=lambda e: (list(e.absolute_path), e.validator),
        ):
            path = ".".join(str(x) for x in error.absolute_path) or "$"
            findings.append(
                _finding(
                    "VAL-L1-SCHEMA",
                    "error",
                    "L1",
                    f"{path}: {error.message}",
                )
            )

        # L2: Type/Profile.
        record_type = record.get("record_type")
        if record_type not in SUPPORTED_TYPES:
            findings.append(
                _finding(
                    "VAL-L2-UNKNOWN-TYPE",
                    "error",
                    "L2",
                    "record_type не поддерживается первым вертикальным срезом",
                )
            )

        if not isinstance(record.get("type_version"), str):
            findings.append(
                _finding(
                    "VAL-L2-TYPE-VERSION",
                    "error",
                    "L2",
                    "type_version должен быть строкой",
                )
            )

        # L3: ссылки проверяются Storage/Reference layer, а здесь только форма.
        if isinstance(record.get("record_id"), str) and not record["record_id"].strip():
            findings.append(
                _finding(
                    "VAL-L3-EMPTY-ID",
                    "error",
                    "L3",
                    "record_id не может быть пустым",
                )
            )

        # L4: минимальные анти-инференс правила.
        if record.get("publication_status") == "published":
            content = record.get("content", {})
            if isinstance(content, dict) and content.get("truth") is True:
                findings.append(
                    _finding(
                        "VAL-L4-PUBLICATION-TRUTH",
                        "error",
                        "L4",
                        "publication_status не может автоматически утверждать истинность",
                    )
                )

        if record.get("record_type") == "evidence_use":
            role = record.get("content", {}).get("evidence_role")
            if role not in {"supports", "contradicts"}:
                findings.append(
                    _finding(
                        "VAL-L4-EVIDENCE-ROLE",
                        "error",
                        "L4",
                        "Core Evidence Role должен быть supports или contradicts",
                    )
                )

        errors = [f for f in findings if f.severity == "error"]
        status = "fail" if errors else "pass"

        return ValidationResult(
            status=status,
            findings=tuple(findings),
            metadata={
                "schema_version": SCHEMA_VERSION,
                "validator_version": VALIDATOR_VERSION,
            },
        )
