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


# Direct regression coverage for every registered L4/L5 semantic rule.
def test_context_precedence_type_is_rejected():
    records = [base("C1", "context", {
        "context_content": {"temperature": 10, "precedence": "high"},
        "target_ref": {"record_id": "T", "version": "1"},
    })]
    assert any(f.code == "CTX_PRECEDENCE_001" for f in validate_semantic_dataset(records))


def test_context_positive_transferability_requires_basis():
    records = [base("C1", "context", {
        "context_content": {
            "transferability": {"status": "transferable"}
        },
        "target_ref": {"record_id": "T", "version": "1"},
    })]
    assert any(f.code == "CTX_TRANSFER_001" for f in validate_semantic_dataset(records))


def test_context_fidelity_loss_requires_losses():
    records = [base("C1", "context", {
        "context_content": {"fidelity": {"status": "lost"}},
        "target_ref": {"record_id": "T", "version": "1"},
    })]
    assert any(f.code == "CTX_FIDELITY_001" for f in validate_semantic_dataset(records))


def test_context_dimension_dependencies_must_be_list():
    records = [base("C1", "context", {
        "context_content": {"dimension_dependencies": "temperature"},
        "target_ref": {"record_id": "T", "version": "1"},
    })]
    assert any(f.code == "CTX_DIMENSION_001" for f in validate_semantic_dataset(records))


def test_scope_unknown_quantifier_is_rejected():
    records = [base("S1", "scope", {
        "scope_content": {"quantifier": "sometimes"}
    })]
    assert any(f.code == "SCOPE_QUANT_001" for f in validate_semantic_dataset(records))


def test_scope_dimensions_must_be_list():
    records = [base("S1", "scope", {
        "scope_content": {"dimensions": {"temperature": "high"}}
    })]
    assert any(f.code == "SCOPE_TUPLE_001" for f in validate_semantic_dataset(records))


def test_scope_universal_transfer_is_rejected():
    records = [base("S1", "scope", {
        "scope_content": {"transferability": "universal"}
    })]
    assert any(f.code == "SCOPE_TRANSFER_001" for f in validate_semantic_dataset(records))


def test_unknown_provenance_relation_is_rejected():
    records = [base("P1", "record", {"note": "x"},
        provenance={"relation": "teleported_from"})]
    assert any(f.code == "PROV_TYPE_001" for f in validate_semantic_dataset(records))


def test_provenance_independence_conflicts_with_lineage():
    records = [base("P1", "record", {"note": "x"},
        provenance={
            "independent": True,
            "created_from": [{"record_id": "SRC", "version": "1"}],
        })]
    assert any(f.code == "PROV_INDEPENDENCE_001" for f in validate_semantic_dataset(records))


def test_provenance_fidelity_loss_requires_losses():
    records = [base("P1", "record", {"note": "x"},
        provenance={"fidelity": {"status": "lost"}})]
    assert any(f.code == "PROV_FIDELITY_001" for f in validate_semantic_dataset(records))


def test_tool_use_is_not_automatically_authorship():
    records = [base("A1", "authorship_contribution", {
        "tool_use": True,
        "contribution": "author",
    })]
    assert any(f.code == "AUTH_ROLE_001" for f in validate_semantic_dataset(records))


def test_disputed_authorship_cannot_be_confirmed():
    records = [base("A1", "authorship_contribution", {
        "attribution_status": "disputed",
        "confirmed": True,
    })]
    assert any(f.code == "AUTH_CONFLICT_001" for f in validate_semantic_dataset(records))


def test_historical_authorship_requires_temporal_or_history_reference():
    records = [base("A1", "authorship_contribution", {
        "historical_attribution": True,
    })]
    assert any(f.code == "AUTH_HISTORY_001" for f in validate_semantic_dataset(records))


def test_trust_requires_subject_and_goal():
    records = [base("TR1", "trust_reputation", {
        "assessment_type": "trust",
    })]
    findings = validate_semantic_dataset(records)
    assert sum(f.code == "TRUST_GOAL_001" for f in findings) == 2


def test_trust_independence_requires_more_than_common_root():
    records = [base("TR1", "trust_reputation", {
        "independence_status": "independent",
        "common_root_ref": {"record_id": "ROOT", "version": "1"},
    })]
    assert any(f.code == "TRUST_INDEPENDENCE_001" for f in validate_semantic_dataset(records))


def test_historical_trust_requires_temporal_or_history_reference():
    records = [base("TR1", "trust_reputation", {
        "historical": True,
    })]
    assert any(f.code == "TRUST_HISTORY_001" for f in validate_semantic_dataset(records))


def test_trust_universal_transfer_is_rejected():
    records = [base("TR1", "trust_reputation", {
        "transferability": "universal",
    })]
    assert any(f.code == "TRUST_TRANSFER_001" for f in validate_semantic_dataset(records))


def test_trust_aggregation_does_not_prove_truth():
    records = [base("TR1", "trust_reputation", {
        "aggregation": {"method": "majority"},
        "truth": True,
    })]
    assert any(f.code == "TRUST_AGGREGATION_001" for f in validate_semantic_dataset(records))


def test_every_registered_l4_l5_rule_has_direct_regression_marker():
    direct_codes = {
        "CTX_INHERIT_001", "CTX_PRECEDENCE_001", "CTX_CONFLICT_001",
        "CTX_TRANSFER_001", "CTX_FIDELITY_001", "CTX_DIMENSION_001",
        "SCOPE_QUANT_001", "SCOPE_TUPLE_001", "SCOPE_TRANSFER_001",
        "PROV_TYPE_001", "PROV_CYCLE_001", "PROV_INDEPENDENCE_001",
        "PROV_FIDELITY_001", "AUTH_ROLE_001", "AUTH_PSEUDONYM_001",
        "AUTH_CONFLICT_001", "AUTH_HISTORY_001", "TRUST_GOAL_001",
        "TRUST_CYCLE_001", "TRUST_INDEPENDENCE_001", "TRUST_HISTORY_001",
        "TRUST_TRANSFER_001", "TRUST_AGGREGATION_001",
    }
    assert set(registry()) == direct_codes
