from __future__ import annotations

import copy
import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.human_view import build_human_view
from encyclopedia_reference.semantic_rules import registry, validate_semantic_dataset
from encyclopedia_reference.storage import FileStorage
from encyclopedia_reference.query import QueryInterface
from encyclopedia_reference.validator import Validator

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"
EXPECTED_TYPES = {
    "record", "claim", "source", "evidence_use", "assessment", "inference",
    "decision", "action", "event", "result", "state", "process", "relation",
    "identity", "context", "scope", "provenance", "authorship_contribution",
    "trust_reputation",
}


def _records():
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(CONTENT.glob("*/records/*.json"))
    ]


def test_integrated_19_type_248_slice_pipeline(tmp_path):
    records = _records()
    assert len(records) == 2637
    assert {r["record_type"] for r in records} == EXPECTED_TYPES

    validator = Validator(SCHEMA)
    for record in records:
        result = validator.validate(record)
        assert result.passed, (record["record_id"], [(f.code, f.message) for f in result.findings])

    assert validate_semantic_dataset(records) == []

    storage = FileStorage(tmp_path / "storage")
    for record in records:
        storage.create(record)
    query = QueryInterface(storage)

    original = copy.deepcopy(records)
    for record in records:
        view = build_human_view(query, record["record_id"], str(record["record_version"]), mode="UNDERSTAND")
        assert view["status"] == "ok"
        assert "traceability" in view
        assert "unknown" in view
        assert set(view["safety"]) >= {
            "historical_action_is_not_current_instruction",
            "source_is_not_truth",
            "inference_is_not_observation",
            "temporal_sequence_is_not_causality",
        }

    assert records == original

    report = build_content_package(
        records,
        package_dir=tmp_path / "package",
        schema_path=SCHEMA,
        package_id="integrated-conformance-2637-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["recovered_record_count"] == 2637
    assert report["expected_record_count"] == 2637
    assert report["findings"] == []
    assert report["publication_present"] is True
    assert report["offline_schema_present"] is True


def test_integrated_registry_is_closed_and_noninferential():
    rules = registry()
    assert len(rules) == 1191
    assert len(set(rules)) == 1191
    statuses = {item["status"] for item in rules.values()}
    assert statuses <= {"ENFORCED", "MAPPED"}
    assert all(item["owner"] in {"L4/L5", "L4", "L5"} for item in rules.values())


def test_semantic_violation_contract_rejects_explicit_declaration():
    records = [{
        "record_id": "ADVERSARIAL-SEMANTIC-001",
        "record_type": "record",
        "record_version": "1",
        "type_version": "1.0",
        "publication_status": "draft",
        "completion_status": "complete",
        "schema": "record/0.1",
        "provenance": {"method": "adversarial-test"},
        "content": {
            "semantic_violations": {
                "S_01_001": True,
                "P_01_001": True,
                "CTX_01_001": True,
                "SCP_01_001": True,
                "PRV_001_001": True,
                "AC_004_001": True,
                "TR_007_001": True,
            }
        },
    }]
    findings = validate_semantic_dataset(records)
    assert {f.code for f in findings} >= {
        "S_01_001", "P_01_001", "CTX_01_001", "SCP_01_001",
        "PRV_001_001", "AC_004_001", "TR_007_001",
    }
