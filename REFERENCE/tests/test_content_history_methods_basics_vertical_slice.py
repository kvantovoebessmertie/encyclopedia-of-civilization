from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "history-methods-basics" / "records"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def _records() -> list[dict]:
    return [json.loads(path.read_text(encoding="utf-8")) for path in SLICE.glob("*.json")]


def test_history_methods_basics_slice_is_complete():
    records = _records()
    assert len(records) == 10
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {
        record["record_type"] for record in records
    }
    sources = {record["record_id"] for record in records if record["record_type"] == "source"}
    assert len(sources) == 2
    for claim in [record for record in records if record["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(
            evidence["content"]["claim_ref"]["record_id"] == claim["record_id"]
            and evidence["content"]["source_ref"]["record_id"] in sources
            for evidence in records
            if evidence["record_type"] == "evidence_use"
        )


def test_history_methods_provenance_evidence_use_has_nara_pinpoint():
    records = {record["record_id"]: record for record in _records()}
    claim = records["CLM-HISTORY_METHODS_BASICS-B"]
    evidence = records["EU-HISTORY_METHODS_BASICS-B"]
    source = records["SRC-HISTORY-METHODS-NARA-DOCUMENT-ANALYSIS"]

    assert evidence["record_version"] == "2"
    assert evidence["content"]["claim_ref"] == {
        "record_id": claim["record_id"],
        "version": claim["record_version"],
    }
    assert evidence["content"]["source_ref"] == {
        "record_id": source["record_id"],
        "version": source["record_version"],
    }
    assert source["content"]["external_ref"]["uri"] == (
        "https://www.archives.gov/education/lessons/worksheets/"
        "analyze-a-written-document-intermediate"
    )
    description = evidence["content"]["material"]["description"]
    assert "Observe its parts" in description
    assert "Try to make sense of it" in description
    assert "Use it as historical evidence" in description
    assert "does not establish that context alone determines reliability" in description

    validator = Validator(SCHEMA)
    for record in (claim, evidence, source):
        result = validator.validate(record)
        assert result.passed, (
            record["record_id"],
            [(finding.code, finding.message) for finding in result.findings],
        )
