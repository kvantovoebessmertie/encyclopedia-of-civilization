from __future__ import annotations

import copy
from pathlib import Path

import pytest

from encyclopedia_reference.pipeline import ReferencePipeline
from encyclopedia_reference.publication import build_publication
from encyclopedia_reference.query import QueryInterface
from encyclopedia_reference.recovery import make_package, recover_package
from encyclopedia_reference.storage import (
    ConcurrentUpdateError,
    FileStorage,
    StorageError,
)
from encyclopedia_reference.system import ReferenceSystem
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def base(record_id: str, record_type: str, content: dict) -> dict:
    return {
        "record_id": record_id,
        "record_type": record_type,
        "record_version": "1",
        "type_version": "1.0",
        "publication_status": "draft",
        "completion_status": "complete",
        "schema": "record/0.1",
        "provenance": {"method": "test"},
        "content": content,
    }


@pytest.fixture
def validator():
    return Validator(SCHEMA)


@pytest.mark.parametrize(
    ("record_type", "content"),
    [
        ("record", {"note": "тест"}),
        ("claim", {"statement": "пример", "claim_type": "descriptive"}),
        ("source", {"source_identity": "SRC-ID-1", "representation": "text"}),
        (
            "evidence_use",
            {
                "claim_ref": {"record_id": "CLM-1", "version": "1"},
                "source_ref": {"record_id": "SRC-1", "version": "1"},
                "material": {"description": "материал"},
                "evidence_role": "supports",
            },
        ),
        (
            "assessment",
            {
                "target": {"record_id": "CLM-1", "version": "1"},
                "aspect": "пример",
                "result": {"value": 1},
            },
        ),
        (
            "inference",
            {
                "conclusion": {"statement": "C"},
                "premises": [{"record_id": "CLM-1", "version": "1"}],
                "attribution": {"mode": "known"},
            },
        ),
        (
            "decision",
            {
                "decision_result": {"choice": "A"},
                "decision_maker": {"record_id": "AG-1", "version": "1"},
            },
        ),
        (
            "action",
            {
                "action_content": {"operation": "A"},
                "execution": "completed",
            },
        ),
        (
            "event",
            {
                "event_content": {"description": "E"},
                "event_status": "observed",
            },
        ),
        (
            "result",
            {
                "result_content": {"value": 10},
                "reference_frame": {"refs": [{"record_id": "ACT-1", "version": "1"}]},
                "origin": ["measured"],
            },
        ),
        (
            "state",
            {"state_content": {"value": "active"}, "subject_ref": {"record_id": "OBJ-1", "version": "1"}},
        ),
        (
            "process",
            {"process_content": {"name": "P"}, "participants": [{"record_id": "OBJ-1", "version": "1"}]},
        ),
        (
            "relation",
            {"relation_type": "related_to", "participants": [{"record_id": "A", "version": "1"}, {"record_id": "B", "version": "1"}]},
        ),
        (
            "identity",
            {"identity_level": "referent", "targets": [{"record_id": "A", "version": "1"}, {"record_id": "B", "version": "1"}], "criterion": "same referent"},
        ),
        (
            "context",
            {"context_content": {"condition": "C"}, "target_ref": {"record_id": "A", "version": "1"}, "epistemic_status": "known"},
        ),
        (
            "scope",
            {"target_ref": {"record_id": "A", "version": "1"}, "scope_content": {"population": "P"}},
        ),
        (
            "provenance",
            {"target_ref": {"record_id": "A", "version": "1"}, "relation": "derived_from", "inputs": [{"record_id": "B", "version": "1"}]},
        ),
        (
            "authorship_contribution",
            {"target_ref": {"record_id": "A", "version": "1"}, "contributor_ref": {"record_id": "PERSON-1", "version": "1"}, "contribution": "author"},
        ),
        (
            "trust_reputation",
            {"target_ref": {"record_id": "A", "version": "1"}, "assessment_type": "trust", "basis_refs": [{"record_id": "B", "version": "1"}]},
        ),
    ],
)
def test_vertical_slice_types_pass(validator, record_type, content):
    record = base(f"{record_type}-1", record_type, content)
    if record_type == "trust_reputation":
        record["type_version"] = "1.1"
        record["content"]["subject_ref"] = {"record_id": "SUBJ-1", "version": "1"}
        record["content"]["goal_ref"] = {"record_id": "GOAL-1", "version": "1"}
    result = validator.validate(record)
    assert result.status == "pass"


def test_invalid_record_fails(validator):
    result = validator.validate(base("CLM-2", "claim", {"statement": ""}))
    assert result.status == "fail"


def test_incompatible_type_version_fails(validator):
    record = base("CLM-V", "claim", {"statement": "пример", "claim_type": "descriptive"})
    record["type_version"] = "9.9"
    result = validator.validate(record)
    assert any(f.code == "VAL-L2-INCOMPATIBLE-TYPE-VERSION" for f in result.findings)


def test_published_does_not_mean_true(validator):
    record = base(
        "CLM-3",
        "claim",
        {
            "statement": "пример",
            "claim_type": "descriptive",
            "truth": True,
        },
    )
    record["publication_status"] = "published"
    result = validator.validate(record)
    assert any(f.code == "VAL-L4-PUBLICATION-TRUTH" for f in result.findings)


def test_historical_versions_are_preserved(tmp_path):
    storage = FileStorage(tmp_path)
    v1 = base("CLM-H", "claim", {"statement": "v1", "claim_type": "descriptive"})
    v2 = copy.deepcopy(v1)
    v2["record_version"] = "2"
    v2["content"]["statement"] = "v2"

    storage.create(v1)
    storage.update(v2, expected_version="1")

    assert storage.list_versions("CLM-H") == ["1", "2"]
    assert storage.read_version("CLM-H", "1")["content"]["statement"] == "v1"


def test_optimistic_concurrency(tmp_path):
    storage = FileStorage(tmp_path)
    v1 = base("CLM-C", "claim", {"statement": "v1", "claim_type": "descriptive"})
    storage.create(v1)
    v2 = copy.deepcopy(v1)
    v2["record_version"] = "2"
    v2["content"]["statement"] = "v2"
    storage.update(v2, expected_version="1")

    v3 = copy.deepcopy(v2)
    v3["record_version"] = "3"
    with pytest.raises(ConcurrentUpdateError):
        storage.update(v3, expected_version="1")


def test_storage_rejects_path_traversal(tmp_path):
    storage = FileStorage(tmp_path)
    record = base("../escape", "record", {"note": "x"})
    with pytest.raises(StorageError, match="STORAGE-PATH-TRAVERSAL"):
        storage.create(record)


def test_pipeline_rejects_missing_versioned_reference(tmp_path):
    pipeline = ReferencePipeline(SCHEMA, tmp_path)
    record = base(
        "EUV-X",
        "evidence_use",
        {
            "claim_ref": {"record_id": "CLM-NOT-FOUND", "version": "1"},
            "source_ref": {"record_id": "SRC-NOT-FOUND", "version": "1"},
            "material": {"description": "материал"},
            "evidence_role": "supports",
        },
    )
    result = pipeline.create(record)
    assert result.status == "fail"
    assert any(f.code == "VAL-L3-REFERENCE-VERSION" for f in result.findings)


def test_query_is_deterministic(tmp_path):
    storage = FileStorage(tmp_path)
    storage.create(base("B", "claim", {"statement": "b", "claim_type": "descriptive"}))
    storage.create(base("A", "source", {"source_identity": "a"}))
    query = QueryInterface(storage)
    assert [r["record_id"] for r in query.query()] == ["A", "B"]
    assert [r["record_id"] for r in query.query(record_type="claim")] == ["B"]


def test_publication_does_not_mutate_record():
    record = base("CLM-P", "claim", {"statement": "пример", "claim_type": "descriptive"})
    original = copy.deepcopy(record)
    publication = build_publication([record])
    assert record == original
    assert publication["source_records_unchanged"] is True


def test_package_round_trip(tmp_path):
    record = base("CLM-R", "claim", {"statement": "пример", "claim_type": "descriptive"})
    package = make_package([record], tmp_path / "package")
    recovered, findings = recover_package(package, SCHEMA)
    assert findings == []
    assert recovered.export_all() == [record]


def test_package_integrity_failure(tmp_path):
    record = base("CLM-I", "claim", {"statement": "пример", "claim_type": "descriptive"})
    package = make_package([record], tmp_path / "package")
    path = package / "records" / "CLM-I--1.json"
    path.write_text(path.read_text(encoding="utf-8") + " ", encoding="utf-8")
    recovered, findings = recover_package(package, SCHEMA)
    assert "RECOVERY-INTEGRITY-MISMATCH" in findings
    assert recovered.export_all() == []


def test_full_vertical_slice(tmp_path):
    system = ReferenceSystem(SCHEMA, tmp_path / "storage")
    claim = base(
        "CLM-E2E",
        "claim",
        {"statement": "пример end-to-end", "claim_type": "descriptive"},
    )

    created = system.create(claim)
    assert created.passed

    edited = copy.deepcopy(claim)
    edited["record_version"] = "2"
    edited["content"]["statement"] = "обновлённый пример"
    edited_result = system.edit(edited, expected_version="1")
    assert edited_result.passed

    queried = system.query.query(record_type="claim")
    assert len(queried) == 2

    publication = system.publish()
    assert publication["source_records_unchanged"] is True

    package = system.package(tmp_path / "package")
    recovered, findings = recover_package(package, SCHEMA)
    assert findings == []
    assert recovered.export_all() == queried


def test_unicode_is_preserved(validator):
    record = base(
        "CLM-U",
        "claim",
        {
            "statement": "Знание должно сохраняться: русский язык, Unicode, Ω.",
            "claim_type": "descriptive",
        },
    )
    result = validator.validate(record)
    assert result.status == "pass"


def test_result_does_not_imply_causality(validator):
    record = base(
        "RES-NC",
        "result",
        {
            "result_content": {"value": 1},
            "reference_frame": {"refs": [{"record_id": "ACT-1", "version": "1"}]},
            "origin": ["observed"],
            "causal_attribution": {"mode": "not_attributed"}
        },
    )
    result = validator.validate(record)
    assert result.status == "pass"


def test_inference_is_not_truth(validator):
    record = base(
        "INF-NT",
        "inference",
        {
            "conclusion": {"statement": "C"},
            "attribution": {"mode": "known"}
        },
    )
    record["publication_status"] = "published"
    result = validator.validate(record)
    assert result.status == "pass"


def test_trust_does_not_equal_truth(validator):
    record = base("TR-1", "trust_reputation", {
        "target_ref": {"record_id": "A", "version": "1"},
        "subject_ref": {"record_id": "S", "version": "1"},
        "goal_ref": {"record_id": "G", "version": "1"},
        "assessment_type": "trust",
        "basis_refs": [{"record_id": "B", "version": "1"}],
        "value": {"score": 1}
    })
    record["type_version"] = "1.1"
    record["publication_status"] = "published"
    assert validator.validate(record).status == "pass"


def test_historical_state_is_not_current_state(validator):
    record = base("ST-1", "state", {
        "state_content": {"value": "old"},
        "subject_ref": {"record_id": "A", "version": "1"},
        "status": "historical"
    })
    assert validator.validate(record).status == "pass"


@pytest.mark.parametrize(
    ("record_type", "content"),
    [
        ("assessment", {"target": {"record_id": "CLM-1", "version": "1"}, "aspect": "quality"}),
        ("inference", {}),
        ("decision", {}),
    ],
)
def test_incomplete_lifecycle_records_may_be_partial(validator, record_type, content):
    record = base(f"{record_type}-draft", record_type, content)
    record["completion_status"] = "incomplete"
    result = validator.validate(record)
    assert result.status == "pass"


def test_complete_assessment_requires_result(validator):
    record = base("ASM-C", "assessment", {
        "target": {"record_id": "CLM-1", "version": "1"},
        "aspect": "quality",
    })
    record["completion_status"] = "complete"
    result = validator.validate(record)
    assert any(f.code == "VAL-L4-ASSESSMENT-RESULT" for f in result.findings)


def test_complete_inference_requires_conclusion_and_attribution(validator):
    record = base("INF-C", "inference", {})
    record["completion_status"] = "complete"
    result = validator.validate(record)
    assert any(f.code == "VAL-L4-INFERENCE-CONCLUSION" for f in result.findings)
    assert any(f.code == "VAL-L4-INFERENCE-ATTRIBUTION" for f in result.findings)


def test_complete_decision_requires_result_and_maker(validator):
    record = base("DEC-C", "decision", {})
    record["completion_status"] = "complete"
    result = validator.validate(record)
    assert any(f.code == "VAL-L4-DECISION-RESULT" for f in result.findings)
    assert any(f.code == "VAL-L4-DECISION-MAKER" for f in result.findings)


def test_trust_requires_subject_and_goal(validator):
    record = base("TR-MISSING", "trust_reputation", {
        "target_ref": {"record_id": "A", "version": "1"},
        "assessment_type": "trust",
        "basis_refs": [{"record_id": "B", "version": "1"}],
    })
    record["type_version"] = "1.1"
    result = validator.validate(record)
    assert any(f.code == "VAL-L4-TRUST-SUBJECT" for f in result.findings)
    assert any(f.code == "VAL-L4-TRUST-GOAL" for f in result.findings)
