from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import tempfile

from . import PACKAGE_VERSION
from .storage import FileStorage
from .validator import Validator


def _package_filename(record_id: str, version: str) -> str:
    for value in (record_id, version):
        if not isinstance(value, str) or not value or value in {".", ".."}:
            raise ValueError("PACKAGE-INVALID-IDENTIFIER")
        if "/" in value or "\\" in value:
            raise ValueError("PACKAGE-PATH-TRAVERSAL")
    return f"{record_id}--{version}.json"


def make_package(records: list[dict[str, Any]], target: Path) -> Path:
    target.mkdir(parents=True, exist_ok=True)
    records_dir = target / "records"
    records_dir.mkdir(exist_ok=True)

    manifest_records = []
    for record in records:
        filename = _package_filename(record["record_id"], record["record_version"])
        path = records_dir / filename
        payload = json.dumps(
            record, ensure_ascii=False, indent=2, sort_keys=True
        ) + "\n"
        path.write_text(payload, encoding="utf-8")
        manifest_records.append(
            {
                "record_id": record["record_id"],
                "record_version": record["record_version"],
                "file": filename,
                "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
            }
        )

    manifest = {
        "package_version": PACKAGE_VERSION,
        "record_count": len(records),
        "records": sorted(
            manifest_records,
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
) -> tuple[Any, list[Any]]:
    validator = Validator(schema_path)
    findings = []
    manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
    snapshot: list[dict[str, Any]] = []

    with tempfile.TemporaryDirectory() as temp:
        storage = FileStorage(Path(temp) / "storage")
        records_dir = (package / "records").resolve()

        for item in manifest["records"]:
            filename = item["file"]
            if Path(filename).name != filename:
                findings.append(
                    validator._finding if False else None
                )
                continue

            path = (records_dir / filename).resolve()
            if records_dir not in path.parents:
                continue

            payload = path.read_text(encoding="utf-8")
            digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
            if digest != item["sha256"]:
                findings.append("RECOVERY-INTEGRITY-MISMATCH")
                continue

            record = json.loads(payload)
            result = validator.validate(record)
            findings.extend(result.findings)
            if result.passed:
                storage.create(record)

        snapshot = storage.export_all()

    return _SnapshotStorage(snapshot), findings


class _SnapshotStorage:
    def __init__(self, records: list[dict[str, Any]]):
        self.records = records

    def export_all(self) -> list[dict[str, Any]]:
        return self.records
