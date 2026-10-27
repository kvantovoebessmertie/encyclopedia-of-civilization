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
    assert len(rows) == 406
    counts_by_batch = defaultdict(int)
    for row in rows:
        counts_by_batch[row["batch"]] += 1
    assert counts_by_batch[12] == 3
    assert counts_by_batch[41] == 100
    assert counts_by_batch[42] == 100
    assert counts_by_batch[43] == 47
    batch42 = [row for row in rows if row["batch"] == 42]
    batch43 = [row for row in rows if row["batch"] == 43]
    assert [row["report_claim_id"] for row in batch43] == ["CLM-SEPTIC-REDUCE-WATER", "CLM-SEPTIC-SEWAGE-CONTACT", "CLM-DISASTER_RESPONSE_FEMA_A", "CLM-EMERGENCY_MANAGEMENT_BASICS-B", "CLM-EMERGENCY_MANAGEMENT_BASICS-C", "CLM-FIRE-C", "CLM-HUMANITARIAN_LOGISTICS_BASICS-C", "CLM-SEPTIC-PROFESSIONAL-INSPECTION", "CLM-WATER-FILTER-LIMITS", "CLM-SYSTEMS_THINKING_BASICS-D", "CLM-WOODWORKING_BASICS-D", "CLM_WATER_QUALITY_WHO_A", "CLM-PLANT_PATHOLOGY_BASICS-A", "CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-B", "CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-C", "CLM-ENTOMOLOGY_BASICS-B", "CLM-ENTOMOLOGY_BASICS-C", "CLM-ENVIRONMENTAL_HEALTH_BASICS-B", "CLM-ERGONOMICS_BASICS-A", "CLM-FOOD_SECURITY_BASICS-D", "CLM-HEALTH_ECONOMICS_BASICS-A", "CLM-HEALTH_ECONOMICS_BASICS-B", "CLM-HEALTH_ECONOMICS_BASICS-C", "CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-A", "CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-B", "CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-C", "CLM-HISTORY_OF_MEDICINE-A", "CLM-HISTORY_OF_MEDICINE-B", "CLM-INSPECTION_BASICS-A", "CLM-INSPECTION_BASICS-B", "CLM-INSPECTION_BASICS-C", "CLM-M4-HEALTH-RESILIENCE-A", "CLM-M5-ENVIRONMENTAL-WASTEWATER-D", "CLM-MANUFACTURING_BASICS-B", "CLM-MEDICAL_DEVICES_BASICS-A", "CLM-MEDICAL_DEVICES_BASICS-B", "CLM-MEDICAL_DEVICES_BASICS-C", "CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-A", "CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-B", "CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-C", "CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-D", "CLM-NUTRITION_BASICS-A", "CLM-NUTRITION_BASICS-B", "CLM-NUTRITION_BASICS-D", "CLM-OCCUPATIONAL_SAFETY_BASICS-A", "CLM-OCCUPATIONAL_SAFETY_BASICS-B", "CLM-OCCUPATIONAL_SAFETY_BASICS-C"]
    assert (batch43[19]["D"], batch43[19]["E"], batch43[19]["B"]) == (2, 2, 2)
    assert "USDA" in batch43[19]["rationale"]
    assert (batch43[20]["D"], batch43[20]["E"], batch43[20]["B"]) == (2, 2, 2)
    assert "WHO" in batch43[20]["rationale"]
    assert (batch43[21]["D"], batch43[21]["E"], batch43[21]["B"]) == (2, 2, 2)
    assert "WHO" in batch43[21]["rationale"]
    assert (batch43[22]["D"], batch43[22]["E"], batch43[22]["B"]) == (2, 1, 2)
    assert "unlinked" in batch43[22]["rationale"]
    assert (batch43[23]["D"], batch43[23]["E"], batch43[23]["B"]) == (2, 2, 2)
    assert "WHO" in batch43[23]["rationale"]
    assert (batch43[24]["D"], batch43[24]["E"], batch43[24]["B"]) == (2, 1, 2)
    assert "unlinked" in batch43[24]["rationale"]
    assert (batch43[25]["D"], batch43[25]["E"], batch43[25]["B"]) == (2, 2, 2)
    assert "policy-level" in batch43[25]["rationale"]
    assert (batch43[26]["D"], batch43[26]["E"], batch43[26]["B"]) == (3, 2, 2)
    assert "MeSH" in batch43[26]["rationale"]
    assert (batch43[27]["D"], batch43[27]["E"], batch43[27]["B"]) == (2, 1, 2)
    assert "not in the canonical" in batch43[27]["rationale"]
    assert (batch43[28]["D"], batch43[28]["E"], batch43[28]["B"]) == (2, 1, 2)
    assert "OSHA" in batch43[28]["rationale"]
    assert (batch43[29]["D"], batch43[29]["E"], batch43[29]["B"]) == (2, 1, 2)
    assert "data-quality" in batch43[29]["rationale"]
    assert (batch43[30]["D"], batch43[30]["E"], batch43[30]["B"]) == (2, 2, 2)
    assert "editorial safety" in batch43[30]["rationale"]
    assert (batch43[31]["D"], batch43[31]["E"], batch43[31]["B"]) == (3, 2, 2)
    assert (batch43[36]["D"], batch43[36]["E"], batch43[36]["B"]) == (3, 2, 3)
    assert "jurisdiction" in batch43[36]["rationale"]
    assert (batch43[37]["D"], batch43[37]["E"], batch43[37]["B"]) == (3, 2, 2)
    assert "pinpoint" in batch43[37]["rationale"]
    assert (batch43[38]["D"], batch43[38]["E"], batch43[38]["B"]) == (3, 2, 2)
    assert "WHO" in batch43[38]["rationale"]
    assert (batch43[39]["D"], batch43[39]["E"], batch43[39]["B"]) == (3, 1, 3)
    assert "does not directly establish" in batch43[39]["rationale"]
    assert (batch43[40]["D"], batch43[40]["E"], batch43[40]["B"]) == (3, 2, 3)
    assert "NIMH" in batch43[40]["rationale"]
    assert (batch43[41]["D"], batch43[41]["E"], batch43[41]["B"]) == (3, 2, 2)
    assert "NIEHS" in batch43[41]["rationale"]
    assert (batch43[42]["D"], batch43[42]["E"], batch43[42]["B"]) == (3, 2, 2)
    assert "macronutrients" in batch43[42]["rationale"]
    assert (batch43[43]["D"], batch43[43]["E"], batch43[43]["B"]) == (3, 2, 2)
    assert "WHO" in batch43[43]["rationale"]
    assert (batch43[44]["D"], batch43[44]["E"], batch43[44]["B"]) == (2, 2, 3)
    assert "slice-name parenthetical" in batch43[44]["rationale"]
    assert (batch43[45]["D"], batch43[45]["E"], batch43[45]["B"]) == (2, 2, 3)
    assert "slice-name parenthetical" in batch43[45]["rationale"]
    assert (batch43[46]["D"], batch43[46]["E"], batch43[46]["B"]) == (2, 2, 3)
    assert "slice-name parenthetical" in batch43[46]["rationale"]
    assert (batch43[32]["D"], batch43[32]["E"], batch43[32]["B"]) == (2, 2, 3)
    assert [row["report_claim_id"] for row in batch42] == ["CLM-FOOD-NO-OUTDOOR-FREEZER", "CLM-FIRE-B", "CLM-FLOOD-FOOD-CONTACT", "CLM-HOME-FIRE-SMOKE-ALARMS", "CLM_TOXICOLOGY_BASICS_B", "CLM-HANDWASH-20SEC", "CLM-WATER-STORAGE-CONTAINER", "CLM-ENVIRONMENTAL_HEALTH_BASICS-A", "CLM-FIRE-A", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-B", "CLM-LIGHTING-CANDLE-UNATTENDED", "CLM-FLOOD-CLEAN-DISINFECT", "CLM_WASTEWATER_ENGINEERING_BASICS_B", "CLM-IPAWS-ALERT-CONTENT", "CLM_FIRE_SAFETY_BASICS_A", "CLM_FIRE_SAFETY_BASICS_B", "CLM-FLOOD-REENTRY-HAZARD-ESCALATION", "CLM-GENERATOR-REFUEL-COOL", "CLM-TOOL-DEFECTIVE", "CLM-HISTORY_OF_MEDICINE-C", "CLM-HOME-FIRE-ESCAPE-PLAN", "CLM-HOME-FIRE-TWO-WAYS-NFPA", "CLM_POWER_ELECTRONICS_BASICS_C", "CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY", "CLM_WASTEWATER_TREATMENT_BASICS_A", "CLM-M4-CONSTRUCTION-HAZARDS-A", "CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-D", "CLM-ELECTRONICS_BASICS-C", "CLM-ALERTS-ENABLE-RESPOND", "CLM-LIGHTING-FLASHLIGHT-OUTAGE", "CLM-EMERGENCY_MANAGEMENT_BASICS-A", "CLM_ENVIRONMENTAL_ENGINEERING_BASICS_A", "CLM-ENVIRONMENTAL_HEALTH_BASICS-C", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-A", "CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-C", "CLM-FOOD_DISTRIBUTION_BASICS-A", "CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B", "CLM-MATERIALS_SCIENCE_BASICS-A", "CLM-MIGRATION_AND_MOBILITY_BASICS-A", "CLM-NUTRITION_BASICS-C", "CLM-PAPERMAKING_BASICS-A", "CLM-PARTICLE_PHYSICS_BASICS-A", "CLM_PATHOLOGY_BASICS_A", "CLM-FOOD-FREEZER-48H", "CLM-FOOD-REFRIGERATOR-4H", "CLM-PUBLIC_RISK_COMMUNICATION_BASICS-A", "CLM-SLEEP_BASICS-A", "CLM-SLEEP_BASICS-C", "CLM-CDC-FOOD-GRADE-CONTAINER", "CLM-URBAN_PLANNING_BASICS-A", "CLM-WASTEWATER_BASICS-B", "CLM-WATER-FILTER-WHO-PERFORMANCE", "CLM-LIGHTING-CANDLE-CHILDREN", "CLM-FLOOD-CLEAN-PROTECT", "CLM-TOOL-INSPECT", "CLM_MEDICAL_IMAGING_BASICS_B", "CLM_MEDICAL_IMAGING_BASICS_C", "CLM-PAPERMAKING_BASICS-D", "CLM_CLINICAL_TRIALS_BASICS_A", "CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-A", "CLM-DISASTER_RECOVERY_BASICS-D", "CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A", "CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_B", "CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_C", "CLM-IPAWS-ALERT-ELEMENTS", "CLM-LIGHTING-EXTINGUISH", "CLM-ENVIRONMENTAL_HEALTH_BASICS-D", "CLM-EPIDEMIOLOGY_BASICS-D", "CLM_EPIGENETICS_BASICS_B", "CLM-HEAT-EXHAUSTION-SIGNS", "CLM-HEAT-HEATSTROKE-EMERGENCY", "CLM-HEAT-STAY-COOL-HYDRATED", "CLM_FIRE_SAFETY_BASICS_C", "CLM-FLOOD-A", "CLM-FLOOD-REENTRY-SAFE", "CLM-FLOOD-FOOD-OPEN-PACKAGE", "CLM_GENETIC_ENGINEERING_BASICS_B", "CLM_GEOCHEMISTRY_BASICS_A", "CLM_GEOCHEMISTRY_BASICS_C", "CLM_GEOTECHNICAL_ENGINEERING_BASICS_C", "CLM-TOOL-PPE", "CLM_HEALTH_SYSTEMS_BASICS_A", "CLM_HEALTH_SYSTEMS_BASICS_B", "CLM_HEALTH_SYSTEMS_BASICS_C", "CLM-HOME-FIRE-LEAVE-STAY-OUT", "CLM_INDUSTRIAL_PROCESS_SAFETY_BASICS_A", "CLM_MEDICAL_IMAGING_BASICS_A", "CLM_NUTRITION_SCIENCE_BASICS_A", "CLM_NUTRITION_SCIENCE_BASICS_B", "CLM_NUTRITION_SCIENCE_BASICS_C", "CLM_OCCUPATIONAL_HEALTH_BASICS_A", "CLM_OCCUPATIONAL_HEALTH_BASICS_B", "CLM_OCCUPATIONAL_HEALTH_BASICS_C", "CLM-PARTICLE_PHYSICS_BASICS-C", "CLM_PHARMACOVIGILANCE_BASICS_A", "CLM_PHARMACOVIGILANCE_BASICS_B", "CLM_PHARMACOVIGILANCE_BASICS_C", "CLM-PLANT_BIOLOGY_BASICS-B", "CLM-PLANT_BIOLOGY_BASICS-C", "CLM_POWER_ELECTRONICS_BASICS_A"]
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
    assert (batch42[75]["D"], batch42[75]["E"], batch42[75]["B"]) == (2, 1, 1)
    assert (batch42[76]["D"], batch42[76]["E"], batch42[76]["B"]) == (1, 1, 1)
    assert (batch42[77]["D"], batch42[77]["E"], batch42[77]["B"]) == (1, 1, 1)
    assert (batch42[78]["D"], batch42[78]["E"], batch42[78]["B"]) == (1, 1, 1)
    assert (batch42[79]["D"], batch42[79]["E"], batch42[79]["B"]) == (2, 1, 1)
    assert (batch42[80]["D"], batch42[80]["E"], batch42[80]["B"]) == (2, 2, 2)
    assert (batch42[81]["D"], batch42[81]["E"], batch42[81]["B"]) == (1, 1, 1)
    assert (batch42[82]["D"], batch42[82]["E"], batch42[82]["B"]) == (1, 1, 1)
    assert (batch42[83]["D"], batch42[83]["E"], batch42[83]["B"]) == (1, 1, 1)
    assert (batch42[84]["D"], batch42[84]["E"], batch42[84]["B"]) == (2, 2, 2)
    assert (batch42[85]["D"], batch42[85]["E"], batch42[85]["B"]) == (2, 1, 1)
    assert (batch42[86]["D"], batch42[86]["E"], batch42[86]["B"]) == (1, 1, 1)
    assert (batch42[87]["D"], batch42[87]["E"], batch42[87]["B"]) == (1, 1, 1)
    assert (batch42[88]["D"], batch42[88]["E"], batch42[88]["B"]) == (1, 1, 1)
    assert (batch42[89]["D"], batch42[89]["E"], batch42[89]["B"]) == (1, 1, 1)
    assert (batch42[90]["D"], batch42[90]["E"], batch42[90]["B"]) == (1, 2, 2)
    assert (batch42[91]["D"], batch42[91]["E"], batch42[91]["B"]) == (1, 2, 2)
    assert (batch42[92]["D"], batch42[92]["E"], batch42[92]["B"]) == (1, 2, 2)
    assert (batch42[93]["D"], batch42[93]["E"], batch42[93]["B"]) == (1, 2, 2)
    assert (batch42[94]["D"], batch42[94]["E"], batch42[94]["B"]) == (1, 2, 2)
    assert (batch42[95]["D"], batch42[95]["E"], batch42[95]["B"]) == (1, 1, 1)
    assert (batch42[96]["D"], batch42[96]["E"], batch42[96]["B"]) == (1, 1, 1)
    assert (batch42[97]["D"], batch42[97]["E"], batch42[97]["B"]) == (1, 2, 2)
    assert (batch42[98]["D"], batch42[98]["E"], batch42[98]["B"]) == (1, 2, 2)
    assert (batch42[99]["D"], batch42[99]["E"], batch42[99]["B"]) == (2, 1, 1)
    assert "Health Canada" in batch42[0]["rationale"]
    assert all(0 <= row[dimension] <= 3 for row in rows for dimension in ("D", "E", "B"))
    assert all(row["report_claim_id"] and row["rationale"] for row in rows)


def test_ledger_preserves_report_rows_and_exposes_duplicate_groups():
    ledger, summary = build_ledger()
    assert len(ledger) == summary["scored_report_rows"]
    assert summary["inventory_claim_records"] == 1494
    assert summary["scored_report_rows"] == 406
    assert summary["unique_normalized_report_ids"] == 399
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
