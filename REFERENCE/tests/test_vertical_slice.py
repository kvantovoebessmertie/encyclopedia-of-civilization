from __future__ import annotations

import copy
from pathlib import Path

import pytest

from encyclopedia_reference.pipeline import ReferencePipeline
from encyclopedia_reference.publication import build_publication
from encyclopedia_reference.recovery import make_package, recover_package
from encyclopedia_reference.storage import (
    ConcurrentUpdateError,
    FileStorage,
    StorageError,
)
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT.parent / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def base(record_id: str, record_type: str, content: dict) -> dict:
    return {
        "record_id": record_id,
        "record_type": record_type,
        "record_version": "1",
        "type_version": "1.0",
        "publication_status": "draft",
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
    ],
)
def test_vertical_slice_types_pass(validator, record_type, content):
    result = validator.validate(base(f"{record_type}-1", record_type, content))
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
