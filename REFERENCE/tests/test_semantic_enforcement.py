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
    assert all(code.startswith(("ID_", "CTX_", "SCOPE_", "PROV_", "AUTH_", "TRUST_")) for code in rules)
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
        "SCOPE_SAMPLE_POP_001", "SCOPE_INHERIT_001", "SCOPE_MEMBERSHIP_PROV_001",
        "SCP_ROLE_001",
        "SCP_TARGET_001",
        "SCP_UNIVERSE_001",
        "SCP_QUANTIFIER_001",
        "SCP_LEVEL_001",
        "SCP_EPISTEMIC_001",
        "SCP_APPLICABILITY_001",
        "SCP_UNKNOWN_001",
        "SCP_CLOSURE_001",
        "SCP_OPENWORLD_001",
        "SCP_BOUNDARY_001",
        "SCP_FUZZY_001",
        "SCP_MEMBERSHIP_001",
        "SCP_DIMENSION_COUPLING_001",
        "SCP_TUPLE_001",
        "SCP_TEMPORAL_001",
        "SCP_TRANSFER_BASIS_001",
        "SCP_OVERLAP_001",
        "SCP_MISMATCH_001",
        "SCP_INHERIT_COMPAT_001",
        "SCP_DERIVED_001",
        "SCP_PROVENANCE_001",
        "SCP_FIDELITY_001",
        "SCP_COMPOSITION_001",
        "SCP_ROLE_DRIFT_001",
        "ID_FRAME_001", "ID_CRITERION_001", "ID_SCOPE_001", "ID_UNCERTAINTY_001",
        "ID_SIMILARITY_001", "ID_ALIAS_001", "ID_HISTORY_001",
        "CTX_ROLE_001", "CTX_ASSUMPTION_001", "CTX_TRANSFER_CONFLICT_001",
        "PROV_SCOPE_001", "PROV_OPERATION_001", "PROV_JOINT_INPUT_001",
        "AUTH_TRANSLATION_001", "AUTH_SYNTHESIS_001", "AUTH_ORDER_001",
        "TRUST_REPUTATION_SIGNAL_001", "TRUST_AUTHORITY_001", "TRUST_EASY_CASES_001",
        "SCOPE_FIDELITY_001", "SCOPE_HISTORY_001", "SCOPE_ALGEBRA_001",
        "PROV_TYPE_001", "PROV_CYCLE_001", "PROV_INDEPENDENCE_001",
        "PROV_FIDELITY_001", "AUTH_ROLE_001", "AUTH_PSEUDONYM_001",
        "AUTH_CONFLICT_001", "AUTH_HISTORY_001", "TRUST_GOAL_001",
        "TRUST_CYCLE_001", "TRUST_INDEPENDENCE_001", "TRUST_HISTORY_001",
        "TRUST_TRANSFER_001", "TRUST_AGGREGATION_001",
    }
    assert set(registry()) == direct_codes


def test_scope_sample_to_population_generalization_requires_basis():
    records = [base("S1", "scope", {
        "scope_content": {"sample_to_population": True}
    })]
    assert any(f.code == "SCOPE_SAMPLE_POP_001" for f in validate_semantic_dataset(records))


def test_scope_inheritance_requires_resolvable_parent():
    records = [base("S1", "scope", {
        "scope_content": {
            "inheritance": {"parent_refs": [{"record_id": "MISSING", "version": "1"}]}
        }
    })]
    assert any(f.code == "SCOPE_INHERIT_001" for f in validate_semantic_dataset(records))


def test_scope_inheritance_cycle_is_rejected():
    records = [
        base("S1", "scope", {"scope_content": {
            "inheritance": {"parent_refs": [{"record_id": "S2", "version": "1"}]}
        }}),
        base("S2", "scope", {"scope_content": {
            "inheritance": {"parent_refs": [{"record_id": "S1", "version": "1"}]}
        }}),
    ]
    assert any(f.code == "SCOPE_INHERIT_001" for f in validate_semantic_dataset(records))


def test_scope_membership_provenance_requires_basis():
    records = [base("S1", "scope", {
        "scope_content": {
            "membership_provenance": {"status": "observed"}
        }
    })]
    assert any(f.code == "SCOPE_MEMBERSHIP_PROV_001" for f in validate_semantic_dataset(records))


def test_scope_fidelity_loss_requires_losses():
    records = [base("S1", "scope", {
        "scope_content": {"fidelity": {"status": "lost"}}
    })]
    assert any(f.code == "SCOPE_FIDELITY_001" for f in validate_semantic_dataset(records))


def test_historical_scope_requires_temporal_or_history_reference():
    records = [base("S1", "scope", {
        "scope_content": {"historical": True}
    })]
    assert any(f.code == "SCOPE_HISTORY_001" for f in validate_semantic_dataset(records))


def test_scope_algebra_union_requires_operands():
    records = [base("S1", "scope", {
        "scope_content": {"operation": "union"}
    })]
    assert any(f.code == "SCOPE_ALGEBRA_001" for f in validate_semantic_dataset(records))


def test_scope_algebra_mapping_requires_mapping_reference():
    records = [base("S1", "scope", {
        "scope_content": {"operation": "mapping"}
    })]
    assert any(f.code == "SCOPE_ALGEBRA_001" for f in validate_semantic_dataset(records))


def test_context_semantic_role_conflict_is_rejected():
    records = [base("C1", "context", {"context_content": {"semantic_role": "cause", "context_only": True}})]
    assert any(f.code == "CTX_ROLE_001" for f in validate_semantic_dataset(records))

def test_context_assumption_cannot_be_observed_silently():
    records = [base("C1", "context", {"context_content": {"assumption": True, "epistemic_status": "observed"}})]
    assert any(f.code == "CTX_ASSUMPTION_001" for f in validate_semantic_dataset(records))

def test_conflicting_context_cannot_be_unconditionally_transferable():
    records = [base("C1", "context", {"context_content": {"transferability": "transferable", "conflict": True}})]
    assert any(f.code == "CTX_TRANSFER_CONFLICT_001" for f in validate_semantic_dataset(records))

def test_component_provenance_requires_scope():
    records = [base("P1", "record", {"note": "x"}, provenance={"component_scope": True})]
    assert any(f.code == "PROV_SCOPE_001" for f in validate_semantic_dataset(records))

def test_specific_provenance_operation_cannot_be_unknown():
    records = [base("P1", "record", {"note": "x"}, provenance={"relation": "translated_from", "operation_semantics": "unknown", "specific_operation": True})]
    assert any(f.code == "PROV_OPERATION_001" for f in validate_semantic_dataset(records))

def test_joint_provenance_requires_input_group():
    records = [base("P1", "record", {"note": "x"}, provenance={"joint_inputs": True})]
    assert any(f.code == "PROV_JOINT_INPUT_001" for f in validate_semantic_dataset(records))

def test_translation_does_not_establish_original_authorship():
    records = [base("A1", "authorship_contribution", {"translation": True, "original_authorship": True})]
    assert any(f.code == "AUTH_TRANSLATION_001" for f in validate_semantic_dataset(records))

def test_synthesis_does_not_establish_source_authorship():
    records = [base("A1", "authorship_contribution", {"synthesis": True, "source_authorship": True})]
    assert any(f.code == "AUTH_SYNTHESIS_001" for f in validate_semantic_dataset(records))

def test_author_order_importance_requires_basis():
    records = [base("A1", "authorship_contribution", {"author_order_semantics": "importance"})]
    assert any(f.code == "AUTH_ORDER_001" for f in validate_semantic_dataset(records))

def test_reputation_signal_is_not_established_fact():
    records = [base("TR1", "trust_reputation", {"signal": True, "established_fact": True})]
    assert any(f.code == "TRUST_REPUTATION_SIGNAL_001" for f in validate_semantic_dataset(records))

def test_authority_does_not_establish_truth():
    records = [base("TR1", "trust_reputation", {"authority": True, "truth": True})]
    assert any(f.code == "TRUST_AUTHORITY_001" for f in validate_semantic_dataset(records))

def test_easy_case_success_does_not_establish_competence():
    records = [base("TR1", "trust_reputation", {"easy_case_selection": True, "competence": "high"})]
    assert any(f.code == "TRUST_EASY_CASES_001" for f in validate_semantic_dataset(records))


def test_resolved_identity_requires_frame():
    records = [base("I1", "identity_assertion", {"identity": {"assertion": True, "resolved": True}})]
    assert any(f.code == "ID_FRAME_001" for f in validate_semantic_dataset(records))

def test_resolved_identity_requires_criterion():
    records = [base("I1", "identity_assertion", {"identity": {"judgment": True, "resolved": True, "frame_ref": {"record_id": "F", "version": "1"}}})]
    assert any(f.code == "ID_CRITERION_001" for f in validate_semantic_dataset(records))

def test_identity_judgment_requires_scope():
    records = [base("I1", "identity_assertion", {"identity": {"judgment": True, "criterion": "legal"}})]
    assert any(f.code == "ID_SCOPE_001" for f in validate_semantic_dataset(records))

def test_uncertain_identity_cannot_be_resolved():
    records = [base("I1", "identity_assertion", {"identity": {"status": "disputed", "resolved": True}})]
    assert any(f.code == "ID_UNCERTAINTY_001" for f in validate_semantic_dataset(records))

def test_similarity_cannot_establish_identity():
    records = [base("I1", "identity_assertion", {"identity": {"similarity": 0.99, "resolved": True, "identity_basis": "similarity"}})]
    assert any(f.code == "ID_SIMILARITY_001" for f in validate_semantic_dataset(records))

def test_alias_identity_requires_basis():
    records = [base("I1", "identity_assertion", {"identity": {"alias": True, "resolved": True}})]
    assert any(f.code == "ID_ALIAS_001" for f in validate_semantic_dataset(records))

def test_historical_identity_requires_temporal_or_history_reference():
    records = [base("I1", "identity_assertion", {"identity": {"historical": True}})]
    assert any(f.code == "ID_HISTORY_001" for f in validate_semantic_dataset(records))


def test_scope_integrity_rules_all_directly_asserted():
    cases = [["SCP_ROLE_001",{"semantic_role_required":true}],["SCP_TARGET_001",{"material_target":true}],["SCP_UNIVERSE_001",{"universe_required":true,"universe_status":"unknown","universe_fabricated":true}],["SCP_QUANTIFIER_001",{"quantifier_required":true}],["SCP_LEVEL_001",{"analysis_level_required":true}],["SCP_EPISTEMIC_001",{"epistemic_status":"unknown","epistemic_resolved":true}],["SCP_APPLICABILITY_001",{"applicability_status":"proven","declared_only":true}],["SCP_UNKNOWN_001",{"status":"unknown","universal":true}],["SCP_CLOSURE_001",{"closure_mode":"closed"}],["SCP_OPENWORLD_001",{"open_world":false,"closure_justified":false}],["SCP_BOUNDARY_001",{"boundary_mode":"exact","boundary_uncertain":true}],["SCP_FUZZY_001",{"boundary_mode":"crisp","fuzzy":true}],["SCP_MEMBERSHIP_001",{"membership_status":"unknown","membership_resolved":true}],["SCP_DIMENSION_COUPLING_001",{"dimensions_coupled":true,"cartesian_product":true}],["SCP_TUPLE_001",{"tuple_semantics":true}],["SCP_TEMPORAL_001",{"temporal_validity_material":true}],["SCP_TRANSFER_BASIS_001",{"transferability":"transferable"}],["SCP_OVERLAP_001",{"overlap":true,"equivalent":true}],["SCP_MISMATCH_001",{"mismatch":true,"contradiction":true}],["SCP_INHERIT_COMPAT_001",{"inherited":true,"inheritance_compatible":false}],["SCP_DERIVED_001",{"derived":true}],["SCP_PROVENANCE_001",{"provenance_required":true}],["SCP_FIDELITY_001",{"fidelity":"lost"}],["SCP_COMPOSITION_001",{"composition":"union","composition_justified":false}],["SCP_ROLE_DRIFT_001",{"role_drift":true,"role_drift_detected":false}]]
    for i, (rule, payload) in enumerate(cases):
        findings = validate_semantic_dataset([base(f"S{i}", "scope", {"scope_content": payload})])
        assert any(f.code == rule for f in findings), rule
