from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.semantic_rules import validate_semantic_dataset
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
CONTENT = (
    ROOT
    / "CONTENT"
    / "vertical-slices"
    / "source-provenance-authorship-trust"
    / "records"
)
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records() -> list[dict]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(CONTENT.glob("*.json"))
    ]


def test_source_provenance_authorship_trust_slice_records_validate():
    validator = Validator(SCHEMA)
    records = _records()

    assert len(records) == 7
    assert {record["record_type"] for record in records} == {
        "source",
        "record",
        "claim",
        "evidence_use",
        "provenance",
        "authorship_contribution",
        "trust_reputation",
    }
    for record in records:
        result = validator.validate(record)
        assert result.passed, (
            record["record_id"],
            [(f.code, f.message) for f in result.findings],
        )


def test_source_provenance_authorship_trust_semantic_dataset_is_clean():
    findings = validate_semantic_dataset(_records())
    assert findings == []


def test_trust_signal_does_not_claim_truth_or_assessed_trust():
    trust = next(
        record for record in _records() if record["record_type"] == "trust_reputation"
    )
    value = trust["content"]["value"]

    assert value["status"] == "not_assessed"
    assert "truth" not in value
