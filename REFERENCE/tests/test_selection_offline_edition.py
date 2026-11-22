from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from encyclopedia_reference.selection import build_selected_offline_edition


def record(record_id, version="1", **extra):
    value = {
        "record_id": record_id,
        "record_version": version,
        "record_type": "claim",
        "type_version": "1.0",
        "schema": "record/0.1",
        "content": {"statement": record_id},
    }
    value.update(extra)
    return value


def pin(record_id, record_type="source", version="1", type_version="1.0", schema="record/0.1"):
    return {
        "record_id": record_id,
        "record_version": version,
        "record_type": record_type,
        "type_version": type_version,
        "schema": schema,
    }


def entry(record_id, version="1", record_type="claim", decision="INCLUDE", dependencies=None, type_version="1.0", schema="record/0.1"):
    return {
        **pin(record_id, record_type, version, type_version, schema),
        "decision": decision,
        "approval": {
            "status": "APPROVED",
            "approver": "SYNTHETIC-TEST-OWNER",
            "reference": "SYNTHETIC-TEST-DECISION",
        },
        "dependencies": dependencies or [],
    }


def selection(*entries):
    return {"schema_version": "1.1", "records": list(entries)}


def _init_git_checkout(root: Path) -> str:
    subprocess.run(["git", "init", str(root)], check=True, capture_output=True, text=True)
    subprocess.run(["git", "-C", str(root), "config", "user.name", "MVP test"], check=True)
    subprocess.run(["git", "-C", str(root), "config", "user.email", "mvp-test@example.invalid"], check=True)
    subprocess.run(["git", "-C", str(root), "add", "CONTENT"], check=True)
    subprocess.run(
        ["git", "-C", str(root), "commit", "-m", "Create synthetic source fixture"],
        check=True,
        capture_output=True,
        text=True,
    )
    return subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def test_valid_exact_selection_builds_only_selected_records(tmp_path):
    source = record("SRC-A", record_type="source")
    claim = record(
        "CLM-A",
        record_type="claim",
        provenance={"created_from": [{"record_id": "SRC-A", "version": "1"}]},
    )
    evidence = record(
        "EU-A",
        record_type="evidence_use",
        provenance={"created_from": [{"record_id": "SRC-A", "version": "1"}]},
        content={
            "claim_ref": {"record_id": "CLM-A", "version": "1"},
            "source_ref": {"record_id": "SRC-A", "version": "1"},
            "evidence_role": "supports",
        },
    )
    manifest = build_selected_offline_edition(
        [source, claim, evidence, record("NOT-SELECTED")],
        selection(
            entry("CLM-A", dependencies=[pin("SRC-A")]),
            entry("SRC-A", record_type="source"),
            entry("EU-A", record_type="evidence_use", dependencies=[
                pin("CLM-A", record_type="claim"),
                pin("SRC-A", record_type="source"),
            ]),
        ),
        tmp_path / "edition",
        source_commit="a" * 40,
    )
    built = json.loads((tmp_path / "edition" / "records.json").read_text(encoding="utf-8"))
    assert {item["record_id"] for item in built} == {"CLM-A", "EU-A", "SRC-A"}
    assert manifest["build_mode"] == "selection"
    assert manifest["source_commit"] == source_commit
    assert manifest["selected_record_count"] == 3
    assert {item["record_type"] for item in manifest["selected_records"]} == {"claim", "source", "evidence_use"}
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
            [claim], selection(entry("CLM-A")), tmp_path / "out", source_commit="b" * 40,
        )


def test_rejects_declared_dependency_not_in_selection(tmp_path):
    with pytest.raises(ValueError, match="not selected"):
        build_selected_offline_edition(
            [record("A"), record("B")],
            selection(entry("A", dependencies=[pin("B", record_type="claim")])),
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
    {"schema_version": "1.1", "records": []},
    {"records": [entry("A")]},
    {"schema_version": "1.1"},
    {"schema_version": "1.0", "records": [entry("A")]},
])
def test_rejects_missing_or_unsupported_selection(tmp_path, manifest):
    with pytest.raises(ValueError):
        build_selected_offline_edition(
            [record("A")], manifest, tmp_path / "out", source_commit="b" * 40,
        )


def test_selection_manifest_digest_is_stable(tmp_path):
    chosen = selection(entry("A", record_type="source"))
    a = build_selected_offline_edition([record("A", record_type="source")], chosen, tmp_path / "a", source_commit="c" * 40)
    b = build_selected_offline_edition([record("A", record_type="source")], chosen, tmp_path / "b", source_commit="c" * 40)
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


@pytest.mark.parametrize("field,bad_value", [
    ("record_type", "source"),
    ("type_version", "9.9"),
    ("schema", "record/9.9"),
])
def test_rejects_selection_type_or_schema_drift(tmp_path, field, bad_value):
    selected = entry("A")
    selected[field] = bad_value
    with pytest.raises(ValueError, match=f"{field} mismatch"):
        build_selected_offline_edition(
            [record("A")], selection(selected),
            tmp_path / "out", source_commit="d" * 40,
        )


@pytest.mark.parametrize("field,bad_value", [
    ("record_type", "claim"),
    ("type_version", "9.9"),
    ("schema", "record/9.9"),
])
def test_rejects_dependency_type_or_schema_drift(tmp_path, field, bad_value):
    claim = record("CLM-A", provenance={"created_from": [{"record_id": "SRC-A", "version": "1"}]})
    source = record("SRC-A", record_type="source")
    dependency = pin("SRC-A")
    dependency[field] = bad_value
    with pytest.raises(ValueError, match=f"{field} mismatch"):
        build_selected_offline_edition(
            [claim, source],
            selection(entry("CLM-A", dependencies=[dependency]), entry("SRC-A", record_type="source")),
            tmp_path / "out", source_commit="d" * 40,
        )


def test_rejects_canonical_record_without_type_profile_pin(tmp_path):
    malformed = record("A")
    malformed.pop("type_version")
    with pytest.raises(ValueError, match="missing type_version"):
        build_selected_offline_edition(
            [malformed], selection(entry("A")),
            tmp_path / "out", source_commit="d" * 40,
        )


def test_detects_record_version_shaped_dependency_reference(tmp_path):
    claim = record("CLM-A", content={"source_ref": {"record_id": "SRC-A", "record_version": "1"}})
    with pytest.raises(ValueError, match="Dependency closure is incomplete"):
        build_selected_offline_edition(
            [record("SRC-A"), claim], selection(entry("CLM-A")),
            tmp_path / "out", source_commit="e" * 40,
        )


def test_rejects_claim_without_selected_evidence_use(tmp_path):
    claim = record("CLM-A", record_type="claim")
    with pytest.raises(ValueError, match="no selected Evidence Use"):
        build_selected_offline_edition(
            [claim], selection(entry("CLM-A")),
            tmp_path / "out", source_commit="f" * 40,
        )


def test_rejects_evidence_use_without_selected_source(tmp_path):
    claim = record("CLM-A", record_type="claim")
    source = record("SRC-A", record_type="source")
    evidence = record(
        "EU-A",
        record_type="evidence_use",
        content={
            "claim_ref": {"record_id": "CLM-A", "version": "1"},
            "source_ref": {"record_id": "SRC-A", "version": "1"},
        },
    )
    with pytest.raises(ValueError, match="Declared dependencies are not selected"):
        build_selected_offline_edition(
            [claim, source, evidence],
            selection(entry("CLM-A"), entry("EU-A", record_type="evidence_use", dependencies=[
                pin("CLM-A", record_type="claim"),
                pin("SRC-A", record_type="source"),
            ])),
            tmp_path / "out", source_commit="f" * 40,
        )


def test_rejects_unreferenced_manifest_dependency(tmp_path):
    with pytest.raises(ValueError, match="non-referenced dependencies"):
        build_selected_offline_edition(
            [record("A", record_type="source"), record("B", record_type="source")],
            selection(
                entry("A", record_type="source", dependencies=[pin("B", record_type="source")]),
                entry("B", record_type="source"),
            ),
            tmp_path / "out", source_commit="7" * 40,
        )


def test_rejects_duplicate_dependency_declaration(tmp_path):
    with pytest.raises(ValueError, match="Duplicate dependency"):
        build_selected_offline_edition(
            [record("A", record_type="source"), record("B", record_type="source")],
            selection(entry("A", record_type="source", dependencies=[pin("B"), pin("B")] ), entry("B", record_type="source")),
            tmp_path / "out", source_commit="7" * 40,
        )


def test_rejects_multiple_versions_of_same_selected_record(tmp_path):
    with pytest.raises(ValueError, match="multiple versions of one record"):
        build_selected_offline_edition(
            [record("A", "1", record_type="source"), record("A", "2", record_type="source")],
            selection(entry("A", "1", record_type="source"), entry("A", "2", record_type="source")),
            tmp_path / "out", source_commit="7" * 40,
        )


def test_cli_selection_manifest_builds_only_selected_records(tmp_path):
    root = tmp_path / "repo"
    records_dir = root / "CONTENT" / "vertical-slices" / "synthetic" / "records"
    records_dir.mkdir(parents=True)

    source = record("SRC-A", record_type="source")
    claim = record(
        "CLM-A",
        record_type="claim",
        provenance={"created_from": [{"record_id": "SRC-A", "version": "1"}]},
    )
    evidence = record(
        "EU-A",
        record_type="evidence_use",
        content={
            "claim_ref": {"record_id": "CLM-A", "version": "1"},
            "source_ref": {"record_id": "SRC-A", "version": "1"},
            "evidence_role": "supports",
        },
    )
    for item in (source, claim, evidence):
        (records_dir / f"{item['record_id']}.json").write_text(
            json.dumps(item), encoding="utf-8"
        )

    source_commit = _init_git_checkout(root)

    selection_path = tmp_path / "selection.json"
    selection_path.write_text(
        json.dumps(
            selection(
                entry("CLM-A", dependencies=[pin("SRC-A")]),
                entry("SRC-A", record_type="source"),
                entry("EU-A", record_type="evidence_use", dependencies=[
                    pin("CLM-A", record_type="claim"),
                    pin("SRC-A", record_type="source"),
                ]),
            )
        ),
        encoding="utf-8",
    )

    script = Path(__file__).resolve().parents[1] / "build_offline_edition.py"
    output_dir = tmp_path / "selected-edition"
    command = [
        sys.executable,
        str(script),
        "--root",
        str(root),
        "--output",
        str(output_dir),
        "--selection-manifest",
        str(selection_path),
    ]
    mismatch = subprocess.run(
        [*command, "--source-commit", "a" * 40],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        text=True,
        check=False,
    )
    assert mismatch.returncode == 2
    assert "does not match the checked-out HEAD" in mismatch.stderr
    assert not output_dir.exists()

    result = subprocess.run(
        [*command, "--source-commit", source_commit],
        cwd=Path(__file__).resolve().parents[2],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    built = json.loads((output_dir / "records.json").read_text(encoding="utf-8"))
    manifest = json.loads(result.stdout)
    assert {item["record_id"] for item in built} == {"CLM-A", "EU-A", "SRC-A"}
    assert manifest["build_mode"] == "selection"
    assert manifest["source_commit"] == "a" * 40
    assert manifest["selected_record_count"] == 3
