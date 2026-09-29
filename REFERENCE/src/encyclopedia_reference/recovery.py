from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import tempfile

from . import PACKAGE_VERSION
from .storage import FileStorage
from .validator import Validator
from .references import ReferenceResolver


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
        payload = json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        path.write_text(payload, encoding="utf-8")
        manifest_records.append({
            "record_id": record["record_id"],
            "record_version": record["record_version"],
            "file": filename,
            "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
        })

    manifest = {
        "package_version": PACKAGE_VERSION,
        "record_count": len(records),
        "records": sorted(manifest_records, key=lambda x: (x["record_id"], x["record_version"])),
    }
    (target / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def recover_package(package: Path, schema_path: Path) -> tuple[Any, list[Any]]:
    validator = Validator(schema_path)
    findings: list[Any] = []
    try:
        manifest = json.loads((package / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return _SnapshotStorage([]), ["RECOVERY-INVALID-MANIFEST"]

    entries = manifest.get("records")
    if not isinstance(entries, list):
        return _SnapshotStorage([]), ["RECOVERY-INVALID-MANIFEST"]

    if manifest.get("record_count") != len(entries):
        findings.append("RECOVERY-MANIFEST-COUNT")

    with tempfile.TemporaryDirectory() as temp:
        storage = FileStorage(Path(temp) / "storage")
        records_dir = (package / "records").resolve()
        seen: set[tuple[Any, Any]] = set()

        for item in entries:
            if not isinstance(item, dict):
                findings.append("RECOVERY-INVALID-ENTRY")
                continue

            record_key = (item.get("record_id"), item.get("record_version"))
            if record_key in seen:
                findings.append("RECOVERY-DUPLICATE-RECORD")
                continue
            seen.add(record_key)

            filename = item.get("file")
            if not isinstance(filename, str) or Path(filename).name != filename or "\\" in filename:
                findings.append("RECOVERY-INVALID-FILENAME")
                continue

            path = (records_dir / filename).resolve()
            if records_dir not in path.parents:
                findings.append("RECOVERY-PATH-TRAVERSAL")
                continue
            if not path.is_file():
                findings.append("RECOVERY-RECORD-MISSING")
                continue

            try:
                payload = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                findings.append("RECOVERY-READ-ERROR")
                continue

            digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
            if digest != item.get("sha256"):
                findings.append("RECOVERY-INTEGRITY-MISMATCH")
                continue

            try:
                record = json.loads(payload)
            except json.JSONDecodeError:
                findings.append("RECOVERY-INVALID-JSON")
                continue

            result = validator.validate(record)
            findings.extend(result.findings)
            if result.passed:
                try:
                    storage.create(record)
                except Exception as exc:
                    findings.append(str(exc))

        snapshot = storage.export_all()

        # L5 dataset checks run only after the complete recoverable snapshot is
        # assembled, so they are independent of manifest/file ordering.
        dataset_result = validator.validate_dataset(snapshot, schema_path)
        findings.extend(dataset_result.findings)

        resolver = ReferenceResolver(storage)
        for record in snapshot:
            findings.extend(resolver.validate(record))

    return _SnapshotStorage(snapshot), findings


class _SnapshotStorage:
    def __init__(self, records: list[dict[str, Any]]):
        self.records = records

    def export_all(self) -> list[dict[str, Any]]:
        return self.records
