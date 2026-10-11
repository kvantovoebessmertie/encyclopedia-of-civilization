from __future__ import annotations

import re

from REFERENCE.m13_claim_audit_inventory import RISK_TERMS, editorial_type_flags, risk_screen_text


def test_risk_screen_has_explicit_nuclear_radiological_domain():
    text = "Радиоактивное загрязнение, fallout and radiological emergency"
    assert re.search(RISK_TERMS["nuclear_radiological"], text, re.IGNORECASE)


def test_risk_screen_has_explicit_communications_continuity_domain():
    text = "При отключении интернета используйте emergency radio and public alert channels"
    assert re.search(RISK_TERMS["communications_information_continuity"], text, re.IGNORECASE)


def test_risk_screen_has_explicit_shelter_and_transport_domains():
    assert re.search(RISK_TERMS["shelter_evacuation_access"], "shelter and evacuation", re.IGNORECASE)
    assert re.search(RISK_TERMS["transport_access"], "road access and transport", re.IGNORECASE)


def test_risk_screen_includes_linked_context_scope_and_source_identity():
    claim = {
        "context": {"record_id": "CTX-1"},
        "scope": {"record_id": "SCP-1"},
    }
    content = {}
    records_by_id = {
        "CTX-1": [{"record": {"record_type": "context", "content": {"condition": "radioactive contamination"}}}],
        "SCP-1": [{"record": {"record_type": "scope", "content": {"boundary": "emergency radio"}}}],
    }
    combined = risk_screen_text(
        claim,
        content,
        "basic statement",
        ["evidence description"],
        [{"source_identity": "Radiological emergency guidance"}],
        records_by_id,
    )
    assert "radioactive contamination" in combined
    assert "emergency radio" in combined
    assert "Radiological emergency guidance" in combined


def test_risk_screen_matches_standalone_russian_electricity_token():
    assert re.search(RISK_TERMS["electricity_energy"], "Отключился ток в районе", re.IGNORECASE)


def test_risk_screen_includes_context_scope_records_pointing_to_claim():
    claim = {"record_id": "CLM-REALISTIC"}
    records_by_id = {
        "CLM-REALISTIC": [{"record": {"record_type": "claim", "record_id": "CLM-REALISTIC"}}],
        "CTX-REALISTIC": [{"record": {
            "record_type": "context",
            "record_id": "CTX-REALISTIC",
            "content": {"context_content": "radioactive contamination", "target_ref": {"record_id": "CLM-REALISTIC"}},
        }}],
        "SCP-REALISTIC": [{"record": {
            "record_type": "scope",
            "record_id": "SCP-REALISTIC",
            "content": {"scope_content": "emergency radio access", "target_ref": {"record_id": "CLM-REALISTIC"}},
        }}],
    }
    combined = risk_screen_text(claim, {}, "basic statement", [], [], records_by_id)
    assert "radioactive contamination" in combined
    assert "emergency radio access" in combined


def test_editorial_slice_purpose_claim_is_flagged_for_type_review():
    statement = "Срез anthropology-basics вводит базовые понятия и отношения, необходимые для ориентации в предметной области."
    assert "slice_purpose_claim_type_review" in editorial_type_flags(statement)


def test_templated_cross_cutting_methodology_claim_is_flagged_for_type_review():
    statement = "Интерпретация сведений по anthropology-basics зависит от источника, контекста и границ применимости утверждения."
    assert "cross_cutting_methodology_claim_type_review" in editorial_type_flags(statement)


def test_domain_specific_noise_recommendation_is_not_misclassified_as_generic_template():
    statement = "Рекомендации по шуму зависят от источника, времени воздействия, контекста и применимой нормативной системы."
    assert editorial_type_flags(statement) == []
