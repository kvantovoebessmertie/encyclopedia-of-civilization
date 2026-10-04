from __future__ import annotations

import copy
import json
from pathlib import Path

from encyclopedia_reference.recovery import recover_package
from encyclopedia_reference.system import ReferenceSystem

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "IMPLEMENTATION" / "005-RECORD-SCHEMA.json"
SLICE = ROOT / "CONTENT" / "vertical-slices" / "earth-system-basics" / "records"


def _load(name: str) -> dict:
    return json.loads((SLICE / name).read_text(encoding="utf-8"))


def test_r17_system_in_action_end_to_end(tmp_path):
    """
    Real runtime scenario:
    authoritative source -> claims -> evidence use -> context/scope
    -> Human View -> publication -> package/recovery -> versioned edit.

    This is intentionally not a corpus-count test. It exercises the ReferenceSystem
    facade and verifies that the semantic chain survives the full operational path.
    """
    system = ReferenceSystem(SCHEMA, tmp_path / "storage")

    names = [
        "SRC-EARTH_SYSTEM_BASICS.json",
        "CLM-EARTH_SYSTEM_BASICS-A.json",
        "CLM-EARTH_SYSTEM_BASICS-B.json",
        "CLM-EARTH_SYSTEM_BASICS-C.json",
        "EU-EARTH_SYSTEM_BASICS-A.json",
        "EU-EARTH_SYSTEM_BASICS-B.json",
        "EU-EARTH_SYSTEM_BASICS-C.json",
        "CTX-EARTH_SYSTEM_BASICS.json",
        "SCP-EARTH_SYSTEM_BASICS.json",
    ]
    records = [_load(name) for name in names]

    # Ingest the dependency graph in source -> claim -> evidence -> context/scope order.
    for record in records:
        result = system.create(record)
        assert result.passed, (
            record["record_id"],
            [(f.code, f.message) for f in result.findings],
        )

    # A user asks to understand a claim and verify its evidential basis.
    understood = system.human(
        "CLM-EARTH_SYSTEM_BASICS-A", "1", mode="UNDERSTAND"
    )
    assert understood["status"] == "ok"
    assert understood["known"]
    assert understood["safety"]["source_is_not_truth"] is True

    verified = system.human(
        "EU-EARTH_SYSTEM_BASICS-A", "1", mode="VERIFY"
    )
    assert verified["status"] == "ok"
    assert verified["verification"]["available"] is True
    assert any(
        ref["record_id"] == "CLM-EARTH_SYSTEM_BASICS-A"
        for ref in verified["verification"]["evidence_path"]
    )
    assert any(
        ref["record_id"] == "SRC-EARTH_SYSTEM_BASICS"
        for ref in verified["verification"]["evidence_path"]
    )

    # APPLY must not silently turn a bounded record into a current recommendation.
    applied = system.human(
        "CLM-EARTH_SYSTEM_BASICS-A", "1", mode="APPLY"
    )
    assert applied["status"] == "ok"
    assert applied["apply"]["required_user_context"] is True
    assert applied["applicability"]["status"] == "not_established"

    # Publication is derived; canonical source records remain unchanged.
    before = copy.deepcopy(system.query.query())
    publication = system.publish()
    assert publication["derived"] is True
    assert publication["source_records_unchanged"] is True
    assert publication["citations_preserved"] is True
    assert len(publication["entries"]) == len(before)

    # Package -> recovery is a real persistence round trip.
    package_dir = system.package(tmp_path / "package")
    recovered, findings = recover_package(package_dir, SCHEMA)
    assert findings == []
    assert len(recovered.export_all()) == len(before)

    # Versioned edit preserves the original version and creates a new one.
    edited = _load("CLM-EARTH_SYSTEM_BASICS-A.json")
    edited["record_version"] = "2"
    edited["content"]["statement"] = (
        "Земная система включает взаимосвязанные компоненты, среди которых "
        "атмосфера, гидросфера, геосфера и биосфера."
    )
    edited_result = system.edit(edited, expected_version="1")
    assert edited_result.passed
    assert system.query.query(record_type="claim")[0]["record_type"] == "claim"
    assert system.pipeline.storage.list_versions(
        "CLM-EARTH_SYSTEM_BASICS-A"
    ) == ["1", "2"]
    assert system.pipeline.storage.read_version(
        "CLM-EARTH_SYSTEM_BASICS-A", "1"
    )["content"]["statement"] != ""
    assert system.pipeline.storage.read_version(
        "CLM-EARTH_SYSTEM_BASICS-A", "2"
    )["content"]["statement"] == edited["content"]["statement"]


def test_r17_system_in_action_rejects_unsafe_semantic_shortcut(tmp_path):
    """
    Adversarial runtime scenario: a caller attempts to create a record that
    declares a semantic violation. The facade must reject it and must not persist it.
    """
    system = ReferenceSystem(SCHEMA, tmp_path / "storage")
    record = {
        "record_id": "SYSTEM-IN-ACTION-ADVERSARIAL-001",
        "record_type": "record",
        "record_version": "1",
        "type_version": "1.0",
        "publication_status": "draft",
        "completion_status": "complete",
        "schema": "record/0.1",
        "provenance": {"method": "system-in-action-test"},
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
    }

    result = system.create(record)
    assert not result.passed
    assert any(f.severity == "error" for f in result.findings)
    assert system.pipeline.storage.export_all() == []
