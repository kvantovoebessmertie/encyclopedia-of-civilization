from __future__ import annotations

from collections import defaultdict

from REFERENCE.m13_claim_scored_report_ledger import (
    build_ledger,
    extract_report_rows,
    normalize_id,
)


def test_identifier_normalization_is_comparison_only_and_separator_limited():
    assert normalize_id("CLM-AGRICULTURAL_ENGINEERING_BASICS-A") == normalize_id(
        "CLM_AGRICULTURAL_ENGINEERING_BASICS_A"
    )
    assert normalize_id("CLM-WATER-A") == normalize_id("CLM_WATER_A")
    assert normalize_id("CLM-WATER-A") != normalize_id("CLM-WATER-B")


def test_scored_report_rows_are_extracted_with_independent_scores():
    rows = extract_report_rows()
    assert len(rows) >= 150
    assert all(0 <= row[dimension] <= 3 for row in rows for dimension in ("D", "E", "B"))
    assert all(row["report_claim_id"] and row["rationale"] for row in rows)


def test_ledger_preserves_report_rows_and_exposes_duplicate_groups():
    ledger, summary = build_ledger()
    assert len(ledger) == summary["scored_report_rows"]
    assert summary["inventory_claim_records"] > 0
    assert summary["unique_normalized_report_ids"] <= summary["scored_report_rows"]
    repeated = defaultdict(list)
    for row in ledger:
        if row["report_row_duplicate_group"]:
            repeated[row["report_claim_id"]].append(row)
    # A duplicate group is surfaced for human adjudication, never silently discarded.
    assert summary["report_row_duplicate_groups"] >= 1
    assert summary["warning"].startswith("This is an identifier/accounting ledger")
