#!/usr/bin/env python3
"""Reconcile generic Evidence Use candidates against existing M13 report mentions.

This is a routing aid, not proof that a Claim received a complete source-passage
review. Every reported match requires human confirmation of scope and quality.
The inputs are the CSV files emitted by the M13 claim-audit and evidence-linkage
workflow artifacts.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


SOURCE_REVIEW_HINTS = (
    "SOURCE-PASSAGE",
    "SOURCE-PINPOINT",
    "EVIDENCE-LOCATOR",
    "GENERIC-EU",
    "SOURCE-IDENTITY",
    "SOURCE-FIT",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def split_ids(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(";") if item.strip()]


def exact_id_pattern(record_id: str) -> re.Pattern[str]:
    # Claim IDs contain hyphens and underscores; do not match a longer ID
    # that merely begins with the same text.
    return re.compile(
        rf"(?<![A-Z0-9_-]){re.escape(record_id)}(?![A-Z0-9_-])"
    )


def build_coverage(
    findings_csv: Path,
    worksheet_csv: Path,
    release_dir: Path,
) -> dict[str, Any]:
    findings = read_csv(findings_csv)
    worksheet = read_csv(worksheet_csv)

    eu_to_claim: dict[str, dict[str, str]] = {}
    for row in worksheet:
        for eu_id in split_ids(row.get("evidence_use_ids")):
            eu_to_claim[eu_id] = {
                "claim_id": row.get("record_id", ""),
                "source_ids": row.get("source_ids", ""),
                "slice": row.get("slice", ""),
            }

    report_files = sorted(
        path for path in release_dir.glob("M13*.md") if path.is_file()
    )
    report_text = {
        path.name: path.read_text(encoding="utf-8")
        for path in report_files
    }

    candidates: list[dict[str, Any]] = []
    unmapped_eus: list[str] = []
    for finding in findings:
        if (
            finding.get("finding") != "generic_material_description"
            or finding.get("record_type") != "evidence_use"
        ):
            continue

        eu_id = finding.get("record_id", "")
        mapped = eu_to_claim.get(eu_id)
        if not mapped or not mapped["claim_id"]:
            unmapped_eus.append(eu_id)
            continue

        claim_id = mapped["claim_id"]
        pattern = exact_id_pattern(claim_id)
        mentions = [
            name for name, body in report_text.items() if pattern.search(body)
        ]
        source_review_mentions = [
            name
            for name in mentions
            if any(hint in name.upper() for hint in SOURCE_REVIEW_HINTS)
        ]

        candidates.append(
            {
                "claim_id": claim_id,
                "evidence_use_id": eu_id,
                "source_ids": split_ids(mapped.get("source_ids")),
                "slice": mapped.get("slice", ""),
                "path": finding.get("path", ""),
                "all_report_mentions": mentions,
                "source_review_report_mentions": source_review_mentions,
                "human_confirmation_required": True,
            }
        )

    candidates.sort(key=lambda item: (item["slice"], item["claim_id"], item["evidence_use_id"]))
    mentioned = sum(bool(item["all_report_mentions"]) for item in candidates)
    source_mentioned = sum(bool(item["source_review_report_mentions"]) for item in candidates)

    return {
        "method": "exact Claim-ID text mention scan; not semantic review verification",
        "generic_evidence_use_candidates": len(candidates) + len(unmapped_eus),
        "mapped_candidates": len(candidates),
        "unmapped_evidence_use_ids": sorted(unmapped_eus),
        "candidates_with_any_m13_report_mention": mentioned,
        "candidates_with_source_review_filename_mention": source_mentioned,
        "candidates_without_any_report_mention": len(candidates) - mentioned,
        "candidates": candidates,
        "limitations": [
            "A text mention is not proof that the report reviewed the exact Claim version or its full Claim-to-EU-to-Source chain.",
            "A report may mention a Claim in a handoff, duplicate check, or exclusion note rather than a substantive passage review.",
            "No report mention does not prove that no review occurred outside the scanned M13 Markdown files.",
            "The tool does not fetch sources, assess passage support, assign D/E/B, modify canonical records, or authorize remediation.",
            "Every candidate requires human confirmation before it is counted as reviewed.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--findings-csv", required=True, type=Path)
    parser.add_argument("--worksheet-csv", required=True, type=Path)
    parser.add_argument("--release-dir", type=Path, default=Path("RELEASE"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = build_coverage(args.findings_csv, args.worksheet_csv, args.release_dir)
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
