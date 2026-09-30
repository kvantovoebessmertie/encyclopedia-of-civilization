from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class SemanticRule:
    rule_id: str
    owner: str
    family: str
    status: str = "ENFORCED"


# Stable machine-facing rule registry. Context-dependent rules are enforced
# only when their explicit machine representation is present; otherwise they
# remain non-applicable rather than being guessed.
RULES = (
    SemanticRule("SCP_ROLE_001", "L4", "scope.semantic_role"),
    SemanticRule("SCP_TARGET_001", "L4", "scope.target"),
    SemanticRule("SCP_UNIVERSE_001", "L4", "scope.universe"),
    SemanticRule("SCP_QUANTIFIER_001", "L4", "scope.quantifier_preservation"),
    SemanticRule("SCP_LEVEL_001", "L4", "scope.analysis_level"),
    SemanticRule("SCP_EPISTEMIC_001", "L4", "scope.epistemic_status"),
    SemanticRule("SCP_APPLICABILITY_001", "L4", "scope.applicability"),
    SemanticRule("SCP_UNKNOWN_001", "L4", "scope.unknown_discipline"),
    SemanticRule("SCP_CLOSURE_001", "L4", "scope.closure"),
    SemanticRule("SCP_OPENWORLD_001", "L4", "scope.open_world"),
    SemanticRule("SCP_BOUNDARY_001", "L4", "scope.boundary"),
    SemanticRule("SCP_FUZZY_001", "L4/L5", "scope.fuzzy_boundary"),
    SemanticRule("SCP_MEMBERSHIP_001", "L4", "scope.membership_status"),
    SemanticRule("SCP_DIMENSION_COUPLING_001", "L4/L5", "scope.dimension_coupling"),
    SemanticRule("SCP_TUPLE_001", "L5", "scope.tuple_integrity"),
    SemanticRule("SCP_TEMPORAL_001", "L5", "scope.temporal_role"),
    SemanticRule("SCP_TRANSFER_BASIS_001", "L4/L5", "scope.transfer_basis"),
    SemanticRule("SCP_OVERLAP_001", "L4", "scope.overlap"),
    SemanticRule("SCP_MISMATCH_001", "L4", "scope.mismatch"),
    SemanticRule("SCP_INHERIT_COMPAT_001", "L4/L5", "scope.inheritance_compatibility"),
    SemanticRule("SCP_DERIVED_001", "L5", "scope.derived_scope"),
    SemanticRule("SCP_PROVENANCE_001", "L4/L5", "scope.provenance"),
    SemanticRule("SCP_FIDELITY_001", "L5", "scope.fidelity_preservation"),
    SemanticRule("SCP_COMPOSITION_001", "L5", "scope.composition"),
    SemanticRule("SCP_ROLE_DRIFT_001", "L5", "scope.role_drift"),
    SemanticRule("S_STATE_ROLE_001", "L4/L5", "state.s_state_role_001"),
    
    SemanticRule("S_SNAPSHOT_INTERVAL_001", "L4/L5", "state.s_snapshot_interval_001"),
    SemanticRule("S_EVIDENCE_INTERVAL_001", "L4/L5", "state.s_evidence_interval_001"),
    SemanticRule("S_CONTINUITY_001", "L4/L5", "state.s_continuity_001"),
    SemanticRule("S_OPEN_WORLD_001", "L4/L5", "state.s_open_world_001"),
    SemanticRule("S_REPRESENTATION_HISTORY_001", "L4/L5", "state.s_representation_history_001"),
    SemanticRule("S_PROVENANCE_CONTINUITY_001", "L4/L5", "state.s_provenance_continuity_001"),
    SemanticRule("S_VALUE_IDENTITY_001", "L4/L5", "state.s_value_identity_001"),
    SemanticRule("S_BREAK_CONTINUITY_001", "L4/L5", "state.s_break_continuity_001"),
    SemanticRule("S_DETAILING_FIDELITY_001", "L4/L5", "state.s_detailing_fidelity_001"),
    SemanticRule("S_MEASUREMENT_CONTEXT_001", "L4/L5", "state.s_measurement_context_001"),
    SemanticRule("S_CONFLICT_RECONCILIATION_001", "L4/L5", "state.s_conflict_reconciliation_001"),
    SemanticRule("S_PART_WHOLE_001", "L4/L5", "state.s_part_whole_001"),
    SemanticRule("S_SAMPLE_POPULATION_001", "L4/L5", "state.s_sample_population_001"),
    SemanticRule("S_AGGREGATE_001", "L4/L5", "state.s_aggregate_001"),
    SemanticRule("S_CONTEXT_LINEAGE_001", "L4/L5", "state.s_context_lineage_001"),
    SemanticRule("S_EFFECTIVE_TIME_001", "L4/L5", "state.s_effective_time_001"),
    SemanticRule("S_RELATIONAL_ROLE_001", "L4/L5", "state.s_relational_role_001"),
    SemanticRule("S_CAUSAL_SEQUENCE_001", "L4/L5", "state.s_causal_sequence_001"),
    SemanticRule("S_CLASSIFICATION_FIDELITY_001", "L4/L5", "state.s_classification_fidelity_001"),
    SemanticRule("S_DECISION_TIME_001", "L4/L5", "state.s_decision_time_001"),
    SemanticRule("P_TYPE_MODEL_001", "L4/L5", "process.p_type_model_001"),
    SemanticRule("P_MODEL_EVIDENCE_001", "L4/L5", "process.p_model_evidence_001"),
    SemanticRule("P_MODEL_IDENTITY_001", "L4/L5", "process.p_model_identity_001"),
    SemanticRule("P_HISTORICAL_EVIDENCE_001", "L4/L5", "process.p_historical_evidence_001"),
    SemanticRule("P_FRAME_001", "L4/L5", "process.p_frame_001"),
    SemanticRule("P_FRAME_CONTEXT_001", "L4/L5", "process.p_frame_context_001"),
    SemanticRule("P_PARTICIPANT_ROLES_001", "L4/L5", "process.p_participant_roles_001"),
    SemanticRule("P_ATTRIBUTION_001", "L4/L5", "process.p_attribution_001"),
    SemanticRule("P_BOUNDARY_EVENT_001", "L4/L5", "process.p_boundary_event_001"),
    SemanticRule("P_OBSERVATION_BOUNDARY_001", "L4/L5", "process.p_observation_boundary_001"),
    SemanticRule("P_PHASE_EVENT_001", "L4/L5", "process.p_phase_event_001"),
    SemanticRule("P_EVENT_PROCESS_001", "L4/L5", "process.p_event_process_001"),
    SemanticRule("P_STATE_SEQUENCE_001", "L4/L5", "process.p_state_sequence_001"),
    SemanticRule("P_ACTION_CAUSE_001", "L4/L5", "process.p_action_cause_001"),
    SemanticRule("P_PURPOSE_001", "L4/L5", "process.p_purpose_001"),
    SemanticRule("P_UNKNOWN_BOUNDARY_001", "L4/L5", "process.p_unknown_boundary_001"),
    SemanticRule("P_OPEN_ENDED_001", "L4/L5", "process.p_open_ended_001"),
    SemanticRule("P_TIME_SCALES_001", "L4/L5", "process.p_time_scales_001"),
    SemanticRule("P_OBSERVATION_GAP_001", "L4/L5", "process.p_observation_gap_001"),
    SemanticRule("P_INTERRUPTION_001", "L4/L5", "process.p_interruption_001"),
    SemanticRule("P_RESUMPTION_IDENTITY_001", "L4/L5", "process.p_resumption_identity_001"),
    SemanticRule("P_CONTENT_IDENTITY_001", "L4/L5", "process.p_content_identity_001"),
    SemanticRule("P_DESCRIPTION_IDENTITY_001", "L4/L5", "process.p_description_identity_001"),
    SemanticRule("P_PROVENANCE_IDENTITY_001", "L4/L5", "process.p_provenance_identity_001"),
    SemanticRule("P_MERGE_SPLIT_001", "L4/L5", "process.p_merge_split_001"),
    SemanticRule("P_DECOMPOSITION_001", "L4/L5", "process.p_decomposition_001"),
    SemanticRule("P_CONTAINMENT_001", "L4/L5", "process.p_containment_001"),
    SemanticRule("P_OVERLAP_PARTOF_001", "L4/L5", "process.p_overlap_partof_001"),
    SemanticRule("P_DECOMPOSITION_CONFLICT_001", "L4/L5", "process.p_decomposition_conflict_001"),
    SemanticRule("P_TEMPORAL_CAUSALITY_001", "L4/L5", "process.p_temporal_causality_001"),
    SemanticRule("P_CAUSAL_CONTEXT_001", "L4/L5", "process.p_causal_context_001"),
    SemanticRule("P_FEEDBACK_001", "L4/L5", "process.p_feedback_001"),
    SemanticRule("P_INPUT_CAUSATION_001", "L4/L5", "process.p_input_causation_001"),
    SemanticRule("P_OUTPUT_RESULT_001", "L4/L5", "process.p_output_result_001"),
    SemanticRule("P_ENABLING_OCCURRENCE_001", "L4/L5", "process.p_enabling_occurrence_001"),
    SemanticRule("P_RECURRING_IDENTITY_001", "L4/L5", "process.p_recurring_identity_001"),
    SemanticRule("P_RATE_IDENTITY_001", "L4/L5", "process.p_rate_identity_001"),
    SemanticRule("P_RATE_INTERVAL_001", "L4/L5", "process.p_rate_interval_001"),
    SemanticRule("P_RATE_CUMULATIVE_001", "L4/L5", "process.p_rate_cumulative_001"),
    SemanticRule("P_LOG_PROCESS_001", "L4/L5", "process.p_log_process_001"),
    SemanticRule("P_WORKFLOW_OCCURRENCE_001", "L4/L5", "process.p_workflow_occurrence_001"),
    SemanticRule("P_SCOPE_001", "L4/L5", "process.p_scope_001"),
    SemanticRule("P_SCOPE_TRANSFER_001", "L4/L5", "process.p_scope_transfer_001"),
    SemanticRule("P_CONTEXT_DRIFT_001", "L4/L5", "process.p_context_drift_001"),
    SemanticRule("P_SIMULTANEOUS_CONFLICT_001", "L4/L5", "process.p_simultaneous_conflict_001"),
    SemanticRule("P_INTERACTION_CAUSALITY_001", "L4/L5", "process.p_interaction_causality_001"),
    SemanticRule("P_PROVENANCE_001", "L4/L5", "process.p_provenance_001"),
    SemanticRule("P_CONFLICT_RECONCILIATION_001", "L4/L5", "process.p_conflict_reconciliation_001"),
    SemanticRule("P_HISTORICAL_CONTEXT_001", "L4/L5", "process.p_historical_context_001"),
    SemanticRule("P_REVISION_HISTORY_001", "L4/L5", "process.p_revision_history_001"),
    SemanticRule("RL_01_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_02_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_03_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_04_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_05_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_06_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_07_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_08_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_09_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_10_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_11_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_12_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_13_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_14_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_15_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_16_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_17_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_18_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_19_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_20_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_21_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_22_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_23_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_24_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_25_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_26_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_27_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_28_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_29_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_30_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_31_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_32_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_33_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_34_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_35_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_36_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_37_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_38_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_39_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_40_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_41_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_42_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_43_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_44_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_45_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_46_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_47_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_48_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_49_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_50_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_51_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_52_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_53_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_54_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_55_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_56_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_57_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_58_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_59_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_60_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_61_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_62_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_63_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_64_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_65_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_66_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_67_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_68_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_69_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_70_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_71_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_72_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_73_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_74_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_75_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_76_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_77_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_78_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_79_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_80_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_81_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_82_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_83_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_84_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_85_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_86_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_87_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_88_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_89_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_90_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_91_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_92_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_93_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_94_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_95_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_96_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_97_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_98_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_99_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_100_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_101_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_102_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_103_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_104_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_105_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_106_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_107_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_108_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_109_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_110_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_111_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_112_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_113_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_114_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("RL_115_001", "L4/L5", "relation."+x.toLowerCase()),
    SemanticRule("ID_02_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_03_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_04_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_05_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_06_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_07_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_08_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_09_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_10_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_11_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_12_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_13_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_14_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_15_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_16_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_17_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_18_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_19_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_20_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_21_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_22_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_23_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_24_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_25_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_26_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_27_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_28_001", "L4/L5", "identity."+x.toLowerCase()),
    SemanticRule("ID_FRAME_001", "L4", "identity.frame"),
    SemanticRule("ID_CRITERION_001", "L4", "identity.criterion"),
    SemanticRule("ID_SCOPE_001", "L4", "identity.scope"),
    SemanticRule("ID_UNCERTAINTY_001", "L4/L5", "identity.uncertainty"),
    SemanticRule("ID_SIMILARITY_001", "L4", "identity.similarity"),
    SemanticRule("ID_ALIAS_001", "L4", "identity.alias"),
    SemanticRule("ID_HISTORY_001", "L5", "identity.history"),
    SemanticRule("CTX_INHERIT_001", "L4", "context.inheritance"),
    SemanticRule("CTX_PRECEDENCE_001", "L4", "context.precedence"),
    SemanticRule("CTX_CONFLICT_001", "L4", "context.conflict"),
    SemanticRule("CTX_TRANSFER_001", "L4/L5", "context.transferability"),
    SemanticRule("CTX_FIDELITY_001", "L5", "context.fidelity"),
    SemanticRule("CTX_DIMENSION_001", "L4", "context.dimension_dependency"),
    SemanticRule("CTX_ROLE_001", "L4", "context.semantic_role"),
    SemanticRule("CTX_ASSUMPTION_001", "L4", "context.assumption"),
    SemanticRule("CTX_TRANSFER_CONFLICT_001", "L4/L5", "context.transfer_conflict"),
    SemanticRule("SCOPE_QUANT_001", "L4", "scope.quantifier"),
    SemanticRule("SCOPE_TUPLE_001", "L4", "scope.multidimensional"),
    SemanticRule("SCOPE_TRANSFER_001", "L4/L5", "scope.transferability"),
    SemanticRule("SCOPE_SAMPLE_POP_001", "L4", "scope.sample_population"),
    SemanticRule("SCOPE_INHERIT_001", "L4/L5", "scope.inheritance"),
    SemanticRule("SCOPE_MEMBERSHIP_PROV_001", "L4", "scope.membership_provenance"),
    SemanticRule("SCOPE_FIDELITY_001", "L5", "scope.fidelity"),
    SemanticRule("SCOPE_HISTORY_001", "L5", "scope.history"),
    SemanticRule("SCOPE_ALGEBRA_001", "L4", "scope.algebra"),
    SemanticRule("PROV_TYPE_001", "L4", "provenance.relation_type"),
    SemanticRule("PROV_CYCLE_001", "L4", "provenance.cycle"),
    SemanticRule("PROV_INDEPENDENCE_001", "L4/L5", "provenance.independence"),
    SemanticRule("PROV_FIDELITY_001", "L5", "provenance.fidelity"),
    SemanticRule("PROV_SCOPE_001", "L4", "provenance.component_scope"),
    SemanticRule("PROV_OPERATION_001", "L4", "provenance.operation_semantics"),
    SemanticRule("PROV_JOINT_INPUT_001", "L4", "provenance.joint_inputs"),
    SemanticRule("AUTH_ROLE_001", "L4", "authorship.role"),
    SemanticRule("AUTH_PSEUDONYM_001", "L4", "authorship.pseudonym"),
    SemanticRule("AUTH_CONFLICT_001", "L4", "authorship.conflict"),
    SemanticRule("AUTH_HISTORY_001", "L5", "authorship.history"),
    SemanticRule("AUTH_TRANSLATION_001", "L4", "authorship.translation"),
    SemanticRule("AUTH_SYNTHESIS_001", "L4", "authorship.synthesis"),
    SemanticRule("AUTH_ORDER_001", "L4", "authorship.order_semantics"),
    SemanticRule("TRUST_GOAL_001", "L4", "trust.goal"),
    SemanticRule("TRUST_CYCLE_001", "L4", "trust.cycle"),
    SemanticRule("TRUST_INDEPENDENCE_001", "L4/L5", "trust.independence"),
    SemanticRule("TRUST_HISTORY_001", "L5", "trust.history"),
    SemanticRule("TRUST_TRANSFER_001", "L5", "trust.transferability"),
    SemanticRule("TRUST_AGGREGATION_001", "L5", "trust.aggregation"),
    SemanticRule("TRUST_REPUTATION_SIGNAL_001", "L4", "trust.signal"),
    SemanticRule("TRUST_AUTHORITY_001", "L5", "trust.authority"),
    SemanticRule("TRUST_EASY_CASES_001", "L5", "trust.selection_bias"),
)


def registry() -> dict[str, dict[str, str]]:
    return {
        r.rule_id: {"owner": r.owner, "family": r.family, "status": r.status}
        for r in RULES
    }


def _finding(code: str, layer: str, message: str, subject: str | None = None):
    # Imported lazily to avoid a module cycle at import time.
    from .validator import Finding
    return Finding(code, "error", layer, message, subject=subject, rule=code)


def _ref_key(ref: Any) -> tuple[str, str | None] | None:
    if not isinstance(ref, dict) or not isinstance(ref.get("record_id"), str):
        return None
    return ref["record_id"], ref.get("version")


def _time_bounds(record: dict[str, Any]) -> tuple[datetime | None, datetime | None]:
    value = record.get("valid_time")
    if not isinstance(value, dict):
        return None, None
    start = value.get("start")
    end = value.get("end")
    def parse(v: Any) -> datetime | None:
        if not isinstance(v, str):
            return None
        try:
            return datetime.fromisoformat(v.replace("Z", "+00:00"))
        except ValueError:
            return None
    return parse(start), parse(end)


def _overlap(a: dict[str, Any], b: dict[str, Any]) -> bool:
    a0, a1 = _time_bounds(a)
    b0, b1 = _time_bounds(b)
    if a0 is None or b0 is None:
        # Without a complete temporal frame, conflict cannot be established.
        return False
    a1 = a1 or datetime.max.replace(tzinfo=a0.tzinfo)
    b1 = b1 or datetime.max.replace(tzinfo=b0.tzinfo)
    return max(a0, b0) <= min(a1, b1)


def _walk_refs(value: Any, path: str = ""):
    if isinstance(value, dict):
        if isinstance(value.get("record_id"), str):
            yield path, value
            return
        for key, child in value.items():
            if key == "extensions":
                continue
            yield from _walk_refs(child, f"{path}.{key}" if path else key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from _walk_refs(child, f"{path}[{i}]")


def _graph_cycle(edges: dict[str, set[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for child in edges.get(node, set()):
            if visit(child):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(n) for n in edges)


def validate_semantic_dataset(records: list[dict[str, Any]]) -> list:
    findings = []
    by_id = {r.get("record_id"): r for r in records if isinstance(r.get("record_id"), str)}

    # Identity: explicit safeguards prevent names/similarity/aliases from silently
    # becoming resolved identity, and require material frame/criterion/scope.
    for record in records:
        if record.get("record_type") not in {"identity", "identity_assertion", "relation", "claim"}:
            continue
        rid = record.get("record_id")
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        ident = c.get("identity") if isinstance(c.get("identity"), dict) else c
        if not isinstance(ident, dict):
            continue
        if ident.get("assertion") is True and ident.get("resolved") is True and not ident.get("frame_ref"):
            findings.append(_finding("ID_FRAME_001", "L4", "resolved identity requires resolvable frame_ref", rid))
        if ident.get("judgment") is True and ident.get("resolved") is True and not ident.get("criterion"):
            findings.append(_finding("ID_CRITERION_001", "L4", "resolved identity requires explicit criterion", rid))
        if ident.get("judgment") is True and not ident.get("scope"):
            findings.append(_finding("ID_SCOPE_001", "L4", "identity judgment requires explicit scope", rid))
        if ident.get("status") in {"possible", "probable", "disputed", "uncertain"} and ident.get("resolved") is True:
            findings.append(_finding("ID_UNCERTAINTY_001", "L4/L5", "uncertain identity cannot be represented as resolved", rid))
        if ident.get("similarity") is not None and ident.get("resolved") is True and ident.get("identity_basis") == "similarity":
            findings.append(_finding("ID_SIMILARITY_001", "L4", "similarity alone cannot establish identity", rid))
        if ident.get("alias") is True and ident.get("resolved") is True and not ident.get("alias_basis"):
            findings.append(_finding("ID_ALIAS_001", "L4", "alias-based identity requires explicit basis", rid))
        if ident.get("historical") is True and not (record.get("valid_time") or ident.get("history_ref")):
            findings.append(_finding("ID_HISTORY_001", "L5", "historical identity requires temporal or history reference", rid))


    # Relation / Identity semantic-debt package.
    # These guards operate only on explicit machine-declared violation flags.
    # No missing semantics are guessed; an absent flag is non-applicable.
    for record in records:
        if record.get("record_type") not in {"relation", "relation_assertion", "identity_assertion", "identity"}:
            continue
        rid = record.get("record_id")
        content = record.get("content", {})
        if not isinstance(content, dict):
            continue
        payload = content.get("relation_content") if record.get("record_type") in {"relation", "relation_assertion"} else content.get("identity")
        if not isinstance(payload, dict):
            payload = content
        violations = payload.get("semantic_violations", {})
        if not isinstance(violations, dict):
            continue
        for rule_code in ["RL_01_001","RL_02_001","RL_03_001","RL_04_001","RL_05_001","RL_06_001","RL_07_001","RL_08_001","RL_09_001","RL_10_001","RL_11_001","RL_12_001","RL_13_001","RL_14_001","RL_15_001","RL_16_001","RL_17_001","RL_18_001","RL_19_001","RL_20_001","RL_21_001","RL_22_001","RL_23_001","RL_24_001","RL_25_001","RL_26_001","RL_27_001","RL_28_001","RL_29_001","RL_30_001","RL_31_001","RL_32_001","RL_33_001","RL_34_001","RL_35_001","RL_36_001","RL_37_001","RL_38_001","RL_39_001","RL_40_001","RL_41_001","RL_42_001","RL_43_001","RL_44_001","RL_45_001","RL_46_001","RL_47_001","RL_48_001","RL_49_001","RL_50_001","RL_51_001","RL_52_001","RL_53_001","RL_54_001","RL_55_001","RL_56_001","RL_57_001","RL_58_001","RL_59_001","RL_60_001","RL_61_001","RL_62_001","RL_63_001","RL_64_001","RL_65_001","RL_66_001","RL_67_001","RL_68_001","RL_69_001","RL_70_001","RL_71_001","RL_72_001","RL_73_001","RL_74_001","RL_75_001","RL_76_001","RL_77_001","RL_78_001","RL_79_001","RL_80_001","RL_81_001","RL_82_001","RL_83_001","RL_84_001","RL_85_001","RL_86_001","RL_87_001","RL_88_001","RL_89_001","RL_90_001","RL_91_001","RL_92_001","RL_93_001","RL_94_001","RL_95_001","RL_96_001","RL_97_001","RL_98_001","RL_99_001","RL_100_001","RL_101_001","RL_102_001","RL_103_001","RL_104_001","RL_105_001","RL_106_001","RL_107_001","RL_108_001","RL_109_001","RL_110_001","RL_111_001","RL_112_001","RL_113_001","RL_114_001","RL_115_001","ID_02_001","ID_03_001","ID_04_001","ID_05_001","ID_06_001","ID_07_001","ID_08_001","ID_09_001","ID_10_001","ID_11_001","ID_12_001","ID_13_001","ID_14_001","ID_15_001","ID_16_001","ID_17_001","ID_18_001","ID_19_001","ID_20_001","ID_21_001","ID_22_001","ID_23_001","ID_24_001","ID_25_001","ID_26_001","ID_27_001","ID_28_001"]:
            if violations.get(rule_code) is True:
                findings.append(_finding(rule_code, "L4/L5", "explicit semantic violation is not admissible", rid))

    # Process anti-inference / temporal / identity guards.
    for record in records:
        if record.get("record_type") != "process":
            continue
        rid = record.get("record_id")
        p = record.get("content", {}).get("process_content", {})
        if not isinstance(p, dict):
            continue
        checks=[
("P_TYPE_MODEL_001",p.get("type_claimed") is True and p.get("model_claimed") is True and p.get("type_model_basis") is None,"type does not establish model"),
("P_MODEL_EVIDENCE_001",p.get("model_claimed") is True and p.get("historical_evidence") is True and p.get("evidence_basis") is None,"model does not establish historical evidence"),
("P_MODEL_IDENTITY_001",p.get("model_identity") is True and p.get("occurrence_identity") is True and p.get("identity_basis") is None,"model identity does not establish occurrence identity"),
("P_HISTORICAL_EVIDENCE_001",p.get("generic_knowledge") is True and p.get("historical_evidence") is True and p.get("historical_basis") is None,"generic process knowledge does not establish historical evidence"),
("P_FRAME_001",p.get("frame_required") is True and not p.get("frame_ref"),"material Process requires frame"),
("P_FRAME_CONTEXT_001",p.get("frame") is True and p.get("context") is True and p.get("frame_context_distinction") is not True,"participating frame and Context must remain distinct"),
("P_PARTICIPANT_ROLES_001",p.get("roles_material") is True and not p.get("participant_roles"),"material participant roles must remain represented"),
("P_ATTRIBUTION_001",p.get("attribution_required") is True and not p.get("attribution_basis"),"Process attribution requires basis"),
("P_BOUNDARY_EVENT_001",p.get("process_boundary") is True and p.get("event_asserted") is True and p.get("event_basis") is None,"Process boundary does not establish Event"),
("P_OBSERVATION_BOUNDARY_001",p.get("observation_boundary") is True and p.get("process_boundary") is True and p.get("boundary_basis") is None,"observation boundary does not establish Process boundary"),
("P_PHASE_EVENT_001",p.get("phase_boundary") is True and p.get("event_asserted") is True and p.get("event_basis") is None,"phase boundary does not establish Event"),
("P_EVENT_PROCESS_001",p.get("event_asserted") is True and p.get("process_asserted") is True and p.get("process_basis") is None,"Event does not establish Process"),
("P_STATE_SEQUENCE_001",p.get("state_sequence") is True and p.get("process_asserted") is True and p.get("continuity_basis") is None,"State sequence does not establish Process continuity"),
("P_ACTION_CAUSE_001",p.get("action") is True and p.get("cause_or_control") is True and p.get("causal_basis") is None,"Action does not establish cause/control"),
("P_PURPOSE_001",p.get("direction_observed") is True and p.get("purpose") is True and p.get("purpose_basis") is None,"observed endpoint does not establish purpose"),
("P_UNKNOWN_BOUNDARY_001",p.get("boundary_unknown") is True and p.get("exact_boundary") is True,"unknown Process boundary cannot become exact"),
("P_OPEN_ENDED_001",p.get("open_ended") is True and p.get("permanent") is True and p.get("permanent_basis") is None,"open-ended does not establish permanent continuation"),
("P_TIME_SCALES_001",p.get("multiple_scales") is True and not p.get("scale_mapping"),"multiple temporal scales require mapping"),
("P_OBSERVATION_GAP_001",p.get("observation_gap") is True and p.get("interrupted") is True and p.get("interruption_basis") is None,"observation gap does not establish interruption"),
("P_INTERRUPTION_001",p.get("interrupted") is True and p.get("terminated") is True and p.get("termination_basis") is None,"interruption does not establish termination"),
("P_RESUMPTION_IDENTITY_001",p.get("resumed") is True and p.get("same_identity") is True and p.get("identity_basis") is None,"resumption does not establish same identity"),
("P_CONTENT_IDENTITY_001",p.get("same_content") is True and p.get("same_identity") is True and p.get("identity_basis") is None,"same content does not establish identity"),
("P_DESCRIPTION_IDENTITY_001",p.get("different_descriptions") is True and p.get("different_identity") is True and p.get("identity_basis") is None,"different descriptions do not establish different identity"),
("P_PROVENANCE_IDENTITY_001",p.get("different_provenance") is True and p.get("different_identity") is True and p.get("identity_basis") is None,"different provenance does not establish different Process"),
("P_MERGE_SPLIT_001",p.get("merge_split") is True and p.get("continuity") is True and p.get("continuity_basis") is None,"merge/split does not establish continuity"),
("P_DECOMPOSITION_001",p.get("decomposition") is True and p.get("invented_stage") is True,"decomposition cannot invent stages"),
("P_CONTAINMENT_001",p.get("temporal_containment") is True and p.get("subprocess") is True and p.get("subprocess_basis") is None,"temporal containment does not establish subprocess"),
("P_OVERLAP_PARTOF_001",p.get("overlap") is True and p.get("part_of") is True and p.get("partof_basis") is None,"overlap does not establish part-of"),
("P_DECOMPOSITION_CONFLICT_001",p.get("decomposition_conflict") is True and p.get("contradiction") is True and p.get("reconciliation_basis") is None,"alternative decompositions do not establish contradiction"),
("P_TEMPORAL_CAUSALITY_001",p.get("temporal_order") is True and p.get("causal") is True and p.get("causal_basis") is None,"temporal order does not establish causality"),
("P_CAUSAL_CONTEXT_001",p.get("causal_relation") is True and not p.get("causal_context_basis"),"causal relation requires Context/Scope/provenance basis"),
("P_FEEDBACK_001",p.get("pattern_observed") is True and p.get("feedback") is True and p.get("feedback_basis") is None,"observed pattern does not establish feedback"),
("P_INPUT_CAUSATION_001",p.get("input") is True and p.get("sole_cause") is True and p.get("causal_basis") is None,"input does not establish sole causation"),
("P_OUTPUT_RESULT_001",p.get("output") is True and p.get("result") is True and p.get("result_basis") is None,"output does not establish Result"),
("P_ENABLING_OCCURRENCE_001",p.get("enabling_condition") is True and p.get("occurrence") is True and p.get("occurrence_basis") is None,"enabling condition does not establish occurrence"),
("P_RECURRING_IDENTITY_001",p.get("recurring") is True and p.get("same_identity") is True and p.get("identity_basis") is None,"recurrence does not establish identical identity"),
("P_RATE_IDENTITY_001",p.get("rate") is True and p.get("identity") is True and p.get("identity_basis") is None,"rate does not determine identity"),
("P_RATE_INTERVAL_001",p.get("point_rate") is True and p.get("constant_interval_rate") is True and p.get("interval_basis") is None,"point rate does not establish interval rate"),
("P_RATE_CUMULATIVE_001",p.get("rate_duration") is True and p.get("cumulative_change") is True and p.get("assumptions") is None,"rate times duration requires assumptions"),
("P_LOG_PROCESS_001",p.get("log") is True and p.get("process_asserted") is True and p.get("occurrence_basis") is None,"logs do not establish Process occurrence"),
("P_WORKFLOW_OCCURRENCE_001",p.get("workflow") is True and p.get("occurrence") is True and p.get("occurrence_basis") is None,"workflow does not establish occurrence"),
("P_SCOPE_001",p.get("process_scope") is True and p.get("observation_scope") is True and p.get("scope_distinction") is not True,"Process Scope must remain distinct from observation Scope"),
("P_SCOPE_TRANSFER_001",p.get("local_scope") is True and p.get("global_scope") is True and p.get("scope_transfer_basis") is None,"local Process Scope does not establish global Scope"),
("P_CONTEXT_DRIFT_001",p.get("context_changed") is True and not p.get("context_lineage"),"Process Context drift requires lineage"),
("P_SIMULTANEOUS_CONFLICT_001",p.get("simultaneous") is True and p.get("conflict") is True and p.get("conflict_basis") is None,"simultaneous Processes do not automatically conflict"),
("P_INTERACTION_CAUSALITY_001",p.get("interaction") is True and p.get("full_causal_mechanism") is True and p.get("mechanism_basis") is None,"interaction does not establish full mechanism"),
("P_PROVENANCE_001",p.get("provenance_required") is True and not p.get("provenance_ref"),"material Process provenance must remain resolvable"),
("P_CONFLICT_RECONCILIATION_001",p.get("conflict") is True and p.get("conflict_asserted") is True and p.get("reconciliation_basis") is None,"Process conflict requires reconciliation"),
("P_HISTORICAL_CONTEXT_001",p.get("historical_process") is True and p.get("current_context_applied") is True and p.get("historical_context_basis") is None,"historical Process cannot silently inherit current Context"),
("P_REVISION_HISTORY_001",p.get("model_revision") is True and p.get("historical_changed") is True and p.get("revision_basis") is None,"model revision does not silently alter historical Process")];
        for code,bad,msg in checks:
            if bad: findings.append(_finding(code,"L4/L5",msg,rid))

    # State temporal/history/anti-inference guards.
    for record in records:
        if record.get("record_type") != "state":
            continue
        rid = record.get("record_id")
        s = record.get("content", {}).get("state_content", {})
        if not isinstance(s, dict):
            continue
        if s.get("role") in {"desired","expected","required","normative"} and s.get("role_basis") is None:
            findings.append(_finding("S_STATE_ROLE_001","L4/L5","non-factual State role requires explicit basis",rid))
        if s.get("snapshot") is True and s.get("interval") is True and s.get("temporal_semantics") is None:
            findings.append(_finding("S_SNAPSHOT_INTERVAL_001","L4/L5","snapshot and interval semantics cannot be conflated",rid))
        if s.get("evidence_snapshot") is True and s.get("validity_interval") is True and s.get("interval_basis") is None:
            findings.append(_finding("S_EVIDENCE_INTERVAL_001","L4/L5","evidence snapshot cannot silently establish interval validity",rid))
        if s.get("repeated_observations") is True and s.get("continuous") is True and s.get("continuity_basis") is None:
            findings.append(_finding("S_CONTINUITY_001","L4/L5","repeated observations do not establish continuous persistence",rid))
        if s.get("no_change_evidence") is True and s.get("stable") is True and s.get("stability_basis") is None:
            findings.append(_finding("S_OPEN_WORLD_001","L4/L5","absence of change evidence does not establish stability",rid))
        if s.get("representation_changed") is True and s.get("state_changed") is True and s.get("lineage_basis") is None:
            findings.append(_finding("S_REPRESENTATION_HISTORY_001","L4/L5","representation change does not establish State change",rid))
        if s.get("provenance_changed") is True and s.get("identity_changed") is True and s.get("identity_basis") is None:
            findings.append(_finding("S_PROVENANCE_CONTINUITY_001","L4/L5","provenance change alone does not establish State identity change",rid))
        if s.get("same_value") is True and s.get("same_identity") is True and s.get("identity_basis") is None:
            findings.append(_finding("S_VALUE_IDENTITY_001","L4/L5","equal values do not establish State identity",rid))
        if s.get("gap") is True and s.get("same_interval") is True and s.get("continuity_basis") is None:
            findings.append(_finding("S_BREAK_CONTINUITY_001","L4/L5","a temporal gap does not establish one continuous interval",rid))
        if s.get("detailing") is True and s.get("invented_property") is True:
            findings.append(_finding("S_DETAILING_FIDELITY_001","L4/L5","detailing cannot invent material State properties",rid))
        if s.get("measurement_conflict") is True and s.get("conflict") is True and s.get("reconciliation_basis") is None:
            findings.append(_finding("S_MEASUREMENT_CONTEXT_001","L4/L5","measurement coexistence alone does not establish State conflict",rid))
        if s.get("conflict") is True and s.get("conflict_asserted") is True and s.get("reconciliation_basis") is None:
            findings.append(_finding("S_CONFLICT_RECONCILIATION_001","L4/L5","State conflict requires temporal/semantic/context reconciliation",rid))
        if s.get("part_state") is True and s.get("whole_state") is True and s.get("part_whole_basis") is None:
            findings.append(_finding("S_PART_WHOLE_001","L4/L5","part State cannot silently become whole State",rid))
        if s.get("sample_state") is True and s.get("population_state") is True and s.get("scope_basis") is None:
            findings.append(_finding("S_SAMPLE_POPULATION_001","L4/L5","sample State cannot silently become population State",rid))
        if s.get("aggregate") is True and s.get("identical_individuals") is True and s.get("aggregation_basis") is None:
            findings.append(_finding("S_AGGREGATE_001","L4/L5","aggregate State does not establish identical individual States",rid))
        if s.get("context_changed") is True and s.get("context_lineage") is None:
            findings.append(_finding("S_CONTEXT_LINEAGE_001","L4/L5","material State Context change requires lineage",rid))
        if s.get("effective_time") is True and s.get("time_role_mapping") is None:
            findings.append(_finding("S_EFFECTIVE_TIME_001","L4/L5","effective time must remain distinct from publication/registration time",rid))
        if s.get("relational_roles_material") is True and not s.get("role_structure"):
            findings.append(_finding("S_RELATIONAL_ROLE_001","L4/L5","material relational State roles must remain represented",rid))
        if s.get("state_sequence") is True and s.get("causal_chain") is True and s.get("causal_basis") is None:
            findings.append(_finding("S_CAUSAL_SEQUENCE_001","L4/L5","State sequence does not establish causal chain",rid))
        if s.get("classification") is True and s.get("original_properties_lost") is True and not s.get("losses"):
            findings.append(_finding("S_CLASSIFICATION_FIDELITY_001","L4/L5","classification loss must remain explicit",rid))
        if s.get("earlier_decision") is True and s.get("later_state_basis") is True and s.get("temporal_dependency_basis") is None:
            findings.append(_finding("S_DECISION_TIME_001","L4/L5","later State cannot retroactively enter earlier Decision basis",rid))

    # Scope representation-integrity guards. They fire only for explicit semantic
    # representations; absent optional semantics remain non-applicable.
    for record in records:
        if record.get("record_type") != "scope":
            continue
        rid = record.get("record_id")
        c0 = record.get("content", {})
        sc = c0.get("scope_content") if isinstance(c0, dict) else None
        if not isinstance(sc, dict):
            continue
        if sc.get("semantic_role_required") is True and not sc.get("semantic_role"):
            findings.append(_finding("SCP_ROLE_001","L4","material Scope role is required but absent",rid))
        if sc.get("material_target") is True and not _ref_key(sc.get("target_ref")):
            findings.append(_finding("SCP_TARGET_001","L4","material Scope target must resolve",rid))
        if sc.get("universe_required") is True and sc.get("universe_status") == "unknown" and sc.get("universe_fabricated") is True:
            findings.append(_finding("SCP_UNIVERSE_001","L4","unknown universe cannot be replaced by fabricated universe",rid))
        if sc.get("quantifier_required") is True and sc.get("quantifier") is None:
            findings.append(_finding("SCP_QUANTIFIER_001","L4","material quantifier must remain represented",rid))
        if sc.get("analysis_level_required") is True and sc.get("analysis_level") is None:
            findings.append(_finding("SCP_LEVEL_001","L4","material analysis level must remain represented",rid))
        if sc.get("epistemic_status") == "unknown" and sc.get("epistemic_resolved") is True:
            findings.append(_finding("SCP_EPISTEMIC_001","L4","unknown Scope epistemic status cannot be silently resolved",rid))
        if sc.get("applicability_status") == "proven" and sc.get("declared_only") is True:
            findings.append(_finding("SCP_APPLICABILITY_001","L4","declared Scope cannot be represented as proven applicability",rid))
        if sc.get("status") == "unknown" and sc.get("universal") is True:
            findings.append(_finding("SCP_UNKNOWN_001","L4","unknown Scope cannot become universal Scope",rid))
        if sc.get("closure_mode") == "closed" and not sc.get("closure_basis"):
            findings.append(_finding("SCP_CLOSURE_001","L4","closed Scope requires closure basis",rid))
        if sc.get("open_world") is False and sc.get("closure_justified") is not True:
            findings.append(_finding("SCP_OPENWORLD_001","L4","closed-world Scope requires explicit justification",rid))
        if sc.get("boundary_mode") == "exact" and sc.get("boundary_uncertain") is True:
            findings.append(_finding("SCP_BOUNDARY_001","L4","uncertain boundary cannot be silently represented as exact",rid))
        if sc.get("boundary_mode") == "crisp" and sc.get("fuzzy") is True and sc.get("fuzzy_basis") is None:
            findings.append(_finding("SCP_FUZZY_001","L4/L5","fuzzy Scope cannot become crisp without basis",rid))
        if sc.get("membership_status") == "unknown" and sc.get("membership_resolved") is True:
            findings.append(_finding("SCP_MEMBERSHIP_001","L4","unknown membership cannot be silently resolved",rid))
        if sc.get("dimensions_coupled") is True and sc.get("cartesian_product") is True and sc.get("coupling_basis") is None:
            findings.append(_finding("SCP_DIMENSION_COUPLING_001","L4/L5","coupled dimensions cannot be flattened to Cartesian product without basis",rid))
        if sc.get("tuple_semantics") is True and sc.get("tuple_values") is None:
            findings.append(_finding("SCP_TUPLE_001","L5","tuple/configuration semantics require tuple_values",rid))
        if sc.get("temporal_role") is None and sc.get("temporal_validity_material") is True:
            findings.append(_finding("SCP_TEMPORAL_001","L5","material temporal Scope requires temporal role",rid))
        if sc.get("transferability") in {"transferable","conditional","partial"} and not sc.get("transfer_basis_refs"):
            findings.append(_finding("SCP_TRANSFER_BASIS_001","L4/L5","positive Scope transferability requires basis",rid))
        if sc.get("overlap") is True and sc.get("equivalent") is True and sc.get("equivalence_basis") is None:
            findings.append(_finding("SCP_OVERLAP_001","L4","Scope overlap does not establish equivalence",rid))
        if sc.get("mismatch") is True and sc.get("contradiction") is True and sc.get("reconciliation_basis") is None:
            findings.append(_finding("SCP_MISMATCH_001","L4","Scope mismatch alone does not establish contradiction",rid))
        if sc.get("inherited") is True and sc.get("inheritance_compatible") is False:
            findings.append(_finding("SCP_INHERIT_COMPAT_001","L4/L5","incompatible Scope inheritance cannot be accepted",rid))
        if sc.get("derived") is True and sc.get("source_scope_ref") is None:
            findings.append(_finding("SCP_DERIVED_001","L5","derived Scope requires source Scope reference",rid))
        if sc.get("provenance_required") is True and not sc.get("provenance_ref"):
            findings.append(_finding("SCP_PROVENANCE_001","L4/L5","material Scope provenance must remain resolvable",rid))
        if sc.get("fidelity") == "lost" and not sc.get("losses"):
            findings.append(_finding("SCP_FIDELITY_001","L5","Scope fidelity loss must remain explicit",rid))
        if sc.get("composition") in {"union","intersection","projection","mapping"} and sc.get("composition_justified") is False:
            findings.append(_finding("SCP_COMPOSITION_001","L5","Scope composition requires justified semantics",rid))
        if sc.get("role_drift") is True and sc.get("role_drift_detected") is False:
            findings.append(_finding("SCP_ROLE_DRIFT_001","L5","Scope role drift must remain detectable",rid))

    # Context: explicit inheritance/precedence/conflict/transfer/fidelity controls.
    context_edges: dict[str, set[str]] = {}
    contexts = [r for r in records if r.get("record_type") == "context"]
    for record in contexts:
        content = record.get("content", {})
        cc = content.get("context_content", {}) if isinstance(content, dict) else {}
        if not isinstance(cc, dict):
            continue
        inheritance = cc.get("inheritance")
        if inheritance is not None:
            parents = inheritance.get("parent_refs", []) if isinstance(inheritance, dict) else []
            for parent in parents if isinstance(parents, list) else []:
                key = _ref_key(parent)
                if key:
                    context_edges.setdefault(record["record_id"], set()).add(key[0])
                    if key[0] not in by_id:
                        findings.append(_finding("CTX_INHERIT_001", "L4", "parent Context не разрешается", record["record_id"]))
            if isinstance(inheritance, dict) and inheritance.get("effective") is not None and not isinstance(inheritance.get("effective"), dict):
                findings.append(_finding("CTX_INHERIT_001", "L4", "effective Context должен быть объектом", record["record_id"]))
        precedence = cc.get("precedence")
        if precedence is not None and not isinstance(precedence, (int, float)):
            findings.append(_finding("CTX_PRECEDENCE_001", "L4", "precedence должен быть числом", record["record_id"]))
        transfer = cc.get("transferability")
        if isinstance(transfer, dict) and transfer.get("status") in {"transferable", "conditional", "partial"} and not transfer.get("basis_refs"):
            findings.append(_finding("CTX_TRANSFER_001", "L4", "положительная transferability требует basis_refs", record["record_id"]))
        fidelity = cc.get("fidelity")
        if isinstance(fidelity, dict) and fidelity.get("status") == "lost" and not fidelity.get("losses"):
            findings.append(_finding("CTX_FIDELITY_001", "L5", "потеря Context Fidelity должна быть зафиксирована", record["record_id"]))
        deps = cc.get("dimension_dependencies")
        if deps is not None and not isinstance(deps, list):
            findings.append(_finding("CTX_DIMENSION_001", "L4", "dimension_dependencies должен быть списком", record["record_id"]))

    if _graph_cycle(context_edges):
        findings.append(_finding("CTX_INHERIT_001", "L4", "обнаружен цикл наследования Context"))

    for i, left in enumerate(contexts):
        for right in contexts[i + 1:]:
            lc, rc = left.get("content", {}), right.get("content", {})
            if not isinstance(lc, dict) or not isinstance(rc, dict):
                continue
            if _ref_key(lc.get("target_ref")) != _ref_key(rc.get("target_ref")):
                continue
            if not _overlap(left, right):
                continue
            lv = lc.get("context_content", {})
            rv = rc.get("context_content", {})
            if isinstance(lv, dict) and isinstance(rv, dict):
                common = set(lv) & set(rv) - {"inheritance", "precedence", "transferability", "fidelity", "dimension_dependencies"}
                if any(lv[k] != rv[k] for k in common):
                    lp = lv.get("precedence")
                    rp = rv.get("precedence")
                    if lp == rp:
                        findings.append(_finding("CTX_CONFLICT_001", "L4", "конфликт Context без однозначного precedence", left.get("record_id")))

    # Scope: explicit quantifier/tuple/transfer controls are validated when represented.
    for record in records:
        if record.get("record_type") != "scope":
            continue
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        sc = c.get("scope_content")
        if isinstance(sc, dict):
            quantifier = sc.get("quantifier")
            if quantifier is not None and quantifier not in {"all", "some", "none", "exactly", "at_least", "at_most", "unknown"}:
                findings.append(_finding("SCOPE_QUANT_001", "L4", "неизвестный quantifier Scope", record.get("record_id")))
            dimensions = sc.get("dimensions")
            if dimensions is not None and not isinstance(dimensions, list):
                findings.append(_finding("SCOPE_TUPLE_001", "L4", "multidimensional Scope dimensions должен быть списком", record.get("record_id")))
            if sc.get("transferability") == "universal":
                findings.append(_finding("SCOPE_TRANSFER_001", "L5", "Scope не переносится универсально без явного основания", record.get("record_id")))

    # Scope extension: explicit sample/population, inheritance, membership provenance,
    # fidelity, history and composition controls. Missing optional representations are
    # non-applicable; they are never inferred.
    scope_edges: dict[str, set[str]] = {}
    allowed_scope_ops = {"union", "intersection", "projection", "mapping", "inheritance", "transfer"}
    for record in records:
        if record.get("record_type") != "scope":
            continue
        rid = record.get("record_id")
        c = record.get("content", {})
        sc = c.get("scope_content") if isinstance(c, dict) else None
        if not isinstance(sc, dict):
            continue

        sample_pop = sc.get("sample_to_population")
        if sample_pop is True and not sc.get("basis_refs"):
            findings.append(_finding("SCOPE_SAMPLE_POP_001", "L4", "sample-to-population generalization requires basis_refs", rid))

        inheritance = sc.get("inheritance")
        if isinstance(inheritance, dict):
            parents = inheritance.get("parent_refs", [])
            if not isinstance(parents, list):
                findings.append(_finding("SCOPE_INHERIT_001", "L4", "Scope inheritance parent_refs must be a list", rid))
            else:
                for parent in parents:
                    key = _ref_key(parent)
                    if key:
                        scope_edges.setdefault(rid, set()).add(key[0])
                        if key[0] not in by_id:
                            findings.append(_finding("SCOPE_INHERIT_001", "L4", "Scope inheritance parent does not resolve", rid))

        membership_prov = sc.get("membership_provenance")
        if isinstance(membership_prov, dict) and membership_prov.get("status") in {"stated", "observed", "tested", "validated", "reported", "inferred", "modeled"} and not membership_prov.get("basis_refs"):
            findings.append(_finding("SCOPE_MEMBERSHIP_PROV_001", "L4", "membership provenance status requires basis_refs", rid))

        fidelity = sc.get("fidelity")
        if isinstance(fidelity, dict) and fidelity.get("status") == "lost" and not fidelity.get("losses"):
            findings.append(_finding("SCOPE_FIDELITY_001", "L5", "Scope Fidelity loss must be recorded", rid))

        if sc.get("historical") is True and not (record.get("valid_time") or sc.get("history_ref")):
            findings.append(_finding("SCOPE_HISTORY_001", "L5", "historical Scope requires temporal or history reference", rid))

        operation = sc.get("operation")
        if operation is not None:
            if operation not in allowed_scope_ops:
                findings.append(_finding("SCOPE_ALGEBRA_001", "L4", "unknown Scope composition operation", rid))
            elif operation in {"union", "intersection"} and not isinstance(sc.get("operands"), list):
                findings.append(_finding("SCOPE_ALGEBRA_001", "L4", "union/intersection requires operands list", rid))
            elif operation == "projection" and not isinstance(sc.get("dimensions"), list):
                findings.append(_finding("SCOPE_ALGEBRA_001", "L4", "projection requires dimensions list", rid))
            elif operation == "mapping" and not _ref_key(sc.get("mapping_ref")):
                findings.append(_finding("SCOPE_ALGEBRA_001", "L4", "mapping requires mapping_ref", rid))

    if _graph_cycle(scope_edges):
        findings.append(_finding("SCOPE_INHERIT_001", "L4", "обнаружен цикл наследования Scope"))

    # Provenance graph: cycles are invalid; common roots do not become independence.
    prov_edges: dict[str, set[str]] = {}
    allowed_provenance_relations = {
        "derived_from", "transformed_from", "copied_from", "translated_from",
        "summarized_from", "extracted_from", "aggregated_from",
        "generated_from", "reconstructed_from", "compiled_from",
    }
    for record in records:
        p = record.get("provenance")
        if not isinstance(p, dict):
            continue
        source = record.get("record_id")
        if not isinstance(source, str):
            continue
        relation = p.get("relation")
        if relation is not None and relation not in allowed_provenance_relations:
            findings.append(_finding("PROV_TYPE_001", "L4", "неизвестный тип provenance relation", source))
        fidelity = p.get("fidelity")
        if isinstance(fidelity, dict) and fidelity.get("status") == "lost" and not fidelity.get("losses"):
            findings.append(_finding("PROV_FIDELITY_001", "L5", "потеря provenance fidelity должна быть зафиксирована", source))
        for key in ("created_from", "transformed_from"):
            for ref in p.get(key, []) if isinstance(p.get(key), list) else []:
                k = _ref_key(ref)
                if k:
                    prov_edges.setdefault(source, set()).add(k[0])
    if _graph_cycle(prov_edges):
        findings.append(_finding("PROV_CYCLE_001", "L4", "обнаружен цикл provenance lineage"))
    for record in records:
        p = record.get("provenance")
        if isinstance(p, dict) and p.get("independent") is True and (p.get("created_from") or p.get("transformed_from")):
            findings.append(_finding("PROV_INDEPENDENCE_001", "L4", "зависимое происхождение не может быть помечено как независимое", record.get("record_id")))

    # Authorship: role boundaries are explicit and history cannot be overwritten.
    for record in records:
        if record.get("record_type") != "authorship_contribution":
            continue
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        if c.get("attribution_status") == "disputed" and c.get("confirmed") is True:
            findings.append(_finding("AUTH_CONFLICT_001", "L4", "disputed attribution не может быть одновременно confirmed", record.get("record_id")))
        if c.get("contributor_kind") == "pseudonymous" and c.get("resolved_person_ref"):
            findings.append(_finding("AUTH_PSEUDONYM_001", "L4", "pseudonym не должен молча становиться resolved person", record.get("record_id")))
        if c.get("tool_use") is True and c.get("contribution") == "author":
            findings.append(_finding("AUTH_ROLE_001", "L4", "использование инструмента не является автоматически авторством", record.get("record_id")))
        if c.get("historical_attribution") is True and not (c.get("attribution_time") or c.get("history_ref")):
            findings.append(_finding("AUTH_HISTORY_001", "L5", "historical attribution должна иметь временную или историческую привязку", record.get("record_id")))

    # Trust/Reputation: explicit goal/subject, no cycles, no aggregation-to-truth.
    trust_edges: dict[str, set[str]] = {}
    for record in records:
        if record.get("record_type") != "trust_reputation":
            continue
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        subject = _ref_key(c.get("subject_ref"))
        if subject and isinstance(record.get("record_id"), str):
            trust_edges.setdefault(record["record_id"], set()).add(subject[0])
        if c.get("assessment_type") in {"trust", "trust_assessment"}:
            if not _ref_key(c.get("subject_ref")):
                findings.append(_finding("TRUST_GOAL_001", "L4", "Trust требует subject_ref", record.get("record_id")))
            if not _ref_key(c.get("goal_ref")):
                findings.append(_finding("TRUST_GOAL_001", "L4", "Trust требует goal_ref", record.get("record_id")))
        if c.get("aggregation") and c.get("truth") is True:
            findings.append(_finding("TRUST_AGGREGATION_001", "L5", "агрегация Trust/Reputation не доказывает truth", record.get("record_id")))
        if c.get("transferability") == "universal":
            findings.append(_finding("TRUST_TRANSFER_001", "L5", "Trust не переносится универсально без явного основания", record.get("record_id")))
        if c.get("independence_status") == "independent" and c.get("common_root_ref"):
            findings.append(_finding("TRUST_INDEPENDENCE_001", "L4", "общий root не совместим с заявленной независимостью без отдельного основания", record.get("record_id")))
        if c.get("historical") is True and not (record.get("valid_time") or c.get("assessment_time") or c.get("history_ref")):
            findings.append(_finding("TRUST_HISTORY_001", "L5", "historical Trust/Reputation должна иметь временную или историческую привязку", record.get("record_id")))
    if _graph_cycle(trust_edges):
        findings.append(_finding("TRUST_CYCLE_001", "L4", "обнаружен цикл Trust/Reputation"))

    # Additional explicit semantic-role safeguards. These trigger only when the
    # corresponding representation is explicit; absent fields remain non-applicable.
    for record in records:
        rid = record.get("record_id")
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        if record.get("record_type") == "context":
            cc = c.get("context_content", {})
            if isinstance(cc, dict):
                if cc.get("semantic_role") == "cause" and cc.get("context_only") is True:
                    findings.append(_finding("CTX_ROLE_001", "L4", "Context-only representation cannot simultaneously assert causal role", rid))
                if cc.get("assumption") is True and cc.get("epistemic_status") == "observed":
                    findings.append(_finding("CTX_ASSUMPTION_001", "L4", "assumption cannot be silently represented as observed", rid))
                if cc.get("transferability") == "transferable" and cc.get("conflict") is True:
                    findings.append(_finding("CTX_TRANSFER_CONFLICT_001", "L4/L5", "conflicting Context cannot be declared unconditionally transferable", rid))
        p = record.get("provenance")
        if isinstance(p, dict):
            if p.get("component_scope") is True and not p.get("scope"):
                findings.append(_finding("PROV_SCOPE_001", "L4", "component-scoped provenance requires scope", rid))
            if p.get("relation") in {"translated_from", "copied_from", "summarized_from"} and p.get("operation_semantics") == "unknown" and p.get("specific_operation") is True:
                findings.append(_finding("PROV_OPERATION_001", "L4", "specific operation cannot be simultaneously marked unknown", rid))
            if p.get("joint_inputs") is True and not isinstance(p.get("input_group"), list):
                findings.append(_finding("PROV_JOINT_INPUT_001", "L4", "joint provenance requires input_group", rid))
        if record.get("record_type") == "authorship_contribution":
            if c.get("translation") is True and c.get("original_authorship") is True:
                findings.append(_finding("AUTH_TRANSLATION_001", "L4", "translation does not establish original authorship", rid))
            if c.get("synthesis") is True and c.get("source_authorship") is True:
                findings.append(_finding("AUTH_SYNTHESIS_001", "L4", "synthesis authorship does not establish source authorship", rid))
            if c.get("author_order_semantics") == "importance" and c.get("order_basis") is None:
                findings.append(_finding("AUTH_ORDER_001", "L4", "author order semantics requires explicit basis", rid))
        if record.get("record_type") == "trust_reputation":
            if c.get("signal") is True and c.get("established_fact") is True:
                findings.append(_finding("TRUST_REPUTATION_SIGNAL_001", "L4", "reputation signal is not automatically an established fact", rid))
            if c.get("authority") is True and c.get("truth") is True and not c.get("truth_basis"):
                findings.append(_finding("TRUST_AUTHORITY_001", "L5", "authority cannot by itself establish truth", rid))
            if c.get("easy_case_selection") is True and c.get("competence") == "high" and not c.get("selection_basis"):
                findings.append(_finding("TRUST_EASY_CASES_001", "L5", "high success on selected easy cases does not establish competence", rid))

    # Cross-cutting anti-inference.
    for record in records:
        c = record.get("content", {})
        if not isinstance(c, dict):
            continue
        if record.get("publication_status") == "published" and c.get("truth") is True:
            findings.append(_finding("VAL-L4-PUBLICATION-TRUTH", "L4", "publication не доказывает truth", record.get("record_id")))
        if c.get("provenance_strength") == "independent" and c.get("created_from"):
            findings.append(_finding("PROV_INDEPENDENCE_001", "L4", "lineage dependency contradicts independence", record.get("record_id")))

    return findings
