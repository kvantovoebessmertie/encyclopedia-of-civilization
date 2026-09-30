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
    assert all(code.startswith(("ID_", "CTX_", "SCOPE_", "SCP_", "S_", "P_", "RL_", "PROV_", "AUTH_", "TRUST_")) for code in rules)
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
        "P_TYPE_MODEL_001",
        "P_MODEL_EVIDENCE_001",
        "P_MODEL_IDENTITY_001",
        "P_HISTORICAL_EVIDENCE_001",
        "P_FRAME_001",
        "P_FRAME_CONTEXT_001",
        "P_PARTICIPANT_ROLES_001",
        "P_ATTRIBUTION_001",
        "P_BOUNDARY_EVENT_001",
        "P_OBSERVATION_BOUNDARY_001",
        "P_PHASE_EVENT_001",
        "P_EVENT_PROCESS_001",
        "P_STATE_SEQUENCE_001",
        "P_ACTION_CAUSE_001",
        "P_PURPOSE_001",
        "P_UNKNOWN_BOUNDARY_001",
        "P_OPEN_ENDED_001",
        "P_TIME_SCALES_001",
        "P_OBSERVATION_GAP_001",
        "P_INTERRUPTION_001",
        "P_RESUMPTION_IDENTITY_001",
        "P_CONTENT_IDENTITY_001",
        "P_DESCRIPTION_IDENTITY_001",
        "P_PROVENANCE_IDENTITY_001",
        "P_MERGE_SPLIT_001",
        "P_DECOMPOSITION_001",
        "P_CONTAINMENT_001",
        "P_OVERLAP_PARTOF_001",
        "P_DECOMPOSITION_CONFLICT_001",
        "P_TEMPORAL_CAUSALITY_001",
        "P_CAUSAL_CONTEXT_001",
        "P_FEEDBACK_001",
        "P_INPUT_CAUSATION_001",
        "P_OUTPUT_RESULT_001",
        "P_ENABLING_OCCURRENCE_001",
        "P_RECURRING_IDENTITY_001",
        "P_RATE_IDENTITY_001",
        "P_RATE_INTERVAL_001",
        "P_RATE_CUMULATIVE_001",
        "P_LOG_PROCESS_001",
        "P_WORKFLOW_OCCURRENCE_001",
        "P_SCOPE_001",
        "P_SCOPE_TRANSFER_001",
        "P_CONTEXT_DRIFT_001",
        "P_SIMULTANEOUS_CONFLICT_001",
        "P_INTERACTION_CAUSALITY_001",
        "P_PROVENANCE_001",
        "P_CONFLICT_RECONCILIATION_001",
        "P_HISTORICAL_CONTEXT_001",
        "P_REVISION_HISTORY_001",
        "S_STATE_ROLE_001",
        "S_SNAPSHOT_INTERVAL_001",
        "S_EVIDENCE_INTERVAL_001",
        "S_CONTINUITY_001",
        "S_OPEN_WORLD_001",
        "S_REPRESENTATION_HISTORY_001",
        "S_PROVENANCE_CONTINUITY_001",
        "S_VALUE_IDENTITY_001",
        "S_BREAK_CONTINUITY_001",
        "S_DETAILING_FIDELITY_001",
        "S_MEASUREMENT_CONTEXT_001",
        "S_CONFLICT_RECONCILIATION_001",
        "S_PART_WHOLE_001",
        "S_SAMPLE_POPULATION_001",
        "S_AGGREGATE_001",
        "S_CONTEXT_LINEAGE_001",
        "S_EFFECTIVE_TIME_001",
        "S_RELATIONAL_ROLE_001",
        "S_CAUSAL_SEQUENCE_001",
        "S_CLASSIFICATION_FIDELITY_001",
        "S_DECISION_TIME_001",
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
    cases = [
        ("SCP_ROLE_001", {"semantic_role_required": True}),
        ("SCP_TARGET_001", {"material_target": True}),
        ("SCP_UNIVERSE_001", {"universe_required": True, "universe_status": "unknown", "universe_fabricated": True}),
        ("SCP_QUANTIFIER_001", {"quantifier_required": True}),
        ("SCP_LEVEL_001", {"analysis_level_required": True}),
        ("SCP_EPISTEMIC_001", {"epistemic_status": "unknown", "epistemic_resolved": True}),
        ("SCP_APPLICABILITY_001", {"applicability_status": "proven", "declared_only": True}),
        ("SCP_UNKNOWN_001", {"status": "unknown", "universal": True}),
        ("SCP_CLOSURE_001", {"closure_mode": "closed"}),
        ("SCP_OPENWORLD_001", {"open_world": False, "closure_justified": False}),
        ("SCP_BOUNDARY_001", {"boundary_mode": "exact", "boundary_uncertain": True}),
        ("SCP_FUZZY_001", {"boundary_mode": "crisp", "fuzzy": True}),
        ("SCP_MEMBERSHIP_001", {"membership_status": "unknown", "membership_resolved": True}),
        ("SCP_DIMENSION_COUPLING_001", {"dimensions_coupled": True, "cartesian_product": True}),
        ("SCP_TUPLE_001", {"tuple_semantics": True}),
        ("SCP_TEMPORAL_001", {"temporal_validity_material": True}),
        ("SCP_TRANSFER_BASIS_001", {"transferability": "transferable"}),
        ("SCP_OVERLAP_001", {"overlap": True, "equivalent": True}),
        ("SCP_MISMATCH_001", {"mismatch": True, "contradiction": True}),
        ("SCP_INHERIT_COMPAT_001", {"inherited": True, "inheritance_compatible": False}),
        ("SCP_DERIVED_001", {"derived": True}),
        ("SCP_PROVENANCE_001", {"provenance_required": True}),
        ("SCP_FIDELITY_001", {"fidelity": "lost"}),
        ("SCP_COMPOSITION_001", {"composition": "union", "composition_justified": False}),
        ("SCP_ROLE_DRIFT_001", {"role_drift": True, "role_drift_detected": False}),
    ]
    for i, (rule, payload) in enumerate(cases):
        findings = validate_semantic_dataset([base(f"S{i}", "scope", {"scope_content": payload})])
        assert any(f.code == rule for f in findings), rule



def test_state_semantic_rules_all_directly_asserted():
    cases = [["S_STATE_ROLE_001",{"role":"desired"}],["S_SNAPSHOT_INTERVAL_001",{"snapshot":True,"interval":True}],["S_EVIDENCE_INTERVAL_001",{"evidence_snapshot":True,"validity_interval":True}],["S_CONTINUITY_001",{"repeated_observations":True,"continuous":True}],["S_OPEN_WORLD_001",{"no_change_evidence":True,"stable":True}],["S_REPRESENTATION_HISTORY_001",{"representation_changed":True,"state_changed":True}],["S_PROVENANCE_CONTINUITY_001",{"provenance_changed":True,"identity_changed":True}],["S_VALUE_IDENTITY_001",{"same_value":True,"same_identity":True}],["S_BREAK_CONTINUITY_001",{"gap":True,"same_interval":True}],["S_DETAILING_FIDELITY_001",{"detailing":True,"invented_property":True}],["S_MEASUREMENT_CONTEXT_001",{"measurement_conflict":True,"conflict":True}],["S_CONFLICT_RECONCILIATION_001",{"conflict":True,"conflict_asserted":True}],["S_PART_WHOLE_001",{"part_state":True,"whole_state":True}],["S_SAMPLE_POPULATION_001",{"sample_state":True,"population_state":True}],["S_AGGREGATE_001",{"aggregate":True,"identical_individuals":True}],["S_CONTEXT_LINEAGE_001",{"context_changed":True}],["S_EFFECTIVE_TIME_001",{"effective_time":True}],["S_RELATIONAL_ROLE_001",{"relational_roles_material":True}],["S_CAUSAL_SEQUENCE_001",{"state_sequence":True,"causal_chain":True}],["S_CLASSIFICATION_FIDELITY_001",{"classification":True,"original_properties_lost":True}],["S_DECISION_TIME_001",{"earlier_decision":True,"later_state_basis":True}]]
    for i, (rule, payload) in enumerate(cases):
        findings = validate_semantic_dataset([base(f"ST{i}", "state", {"state_content": payload})])
        assert any(f.code == rule for f in findings), rule


def test_process_semantic_rules_all_directly_asserted():
    cases = [["P_TYPE_MODEL_001",{"type_claimed":True,"model_claimed":True}],["P_MODEL_EVIDENCE_001",{"model_claimed":True,"historical_evidence":True}],["P_MODEL_IDENTITY_001",{"model_identity":True,"occurrence_identity":True}],["P_HISTORICAL_EVIDENCE_001",{"generic_knowledge":True,"historical_evidence":True}],["P_FRAME_001",{"frame_required":True}],["P_FRAME_CONTEXT_001",{"frame":True,"context":True}],["P_PARTICIPANT_ROLES_001",{"roles_material":True}],["P_ATTRIBUTION_001",{"attribution_required":True}],["P_BOUNDARY_EVENT_001",{"process_boundary":True,"event_asserted":True}],["P_OBSERVATION_BOUNDARY_001",{"observation_boundary":True,"process_boundary":True}],["P_PHASE_EVENT_001",{"phase_boundary":True,"event_asserted":True}],["P_EVENT_PROCESS_001",{"event_asserted":True,"process_asserted":True}],["P_STATE_SEQUENCE_001",{"state_sequence":True,"process_asserted":True}],["P_ACTION_CAUSE_001",{"action":True,"cause_or_control":True}],["P_PURPOSE_001",{"direction_observed":True,"purpose":True}],["P_UNKNOWN_BOUNDARY_001",{"boundary_unknown":True,"exact_boundary":True}],["P_OPEN_ENDED_001",{"open_ended":True,"permanent":True}],["P_TIME_SCALES_001",{"multiple_scales":True}],["P_OBSERVATION_GAP_001",{"observation_gap":True,"interrupted":True}],["P_INTERRUPTION_001",{"interrupted":True,"terminated":True}],["P_RESUMPTION_IDENTITY_001",{"resumed":True,"same_identity":True}],["P_CONTENT_IDENTITY_001",{"same_content":True,"same_identity":True}],["P_DESCRIPTION_IDENTITY_001",{"different_descriptions":True,"different_identity":True}],["P_PROVENANCE_IDENTITY_001",{"different_provenance":True,"different_identity":True}],["P_MERGE_SPLIT_001",{"merge_split":True,"continuity":True}],["P_DECOMPOSITION_001",{"decomposition":True,"invented_stage":True}],["P_CONTAINMENT_001",{"temporal_containment":True,"subprocess":True}],["P_OVERLAP_PARTOF_001",{"overlap":True,"part_of":True}],["P_DECOMPOSITION_CONFLICT_001",{"decomposition_conflict":True,"contradiction":True}],["P_TEMPORAL_CAUSALITY_001",{"temporal_order":True,"causal":True}],["P_CAUSAL_CONTEXT_001",{"causal_relation":True}],["P_FEEDBACK_001",{"pattern_observed":True,"feedback":True}],["P_INPUT_CAUSATION_001",{"input":True,"sole_cause":True}],["P_OUTPUT_RESULT_001",{"output":True,"result":True}],["P_ENABLING_OCCURRENCE_001",{"enabling_condition":True,"occurrence":True}],["P_RECURRING_IDENTITY_001",{"recurring":True,"same_identity":True}],["P_RATE_IDENTITY_001",{"rate":True,"identity":True}],["P_RATE_INTERVAL_001",{"point_rate":True,"constant_interval_rate":True}],["P_RATE_CUMULATIVE_001",{"rate_duration":True,"cumulative_change":True}],["P_LOG_PROCESS_001",{"log":True,"process_asserted":True}],["P_WORKFLOW_OCCURRENCE_001",{"workflow":True,"occurrence":True}],["P_SCOPE_001",{"process_scope":True,"observation_scope":True}],["P_SCOPE_TRANSFER_001",{"local_scope":True,"global_scope":True}],["P_CONTEXT_DRIFT_001",{"context_changed":True}],["P_SIMULTANEOUS_CONFLICT_001",{"simultaneous":True,"conflict":True}],["P_INTERACTION_CAUSALITY_001",{"interaction":True,"full_causal_mechanism":True}],["P_PROVENANCE_001",{"provenance_required":True}],["P_CONFLICT_RECONCILIATION_001",{"conflict":True,"conflict_asserted":True}],["P_HISTORICAL_CONTEXT_001",{"historical_process":True,"current_context_applied":True}],["P_REVISION_HISTORY_001",{"model_revision":True,"historical_changed":True}]]
    for i, (rule, payload) in enumerate(cases):
        findings = validate_semantic_dataset([base(f"P{i}", "process", {"process_content": payload})])
        assert any(f.code == rule for f in findings), rule


def test_relation_identity_semantic_debt_150_rules_all_directly_asserted():
    cases = [
        ("RL_01_001", {"semantic_violations": {"RL_01_001": True}}),
        ("RL_02_001", {"semantic_violations": {"RL_02_001": True}}),
        ("RL_03_001", {"semantic_violations": {"RL_03_001": True}}),
        ("RL_04_001", {"semantic_violations": {"RL_04_001": True}}),
        ("RL_05_001", {"semantic_violations": {"RL_05_001": True}}),
        ("RL_06_001", {"semantic_violations": {"RL_06_001": True}}),
        ("RL_07_001", {"semantic_violations": {"RL_07_001": True}}),
        ("RL_08_001", {"semantic_violations": {"RL_08_001": True}}),
        ("RL_09_001", {"semantic_violations": {"RL_09_001": True}}),
        ("RL_10_001", {"semantic_violations": {"RL_10_001": True}}),
        ("RL_11_001", {"semantic_violations": {"RL_11_001": True}}),
        ("RL_12_001", {"semantic_violations": {"RL_12_001": True}}),
        ("RL_13_001", {"semantic_violations": {"RL_13_001": True}}),
        ("RL_14_001", {"semantic_violations": {"RL_14_001": True}}),
        ("RL_15_001", {"semantic_violations": {"RL_15_001": True}}),
        ("RL_16_001", {"semantic_violations": {"RL_16_001": True}}),
        ("RL_17_001", {"semantic_violations": {"RL_17_001": True}}),
        ("RL_18_001", {"semantic_violations": {"RL_18_001": True}}),
        ("RL_19_001", {"semantic_violations": {"RL_19_001": True}}),
        ("RL_20_001", {"semantic_violations": {"RL_20_001": True}}),
        ("RL_21_001", {"semantic_violations": {"RL_21_001": True}}),
        ("RL_22_001", {"semantic_violations": {"RL_22_001": True}}),
        ("RL_23_001", {"semantic_violations": {"RL_23_001": True}}),
        ("RL_24_001", {"semantic_violations": {"RL_24_001": True}}),
        ("RL_25_001", {"semantic_violations": {"RL_25_001": True}}),
        ("RL_26_001", {"semantic_violations": {"RL_26_001": True}}),
        ("RL_27_001", {"semantic_violations": {"RL_27_001": True}}),
        ("RL_28_001", {"semantic_violations": {"RL_28_001": True}}),
        ("RL_29_001", {"semantic_violations": {"RL_29_001": True}}),
        ("RL_30_001", {"semantic_violations": {"RL_30_001": True}}),
        ("RL_31_001", {"semantic_violations": {"RL_31_001": True}}),
        ("RL_32_001", {"semantic_violations": {"RL_32_001": True}}),
        ("RL_33_001", {"semantic_violations": {"RL_33_001": True}}),
        ("RL_34_001", {"semantic_violations": {"RL_34_001": True}}),
        ("RL_35_001", {"semantic_violations": {"RL_35_001": True}}),
        ("RL_36_001", {"semantic_violations": {"RL_36_001": True}}),
        ("RL_37_001", {"semantic_violations": {"RL_37_001": True}}),
        ("RL_38_001", {"semantic_violations": {"RL_38_001": True}}),
        ("RL_39_001", {"semantic_violations": {"RL_39_001": True}}),
        ("RL_40_001", {"semantic_violations": {"RL_40_001": True}}),
        ("RL_41_001", {"semantic_violations": {"RL_41_001": True}}),
        ("RL_42_001", {"semantic_violations": {"RL_42_001": True}}),
        ("RL_43_001", {"semantic_violations": {"RL_43_001": True}}),
        ("RL_44_001", {"semantic_violations": {"RL_44_001": True}}),
        ("RL_45_001", {"semantic_violations": {"RL_45_001": True}}),
        ("RL_46_001", {"semantic_violations": {"RL_46_001": True}}),
        ("RL_47_001", {"semantic_violations": {"RL_47_001": True}}),
        ("RL_48_001", {"semantic_violations": {"RL_48_001": True}}),
        ("RL_49_001", {"semantic_violations": {"RL_49_001": True}}),
        ("RL_50_001", {"semantic_violations": {"RL_50_001": True}}),
        ("RL_51_001", {"semantic_violations": {"RL_51_001": True}}),
        ("RL_52_001", {"semantic_violations": {"RL_52_001": True}}),
        ("RL_53_001", {"semantic_violations": {"RL_53_001": True}}),
        ("RL_54_001", {"semantic_violations": {"RL_54_001": True}}),
        ("RL_55_001", {"semantic_violations": {"RL_55_001": True}}),
        ("RL_56_001", {"semantic_violations": {"RL_56_001": True}}),
        ("RL_57_001", {"semantic_violations": {"RL_57_001": True}}),
        ("RL_58_001", {"semantic_violations": {"RL_58_001": True}}),
        ("RL_59_001", {"semantic_violations": {"RL_59_001": True}}),
        ("RL_60_001", {"semantic_violations": {"RL_60_001": True}}),
        ("RL_61_001", {"semantic_violations": {"RL_61_001": True}}),
        ("RL_62_001", {"semantic_violations": {"RL_62_001": True}}),
        ("RL_63_001", {"semantic_violations": {"RL_63_001": True}}),
        ("RL_64_001", {"semantic_violations": {"RL_64_001": True}}),
        ("RL_65_001", {"semantic_violations": {"RL_65_001": True}}),
        ("RL_66_001", {"semantic_violations": {"RL_66_001": True}}),
        ("RL_67_001", {"semantic_violations": {"RL_67_001": True}}),
        ("RL_68_001", {"semantic_violations": {"RL_68_001": True}}),
        ("RL_69_001", {"semantic_violations": {"RL_69_001": True}}),
        ("RL_70_001", {"semantic_violations": {"RL_70_001": True}}),
        ("RL_71_001", {"semantic_violations": {"RL_71_001": True}}),
        ("RL_72_001", {"semantic_violations": {"RL_72_001": True}}),
        ("RL_73_001", {"semantic_violations": {"RL_73_001": True}}),
        ("RL_74_001", {"semantic_violations": {"RL_74_001": True}}),
        ("RL_75_001", {"semantic_violations": {"RL_75_001": True}}),
        ("RL_76_001", {"semantic_violations": {"RL_76_001": True}}),
        ("RL_77_001", {"semantic_violations": {"RL_77_001": True}}),
        ("RL_78_001", {"semantic_violations": {"RL_78_001": True}}),
        ("RL_79_001", {"semantic_violations": {"RL_79_001": True}}),
        ("RL_80_001", {"semantic_violations": {"RL_80_001": True}}),
        ("RL_81_001", {"semantic_violations": {"RL_81_001": True}}),
        ("RL_82_001", {"semantic_violations": {"RL_82_001": True}}),
        ("RL_83_001", {"semantic_violations": {"RL_83_001": True}}),
        ("RL_84_001", {"semantic_violations": {"RL_84_001": True}}),
        ("RL_85_001", {"semantic_violations": {"RL_85_001": True}}),
        ("RL_86_001", {"semantic_violations": {"RL_86_001": True}}),
        ("RL_87_001", {"semantic_violations": {"RL_87_001": True}}),
        ("RL_88_001", {"semantic_violations": {"RL_88_001": True}}),
        ("RL_89_001", {"semantic_violations": {"RL_89_001": True}}),
        ("RL_90_001", {"semantic_violations": {"RL_90_001": True}}),
        ("RL_91_001", {"semantic_violations": {"RL_91_001": True}}),
        ("RL_92_001", {"semantic_violations": {"RL_92_001": True}}),
        ("RL_93_001", {"semantic_violations": {"RL_93_001": True}}),
        ("RL_94_001", {"semantic_violations": {"RL_94_001": True}}),
        ("RL_95_001", {"semantic_violations": {"RL_95_001": True}}),
        ("RL_96_001", {"semantic_violations": {"RL_96_001": True}}),
        ("RL_97_001", {"semantic_violations": {"RL_97_001": True}}),
        ("RL_98_001", {"semantic_violations": {"RL_98_001": True}}),
        ("RL_99_001", {"semantic_violations": {"RL_99_001": True}}),
        ("RL_100_001", {"semantic_violations": {"RL_100_001": True}}),
        ("RL_101_001", {"semantic_violations": {"RL_101_001": True}}),
        ("RL_102_001", {"semantic_violations": {"RL_102_001": True}}),
        ("RL_103_001", {"semantic_violations": {"RL_103_001": True}}),
        ("RL_104_001", {"semantic_violations": {"RL_104_001": True}}),
        ("RL_105_001", {"semantic_violations": {"RL_105_001": True}}),
        ("RL_106_001", {"semantic_violations": {"RL_106_001": True}}),
        ("RL_107_001", {"semantic_violations": {"RL_107_001": True}}),
        ("RL_108_001", {"semantic_violations": {"RL_108_001": True}}),
        ("RL_109_001", {"semantic_violations": {"RL_109_001": True}}),
        ("RL_110_001", {"semantic_violations": {"RL_110_001": True}}),
        ("RL_111_001", {"semantic_violations": {"RL_111_001": True}}),
        ("RL_112_001", {"semantic_violations": {"RL_112_001": True}}),
        ("RL_113_001", {"semantic_violations": {"RL_113_001": True}}),
        ("RL_114_001", {"semantic_violations": {"RL_114_001": True}}),
        ("RL_115_001", {"semantic_violations": {"RL_115_001": True}}),
        ("ID_02_001", {"semantic_violations": {"ID_02_001": True}}),
        ("ID_03_001", {"semantic_violations": {"ID_03_001": True}}),
        ("ID_04_001", {"semantic_violations": {"ID_04_001": True}}),
        ("ID_05_001", {"semantic_violations": {"ID_05_001": True}}),
        ("ID_06_001", {"semantic_violations": {"ID_06_001": True}}),
        ("ID_07_001", {"semantic_violations": {"ID_07_001": True}}),
        ("ID_08_001", {"semantic_violations": {"ID_08_001": True}}),
        ("ID_09_001", {"semantic_violations": {"ID_09_001": True}}),
        ("ID_10_001", {"semantic_violations": {"ID_10_001": True}}),
        ("ID_11_001", {"semantic_violations": {"ID_11_001": True}}),
        ("ID_12_001", {"semantic_violations": {"ID_12_001": True}}),
        ("ID_13_001", {"semantic_violations": {"ID_13_001": True}}),
        ("ID_14_001", {"semantic_violations": {"ID_14_001": True}}),
        ("ID_15_001", {"semantic_violations": {"ID_15_001": True}}),
        ("ID_16_001", {"semantic_violations": {"ID_16_001": True}}),
        ("ID_17_001", {"semantic_violations": {"ID_17_001": True}}),
        ("ID_18_001", {"semantic_violations": {"ID_18_001": True}}),
        ("ID_19_001", {"semantic_violations": {"ID_19_001": True}}),
        ("ID_20_001", {"semantic_violations": {"ID_20_001": True}}),
        ("ID_21_001", {"semantic_violations": {"ID_21_001": True}}),
        ("ID_22_001", {"semantic_violations": {"ID_22_001": True}}),
        ("ID_23_001", {"semantic_violations": {"ID_23_001": True}}),
        ("ID_24_001", {"semantic_violations": {"ID_24_001": True}}),
        ("ID_25_001", {"semantic_violations": {"ID_25_001": True}}),
        ("ID_26_001", {"semantic_violations": {"ID_26_001": True}}),
        ("ID_27_001", {"semantic_violations": {"ID_27_001": True}}),
        ("ID_28_001", {"semantic_violations": {"ID_28_001": True}}),
    ]
    for i, (rule, payload) in enumerate(cases):
        record_type = "relation" if rule.startswith("RL_") else "identity_assertion"
        key = "relation_content" if record_type == "relation" else "identity"
        findings = validate_semantic_dataset([base(f"RI{i}", record_type, {key: payload})])
        assert any(f.code == rule for f in findings), rule


def test_remaining_state_process_semantic_rules_directly_asserted():
    cases = [
        ("S_EVENT_COUNT_001", {"semantic_violations": {"S_EVENT_COUNT_001": True}}),
        ("S_MEASUREMENT_SEMANTICS_001", {"semantic_violations": {"S_MEASUREMENT_SEMANTICS_001": True}}),
        ("S_QUALITATIVE_THRESHOLD_001", {"semantic_violations": {"S_QUALITATIVE_THRESHOLD_001": True}}),
        ("P_LIFECYCLE_SEMANTICS_001", {"semantic_violations": {"P_LIFECYCLE_SEMANTICS_001": True}}),
        ("P_STATE_CAUSAL_LINK_001", {"semantic_violations": {"P_STATE_CAUSAL_LINK_001": True}}),
        ("P_EVENT_CAUSAL_LINK_001", {"semantic_violations": {"P_EVENT_CAUSAL_LINK_001": True}}),
        ("P_PROFILE_CORE_001", {"semantic_violations": {"P_PROFILE_CORE_001": True}}),
        ("P_PROFILE_RESOLUTION_001", {"semantic_violations": {"P_PROFILE_RESOLUTION_001": True}}),
    ]
    for i, (rule, payload) in enumerate(cases):
        record_type = "state" if rule.startswith("S_") else "process"
        key = "state_content" if record_type == "state" else "process_content"
        findings = validate_semantic_dataset([base(f"SP{i}", record_type, {key: payload})])
        assert any(f.code == rule for f in findings), rule
