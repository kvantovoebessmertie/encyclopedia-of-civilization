from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "CONTENT" / "vertical-slices"
RELEASE = ROOT / "RELEASE"
ROW = re.compile(r"^\|\s*`([^\`]+)`\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*$")
BATCH = re.compile(r"BATCH-(\d+)", re.IGNORECASE)


def normalize_id(value: str) -> str:
    """Comparison-only normalization; never use this value to rewrite stored IDs."""
    return re.sub(r"[-_]", "", value).casefold()


def load_inventory() -> list[dict]:
    rows = []
    for path in sorted(CONTENT.glob("*/records/*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("record_type") != "claim":
            continue
        filename_id = path.stem
        internal_id = str(record.get("record_id", ""))
        rows.append({
            "path": str(path.relative_to(ROOT)),
            "filename_id": filename_id,
            "internal_id": internal_id,
            "normalized_filename_id": normalize_id(filename_id),
            "normalized_internal_id": normalize_id(internal_id),
        })
    return rows


def extract_report_rows() -> list[dict]:
    rows = []
    for path in sorted(RELEASE.glob("M13-CLAIM-REVIEW-BATCH-*.md")):
        text = path.read_text(encoding="utf-8")
        batch_match = BATCH.search(path.name)
        batch = int(batch_match.group(1)) if batch_match else None
        table_row = 0
        for line_number, line in enumerate(text.splitlines(), start=1):
            match = ROW.match(line)
            if not match:
                continue
            claim_id, d, e, b, rationale = match.groups()
            table_row += 1
            rows.append({
                "report_file": str(path.relative_to(ROOT)),
                "batch": batch,
                "report_line": line_number,
                "row_in_report": table_row,
                "report_claim_id": claim_id.strip(),
                "D": int(d), "E": int(e), "B": int(b),
                "rationale": rationale.strip(),
                "normalized_id": normalize_id(claim_id.strip()),
            })
    return rows


def build_ledger():
    inventory = load_inventory()
    by_filename = defaultdict(list)
    by_internal = defaultdict(list)
    for item in inventory:
        by_filename[item["normalized_filename_id"]].append(item)
        by_internal[item["normalized_internal_id"]].append(item)

    rows = extract_report_rows()
    by_norm_rows = defaultdict(list)
    for index, row in enumerate(rows):
        by_norm_rows[row["normalized_id"]].append(index)

    duplicate_groups = {
        key: indices for key, indices in by_norm_rows.items() if len(indices) > 1
    }
    ledger = []
    matched_inventory_ids = set()
    unresolved = []
    alias_rows = []
    for index, row in enumerate(rows, start=1):
        candidates = {
            (item["path"], item["filename_id"], item["internal_id"]): item
            for item in (
                by_filename.get(row["normalized_id"], [])
                + by_internal.get(row["normalized_id"], [])
            )
        }
        candidates = list(candidates.values())
        exact_candidates = [
            item for item in candidates
            if row["report_claim_id"] in {item["filename_id"], item["internal_id"]}
        ]
        if exact_candidates and len(candidates) == len(exact_candidates):
            match_type = "exact"
            selected = exact_candidates
        elif exact_candidates:
            match_type = "exact-with-normalized-collision"
            selected = candidates
            alias_rows.append({
                "report_file": row["report_file"],
                "report_line": row["report_line"],
                "report_claim_id": row["report_claim_id"],
                "inventory_matches": [
                    {"path": x["path"], "filename_id": x["filename_id"], "internal_id": x["internal_id"]}
                    for x in selected
                ],
                "status": "normalized collision despite exact match; manual adjudication required; stored identifiers preserved",
            })
        elif candidates:
            match_type = "separator-normalized"
            selected = candidates
            alias_rows.append({
                "report_file": row["report_file"],
                "report_line": row["report_line"],
                "report_claim_id": row["report_claim_id"],
                "inventory_matches": [
                    {"path": x["path"], "filename_id": x["filename_id"], "internal_id": x["internal_id"]}
                    for x in selected
                ],
                "status": "manual confirmation required; stored identifiers preserved",
            })
        else:
            match_type = "unmatched"
            selected = []
            unresolved.append({
                "report_file": row["report_file"],
                "report_line": row["report_line"],
                "report_claim_id": row["report_claim_id"],
                "issue": "scored report row did not match any Claim filename or internal ID, even after separator normalization",
            })
        for item in selected:
            matched_inventory_ids.add(item["path"])
        dup_indices = duplicate_groups.get(row["normalized_id"], [])
        duplicate_reports = [rows[i]["report_file"] for i in dup_indices]
        duplicate_ids = [rows[i]["report_claim_id"] for i in dup_indices]
        ledger.append({
            **{k: row[k] for k in ("report_file", "batch", "report_line", "row_in_report", "report_claim_id", "D", "E", "B", "rationale")},
            "inventory_match_type": match_type,
            "inventory_paths": ";".join(x["path"] for x in selected),
            "filename_ids": ";".join(x["filename_id"] for x in selected),
            "internal_ids": ";".join(x["internal_id"] for x in selected),
            "report_row_duplicate_group": " | ".join(f"{a} [{b}]" for a, b in zip(duplicate_reports, duplicate_ids)) if len(dup_indices) > 1 else "",
            "inventory_match_count": len(selected),
        })

    inventory_unscored = [x for x in inventory if x["path"] not in matched_inventory_ids]
    summary = {
        "scope": "all RELEASE/M13-CLAIM-REVIEW-BATCH-*.md files containing explicit scored Claim rows; all Claim JSON records under CONTENT/vertical-slices",
        "inventory_claim_records": len(inventory),
        "scored_report_rows": len(rows),
        "unique_normalized_report_ids": len({r["normalized_id"] for r in rows}),
        "report_row_duplicate_groups": len(duplicate_groups),
        "rows_in_duplicate_groups": sum(len(v) for v in duplicate_groups.values()),
        "unmatched_scored_report_rows": len(unresolved),
        "separator_normalized_matches_requiring_manual_confirmation": len(alias_rows),
        "inventory_claims_with_at_least_one_scored_row_match": len(matched_inventory_ids),
        "inventory_claims_without_a_scored_row_match": len(inventory_unscored),
        "inventory_claims_with_filename_internal_id_mismatch": sum(x["filename_id"] != x["internal_id"] for x in inventory),
        "warning": "This is an identifier/accounting ledger, not semantic duplicate adjudication, evidence validation, or acceptance of prior scores. Matching normalization is comparison-only.",
        "unmatched_rows": unresolved,
        "separator_aliases": alias_rows,
        "inventory_claims_without_scored_rows": inventory_unscored,
    }
    return ledger, summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(ROOT / "RELEASE" / "m13-claim-audit-ledger"))
    args = parser.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    ledger, summary = build_ledger()
    csv_path = out / "scored-claim-row-ledger.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(ledger[0].keys()) if ledger else [])
        writer.writeheader()
        writer.writerows(ledger)
    (out / "reconciliation-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in summary.items() if k not in {"unmatched_rows", "separator_aliases", "inventory_claims_without_scored_rows"}}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
