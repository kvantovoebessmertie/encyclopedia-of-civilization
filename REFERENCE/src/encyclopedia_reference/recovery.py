from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import shutil
import tempfile

from . import PACKAGE_VERSION
from .storage import FileStorage
from .validator import Validator


def make_package(records: list[dict[str, Any]], target: Path) -> Path:
    target.mkdir(parents=True, exist_ok=True)
    (target / "records").mkdir(exist_ok=True)
    for record in records:
        path = target / "records" / f"{record['record_id']}--{record['record_version']}.json"
        path.write_text(
            json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    manifest = {
        "package_version": PACKAGE_VERSION,
        "record_count": len(records),
        "records": sorted(
            [
                {
                    "record_id": r["record_id"],
                    "record_version": r["record_version"],
                }
                for r in records
            ],
            key=lambda x: (x["record_id"], x["record_version"]),
        ),
    }
    (target / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def recover_package(
    package: Path,
    schema_path: Path,
) -> tuple[FileStorage, list[Any]]:
    with tempfile.TemporaryDirectory() as temp:
        storage = FileStorage(Path(temp) / "storage")
        validator = Validator(schema_path)
        findings = []

        manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
        for item in manifest["records"]:
            path = (
                package
                / "records"
                / f"{item['record_id']}--{item['record_version']}.json"
            )
            record = json.loads(path.read_text(encoding="utf-8"))
            result = validator.validate(record)
            findings.extend(result.findings)
            if result.passed:
                storage.create(record)

        # Возвращаем объект и findings до завершения clean-environment теста
        # через копирование во временную директорию невозможно, поэтому для
        # первого среза возвращается только итог в виде detached snapshot.
        snapshot = FileStorage(Path(temp) / "snapshot").export_all()
        return _SnapshotStorage(snapshot), findings


class _SnapshotStorage:
    def __init__(self, records: list[dict[str, Any]]):
        self.records = records

    def export_all(self) -> list[dict[str, Any]]:
        return self.records
