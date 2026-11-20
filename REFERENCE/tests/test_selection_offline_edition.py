from __future__ import annotations

import json

import pytest

from encyclopedia_reference.selection import build_selected_offline_edition


def record(record_id, version="1", **extra):
    value = {
        "record_id": record_id,
        "record_version": version,
        "record_type": "claim",
        "content": {"statement": record_id},
    }
    value.update(extra)
    return value


def entry(record_id, version="1", decision="INCLUDE", dependencies=None):
    return {
        "record_id": record_id,
        "record_version": version,
        "decision": decision,
        "approval": {
            "status": "APPROVED",
            "approver": "SYNTHETIC-TEST-OWNER",
            "reference": "SYNTHETIC-TEST-DECISION",
        },
        "dependencies": dependencies or [],
    }


def selection(*entries):
    return {"schema_version": "1.0", "records": list(entries)}


def test_valid_exact_selection_builds_only_selected_records(tmp_path):
    source = record("SRC-A")
    claim = record("CLM-A", content={"source_ref": {"record_id": "SRC-A", "version": "1"}, "statement": "synthetic"})
    manifest = build_selected_offline_edition(
        [source, claim],
        selection(entry("CLM-A", dependencies=[{"record_id": "SRC-A", "record_version": "1"}]),
                  entry("SRC-A")),
        tmp_path / "edition",
        source_commit="a" * 40,
    )
    built = json.loads((tmp_path / "edition" / "records.json").read_text(encoding="utf-8"))
    assert {item["record_id"] for item in built} == {"CLM-A", "SRC-A"}
    assert manifest["build_mode"] == "selection"
    assert manifest["source_commit"] == "a" * 40
    assert manifest["selected_record_count"] == 2
    assert len(manifest["selection_manifest_sha256"]) == 64


@pytest.mark.parametrize("decision", ["HOLD", "EXCLUDE"])
def test_rejects_non_include_dispositions(tmp_path, decision):
    with pytest.raises(ValueError, match="not approved"):
        build_selected_offline_edition(
            [record("A")], selection(entry("A", decision=decision)),
            tmp_path / "out", source_commit="b" * 40,
        )


def test_rejects_stale_record_version(tmp_path):
    with pytest.raises(ValueError, match="Stale record version"):
        build_selected_offline_edition(
            [record("A", "2")], selection(entry("A", "1")),
            tmp_path / "out", source_commit="b" * 40,
        )


def test_rejects_missing_dependency(tmp_path):
    claim = record("CLM-A", content={"source_ref": {"record_id": "SRC-MISSING", "version": "1"}})
    with pytest.raises(ValueError, match="Missing or stale referenced dependency"):
        build_selected_offline_edition(
            [claim], selection(entry("CLM-A")),
            tmp_path / "out", source_commit="b" * 40,
        )


def test_rejects_declared_dependency_not_in_selection(tmp_path):
    with pytest.raises(ValueError, match="not selected"):
        build_selected_offline_edition(
            [record("A"), record("B")],
            selection(entry("A", dependencies=[{"record_id": "B", "record_version": "1"}])),
            tmp_path / "out", source_commit="b" * 40,
        )


def test_rejects_duplicate_selection_identity(tmp_path):
    with pytest.raises(ValueError, match="Duplicate selection identity"):
        build_selected_offline_edition(
            [record("A")], selection(entry("A"), entry("A")),
            tmp_path / "out", source_commit="b" * 40,
        )


def test_rejects_duplicate_canonical_identity(tmp_path):
    with pytest.raises(ValueError, match="duplicate canonical"):
        build_selected_offline_edition(
            [record("A"), record("A")], selection(entry("A")),
            tmp_path / "out", source_commit="b" * 40,
        )


@pytest.mark.parametrize("manifest", [
    {"schema_version": "1.0", "records": []},
    {"records": [entry("A")]},
    {"schema_version": "1.0"},
])
def test_rejects_missing_or_invalid_selection(tmp_path, manifest):
    with pytest.raises(ValueError):
        build_selected_offline_edition(
            [record("A")], manifest, tmp_path / "out", source_commit="b" * 40,
        )


def test_selection_manifest_digest_is_stable(tmp_path):
    chosen = selection(entry("A"))
    a = build_selected_offline_edition([record("A")], chosen, tmp_path / "a", source_commit="c" * 40)
    b = build_selected_offline_edition([record("A")], chosen, tmp_path / "b", source_commit="c" * 40)
    assert a["selection_manifest_sha256"] == b["selection_manifest_sha256"]


def test_rejects_non_full_source_commit_sha(tmp_path):
    with pytest.raises(ValueError, match="full 40-character Git commit SHA"):
        build_selected_offline_edition(
            [record("A")], selection(entry("A")),
            tmp_path / "out", source_commit="not-a-commit",
        )


def test_rejects_missing_approval_attestation(tmp_path):
    unapproved = entry("A")
    unapproved.pop("approval")
    with pytest.raises(ValueError, match="Missing explicit approval attestation"):
        build_selected_offline_edition(
            [record("A")], selection(unapproved),
            tmp_path / "out", source_commit="d" * 40,
        )


def test_detects_record_version_shaped_dependency_reference(tmp_path):
    claim = record("CLM-A", content={"source_ref": {"record_id": "SRC-A", "record_version": "1"}})
    with pytest.raises(ValueError, match="Dependency closure is incomplete"):
        build_selected_offline_edition(
            [record("SRC-A"), claim], selection(entry("CLM-A")),
            tmp_path / "out", source_commit="e" * 40,
        )
