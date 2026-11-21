# M13 — Master normalized crosswalk for the 200 Batch 42–43 reports

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Audit base for Batch 42 rows 001–068: `dd1cd26fa01578770d8b1cc0454c2d346644698c`  
Crosswalk artifact commit: this commit  
Scope: the complete 200-report cohort (Batch 42 rows 001–100; Batch 43 rows 001–100). This is a report-cohort crosswalk, not the entire 1,494-Claim corpus ledger.

## 1. Master result

**200/200 report rows joined; 200/200 normalized Claim IDs are unique; 200/200 primary current graph chains are confirmed.**

| Measure | Result |
|---|---:|
| Historical report bodies individually inspected | 200/200 |
| Batch 42 rows in crosswalk | 100/100 |
| Batch 43 rows in crosswalk | 100/100 |
| Report-row occurrences | 200 |
| Unique normalized Claim IDs | 200 |
| Duplicate normalized Claim-ID groups within this 200-row cohort | 0 |
| Primary current Claim → EU → Source chains confirmed | 200/200 |
| Version mismatch in primary chain | 0 |
| Claim↔EU or EU↔Source cross-link mismatch | 0 |
| Current accepted D/E/B assessments from this join | 0 |
| Canonical record mutations performed | 0 |

Claim version distribution in the 200 historical report headers:
- Claim@1: **199**
- Claim@2: **1** — Batch 43 row 098, hydrology.

The 200 report rows contain no duplicate Claim IDs after separator/case normalization. This is a bounded statement about the Batch 42–43 200-report cohort only. It does not replace the full 1,494-Claim inventory-to-ledger reconciliation or adjudicate duplicate groups elsewhere in the corpus.

## 2. Row-level normalized Claim crosswalk

The primary graph result is taken from the dedicated current-graph reconciliation artifacts:
- Batch 42 rows 001–068: `M13-BATCH-42-68-CHAIN-RECONCILIATION-AND-STRUCTURAL-CLOSURE-2026-11-21.md`.
- Batch 42 rows 069–100: `M13-BATCH-42-CURRENT-CANONICAL-GRAPH-RECONCILIATION-ROWS-069-100-2026-11-21.md`.
- Batch 43 rows 001–100: `M13-BATCH-43-CURRENT-CANONICAL-GRAPH-RECONCILIATION-ROWS-001-100-2026-11-21.md`.

| Batch | Row | Historical Claim ID @version | Current primary graph result |
|---:|---:|---|---|
| 42 | 001 | `CLM-FOOD-NO-OUTDOOR-FREEZER@1` | EXACT_PRIMARY_CHAIN |
| 42 | 002 | `CLM-FIRE-B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 003 | `CLM-FLOOD-FOOD-CONTACT@1` | EXACT_PRIMARY_CHAIN |
| 42 | 004 | `CLM-HOME-FIRE-SMOKE-ALARMS@1` | EXACT_PRIMARY_CHAIN |
| 42 | 005 | `CLM_TOXICOLOGY_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 006 | `CLM-HANDWASH-20SEC@1` | EXACT_PRIMARY_CHAIN |
| 42 | 007 | `CLM-WATER-STORAGE-CONTAINER@1` | EXACT_PRIMARY_CHAIN |
| 42 | 008 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 009 | `CLM-FIRE-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 010 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 011 | `CLM-LIGHTING-CANDLE-UNATTENDED@1` | EXACT_PRIMARY_CHAIN |
| 42 | 012 | `CLM-FLOOD-CLEAN-DISINFECT@1` | EXACT_PRIMARY_CHAIN |
| 42 | 013 | `CLM_WASTEWATER_ENGINEERING_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 014 | `CLM-IPAWS-ALERT-CONTENT@1` | EXACT_PRIMARY_CHAIN |
| 42 | 015 | `CLM_FIRE_SAFETY_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 016 | `CLM_FIRE_SAFETY_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 017 | `CLM-FLOOD-REENTRY-HAZARD-ESCALATION@1` | EXACT_PRIMARY_CHAIN |
| 42 | 018 | `CLM-GENERATOR-REFUEL-COOL@1` | EXACT_PRIMARY_CHAIN |
| 42 | 019 | `CLM-TOOL-DEFECTIVE@1` | EXACT_PRIMARY_CHAIN |
| 42 | 020 | `CLM-HISTORY_OF_MEDICINE-C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 021 | `CLM-HOME-FIRE-ESCAPE-PLAN@1` | EXACT_PRIMARY_CHAIN |
| 42 | 022 | `CLM-HOME-FIRE-TWO-WAYS-NFPA@1` | EXACT_PRIMARY_CHAIN |
| 42 | 023 | `CLM_POWER_ELECTRONICS_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 024 | `CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY@1` | EXACT_PRIMARY_CHAIN |
| 42 | 025 | `CLM_WASTEWATER_TREATMENT_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 026 | `CLM-M4-CONSTRUCTION-HAZARDS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 027 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 42 | 028 | `CLM-ELECTRONICS_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 029 | `CLM-ALERTS-ENABLE-RESPOND@1` | EXACT_PRIMARY_CHAIN |
| 42 | 030 | `CLM-LIGHTING-FLASHLIGHT-OUTAGE@1` | EXACT_PRIMARY_CHAIN |
| 42 | 031 | `CLM-EMERGENCY_MANAGEMENT_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 032 | `CLM_ENVIRONMENTAL_ENGINEERING_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 033 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 034 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 035 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 036 | `CLM-FOOD_DISTRIBUTION_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 037 | `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 038 | `CLM-MATERIALS_SCIENCE_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 039 | `CLM-MIGRATION_AND_MOBILITY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 040 | `CLM-NUTRITION_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 041 | `CLM-PAPERMAKING_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 042 | `CLM-PARTICLE_PHYSICS_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 043 | `CLM_PATHOLOGY_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 044 | `CLM-FOOD-FREEZER-48H@1` | EXACT_PRIMARY_CHAIN |
| 42 | 045 | `CLM-FOOD-REFRIGERATOR-4H@1` | EXACT_PRIMARY_CHAIN |
| 42 | 046 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 047 | `CLM-SLEEP_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 048 | `CLM-SLEEP_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 049 | `CLM-CDC-FOOD-GRADE-CONTAINER@1` | EXACT_PRIMARY_CHAIN |
| 42 | 050 | `CLM-URBAN_PLANNING_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 051 | `CLM-WASTEWATER_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 052 | `CLM-WATER-FILTER-WHO-PERFORMANCE@1` | EXACT_PRIMARY_CHAIN |
| 42 | 053 | `CLM-LIGHTING-CANDLE-CHILDREN@1` | EXACT_PRIMARY_CHAIN |
| 42 | 054 | `CLM-FLOOD-CLEAN-PROTECT@1` | EXACT_PRIMARY_CHAIN |
| 42 | 055 | `CLM-TOOL-INSPECT@1` | EXACT_PRIMARY_CHAIN |
| 42 | 056 | `CLM_MEDICAL_IMAGING_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 057 | `CLM_MEDICAL_IMAGING_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 058 | `CLM-PAPERMAKING_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 42 | 059 | `CLM_CLINICAL_TRIALS_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 060 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 061 | `CLM-DISASTER_RECOVERY_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 42 | 062 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 063 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 064 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 065 | `CLM-IPAWS-ALERT-ELEMENTS@1` | EXACT_PRIMARY_CHAIN |
| 42 | 066 | `CLM-LIGHTING-EXTINGUISH@1` | EXACT_PRIMARY_CHAIN |
| 42 | 067 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 42 | 068 | `CLM-EPIDEMIOLOGY_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 42 | 069 | `CLM_EPIGENETICS_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 070 | `CLM-HEAT-EXHAUSTION-SIGNS@1` | EXACT_PRIMARY_CHAIN |
| 42 | 071 | `CLM-HEAT-HEATSTROKE-EMERGENCY@1` | EXACT_PRIMARY_CHAIN |
| 42 | 072 | `CLM-HEAT-STAY-COOL-HYDRATED@1` | EXACT_PRIMARY_CHAIN |
| 42 | 073 | `CLM_FIRE_SAFETY_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 074 | `CLM-FLOOD-A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 075 | `CLM-FLOOD-REENTRY-SAFE@1` | EXACT_PRIMARY_CHAIN |
| 42 | 076 | `CLM-FLOOD-FOOD-OPEN-PACKAGE@1` | EXACT_PRIMARY_CHAIN |
| 42 | 077 | `CLM_GENETIC_ENGINEERING_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 078 | `CLM_GEOCHEMISTRY_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 079 | `CLM_GEOCHEMISTRY_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 080 | `CLM_GEOTECHNICAL_ENGINEERING_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 081 | `CLM-TOOL-PPE@1` | EXACT_PRIMARY_CHAIN |
| 42 | 082 | `CLM_HEALTH_SYSTEMS_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 083 | `CLM_HEALTH_SYSTEMS_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 084 | `CLM_HEALTH_SYSTEMS_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 085 | `CLM-HOME-FIRE-LEAVE-STAY-OUT@1` | EXACT_PRIMARY_CHAIN |
| 42 | 086 | `CLM_INDUSTRIAL_PROCESS_SAFETY_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 087 | `CLM_MEDICAL_IMAGING_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 088 | `CLM_NUTRITION_SCIENCE_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 089 | `CLM_NUTRITION_SCIENCE_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 090 | `CLM_NUTRITION_SCIENCE_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 091 | `CLM_OCCUPATIONAL_HEALTH_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 092 | `CLM_OCCUPATIONAL_HEALTH_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 093 | `CLM_OCCUPATIONAL_HEALTH_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 094 | `CLM-PARTICLE_PHYSICS_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 095 | `CLM_PHARMACOVIGILANCE_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 42 | 096 | `CLM_PHARMACOVIGILANCE_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 097 | `CLM_PHARMACOVIGILANCE_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 098 | `CLM-PLANT_BIOLOGY_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 42 | 099 | `CLM-PLANT_BIOLOGY_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 42 | 100 | `CLM_POWER_ELECTRONICS_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 001 | `CLM-SEPTIC-REDUCE-WATER@1` | EXACT_PRIMARY_CHAIN |
| 43 | 002 | `CLM-SEPTIC-SEWAGE-CONTACT@1` | EXACT_PRIMARY_CHAIN |
| 43 | 003 | `CLM-DISASTER_RESPONSE_FEMA_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 004 | `CLM-EMERGENCY_MANAGEMENT_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 005 | `CLM-EMERGENCY_MANAGEMENT_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 006 | `CLM-FIRE-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 007 | `CLM-HUMANITARIAN_LOGISTICS_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 008 | `CLM-SEPTIC-PROFESSIONAL-INSPECTION@1` | EXACT_PRIMARY_CHAIN |
| 43 | 009 | `CLM-WATER-FILTER-LIMITS@1` | EXACT_PRIMARY_CHAIN |
| 43 | 010 | `CLM-SYSTEMS_THINKING_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 43 | 011 | `CLM-WOODWORKING_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 43 | 012 | `CLM_WATER_QUALITY_WHO_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 013 | `CLM-PLANT_PATHOLOGY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 014 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 015 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 016 | `CLM-ENTOMOLOGY_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 017 | `CLM-ENTOMOLOGY_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 018 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 019 | `CLM-ERGONOMICS_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 020 | `CLM-FOOD_SECURITY_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 43 | 021 | `CLM-HEALTH_ECONOMICS_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 022 | `CLM-HEALTH_ECONOMICS_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 023 | `CLM-HEALTH_ECONOMICS_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 024 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 025 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 026 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 027 | `CLM-HISTORY_OF_MEDICINE-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 028 | `CLM-HISTORY_OF_MEDICINE-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 029 | `CLM-INSPECTION_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 030 | `CLM-INSPECTION_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 031 | `CLM-INSPECTION_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 032 | `CLM-M4-HEALTH-RESILIENCE-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 033 | `CLM-M5-ENVIRONMENTAL-WASTEWATER-D@1` | EXACT_PRIMARY_CHAIN |
| 43 | 034 | `CLM-MANUFACTURING_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 035 | `CLM-MEDICAL_DEVICES_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 036 | `CLM-MEDICAL_DEVICES_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 037 | `CLM-MEDICAL_DEVICES_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 038 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 039 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 040 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 041 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-D@1` | EXACT_PRIMARY_CHAIN |
| 43 | 042 | `CLM-NUTRITION_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 043 | `CLM-NUTRITION_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 044 | `CLM-NUTRITION_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 43 | 045 | `CLM-OCCUPATIONAL_SAFETY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 046 | `CLM-OCCUPATIONAL_SAFETY_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 047 | `CLM-OCCUPATIONAL_SAFETY_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 048 | `CLM-PHYSIOLOGY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 049 | `CLM-PLANT_PATHOLOGY_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 050 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 051 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 052 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 053 | `CLM-PUBLIC_HEALTH_SURVEILLANCE_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 43 | 054 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 055 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 056 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-D@1` | EXACT_PRIMARY_CHAIN |
| 43 | 057 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 058 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 059 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 060 | `CLM-SOCIAL_POLICY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 061 | `CLM-SOIL_MICROBIOLOGY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 062 | `CLM-SOIL_MICROBIOLOGY_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 063 | `CLM-SOIL_MICROBIOLOGY_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 064 | `CLM-SYSTEMS_THINKING_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 065 | `CLM-SYSTEMS_THINKING_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 066 | `CLM-SYSTEMS_THINKING_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 067 | `CLM-VACCINATION_INFORMATION_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 068 | `CLM-WASTEWATER_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 069 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 070 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 071 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 072 | `CLM_PUBLIC_HEALTH_SURVEILLANCE_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 073 | `CLM_REHABILITATION_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 074 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 075 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 076 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 077 | `CLM_TELEMEDICINE_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 078 | `CLM_TELEMEDICINE_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 079 | `CLM_TELEMEDICINE_BASICS_C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 080 | `CLM_WATER_QUALITY_BASICS_A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 081 | `CLM-FOOD-TARGET-TEMP@1` | EXACT_PRIMARY_CHAIN |
| 43 | 082 | `CLM-SEED-DRY-STORAGE@1` | EXACT_PRIMARY_CHAIN |
| 43 | 083 | `CLM-WASTEWATER_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 084 | `CLM-WATER_INFRASTRUCTURE_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 085 | `CLM-WATER_INFRASTRUCTURE_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 086 | `CLM-WATER_INFRASTRUCTURE_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 087 | `CLM_MARINE_BIOLOGY_BASICS_B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 088 | `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 089 | `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 090 | `CLM-ELECTRICAL_MACHINES_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 091 | `CLM-ELECTRICAL_MACHINES_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 092 | `CLM-ELECTRICAL_MACHINES_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 093 | `CLM-ELECTRICITY_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 094 | `CLM-ELECTRICITY_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 095 | `CLM-ELECTRICITY_BASICS-C@1` | EXACT_PRIMARY_CHAIN |
| 43 | 096 | `CLM-ELECTRONICS_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 097 | `CLM-ELECTRONICS_BASICS-B@1` | EXACT_PRIMARY_CHAIN |
| 43 | 098 | `CLM-HYDROLOGY_BASICS-C@2` | EXACT_PRIMARY_CHAIN |
| 43 | 099 | `CLM-HYDROPOWER_BASICS-A@1` | EXACT_PRIMARY_CHAIN |
| 43 | 100 | `CLM-M5-ENERGY-GRID-RESILIENCE-D@1` | EXACT_PRIMARY_CHAIN |

## 3. Multi-EU / multi-Source preservation

These are separate graph edges and must not be collapsed into a single “source checked” flag:

- **Batch 42 row 016:** one Claim@1, two Evidence Use records@1, two corresponding Source records@1. Both EUs point to the same Claim and their own Source.
- **Batch 43 row 032:** two EU edges for the health-system resilience Claim, including the WHO EU@2; preserve the earlier distinct EU edge.
- **Batch 43 row 034:** NIST primary evidence plus a separate UNIDO EU/Source edge for manufacturing operations.
- **Batch 43 rows 038–040:** WHO primary edges plus additional NIMH edges for related mental-health information claims.
- **Batch 43 rows 054–055:** UNDRR primary edges plus CDC supplementary edges for risk communication.
- **Batch 43 rows 064–066:** CDC primary edges plus separate WHO-linked EU edges for systems-thinking claims.
- **Batch 43 row 068:** EPA primary edge plus separate WHO edge for wastewater.
- **Batch 43 row 081:** USDA primary chain plus a separate FDA EU/Source edge that may directly support the 40°F/0°F temperature thresholds; FDA passage verification remains required.
- **Batch 43 row 083:** EPA primary chain plus a separate WHO edge; neither edge alone establishes all jurisdiction-specific requirements.
- **Batch 43 row 098:** Claim@2 → EU@2 → Source@2; USGS hydrology section and paragraph locator are present in the current EU. Rights and independent review remain separate.

## 4. Version and duplicate adjudication

### Normalization rule

Normalization was used only for comparison: case-fold and remove separator/punctuation differences from IDs. Canonical IDs, JSON `record_id` values, filenames and references were not rewritten.

For Batch 42 rows 001–068, all 68 Claim JSONs and all 69 EU JSONs were directly read; all 54 distinct Source records were resolved and directly read. Current `record_version`, `record_id`, Claim provenance, EU `claim_ref`, EU `source_ref`, and EU provenance agree with the row chains. Filename separator variants were resolved against the recursive tree; no missing record remained and no JSON identity mismatch was observed.

For Batch 42 rows 069–100 and Batch 43 rows 001–100, the dedicated graph reports document exact primary ID/version matching and the current cross-link/provenance checks. Batch 43 row 098 is the only version-2 primary chain in the cohort; the other primary chains are version 1.

### Duplicate groups

No repeated normalized Claim ID occurs among the 200 report rows. Therefore there is no within-cohort duplicate score conflict to select or merge. This does not settle semantic duplicates between different Claim IDs, alias groups outside this cohort, or duplicate groups in the broader historical ledger.

## 5. Evidence-fit issues remain open despite exact graph identity

Exact primary graph matching is not source-passage acceptance. The following high-priority issues remain explicitly open:

1. **Batch 42 rows 001–020:** source scope, exact locator and source identity problems documented in the individual reports. Priority defects include Health Canada scope expansion (001), evacuation/accessibility overreach (002), floodwater vs sewage (003), smoke-alarm wording (004), ATSDR broad landing page (005), broad/generic evidence links (011–015), incomplete fire-safety taxonomy coverage (016), EPA interactive-page locator gap (017), CPSC source mismatch for generator refuelling (018), CCOHS removal-from-service wording (019), and NLM MeSH not supporting primary/interpretive-source distinction (020).
2. **Batch 42 rows 021–068:** retain the row-specific source-fit issues in the six supplementary packages. In particular, row 021 has an apparent USFA URI/content mismatch (smoke-alarm page vs escape-plan claim); row 023 has an unpinpointed broad DOE source; row 030's NFPA candle-safety source must be checked against the flashlight preference; row 032's secondary AAEES definition is not the primary EPA source; rows 056–057 require direct FDA modality passages; row 062–064 use a broad OCHA homepage for logistics propositions; row 068's WHO participatory-surveillance URI is not an obvious epidemiology definition source.
3. **Batch 42 rows 069–100:** the separate report identifies a large set of generic-EU locator gaps and source-scope limitations; preserve the explicit row dispositions and do not infer passage support from exact chain IDs.
4. **Batch 43 rows 001–100:** preserve the source-fit and editorial issues in the Batch 43 report-body inspection artifact. Key examples include row 012 WHO URI/version-history concern; row 081 USDA vs FDA temperature evidence; rows 077–079 broad digital-health page vs telemedicine definitions; rows 096–097 generic pharmacovigilance evidence; row 100 DOE photovoltaic inverter source vs general power-electronics Claim; and the editorial artifacts in rows 007 and 045–047.
5. **Rights and attribution:** OpenStax CC BY-NC-SA material (including Batch 43 hydrology/plant-biology records) requires a separate rights and attribution decision. A public URL or evidence match is not permission to reuse.
6. **Independent review:** specialist review, independent Human View, formal risk assessment, jurisdictional applicability, editorial review and release gates remain separate. None is satisfied by this crosswalk.

## 6. Assessment and release guardrails

- Historical D/E/B values remain historical report data only.
- Current accepted D/E/B created by this crosswalk: **0**.
- Current worksheet statuses and blank D/E/B fields remain unchanged.
- No Claim was marked source-passage-reviewed, risk-assessed, Human-View-approved or release-cleared by this operation.
- No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record was changed.
- No queue exclusion, priority, risk-domain classification or semantic duplicate adjudication was changed.
- PR #21 remains Open / Draft / Unmerged.
- `main` remains `d58289f319993ede5294a46f4741a506fd2fd710`.

## 7. Scope boundary and next gate

The 200-report cohort is now closed for report-body inspection, normalized Claim-ID joining and primary current graph identity. The broader M13 ledger still has independent work: reconcile the 1,494-Claim inventory and historical score ledger; resolve the 496 generic-EU cohort and 356 residual rows; investigate version-history concerns (including Batch 43 row 012); verify all source passages and locators; perform evidence-diversity and semantic duplicate review; then complete risk, rights, specialist, independent Human View and release gates.

Do not call M13 complete or CLEAN based on this 200-row crosswalk. It closes one report cohort and preserves all remaining substantive review gates.
