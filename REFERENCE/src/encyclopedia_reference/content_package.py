from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .publication import build_publication
from .recovery import make_package, recover_package


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_content_package(
    records: list[dict[str, Any]],
    *,
    package_dir: Path,
    schema_path: Path,
    package_id: str,
    package_version: str = "1.0",
) -> dict[str, Any]:
    """Build a deterministic, offline content package and evidence report."""
    package_dir.mkdir(parents=True, exist_ok=True)
    make_package(records, package_dir)

    schema_target = package_dir / "schemas" / schema_path.name
    schema_target.parent.mkdir(parents=True, exist_ok=True)
    schema_bytes = schema_path.read_bytes()
    schema_target.write_bytes(schema_bytes)

    publication = build_publication(records)
    publication_path = package_dir / "publication.json"
    publication_bytes = (
        json.dumps(publication, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    publication_path.write_bytes(publication_bytes)

    manifest_path = package_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({
        "package_id": package_id,
        "package_version": package_version,
        "package_class": "content-vertical-slice",
        "completeness": "complete_for_declared_slice",
        "network_required": False,
        "schema": {
            "file": f"schemas/{schema_path.name}",
            "sha256": _sha256_bytes(schema_bytes),
        },
        "publication": {
            "file": "publication.json",
            "sha256": _sha256_bytes(publication_bytes),
        },
        "source_policy": "external source identities are preserved; source pages are not silently copied",
        "semantic_boundary": "package integrity and conformance do not establish truth",
    })
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    recovered, findings = recover_package(package_dir, schema_target)
    recovery = {
        "package_id": package_id,
        "package_version": package_version,
        "network_required": False,
        "integrity_and_validation": "PASS" if not findings else "FAIL",
        "recovered_record_count": len(recovered.export_all()),
        "expected_record_count": len(records),
        "findings": findings,
        "publication_present": publication_path.is_file(),
        "offline_schema_present": schema_target.is_file(),
        "reproducible_record_ids": sorted(
            (r["record_id"], r["record_version"]) for r in recovered.export_all()
        ),
    }
    runtime_manifest = {
        "runtime_manifest_version": "1.0",
        "reference_implementation": "encyclopedia_reference",
        "validator": "REFERENCE/src/encyclopedia_reference/validator.py",
        "schema": f"schemas/{schema_path.name}",
        "network_required": False,
        "execution_policy": "recovery and validation must complete from package-local inputs",
    }
    runtime_path = package_dir / "runtime-manifest.json"
    runtime_path.write_text(
        json.dumps(runtime_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    audit = {
        "audit_trail_version": "1.0",
        "package_id": package_id,
        "package_version": package_version,
        "operation": "build_content_package",
        "record_count": len(records),
        "records": [
            {
                "record_id": record["record_id"],
                "record_version": record["record_version"],
                "record_sha256": hashlib.sha256(
                    (json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
                ).hexdigest(),
            }
            for record in sorted(records, key=lambda r: (r["record_id"], r["record_version"]))
        ],
        "schema_sha256": _sha256_bytes(schema_bytes),
        "publication_sha256": _sha256_bytes(publication_bytes),
        "network_required": False,
        "epistemic_boundary": "audit trail records build provenance; it does not establish truth",
    }
    audit_path = package_dir / "package-audit.json"
    audit_path.write_text(
        json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({
        "runtime_manifest": {
            "file": "runtime-manifest.json",
            "sha256": _sha256_bytes(runtime_path.read_bytes()),
        },
        "audit_trail": {
            "file": "package-audit.json",
            "sha256": _sha256_bytes(audit_path.read_bytes()),
        },
    })
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    recovery["runtime_manifest_present"] = runtime_path.is_file()
    recovery["audit_trail_present"] = audit_path.is_file()
    recovery_path = package_dir / "recovery-report.json"
    recovery_path.write_text(
        json.dumps(recovery, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return recovery
