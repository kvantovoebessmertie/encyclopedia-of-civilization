from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from encyclopedia_reference.publication import build_publication
from encyclopedia_reference.recovery import make_package, recover_package
from encyclopedia_reference.storage import ConcurrentUpdateError, FileStorage
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


def test_record_passes(validator):
    result = validator.validate(base("REC-1", "record", {"note": "тест"}))
    assert result.status == "pass"


def test_claim_passes(validator):
    result = validator.validate(
        base(
            "CLM-1",
            "claim",
            {"statement": "Вода кипит при соответствующих условиях.", "claim_type": "descriptive"},
        )
    )
    assert result.status == "pass"


def test_source_passes(validator):
    result = validator.validate(
        base(
            "SRC-1",
            "source",
            {"source_identity": "SRC-ID-1", "representation": "text"},
        )
    )
    assert result.status == "pass"


def test_evidence_use_passes(validator):
    result = validator.validate(
        base(
            "EUV-1",
            "evidence_use",
            {
                "claim_ref": {"record_id": "CLM-1", "version": "1"},
                "source_ref": {"record_id": "SRC-1", "version": "1"},
                "material": {"description": "материал"},
                "evidence_role": "supports",
            },
        )
    )
    assert result.status == "pass"


def test_assessment_passes(validator):
    result = validator.validate(
        base(
            "ASM-1",
            "assessment",
            {
                "target": {"record_id": "CLM-1", "version": "1"},
                "aspect": "пример",
                "result": {"value": 1},
            },
        )
    )
    assert result.status == "pass"


def test_invalid_record_fails(validator):
    record = base("CLM-2", "claim", {"statement": ""})
    result = validator.validate(record)
    assert result.status == "fail"


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


def test_unicode_is_preserved(validator):
    record = base(
        "CLM-U",
        "claim",
        {"statement": "Знание должно сохраняться: русский язык, Unicode, Ω.", "claim_type": "descriptive"},
    )
    result = validator.validate(record)
    assert result.status == "pass"
