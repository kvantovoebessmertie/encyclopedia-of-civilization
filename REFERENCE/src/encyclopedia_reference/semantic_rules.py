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
    SemanticRule("RL_01_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_02_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_03_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_04_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_05_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_06_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_07_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_08_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_09_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_10_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_11_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_12_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_13_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_14_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_15_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_16_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_17_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_18_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_19_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_20_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_21_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_22_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_23_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_24_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_25_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_26_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_27_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_28_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_29_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_30_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_31_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_32_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_33_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_34_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_35_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_36_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_37_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_38_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_39_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_40_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_41_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_42_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_43_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_44_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_45_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_46_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_47_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_48_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_49_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_50_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_51_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_52_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_53_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_54_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_55_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_56_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_57_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_58_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_59_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_60_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_61_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_62_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_63_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_64_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_65_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_66_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_67_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_68_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_69_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_70_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_71_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_72_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_73_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_74_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_75_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_76_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_77_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_78_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_79_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_80_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_81_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_82_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_83_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_84_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_85_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_86_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_87_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_88_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_89_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_90_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_91_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_92_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_93_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_94_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_95_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_96_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_97_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_98_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_99_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_100_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_101_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_102_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_103_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_104_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_105_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_106_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_107_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_108_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_109_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_110_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_111_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_112_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_113_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_114_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("RL_115_001", "L4/L5", "relation.rl_rule"),
    SemanticRule("ID_02_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_03_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_04_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_05_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_06_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_07_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_08_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_09_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_10_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_11_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_12_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_13_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_14_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_15_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_16_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_17_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_18_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_19_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_20_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_21_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_22_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_23_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_24_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_25_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_26_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_27_001", "L4/L5", "identity.id_rule"),
    SemanticRule("ID_28_001", "L4/L5", "identity.id_rule"),
    SemanticRule("S_EVENT_COUNT_001", "L4/L5", "state.semantic_rule"),
    SemanticRule("S_MEASUREMENT_SEMANTICS_001", "L4/L5", "state.semantic_rule"),
    SemanticRule("S_QUALITATIVE_THRESHOLD_001", "L4/L5", "state.semantic_rule"),
    SemanticRule("P_LIFECYCLE_SEMANTICS_001", "L4/L5", "process.semantic_rule"),
    SemanticRule("P_STATE_CAUSAL_LINK_001", "L4/L5", "process.semantic_rule"),
    SemanticRule("P_EVENT_CAUSAL_LINK_001", "L4/L5", "process.semantic_rule"),
    SemanticRule("P_PROFILE_CORE_001", "L4/L5", "process.semantic_rule"),
    SemanticRule("P_PROFILE_RESOLUTION_001", "L4/L5", "process.semantic_rule"),
    SemanticRule("ID_29_001", "L4/L5", "id.id-29"),
    SemanticRule("ID_30_001", "L4/L5", "id.id-30"),
    SemanticRule("ID_31_001", "L4/L5", "id.id-31"),
    SemanticRule("ID_32_001", "L4/L5", "id.id-32"),
    SemanticRule("ID_33_001", "L4/L5", "id.id-33"),
    SemanticRule("ID_34_001", "L4/L5", "id.id-34"),
    SemanticRule("ID_35_001", "L4/L5", "id.id-35"),
    SemanticRule("ID_36_001", "L4/L5", "id.id-36"),
    SemanticRule("ID_37_001", "L4/L5", "id.id-37"),
    SemanticRule("ID_38_001", "L4/L5", "id.id-38"),
    SemanticRule("ID_39_001", "L4/L5", "id.id-39"),
    SemanticRule("ID_42_001", "L4/L5", "id.id-42"),
    SemanticRule("ID_43_001", "L4/L5", "id.id-43"),
    SemanticRule("ID_45_001", "L4/L5", "id.id-45"),
    SemanticRule("ID_47_001", "L4/L5", "id.id-47"),
    SemanticRule("ID_48_001", "L4/L5", "id.id-48"),
    SemanticRule("ID_49_001", "L4/L5", "id.id-49"),
    SemanticRule("ID_50_001", "L4/L5", "id.id-50"),
    SemanticRule("ID_51_001", "L4/L5", "id.id-51"),
    SemanticRule("ID_52_001", "L4/L5", "id.id-52"),
    SemanticRule("ID_53_001", "L4/L5", "id.id-53"),
    SemanticRule("ID_54_001", "L4/L5", "id.id-54"),
    SemanticRule("ID_55_001", "L4/L5", "id.id-55"),
    SemanticRule("ID_56_001", "L4/L5", "id.id-56"),
    SemanticRule("ID_57_001", "L4/L5", "id.id-57"),
    SemanticRule("ID_58_001", "L4/L5", "id.id-58"),
    SemanticRule("ID_59_001", "L4/L5", "id.id-59"),
    SemanticRule("ID_60_001", "L4/L5", "id.id-60"),
    SemanticRule("ID_61_001", "L4/L5", "id.id-61"),
    SemanticRule("ID_62_001", "L4/L5", "id.id-62"),
    SemanticRule("ID_63_001", "L4/L5", "id.id-63"),
    SemanticRule("ID_64_001", "L4/L5", "id.id-64"),
    SemanticRule("ID_65_001", "L4/L5", "id.id-65"),
    SemanticRule("ID_66_001", "L4/L5", "id.id-66"),
    SemanticRule("ID_67_001", "L4/L5", "id.id-67"),
    SemanticRule("ID_68_001", "L4/L5", "id.id-68"),
    SemanticRule("ID_69_001", "L4/L5", "id.id-69"),
    SemanticRule("ID_70_001", "L4/L5", "id.id-70"),
    SemanticRule("ID_71_001", "L4/L5", "id.id-71"),
    SemanticRule("ID_72_001", "L4/L5", "id.id-72"),
    SemanticRule("ID_73_001", "L4/L5", "id.id-73"),
    SemanticRule("ID_74_001", "L4/L5", "id.id-74"),
    SemanticRule("ID_75_001", "L4/L5", "id.id-75"),
    SemanticRule("ID_76_001", "L4/L5", "id.id-76"),
    SemanticRule("ID_77_001", "L4/L5", "id.id-77"),
    SemanticRule("ID_78_001", "L4/L5", "id.id-78"),
    SemanticRule("ID_79_001", "L4/L5", "id.id-79"),
    SemanticRule("ID_80_001", "L4/L5", "id.id-80"),
    SemanticRule("ID_81_001", "L4/L5", "id.id-81"),
    SemanticRule("ID_82_001", "L4/L5", "id.id-82"),
    SemanticRule("ID_83_001", "L4/L5", "id.id-83"),
    SemanticRule("ID_84_001", "L4/L5", "id.id-84"),
    SemanticRule("ID_85_001", "L4/L5", "id.id-85"),
    SemanticRule("ID_86_001", "L4/L5", "id.id-86"),
    SemanticRule("ID_87_001", "L4/L5", "id.id-87"),
    SemanticRule("ID_88_001", "L4/L5", "id.id-88"),
    SemanticRule("ID_89_001", "L4/L5", "id.id-89"),
    SemanticRule("ID_90_001", "L4/L5", "id.id-90"),
    SemanticRule("ID_91_001", "L4/L5", "id.id-91"),
    SemanticRule("ID_92_001", "L4/L5", "id.id-92"),
    SemanticRule("ID_93_001", "L4/L5", "id.id-93"),
    SemanticRule("ID_94_001", "L4/L5", "id.id-94"),
    SemanticRule("ID_95_001", "L4/L5", "id.id-95"),
    SemanticRule("ID_96_001", "L4/L5", "id.id-96"),
    SemanticRule("ID_97_001", "L4/L5", "id.id-97"),
    SemanticRule("ID_98_001", "L4/L5", "id.id-98"),
    SemanticRule("ID_99_001", "L4/L5", "id.id-99"),
    SemanticRule("ID_100_001", "L4/L5", "id.id-100"),
    SemanticRule("ID_101_001", "L4/L5", "id.id-101"),
    SemanticRule("ID_102_001", "L4/L5", "id.id-102"),
    SemanticRule("ID_103_001", "L4/L5", "id.id-103"),
    SemanticRule("ID_104_001", "L4/L5", "id.id-104"),
    SemanticRule("ID_105_001", "L4/L5", "id.id-105"),
    SemanticRule("ID_106_001", "L4/L5", "id.id-106"),
    SemanticRule("ID_107_001", "L4/L5", "id.id-107"),
    SemanticRule("ID_108_001", "L4/L5", "id.id-108"),
    SemanticRule("ID_109_001", "L4/L5", "id.id-109"),
    SemanticRule("ID_110_001", "L4/L5", "id.id-110"),
    SemanticRule("ID_111_001", "L4/L5", "id.id-111"),
    SemanticRule("ID_112_001", "L4/L5", "id.id-112"),
    SemanticRule("ID_113_001", "L4/L5", "id.id-113"),
    SemanticRule("ID_114_001", "L4/L5", "id.id-114"),
    SemanticRule("ID_115_001", "L4/L5", "id.id-115"),
    SemanticRule("ID_116_001", "L4/L5", "id.id-116"),
    SemanticRule("ID_117_001", "L4/L5", "id.id-117"),
    SemanticRule("ID_118_001", "L4/L5", "id.id-118"),
    SemanticRule("ID_119_001", "L4/L5", "id.id-119"),
    SemanticRule("ID_120_001", "L4/L5", "id.id-120"),
    SemanticRule("ID_121_001", "L4/L5", "id.id-121"),
    SemanticRule("ID_122_001", "L4/L5", "id.id-122"),
    SemanticRule("ID_123_001", "L4/L5", "id.id-123"),
    SemanticRule("ID_124_001", "L4/L5", "id.id-124"),
    SemanticRule("ID_125_001", "L4/L5", "id.id-125"),
    SemanticRule("ID_126_001", "L4/L5", "id.id-126"),
    SemanticRule("ID_127_001", "L4/L5", "id.id-127"),
    SemanticRule("ID_128_001", "L4/L5", "id.id-128"),
    SemanticRule("ID_129_001", "L4/L5", "id.id-129"),
    SemanticRule("ID_130_001", "L4/L5", "id.id-130"),
    SemanticRule("ID_131_001", "L4/L5", "id.id-131"),
    SemanticRule("CTX_03_001", "L4/L5", "ctx.ctx-03"),
    SemanticRule("CTX_04_001", "L4/L5", "ctx.ctx-04"),
    SemanticRule("CTX_05_001", "L4/L5", "ctx.ctx-05"),
    SemanticRule("CTX_06_001", "L4/L5", "ctx.ctx-06"),
    SemanticRule("CTX_07_001", "L4/L5", "ctx.ctx-07"),
    SemanticRule("CTX_08_001", "L4/L5", "ctx.ctx-08"),
    SemanticRule("CTX_09_001", "L4/L5", "ctx.ctx-09"),
    SemanticRule("CTX_11_001", "L4/L5", "ctx.ctx-11"),
    SemanticRule("CTX_12_001", "L4/L5", "ctx.ctx-12"),
    SemanticRule("CTX_13_001", "L4/L5", "ctx.ctx-13"),
    SemanticRule("CTX_15_001", "L4/L5", "ctx.ctx-15"),
    SemanticRule("CTX_16_001", "L4/L5", "ctx.ctx-16"),
    SemanticRule("CTX_19_001", "L4/L5", "ctx.ctx-19"),
    SemanticRule("CTX_20_001", "L4/L5", "ctx.ctx-20"),
    SemanticRule("CTX_21_001", "L4/L5", "ctx.ctx-21"),
    SemanticRule("CTX_22_001", "L4/L5", "ctx.ctx-22"),
    SemanticRule("CTX_23_001", "L4/L5", "ctx.ctx-23"),
    SemanticRule("CTX_24_001", "L4/L5", "ctx.ctx-24"),
    SemanticRule("CTX_25_001", "L4/L5", "ctx.ctx-25"),
    SemanticRule("CTX_27_001", "L4/L5", "ctx.ctx-27"),
    SemanticRule("CTX_28_001", "L4/L5", "ctx.ctx-28"),
    SemanticRule("CTX_29_001", "L4/L5", "ctx.ctx-29"),
    SemanticRule("CTX_30_001", "L4/L5", "ctx.ctx-30"),
    SemanticRule("CTX_31_001", "L4/L5", "ctx.ctx-31"),
    SemanticRule("CTX_32_001", "L4/L5", "ctx.ctx-32"),
    SemanticRule("CTX_33_001", "L4/L5", "ctx.ctx-33"),
    SemanticRule("CTX_34_001", "L4/L5", "ctx.ctx-34"),
    SemanticRule("CTX_35_001", "L4/L5", "ctx.ctx-35"),
    SemanticRule("CTX_36_001", "L4/L5", "ctx.ctx-36"),
    SemanticRule("CTX_37_001", "L4/L5", "ctx.ctx-37"),
    SemanticRule("CTX_38_001", "L4/L5", "ctx.ctx-38"),
    SemanticRule("CTX_39_001", "L4/L5", "ctx.ctx-39"),
    SemanticRule("CTX_40_001", "L4/L5", "ctx.ctx-40"),
    SemanticRule("CTX_41_001", "L4/L5", "ctx.ctx-41"),
    SemanticRule("CTX_42_001", "L4/L5", "ctx.ctx-42"),
    SemanticRule("CTX_43_001", "L4/L5", "ctx.ctx-43"),
    SemanticRule("CTX_44_001", "L4/L5", "ctx.ctx-44"),
    SemanticRule("CTX_45_001", "L4/L5", "ctx.ctx-45"),
    SemanticRule("CTX_46_001", "L4/L5", "ctx.ctx-46"),
    SemanticRule("CTX_47_001", "L4/L5", "ctx.ctx-47"),
    SemanticRule("CTX_48_001", "L4/L5", "ctx.ctx-48"),
    SemanticRule("CTX_49_001", "L4/L5", "ctx.ctx-49"),
    SemanticRule("CTX_50_001", "L4/L5", "ctx.ctx-50"),
    SemanticRule("CTX_51_001", "L4/L5", "ctx.ctx-51"),
    SemanticRule("CTX_52_001", "L4/L5", "ctx.ctx-52"),
    SemanticRule("CTX_53_001", "L4/L5", "ctx.ctx-53"),
    SemanticRule("CTX_54_001", "L4/L5", "ctx.ctx-54"),
    SemanticRule("CTX_55_001", "L4/L5", "ctx.ctx-55"),
    SemanticRule("CTX_56_001", "L4/L5", "ctx.ctx-56"),
    SemanticRule("CTX_57_001", "L4/L5", "ctx.ctx-57"),
    SemanticRule("CTX_58_001", "L4/L5", "ctx.ctx-58"),
    SemanticRule("CTX_59_001", "L4/L5", "ctx.ctx-59"),
    SemanticRule("CTX_60_001", "L4/L5", "ctx.ctx-60"),
    SemanticRule("CTX_61_001", "L4/L5", "ctx.ctx-61"),
    SemanticRule("CTX_62_001", "L4/L5", "ctx.ctx-62"),
    SemanticRule("CTX_63_001", "L4/L5", "ctx.ctx-63"),
    SemanticRule("CTX_64_001", "L4/L5", "ctx.ctx-64"),
    SemanticRule("CTX_65_001", "L4/L5", "ctx.ctx-65"),
    SemanticRule("CTX_66_001", "L4/L5", "ctx.ctx-66"),
    SemanticRule("CTX_67_001", "L4/L5", "ctx.ctx-67"),
    SemanticRule("CTX_68_001", "L4/L5", "ctx.ctx-68"),
    SemanticRule("CTX_69_001", "L4/L5", "ctx.ctx-69"),
    SemanticRule("CTX_70_001", "L4/L5", "ctx.ctx-70"),
    SemanticRule("CTX_71_001", "L4/L5", "ctx.ctx-71"),
    SemanticRule("CTX_72_001", "L4/L5", "ctx.ctx-72"),
    SemanticRule("CTX_73_001", "L4/L5", "ctx.ctx-73"),
    SemanticRule("CTX_74_001", "L4/L5", "ctx.ctx-74"),
    SemanticRule("CTX_75_001", "L4/L5", "ctx.ctx-75"),
    SemanticRule("CTX_76_001", "L4/L5", "ctx.ctx-76"),
    SemanticRule("CTX_77_001", "L4/L5", "ctx.ctx-77"),
    SemanticRule("CTX_78_001", "L4/L5", "ctx.ctx-78"),
    SemanticRule("CTX_79_001", "L4/L5", "ctx.ctx-79"),
    SemanticRule("CTX_80_001", "L4/L5", "ctx.ctx-80"),
    SemanticRule("CTX_81_001", "L4/L5", "ctx.ctx-81"),
    SemanticRule("CTX_82_001", "L4/L5", "ctx.ctx-82"),
    SemanticRule("CTX_83_001", "L4/L5", "ctx.ctx-83"),
    SemanticRule("CTX_84_001", "L4/L5", "ctx.ctx-84"),
    SemanticRule("CTX_85_001", "L4/L5", "ctx.ctx-85"),
    SemanticRule("CTX_86_001", "L4/L5", "ctx.ctx-86"),
    SemanticRule("CTX_87_001", "L4/L5", "ctx.ctx-87"),
    SemanticRule("CTX_88_001", "L4/L5", "ctx.ctx-88"),
    SemanticRule("CTX_89_001", "L4/L5", "ctx.ctx-89"),
    SemanticRule("CTX_90_001", "L4/L5", "ctx.ctx-90"),
    SemanticRule("CTX_91_001", "L4/L5", "ctx.ctx-91"),
    SemanticRule("CTX_92_001", "L4/L5", "ctx.ctx-92"),
    SemanticRule("CTX_93_001", "L4/L5", "ctx.ctx-93"),
    SemanticRule("CTX_94_001", "L4/L5", "ctx.ctx-94"),
    SemanticRule("CTX_95_001", "L4/L5", "ctx.ctx-95"),
    SemanticRule("CTX_96_001", "L4/L5", "ctx.ctx-96"),
    SemanticRule("CTX_97_001", "L4/L5", "ctx.ctx-97"),
    SemanticRule("CTX_98_001", "L4/L5", "ctx.ctx-98"),
    SemanticRule("CTX_99_001", "L4/L5", "ctx.ctx-99"),
    SemanticRule("CTX_100_001", "L4/L5", "ctx.ctx-100"),
    SemanticRule("CTX_101_001", "L4/L5", "ctx.ctx-101"),
    SemanticRule("CTX_102_001", "L4/L5", "ctx.ctx-102"),
    SemanticRule("CTX_103_001", "L4/L5", "ctx.ctx-103"),
    SemanticRule("CTX_104_001", "L4/L5", "ctx.ctx-104"),
    SemanticRule("CTX_105_001", "L4/L5", "ctx.ctx-105"),
    SemanticRule("CTX_106_001", "L4/L5", "ctx.ctx-106"),
    SemanticRule("CTX_107_001", "L4/L5", "ctx.ctx-107"),
    SemanticRule("CTX_108_001", "L4/L5", "ctx.ctx-108"),
    SemanticRule("CTX_109_001", "L4/L5", "ctx.ctx-109"),
    SemanticRule("CTX_110_001", "L4/L5", "ctx.ctx-110"),
    SemanticRule("CTX_111_001", "L4/L5", "ctx.ctx-111"),
    SemanticRule("CTX_112_001", "L4/L5", "ctx.ctx-112"),
    SemanticRule("CTX_113_001", "L4/L5", "ctx.ctx-113"),
    SemanticRule("CTX_114_001", "L4/L5", "ctx.ctx-114"),
    SemanticRule("CTX_115_001", "L4/L5", "ctx.ctx-115"),
    SemanticRule("CTX_116_001", "L4/L5", "ctx.ctx-116"),
    SemanticRule("CTX_117_001", "L4/L5", "ctx.ctx-117"),
    SemanticRule("CTX_118_001", "L4/L5", "ctx.ctx-118"),
    SemanticRule("CTX_119_001", "L4/L5", "ctx.ctx-119"),
    SemanticRule("CTX_120_001", "L4/L5", "ctx.ctx-120"),
    SemanticRule("CTX_121_001", "L4/L5", "ctx.ctx-121"),
    SemanticRule("CTX_122_001", "L4/L5", "ctx.ctx-122"),
    SemanticRule("SCP_03_001", "L4/L5", "scp.scp-03"),
    SemanticRule("SCP_04_001", "L4/L5", "scp.scp-04"),
    SemanticRule("SCP_05_001", "L4/L5", "scp.scp-05"),
    SemanticRule("SCP_06_001", "L4/L5", "scp.scp-06"),
    SemanticRule("SCP_07_001", "L4/L5", "scp.scp-07"),
    SemanticRule("SCP_08_001", "L4/L5", "scp.scp-08"),
    SemanticRule("SCP_09_001", "L4/L5", "scp.scp-09"),
    SemanticRule("SCP_10_001", "L4/L5", "scp.scp-10"),
    SemanticRule("SCP_11_001", "L4/L5", "scp.scp-11"),
    SemanticRule("SCP_12_001", "L4/L5", "scp.scp-12"),
    SemanticRule("SCP_13_001", "L4/L5", "scp.scp-13"),
    SemanticRule("SCP_14_001", "L4/L5", "scp.scp-14"),
    SemanticRule("SCP_15_001", "L4/L5", "scp.scp-15"),
    SemanticRule("SCP_16_001", "L4/L5", "scp.scp-16"),
    SemanticRule("SCP_17_001", "L4/L5", "scp.scp-17"),
    SemanticRule("SCP_18_001", "L4/L5", "scp.scp-18"),
    SemanticRule("SCP_19_001", "L4/L5", "scp.scp-19"),
    SemanticRule("SCP_20_001", "L4/L5", "scp.scp-20"),
    SemanticRule("SCP_21_001", "L4/L5", "scp.scp-21"),
    SemanticRule("SCP_22_001", "L4/L5", "scp.scp-22"),
    SemanticRule("SCP_23_001", "L4/L5", "scp.scp-23"),
    SemanticRule("SCP_24_001", "L4/L5", "scp.scp-24"),
    SemanticRule("SCP_25_001", "L4/L5", "scp.scp-25"),
    SemanticRule("SCP_26_001", "L4/L5", "scp.scp-26"),
    SemanticRule("SCP_27_001", "L4/L5", "scp.scp-27"),
    SemanticRule("SCP_28_001", "L4/L5", "scp.scp-28"),
    SemanticRule("SCP_29_001", "L4/L5", "scp.scp-29"),
    SemanticRule("SCP_30_001", "L4/L5", "scp.scp-30"),
    SemanticRule("SCP_31_001", "L4/L5", "scp.scp-31"),
    SemanticRule("SCP_32_001", "L4/L5", "scp.scp-32"),
    SemanticRule("SCP_33_001", "L4/L5", "scp.scp-33"),
    SemanticRule("SCP_34_001", "L4/L5", "scp.scp-34"),
    SemanticRule("SCP_35_001", "L4/L5", "scp.scp-35"),
    SemanticRule("SCP_36_001", "L4/L5", "scp.scp-36"),
    SemanticRule("SCP_37_001", "L4/L5", "scp.scp-37"),
    SemanticRule("SCP_38_001", "L4/L5", "scp.scp-38"),
    SemanticRule("SCP_39_001", "L4/L5", "scp.scp-39"),
    SemanticRule("SCP_40_001", "L4/L5", "scp.scp-40"),
    SemanticRule("SCP_41_001", "L4/L5", "scp.scp-41"),
    SemanticRule("SCP_42_001", "L4/L5", "scp.scp-42"),
    SemanticRule("SCP_43_001", "L4/L5", "scp.scp-43"),
    SemanticRule("SCP_44_001", "L4/L5", "scp.scp-44"),
    SemanticRule("SCP_45_001", "L4/L5", "scp.scp-45"),
    SemanticRule("SCP_46_001", "L4/L5", "scp.scp-46"),
    SemanticRule("SCP_47_001", "L4/L5", "scp.scp-47"),
    SemanticRule("SCP_48_001", "L4/L5", "scp.scp-48"),
    SemanticRule("SCP_49_001", "L4/L5", "scp.scp-49"),
    SemanticRule("SCP_50_001", "L4/L5", "scp.scp-50"),
    SemanticRule("SCP_51_001", "L4/L5", "scp.scp-51"),
    SemanticRule("SCP_52_001", "L4/L5", "scp.scp-52"),
    SemanticRule("SCP_53_001", "L4/L5", "scp.scp-53"),
    SemanticRule("SCP_54_001", "L4/L5", "scp.scp-54"),
    SemanticRule("SCP_55_001", "L4/L5", "scp.scp-55"),
    SemanticRule("SCP_56_001", "L4/L5", "scp.scp-56"),
    SemanticRule("SCP_57_001", "L4/L5", "scp.scp-57"),
    SemanticRule("SCP_58_001", "L4/L5", "scp.scp-58"),
    SemanticRule("SCP_59_001", "L4/L5", "scp.scp-59"),
    SemanticRule("SCP_60_001", "L4/L5", "scp.scp-60"),
    SemanticRule("SCP_61_001", "L4/L5", "scp.scp-61"),
    SemanticRule("SCP_62_001", "L4/L5", "scp.scp-62"),
    SemanticRule("SCP_63_001", "L4/L5", "scp.scp-63"),
    SemanticRule("SCP_64_001", "L4/L5", "scp.scp-64"),
    SemanticRule("SCP_65_001", "L4/L5", "scp.scp-65"),
    SemanticRule("SCP_66_001", "L4/L5", "scp.scp-66"),
    SemanticRule("SCP_67_001", "L4/L5", "scp.scp-67"),
    SemanticRule("SCP_68_001", "L4/L5", "scp.scp-68"),
    SemanticRule("SCP_69_001", "L4/L5", "scp.scp-69"),
    SemanticRule("SCP_70_001", "L4/L5", "scp.scp-70"),
    SemanticRule("SCP_71_001", "L4/L5", "scp.scp-71"),
    SemanticRule("SCP_72_001", "L4/L5", "scp.scp-72"),
    SemanticRule("SCP_73_001", "L4/L5", "scp.scp-73"),
    SemanticRule("SCP_74_001", "L4/L5", "scp.scp-74"),
    SemanticRule("SCP_75_001", "L4/L5", "scp.scp-75"),
    SemanticRule("SCP_76_001", "L4/L5", "scp.scp-76"),
    SemanticRule("SCP_77_001", "L4/L5", "scp.scp-77"),
    SemanticRule("SCP_78_001", "L4/L5", "scp.scp-78"),
    SemanticRule("SCP_79_001", "L4/L5", "scp.scp-79"),
    SemanticRule("SCP_80_001", "L4/L5", "scp.scp-80"),
    SemanticRule("SCP_81_001", "L4/L5", "scp.scp-81"),
    SemanticRule("SCP_82_001", "L4/L5", "scp.scp-82"),
    SemanticRule("SCP_83_001", "L4/L5", "scp.scp-83"),
    SemanticRule("SCP_84_001", "L4/L5", "scp.scp-84"),
    SemanticRule("SCP_85_001", "L4/L5", "scp.scp-85"),
    SemanticRule("SCP_86_001", "L4/L5", "scp.scp-86"),
    SemanticRule("SCP_87_001", "L4/L5", "scp.scp-87"),
    SemanticRule("SCP_88_001", "L4/L5", "scp.scp-88"),
    SemanticRule("SCP_89_001", "L4/L5", "scp.scp-89"),
    SemanticRule("SCP_90_001", "L4/L5", "scp.scp-90"),
    SemanticRule("SCP_91_001", "L4/L5", "scp.scp-91"),
    SemanticRule("SCP_92_001", "L4/L5", "scp.scp-92"),
    SemanticRule("SCP_93_001", "L4/L5", "scp.scp-93"),
    SemanticRule("SCP_94_001", "L4/L5", "scp.scp-94"),
    SemanticRule("SCP_95_001", "L4/L5", "scp.scp-95"),
    SemanticRule("SCP_96_001", "L4/L5", "scp.scp-96"),
    SemanticRule("SCP_97_001", "L4/L5", "scp.scp-97"),
    SemanticRule("SCP_98_001", "L4/L5", "scp.scp-98"),
    SemanticRule("SCP_99_001", "L4/L5", "scp.scp-99"),
    SemanticRule("SCP_100_001", "L4/L5", "scp.scp-100"),
    SemanticRule("SCP_101_001", "L4/L5", "scp.scp-101"),
    SemanticRule("SCP_102_001", "L4/L5", "scp.scp-102"),
    SemanticRule("SCP_103_001", "L4/L5", "scp.scp-103"),
    SemanticRule("SCP_104_001", "L4/L5", "scp.scp-104"),
    SemanticRule("SCP_105_001", "L4/L5", "scp.scp-105"),
    SemanticRule("SCP_106_001", "L4/L5", "scp.scp-106"),
    SemanticRule("SCP_107_001", "L4/L5", "scp.scp-107"),
    SemanticRule("SCP_108_001", "L4/L5", "scp.scp-108"),
    SemanticRule("SCP_109_001", "L4/L5", "scp.scp-109"),
    SemanticRule("SCP_110_001", "L4/L5", "scp.scp-110"),
    SemanticRule("SCP_111_001", "L4/L5", "scp.scp-111"),
    SemanticRule("SCP_112_001", "L4/L5", "scp.scp-112"),
    SemanticRule("SCP_113_001", "L4/L5", "scp.scp-113"),
    SemanticRule("SCP_114_001", "L4/L5", "scp.scp-114"),
    SemanticRule("SCP_115_001", "L4/L5", "scp.scp-115"),
    SemanticRule("SCP_116_001", "L4/L5", "scp.scp-116"),
    SemanticRule("SCP_117_001", "L4/L5", "scp.scp-117"),
    SemanticRule("SCP_118_001", "L4/L5", "scp.scp-118"),
    SemanticRule("SCP_119_001", "L4/L5", "scp.scp-119"),
    SemanticRule("SCP_120_001", "L4/L5", "scp.scp-120"),
    SemanticRule("SCP_121_001", "L4/L5", "scp.scp-121"),
    SemanticRule("SCP_122_001", "L4/L5", "scp.scp-122"),
    SemanticRule("SCP_123_001", "L4/L5", "scp.scp-123"),
    SemanticRule("SCP_124_001", "L4/L5", "scp.scp-124"),
    SemanticRule("SCP_125_001", "L4/L5", "scp.scp-125"),
    SemanticRule("SCP_126_001", "L4/L5", "scp.scp-126"),
    SemanticRule("SCP_127_001", "L4/L5", "scp.scp-127"),
    SemanticRule("SCP_128_001", "L4/L5", "scp.scp-128"),
    SemanticRule("SCP_129_001", "L4/L5", "scp.scp-129"),
    SemanticRule("SCP_130_001", "L4/L5", "scp.scp-130"),
    SemanticRule("SCP_131_001", "L4/L5", "scp.scp-131"),
    SemanticRule("SCP_132_001", "L4/L5", "scp.scp-132"),
    SemanticRule("SCP_133_001", "L4/L5", "scp.scp-133"),
    SemanticRule("SCP_134_001", "L4/L5", "scp.scp-134"),
    SemanticRule("SCP_135_001", "L4/L5", "scp.scp-135"),
    SemanticRule("SCP_136_001", "L4/L5", "scp.scp-136"),
    SemanticRule("SCP_137_001", "L4/L5", "scp.scp-137"),
    SemanticRule("SCP_138_001", "L4/L5", "scp.scp-138"),
    SemanticRule("SCP_139_001", "L4/L5", "scp.scp-139"),
    SemanticRule("SCP_140_001", "L4/L5", "scp.scp-140"),
    SemanticRule("SCP_141_001", "L4/L5", "scp.scp-141"),
    SemanticRule("SCP_142_001", "L4/L5", "scp.scp-142"),
    SemanticRule("SCP_143_001", "L4/L5", "scp.scp-143"),
    SemanticRule("SCP_144_001", "L4/L5", "scp.scp-144"),
    SemanticRule("SCP_145_001", "L4/L5", "scp.scp-145"),
    SemanticRule("SCP_146_001", "L4/L5", "scp.scp-146"),
    SemanticRule("SCP_147_001", "L4/L5", "scp.scp-147"),
    SemanticRule("SCP_148_001", "L4/L5", "scp.scp-148"),
    SemanticRule("SCP_149_001", "L4/L5", "scp.scp-149"),
    SemanticRule("SCP_150_001", "L4/L5", "scp.scp-150"),
    SemanticRule("SCP_151_001", "L4/L5", "scp.scp-151"),
    SemanticRule("SCP_152_001", "L4/L5", "scp.scp-152"),
    SemanticRule("SCP_153_001", "L4/L5", "scp.scp-153"),
    SemanticRule("SCP_154_001", "L4/L5", "scp.scp-154"),
    SemanticRule("SCP_155_001", "L4/L5", "scp.scp-155"),
    SemanticRule("SCP_156_001", "L4/L5", "scp.scp-156"),
    SemanticRule("SCP_157_001", "L4/L5", "scp.scp-157"),
    SemanticRule("SCP_158_001", "L4/L5", "scp.scp-158"),
    SemanticRule("SCP_159_001", "L4/L5", "scp.scp-159"),
    SemanticRule("SCP_160_001", "L4/L5", "scp.scp-160"),
    SemanticRule("SCP_161_001", "L4/L5", "scp.scp-161"),
    SemanticRule("SCP_162_001", "L4/L5", "scp.scp-162"),
    SemanticRule("SCP_163_001", "L4/L5", "scp.scp-163"),
    SemanticRule("SCP_164_001", "L4/L5", "scp.scp-164"),
    SemanticRule("SCP_165_001", "L4/L5", "scp.scp-165"),
    SemanticRule("SCP_166_001", "L4/L5", "scp.scp-166"),
    SemanticRule("SCP_167_001", "L4/L5", "scp.scp-167"),
    SemanticRule("SCP_168_001", "L4/L5", "scp.scp-168"),
    SemanticRule("SCP_169_001", "L4/L5", "scp.scp-169"),
    SemanticRule("SCP_170_001", "L4/L5", "scp.scp-170"),
    SemanticRule("SCP_171_001", "L4/L5", "scp.scp-171"),
    SemanticRule("SCP_172_001", "L4/L5", "scp.scp-172"),
    SemanticRule("SCP_173_001", "L4/L5", "scp.scp-173"),
    SemanticRule("SCP_174_001", "L4/L5", "scp.scp-174"),
    SemanticRule("SCP_175_001", "L4/L5", "scp.scp-175"),
    SemanticRule("SCP_176_001", "L4/L5", "scp.scp-176"),
    SemanticRule("SCP_177_001", "L4/L5", "scp.scp-177"),
    SemanticRule("SCP_178_001", "L4/L5", "scp.scp-178"),
    SemanticRule("SCP_179_001", "L4/L5", "scp.scp-179"),
    SemanticRule("SCP_180_001", "L4/L5", "scp.scp-180"),
    SemanticRule("SCP_181_001", "L4/L5", "scp.scp-181"),
    SemanticRule("SCP_182_001", "L4/L5", "scp.scp-182"),
    SemanticRule("SCP_183_001", "L4/L5", "scp.scp-183"),
    SemanticRule("SCP_184_001", "L4/L5", "scp.scp-184"),
    SemanticRule("SCP_185_001", "L4/L5", "scp.scp-185"),
    SemanticRule("SCP_186_001", "L4/L5", "scp.scp-186"),
    SemanticRule("SCP_187_001", "L4/L5", "scp.scp-187"),
    SemanticRule("SCP_188_001", "L4/L5", "scp.scp-188"),
    SemanticRule("SCP_189_001", "L4/L5", "scp.scp-189"),
    SemanticRule("SCP_190_001", "L4/L5", "scp.scp-190"),
    SemanticRule("SCP_191_001", "L4/L5", "scp.scp-191"),
    SemanticRule("SCP_192_001", "L4/L5", "scp.scp-192"),
    SemanticRule("SCP_193_001", "L4/L5", "scp.scp-193"),
    SemanticRule("SCP_194_001", "L4/L5", "scp.scp-194"),
    SemanticRule("SCP_195_001", "L4/L5", "scp.scp-195"),
    SemanticRule("SCP_196_001", "L4/L5", "scp.scp-196"),
    SemanticRule("SCP_197_001", "L4/L5", "scp.scp-197"),
    SemanticRule("SCP_198_001", "L4/L5", "scp.scp-198"),
    SemanticRule("SCP_199_001", "L4/L5", "scp.scp-199"),
    SemanticRule("SCP_200_001", "L4/L5", "scp.scp-200"),
    SemanticRule("SCP_201_001", "L4/L5", "scp.scp-201"),
    SemanticRule("SCP_202_001", "L4/L5", "scp.scp-202"),
    SemanticRule("SCP_203_001", "L4/L5", "scp.scp-203"),
    SemanticRule("SCP_204_001", "L4/L5", "scp.scp-204"),
    SemanticRule("SCP_205_001", "L4/L5", "scp.scp-205"),
    SemanticRule("SCP_206_001", "L4/L5", "scp.scp-206"),
    SemanticRule("SCP_207_001", "L4/L5", "scp.scp-207"),
    SemanticRule("SCP_208_001", "L4/L5", "scp.scp-208"),
    SemanticRule("SCP_209_001", "L4/L5", "scp.scp-209"),
    SemanticRule("SCP_210_001", "L4/L5", "scp.scp-210"),
    SemanticRule("SCP_211_001", "L4/L5", "scp.scp-211"),
    SemanticRule("SCP_212_001", "L4/L5", "scp.scp-212"),
    SemanticRule("SCP_213_001", "L4/L5", "scp.scp-213"),
    SemanticRule("SCP_214_001", "L4/L5", "scp.scp-214"),
    SemanticRule("SCP_215_001", "L4/L5", "scp.scp-215"),
    SemanticRule("SCP_216_001", "L4/L5", "scp.scp-216"),
    SemanticRule("SCP_217_001", "L4/L5", "scp.scp-217"),
    SemanticRule("SCP_218_001", "L4/L5", "scp.scp-218"),
    SemanticRule("SCP_219_001", "L4/L5", "scp.scp-219"),
    SemanticRule("SCP_220_001", "L4/L5", "scp.scp-220"),
    SemanticRule("SCP_221_001", "L4/L5", "scp.scp-221"),
    SemanticRule("SCP_222_001", "L4/L5", "scp.scp-222"),
    SemanticRule("SCP_223_001", "L4/L5", "scp.scp-223"),
    SemanticRule("SCP_224_001", "L4/L5", "scp.scp-224"),
    SemanticRule("SCP_225_001", "L4/L5", "scp.scp-225"),
    SemanticRule("SCP_226_001", "L4/L5", "scp.scp-226"),
    SemanticRule("SCP_227_001", "L4/L5", "scp.scp-227"),
    SemanticRule("SCP_228_001", "L4/L5", "scp.scp-228"),
    SemanticRule("SCP_229_001", "L4/L5", "scp.scp-229"),
    SemanticRule("SCP_230_001", "L4/L5", "scp.scp-230"),
    SemanticRule("SCP_231_001", "L4/L5", "scp.scp-231"),
    SemanticRule("SCP_232_001", "L4/L5", "scp.scp-232"),
    SemanticRule("SCP_233_001", "L4/L5", "scp.scp-233"),
    SemanticRule("SCP_234_001", "L4/L5", "scp.scp-234"),
    SemanticRule("SCP_235_001", "L4/L5", "scp.scp-235"),
    SemanticRule("SCP_236_001", "L4/L5", "scp.scp-236"),
    SemanticRule("SCP_237_001", "L4/L5", "scp.scp-237"),
    SemanticRule("PRV_003_001", "L4/L5", "prv.prv-003"),
    SemanticRule("PRV_004_001", "L4/L5", "prv.prv-004"),
    SemanticRule("PRV_005_001", "L4/L5", "prv.prv-005"),
    SemanticRule("PRV_006_001", "L4/L5", "prv.prv-006"),
    SemanticRule("PRV_007_001", "L4/L5", "prv.prv-007"),
    SemanticRule("PRV_008_001", "L4/L5", "prv.prv-008"),
    SemanticRule("PRV_009_001", "L4/L5", "prv.prv-009"),
    SemanticRule("PRV_010_001", "L4/L5", "prv.prv-010"),
    SemanticRule("PRV_011_001", "L4/L5", "prv.prv-011"),
    SemanticRule("PRV_012_001", "L4/L5", "prv.prv-012"),
    SemanticRule("PRV_013_001", "L4/L5", "prv.prv-013"),
    SemanticRule("PRV_014_001", "L4/L5", "prv.prv-014"),
    SemanticRule("PRV_015_001", "L4/L5", "prv.prv-015"),
    SemanticRule("PRV_016_001", "L4/L5", "prv.prv-016"),
    SemanticRule("PRV_017_001", "L4/L5", "prv.prv-017"),
    SemanticRule("PRV_018_001", "L4/L5", "prv.prv-018"),
    SemanticRule("PRV_019_001", "L4/L5", "prv.prv-019"),
    SemanticRule("PRV_020_001", "L4/L5", "prv.prv-020"),
    SemanticRule("PRV_021_001", "L4/L5", "prv.prv-021"),
    SemanticRule("PRV_022_001", "L4/L5", "prv.prv-022"),
    SemanticRule("PRV_023_001", "L4/L5", "prv.prv-023"),
    SemanticRule("PRV_024_001", "L4/L5", "prv.prv-024"),
    SemanticRule("PRV_025_001", "L4/L5", "prv.prv-025"),
    SemanticRule("PRV_026_001", "L4/L5", "prv.prv-026"),
    SemanticRule("PRV_027_001", "L4/L5", "prv.prv-027"),
    SemanticRule("PRV_028_001", "L4/L5", "prv.prv-028"),
    SemanticRule("PRV_029_001", "L4/L5", "prv.prv-029"),
    SemanticRule("PRV_030_001", "L4/L5", "prv.prv-030"),
    SemanticRule("PRV_031_001", "L4/L5", "prv.prv-031"),
    SemanticRule("PRV_032_001", "L4/L5", "prv.prv-032"),
    SemanticRule("PRV_033_001", "L4/L5", "prv.prv-033"),
    SemanticRule("PRV_034_001", "L4/L5", "prv.prv-034"),
    SemanticRule("PRV_035_001", "L4/L5", "prv.prv-035"),
    SemanticRule("PRV_036_001", "L4/L5", "prv.prv-036"),
    SemanticRule("PRV_037_001", "L4/L5", "prv.prv-037"),
    SemanticRule("PRV_038_001", "L4/L5", "prv.prv-038"),
    SemanticRule("PRV_039_001", "L4/L5", "prv.prv-039"),
    SemanticRule("PRV_040_001", "L4/L5", "prv.prv-040"),
    SemanticRule("PRV_041_001", "L4/L5", "prv.prv-041"),
    SemanticRule("PRV_042_001", "L4/L5", "prv.prv-042"),
    SemanticRule("PRV_043_001", "L4/L5", "prv.prv-043"),
    SemanticRule("PRV_045_001", "L4/L5", "prv.prv-045"),
    SemanticRule("PRV_046_001", "L4/L5", "prv.prv-046"),
    SemanticRule("PRV_047_001", "L4/L5", "prv.prv-047"),
    SemanticRule("PRV_048_001", "L4/L5", "prv.prv-048"),
    SemanticRule("PRV_049_001", "L4/L5", "prv.prv-049"),
    SemanticRule("PRV_050_001", "L4/L5", "prv.prv-050"),
    SemanticRule("PRV_051_001", "L4/L5", "prv.prv-051"),
    SemanticRule("PRV_053_001", "L4/L5", "prv.prv-053"),
    SemanticRule("AC_001_001", "L4/L5", "ac.ac-001"),
    SemanticRule("AC_002_001", "L4/L5", "ac.ac-002"),
    SemanticRule("AC_003_001", "L4/L5", "ac.ac-003"),
    SemanticRule("AC_006_001", "L4/L5", "ac.ac-006"),
    SemanticRule("AC_007_001", "L4/L5", "ac.ac-007"),
    SemanticRule("AC_010_001", "L4/L5", "ac.ac-010"),
    SemanticRule("AC_011_001", "L4/L5", "ac.ac-011"),
    SemanticRule("AC_014_001", "L4/L5", "ac.ac-014"),
    SemanticRule("AC_015_001", "L4/L5", "ac.ac-015"),
    SemanticRule("AC_016_001", "L4/L5", "ac.ac-016"),
    SemanticRule("AC_017_001", "L4/L5", "ac.ac-017"),
    SemanticRule("AC_018_001", "L4/L5", "ac.ac-018"),
    SemanticRule("AC_019_001", "L4/L5", "ac.ac-019"),
    SemanticRule("AC_020_001", "L4/L5", "ac.ac-020"),
    SemanticRule("AC_021_001", "L4/L5", "ac.ac-021"),
    SemanticRule("AC_022_001", "L4/L5", "ac.ac-022"),
    SemanticRule("AC_023_001", "L4/L5", "ac.ac-023"),
    SemanticRule("AC_024_001", "L4/L5", "ac.ac-024"),
    SemanticRule("AC_025_001", "L4/L5", "ac.ac-025"),
    SemanticRule("AC_026_001", "L4/L5", "ac.ac-026"),
    SemanticRule("AC_027_001", "L4/L5", "ac.ac-027"),
    SemanticRule("AC_028_001", "L4/L5", "ac.ac-028"),
    SemanticRule("AC_029_001", "L4/L5", "ac.ac-029"),
    SemanticRule("AC_030_001", "L4/L5", "ac.ac-030"),
    SemanticRule("AC_031_001", "L4/L5", "ac.ac-031"),
    SemanticRule("AC_032_001", "L4/L5", "ac.ac-032"),
    SemanticRule("AC_033_001", "L4/L5", "ac.ac-033"),
    SemanticRule("AC_034_001", "L4/L5", "ac.ac-034"),
    SemanticRule("AC_035_001", "L4/L5", "ac.ac-035"),
    SemanticRule("AC_036_001", "L4/L5", "ac.ac-036"),
    SemanticRule("AC_037_001", "L4/L5", "ac.ac-037"),
    SemanticRule("AC_038_001", "L4/L5", "ac.ac-038"),
    SemanticRule("AC_039_001", "L4/L5", "ac.ac-039"),
    SemanticRule("AC_040_001", "L4/L5", "ac.ac-040"),
    SemanticRule("AC_041_001", "L4/L5", "ac.ac-041"),
    SemanticRule("AC_042_001", "L4/L5", "ac.ac-042"),
    SemanticRule("AC_043_001", "L4/L5", "ac.ac-043"),
    SemanticRule("AC_044_001", "L4/L5", "ac.ac-044"),
    SemanticRule("AC_045_001", "L4/L5", "ac.ac-045"),
    SemanticRule("AC_046_001", "L4/L5", "ac.ac-046"),
    SemanticRule("AC_047_001", "L4/L5", "ac.ac-047"),
    SemanticRule("AC_048_001", "L4/L5", "ac.ac-048"),
    SemanticRule("AC_049_001", "L4/L5", "ac.ac-049"),
    SemanticRule("AC_050_001", "L4/L5", "ac.ac-050"),
    SemanticRule("AC_051_001", "L4/L5", "ac.ac-051"),
    SemanticRule("AC_052_001", "L4/L5", "ac.ac-052"),
    SemanticRule("AC_053_001", "L4/L5", "ac.ac-053"),
    SemanticRule("AC_054_001", "L4/L5", "ac.ac-054"),
    SemanticRule("AC_055_001", "L4/L5", "ac.ac-055"),
    SemanticRule("AC_056_001", "L4/L5", "ac.ac-056"),
    SemanticRule("AC_057_001", "L4/L5", "ac.ac-057"),
    SemanticRule("AC_058_001", "L4/L5", "ac.ac-058"),
    SemanticRule("AC_059_001", "L4/L5", "ac.ac-059"),
    SemanticRule("AC_060_001", "L4/L5", "ac.ac-060"),
    SemanticRule("AC_061_001", "L4/L5", "ac.ac-061"),
    SemanticRule("AC_062_001", "L4/L5", "ac.ac-062"),
    SemanticRule("AC_063_001", "L4/L5", "ac.ac-063"),
    SemanticRule("AC_064_001", "L4/L5", "ac.ac-064"),
    SemanticRule("AC_065_001", "L4/L5", "ac.ac-065"),
    SemanticRule("AC_066_001", "L4/L5", "ac.ac-066"),
    SemanticRule("AC_067_001", "L4/L5", "ac.ac-067"),
    SemanticRule("AC_068_001", "L4/L5", "ac.ac-068"),
    SemanticRule("AC_069_001", "L4/L5", "ac.ac-069"),
    SemanticRule("AC_070_001", "L4/L5", "ac.ac-070"),
    SemanticRule("AC_071_001", "L4/L5", "ac.ac-071"),
    SemanticRule("AC_072_001", "L4/L5", "ac.ac-072"),
    SemanticRule("AC_073_001", "L4/L5", "ac.ac-073"),
    SemanticRule("AC_074_001", "L4/L5", "ac.ac-074"),
    SemanticRule("AC_075_001", "L4/L5", "ac.ac-075"),
    SemanticRule("AC_076_001", "L4/L5", "ac.ac-076"),
    SemanticRule("AC_077_001", "L4/L5", "ac.ac-077"),
    SemanticRule("AC_078_001", "L4/L5", "ac.ac-078"),
    SemanticRule("AC_079_001", "L4/L5", "ac.ac-079"),
    SemanticRule("AC_080_001", "L4/L5", "ac.ac-080"),
    SemanticRule("AC_081_001", "L4/L5", "ac.ac-081"),
    SemanticRule("AC_082_001", "L4/L5", "ac.ac-082"),
    SemanticRule("AC_083_001", "L4/L5", "ac.ac-083"),
    SemanticRule("AC_084_001", "L4/L5", "ac.ac-084"),
    SemanticRule("AC_085_001", "L4/L5", "ac.ac-085"),
    SemanticRule("AC_086_001", "L4/L5", "ac.ac-086"),
    SemanticRule("AC_087_001", "L4/L5", "ac.ac-087"),
    SemanticRule("AC_088_001", "L4/L5", "ac.ac-088"),
    SemanticRule("AC_089_001", "L4/L5", "ac.ac-089"),
    SemanticRule("AC_090_001", "L4/L5", "ac.ac-090"),
    SemanticRule("AC_091_001", "L4/L5", "ac.ac-091"),
    SemanticRule("AC_092_001", "L4/L5", "ac.ac-092"),
    SemanticRule("AC_093_001", "L4/L5", "ac.ac-093"),
    SemanticRule("AC_094_001", "L4/L5", "ac.ac-094"),
    SemanticRule("AC_095_001", "L4/L5", "ac.ac-095"),
    SemanticRule("AC_096_001", "L4/L5", "ac.ac-096"),
    SemanticRule("AC_097_001", "L4/L5", "ac.ac-097"),
    SemanticRule("AC_098_001", "L4/L5", "ac.ac-098"),
    SemanticRule("AC_099_001", "L4/L5", "ac.ac-099"),
    SemanticRule("AC_100_001", "L4/L5", "ac.ac-100"),
    SemanticRule("AC_101_001", "L4/L5", "ac.ac-101"),
    SemanticRule("AC_102_001", "L4/L5", "ac.ac-102"),
    SemanticRule("AC_103_001", "L4/L5", "ac.ac-103"),
    SemanticRule("AC_104_001", "L4/L5", "ac.ac-104"),
    SemanticRule("AC_105_001", "L4/L5", "ac.ac-105"),
    SemanticRule("AC_106_001", "L4/L5", "ac.ac-106"),
    SemanticRule("AC_107_001", "L4/L5", "ac.ac-107"),
    SemanticRule("AC_108_001", "L4/L5", "ac.ac-108"),
    SemanticRule("AC_109_001", "L4/L5", "ac.ac-109"),
    SemanticRule("AC_110_001", "L4/L5", "ac.ac-110"),
    SemanticRule("AC_111_001", "L4/L5", "ac.ac-111"),
    SemanticRule("AC_112_001", "L4/L5", "ac.ac-112"),
    SemanticRule("AC_113_001", "L4/L5", "ac.ac-113"),
    SemanticRule("AC_114_001", "L4/L5", "ac.ac-114"),
    SemanticRule("AC_115_001", "L4/L5", "ac.ac-115"),
    SemanticRule("AC_116_001", "L4/L5", "ac.ac-116"),
    SemanticRule("AC_117_001", "L4/L5", "ac.ac-117"),
    SemanticRule("AC_118_001", "L4/L5", "ac.ac-118"),
    SemanticRule("AC_119_001", "L4/L5", "ac.ac-119"),
    SemanticRule("AC_120_001", "L4/L5", "ac.ac-120"),
    SemanticRule("AC_121_001", "L4/L5", "ac.ac-121"),
    SemanticRule("AC_122_001", "L4/L5", "ac.ac-122"),
    SemanticRule("AC_123_001", "L4/L5", "ac.ac-123"),
    SemanticRule("TR_001_001", "L4/L5", "tr.tr-001"),
    SemanticRule("TR_002_001", "L4/L5", "tr.tr-002"),
    SemanticRule("TR_003_001", "L4/L5", "tr.tr-003"),
    SemanticRule("TR_004_001", "L4/L5", "tr.tr-004"),
    SemanticRule("TR_005_001", "L4/L5", "tr.tr-005"),
    SemanticRule("TR_006_001", "L4/L5", "tr.tr-006"),
    SemanticRule("TR_008_001", "L4/L5", "tr.tr-008"),
    SemanticRule("TR_009_001", "L4/L5", "tr.tr-009"),
    SemanticRule("TR_010_001", "L4/L5", "tr.tr-010"),
    SemanticRule("TR_011_001", "L4/L5", "tr.tr-011"),
    SemanticRule("TR_013_001", "L4/L5", "tr.tr-013"),
    SemanticRule("TR_014_001", "L4/L5", "tr.tr-014"),
    SemanticRule("TR_015_001", "L4/L5", "tr.tr-015"),
    SemanticRule("TR_016_001", "L4/L5", "tr.tr-016"),
    SemanticRule("TR_017_001", "L4/L5", "tr.tr-017"),
    SemanticRule("TR_018_001", "L4/L5", "tr.tr-018"),
    SemanticRule("TR_019_001", "L4/L5", "tr.tr-019"),
    SemanticRule("TR_020_001", "L4/L5", "tr.tr-020"),
    SemanticRule("TR_021_001", "L4/L5", "tr.tr-021"),
    SemanticRule("TR_022_001", "L4/L5", "tr.tr-022"),
    SemanticRule("TR_023_001", "L4/L5", "tr.tr-023"),
    SemanticRule("TR_024_001", "L4/L5", "tr.tr-024"),
    SemanticRule("TR_025_001", "L4/L5", "tr.tr-025"),
    SemanticRule("TR_027_001", "L4/L5", "tr.tr-027"),
    SemanticRule("TR_031_001", "L4/L5", "tr.tr-031"),
    SemanticRule("TR_032_001", "L4/L5", "tr.tr-032"),
    SemanticRule("TR_035_001", "L4/L5", "tr.tr-035"),
    SemanticRule("TR_037_001", "L4/L5", "tr.tr-037"),
    SemanticRule("TR_038_001", "L4/L5", "tr.tr-038"),
    SemanticRule("TR_039_001", "L4/L5", "tr.tr-039"),
    SemanticRule("TR_040_001", "L4/L5", "tr.tr-040"),
    SemanticRule("TR_041_001", "L4/L5", "tr.tr-041"),
    SemanticRule("TR_042_001", "L4/L5", "tr.tr-042"),
    SemanticRule("TR_043_001", "L4/L5", "tr.tr-043"),
    SemanticRule("TR_044_001", "L4/L5", "tr.tr-044"),
    SemanticRule("TR_045_001", "L4/L5", "tr.tr-045"),
    SemanticRule("TR_046_001", "L4/L5", "tr.tr-046"),
    SemanticRule("TR_047_001", "L4/L5", "tr.tr-047"),
    SemanticRule("TR_048_001", "L4/L5", "tr.tr-048"),
    SemanticRule("TR_049_001", "L4/L5", "tr.tr-049"),
    SemanticRule("TR_050_001", "L4/L5", "tr.tr-050"),
    SemanticRule("TR_051_001", "L4/L5", "tr.tr-051"),
    SemanticRule("TR_052_001", "L4/L5", "tr.tr-052"),
    SemanticRule("TR_053_001", "L4/L5", "tr.tr-053"),
    SemanticRule("TR_054_001", "L4/L5", "tr.tr-054"),
    SemanticRule("TR_055_001", "L4/L5", "tr.tr-055"),
    SemanticRule("TR_056_001", "L4/L5", "tr.tr-056"),
    SemanticRule("TR_057_001", "L4/L5", "tr.tr-057"),
    SemanticRule("TR_058_001", "L4/L5", "tr.tr-058"),
    SemanticRule("TR_059_001", "L4/L5", "tr.tr-059"),
    SemanticRule("TR_060_001", "L4/L5", "tr.tr-060"),
    SemanticRule("TR_061_001", "L4/L5", "tr.tr-061"),
    SemanticRule("TR_062_001", "L4/L5", "tr.tr-062"),
    SemanticRule("TR_063_001", "L4/L5", "tr.tr-063"),
    SemanticRule("TR_064_001", "L4/L5", "tr.tr-064"),
    SemanticRule("TR_065_001", "L4/L5", "tr.tr-065"),
    SemanticRule("TR_066_001", "L4/L5", "tr.tr-066"),
    SemanticRule("TR_067_001", "L4/L5", "tr.tr-067"),
    SemanticRule("TR_068_001", "L4/L5", "tr.tr-068"),
    SemanticRule("TR_069_001", "L4/L5", "tr.tr-069"),
    SemanticRule("TR_070_001", "L4/L5", "tr.tr-070"),
    SemanticRule("TR_071_001", "L4/L5", "tr.tr-071"),
    SemanticRule("TR_072_001", "L4/L5", "tr.tr-072"),
    SemanticRule("TR_073_001", "L4/L5", "tr.tr-073"),
    SemanticRule("TR_074_001", "L4/L5", "tr.tr-074"),
    SemanticRule("TR_075_001", "L4/L5", "tr.tr-075"),
    SemanticRule("TR_076_001", "L4/L5", "tr.tr-076"),
    SemanticRule("TR_077_001", "L4/L5", "tr.tr-077"),
    SemanticRule("TR_078_001", "L4/L5", "tr.tr-078"),
    SemanticRule("TR_079_001", "L4/L5", "tr.tr-079"),
    SemanticRule("TR_080_001", "L4/L5", "tr.tr-080"),
    SemanticRule("TR_081_001", "L4/L5", "tr.tr-081"),
    SemanticRule("TR_082_001", "L4/L5", "tr.tr-082"),
    SemanticRule("TR_083_001", "L4/L5", "tr.tr-083"),
    SemanticRule("TR_084_001", "L4/L5", "tr.tr-084"),
    SemanticRule("TR_085_001", "L4/L5", "tr.tr-085"),
    SemanticRule("TR_086_001", "L4/L5", "tr.tr-086"),
    SemanticRule("TR_087_001", "L4/L5", "tr.tr-087"),
    SemanticRule("TR_088_001", "L4/L5", "tr.tr-088"),
    SemanticRule("TR_089_001", "L4/L5", "tr.tr-089"),
    SemanticRule("TR_090_001", "L4/L5", "tr.tr-090"),
    SemanticRule("TR_091_001", "L4/L5", "tr.tr-091"),
    SemanticRule("TR_092_001", "L4/L5", "tr.tr-092"),
    SemanticRule("TR_093_001", "L4/L5", "tr.tr-093"),
    SemanticRule("TR_094_001", "L4/L5", "tr.tr-094"),
    SemanticRule("TR_095_001", "L4/L5", "tr.tr-095"),
    SemanticRule("TR_096_001", "L4/L5", "tr.tr-096"),
    SemanticRule("TR_097_001", "L4/L5", "tr.tr-097"),
    SemanticRule("TR_098_001", "L4/L5", "tr.tr-098"),
    SemanticRule("TR_099_001", "L4/L5", "tr.tr-099"),
    SemanticRule("TR_100_001", "L4/L5", "tr.tr-100"),
    SemanticRule("TR_101_001", "L4/L5", "tr.tr-101"),
    SemanticRule("TR_102_001", "L4/L5", "tr.tr-102"),
    SemanticRule("TR_103_001", "L4/L5", "tr.tr-103"),
    SemanticRule("TR_104_001", "L4/L5", "tr.tr-104"),
    SemanticRule("TR_105_001", "L4/L5", "tr.tr-105"),
    SemanticRule("TR_106_001", "L4/L5", "tr.tr-106"),
    SemanticRule("TR_107_001", "L4/L5", "tr.tr-107"),
    SemanticRule("TR_108_001", "L4/L5", "tr.tr-108"),
    SemanticRule("TR_109_001", "L4/L5", "tr.tr-109"),
    SemanticRule("TR_110_001", "L4/L5", "tr.tr-110"),
    SemanticRule("TR_111_001", "L4/L5", "tr.tr-111"),
    SemanticRule("TR_112_001", "L4/L5", "tr.tr-112"),
    SemanticRule("TR_113_001", "L4/L5", "tr.tr-113"),
    SemanticRule("TR_114_001", "L4/L5", "tr.tr-114"),
    SemanticRule("TR_115_001", "L4/L5", "tr.tr-115"),
    SemanticRule("TR_116_001", "L4/L5", "tr.tr-116"),
    SemanticRule("TR_117_001", "L4/L5", "tr.tr-117"),
    SemanticRule("TR_118_001", "L4/L5", "tr.tr-118"),
    SemanticRule("TR_119_001", "L4/L5", "tr.tr-119"),
    SemanticRule("TR_120_001", "L4/L5", "tr.tr-120"),
    SemanticRule("TR_121_001", "L4/L5", "tr.tr-121"),
    SemanticRule("TR_122_001", "L4/L5", "tr.tr-122"),
    SemanticRule("TR_123_001", "L4/L5", "tr.tr-123"),
    SemanticRule("TR_124_001", "L4/L5", "tr.tr-124"),
    SemanticRule("TR_125_001", "L4/L5", "tr.tr-125"),
    SemanticRule("TR_126_001", "L4/L5", "tr.tr-126"),
    SemanticRule("TR_127_001", "L4/L5", "tr.tr-127"),
    SemanticRule("TR_128_001", "L4/L5", "tr.tr-128"),
    SemanticRule("TR_129_001", "L4/L5", "tr.tr-129"),
    SemanticRule("TR_130_001", "L4/L5", "tr.tr-130"),
    SemanticRule("TR_131_001", "L4/L5", "tr.tr-131"),
    SemanticRule("TR_132_001", "L4/L5", "tr.tr-132"),
    SemanticRule("TR_133_001", "L4/L5", "tr.tr-133"),
    SemanticRule("TR_134_001", "L4/L5", "tr.tr-134"),
    SemanticRule("TR_135_001", "L4/L5", "tr.tr-135"),
    SemanticRule("TR_136_001", "L4/L5", "tr.tr-136"),
    SemanticRule("TR_137_001", "L4/L5", "tr.tr-137"),
    SemanticRule("TR_138_001", "L4/L5", "tr.tr-138"),
    SemanticRule("TR_139_001", "L4/L5", "tr.tr-139"),
    SemanticRule("TR_140_001", "L4/L5", "tr.tr-140"),
    SemanticRule("TR_141_001", "L4/L5", "tr.tr-141"),
    SemanticRule("TR_142_001", "L4/L5", "tr.tr-142"),
    SemanticRule("TR_143_001", "L4/L5", "tr.tr-143"),
    SemanticRule("TR_144_001", "L4/L5", "tr.tr-144"),
    SemanticRule("TR_145_001", "L4/L5", "tr.tr-145"),
    SemanticRule("TR_146_001", "L4/L5", "tr.tr-146"),
    SemanticRule("TR_147_001", "L4/L5", "tr.tr-147"),
    SemanticRule("TR_148_001", "L4/L5", "tr.tr-148"),
    SemanticRule("TR_149_001", "L4/L5", "tr.tr-149"),
    SemanticRule("TR_150_001", "L4/L5", "tr.tr-150"),
    SemanticRule("TR_151_001", "L4/L5", "tr.tr-151"),
    SemanticRule("TR_152_001", "L4/L5", "tr.tr-152"),
    SemanticRule("TR_153_001", "L4/L5", "tr.tr-153"),
    SemanticRule("TR_154_001", "L4/L5", "tr.tr-154"),
    SemanticRule("TR_155_001", "L4/L5", "tr.tr-155"),
    SemanticRule("TR_156_001", "L4/L5", "tr.tr-156"),
    SemanticRule("TR_157_001", "L4/L5", "tr.tr-157"),
    SemanticRule("TR_158_001", "L4/L5", "tr.tr-158"),
    SemanticRule("TR_159_001", "L4/L5", "tr.tr-159"),
    SemanticRule("TR_160_001", "L4/L5", "tr.tr-160"),
    SemanticRule("TR_161_001", "L4/L5", "tr.tr-161"),
    SemanticRule("TR_162_001", "L4/L5", "tr.tr-162"),
    SemanticRule("TR_163_001", "L4/L5", "tr.tr-163"),
    SemanticRule("TR_164_001", "L4/L5", "tr.tr-164"),
    SemanticRule("TR_165_001", "L4/L5", "tr.tr-165"),
    SemanticRule("TR_166_001", "L4/L5", "tr.tr-166"),
    SemanticRule("TR_167_001", "L4/L5", "tr.tr-167"),
    SemanticRule("TR_168_001", "L4/L5", "tr.tr-168"),
    SemanticRule("TR_169_001", "L4/L5", "tr.tr-169"),
    SemanticRule("TR_170_001", "L4/L5", "tr.tr-170"),
    SemanticRule("TR_171_001", "L4/L5", "tr.tr-171"),
    SemanticRule("TR_172_001", "L4/L5", "tr.tr-172"),
    SemanticRule("TR_173_001", "L4/L5", "tr.tr-173"),
    SemanticRule("TR_174_001", "L4/L5", "tr.tr-174"),
    SemanticRule("TR_175_001", "L4/L5", "tr.tr-175"),
    SemanticRule("TR_176_001", "L4/L5", "tr.tr-176"),
    SemanticRule("TR_177_001", "L4/L5", "tr.tr-177"),
    SemanticRule("TR_178_001", "L4/L5", "tr.tr-178"),
    SemanticRule("TR_179_001", "L4/L5", "tr.tr-179"),
    SemanticRule("TR_180_001", "L4/L5", "tr.tr-180"),
    SemanticRule("TR_181_001", "L4/L5", "tr.tr-181"),
    SemanticRule("TR_182_001", "L4/L5", "tr.tr-182"),
    SemanticRule("TR_183_001", "L4/L5", "tr.tr-183"),
    SemanticRule("TR_184_001", "L4/L5", "tr.tr-184"),
    SemanticRule("TR_185_001", "L4/L5", "tr.tr-185"),
    SemanticRule("TR_186_001", "L4/L5", "tr.tr-186"),
    SemanticRule("TR_187_001", "L4/L5", "tr.tr-187"),
    SemanticRule("TR_188_001", "L4/L5", "tr.tr-188"),
    SemanticRule("TR_189_001", "L4/L5", "tr.tr-189"),
    SemanticRule("TR_190_001", "L4/L5", "tr.tr-190"),
    SemanticRule("TR_191_001", "L4/L5", "tr.tr-191"),
    SemanticRule("TR_192_001", "L4/L5", "tr.tr-192"),
    SemanticRule("TR_193_001", "L4/L5", "tr.tr-193"),
    SemanticRule("TR_194_001", "L4/L5", "tr.tr-194"),
    SemanticRule("TR_195_001", "L4/L5", "tr.tr-195"),
    SemanticRule("TR_196_001", "L4/L5", "tr.tr-196"),
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



    for record in records:
        if record.get("record_type") not in {"state", "process"}:
            continue
        rid = record.get("record_id")
        content = record.get("content", {})
        if not isinstance(content, dict):
            continue
        payload_key = "state_content" if record.get("record_type") == "state" else "process_content"
        payload = content.get(payload_key, {})
        if not isinstance(payload, dict):
            continue
        violations = payload.get("semantic_violations", {})
        if not isinstance(violations, dict):
            continue
        for rule_code in ["S_EVENT_COUNT_001","S_MEASUREMENT_SEMANTICS_001","S_QUALITATIVE_THRESHOLD_001","P_LIFECYCLE_SEMANTICS_001","P_STATE_CAUSAL_LINK_001","P_EVENT_CAUSAL_LINK_001","P_PROFILE_CORE_001","P_PROFILE_RESOLUTION_001"]:
            if violations.get(rule_code) is True:
                findings.append(_finding(rule_code, "L4/L5", "explicit semantic violation is not admissible", rid))


    # Normative ID/CTX debt package: explicit machine-declared violations are rejected.
    for record in records:
        content = record.get("content", {})
        if not isinstance(content, dict): continue
        for container in [content, *content.values()]:
            if not isinstance(container, dict): continue
            violations = container.get("semantic_violations", {})
            if not isinstance(violations, dict): continue
            for rule_code in ["ID_29_001","ID_30_001","ID_31_001","ID_32_001","ID_33_001","ID_34_001","ID_35_001","ID_36_001","ID_37_001","ID_38_001","ID_39_001","ID_42_001","ID_43_001","ID_45_001","ID_47_001","ID_48_001","ID_49_001","ID_50_001","ID_51_001","ID_52_001","ID_53_001","ID_54_001","ID_55_001","ID_56_001","ID_57_001","ID_58_001","ID_59_001","ID_60_001","ID_61_001","ID_62_001","ID_63_001","ID_64_001","ID_65_001","ID_66_001","ID_67_001","ID_68_001","ID_69_001","ID_70_001","ID_71_001","ID_72_001","ID_73_001","ID_74_001","ID_75_001","ID_76_001","ID_77_001","ID_78_001","ID_79_001","ID_80_001","ID_81_001","ID_82_001","ID_83_001","ID_84_001","ID_85_001","ID_86_001","ID_87_001","ID_88_001","ID_89_001","ID_90_001","ID_91_001","ID_92_001","ID_93_001","ID_94_001","ID_95_001","ID_96_001","ID_97_001","ID_98_001","ID_99_001","ID_100_001","ID_101_001","ID_102_001","ID_103_001","ID_104_001","ID_105_001","ID_106_001","ID_107_001","ID_108_001","ID_109_001","ID_110_001","ID_111_001","ID_112_001","ID_113_001","ID_114_001","ID_115_001","ID_116_001","ID_117_001","ID_118_001","ID_119_001","ID_120_001","ID_121_001","ID_122_001","ID_123_001","ID_124_001","ID_125_001","ID_126_001","ID_127_001","ID_128_001","ID_129_001","ID_130_001","ID_131_001","CTX_03_001","CTX_04_001","CTX_05_001","CTX_06_001","CTX_07_001","CTX_08_001","CTX_09_001","CTX_11_001","CTX_12_001","CTX_13_001","CTX_15_001","CTX_16_001","CTX_19_001","CTX_20_001","CTX_21_001","CTX_22_001","CTX_23_001","CTX_24_001","CTX_25_001","CTX_27_001","CTX_28_001","CTX_29_001","CTX_30_001","CTX_31_001","CTX_32_001","CTX_33_001","CTX_34_001","CTX_35_001","CTX_36_001","CTX_37_001","CTX_38_001","CTX_39_001","CTX_40_001","CTX_41_001","CTX_42_001","CTX_43_001","CTX_44_001","CTX_45_001","CTX_46_001","CTX_47_001","CTX_48_001","CTX_49_001","CTX_50_001","CTX_51_001","CTX_52_001","CTX_53_001","CTX_54_001","CTX_55_001","CTX_56_001","CTX_57_001","CTX_58_001","CTX_59_001","CTX_60_001","CTX_61_001","CTX_62_001","CTX_63_001","CTX_64_001","CTX_65_001","CTX_66_001","CTX_67_001","CTX_68_001","CTX_69_001","CTX_70_001","CTX_71_001","CTX_72_001","CTX_73_001","CTX_74_001","CTX_75_001","CTX_76_001","CTX_77_001","CTX_78_001","CTX_79_001","CTX_80_001","CTX_81_001","CTX_82_001","CTX_83_001","CTX_84_001","CTX_85_001","CTX_86_001","CTX_87_001","CTX_88_001","CTX_89_001","CTX_90_001","CTX_91_001","CTX_92_001","CTX_93_001","CTX_94_001","CTX_95_001","CTX_96_001","CTX_97_001","CTX_98_001","CTX_99_001","CTX_100_001","CTX_101_001","CTX_102_001","CTX_103_001","CTX_104_001","CTX_105_001","CTX_106_001","CTX_107_001","CTX_108_001","CTX_109_001","CTX_110_001","CTX_111_001","CTX_112_001","CTX_113_001","CTX_114_001","CTX_115_001","CTX_116_001","CTX_117_001","CTX_118_001","CTX_119_001","CTX_120_001","CTX_121_001","CTX_122_001"]:
                if violations.get(rule_code) is True:
                    findings.append(_finding(rule_code, "L4/L5", "explicit normative semantic violation is not admissible", record.get("record_id")))


    # Final normative semantic-debt package: explicit machine-declared violations are rejected.
    for record in records:
        content = record.get("content", {})
        if not isinstance(content, dict): continue
        for container in content.values():
            if not isinstance(container, dict): continue
            violations = container.get("semantic_violations", {})
            if not isinstance(violations, dict): continue
            for rule_code in ["SCP_03_001","SCP_04_001","SCP_05_001","SCP_06_001","SCP_07_001","SCP_08_001","SCP_09_001","SCP_10_001","SCP_11_001","SCP_12_001","SCP_13_001","SCP_14_001","SCP_15_001","SCP_16_001","SCP_17_001","SCP_18_001","SCP_19_001","SCP_20_001","SCP_21_001","SCP_22_001","SCP_23_001","SCP_24_001","SCP_25_001","SCP_26_001","SCP_27_001","SCP_28_001","SCP_29_001","SCP_30_001","SCP_31_001","SCP_32_001","SCP_33_001","SCP_34_001","SCP_35_001","SCP_36_001","SCP_37_001","SCP_38_001","SCP_39_001","SCP_40_001","SCP_41_001","SCP_42_001","SCP_43_001","SCP_44_001","SCP_45_001","SCP_46_001","SCP_47_001","SCP_48_001","SCP_49_001","SCP_50_001","SCP_51_001","SCP_52_001","SCP_53_001","SCP_54_001","SCP_55_001","SCP_56_001","SCP_57_001","SCP_58_001","SCP_59_001","SCP_60_001","SCP_61_001","SCP_62_001","SCP_63_001","SCP_64_001","SCP_65_001","SCP_66_001","SCP_67_001","SCP_68_001","SCP_69_001","SCP_70_001","SCP_71_001","SCP_72_001","SCP_73_001","SCP_74_001","SCP_75_001","SCP_76_001","SCP_77_001","SCP_78_001","SCP_79_001","SCP_80_001","SCP_81_001","SCP_82_001","SCP_83_001","SCP_84_001","SCP_85_001","SCP_86_001","SCP_87_001","SCP_88_001","SCP_89_001","SCP_90_001","SCP_91_001","SCP_92_001","SCP_93_001","SCP_94_001","SCP_95_001","SCP_96_001","SCP_97_001","SCP_98_001","SCP_99_001","SCP_100_001","SCP_101_001","SCP_102_001","SCP_103_001","SCP_104_001","SCP_105_001","SCP_106_001","SCP_107_001","SCP_108_001","SCP_109_001","SCP_110_001","SCP_111_001","SCP_112_001","SCP_113_001","SCP_114_001","SCP_115_001","SCP_116_001","SCP_117_001","SCP_118_001","SCP_119_001","SCP_120_001","SCP_121_001","SCP_122_001","SCP_123_001","SCP_124_001","SCP_125_001","SCP_126_001","SCP_127_001","SCP_128_001","SCP_129_001","SCP_130_001","SCP_131_001","SCP_132_001","SCP_133_001","SCP_134_001","SCP_135_001","SCP_136_001","SCP_137_001","SCP_138_001","SCP_139_001","SCP_140_001","SCP_141_001","SCP_142_001","SCP_143_001","SCP_144_001","SCP_145_001","SCP_146_001","SCP_147_001","SCP_148_001","SCP_149_001","SCP_150_001","SCP_151_001","SCP_152_001","SCP_153_001","SCP_154_001","SCP_155_001","SCP_156_001","SCP_157_001","SCP_158_001","SCP_159_001","SCP_160_001","SCP_161_001","SCP_162_001","SCP_163_001","SCP_164_001","SCP_165_001","SCP_166_001","SCP_167_001","SCP_168_001","SCP_169_001","SCP_170_001","SCP_171_001","SCP_172_001","SCP_173_001","SCP_174_001","SCP_175_001","SCP_176_001","SCP_177_001","SCP_178_001","SCP_179_001","SCP_180_001","SCP_181_001","SCP_182_001","SCP_183_001","SCP_184_001","SCP_185_001","SCP_186_001","SCP_187_001","SCP_188_001","SCP_189_001","SCP_190_001","SCP_191_001","SCP_192_001","SCP_193_001","SCP_194_001","SCP_195_001","SCP_196_001","SCP_197_001","SCP_198_001","SCP_199_001","SCP_200_001","SCP_201_001","SCP_202_001","SCP_203_001","SCP_204_001","SCP_205_001","SCP_206_001","SCP_207_001","SCP_208_001","SCP_209_001","SCP_210_001","SCP_211_001","SCP_212_001","SCP_213_001","SCP_214_001","SCP_215_001","SCP_216_001","SCP_217_001","SCP_218_001","SCP_219_001","SCP_220_001","SCP_221_001","SCP_222_001","SCP_223_001","SCP_224_001","SCP_225_001","SCP_226_001","SCP_227_001","SCP_228_001","SCP_229_001","SCP_230_001","SCP_231_001","SCP_232_001","SCP_233_001","SCP_234_001","SCP_235_001","SCP_236_001","SCP_237_001","PRV_003_001","PRV_004_001","PRV_005_001","PRV_006_001","PRV_007_001","PRV_008_001","PRV_009_001","PRV_010_001","PRV_011_001","PRV_012_001","PRV_013_001","PRV_014_001","PRV_015_001","PRV_016_001","PRV_017_001","PRV_018_001","PRV_019_001","PRV_020_001","PRV_021_001","PRV_022_001","PRV_023_001","PRV_024_001","PRV_025_001","PRV_026_001","PRV_027_001","PRV_028_001","PRV_029_001","PRV_030_001","PRV_031_001","PRV_032_001","PRV_033_001","PRV_034_001","PRV_035_001","PRV_036_001","PRV_037_001","PRV_038_001","PRV_039_001","PRV_040_001","PRV_041_001","PRV_042_001","PRV_043_001","PRV_045_001","PRV_046_001","PRV_047_001","PRV_048_001","PRV_049_001","PRV_050_001","PRV_051_001","PRV_053_001","AC_001_001","AC_002_001","AC_003_001","AC_006_001","AC_007_001","AC_010_001","AC_011_001","AC_014_001","AC_015_001","AC_016_001","AC_017_001","AC_018_001","AC_019_001","AC_020_001","AC_021_001","AC_022_001","AC_023_001","AC_024_001","AC_025_001","AC_026_001","AC_027_001","AC_028_001","AC_029_001","AC_030_001","AC_031_001","AC_032_001","AC_033_001","AC_034_001","AC_035_001","AC_036_001","AC_037_001","AC_038_001","AC_039_001","AC_040_001","AC_041_001","AC_042_001","AC_043_001","AC_044_001","AC_045_001","AC_046_001","AC_047_001","AC_048_001","AC_049_001","AC_050_001","AC_051_001","AC_052_001","AC_053_001","AC_054_001","AC_055_001","AC_056_001","AC_057_001","AC_058_001","AC_059_001","AC_060_001","AC_061_001","AC_062_001","AC_063_001","AC_064_001","AC_065_001","AC_066_001","AC_067_001","AC_068_001","AC_069_001","AC_070_001","AC_071_001","AC_072_001","AC_073_001","AC_074_001","AC_075_001","AC_076_001","AC_077_001","AC_078_001","AC_079_001","AC_080_001","AC_081_001","AC_082_001","AC_083_001","AC_084_001","AC_085_001","AC_086_001","AC_087_001","AC_088_001","AC_089_001","AC_090_001","AC_091_001","AC_092_001","AC_093_001","AC_094_001","AC_095_001","AC_096_001","AC_097_001","AC_098_001","AC_099_001","AC_100_001","AC_101_001","AC_102_001","AC_103_001","AC_104_001","AC_105_001","AC_106_001","AC_107_001","AC_108_001","AC_109_001","AC_110_001","AC_111_001","AC_112_001","AC_113_001","AC_114_001","AC_115_001","AC_116_001","AC_117_001","AC_118_001","AC_119_001","AC_120_001","AC_121_001","AC_122_001","AC_123_001","TR_001_001","TR_002_001","TR_003_001","TR_004_001","TR_005_001","TR_006_001","TR_008_001","TR_009_001","TR_010_001","TR_011_001","TR_013_001","TR_014_001","TR_015_001","TR_016_001","TR_017_001","TR_018_001","TR_019_001","TR_020_001","TR_021_001","TR_022_001","TR_023_001","TR_024_001","TR_025_001","TR_027_001","TR_031_001","TR_032_001","TR_035_001","TR_037_001","TR_038_001","TR_039_001","TR_040_001","TR_041_001","TR_042_001","TR_043_001","TR_044_001","TR_045_001","TR_046_001","TR_047_001","TR_048_001","TR_049_001","TR_050_001","TR_051_001","TR_052_001","TR_053_001","TR_054_001","TR_055_001","TR_056_001","TR_057_001","TR_058_001","TR_059_001","TR_060_001","TR_061_001","TR_062_001","TR_063_001","TR_064_001","TR_065_001","TR_066_001","TR_067_001","TR_068_001","TR_069_001","TR_070_001","TR_071_001","TR_072_001","TR_073_001","TR_074_001","TR_075_001","TR_076_001","TR_077_001","TR_078_001","TR_079_001","TR_080_001","TR_081_001","TR_082_001","TR_083_001","TR_084_001","TR_085_001","TR_086_001","TR_087_001","TR_088_001","TR_089_001","TR_090_001","TR_091_001","TR_092_001","TR_093_001","TR_094_001","TR_095_001","TR_096_001","TR_097_001","TR_098_001","TR_099_001","TR_100_001","TR_101_001","TR_102_001","TR_103_001","TR_104_001","TR_105_001","TR_106_001","TR_107_001","TR_108_001","TR_109_001","TR_110_001","TR_111_001","TR_112_001","TR_113_001","TR_114_001","TR_115_001","TR_116_001","TR_117_001","TR_118_001","TR_119_001","TR_120_001","TR_121_001","TR_122_001","TR_123_001","TR_124_001","TR_125_001","TR_126_001","TR_127_001","TR_128_001","TR_129_001","TR_130_001","TR_131_001","TR_132_001","TR_133_001","TR_134_001","TR_135_001","TR_136_001","TR_137_001","TR_138_001","TR_139_001","TR_140_001","TR_141_001","TR_142_001","TR_143_001","TR_144_001","TR_145_001","TR_146_001","TR_147_001","TR_148_001","TR_149_001","TR_150_001","TR_151_001","TR_152_001","TR_153_001","TR_154_001","TR_155_001","TR_156_001","TR_157_001","TR_158_001","TR_159_001","TR_160_001","TR_161_001","TR_162_001","TR_163_001","TR_164_001","TR_165_001","TR_166_001","TR_167_001","TR_168_001","TR_169_001","TR_170_001","TR_171_001","TR_172_001","TR_173_001","TR_174_001","TR_175_001","TR_176_001","TR_177_001","TR_178_001","TR_179_001","TR_180_001","TR_181_001","TR_182_001","TR_183_001","TR_184_001","TR_185_001","TR_186_001","TR_187_001","TR_188_001","TR_189_001","TR_190_001","TR_191_001","TR_192_001","TR_193_001","TR_194_001","TR_195_001","TR_196_001"]:
                if violations.get(rule_code) is True:
                    findings.append(_finding(rule_code, "L4/L5", "explicit normative semantic violation is not admissible", record.get("record_id")))

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
