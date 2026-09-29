from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import json

from jsonschema import Draft202012Validator, FormatChecker

from . import SCHEMA_VERSION, SUPPORTED_TYPES, VALIDATOR_VERSION


SUPPORTED_PROFILE_VERSIONS = {
    "record": {"1.0"},
    "claim": {"1.0"},
    "source": {"1.0"},
    "evidence_use": {"1.0"},
    "assessment": {"1.0"},
    "inference": {"1.0"},
    "decision": {"1.0"},
    "action": {"1.0"},
    "event": {"1.0"},
    "result": {"1.0"},
    "state": {"1.0"},
    "process": {"1.0"},
    "relation": {"1.0"},
    "identity": {"1.0"},
    "context": {"1.0"},
    "scope": {"1.0"},
    "provenance": {"1.0"},
    "authorship_contribution": {"1.0"},
    "trust_reputation": {"1.0", "1.1"},
}


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


def _finding(code: str, severity: str, layer: str, message: str) -> Finding:
    # Stable finding code is the machine-readable rule reference for the
    # current reference implementation. A future normative rule registry may
    # replace this with a distinct rule_id without changing result semantics.
    return Finding(
        code,
        severity,
        layer,
        message,
        rule=code,
        verification_state="verified",
    )


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

        record_type = record.get("record_type")
        type_version = record.get("type_version")

        # L2: Type/Profile.
        if record_type not in SUPPORTED_TYPES:
            findings.append(
                _finding(
                    "VAL-L2-UNKNOWN-TYPE",
                    "error",
                    "L2",
                    "record_type не поддерживается первым вертикальным срезом",
                )
            )
        elif type_version not in SUPPORTED_PROFILE_VERSIONS[record_type]:
            findings.append(
                _finding(
                    "VAL-L2-INCOMPATIBLE-TYPE-VERSION",
                    "error",
                    "L2",
                    f"type_version {type_version!r} не реализован для {record_type}",
                )
            )

        if record.get("schema") != "record/0.1":
            findings.append(
                _finding(
                    "VAL-L2-SCHEMA-VERSION",
                    "error",
                    "L2",
                    "первый вертикальный срез поддерживает schema=record/0.1",
                )
            )

        # L3: минимальные правила ссылочной формы.
        self._validate_ref_shapes(record, findings)

        # L4: специализированные семантические правила.
        content = record.get("content")
        if isinstance(content, dict):
            if record_type == "source" and not content.get("source_identity"):
                findings.append(
                    _finding(
                        "VAL-L4-SOURCE-IDENTITY",
                        "error",
                        "L4",
                        "Source должен содержать source_identity",
                    )
                )

            if record_type == "action" and "action_content" not in content:
                findings.append(_finding("VAL-L4-ACTION-CONTENT", "error", "L4", "Action должен содержать action_content"))
            if record_type == "event" and "event_content" not in content:
                findings.append(_finding("VAL-L4-EVENT-CONTENT", "error", "L4", "Event должен содержать event_content"))
            if record_type == "result" and "result_content" not in content:
                findings.append(_finding("VAL-L4-RESULT-CONTENT", "error", "L4", "Result должен содержать result_content"))
            if record_type == "result" and "reference_frame" not in content:
                findings.append(_finding("VAL-L4-RESULT-REFERENCE-FRAME", "error", "L4", "Result должен содержать reference_frame"))
            if record_type == "state" and "subject_ref" not in content:
                findings.append(_finding("VAL-L4-STATE-SUBJECT", "error", "L4", "State должен содержать subject_ref"))
            if record_type == "state":
                # Standard 011: State retains an explicit applicable frame.
                frame_present = any(
                    key in content for key in ("frame_ref", "time")
                ) or any(
                    key in record for key in ("context", "scope")
                )
                if not frame_present:
                    findings.append(
                        _finding(
                            "VAL-L4-STATE-FRAME",
                            "error",
                            "L4",
                            "State должен сохранять явную применимую рамку через frame_ref, time, context или scope",
                        )
                    )
            if record_type == "process" and "process_content" not in content:
                findings.append(_finding("VAL-L4-PROCESS-CONTENT", "error", "L4", "Process должен содержать process_content"))

            if record_type == "relation":
                # Standard 013: a Relation must retain an explicit applicable
                # frame. The frame may be represented by a dedicated frame_ref,
                # or by an explicit top-level temporal/context/scope frame.
                frame_present = any(
                    (
                        "frame_ref" in content,
                        "valid_time" in record,
                        "context" in record,
                        "scope" in record,
                    )
                )
                if not frame_present:
                    findings.append(
                        _finding(
                            "VAL-L4-RELATION-FRAME",
                            "error",
                            "L4",
                            "Relation должен сохранять явную applicable frame через frame_ref, valid_time, context или scope",
                        )
                    )


            if record_type == "process":
                # Standard 012: a concrete Process occurrence retains an explicit
                # temporal/process frame without forcing exact start/end values.
                frame_present = any(
                    key in content for key in ("time", "start_ref", "end_ref")
                )
                if not frame_present:
                    findings.append(
                        _finding(
                            "VAL-L4-PROCESS-FRAME",
                            "error",
                            "L4",
                            "Process должен сохранять явную временную/процессную рамку через time, start_ref или end_ref",
                        )
                    )
            if record_type == "relation" and "relation_type" not in content:
                findings.append(_finding("VAL-L4-RELATION-TYPE", "error", "L4", "Relation должен содержать relation_type"))
            if record_type == "identity":
                if "criterion" not in content:
                    findings.append(_finding("VAL-L4-IDENTITY-CRITERION", "error", "L4", "Identity должен содержать criterion"))
                identity_status = content.get("identity_status")
                frame_present = any(
                    (
                        "frame_ref" in content,
                        "valid_time" in record,
                        "context" in record,
                        "scope" in record,
                    )
                )
                if identity_status in {
                    "resolved_same",
                    "resolved_distinct",
                    "probable_same",
                    "possible_same",
                    "ambiguous",
                    "unresolved",
                    "disputed",
                    "unknown",
                } and not frame_present:
                    findings.append(_finding(
                        "VAL-L4-IDENTITY-FRAME",
                        "error",
                        "L4",
                        "Identity с явным статусом разрешения должен сохранять применимую рамку через frame_ref, valid_time, context или scope",
                    ))
                if identity_status in {"possible_same", "probable_same", "ambiguous"} and "candidate_refs" not in content:
                    findings.append(_finding(
                        "VAL-L4-IDENTITY-CANDIDATES",
                        "error",
                        "L4",
                        "Неокончательное Identity-разрешение должно сохранять candidate_refs",
                    ))
            if record_type == "context" and "target_ref" not in content:
                findings.append(_finding("VAL-L4-CONTEXT-TARGET", "error", "L4", "Context должен содержать target_ref"))
            if record_type == "scope" and "target_ref" not in content:
                findings.append(_finding("VAL-L4-SCOPE-TARGET", "error", "L4", "Scope должен содержать target_ref"))
            if record_type == "provenance" and "target_ref" not in content:
                findings.append(_finding("VAL-L4-PROVENANCE-TARGET", "error", "L4", "Provenance должен содержать target_ref"))
            if record_type == "authorship_contribution" and "contributor_ref" not in content:
                findings.append(_finding("VAL-L4-AUTHORSHIP-CONTRIBUTOR", "error", "L4", "Authorship Contribution должен содержать contributor_ref"))
            if record_type == "trust_reputation" and "basis_refs" not in content:
                findings.append(_finding("VAL-L4-TRUST-BASIS", "error", "L4", "Trust/Reputation должен содержать basis_refs"))
            if record_type == "trust_reputation" and content.get("assessment_type") in {"trust", "trust_assessment"}:
                if "subject_ref" not in content:
                    findings.append(_finding("VAL-L4-TRUST-SUBJECT", "error", "L4", "Trust должен содержать subject_ref"))
                if "goal_ref" not in content:
                    findings.append(_finding("VAL-L4-TRUST-GOAL", "error", "L4", "Trust должен содержать goal_ref"))
            if record_type == "assessment" and record.get("completion_status") == "complete":
                if "result" not in content:
                    findings.append(
                        _finding(
                            "VAL-L4-ASSESSMENT-RESULT",
                            "error",
                            "L4",
                            "завершённая Assessment должна содержать result",
                        )
                    )
            if record_type == "inference" and record.get("completion_status") == "complete":
                if "conclusion" not in content:
                    findings.append(_finding("VAL-L4-INFERENCE-CONCLUSION", "error", "L4", "завершённый Inference должен содержать conclusion"))
                if "attribution" not in content:
                    findings.append(_finding("VAL-L4-INFERENCE-ATTRIBUTION", "error", "L4", "завершённый Inference должен содержать attribution"))
            if record_type == "decision" and record.get("completion_status") == "complete":
                if "decision_result" not in content:
                    findings.append(_finding("VAL-L4-DECISION-RESULT", "error", "L4", "завершённый Decision должен содержать decision_result"))
                if "decision_maker" not in content:
                    findings.append(_finding("VAL-L4-DECISION-MAKER", "error", "L4", "завершённый Decision должен содержать decision_maker"))

            if record_type == "evidence_use":
                role = content.get("evidence_role")
                if role not in {"supports", "contradicts"}:
                    findings.append(
                        _finding(
                            "VAL-L4-EVIDENCE-ROLE",
                            "error",
                            "L4",
                            "Core Evidence Role должен быть supports или contradicts",
                        )
                    )

        if record.get("publication_status") == "published":
            if isinstance(content, dict) and content.get("truth") is True:
                findings.append(
                    _finding(
                        "VAL-L4-PUBLICATION-TRUTH",
                        "error",
                        "L4",
                        "publication_status не может автоматически утверждать истинность",
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
            coverage={
                "L1": "executed",
                "L2": "executed",
                "L3": "executed",
                "L4": "executed",
                "L5": "not_implemented",
            },
        )

    @staticmethod
    def _validate_ref_shapes(record: dict[str, Any], findings: list[Finding]) -> None:
        def check_ref(value: Any, path: str) -> None:
            if not isinstance(value, dict) or not isinstance(value.get("record_id"), str):
                findings.append(
                    _finding(
                        "VAL-L3-REFERENCE-SHAPE",
                        "error",
                        "L3",
                        f"{path}: ссылка должна содержать record_id",
                    )
                )

        def check_many(values: Any, path: str) -> None:
            if values is None:
                return
            if not isinstance(values, list):
                findings.append(
                    _finding(
                        "VAL-L3-REFERENCE-LIST",
                        "error",
                        "L3",
                        f"{path}: ожидается список ссылок",
                    )
                )
                return
            for index, value in enumerate(values):
                check_ref(value, f"{path}[{index}]")

        provenance = record.get("provenance")
        if isinstance(provenance, dict):
            for key in ("agent_refs", "created_from", "transformed_from"):
                check_many(provenance.get(key), f"provenance.{key}")

        if record.get("record_type") == "claim":
            content = record.get("content", {})
            for key in ("scope_ref", "context_ref"):
                if key in content:
                    check_ref(content[key], f"content.{key}")
            check_many(content.get("referents"), "content.referents")
            check_many(content.get("relation_refs"), "content.relation_refs")

        elif record.get("record_type") == "evidence_use":
            content = record.get("content", {})
            for key in (
                "claim_ref",
                "source_ref",
                "resolution_context",
                "source_state_ref",
            ):
                if key in content:
                    check_ref(content[key], f"content.{key}")

        elif record.get("record_type") == "assessment":
            content = record.get("content", {})
            for key in (
                "target",
                "assessor_ref",
                "method_ref",
                "scale_ref",
                "profile_ref",
            ):
                if key in content:
                    check_ref(content[key], f"content.{key}")
            check_many(content.get("inputs"), "content.inputs")
