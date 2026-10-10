from __future__ import annotations

import re

from REFERENCE.m13_claim_audit_inventory import RISK_TERMS, risk_screen_text


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
