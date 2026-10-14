from __future__ import annotations

"""Deterministic M13 triage orchestrator.

Runs existing inventory, linkage and scored-ledger generators, then creates a
non-overlapping review queue. Machine signals only route work; they never assign
D/E/B scores or edit canonical records.
"""

import argparse
import csv
import json
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "REFERENCE"


def run_generator(script: str, output_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(REFERENCE / script), "--output-dir", str(output_dir)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def _finding_priority(findings: list[dict], claim_to_evidence: dict[str, set[str]]) -> dict[str, int]:
    """Map Claim IDs to the strongest associated structural finding severity."""
    rank = {"high": 3, "medium": 2, "low": 1}
    priority: dict[str, int] = defaultdict(int)
    evidence_to_claim = {
        evidence_id: claim_id
        for claim_id, evidence_ids in claim_to_evidence.items()
        for evidence_id in evidence_ids
    }
    for finding in findings:
        record_id = str(finding.get("record_id", ""))
        claim_id = record_id if record_id in claim_to_evidence else evidence_to_claim.get(record_id)
        if claim_id:
            priority[claim_id] = max(priority[claim_id], rank.get(str(finding.get("severity", "")).lower(), 0))
    return priority


def build_lanes(
    claims: list[dict],
    scored_paths: set[str],
    findings: list[dict],
    batch_size: int = 100,
    lane_count: int = 5,
) -> dict:
    if batch_size < 1 or lane_count < 1 or batch_size % lane_count:
        raise ValueError("batch_size must be positive and evenly divisible by lane_count")

    claim_to_evidence = {
        str(claim.get("record_id", "")): set(claim.get("evidence_use_ids") or [])
        for claim in claims
    }
    finding_priority = _finding_priority(findings, claim_to_evidence)
    candidates = [c for c in claims if str(c.get("file", "")) not in scored_paths]
    # Risk flags are routing signals only. Tie-breaks are stable and reproducible.
    candidates.sort(key=lambda c: (
        0 if "high_consequence_screen" in (c.get("machine_triage_flags") or []) else 1,
        -finding_priority.get(str(c.get("record_id", "")), 0),
        -len(c.get("machine_triage_flags") or []),
        str(c.get("slice", "")),
        str(c.get("record_id", "")),
    ))
    selected = candidates[:batch_size]
    lane_size = batch_size // lane_count
    lanes = []
    for index in range(lane_count):
        rows = selected[index * lane_size:(index + 1) * lane_size]
        lanes.append({
            "lane": index + 1,
            "capacity": lane_size,
            "claim_count": len(rows),
            "claims": [{
                "record_id": str(row.get("record_id", "")),
                "record_version": str(row.get("record_version", "")),
                "slice": str(row.get("slice", "")),
                "file": str(row.get("file", "")),
                "evidence_use_ids": sorted(row.get("evidence_use_ids") or []),
                "source_ids": sorted(row.get("source_ids") or []),
                "risk_domains": sorted(row.get("risk_domains") or []),
                "machine_triage_flags": sorted(row.get("machine_triage_flags") or []),
                "structural_finding_priority": finding_priority.get(str(row.get("record_id", "")), 0),
                "review_status": "NOT_YET_REVIEWED",
                "D_score": None,
                "E_score": None,
                "B_score": None,
            } for row in rows],
        })
    all_ids = [c["record_id"] for lane in lanes for c in lane["claims"]]
    if len(all_ids) != len(set(all_ids)):
        raise AssertionError("Queue partition produced duplicate Claim IDs")
    return {
        "protocol": "M13 deterministic triage queue; no automated scoring or canonical edits",
        "batch_size_requested": batch_size,
        "lane_count": lane_count,
        "lane_size": lane_size,
        "candidate_claims_without_scored_report_match": len(candidates),
        "selected_claims": len(selected),
        "unfilled_slots": batch_size - len(selected),
        "unique_selected_claim_ids": len(set(all_ids)),
        "lane_counts": {str(lane["lane"]): lane["claim_count"] for lane in lanes},
        "selection_order": "high-consequence screen, associated structural finding severity, triage-flag count, slice, Claim ID",
        "interpretation": "Risk/finding flags are routing signals only. Prior score-ledger matches are excluded from this queue but are not certified as valid final assessments. Reviewers must verify Claim → Evidence Use → Source/pinpoint and independently adjudicate D/E/B.",
        "lanes": lanes,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default=str(ROOT / "RELEASE" / "m13-automation-run"))
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--lanes", type=int, default=5)
    args = parser.parse_args()
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="m13-pipeline-") as tmp:
        temp = Path(tmp)
        worksheet_dir, linkage_dir, ledger_dir = (temp / "worksheet", temp / "linkage", temp / "ledger")
        run_generator("m13_claim_audit_inventory.py", worksheet_dir)
        run_generator("m13_evidence_linkage_audit.py", linkage_dir)
        run_generator("m13_claim_scored_report_ledger.py", ledger_dir)

        worksheet = json.loads((worksheet_dir / "M13-CLAIM-AUDIT-WORKSHEET.json").read_text(encoding="utf-8"))
        ledger = json.loads((ledger_dir / "reconciliation-summary.json").read_text(encoding="utf-8"))
        with (linkage_dir / "evidence-linkage-findings.csv").open(encoding="utf-8-sig", newline="") as handle:
            findings = list(csv.DictReader(handle))
        unscored_paths = {
            str(row.get("path", ""))
            for row in ledger.get("inventory_claims_without_scored_rows", [])
        }
        all_claim_paths = {str(row.get("file", "")) for row in worksheet.get("claims", [])}
        scored_paths = all_claim_paths - unscored_paths
        queue = build_lanes(worksheet.get("claims", []), scored_paths, findings, args.batch_size, args.lanes)

        summary = {
            "source_revision": worksheet.get("source_revision", "unknown"),
            "records_scanned": worksheet.get("records_scanned"),
            "claims_inventoried": worksheet.get("claim_count"),
            "scored_report_rows": ledger.get("scored_report_rows"),
            "claims_without_scored_report_match": len(unscored_paths),
            "structural_finding_rows": len(findings),
            "structural_findings_by_severity": dict(Counter(row.get("severity", "unknown") for row in findings)),
            "queue": queue,
            "guardrails": [
                "No canonical record files are written or modified.",
                "No D/E/B score is generated by this pipeline.",
                "Historical score matches are not treated as proof of score validity.",
                "Identifier normalization is comparison-only; stored IDs are not rewritten.",
                "Human source-passage review, rights, specialist, Human View and editorial gates remain mandatory.",
            ],
        }
        (output / "m13-automation-queue.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        csv_path = output / "m13-automation-queue.csv"
        fields = ["lane", "record_id", "record_version", "slice", "file", "evidence_use_ids",
                  "source_ids", "risk_domains", "machine_triage_flags", "structural_finding_priority",
                  "review_status", "D_score", "E_score", "B_score"]
        with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for lane in queue["lanes"]:
                for claim in lane["claims"]:
                    writer.writerow({**claim, "lane": lane["lane"],
                                     "evidence_use_ids": ";".join(claim["evidence_use_ids"]),
                                     "source_ids": ";".join(claim["source_ids"]),
                                     "risk_domains": ";".join(claim["risk_domains"]),
                                     "machine_triage_flags": ";".join(claim["machine_triage_flags"])})
        print(json.dumps({
            "source_revision": summary["source_revision"],
            "claims_inventoried": summary["claims_inventoried"],
            "claims_without_scored_report_match": summary["claims_without_scored_report_match"],
            "structural_finding_rows": summary["structural_finding_rows"],
            "selected_claims": queue["selected_claims"],
            "lane_counts": queue["lane_counts"],
            "json": str(output / "m13-automation-queue.json"),
            "csv": str(csv_path),
            "canonical_records_modified": False,
            "automated_D_E_B_scores": False,
        }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
