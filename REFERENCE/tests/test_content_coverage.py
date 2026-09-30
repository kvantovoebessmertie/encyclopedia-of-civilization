from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
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
    records = []
    for path in sorted(CONTENT.glob("*/records/*.json")):
        records.append(json.loads(path.read_text(encoding="utf-8")))
    return records


def test_full_content_type_coverage_is_complete():
    records = _records()
    validator = Validator(SCHEMA)
    assert records
    assert all(validator.validate(record).passed for record in records)
    assert validate_semantic_dataset(records) == []

    counts = Counter(r["record_type"] for r in records)
    assert set(counts) == EXPECTED_TYPES
    assert all(counts[t] >= 1 for t in EXPECTED_TYPES)

    expected_total = 73
    assert len(records) == expected_total

    manifest = json.loads((ROOT / "RELEASE" / "CONTENT-COVERAGE.json").read_text(encoding="utf-8"))
    assert manifest["total_records"] == len(records)
    assert manifest["types_total"] == len(EXPECTED_TYPES)
    assert manifest["types_directly_covered"] == len(EXPECTED_TYPES)
    assert manifest["types_without_direct_content_coverage"] == []
    assert {t: manifest["types"][t]["count"] for t in EXPECTED_TYPES} == dict(counts)


def test_cross_cutting_types_have_direct_content_records():
    records = _records()
    by_type = {t: [r for r in records if r["record_type"] == t] for t in EXPECTED_TYPES}
    assert by_type["provenance"]
    assert by_type["authorship_contribution"]
    assert by_type["trust_reputation"]

    trust = by_type["trust_reputation"][0]["content"]
    assert trust["value"]["status"] == "not_assessed"
    assert "truth" not in trust["value"]


def test_full_content_corpus_package_is_reproducible(tmp_path):
    records = _records()
    report = build_content_package(
        records,
        package_dir=tmp_path / "package",
        schema_path=SCHEMA,
        package_id="content-full-coverage-v1",
    )
    assert report["integrity_and_validation"] == "PASS"
    assert report["findings"] == []
