from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import hashlib
import json
from datetime import datetime

from jsonschema import Draft202012Validator, FormatChecker

from . import SCHEMA_VERSION, SUPPORTED_TYPES, VALIDATOR_VERSION


SUPPORTED_PROFILE_VERSIONS = {
    "record": {"1.0"}, "claim": {"1.0"}, "source": {"1.0"},
    "evidence_use": {"1.0"}, "assessment": {"1.0"}, "inference": {"1.0"},
    "decision": {"1.0"}, "action": {"1.0"}, "event": {"1.0"},
    "result": {"1.0"}, "state": {"1.0"}, "process": {"1.0"},
    "relation": {"1.0"}, "identity": {"1.0"}, "context": {"1.0"},
    "scope": {"1.0"}, "provenance": {"1.0"}, "authorship_contribution": {"1.0"},
    "trust_reputation": {"1.0", "1.1"},
}

SUPPORTED_INTEGRITY_ALGORITHMS = {"sha256"}
SUPPORTED_INTEGRITY_CANONICALIZATION = "json-sort-keys-utf8-excluding-integrity"


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    layer: str
    message: str
    subject: str | None = None
    rule: str | None = None
    verification_state: str = "verified"


@dataclass(frozen=True)
class ValidationResult:
    status: str
    findings: tuple[Finding, ...]
    metadata: dict[str, str]
    coverage: dict[str, str] = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return self.status == "pass"


def _finding(
    code: str,
    severity: str,
    layer: str,
    message: str,
    *,
    subject: str | None = None,
    verification_state: str = "verified",
) -> Finding:
    return Finding(
        code, severity, layer, message,
        subject=subject, rule=code, verification_state=verification_state,
    )


class Validator:
    """Детерминированный read-only Validator."""

    def __init__(self, schema_path: Path):
        self.schema_path = schema_path
        self.schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self._schema_validator = Draft202012Validator(
            self.schema, format_checker=FormatChecker()
        )

    def validate(self, record: dict[str, Any]) -> ValidationResult:
        findings: list[Finding] = []

        # L1: Structural.
        for error in sorted(
            self._schema_validator.iter_errors(record),
            key=lambda e: (list(e.absolute_path), e.validator),
        ):
            path = ".".join(str(x) for x in error.absolute_path) or "$"
            findings.append(_finding(
                "VAL-L1-SCHEMA", "error", "L1", f"{path}: {error.message}"
            ))

        record_type = record.get("record_type")
        type_version = record.get("type_version")

        # L2: Type/Profile.
        if record_type not in SUPPORTED_TYPES:
            findings.append(_finding(
                "VAL-L2-UNKNOWN-TYPE", "error", "L2",
                "record_type не поддерживается текущей реализацией",
            ))
        elif type_version not in SUPPORTED_PROFILE_VERSIONS[record_type]:
            findings.append(_finding(
                "VAL-L2-INCOMPATIBLE-TYPE-VERSION", "error", "L2",
                f"type_version {type_version!r} не реализован для {record_type}",
            ))

        if record.get("schema") != "record/0.1":
            findings.append(_finding(
                "VAL-L2-SCHEMA-VERSION", "error", "L2",
                "текущий Reference Validator поддерживает schema=record/0.1",
            ))

        # L3: structural reference shapes; graph resolution is performed by
        # ReferenceResolver and therefore remains a separate integration step.
        self._validate_ref_shapes(record, findings)

        # L4: semantic and Standard-specific invariants.
        self._validate_l4(record, findings)

        # L5: record-local integrity/history invariants.
        self._validate_l5_record(record, findings)

        errors = [f for f in findings if f.severity == "error"]
        unverifiable = [f for f in findings if f.verification_state != "verified"]
        status = "fail" if errors else ("indeterminate" if unverifiable else "pass")

        return ValidationResult(
            status=status,
            findings=tuple(findings),
            metadata={
                "schema_version": SCHEMA_VERSION,
                "validator_version": VALIDATOR_VERSION,
                "integrity_canonicalization": SUPPORTED_INTEGRITY_CANONICALIZATION,
            },
            coverage={
                "L1": "executed",
                "L2": "executed",
                "L3": "executed",
                "L4": "executed",
                "L5": "executed",
            },
        )

    @staticmethod
    def _validate_l4(record: dict[str, Any], findings: list[Finding]) -> None:
        content = record.get("content")
        if not isinstance(content, dict):
            return
        record_type = record.get("record_type")
        complete = record.get("completion_status") == "complete"

        if record_type == "source" and not content.get("source_identity"):
            findings.append(_finding(
                "VAL-L4-SOURCE-IDENTITY", "error", "L4",
                "Source должен содержать source_identity",
            ))

        if record_type == "evidence_use" and content.get("evidence_role") not in {"supports", "contradicts"}:
            findings.append(_finding(
                "VAL-L4-EVIDENCE-ROLE", "error", "L4",
                "Core Evidence Role должен быть supports или contradicts",
            ))

        if record_type == "assessment":
            if complete:
                for field_name, code in (
                    ("target", "VAL-L4-ASSESSMENT-TARGET"),
                    ("aspect", "VAL-L4-ASSESSMENT-ASPECT"),
                    ("result", "VAL-L4-ASSESSMENT-RESULT"),
                ):
                    if field_name not in content:
                        findings.append(_finding(
                            code, "error", "L4",
                            f"завершённая Assessment должна содержать {field_name}",
                        ))

        if record_type == "inference" and complete:
            if "conclusion" not in content:
                findings.append(_finding(
                    "VAL-L4-INFERENCE-CONCLUSION", "error", "L4",
                    "завершённый Inference должен содержать conclusion",
                ))
            attribution = content.get("attribution")
            if not isinstance(attribution, dict):
                findings.append(_finding(
                    "VAL-L4-INFERENCE-ATTRIBUTION", "error", "L4",
                    "завершённый Inference должен содержать разрешимую attribution",
                ))
            else:
                mode = attribution.get("mode")
                if mode == "known" and "agent_ref" not in attribution:
                    findings.append(_finding(
                        "VAL-L4-INFERENCE-ATTRIBUTION-AGENT", "error", "L4",
                        "attribution.mode=known должна содержать agent_ref",
                    ))
                if mode == "reconstructed" and "method_ref" not in attribution:
                    findings.append(_finding(
                        "VAL-L4-INFERENCE-ATTRIBUTION-METHOD", "error", "L4",
                        "reconstructed attribution должна содержать method_ref",
                    ))

        if record_type == "decision" and complete:
            if "decision_result" not in content:
                findings.append(_finding(
                    "VAL-L4-DECISION-RESULT", "error", "L4",
                    "завершённый Decision должен содержать decision_result",
                ))
            if "decision_maker" not in content:
                findings.append(_finding(
                    "VAL-L4-DECISION-MAKER", "error", "L4",
                    "завершённый Decision должен содержать decision_maker",
                ))


        if record_type == "result":
            causal = content.get("causal_attribution")
            if isinstance(causal, dict) and causal.get("mode") == "attributed" and "basis_ref" not in causal:
                findings.append(_finding(
                    "VAL-L4-RESULT-CAUSAL-BASIS", "error", "L4",
                    "causal_attribution.mode=attributed должен сохранять basis_ref",
                ))

        if record_type == "state":
            frame_present = (
                "frame_ref" in content or "time" in content
                or "context" in record or "scope" in record
            )
            if not frame_present:
                findings.append(_finding(
                    "VAL-L4-STATE-FRAME", "error", "L4",
                    "State должен сохранять явную применимую рамку через frame_ref, time, context или scope",
                ))

        if record_type == "process":
            if not any(k in content for k in ("time", "start_ref", "end_ref")):
                findings.append(_finding(
                    "VAL-L4-PROCESS-FRAME", "error", "L4",
                    "Process должен сохранять явную временную/процессную рамку через time, start_ref или end_ref",
                ))

        if record_type == "relation":
            if "relation_type" not in content:
                findings.append(_finding(
                    "VAL-L4-RELATION-TYPE", "error", "L4",
                    "Relation должен содержать relation_type",
                ))
            if not any(k in content for k in ("frame_ref",)) and not any(
                k in record for k in ("valid_time", "context", "scope")
            ):
                findings.append(_finding(
                    "VAL-L4-RELATION-FRAME", "error", "L4",
                    "Relation должен сохранять явную применимую рамку через frame_ref, valid_time, context или scope",
                ))

        if record_type == "identity":
            if "criterion" not in content:
                findings.append(_finding(
                    "VAL-L4-IDENTITY-CRITERION", "error", "L4",
                    "Identity должен содержать criterion",
                ))
            identity_status = content.get("identity_status")
            if identity_status in {
                "resolved_same", "resolved_distinct", "probable_same",
                "possible_same", "ambiguous", "unresolved", "disputed", "unknown",
            } and not (
                "frame_ref" in content or "scope_ref" in content
                or "valid_time" in record or "context" in record or "scope" in record
            ):
                findings.append(_finding(
                    "VAL-L4-IDENTITY-FRAME", "error", "L4",
                    "Identity с явным статусом разрешения должен сохранять применимую рамку",
                ))
            if identity_status in {"possible_same", "probable_same", "ambiguous"} and "candidate_refs" not in content:
                findings.append(_finding(
                    "VAL-L4-IDENTITY-CANDIDATES", "error", "L4",
                    "Неокончательное Identity-разрешение должно сохранять candidate_refs",
                ))

        required_targets = {
            "context": ("target_ref", "VAL-L4-CONTEXT-TARGET"),
            "scope": ("target_ref", "VAL-L4-SCOPE-TARGET"),
            "provenance": ("target_ref", "VAL-L4-PROVENANCE-TARGET"),
            "authorship_contribution": ("contributor_ref", "VAL-L4-AUTHORSHIP-CONTRIBUTOR"),
            "trust_reputation": ("basis_refs", "VAL-L4-TRUST-BASIS"),
        }
        if record_type in required_targets:
            field_name, code = required_targets[record_type]
            if field_name not in content:
                findings.append(_finding(
                    code, "error", "L4",
                    f"{record_type} должен содержать {field_name}",
                ))

        if record_type == "trust_reputation" and content.get("assessment_type") in {"trust", "trust_assessment"}:
            if "subject_ref" not in content:
                findings.append(_finding(
                    "VAL-L4-TRUST-SUBJECT", "error", "L4",
                    "Trust должен содержать subject_ref",
                ))
            if "goal_ref" not in content:
                findings.append(_finding(
                    "VAL-L4-TRUST-GOAL", "error", "L4",
                    "Trust должен содержать goal_ref",
                ))

        # Cross-cutting anti-inference rules.
        if record.get("publication_status") == "published" and content.get("truth") is True:
            findings.append(_finding(
                "VAL-L4-PUBLICATION-TRUTH", "error", "L4",
                "publication_status не может автоматически утверждать истинность",
            ))
        if content.get("truth") is True and record_type not in {"claim"}:
            findings.append(_finding(
                "VAL-L4-TRUTH-TYPE-INFERENCE", "error", "L4",
                "истинность не должна создаваться как побочный эффект другого типа Record",
            ))

    @staticmethod
    def _canonical_integrity_bytes(record: dict[str, Any]) -> bytes:
        payload = dict(record)
        payload.pop("integrity", None)
        return (
            json.dumps(
                payload,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        )

    @classmethod
    def _validate_l5_record(cls, record: dict[str, Any], findings: list[Finding]) -> None:
        integrity = record.get("integrity")
        if isinstance(integrity, dict):
            algorithm = integrity.get("algorithm")
            canonicalization = integrity.get("canonicalization")
            if algorithm not in SUPPORTED_INTEGRITY_ALGORITHMS:
                findings.append(_finding(
                    "VAL-L5-INTEGRITY-UNVERIFIABLE", "warning", "L5",
                    f"алгоритм целостности {algorithm!r} не поддерживается текущим Validator",
                    verification_state="unverified",
                ))
            elif canonicalization != SUPPORTED_INTEGRITY_CANONICALIZATION:
                findings.append(_finding(
                    "VAL-L5-INTEGRITY-CANONICALIZATION-UNVERIFIABLE", "warning", "L5",
                    f"canonicalization должна быть {SUPPORTED_INTEGRITY_CANONICALIZATION!r} для локальной проверки",
                    verification_state="unverified",
                ))
            else:
                expected = hashlib.sha256(cls._canonical_integrity_bytes(record)).hexdigest()
                if integrity.get("digest") != expected:
                    findings.append(_finding(
                        "VAL-L5-INTEGRITY-MISMATCH", "error", "L5",
                        "integrity.digest не соответствует каноническому содержимому Record",
                    ))

        valid_time = record.get("valid_time")
        if isinstance(valid_time, dict):
            start = valid_time.get("start")
            end = valid_time.get("end")
            if isinstance(start, str) and isinstance(end, str):
                try:
                    start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
                    end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
                    if start_dt > end_dt:
                        findings.append(_finding(
                            "VAL-L5-TIME-INTERVAL-ORDER", "error", "L5",
                            "valid_time.start не может быть позже valid_time.end",
                        ))
                except ValueError:
                    # L1 owns format validation; do not duplicate it as an L5 error.
                    pass

        if record.get("record_id") and record.get("record_version"):
            if record["record_id"] == record.get("record_version"):
                findings.append(_finding(
                    "VAL-L5-ID-VERSION-COLLISION", "error", "L5",
                    "record_id и record_version не должны быть одним и тем же идентификатором",
                ))

    @classmethod
    def validate_dataset(cls, records: list[dict[str, Any]], schema_path: Path) -> ValidationResult:
        validator = cls(schema_path)
        findings: list[Finding] = []
        seen: set[tuple[str, str]] = set()
        for record in records:
            result = validator.validate(record)
            findings.extend(result.findings)
            key = (record.get("record_id"), record.get("record_version"))
            if key in seen:
                findings.append(_finding(
                    "VAL-L5-DUPLICATE-RECORD-VERSION", "error", "L5",
                    f"дубликат логической версии Record: {key[0]!r}@{key[1]!r}",
                    subject=str(key[0]),
                ))
            else:
                seen.add(key)

        from .semantic_rules import validate_semantic_dataset
        findings.extend(validate_semantic_dataset(records))

        errors = [f for f in findings if f.severity == "error"]
        unverifiable = [f for f in findings if f.verification_state != "verified"]
        status = "fail" if errors else ("indeterminate" if unverifiable else "pass")
        return ValidationResult(
            status=status,
            findings=tuple(findings),
            metadata={
                "schema_version": SCHEMA_VERSION,
                "validator_version": VALIDATOR_VERSION,
                "dataset_record_count": str(len(records)),
            },
            coverage={"L1": "executed", "L2": "executed", "L3": "executed", "L4": "executed", "L5": "executed", "semantic_registry": "executed"},
        )

    @staticmethod
    def _validate_ref_shapes(record: dict[str, Any], findings: list[Finding]) -> None:
        def check_ref(value: Any, path: str) -> None:
            if not isinstance(value, dict) or not isinstance(value.get("record_id"), str):
                findings.append(_finding(
                    "VAL-L3-REFERENCE-SHAPE", "error", "L3",
                    f"{path}: ссылка должна содержать record_id",
                    subject=path,
                ))

        def check_many(values: Any, path: str) -> None:
            if values is None:
                return
            if not isinstance(values, list):
                findings.append(_finding(
                    "VAL-L3-REFERENCE-LIST", "error", "L3",
                    f"{path}: ожидается список ссылок", subject=path,
                ))
                return
            for index, value in enumerate(values):
                check_ref(value, f"{path}[{index}]")

        provenance = record.get("provenance")
        if isinstance(provenance, dict):
            for key in ("agent_refs", "created_from", "transformed_from"):
                check_many(provenance.get(key), f"provenance.{key}")

        record_type = record.get("record_type")
        content = record.get("content", {})
        if not isinstance(content, dict):
            return

        if record_type == "claim":
            for key in ("scope_ref", "context_ref"):
                if key in content:
                    check_ref(content[key], f"content.{key}")
            check_many(content.get("referents"), "content.referents")
            check_many(content.get("relation_refs"), "content.relation_refs")
        elif record_type == "evidence_use":
            for key in ("claim_ref", "source_ref", "resolution_context", "source_state_ref"):
                if key in content:
                    check_ref(content[key], f"content.{key}")
        elif record_type == "assessment":
            for key in ("target", "assessor_ref", "method_ref", "scale_ref", "profile_ref"):
                if key in content:
                    check_ref(content[key], f"content.{key}")
            check_many(content.get("inputs"), "content.inputs")
