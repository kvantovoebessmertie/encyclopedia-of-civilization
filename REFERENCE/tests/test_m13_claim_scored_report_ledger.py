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
    assert len(rows) == 334
    counts_by_batch = defaultdict(int)
    for row in rows:
        counts_by_batch[row["batch"]] += 1
    assert counts_by_batch[12] == 3
    assert counts_by_batch[41] == 100
    assert counts_by_batch[42] == 75
    batch42 = [row for row in rows if row["batch"] == 42]
    assert [row["report_claim_id"] for row in batch42] == ["CLM-FOOD-NO-OUTDOOR-FREEZER", "CLM-FIRE-B", "CLM-FLOOD-FOOD-CONTACT", "CLM-HOME-FIRE-SMOKE-ALARMS", "CLM_TOXICOLOGY_BASICS_B", "CLM-HANDWASH-20SEC", "CLM-WATER-STORAGE-CONTAINER", "CLM-ENVIRONMENTAL_HEALTH_BASICS-A", "CLM-FIRE-A", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-B", "CLM-LIGHTING-CANDLE-UNATTENDED", "CLM-FLOOD-CLEAN-DISINFECT", "CLM_WASTEWATER_ENGINEERING_BASICS_B", "CLM-IPAWS-ALERT-CONTENT", "CLM_FIRE_SAFETY_BASICS_A", "CLM_FIRE_SAFETY_BASICS_B", "CLM-FLOOD-REENTRY-HAZARD-ESCALATION", "CLM-GENERATOR-REFUEL-COOL", "CLM-TOOL-DEFECTIVE", "CLM-HISTORY_OF_MEDICINE-C", "CLM-HOME-FIRE-ESCAPE-PLAN", "CLM-HOME-FIRE-TWO-WAYS-NFPA", "CLM_POWER_ELECTRONICS_BASICS_C", "CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY", "CLM_WASTEWATER_TREATMENT_BASICS_A", "CLM-M4-CONSTRUCTION-HAZARDS-A", "CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-D", "CLM-ELECTRONICS_BASICS-C", "CLM-ALERTS-ENABLE-RESPOND", "CLM-LIGHTING-FLASHLIGHT-OUTAGE", "CLM-EMERGENCY_MANAGEMENT_BASICS-A", "CLM_ENVIRONMENTAL_ENGINEERING_BASICS_A", "CLM-ENVIRONMENTAL_HEALTH_BASICS-C", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-A", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-C", "CLM-FOOD_DISTRIBUTION_BASICS-A", "CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B", "CLM-MATERIALS_SCIENCE_BASICS-A", "CLM-MIGRATION_AND_MOBILITY_BASICS-A", "CLM-NUTRITION_BASICS-C", "CLM-PAPERMAKING_BASICS-A", "CLM-PARTICLE_PHYSICS_BASICS-A", "CLM_PATHOLOGY_BASICS_A", "CLM-FOOD-FREEZER-48H", "CLM-FOOD-REFRIGERATOR-4H", "CLM-PUBLIC_RISK_COMMUNICATION_BASICS-A", "CLM-SLEEP_BASICS-A", "CLM-SLEEP_BASICS-C", "CLM-CDC-FOOD-GRADE-CONTAINER", "CLM-URBAN_PLANNING_BASICS-A", "CLM-WASTEWATER_BASICS-B", "CLM-WATER-FILTER-WHO-PERFORMANCE", "CLM-LIGHTING-CANDLE-CHILDREN", "CLM-FLOOD-CLEAN-PROTECT", "CLM-TOOL-INSPECT", "CLM_MEDICAL_IMAGING_BASICS_B", "CLM_MEDICAL_IMAGING_BASICS_C", "CLM-PAPERMAKING_BASICS-D", "CLM_CLINICAL_TRIALS_BASICS_A", "CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-A", "CLM-DISASTER_RECOVERY_BASICS-D", "CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A", "CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_B", "CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_C", "CLM-IPAWS-ALERT-ELEMENTS", "CLM-LIGHTING-EXTINGUISH", "CLM-ENVIRONMENTAL_HEALTH_BASICS-D", "CLM-EPIDEMIOLOGY_BASICS-D", "CLM_EPIGENETICS_BASICS_B", "CLM-HEAT-EXHAUSTION-SIGNS", "CLM-HEAT-HEATSTROKE-EMERGENCY", "CLM-HEAT-STAY-COOL-HYDRATED", "CLM_FIRE_SAFETY_BASICS_C", "CLM-FLOOD-A", "CLM-FLOOD-REENTRY-SAFE"]
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
    assert (batch42[40]["D"], batch42[40]["E"], batch42[40]["B"]) == (1, 2, 2)
    assert (batch42[41]["D"], batch42[41]["E"], batch42[41]["B"]) == (1, 2, 2)
    assert (batch42[42]["D"], batch42[42]["E"], batch42[42]["B"]) == (1, 2, 2)
    assert (batch42[43]["D"], batch42[43]["E"], batch42[43]["B"]) == (2, 2, 1)
    assert (batch42[44]["D"], batch42[44]["E"], batch42[44]["B"]) == (2, 2, 1)
    assert (batch42[45]["D"], batch42[45]["E"], batch42[45]["B"]) == (1, 1, 1)
    assert (batch42[46]["D"], batch42[46]["E"], batch42[46]["B"]) == (1, 2, 2)
    assert (batch42[47]["D"], batch42[47]["E"], batch42[47]["B"]) == (1, 2, 2)
    assert (batch42[48]["D"], batch42[48]["E"], batch42[48]["B"]) == (2, 2, 2)
    assert (batch42[49]["D"], batch42[49]["E"], batch42[49]["B"]) == (1, 1, 1)
    assert (batch42[50]["D"], batch42[50]["E"], batch42[50]["B"]) == (1, 1, 1)
    assert (batch42[51]["D"], batch42[51]["E"], batch42[51]["B"]) == (2, 2, 2)
    assert (batch42[52]["D"], batch42[52]["E"], batch42[52]["B"]) == (2, 2, 2)
    assert (batch42[53]["D"], batch42[53]["E"], batch42[53]["B"]) == (2, 1, 1)
    assert (batch42[54]["D"], batch42[54]["E"], batch42[54]["B"]) == (2, 2, 2)
    assert (batch42[55]["D"], batch42[55]["E"], batch42[55]["B"]) == (1, 1, 1)
    assert (batch42[56]["D"], batch42[56]["E"], batch42[56]["B"]) == (2, 1, 1)
    assert (batch42[57]["D"], batch42[57]["E"], batch42[57]["B"]) == (1, 2, 2)
    assert (batch42[58]["D"], batch42[58]["E"], batch42[58]["B"]) == (1, 2, 2)
    assert (batch42[59]["D"], batch42[59]["E"], batch42[59]["B"]) == (1, 1, 1)
    assert (batch42[60]["D"], batch42[60]["E"], batch42[60]["B"]) == (1, 2, 2)
    assert (batch42[61]["D"], batch42[61]["E"], batch42[61]["B"]) == (1, 1, 1)
    assert (batch42[62]["D"], batch42[62]["E"], batch42[62]["B"]) == (1, 1, 1)
    assert (batch42[63]["D"], batch42[63]["E"], batch42[63]["B"]) == (1, 1, 1)
    assert (batch42[64]["D"], batch42[64]["E"], batch42[64]["B"]) == (2, 2, 2)
    assert (batch42[65]["D"], batch42[65]["E"], batch42[65]["B"]) == (2, 2, 2)
    assert (batch42[66]["D"], batch42[66]["E"], batch42[66]["B"]) == (1, 2, 2)
    assert (batch42[67]["D"], batch42[67]["E"], batch42[67]["B"]) == (1, 1, 1)
    assert (batch42[68]["D"], batch42[68]["E"], batch42[68]["B"]) == (1, 2, 2)
    assert (batch42[69]["D"], batch42[69]["E"], batch42[69]["B"]) == (2, 2, 1)
    assert (batch42[70]["D"], batch42[70]["E"], batch42[70]["B"]) == (2, 1, 1)
    assert (batch42[71]["D"], batch42[71]["E"], batch42[71]["B"]) == (2, 2, 2)
    assert (batch42[72]["D"], batch42[72]["E"], batch42[72]["B"]) == (2, 1, 1)
    assert (batch42[73]["D"], batch42[73]["E"], batch42[73]["B"]) == (2, 1, 1)
    assert (batch42[74]["D"], batch42[74]["E"], batch42[74]["B"]) == (2, 2, 1)
    assert "Health Canada" in batch42[0]["rationale"]
    assert all(0 <= row[dimension] <= 3 for row in rows for dimension in ("D", "E", "B"))
    assert all(row["report_claim_id"] and row["rationale"] for row in rows)


def test_ledger_preserves_report_rows_and_exposes_duplicate_groups():
    ledger, summary = build_ledger()
    assert len(ledger) == summary["scored_report_rows"]
    assert summary["inventory_claim_records"] == 1494
    assert summary["scored_report_rows"] == 334
    assert summary["unique_normalized_report_ids"] == 325
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
