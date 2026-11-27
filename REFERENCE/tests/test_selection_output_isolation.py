from __future__ import annotations

from pathlib import Path

import pytest

from encyclopedia_reference.selection import build_selected_offline_edition


def _source():
    return {
        "record_id": "SRC-ISOLATION-TEST",
        "record_version": "1",
        "record_type": "source",
        "type_version": "1.0",
        "schema": "record/0.1",
        "content": {"title": "Synthetic isolation fixture"},
    }


def _selection():
    return {
        "schema_version": "1.1",
        "records": [{
            "record_id": "SRC-ISOLATION-TEST",
            "record_version": "1",
            "record_type": "source",
            "type_version": "1.0",
            "schema": "record/0.1",
            "decision": "INCLUDE",
            "approval": {
                "status": "APPROVED",
                "approver": "SYNTHETIC-TEST-OWNER",
                "reference": "SYNTHETIC-OUTPUT-ISOLATION-TEST",
            },
            "dependencies": [],
        }],
    }


def test_selected_build_refuses_nonempty_output_directory(tmp_path: Path):
    output = tmp_path / "edition"
    output.mkdir()
    stale = output / "records-from-previous-full-build.json"
    stale.write_text('[{"record_id":"UNSELECTED-STALE-RECORD"}]', encoding="utf-8")

    with pytest.raises(ValueError, match="must be empty"):
        build_selected_offline_edition(
            [_source()], _selection(), output, source_commit="a" * 40
        )

    assert stale.read_text(encoding="utf-8") == '[{"record_id":"UNSELECTED-STALE-RECORD"}]'
    assert sorted(path.name for path in output.iterdir()) == [stale.name]


def test_selected_build_refuses_output_path_that_is_a_file(tmp_path: Path):
    output = tmp_path / "not-a-directory"
    output.write_text("do not overwrite", encoding="utf-8")

    with pytest.raises(ValueError, match="not a directory"):
        build_selected_offline_edition(
            [_source()], _selection(), output, source_commit="a" * 40
        )

    assert output.read_text(encoding="utf-8") == "do not overwrite"


def test_selected_build_refuses_output_symlink(tmp_path: Path):
    target = tmp_path / "empty-target"
    target.mkdir()
    output = tmp_path / "edition-link"
    output.symlink_to(target, target_is_directory=True)

    with pytest.raises(ValueError, match="must not be a symbolic link"):
        build_selected_offline_edition(
            [_source()], _selection(), output, source_commit="a" * 40
        )

    assert list(target.iterdir()) == []
