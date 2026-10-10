from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
GENERIC_PATTERNS = (
    "используется для представления утверждения без вывода за пределы указанного материала",
    "используется в пределах заявленного контекста и ограничений",
    "связанный источник используется для представления утверждения без вывода за пределы указанного материала",
    "source is used within the stated context and limitations",
    "source is used to represent the claim without going beyond the stated material",
)


def normalize_id(value: str) -> str:
    return re.sub(r"[-_]", "", value).casefold()


def load_records():
    records = []
    for path in sorted(CONTENT.glob("*/records/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            records.append({
                "path": str(path.relative_to(ROOT)),
                "record_id": "",
                "record_type": "INVALID_JSON",
                "data": {},
                "error": str(exc),
            })
            continue
        records.append({
            "path": str(path.relative_to(ROOT)),
            "record_id": str(data.get("record_id", "")),
            "record_type": str(data.get("record_type", "")),
            "data": data,
            "error": "",
        })
    return records


def audit_records(records):
    by_id = {}
    for record in records:
        if record["record_id"]:
            by_id.setdefault(record["record_id"], []).append(record)
    findings = []
    for record in records:
        data = record["data"]
        path = record["path"]
        record_id = record["record_id"]
        if record["error"]:
            findings.append({ "path": path, "record_id": record_id, "record_type": record["record_type"], "finding": "invalid_json", "severity": "high", "detail": record["error"] })
            continue
        filename_id = Path(path).stem
        if filename_id != record_id:
            kind = "separator_only_filename_id_alias" if normalize_id(filename_id) == normalize_id(record_id) else "filename_internal_id_mismatch"
            findings.append({ "path": path, "record_id": record_id, "record_type": record["record_type"], "finding": kind, "severity": "medium" if kind == "separator_only_filename_id_alias" else "high", "detail": f"filename_id={filename_id}; internal_id={record_id}" })
        if record["record_type"] != "evidence_use":
            continue
        content = data.get("content") if isinstance(data.get("content"), dict) else {}
        claim_ref = content.get("claim_ref") if isinstance(content.get("claim_ref"), dict) else {}
        source_ref = content.get("source_ref") if isinstance(content.get("source_ref"), dict) else {}
        claim_id = str(claim_ref.get("record_id", ""))
        source_id = str(source_ref.get("record_id", ""))
        if not claim_id:
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"missing_claim_ref","severity":"high","detail":"content.claim_ref.record_id is absent"})
        elif claim_id not in by_id:
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"unresolved_claim_ref","severity":"high","detail":f"claim_ref={claim_id}"})
        elif not any(x["record_type"] == "claim" for x in by_id[claim_id]):
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"claim_ref_wrong_record_type","severity":"high","detail":f"claim_ref={claim_id} resolves but not to a Claim record"})
        if not source_id:
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"missing_source_ref","severity":"high","detail":"content.source_ref.record_id is absent"})
        elif source_id not in by_id:
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"unresolved_source_ref","severity":"high","detail":f"source_ref={source_id}"})
        elif not any(x["record_type"] == "source" for x in by_id[source_id]):
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"source_ref_wrong_record_type","severity":"high","detail":f"source_ref={source_id} resolves but not to a Source record"})
        role = content.get("evidence_role")
        if role not in {"supports", "contradicts"}:
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"invalid_or_missing_evidence_role","severity":"high","detail":f"evidence_role={role!r}"})
        material = content.get("material") if isinstance(content.get("material"), dict) else {}
        description = str(material.get("description", "")).strip()
        if not description:
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"missing_material_description","severity":"high","detail":"content.material.description is absent or empty"})
        elif any(pattern in description.casefold() for pattern in GENERIC_PATTERNS):
            findings.append({"path":path,"record_id":record_id,"record_type":"evidence_use","finding":"generic_material_description","severity":"medium","detail":description})
    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(ROOT / "RELEASE" / "m13-evidence-linkage-audit"))
    args = parser.parse_args()
    records = load_records()
    findings = audit_records(records)
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    with (out / "evidence-linkage-findings.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        fields = ["path", "record_id", "record_type", "finding", "severity", "detail"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(findings)
    counts = Counter(f["finding"] for f in findings)
    summary = {
        "record_files_seen": len(records),
        "valid_record_files": sum(not r["error"] for r in records),
        "claim_records": sum(r["record_type"] == "claim" for r in records),
        "evidence_use_records": sum(r["record_type"] == "evidence_use" for r in records),
        "finding_rows": len(findings),
        "findings_by_type": dict(sorted(counts.items())),
        "warning": "Static structural triage only. Generic descriptions are flags for human review, not automatic proof that evidence is invalid. No records are changed.",
    }
    (out / "evidence-linkage-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
