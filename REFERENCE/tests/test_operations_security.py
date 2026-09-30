from pathlib import Path
import json
import zipfile

from encyclopedia_reference.operations import (
    authorize,
    digest_file,
    manifest_for_files,
    operational_registry,
    scan_secrets,
    validate_archive,
    validate_change_record,
    validate_dependency_lock,
    validate_rollback,
    verify_manifest,
)


def test_operations_registry_covers_o01_o30():
    values = set(operational_registry().values())
    assert {f"O{i:02d}" for i in range(1, 31)} <= values


def test_manifest_detects_corruption(tmp_path: Path):
    target = tmp_path / "record.json"
    target.write_text('{"record_id":"R1"}', encoding="utf-8")
    manifest = manifest_for_files(tmp_path)
    target.write_text('{"record_id":"R2"}', encoding="utf-8")
    assert any(f.code == "OPS-INTEGRITY-MISMATCH" for f in verify_manifest(tmp_path, manifest))


def test_secret_scanning_blocks_public_secret(tmp_path: Path):
    (tmp_path / "public.json").write_text('{"api_key":"supersecret12345"}', encoding="utf-8")
    assert any(f.code == "OPS-SECRET-EXPOSURE" for f in scan_secrets(tmp_path))


def test_archive_path_traversal_is_rejected(tmp_path: Path):
    archive = tmp_path / "bad.zip"
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("../escape.txt", "x")
    assert any(f.code == "OPS-PATH-TRAVERSAL" for f in validate_archive(archive, tmp_path / "extract"))


def test_archive_integrity_is_checked(tmp_path: Path):
    archive = tmp_path / "ok.zip"
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("record.json", "{}")
    assert validate_archive(archive, tmp_path / "extract") == []


def test_authorization_requires_role():
    assert authorize({"editor"}, "editor")
    assert not authorize({"reader"}, "editor")
    assert authorize({"administrator"}, "recovery operator")


def test_dependency_lock_requires_digest():
    assert validate_dependency_lock({"dependencies":[{"name":"pytest","version":"1.0"}]})
    assert not validate_dependency_lock({"dependencies":[{"name":"pytest","version":"1.0","digest":"sha256:x"}]})


def test_change_record_is_complete():
    complete = {
        "change_id":"CH-1","reason":"test","components":["validator"],
        "actor":"operator","from_version":"1","to_version":"2",
        "test_result":"pass","rollback_plan":"restore package"
    }
    assert validate_change_record(complete) == []


def test_rollback_never_deletes_history():
    findings = validate_rollback(
        {"record_id":"R","record_version":"3"},
        {"record_id":"R","record_version":"2","history_deleted":True},
    )
    assert any(f.code == "OPS-ROLLBACK-HISTORY-LOSS" for f in findings)


def test_backup_restore_fixture_round_trip(tmp_path: Path):
    source = tmp_path / "source"
    restored = tmp_path / "restored"
    source.mkdir()
    restored.mkdir()
    (source / "record.json").write_text('{"record_id":"R","record_version":"1"}', encoding="utf-8")
    import shutil
    shutil.copytree(source, restored, dirs_exist_ok=True)
    before = manifest_for_files(source)
    after = manifest_for_files(restored)
    assert before == after
