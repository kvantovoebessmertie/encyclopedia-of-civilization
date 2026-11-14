from __future__ import annotations

"""Deterministic M13 triage orchestrator.

Runs existing inventory, linkage and scored-ledger generators, then creates a
non-overlapping review queue. Machine signals only route work; they never assign
D/E/B scores or edit canonical records.
"""

import argparse
import csv
import json
import re
import subprocess
import sys
import tempfile
import time
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


def build_runtime_metrics(stage_seconds: dict[str, float], total_seconds: float, source_revision: str) -> dict:
    """Describe reproducible machine runtime without implying human-review speedup."""
    return {
        "schema_version": "1.0",
        "source_revision": source_revision,
        "runtime_seconds_by_stage": {key: round(max(0.0, value), 3) for key, value in stage_seconds.items()},
        "pipeline_elapsed_seconds": round(max(0.0, total_seconds), 3),
        "human_review_time_measured": False,
        "manual_baseline_available": False,
        "speedup_claim_authorized": False,
        "interpretation": "Machine runtime measures queue preparation only. It is not human review time and cannot establish a speedup without a comparable baseline and measured reviewer effort.",
    }


def _finding_priority(
    findings: list[dict],
    claim_to_evidence: dict[str, set[str]],
    claim_to_sources: dict[str, set[str]] | None = None,
) -> dict[str, int]:
    """Propagate structural findings from Claim, linked Evidence Use, or linked Source."""
    rank = {"high": 3, "medium": 2, "low": 1}
    priority: dict[str, int] = defaultdict(int)
    record_to_claims: dict[str, set[str]] = defaultdict(set)
    for claim_id, evidence_ids in claim_to_evidence.items():
        record_to_claims[claim_id].add(claim_id)
        for evidence_id in evidence_ids:
            record_to_claims[evidence_id].add(claim_id)
    for claim_id, source_ids in (claim_to_sources or {}).items():
        for source_id in source_ids:
            record_to_claims[source_id].add(claim_id)
    for finding in findings:
        record_id = str(finding.get("record_id", ""))
        severity = rank.get(str(finding.get("severity", "")).lower(), 0)
        for claim_id in record_to_claims.get(record_id, set()):
            priority[claim_id] = max(priority[claim_id], severity)
    return priority


def build_evidence_packets(
    selected_claims: list[dict],
    worksheet_claims: list[dict],
    findings: list[dict],
) -> dict:
    """Create reviewer packets from local records only; never fetch or invent source text."""
    by_id = {str(row.get("record_id", "")): row for row in worksheet_claims}
    packets = []
    for selected in selected_claims:
        claim = by_id.get(str(selected.get("record_id", "")), {})
        evidence_items = claim.get("evidence_items") or []
        linked_ids = set(selected.get("evidence_use_ids") or [])
        source_ids = set(selected.get("source_ids") or [])
        associated = [
            finding for finding in findings
            if str(finding.get("record_id", "")) == str(selected.get("record_id", ""))
            or str(finding.get("record_id", "")) in linked_ids
            or str(finding.get("record_id", "")) in source_ids
        ]
        evidence = []
        for item in evidence_items:
            source_uri = item.get("source_uri")
            material = str(item.get("evidence_material") or "").strip()
            evidence.append({
                "evidence_use_id": item.get("evidence_use_id"),
                "evidence_role": item.get("evidence_role"),
                "evidence_material": material,
                "source_id": item.get("source_id"),
                "source_record_version": item.get("source_record_version"),
                "source_identity": item.get("source_identity"),
                "source_external_ref": item.get("source_external_ref"),
                "source_uri": source_uri,
                "source_representation": item.get("source_representation"),
                "pinpoint_status": "HUMAN_VERIFICATION_REQUIRED",
                "review_flags": [
                    flag for condition, flag in (
                        (not item.get("source_id"), "missing_source_link"),
                        (not source_uri, "source_uri_not_recorded"),
                        (not material, "evidence_material_missing"),
                    ) if condition
                ],
            })
        packets.append({
            "claim_id": selected.get("record_id"),
            "record_version": selected.get("record_version"),
            "slice": selected.get("slice"),
            "claim_file": selected.get("file"),
            "claim_statement": claim.get("statement"),
            "risk_domains": selected.get("risk_domains") or [],
            "machine_triage_flags": selected.get("machine_triage_flags") or [],
            "risk_triage_status": selected.get("risk_triage_status") or ("UNASSESSED" if not (selected.get("risk_domains") or selected.get("machine_triage_flags")) else "FLAGGED_FOR_REVIEW"),
            "structural_finding_priority": selected.get("structural_finding_priority", 0),
            "associated_structural_findings": associated,
            "evidence_use_count_expected": len(linked_ids),
            "evidence_items": evidence,
            "linkage_review": {
                "claim_to_evidence_use": "VERIFY_IN_SOURCE_RECORDS",
                "evidence_use_to_source": "VERIFY_IN_SOURCE_RECORDS",
                "source_identity_and_version": "HUMAN_VERIFICATION_REQUIRED",
                "source_passage_pinpoint": "HUMAN_VERIFICATION_REQUIRED",
                "source_access_and_rights": "HUMAN_VERIFICATION_REQUIRED",
                "contradictory_or_independent_evidence": "HUMAN_ADJUDICATION_REQUIRED",
            },
            "D_score": None,
            "E_score": None,
            "B_score": None,
            "review_status": "NOT_YET_REVIEWED",
        })
    return {
        "protocol": "Reviewer evidence packets assembled from repository-local record fields only",
        "packet_count": len(packets),
        "source_text_fetched": False,
        "scores_assigned": False,
        "canonical_records_modified": False,
        "limitations": [
            "A URI or source identity is not proof that the source passage supports the Claim.",
            "No external page text, quotation, page number, section, or locator is inferred.",
            "Human reviewers must verify the exact source edition, pinpoint, context, rights, independence, and contradictions.",
            "Structural flags are triage signals, not final evidence judgements.",
        ],
        "packets": packets,
    }


def write_unassessed_queue_csv(path: Path, claims: list[dict]) -> None:
    """Write the complete unassessed-risk screening queue as a stable CSV."""
    fields = [
        "record_id", "record_version", "slice", "file",
        "evidence_use_ids", "source_ids", "risk_triage_status",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for claim in claims:
            writer.writerow({
                **claim,
                "evidence_use_ids": ";".join(claim["evidence_use_ids"]),
                "source_ids": ";".join(claim["source_ids"]),
            })



REVIEW_HOLDOUT_SLICE_PREFIXES = (
    "disaster-response",
    "disaster-risk-reduction",
    "hydropower",
    "industrial-safety",
    "public-health-surveillance",
    "safety-engineering",
    "infrastructure-resilience",
)

REVIEWED_RISK_REPORT_PATTERNS = (
    "M13-UNASSESSED-RISK-PRELIMINARY-SCREEN-2026-11-14.md",
    "M13-UNASSESSED-RISK-SECOND-SCREEN-2026-11-14.md",
    "M13-UNASSESSED-RISK-CONTENT-SCREEN-PACKAGE-*.md",
    "M13-BATCH-53-LANE-*-CONTENT-RISK-SCREEN*.md",
    "M13-CLAIM-REVIEW-BATCH-53*.md",
    "M13-CLAIM-REVIEW-BATCH-54*.md",
    "M13-POST-BATCH-53-UNSCORED-QUEUE-RISK-SCREEN-2026-11-12.md",
)


def _report_mentions_claim_id(record_id: str, report_text: str) -> bool:
    """Match exact IDs and compact grouped forms such as CLM-FOO-A/B/C."""
    exact = re.search(
        rf"(?<![A-Z0-9_-]){re.escape(record_id)}(?![A-Z0-9_-])",
        report_text,
    )
    if exact:
        return True
    if "-" not in record_id:
        return False
    prefix, suffix = record_id.rsplit("-", 1)
    grouped = re.compile(
        rf"(?<![A-Z0-9_-]){re.escape(prefix)}-([A-Z0-9]+(?:/[A-Z0-9]+)*)(?![A-Z0-9_-])"
    )
    return any(suffix in match.group(1).split("/") for match in grouped.finditer(report_text))


def collect_previously_screened_claim_ids(
    claims: list[dict],
    release_dir: Path | None = None,
) -> set[str]:
    """Collect explicit prior risk-screen IDs from auditable M13 review reports."""
    release = release_dir or (ROOT / "RELEASE")
    report_paths: set[Path] = set()
    for pattern in REVIEWED_RISK_REPORT_PATTERNS:
        report_paths.update(release.glob(pattern))
    report_texts = [
        path.read_text(encoding="utf-8")
        for path in sorted(report_paths)
        if path.is_file()
    ]
    reviewed: set[str] = set()
    for claim in claims:
        claim_id = str(claim.get("record_id", ""))
        if claim_id and any(_report_mentions_claim_id(claim_id, text) for text in report_texts):
            reviewed.add(claim_id)
    return reviewed


def build_lanes(
    claims: list[dict],
    scored_paths: set[str],
    findings: list[dict],
    batch_size: int = 100,
    lane_count: int = 5,
    reviewed_claim_ids: set[str] | None = None,
    holdout_slice_prefixes: tuple[str, ...] = REVIEW_HOLDOUT_SLICE_PREFIXES,
) -> dict:
    if batch_size < 1 or lane_count < 1 or batch_size % lane_count:
        raise ValueError("batch_size must be positive and evenly divisible by lane_count")

    claim_to_evidence = {
        str(claim.get("record_id", "")): set(claim.get("evidence_use_ids") or [])
        for claim in claims
    }
    claim_to_sources = {
        str(claim.get("record_id", "")): set(claim.get("source_ids") or [])
        for claim in claims
    }
    finding_priority = _finding_priority(findings, claim_to_evidence, claim_to_sources)
    risk_signal_claims = [c for c in claims if (c.get("risk_domains") or c.get("machine_triage_flags"))]
    high_consequence_claims = [c for c in claims if "high_consequence_screen" in (c.get("machine_triage_flags") or [])]
    risk_triage_coverage = {
        "claims_in_inventory": len(claims),
        "claims_with_any_risk_signal": len(risk_signal_claims),
        "claims_with_high_consequence_screen": len(high_consequence_claims),
        "claims_without_recorded_risk_signal": len(claims) - len(risk_signal_claims),
    }
    risk_triage_warning = (
        "Absence of risk_domains or machine_triage_flags does not establish low risk; these Claims remain UNASSESSED by the queue."
        if len(risk_signal_claims) < len(claims) else None
    )
    unassessed_claims = [
        {
            "record_id": str(row.get("record_id", "")),
            "record_version": str(row.get("record_version", "")),
            "slice": str(row.get("slice", "")),
            "file": str(row.get("file", "")),
            "evidence_use_ids": sorted(row.get("evidence_use_ids") or []),
            "source_ids": sorted(row.get("source_ids") or []),
            "risk_triage_status": "UNASSESSED",
        }
        for row in sorted(
            (c for c in claims if not (c.get("risk_domains") or c.get("machine_triage_flags"))),
            key=lambda item: (str(item.get("slice", "")), str(item.get("record_id", ""))),
        )
    ]
    # This queue is specifically for Claims with no recorded risk-domain or
    # machine-triage signal. A historical D/E/B ledger match is orthogonal:
    # it must not remove a Claim from risk triage. The scored_paths argument
    # is retained for API compatibility and deliberately does not filter here.
    reviewed_ids = reviewed_claim_ids or set()
    unassessed_claims_for_selection = [
        c for c in claims if not (c.get("risk_domains") or c.get("machine_triage_flags"))
    ]
    holdout_claims = [
        c for c in unassessed_claims_for_selection
        if any(str(c.get("slice", "")).startswith(prefix) for prefix in holdout_slice_prefixes)
    ]
    candidates = [
        c for c in unassessed_claims_for_selection
        if str(c.get("record_id", "")) not in reviewed_ids
        and not any(str(c.get("slice", "")).startswith(prefix) for prefix in holdout_slice_prefixes)
    ]
    # All candidates are UNASSESSED. Exclude exact IDs already covered by prior
    # human review reports and hold topic families containing unreconciled
    # historical observations. Route structural findings first; stable ties.
    candidates.sort(key=lambda c: (
        -finding_priority.get(str(c.get("record_id", "")), 0),
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
                "risk_triage_status": "UNASSESSED" if not (row.get("risk_domains") or row.get("machine_triage_flags")) else "FLAGGED_FOR_REVIEW",
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
        "candidate_unassessed_risk_claims": len(candidates),
        "previously_screened_claims_excluded": len(reviewed_ids & {str(c.get("record_id", "")) for c in unassessed_claims_for_selection}),
        "unreconciled_holdout_claims_excluded": len(holdout_claims),
        "selected_claims": len(selected),
        "unfilled_slots": batch_size - len(selected),
        "unique_selected_claim_ids": len(set(all_ids)),
        "lane_counts": {str(lane["lane"]): lane["claim_count"] for lane in lanes},
        "selection_order": "unassessed risk-metadata state, associated structural finding severity, slice, Claim ID",
        "risk_triage_coverage": risk_triage_coverage,
        "risk_triage_warning": risk_triage_warning,
        "unassessed_claims": unassessed_claims,
        "unassessed_claim_ids": [row["record_id"] for row in unassessed_claims],
        "previously_screened_claim_ids_excluded": sorted(reviewed_ids & {str(c.get("record_id", "")) for c in unassessed_claims_for_selection}),
        "unreconciled_holdout_claim_ids_excluded": sorted(str(c.get("record_id", "")) for c in holdout_claims),
        "interpretation": "Risk/finding flags are routing signals only. The unassessed_claims list is an explicit screening queue, not a low-risk designation. Prior score-ledger matches are excluded from the scoring queue but are not certified as valid final assessments. Reviewers must verify Claim → Evidence Use → Source/pinpoint and independently adjudicate D/E/B.",
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
    pipeline_started = time.perf_counter()
    stage_seconds: dict[str, float] = {}

    with tempfile.TemporaryDirectory(prefix="m13-pipeline-") as tmp:
        temp = Path(tmp)
        worksheet_dir, linkage_dir, ledger_dir = (temp / "worksheet", temp / "linkage", temp / "ledger")
        for stage, script, stage_dir in (
            ("inventory", "m13_claim_audit_inventory.py", worksheet_dir),
            ("evidence_linkage", "m13_evidence_linkage_audit.py", linkage_dir),
            ("scored_ledger_reconciliation", "m13_claim_scored_report_ledger.py", ledger_dir),
        ):
            started = time.perf_counter()
            run_generator(script, stage_dir)
            stage_seconds[stage] = time.perf_counter() - started

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
        assembly_started = time.perf_counter()
        reviewed_claim_ids = collect_previously_screened_claim_ids(worksheet.get("claims", []))
        queue = build_lanes(
            worksheet.get("claims", []), scored_paths, findings, args.batch_size, args.lanes,
            reviewed_claim_ids=reviewed_claim_ids,
        )
        selected_claims = [claim for lane in queue["lanes"] for claim in lane["claims"]]
        evidence_packets = build_evidence_packets(selected_claims, worksheet.get("claims", []), findings)
        stage_seconds["queue_and_evidence_packet_assembly"] = time.perf_counter() - assembly_started
        (output / "m13-review-evidence-packets.json").write_text(
            json.dumps(evidence_packets, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8"
        )

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
                  "source_ids", "risk_domains", "machine_triage_flags", "risk_triage_status", "structural_finding_priority",
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

        unassessed_csv_path = output / "m13-unassessed-risk-screening.csv"
        write_unassessed_queue_csv(unassessed_csv_path, queue["unassessed_claims"])

        runtime_metrics = build_runtime_metrics(stage_seconds, time.perf_counter() - pipeline_started, summary["source_revision"])
        (output / "m13-runtime-metrics.json").write_text(
            json.dumps(runtime_metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(json.dumps({
            "source_revision": summary["source_revision"],
            "claims_inventoried": summary["claims_inventoried"],
            "claims_without_scored_report_match": summary["claims_without_scored_report_match"],
            "previously_screened_claims_excluded": queue["previously_screened_claims_excluded"],
            "unreconciled_holdout_claims_excluded": queue["unreconciled_holdout_claims_excluded"],
            "structural_finding_rows": summary["structural_finding_rows"],
            "selected_claims": queue["selected_claims"],
            "lane_counts": queue["lane_counts"],
            "json": str(output / "m13-automation-queue.json"),
            "csv": str(csv_path),
            "unassessed_risk_csv": str(unassessed_csv_path),
            "unassessed_claim_count": len(queue["unassessed_claims"]),
            "evidence_packets": str(output / "m13-review-evidence-packets.json"),
            "evidence_packet_count": evidence_packets["packet_count"],
            "runtime_metrics": str(output / "m13-runtime-metrics.json"),
            "pipeline_elapsed_seconds": runtime_metrics["pipeline_elapsed_seconds"],
            "human_review_time_measured": False,
            "speedup_claim_authorized": False,
            "canonical_records_modified": False,
            "automated_D_E_B_scores": False,
        }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
