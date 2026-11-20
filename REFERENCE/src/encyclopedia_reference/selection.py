from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .offline_edition import build_offline_edition

_REF = re.compile(r"^([A-Za-z0-9][A-Za-z0-9_.:-]*)@([0-9]+)$")


def _digest(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _record_refs(value: Any):
    """Yield exact version-pinned references represented as ID@integer strings."""
    if isinstance(value, dict):
        ref_version = value.get("version", value.get("record_version"))
        if isinstance(value.get("record_id"), str) and isinstance(ref_version, (str, int)):
            yield (value["record_id"], str(ref_version))
        for item in value.values():
            yield from _record_refs(item)
    elif isinstance(value, list):
        for item in value:
            yield from _record_refs(item)
    elif isinstance(value, str):
        match = _REF.fullmatch(value)
        if match:
            yield (match.group(1), match.group(2))


def _structured_ref(value: Any) -> tuple[str, str] | None:
    if not isinstance(value, dict) or not isinstance(value.get("record_id"), str):
        return None
    version = value.get("version", value.get("record_version"))
    if not isinstance(version, (str, int)):
        return None
    return (value["record_id"], str(version))


def _validate_claim_evidence_closure(
    selected_records: list[dict[str, Any]],
    selected_keys: set[tuple[str, str]],
) -> None:
    """Require each selected Claim to have selected Evidence Use -> Source."""
    evidence_by_claim: dict[tuple[str, str], list[dict[str, Any]]] = {}
    selected_by_key = {
        (record["record_id"], str(record["record_version"])): record
        for record in selected_records
    }
    for record in selected_records:
        if record.get("record_type") != "evidence_use":
            continue
        content = record.get("content")
        if not isinstance(content, dict):
            raise ValueError(f"Evidence Use has no content object: {record.get('record_id')}")
        claim_key = _structured_ref(content.get("claim_ref"))
        source_key = _structured_ref(content.get("source_ref"))
        if claim_key is None or source_key is None:
            raise ValueError(f"Evidence Use requires exact claim_ref and source_ref: {record.get('record_id')}")
        if claim_key not in selected_keys:
            raise ValueError(f"Evidence Use Claim dependency is not selected: {claim_key}")
        if source_key not in selected_keys:
            raise ValueError(f"Evidence Use Source dependency is not selected: {source_key}")
        if selected_by_key[claim_key].get("record_type") != "claim":
            raise ValueError(f"Evidence Use claim_ref does not target a Claim: {claim_key}")
        if selected_by_key[source_key].get("record_type") != "source":
            raise ValueError(f"Evidence Use source_ref does not target a Source: {source_key}")
        evidence_by_claim.setdefault(claim_key, []).append(record)

    for key in selected_keys:
        if selected_by_key[key].get("record_type") == "claim" and not evidence_by_claim.get(key):
            raise ValueError(f"Selected Claim has no selected Evidence Use: {key}")


def build_selected_offline_edition(
    all_records: list[dict[str, Any]],
    selection: dict[str, Any],
    output_dir: Path,
    *,
    source_commit: str,
    edition_id: str = "encyclopedia-selected-offline",
) -> dict[str, Any]:
    """Build only an explicitly approved, exact-version selection.

    The selection document must enumerate every selected record and its direct
    dependencies. References found in record payloads are checked against that
    declared selection; dependencies are never silently auto-added.
    """
    if selection.get("schema_version") != "1.0":
        raise ValueError("Unsupported or missing selection schema_version")
    entries = selection.get("records")
    if not isinstance(entries, list) or not entries:
        raise ValueError("Selection must contain a non-empty records list")
    if not isinstance(source_commit, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", source_commit):
        raise ValueError("source_commit must be a full 40-character Git commit SHA")

    available: dict[tuple[str, str], dict[str, Any]] = {}
    identities: set[tuple[str, str]] = set()
    for record in all_records:
        key = (str(record.get("record_id", "")), str(record.get("record_version", "")))
        if not all(key) or key in identities:
            raise ValueError(f"Missing or duplicate canonical record identity: {key}")
        identities.add(key)
        available[key] = record

    selected_keys: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    declared_dependencies: dict[tuple[str, str], set[tuple[str, str]]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("Each selection entry must be an object")
        key = (str(entry.get("record_id", "")), str(entry.get("record_version", "")))
        if not all(key):
            raise ValueError("Selection entry requires record_id and record_version")
        if key in seen:
            raise ValueError(f"Duplicate selection identity: {key}")
        seen.add(key)
        if entry.get("decision") != "INCLUDE":
            raise ValueError(f"Record is not approved for inclusion: {key}")
        approval = entry.get("approval")
        if (
            not isinstance(approval, dict)
            or approval.get("status") != "APPROVED"
            or not isinstance(approval.get("approver"), str)
            or not approval["approver"].strip()
            or not isinstance(approval.get("reference"), str)
            or not approval["reference"].strip()
        ):
            raise ValueError(f"Missing explicit approval attestation for {key}")
        if key not in available:
            same_id = sorted(v for rid, v in identities if rid == key[0])
            if same_id:
                raise ValueError(f"Stale record version for {key}; available versions: {same_id}")
            raise ValueError(f"Selected record does not exist: {key}")
        deps = entry.get("dependencies", [])
        if not isinstance(deps, list):
            raise ValueError(f"dependencies must be a list for {key}")
        dep_keys = set()
        for dep in deps:
            if not isinstance(dep, dict) or not dep.get("record_id") or not dep.get("record_version"):
                raise ValueError(f"Dependency must pin record_id and record_version for {key}")
            dep_key = (str(dep["record_id"]), str(dep["record_version"]))
            if dep_key not in available:
                raise ValueError(f"Missing or stale dependency {dep_key} required by {key}")
            dep_keys.add(dep_key)
        declared_dependencies[key] = dep_keys
        selected_keys.append(key)

    selected_set = set(selected_keys)
    for key in selected_keys:
        references = set(_record_refs(available[key]))
        unresolved = references - identities
        if unresolved:
            raise ValueError(f"Missing or stale referenced dependency for {key}: {sorted(unresolved)}")
        undeclared = references - declared_dependencies[key]
        if undeclared:
            raise ValueError(f"Dependency closure is incomplete for {key}: {sorted(undeclared)}")
        omitted_declarations = declared_dependencies[key] - selected_set
        if omitted_declarations:
            raise ValueError(f"Declared dependencies are not selected for {key}: {sorted(omitted_declarations)}")

    selected_records = [available[key] for key in selected_keys]
    _validate_claim_evidence_closure(selected_records, selected_set)
    base_manifest = build_offline_edition(selected_records, output_dir, edition_id)
    manifest_path = output_dir / "edition-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({
        "build_mode": "selection",
        "selection_schema_version": selection["schema_version"],
        "selection_manifest_sha256": _digest(selection),
        "source_commit": source_commit,
        "builder_version": "0.1.0",
        "selected_records": [
            {"record_id": rid, "record_version": version}
            for rid, version in sorted(selected_keys)
        ],
        "selected_record_count": len(selected_keys),
    })
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest
