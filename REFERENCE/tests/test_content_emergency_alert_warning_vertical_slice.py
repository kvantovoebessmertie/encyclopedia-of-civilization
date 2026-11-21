from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "emergency-alert-warning" / "records"


def test_emergency_alert_warning_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) == 10
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {
        r["record_type"] for r in records
    }
    by_id = {r["record_id"]: r for r in records}
    assert {
        "CLM-IPAWS-ALERT-CONTENT",
        "CLM-IPAWS-ALERT-ELEMENTS",
    } <= by_id.keys()

    content = by_id["EU-IPAWS-ALERT-CONTENT"]
    assert content["content"]["claim_ref"] == {
        "record_id": "CLM-IPAWS-ALERT-CONTENT", "version": "1"
    }
    assert content["content"]["source_ref"] == {
        "record_id": "SRC-PUBLIC-ALERT-GUIDANCE", "version": "1"
    }
    assert content["content"]["material"]["locator"] == (
        "FEMA IPAWS TIP 44, §II.A–B, printed p. 1"
    )
    assert "incident" in content["content"]["material"]["description"].lower()
    assert "protective action" in content["content"]["material"]["description"].lower()

    elements = by_id["EU-IPAWS-ALERT-ELEMENTS"]
    assert elements["content"]["claim_ref"] == {
        "record_id": "CLM-IPAWS-ALERT-ELEMENTS", "version": "1"
    }
    assert elements["content"]["source_ref"] == {
        "record_id": "SRC-PUBLIC-ALERT-GUIDANCE", "version": "1"
    }
    assert elements["content"]["material"]["locator"] == (
        "FEMA IPAWS TIP 44, §II.B, printed p. 1"
    )
    description = elements["content"]["material"]["description"].lower()
    for element in (
        "trusted sender",
        "event description",
        "incident location",
        "protective action",
        "guidance/expiration time",
    ):
        assert element in description
