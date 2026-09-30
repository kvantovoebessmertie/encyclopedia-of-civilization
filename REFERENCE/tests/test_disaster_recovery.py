from __future__ import annotations

import json
from pathlib import Path

from encyclopedia_reference.content_package import build_content_package
from encyclopedia_reference.recovery import recover_package

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"

def _records():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*/records/*.json"))]

def test_disaster_recovery_uses_only_archived_package(tmp_path):
    records = _records()
    package = tmp_path / "archive"
    report = build_content_package(records, package_dir=package, schema_path=SCHEMA, package_id="encyclopedia-v1.0")
    assert report["integrity_and_validation"] == "PASS"
    # Simulate a clean recovery host: only the archived package and local schema remain.
    clean = tmp_path / "clean-host"
    clean.mkdir()
    archived = clean / "package"
    import shutil
    shutil.copytree(package, archived)
    recovered, findings = recover_package(archived, archived / "schemas" / SCHEMA.name)
    assert findings == []
    recovered_records = recovered.export_all()
    assert len(recovered_records) == len(records)
    assert {(r["record_id"], r["record_version"]) for r in recovered_records} == {(r["record_id"], r["record_version"]) for r in records}

def test_disaster_recovery_rejects_tampered_archived_record(tmp_path):
    records = _records()
    package = tmp_path / "archive"
    build_content_package(records, package_dir=package, schema_path=SCHEMA, package_id="encyclopedia-v1.0")
    target = next((package / "records").glob("*.json"))
    target.write_text(target.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    _, findings = recover_package(package, package / "schemas" / SCHEMA.name)
    assert "RECOVERY-INTEGRITY-MISMATCH" in findings

def test_disaster_recovery_rejects_missing_archived_record(tmp_path):
    records = _records()
    package = tmp_path / "archive"
    build_content_package(records, package_dir=package, schema_path=SCHEMA, package_id="encyclopedia-v1.0")
    target = next((package / "records").glob("*.json"))
    target.unlink()
    _, findings = recover_package(package, package / "schemas" / SCHEMA.name)
    assert "RECOVERY-RECORD-MISSING" in findings
