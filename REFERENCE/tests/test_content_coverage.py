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
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(CONTENT.glob("*/records/*.json"))]

def test_full_content_type_coverage_is_complete():
    records = _records()
    validator = Validator(SCHEMA)
    assert records
    for record in records:
        result = validator.validate(record)
        assert result.passed, (
            record["record_id"],
            [(f.code, f.message) for f in result.findings],
        )
    assert validate_semantic_dataset(records) == []
    counts = Counter(r["record_type"] for r in records)
    assert set(counts) == EXPECTED_TYPES
    assert all(counts[t] >= 1 for t in EXPECTED_TYPES)
    manifest = json.loads((ROOT / "RELEASE" / "CONTENT-COVERAGE.json").read_text(encoding="utf-8"))
    expected_total = manifest["total_records"]
    assert len(records) == expected_total
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
    report = build_content_package(records, package_dir=tmp_path / "package", schema_path=SCHEMA, package_id="content-full-coverage-v1")
    assert report["integrity_and_validation"] == "PASS"
    assert report["findings"] == []

def test_corpus_documentation_registers_every_slice():
    records = _records()
    slugs = {path.parent.parent.name for path in CONTENT.glob("*/records/*.json")}
    content_readme = (ROOT / "CONTENT" / "README.md").read_text(encoding="utf-8")
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    for slug in slugs:
        assert f"vertical-slices/{slug}" in content_readme, slug
        assert f"vertical-slices/{slug}" in roadmap, slug
    assert len(slugs) == json.loads((ROOT / "RELEASE" / "CONTENT-COVERAGE.json").read_text(encoding="utf-8"))["vertical_slices"]

def test_all_dedicated_vertical_slice_regressions_are_python_tests():
    test_dir = ROOT / "REFERENCE" / "tests"
    tests = sorted(test_dir.glob("test_content_*_vertical_slice.py"))
    assert len(tests) == json.loads((ROOT / "RELEASE" / "CONTENT-COVERAGE.json").read_text(encoding="utf-8"))["vertical_slices"]
    for path in tests:
        text = path.read_text(encoding="utf-8")
        assert "def test_" in text, path
        assert not text.lstrip().startswith(("{", "[")), path


def test_relation_context_frames_are_target_specific():
    records = _records()
    by_identity = {
        (record["record_id"], str(record["record_version"])): record
        for record in records
    }
    relations = [record for record in records if record["record_type"] == "relation"]
    relation_contexts = [
        record for record in records
        if record["record_id"].startswith("CTX-REL-")
        or record["record_id"].startswith("CTX-REL_")
    ]

    assert len(relations) == 63
    assert len(relation_contexts) == 61

    expected_condition = (
        "связь между участниками фиксируется только в пределах явно указанного "
        "типа Relation и не заменяет исходные Claim, Scope или Evidence Use"
    )
    shared_context_users = []

    for relation in relations:
        relation_id = relation["record_id"]
        frame = relation["content"]["frame_ref"]

        if relation_id == "REL-CONTAINER-WATER-STORAGE":
            assert frame == {
                "record_id": "CTX-WATER-STORAGE-EMERGENCY",
                "version": "1",
            }
            continue

        if relation_id == "REL-CROSS-WATER-CHEMICAL":
            assert frame == {
                "record_id": "CTX-CROSS-SLICE-LINKAGE",
                "version": "1",
            }
            shared_context_users.append(relation_id)
            shared = by_identity[("CTX-CROSS-SLICE-LINKAGE", "1")]
            assert shared["content"]["target_ref"] == {
                "record_id": relation_id,
                "version": str(relation["record_version"]),
            }
            continue

        context_id = f"CTX-{relation_id}"
        assert frame["record_id"] == context_id
        context = by_identity[(context_id, str(frame["version"]))]
        assert context["content"]["target_ref"] == {
            "record_id": relation_id,
            "version": str(relation["record_version"]),
        }
        # Context and Relation have independent provenance. The Context's target_ref
        # is the target-specificity invariant; their created_from lists need not match.
        assert context["content"]["context_content"]["condition"] == expected_condition

    assert shared_context_users == ["REL-CROSS-WATER-CHEMICAL"]
