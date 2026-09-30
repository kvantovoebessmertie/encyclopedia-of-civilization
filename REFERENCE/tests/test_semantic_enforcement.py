from __future__ import annotations

from pathlib import Path

from encyclopedia_reference.semantic_rules import registry, validate_semantic_dataset
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def base(record_id: str, record_type: str, content: dict, **extra) -> dict:
    return {
        "record_id": record_id,
        "record_type": record_type,
        "record_version": "1",
        "type_version": "1.0",
        "publication_status": "draft",
        "completion_status": "complete",
        "schema": "record/0.1",
        "provenance": {"method": "semantic-enforcement-test"},
        "content": content,
        **extra,
    }


def test_semantic_registry_has_stable_codes():
    rules = registry()
    assert len(rules) >= 20
    assert all(code.startswith(("CTX_", "SCOPE_", "PROV_", "AUTH_", "TRUST_")) for code in rules)
    assert all(item["status"] == "ENFORCED" for item in rules.values())


def test_context_inheritance_cycle_is_rejected():
    records = [
        base("C1", "context", {
            "context_content": {"inheritance": {"parent_refs": [{"record_id": "C2", "version": "1"}]}},
            "target_ref": {"record_id": "T", "version": "1"},
        }),
        base("C2", "context", {
            "context_content": {"inheritance": {"parent_refs": [{"record_id": "C1", "version": "1"}]}},
            "target_ref": {"record_id": "T", "version": "1"},
        }),
    ]
    findings = validate_semantic_dataset(records)
    assert any(f.code == "CTX_INHERIT_001" for f in findings)


def test_context_equal_precedence_conflict_is_rejected():
    records = [
        base("C1", "context", {
            "context_content": {"temperature": 10, "precedence": 1},
            "target_ref": {"record_id": "T", "version": "1"},
        }, valid_time={"start": "2026-01-01T00:00:00Z", "end": "2026-12-31T00:00:00Z"}),
        base("C2", "context", {
            "context_content": {"temperature": 20, "precedence": 1},
            "target_ref": {"record_id": "T", "version": "1"},
        }, valid_time={"start": "2026-06-01T00:00:00Z", "end": "2026-12-31T00:00:00Z"}),
    ]
    findings = validate_semantic_dataset(records)
    assert any(f.code == "CTX_CONFLICT_001" for f in findings)


def test_non_overlapping_contexts_do_not_conflict():
    records = [
        base("C1", "context", {
            "context_content": {"temperature": 10, "precedence": 1},
            "target_ref": {"record_id": "T", "version": "1"},
        }, valid_time={"start": "2026-01-01T00:00:00Z", "end": "2026-05-31T00:00:00Z"}),
        base("C2", "context", {
            "context_content": {"temperature": 20, "precedence": 1},
            "target_ref": {"record_id": "T", "version": "1"},
        }, valid_time={"start": "2026-06-01T00:00:00Z", "end": "2026-12-31T00:00:00Z"}),
    ]
    assert not any(f.code == "CTX_CONFLICT_001" for f in validate_semantic_dataset(records))


def test_provenance_cycle_is_rejected():
    records = [
        base("A", "record", {"note": "a"}, provenance={"created_from": [{"record_id": "B", "version": "1"}]}),
        base("B", "record", {"note": "b"}, provenance={"created_from": [{"record_id": "A", "version": "1"}]}),
    ]
    assert any(f.code == "PROV_CYCLE_001" for f in validate_semantic_dataset(records))


def test_pseudonymous_attribution_is_not_resolved_person():
    records = [base("A", "authorship_contribution", {
        "target_ref": {"record_id": "DOC", "version": "1"},
        "contributor_ref": {"record_id": "PSEUDO", "version": "1"},
        "contribution": "author",
        "contributor_kind": "pseudonymous",
        "resolved_person_ref": {"record_id": "PERSON", "version": "1"},
    })]
    assert any(f.code == "AUTH_PSEUDONYM_001" for f in validate_semantic_dataset(records))


def test_trust_cycle_is_rejected():
    records = [
        base("T1", "trust_reputation", {
            "target_ref": {"record_id": "A", "version": "1"},
            "assessment_type": "trust",
            "basis_refs": [{"record_id": "E", "version": "1"}],
            "subject_ref": {"record_id": "T2", "version": "1"},
            "goal_ref": {"record_id": "G", "version": "1"},
        }, type_version="1.1"),
        base("T2", "trust_reputation", {
            "target_ref": {"record_id": "B", "version": "1"},
            "assessment_type": "trust",
            "basis_refs": [{"record_id": "E", "version": "1"}],
            "subject_ref": {"record_id": "T1", "version": "1"},
            "goal_ref": {"record_id": "G", "version": "1"},
        }, type_version="1.1"),
    ]
    assert any(f.code == "TRUST_CYCLE_001" for f in validate_semantic_dataset(records))


def test_validator_dataset_executes_semantic_registry():
    records = [base("C", "context", {
        "context_content": {"condition": "lab"},
        "target_ref": {"record_id": "T", "version": "1"},
    })]
    result = Validator(SCHEMA).validate_dataset(records, SCHEMA)
    assert result.coverage["semantic_registry"] == "executed"
