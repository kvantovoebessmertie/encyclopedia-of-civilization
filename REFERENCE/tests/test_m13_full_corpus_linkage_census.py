from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "CONTENT" / "vertical-slices"


def _records():
    rows = []
    for path in sorted(CONTENT.glob("*/records/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        rows.append((path, data))
    return rows


def _walk_refs(value, trail="$"):
    """Yield schema-shaped local record references without guessing from filenames."""
    if isinstance(value, dict):
        if (
            isinstance(value.get("record_id"), str)
            and set(value).issubset({"record_id", "version"})
            and value.get("record_id")
        ):
            yield trail, value
            return
        for key, child in value.items():
            yield from _walk_refs(child, f"{trail}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk_refs(child, f"{trail}[{index}]")


def _census():
    rows = _records()
    by_id = defaultdict(list)
    slice_counts = Counter()
    type_counts = Counter()
    for path, record in rows:
        by_id[str(record.get("record_id", ""))].append(str(record.get("record_version", "")))
        slice_counts[path.parent.parent.name] += 1
        type_counts[str(record.get("record_type", "<missing>"))] += 1

    duplicate_ids = {
        record_id: versions
        for record_id, versions in by_id.items()
        if not record_id or len(versions) != len(set(versions))
    }
    unresolved = []
    ref_count = 0
    claim_ids = {
        str(r.get("record_id")) for _, r in rows if r.get("record_type") == "claim"
    }
    evidence_rows = [
        (p, r) for p, r in rows if r.get("record_type") == "evidence_use"
    ]
    linked_claims = set()
    evidence_without_claim = []
    evidence_without_source = []
    evidence_links = []

    for path, record in rows:
        root_id = record.get("record_id")
        # Inspect all actual record reference shapes in metadata and content.
        for area in ("provenance", "content", "scope", "context"):
            if area not in record:
                continue
            for trail, ref in _walk_refs(record[area], area):
                ref_count += 1
                target_id = ref["record_id"]
                versions = by_id.get(target_id, [])
                requested_version = ref.get("version")
                if not versions:
                    unresolved.append({
                        "source": str(path.relative_to(ROOT)),
                        "source_id": root_id,
                        "path": trail,
                        "target_id": target_id,
                        "target_version": requested_version,
                        "issue": "missing_record_id",
                    })
                elif requested_version is not None and str(requested_version) not in versions:
                    unresolved.append({
                        "source": str(path.relative_to(ROOT)),
                        "source_id": root_id,
                        "path": trail,
                        "target_id": target_id,
                        "target_version": requested_version,
                        "available_versions": versions,
                        "issue": "missing_record_version",
                    })

    for path, record in evidence_rows:
        c = record.get("content", {})
        claim_ref = c.get("claim_ref", {}) if isinstance(c, dict) else {}
        source_ref = c.get("source_ref", {}) if isinstance(c, dict) else {}
        claim_id = claim_ref.get("record_id") if isinstance(claim_ref, dict) else None
        source_id = source_ref.get("record_id") if isinstance(source_ref, dict) else None
        if claim_id in claim_ids:
            linked_claims.add(claim_id)
        else:
            evidence_without_claim.append({
                "file": str(path.relative_to(ROOT)),
                "evidence_use_id": record.get("record_id"),
                "claim_ref": claim_id,
            })
        if source_id not in by_id or not any(
            r.get("record_type") == "source" and r.get("record_id") == source_id
            for _, r in rows
        ):
            evidence_without_source.append({
                "file": str(path.relative_to(ROOT)),
                "evidence_use_id": record.get("record_id"),
                "source_ref": source_id,
            })
        evidence_links.append({
            "evidence_use_id": record.get("record_id"),
            "claim_id": claim_id,
            "source_id": source_id,
            "evidence_role": c.get("evidence_role") if isinstance(c, dict) else None,
            "slice": path.parent.parent.name,
        })

    claims_without_evidence = sorted(claim_ids - linked_claims)
    return {
        "records": len(rows),
        "slices": len(slice_counts),
        "record_types": dict(sorted(type_counts.items())),
        "local_reference_objects": ref_count,
        "duplicate_or_empty_record_identity_groups": duplicate_ids,
        "unresolved_reference_count": len(unresolved),
        "unresolved_references": unresolved,
        "claims": len(claim_ids),
        "evidence_use_records": len(evidence_rows),
        "claims_with_evidence_use": len(linked_claims),
        "claims_without_evidence_use": claims_without_evidence,
        "evidence_use_without_valid_claim": evidence_without_claim,
        "evidence_use_without_source_record": evidence_without_source,
        "evidence_links": evidence_links,
    }


def test_m13_full_corpus_linkage_census_has_no_dangling_record_refs():
    report = _census()
    # Keep the full actionable finding set in the assertion output if this audit gate fails.
    assert report["records"] > 0 and report["slices"] > 0, json.dumps(report, ensure_ascii=False)
    assert not report["duplicate_or_empty_record_identity_groups"], json.dumps(
        report["duplicate_or_empty_record_identity_groups"], ensure_ascii=False, indent=2
    )
    assert not report["unresolved_references"], json.dumps(
        {
            "summary": {
                "records": report["records"],
                "slices": report["slices"],
                "local_reference_objects": report["local_reference_objects"],
                "unresolved_reference_count": report["unresolved_reference_count"],
            },
            "findings": report["unresolved_references"],
        },
        ensure_ascii=False,
        indent=2,
    )
    assert not report["claims_without_evidence_use"], json.dumps(
        report["claims_without_evidence_use"], ensure_ascii=False, indent=2
    )
    assert not report["evidence_use_without_valid_claim"], json.dumps(
        report["evidence_use_without_valid_claim"], ensure_ascii=False, indent=2
    )
    assert not report["evidence_use_without_source_record"], json.dumps(
        report["evidence_use_without_source_record"], ensure_ascii=False, indent=2
    )
