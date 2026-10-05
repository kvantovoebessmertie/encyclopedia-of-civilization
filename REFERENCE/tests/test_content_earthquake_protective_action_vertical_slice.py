from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices" / "earthquake-protective-action" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]


def test_earthquake_event_decision_action_result_slice_validates():
    records = _records()
    assert len(records) == 12
    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (
            record["record_id"],
            [(f.code, f.message) for f in result.findings],
        )
    assert validate_semantic_dataset(records) == []

    by_id = {r["record_id"]: r for r in records}
    event = by_id["EVT-EARTHQUAKE-SHAKING"]
    decision = by_id["DEC-EARTHQUAKE-PROTECT"]
    action = by_id["ACT-EARTHQUAKE-DROP-COVER-HOLD"]
    result = by_id["RES-EARTHQUAKE-PROTECTIVE"]

    assert event["record_type"] == "event"
    assert decision["record_type"] == "decision"
    assert action["content"]["decision_ref"]["record_id"] == decision["record_id"]
    assert action["content"]["context_ref"]["record_id"] == event["content"]["context_ref"]["record_id"]
    assert {r["record_id"] for r in result["content"]["reference_frame"]["refs"]} == {
        event["record_id"], decision["record_id"], action["record_id"]
    }
    assert result["content"]["causal_attribution"]["mode"] == "not_attributed"


def test_earthquake_package_preserves_epistemic_layers(tmp_path):
    report = build_content_package(
        _records(),
        package_dir=tmp_path / "package",
        schema_path=SCHEMA,
        package_id="earthquake-protective-action-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["findings"] == []
    publication = json.loads((tmp_path / "package" / "publication.json").read_text(encoding="utf-8"))
    assert publication["citations_preserved"] is True
    assert any(e["record_type"] == "claim" and e["evidence"] for e in publication["entries"])
