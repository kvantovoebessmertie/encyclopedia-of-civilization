from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from encyclopedia_reference.recovery import make_package, recover_package
from encyclopedia_reference.storage import FileStorage, StorageError
from encyclopedia_reference.validator import Validator


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"


def base(record_id="R", version="1", record_type="claim"):
    return {
        "record_id": record_id,
        "record_type": record_type,
        "record_version": version,
        "type_version": "1.0",
        "publication_status": "draft",
        "schema": "record/0.1",
        "provenance": {"method": "stress"},
        "content": {"statement": "stress", "claim_type": "descriptive"}
        if record_type == "claim" else {"note": "stress"},
    }


@pytest.fixture
def validator():
    return Validator(SCHEMA)


def test_version_order_is_numeric_for_latest(tmp_path):
    storage = FileStorage(tmp_path)
    for version in ("1", "2", "10"):
        storage.create(base("NUM", version))
    assert storage.list_versions("NUM") == ["1", "2", "10"]
    assert storage.latest("NUM")["record_version"] == "10"


def test_duplicate_record_version_is_rejected(tmp_path):
    storage = FileStorage(tmp_path)
    storage.create(base("DUP", "1"))
    with pytest.raises(StorageError, match="STORAGE-VERSION-EXISTS"):
        storage.create(base("DUP", "1"))


def test_storage_rejects_empty_and_dotdot_identifiers(tmp_path):
    storage = FileStorage(tmp_path)
    for record_id in ("", ".", "..", "a/b", "a\\b"):
        with pytest.raises(StorageError):
            storage.create(base(record_id))


def test_schema_rejects_unknown_record_type(validator):
    record = base(record_type="not_a_type")
    assert validator.validate(record).status == "fail"


def test_schema_rejects_missing_required_envelope_field(validator):
    record = base()
    del record["record_id"]
    result = validator.validate(record)
    assert result.status == "fail"
    assert any(f.layer == "L1" for f in result.findings)


def test_schema_rejects_extra_root_field(validator):
    record = base()
    record["unexpected"] = "x"
    assert validator.validate(record).status == "fail"


def test_publication_truth_boundary_is_not_bypassed_by_other_status(validator):
    for status in ("proposal", "draft", "review", "published", "withdrawn", "archived"):
        record = base()
        record["publication_status"] = status
        record["content"]["truth"] = True
        result = validator.validate(record)
        if status == "published":
            assert any(f.code == "VAL-L4-PUBLICATION-TRUTH" for f in result.findings)
        else:
            assert not any(f.code == "VAL-L4-PUBLICATION-TRUTH" for f in result.findings)


def test_unicode_and_nested_data_survive_storage(tmp_path):
    storage = FileStorage(tmp_path)
    record = base()
    record["content"] = {"statement": "Русский Ω 中文", "claim_type": "descriptive", "nested": {"x": [1, 2, 3]}}
    storage.create(record)
    assert storage.read_version("R", "1") == record


def test_package_rejects_tampered_manifest_hash(tmp_path):
    package = make_package([base("PKG")], tmp_path / "package")
    manifest_path = package / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["records"][0]["sha256"] = "0" * 64
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    recovered, findings = recover_package(package, SCHEMA)
    assert "RECOVERY-INTEGRITY-MISMATCH" in findings
    assert recovered.export_all() == []


def test_package_detects_record_count_mismatch(tmp_path):
    package = make_package([base("PKG")], tmp_path / "package")
    manifest_path = package / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["record_count"] = 999
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    recovered, findings = recover_package(package, SCHEMA)
    assert "RECOVERY-MANIFEST-COUNT" in findings


def test_package_missing_record_is_reported(tmp_path):
    package = make_package([base("PKG")], tmp_path / "package")
    (package / "records" / "PKG--1.json").unlink()
    recovered, findings = recover_package(package, SCHEMA)
    assert "RECOVERY-RECORD-MISSING" in findings
    assert recovered.export_all() == []


def test_package_invalid_json_is_reported(tmp_path):
    package = make_package([base("PKG")], tmp_path / "package")
    path = package / "records" / "PKG--1.json"
    path.write_text("{broken", encoding="utf-8")
    manifest_path = package / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["records"][0]["sha256"] = __import__("hashlib").sha256(b"{broken").hexdigest()
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    recovered, findings = recover_package(package, SCHEMA)
    assert "RECOVERY-INVALID-JSON" in findings
    assert recovered.export_all() == []


def test_package_duplicate_manifest_entry_is_reported(tmp_path):
    package = make_package([base("PKG")], tmp_path / "package")
    manifest_path = package / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["records"].append(copy.deepcopy(manifest["records"][0]))
    manifest["record_count"] = 2
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    recovered, findings = recover_package(package, SCHEMA)
    assert "RECOVERY-DUPLICATE-RECORD" in findings
