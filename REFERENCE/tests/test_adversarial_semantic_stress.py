from __future__ import annotations

from encyclopedia_reference.semantic_rules import validate_semantic_dataset


def base(record_id: str, record_type: str, content: dict, **extra) -> dict:
    return {
        "record_id": record_id,
        "record_type": record_type,
        "record_version": "1",
        "type_version": "1.0",
        "publication_status": "draft",
        "completion_status": "complete",
        "schema": "record/0.1",
        "provenance": {"method": "adversarial-stress-test"},
        "content": content,
        **extra,
    }


def codes(findings):
    return {f.code for f in findings}


def test_adversarial_identity_context_provenance_combo():
    records = [
        base("ID1", "identity", {
            "identity": {"assertion": True, "resolved": True}
        }),
        base("C1", "context", {
            "context_content": {
                "assumption": True,
                "epistemic_status": "observed",
                "transferability": "transferable",
                "conflict": True,
            }
        }),
        base("P1", "source", {
            "note": "cycle root"
        }, provenance={"created_from": [{"record_id": "P2", "version": "1"}]}),
        base("P2", "source", {
            "note": "cycle child"
        }, provenance={"created_from": [{"record_id": "P1", "version": "1"}]}),
    ]
    found = codes(validate_semantic_dataset(records))
    assert "ID_RESOLUTION_001" in found
    assert "CTX_ASSUMPTION_001" in found
    assert "CTX_TRANSFER_CONFLICT_001" in found
    assert "PROV_CYCLE_001" in found


def test_adversarial_trust_transfer_and_independence_combo():
    records = [
        base("T1", "trust_reputation", {
            "assessment_type": "trust",
            "transferability": "universal",
            "independence_status": "independent",
            "common_root_ref": {"record_id": "ROOT", "version": "1"},
        }),
        base("T2", "trust_reputation", {
            "assessment_type": "trust",
            "historical": True,
        }),
    ]
    found = codes(validate_semantic_dataset(records))
    assert "TRUST_TRANSFER_001" in found
    assert "TRUST_INDEPENDENCE_001" in found
    assert "TRUST_HISTORY_001" in found


def test_adversarial_scope_generalization_and_fidelity_combo():
    record = base("S1", "scope", {
        "scope_content": {
            "sample_to_population": True,
            "fidelity": {"status": "lost"},
            "historical": True,
            "operation": "mapping",
        }
    })
    found = codes(validate_semantic_dataset([record]))
    assert "SCOPE_SAMPLE_POP_001" in found
    assert "SCOPE_FIDELITY_001" in found
    assert "SCOPE_HISTORY_001" in found
    assert "SCOPE_ALGEBRA_001" in found


def test_adversarial_authorship_and_tool_use_combo():
    records = [
        base("A1", "authorship_contribution", {
            "tool_use": True,
            "contribution": "author",
            "attribution_status": "disputed",
            "confirmed": True,
            "historical_attribution": True,
        })
    ]
    found = codes(validate_semantic_dataset(records))
    assert "AUTH_ROLE_001" in found
    assert "AUTH_CONFLICT_001" in found
    assert "AUTH_HISTORY_001" in found


def test_adversarial_relation_structure_is_not_semantically_inferred():
    refs = [
        {"record_id": "A", "version": "1"},
        {"record_id": "B", "version": "1"},
        {"record_id": "C", "version": "1"},
    ]
    records = [
        base("R1", "relation", {
            "relation": {
                "relation_type": "supports",
                "participants": refs,
                "roles": ["subject", "object", "context"],
                "direction": "directed",
            }
        }),
        base("R2", "relation", {
            "relation": {
                "relation_type": "supports",
                "participants": refs[:2],
                "direction": "unknown",
            }
        }, valid_time={"start": "2025-01-01T00:00:00Z", "end": "2025-12-31T00:00:00Z"}),
        base("R3", "relation", {
            "relation": {
                "relation_type": "supports",
                "participants": refs[:2],
                "direction": "unknown",
            }
        }, valid_time={"start": "2026-01-01T00:00:00Z", "end": "2026-12-31T00:00:00Z"}),
    ]
    found = codes(validate_semantic_dataset(records))
    assert not found.intersection({
        "RL_03_001", "RL_24_001", "RL_25_001", "RL_29_001",
        "RL_39_001", "RL_45_001", "RL_49_001",
    })
    assert records[0]["content"]["relation"]["participants"] == refs
    assert records[1]["content"]["relation"]["participants"] == refs[:2]


def test_adversarial_context_overlap_detects_only_real_conflict():
    records = [
        base("C1", "context", {
            "context_content": {"temperature": 10, "precedence": 1},
            "target_ref": {"record_id": "T", "version": "1"},
        }, valid_time={"start": "2026-01-01T00:00:00Z", "end": "2026-06-30T00:00:00Z"}),
        base("C2", "context", {
            "context_content": {"temperature": 20, "precedence": 1},
            "target_ref": {"record_id": "T", "version": "1"},
        }, valid_time={"start": "2026-06-01T00:00:00Z", "end": "2026-12-31T00:00:00Z"}),
        base("C3", "context", {
            "context_content": {"temperature": 99, "precedence": 1},
            "target_ref": {"record_id": "OTHER", "version": "1"},
        }, valid_time={"start": "2026-01-01T00:00:00Z", "end": "2026-12-31T00:00:00Z"}),
    ]
    found = codes(validate_semantic_dataset(records))
    assert "CTX_CONFLICT_001" in found


def test_adversarial_explicit_debt_contract_cannot_be_bypassed():
    debt_codes = [
        "S_01_001", "P_01_001", "ID_41_001", "CTX_01_001",
        "SCP_01_001", "PRV_001_001", "AC_004_001", "TR_007_001",
    ]
    records = [
        base("D-" + code, "record", {
            "semantic_violations": {code: True},
            "decoy": {"claim": "false but structurally plausible"},
        })
        for code in debt_codes
    ]
    found = codes(validate_semantic_dataset(records))
    assert set(debt_codes) <= found


def test_adversarial_duplicate_identity_does_not_create_new_truth():
    records = [
        base("I1", "identity", {
            "identity": {
                "similarity": 0.99,
                "identity_basis": "similarity",
                "resolved": True,
            }
        }),
        base("I2", "identity", {
            "identity": {
                "similarity_only": True,
                "resolved": True,
            }
        }),
    ]
    found = codes(validate_semantic_dataset(records))
    assert "ID_RESOLUTION_001" in found
    assert len(records) == 2


def test_adversarial_non_applicable_shapes_remain_non_failing():
    records = [
        base("N1", "record", {"note": "no semantic domain payload"}),
        base("N2", "record", {"note": "another ordinary record"}),
    ]
    found = codes(validate_semantic_dataset(records))
    assert not found
