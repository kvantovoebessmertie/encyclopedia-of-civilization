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
    assert len(rows) == 299
    counts_by_batch = defaultdict(int)
    for row in rows:
        counts_by_batch[row["batch"]] += 1
    assert counts_by_batch[12] == 3
    assert counts_by_batch[41] == 100
    assert counts_by_batch[42] == 40
    batch42 = [row for row in rows if row["batch"] == 42]
    assert [row["report_claim_id"] for row in batch42] == ["CLM-FOOD-NO-OUTDOOR-FREEZER", "CLM-FIRE-B", "CLM-FLOOD-FOOD-CONTACT", "CLM-HOME-FIRE-SMOKE-ALARMS", "CLM_TOXICOLOGY_BASICS_B", "CLM-HANDWASH-20SEC", "CLM-WATER-STORAGE-CONTAINER", "CLM-ENVIRONMENTAL_HEALTH_BASICS-A", "CLM-FIRE-A", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-B", "CLM-LIGHTING-CANDLE-UNATTENDED", "CLM-FLOOD-CLEAN-DISINFECT", "CLM_WASTEWATER_ENGINEERING_BASICS_B", "CLM-IPAWS-ALERT-CONTENT", "CLM_FIRE_SAFETY_BASICS_A", "CLM_FIRE_SAFETY_BASICS_B", "CLM-FLOOD-REENTRY-HAZARD-ESCALATION", "CLM-GENERATOR-REFUEL-COOL", "CLM-TOOL-DEFECTIVE", "CLM-HISTORY_OF_MEDICINE-C", "CLM-HOME-FIRE-ESCAPE-PLAN", "CLM-HOME-FIRE-TWO-WAYS-NFPA", "CLM_POWER_ELECTRONICS_BASICS_C", "CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY", "CLM_WASTEWATER_TREATMENT_BASICS_A", "CLM-M4-CONSTRUCTION-HAZARDS-A", "CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-D", "CLM-ELECTRONICS_BASICS-C", "CLM-ALERTS-ENABLE-RESPOND", "CLM-LIGHTING-FLASHLIGHT-OUTAGE", "CLM-EMERGENCY_MANAGEMENT_BASICS-A", "CLM_ENVIRONMENTAL_ENGINEERING_BASICS_A", "CLM-ENVIRONMENTAL_HEALTH_BASICS-C", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-A", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-C", "CLM-FOOD_DISTRIBUTION_BASICS-A", "CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B", "CLM-MATERIALS_SCIENCE_BASICS-A", "CLM-MIGRATION_AND_MOBILITY_BASICS-A", "CLM-NUTRITION_BASICS-C"]
    assert (batch42[0]["D"], batch42[0]["E"], batch42[0]["B"]) == (2, 1, 1)
    assert (batch42[20]["D"], batch42[20]["E"], batch42[20]["B"]) == (2, 1, 1)
    assert "canonical Source URI" in batch42[20]["rationale"]
    assert (batch42[21]["D"], batch42[21]["E"], batch42[21]["B"]) == (2, 1, 1)
    assert (batch42[22]["D"], batch42[22]["E"], batch42[22]["B"]) == (1, 1, 1)
    assert (batch42[23]["D"], batch42[23]["E"], batch42[23]["B"]) == (2, 2, 2)
    assert (batch42[24]["D"], batch42[24]["E"], batch42[24]["B"]) == (1, 1, 1)
    assert (batch42[25]["D"], batch42[25]["E"], batch42[25]["B"]) == (2, 1, 1)
    assert (batch42[26]["D"], batch42[26]["E"], batch42[26]["B"]) == (1, 2, 2)
    assert (batch42[27]["D"], batch42[27]["E"], batch42[27]["B"]) == (1, 1, 1)
    assert (batch42[28]["D"], batch42[28]["E"], batch42[28]["B"]) == (2, 1, 1)
    assert (batch42[29]["D"], batch42[29]["E"], batch42[29]["B"]) == (2, 2, 1)
    assert (batch42[30]["D"], batch42[30]["E"], batch42[30]["B"]) == (1, 1, 1)
    assert (batch42[31]["D"], batch42[31]["E"], batch42[31]["B"]) == (1, 1, 1)
    assert (batch42[32]["D"], batch42[32]["E"], batch42[32]["B"]) == (1, 1, 1)
    assert (batch42[33]["D"], batch42[33]["E"], batch42[33]["B"]) == (2, 1, 1)
    assert (batch42[34]["D"], batch42[34]["E"], batch42[34]["B"]) == (2, 1, 1)
    assert (batch42[35]["D"], batch42[35]["E"], batch42[35]["B"]) == (1, 1, 1)
    assert (batch42[36]["D"], batch42[36]["E"], batch42[36]["B"]) == (1, 2, 2)
    assert (batch42[37]["D"], batch42[37]["E"], batch42[37]["B"]) == (1, 2, 1)
    assert (batch42[38]["D"], batch42[38]["E"], batch42[38]["B"]) == (1, 2, 2)
    assert (batch42[39]["D"], batch42[39]["E"], batch42[39]["B"]) == (1, 2, 2)
    assert "Health Canada" in batch42[0]["rationale"]
    assert all(0 <= row[dimension] <= 3 for row in rows for dimension in ("D", "E", "B"))
    assert all(row["report_claim_id"] and row["rationale"] for row in rows)


def test_ledger_preserves_report_rows_and_exposes_duplicate_groups():
    ledger, summary = build_ledger()
    assert len(ledger) == summary["scored_report_rows"]
    assert summary["inventory_claim_records"] == 1494
    assert summary["scored_report_rows"] == 299
    assert summary["unique_normalized_report_ids"] == 290
    assert summary["report_row_duplicate_groups"] == 7
    assert summary["unmatched_scored_report_rows"] == 0
    assert summary["unique_normalized_report_ids"] <= summary["scored_report_rows"]
    repeated = defaultdict(list)
    for row in ledger:
        if row["report_row_duplicate_group"]:
            repeated[row["report_claim_id"]].append(row)
    # A duplicate group is surfaced for human adjudication, never silently discarded.
    assert summary["report_row_duplicate_groups"] >= 1
    assert summary["warning"].startswith("This is an identifier/accounting ledger")
