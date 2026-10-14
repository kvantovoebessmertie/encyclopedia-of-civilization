# M13 Batch 42 — 100-Claim high-consequence scoring worklist

Date: 2026-10-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Selection basis: exact-head Reference Tests artifacts generated from M13 HEAD `795cf63ad6f921aa2c5c3230e3ebdc5f3abb53c1`  
Worksheet artifact SHA-256: `174736a5286124de82b214e5e7aa7f3a02d2f1166bf48927043819ecc6a5c70c`  
Scored-ledger artifact SHA-256: `efa179f6959326c6a20461ecc30895d839107910f630dc81b6e17c14144ce062`  
Evidence-linkage artifact SHA-256: `ab668ad89285467321ee53655a2c061b5bce92df64e8318168445be225b9a0da`

## Purpose and status

**Worklist frozen; scoring NOT STARTED.** This is a bounded set of 100 unique currently unscored Claim versions selected for the next passage-level D/E/B scoring pass. It is not a scoring result, source validation, safety clearance, editorial approval, or publication allowlist.

## Exact-head reconciliation

The generated worksheet and score ledger were built by the Reference Tests workflow for the exact M13 head above. The generated ledger reports:

- 1,494 Claim records in the corpus.
- 259 historical scored report rows covering 252 normalized Claim IDs.
- 1,242 Claims without a scored-report match.
- 7 repeated report-ID groups (14 rows within those groups).
- 0 scored report rows unmatched to the Claim inventory.
- 163 filename/internal-ID mismatch candidates in the inventory.
- Evidence-linkage static census: 4,834 record files; 1,670 Evidence Use records; 619 Source records; 1,143 structural triage findings.

These are machine-generated accounting and routing results, not semantic duplicate adjudication or evidence acceptance. Identifier normalization is comparison-only; stored IDs and paths must never be rewritten by this worklist.

## Selection protocol

1. Exclude every Claim with a normalized ID already represented in the exact-head scored-report ledger.
2. Prioritize unscored Claims carrying risk domains relevant to health, emergency/fire/CO, water/food/sanitation, electricity/energy, construction/tools/materials, chemicals, transport/access, shelter/evacuation, communications continuity, or nuclear/radiological matters.
3. Use existing machine flags only to route review. A flag—including `high_consequence_screen`—is not itself proof of danger, error, or substantive high consequence. Editorial/methodology Claims and false-positive flags must be explicitly adjudicated.
4. For each row, inspect the exact Claim, current Evidence Use and Source versions, full cited passage, scope/context, currentness, jurisdiction, source lineage/independence, and any applicable specialist-review requirement.
5. Record D/E/B scores and a Claim-specific rationale only after passage review. If evidence is broad, inaccessible, stale, non-independent, or fails to support the whole proposition, retain HOLD / insufficient evidence rather than infer support from source reputation.
6. Preserve all existing score rows; do not edit canonical content from this worklist. Any record correction requires its own bounded authorization and versioned regression.
7. Keep high-consequence Claims on HOLD for public pilot until specialist Human View and other applicable gates are documented.

## Candidate set (100 unique Claims)

| # | Claim version | Slice | Risk domains | Machine triage flags (routing only) |
|---:|---|---|---|---|
| 1 | `CLM-FOOD-NO-OUTDOOR-FREEZER@1` | `power-outage-food` | `health_medical;emergency_fire_co;water_food_sanitation;electricity_energy` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 2 | `CLM-FIRE-B@1` | `fire` | `emergency_fire_co;shelter_evacuation_access;transport_access` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 3 | `CLM-FLOOD-FOOD-CONTACT@1` | `flood-food-safety` | `health_medical;emergency_fire_co;water_food_sanitation` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 4 | `CLM-HOME-FIRE-SMOKE-ALARMS@1` | `home-fire-smoke-safety` | `emergency_fire_co;construction_tools_materials;shelter_evacuation_access` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 5 | `CLM_TOXICOLOGY_BASICS_B@1` | `toxicology-basics` | `health_medical;chemicals_hazards;transport_access` | `short_evidence_material_review;high_consequence_screen` |
| 6 | `CLM-HANDWASH-20SEC@1` | `emergency-hand-hygiene` | `health_medical;emergency_fire_co;water_food_sanitation` | `high_consequence_screen` |
| 7 | `CLM-WATER-STORAGE-CONTAINER@1` | `emergency-water-storage-state` | `emergency_fire_co;water_food_sanitation;chemicals_hazards` | `high_consequence_screen` |
| 8 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-A@1` | `environmental-health-basics` | `health_medical;water_food_sanitation;chemicals_hazards` | `high_consequence_screen` |
| 9 | `CLM-FIRE-A@1` | `fire` | `emergency_fire_co;communications_information_continuity;shelter_evacuation_access` | `high_consequence_screen` |
| 10 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-B@1` | `fire-protection-and-life-safety-basics` | `emergency_fire_co;construction_tools_materials;communications_information_continuity` | `high_consequence_screen` |
| 11 | `CLM-LIGHTING-CANDLE-UNATTENDED@1` | `emergency-lighting-safety` | `emergency_fire_co;electricity_energy` | `very_short_claim_statement_review;short_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 12 | `CLM-FLOOD-CLEAN-DISINFECT@1` | `flood-cleanup-safety` | `health_medical;emergency_fire_co` | `short_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 13 | `CLM_WASTEWATER_ENGINEERING_BASICS_B@1` | `wastewater-engineering-basics` | `water_food_sanitation;chemicals_hazards` | `potentially_generic_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 14 | `CLM-IPAWS-ALERT-CONTENT@1` | `emergency-alert-warning` | `emergency_fire_co;communications_information_continuity` | `short_evidence_material_review;high_consequence_screen` |
| 15 | `CLM_FIRE_SAFETY_BASICS_A@1` | `fire-safety-basics` | `emergency_fire_co;shelter_evacuation_access` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 16 | `CLM_FIRE_SAFETY_BASICS_B@1` | `fire-safety-basics` | `emergency_fire_co;shelter_evacuation_access` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 17 | `CLM-FLOOD-REENTRY-HAZARD-ESCALATION@1` | `flood-cleanup-safety` | `electricity_energy;construction_tools_materials` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 18 | `CLM-GENERATOR-REFUEL-COOL@1` | `generator-carbon-monoxide-safety` | `emergency_fire_co;electricity_energy` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 19 | `CLM-TOOL-DEFECTIVE@1` | `hand-tool-safety` | `health_medical;construction_tools_materials` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 20 | `CLM-HISTORY_OF_MEDICINE-C@1` | `history-of-medicine-basics` | `health_medical;construction_tools_materials` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 21 | `CLM-HOME-FIRE-ESCAPE-PLAN@1` | `home-fire-smoke-safety` | `emergency_fire_co;shelter_evacuation_access` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 22 | `CLM-HOME-FIRE-TWO-WAYS-NFPA@1` | `home-fire-smoke-safety` | `emergency_fire_co;shelter_evacuation_access` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 23 | `CLM_POWER_ELECTRONICS_BASICS_C@1` | `power-electronics-basics` | `electricity_energy;transport_access` | `short_evidence_material_review;high_consequence_screen` |
| 24 | `CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY@1` | `power-outage-food` | `water_food_sanitation;electricity_energy` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 25 | `CLM_WASTEWATER_TREATMENT_BASICS_A@1` | `wastewater-treatment-basics` | `water_food_sanitation;chemicals_hazards` | `short_evidence_material_review;high_consequence_screen` |
| 26 | `CLM-M4-CONSTRUCTION-HAZARDS-A@1` | `construction-basics` | `electricity_energy;construction_tools_materials` | `high_consequence_screen` |
| 27 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-D@1` | `disaster-behavioral-health-basics` | `health_medical;emergency_fire_co` | `high_consequence_screen` |
| 28 | `CLM-ELECTRONICS_BASICS-C@1` | `electronics-basics` | `electricity_energy;construction_tools_materials` | `high_consequence_screen` |
| 29 | `CLM-ALERTS-ENABLE-RESPOND@1` | `emergency-alert-warning` | `emergency_fire_co;communications_information_continuity` | `high_consequence_screen` |
| 30 | `CLM-LIGHTING-FLASHLIGHT-OUTAGE@1` | `emergency-lighting-safety` | `emergency_fire_co;electricity_energy` | `high_consequence_screen` |
| 31 | `CLM-EMERGENCY_MANAGEMENT_BASICS-A@1` | `emergency-management-basics` | `emergency_fire_co;communications_information_continuity` | `high_consequence_screen` |
| 32 | `CLM_ENVIRONMENTAL_ENGINEERING_BASICS_A@1` | `environmental-engineering-basics` | `health_medical;communications_information_continuity` | `high_consequence_screen` |
| 33 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-C@1` | `environmental-health-basics` | `health_medical;transport_access` | `high_consequence_screen` |
| 34 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-A@1` | `fire-protection-and-life-safety-basics` | `emergency_fire_co;construction_tools_materials` | `high_consequence_screen` |
| 35 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-C@1` | `fire-protection-and-life-safety-basics` | `emergency_fire_co;construction_tools_materials;legal_financial` | `high_consequence_screen` |
| 36 | `CLM-FOOD_DISTRIBUTION_BASICS-A@1` | `food-distribution-basics` | `emergency_fire_co;transport_access` | `high_consequence_screen` |
| 37 | `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1` | `human-settlement-systems-basics` | `water_food_sanitation;transport_access` | `high_consequence_screen` |
| 38 | `CLM-MATERIALS_SCIENCE_BASICS-A@1` | `materials-science-basics` | `electricity_energy;chemicals_hazards` | `high_consequence_screen` |
| 39 | `CLM-MIGRATION_AND_MOBILITY_BASICS-A@1` | `migration-and-mobility-basics` | `legal_financial;shelter_evacuation_access;transport_access` | `high_consequence_screen` |
| 40 | `CLM-NUTRITION_BASICS-C@1` | `nutrition-basics` | `health_medical;electricity_energy` | `high_consequence_screen` |
| 41 | `CLM-PAPERMAKING_BASICS-A@1` | `papermaking-basics` | `water_food_sanitation;chemicals_hazards` | `high_consequence_screen` |
| 42 | `CLM-PARTICLE_PHYSICS_BASICS-A@1` | `particle-physics-basics` | `electricity_energy;construction_tools_materials` | `high_consequence_screen` |
| 43 | `CLM_PATHOLOGY_BASICS_A@1` | `pathology-basics` | `health_medical;electricity_energy` | `high_consequence_screen` |
| 44 | `CLM-FOOD-FREEZER-48H@1` | `power-outage-food` | `water_food_sanitation;electricity_energy` | `high_consequence_screen` |
| 45 | `CLM-FOOD-REFRIGERATOR-4H@1` | `power-outage-food` | `water_food_sanitation;electricity_energy` | `high_consequence_screen` |
| 46 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-A@1` | `public-risk-communication-basics` | `health_medical;communications_information_continuity` | `high_consequence_screen` |
| 47 | `CLM-SLEEP_BASICS-A@1` | `sleep-basics` | `health_medical;communications_information_continuity` | `high_consequence_screen` |
| 48 | `CLM-SLEEP_BASICS-C@1` | `sleep-basics` | `health_medical;electricity_energy` | `high_consequence_screen` |
| 49 | `CLM-CDC-FOOD-GRADE-CONTAINER@1` | `source-provenance-authorship-trust` | `emergency_fire_co;chemicals_hazards` | `high_consequence_screen` |
| 50 | `CLM-URBAN_PLANNING_BASICS-A@1` | `urban-planning-basics` | `construction_tools_materials;transport_access` | `high_consequence_screen` |
| 51 | `CLM-WASTEWATER_BASICS-B@1` | `wastewater-basics` | `health_medical;water_food_sanitation` | `high_consequence_screen` |
| 52 | `CLM-WATER-FILTER-WHO-PERFORMANCE@1` | `water-filter-assessment` | `health_medical;water_food_sanitation` | `high_consequence_screen` |
| 53 | `CLM-LIGHTING-CANDLE-CHILDREN@1` | `emergency-lighting-safety` | `emergency_fire_co` | `short_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 54 | `CLM-FLOOD-CLEAN-PROTECT@1` | `flood-cleanup-safety` | `emergency_fire_co` | `short_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 55 | `CLM-TOOL-INSPECT@1` | `hand-tool-safety` | `construction_tools_materials` | `short_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 56 | `CLM_MEDICAL_IMAGING_BASICS_B@1` | `medical-imaging-basics` | `health_medical` | `short_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 57 | `CLM_MEDICAL_IMAGING_BASICS_C@1` | `medical-imaging-basics` | `health_medical` | `short_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 58 | `CLM-PAPERMAKING_BASICS-D@1` | `papermaking-basics` | `water_food_sanitation` | `potentially_generic_evidence_material_review;actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 59 | `CLM_CLINICAL_TRIALS_BASICS_A@1` | `clinical-trials-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 60 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-A@1` | `disaster-behavioral-health-basics` | `health_medical` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 61 | `CLM-DISASTER_RECOVERY_BASICS-D@1` | `disaster-recovery-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 62 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A@1` | `disaster-response-logistics-basics` | `emergency_fire_co` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 63 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_B@1` | `disaster-response-logistics-basics` | `emergency_fire_co` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 64 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_C@1` | `disaster-response-logistics-basics` | `emergency_fire_co` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 65 | `CLM-IPAWS-ALERT-ELEMENTS@1` | `emergency-alert-warning` | `communications_information_continuity` | `short_evidence_material_review;high_consequence_screen` |
| 66 | `CLM-LIGHTING-EXTINGUISH@1` | `emergency-lighting-safety` | `emergency_fire_co` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 67 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-D@1` | `environmental-health-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 68 | `CLM-EPIDEMIOLOGY_BASICS-D@1` | `epidemiology-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 69 | `CLM_EPIGENETICS_BASICS_B@1` | `epigenetics-basics` | `chemicals_hazards` | `short_evidence_material_review;high_consequence_screen` |
| 70 | `CLM-HEAT-EXHAUSTION-SIGNS@1` | `extreme-heat-safety` | `health_medical` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 71 | `CLM-HEAT-HEATSTROKE-EMERGENCY@1` | `extreme-heat-safety` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 72 | `CLM-HEAT-STAY-COOL-HYDRATED@1` | `extreme-heat-safety` | `health_medical` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 73 | `CLM_FIRE_SAFETY_BASICS_C@1` | `fire-safety-basics` | `emergency_fire_co` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 74 | `CLM-FLOOD-A@1` | `flood` | `communications_information_continuity` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 75 | `CLM-FLOOD-REENTRY-SAFE@1` | `flood-cleanup-safety` | `electricity_energy` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 76 | `CLM-FLOOD-FOOD-OPEN-PACKAGE@1` | `flood-food-safety` | `emergency_fire_co` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 77 | `CLM_GENETIC_ENGINEERING_BASICS_B@1` | `genetic-engineering-basics` | `health_medical` | `short_evidence_material_review;high_consequence_screen` |
| 78 | `CLM_GEOCHEMISTRY_BASICS_A@1` | `geochemistry-basics` | `chemicals_hazards` | `short_evidence_material_review;high_consequence_screen` |
| 79 | `CLM_GEOCHEMISTRY_BASICS_C@1` | `geochemistry-basics` | `chemicals_hazards` | `short_evidence_material_review;high_consequence_screen` |
| 80 | `CLM_GEOTECHNICAL_ENGINEERING_BASICS_C@1` | `geotechnical-engineering-basics` | `construction_tools_materials` | `short_evidence_material_review;high_consequence_screen` |
| 81 | `CLM-TOOL-PPE@1` | `hand-tool-safety` | `construction_tools_materials` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 82 | `CLM_HEALTH_SYSTEMS_BASICS_A@1` | `health-systems-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 83 | `CLM_HEALTH_SYSTEMS_BASICS_B@1` | `health-systems-basics` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 84 | `CLM_HEALTH_SYSTEMS_BASICS_C@1` | `health-systems-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 85 | `CLM-HOME-FIRE-LEAVE-STAY-OUT@1` | `home-fire-smoke-safety` | `emergency_fire_co` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 86 | `CLM_INDUSTRIAL_PROCESS_SAFETY_BASICS_A@1` | `industrial-process-safety-basics` | `chemicals_hazards` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 87 | `CLM_MEDICAL_IMAGING_BASICS_A@1` | `medical-imaging-basics` | `health_medical` | `short_evidence_material_review;high_consequence_screen` |
| 88 | `CLM_NUTRITION_SCIENCE_BASICS_A@1` | `nutrition-science-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 89 | `CLM_NUTRITION_SCIENCE_BASICS_B@1` | `nutrition-science-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 90 | `CLM_NUTRITION_SCIENCE_BASICS_C@1` | `nutrition-science-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 91 | `CLM_OCCUPATIONAL_HEALTH_BASICS_A@1` | `occupational-health-basics` | `health_medical` | `short_evidence_material_review;high_consequence_screen` |
| 92 | `CLM_OCCUPATIONAL_HEALTH_BASICS_B@1` | `occupational-health-basics` | `health_medical` | `short_evidence_material_review;high_consequence_screen` |
| 93 | `CLM_OCCUPATIONAL_HEALTH_BASICS_C@1` | `occupational-health-basics` | `health_medical` | `short_evidence_material_review;high_consequence_screen` |
| 94 | `CLM-PARTICLE_PHYSICS_BASICS-C@1` | `particle-physics-basics` | `construction_tools_materials` | `actionable_or_prescriptive_claim_review;high_consequence_screen` |
| 95 | `CLM_PHARMACOVIGILANCE_BASICS_A@1` | `pharmacovigilance-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 96 | `CLM_PHARMACOVIGILANCE_BASICS_B@1` | `pharmacovigilance-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 97 | `CLM_PHARMACOVIGILANCE_BASICS_C@1` | `pharmacovigilance-basics` | `health_medical` | `potentially_generic_evidence_material_review;high_consequence_screen` |
| 98 | `CLM-PLANT_BIOLOGY_BASICS-B@1` | `plant-biology-basics` | `transport_access` | `short_evidence_material_review;high_consequence_screen` |
| 99 | `CLM-PLANT_BIOLOGY_BASICS-C@1` | `plant-biology-basics` | `transport_access` | `short_evidence_material_review;high_consequence_screen` |
| 100 | `CLM_POWER_ELECTRONICS_BASICS_A@1` | `power-electronics-basics` | `electricity_energy` | `short_evidence_material_review;high_consequence_screen` |

## Batch 42 execution worksheet

For each candidate, record the exact Claim/Evidence Use/Source version and source pinpoint; D/E/B values; rationale; source currentness and independence; rights/attribution note; Human View/specialist requirement; disposition; and any bounded correction authorization required. Keep unverified passages and specialist-dependent claims on HOLD. Do not convert this worklist into a score by copying machine flags.

## Exit criteria

Batch 42 is complete only after all 100 rows have claim-specific passage review and documented scoring or explicit HOLD disposition, prior-score and duplicate reconciliation, and required specialist/independent review routing. Any resulting content change must be versioned and separately authorized. M13 remains open until the full corpus audit, all review passes, exact-head CI, and final base/main/tree checks pass.
