# M13 Batch 43 — frozen 100-Claim high-consequence scoring worklist

Date: 2026-10-20  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **27/100 passage reviews recorded; 73 pending.** All machine flags remain routing signals, not scores or findings.

## Frozen selection and reconciliation

- Selection worksheet artifact: `m13-claim-audit-worksheet`, workflow run [39126810240](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/39126810240), ZIP SHA-256 `baf93da378ef181e8e1bd5626a959ee6c9b9a1f149e6080722898c061882ce56`.
- Worksheet's embedded source revision: `81860774bba4d7bcbf1271361b1f13c15eeccdf2`.
- Scored-ledger artifact from the same exact-head Reference Tests run: `m13-scored-claim-reconciliation-ledger`, SHA-256 `6e65f1be44080e34ab387f802fa8d14b024536f90af1390d4c6729a0b854fd4f`.
- At worklist freeze, the exclusion join used the then-current ledger snapshot (359 report rows / 352 normalized comparison IDs). After Batch 43 rows 020–026 were reconciled, the current regression baseline is 385 report rows / 378 normalized IDs. The ledger is an accounting join, not semantic duplicate adjudication.
- Selection includes only currently unscored worksheet Claims in the priority risk domains: emergency/fire/CO, health/medical, water/food/sanitation, electricity/energy, construction/tools/materials, chemicals/hazards, transport/access, shelter/evacuation, communications continuity, and nuclear/radiological. Ordering is by that domain priority, then actionable/prescriptive flag, very-short-claim flag, and literal Claim ID. This is a reproducible routing order, not a risk verdict.
- The worksheet is a frozen candidate-discovery artifact. Before scoring each item, resolve the exact current Claim/Evidence Use/Source IDs and versions in the branch and inspect the canonical linked source passage. Do not infer a source reference if the chain does not resolve.
- No canonical Claim, Evidence Use, or Source JSON changes are authorized by this worklist. Do not add any candidate to the MVP allowlist on the strength of this scoring pass.

## Scoring protocol

For each Claim, inspect the exact proposition, current linked Evidence Use and Source versions, source passage and context, locator, scope, currentness, jurisdiction, independence and risk. Record D/E/B (0–3) with dimension-specific rationales. A broad, inaccessible, mismatched, or partial passage must remain HOLD; do not silently substitute another source. High-consequence Claims require the applicable qualified Human View and remain excluded from a public pilot until all gates pass.

## Frozen candidate set

| # | Claim version | Slice |
|---:|---|---|
| 001 | `CLM-SEPTIC-REDUCE-WATER@1` | `septic-system-emergency` |
| 002 | `CLM-SEPTIC-SEWAGE-CONTACT@1` | `septic-system-emergency` |
| 003 | `CLM-DISASTER_RESPONSE_FEMA_A@1` | `disaster-response-basics` |
| 004 | `CLM-EMERGENCY_MANAGEMENT_BASICS-B@1` | `emergency-management-basics` |
| 005 | `CLM-EMERGENCY_MANAGEMENT_BASICS-C@1` | `emergency-management-basics` |
| 006 | `CLM-FIRE-C@1` | `fire` |
| 007 | `CLM-HUMANITARIAN_LOGISTICS_BASICS-C@1` | `humanitarian-logistics-basics` |
| 008 | `CLM-SEPTIC-PROFESSIONAL-INSPECTION@1` | `septic-system-emergency` |
| 009 | `CLM-WATER-FILTER-LIMITS@1` | `water-filter-assessment` |
| 010 | `CLM-SYSTEMS_THINKING_BASICS-D@1` | `systems-thinking-basics` |
| 011 | `CLM-WOODWORKING_BASICS-D@1` | `woodworking-basics` |
| 012 | `CLM_WATER_QUALITY_WHO_A@1` | `water-quality-basics` |
| 013 | `CLM-PLANT_PATHOLOGY_BASICS-A@1` | `plant-pathology-basics` |
| 014 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-B@1` | `disaster-behavioral-health-basics` |
| 015 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-C@1` | `disaster-behavioral-health-basics` |
| 016 | `CLM-ENTOMOLOGY_BASICS-B@1` | `entomology-basics` |
| 017 | `CLM-ENTOMOLOGY_BASICS-C@1` | `entomology-basics` |
| 018 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-B@1` | `environmental-health-basics` |
| 019 | `CLM-ERGONOMICS_BASICS-A@1` | `ergonomics-basics` |
| 020 | `CLM-FOOD_SECURITY_BASICS-D@1` | `food-security-basics` |
| 021 | `CLM-HEALTH_ECONOMICS_BASICS-A@1` | `health-economics-basics` |
| 022 | `CLM-HEALTH_ECONOMICS_BASICS-B@1` | `health-economics-basics` |
| 023 | `CLM-HEALTH_ECONOMICS_BASICS-C@1` | `health-economics-basics` |
| 024 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-A@1` | `health-technology-assessment-basics` |
| 025 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-B@1` | `health-technology-assessment-basics` |
| 026 | `CLM-HEALTH_TECHNOLOGY_ASSESSMENT_BASICS-C@1` | `health-technology-assessment-basics` |
| 027 | `CLM-HISTORY_OF_MEDICINE-A@1` | `history-of-medicine-basics` |
| 028 | `CLM-HISTORY_OF_MEDICINE-B@1` | `history-of-medicine-basics` |
| 029 | `CLM-INSPECTION_BASICS-A@1` | `inspection-basics` |
| 030 | `CLM-INSPECTION_BASICS-B@1` | `inspection-basics` |
| 031 | `CLM-INSPECTION_BASICS-C@1` | `inspection-basics` |
| 032 | `CLM-M4-HEALTH-RESILIENCE-A@1` | `health-systems-basics` |
| 033 | `CLM-M5-ENVIRONMENTAL-WASTEWATER-D@1` | `environmental-engineering-basics` |
| 034 | `CLM-MANUFACTURING_BASICS-B@1` | `manufacturing-basics` |
| 035 | `CLM-MEDICAL_DEVICES_BASICS-A@1` | `medical-devices-basics` |
| 036 | `CLM-MEDICAL_DEVICES_BASICS-B@1` | `medical-devices-basics` |
| 037 | `CLM-MEDICAL_DEVICES_BASICS-C@1` | `medical-devices-basics` |
| 038 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-A@1` | `mental-health-information-boundaries` |
| 039 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-B@1` | `mental-health-information-boundaries` |
| 040 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-C@1` | `mental-health-information-boundaries` |
| 041 | `CLM-MENTAL_HEALTH_INFORMATION_BOUNDARIES-D@1` | `mental-health-information-boundaries` |
| 042 | `CLM-NUTRITION_BASICS-A@1` | `nutrition-basics` |
| 043 | `CLM-NUTRITION_BASICS-B@1` | `nutrition-basics` |
| 044 | `CLM-NUTRITION_BASICS-D@1` | `nutrition-basics` |
| 045 | `CLM-OCCUPATIONAL_SAFETY_BASICS-A@1` | `occupational-safety-basics` |
| 046 | `CLM-OCCUPATIONAL_SAFETY_BASICS-B@1` | `occupational-safety-basics` |
| 047 | `CLM-OCCUPATIONAL_SAFETY_BASICS-C@1` | `occupational-safety-basics` |
| 048 | `CLM-PHYSIOLOGY_BASICS-A@1` | `physiology-basics` |
| 049 | `CLM-PLANT_PATHOLOGY_BASICS-B@1` | `plant-pathology-basics` |
| 050 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-A@1` | `public-health-ethics-basics` |
| 051 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-B@1` | `public-health-ethics-basics` |
| 052 | `CLM-PUBLIC_HEALTH_ETHICS_BASICS-C@1` | `public-health-ethics-basics` |
| 053 | `CLM-PUBLIC_HEALTH_SURVEILLANCE_BASICS-D@1` | `public-health-surveillance-basics` |
| 054 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-B@1` | `public-risk-communication-basics` |
| 055 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-C@1` | `public-risk-communication-basics` |
| 056 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-D@1` | `public-risk-communication-basics` |
| 057 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-A@1` | `scientific-publishing-basics` |
| 058 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-B@1` | `scientific-publishing-basics` |
| 059 | `CLM-SCIENTIFIC_PUBLISHING_BASICS-C@1` | `scientific-publishing-basics` |
| 060 | `CLM-SOCIAL_POLICY_BASICS-A@1` | `social-policy-basics` |
| 061 | `CLM-SOIL_MICROBIOLOGY_BASICS-A@1` | `soil-microbiology-basics` |
| 062 | `CLM-SOIL_MICROBIOLOGY_BASICS-B@1` | `soil-microbiology-basics` |
| 063 | `CLM-SOIL_MICROBIOLOGY_BASICS-C@1` | `soil-microbiology-basics` |
| 064 | `CLM-SYSTEMS_THINKING_BASICS-A@1` | `systems-thinking-basics` |
| 065 | `CLM-SYSTEMS_THINKING_BASICS-B@1` | `systems-thinking-basics` |
| 066 | `CLM-SYSTEMS_THINKING_BASICS-C@1` | `systems-thinking-basics` |
| 067 | `CLM-VACCINATION_INFORMATION_BASICS-A@1` | `vaccination-information-basics` |
| 068 | `CLM-WASTEWATER_BASICS-A@1` | `wastewater-basics` |
| 069 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_A@1` | `pharmacology-information-basics` |
| 070 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_B@1` | `pharmacology-information-basics` |
| 071 | `CLM_PHARMACOLOGY_INFORMATION_BASICS_C@1` | `pharmacology-information-basics` |
| 072 | `CLM_PUBLIC_HEALTH_SURVEILLANCE_BASICS_A@1` | `public-health-surveillance-basics` |
| 073 | `CLM_REHABILITATION_BASICS_A@1` | `rehabilitation-basics` |
| 074 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_A@1` | `reproductive-health-information-boundaries` |
| 075 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_B@1` | `reproductive-health-information-boundaries` |
| 076 | `CLM_REPRODUCTIVE_HEALTH_INFORMATION_BOUNDARIES_C@1` | `reproductive-health-information-boundaries` |
| 077 | `CLM_TELEMEDICINE_BASICS_A@1` | `telemedicine-basics` |
| 078 | `CLM_TELEMEDICINE_BASICS_B@1` | `telemedicine-basics` |
| 079 | `CLM_TELEMEDICINE_BASICS_C@1` | `telemedicine-basics` |
| 080 | `CLM_WATER_QUALITY_BASICS_A@1` | `water-quality-basics` |
| 081 | `CLM-FOOD-TARGET-TEMP@1` | `power-outage-food` |
| 082 | `CLM-SEED-DRY-STORAGE@1` | `seed-storage-basics` |
| 083 | `CLM-WASTEWATER_BASICS-C@1` | `wastewater-basics` |
| 084 | `CLM-WATER_INFRASTRUCTURE_BASICS-A@1` | `water-infrastructure-basics` |
| 085 | `CLM-WATER_INFRASTRUCTURE_BASICS-B@1` | `water-infrastructure-basics` |
| 086 | `CLM-WATER_INFRASTRUCTURE_BASICS-C@1` | `water-infrastructure-basics` |
| 087 | `CLM_MARINE_BIOLOGY_BASICS_B@1` | `marine-biology-basics` |
| 088 | `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-A@1` | `developmental-biology-basics` |
| 089 | `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-B@1` | `developmental-biology-basics` |
| 090 | `CLM-ELECTRICAL_MACHINES_BASICS-A@1` | `electrical-machines-basics` |
| 091 | `CLM-ELECTRICAL_MACHINES_BASICS-B@1` | `electrical-machines-basics` |
| 092 | `CLM-ELECTRICAL_MACHINES_BASICS-C@1` | `electrical-machines-basics` |
| 093 | `CLM-ELECTRICITY_BASICS-A@1` | `electricity-basics` |
| 094 | `CLM-ELECTRICITY_BASICS-B@1` | `electricity-basics` |
| 095 | `CLM-ELECTRICITY_BASICS-C@1` | `electricity-basics` |
| 096 | `CLM-ELECTRONICS_BASICS-A@1` | `electronics-basics` |
| 097 | `CLM-ELECTRONICS_BASICS-B@1` | `electronics-basics` |
| 098 | `CLM-HYDROLOGY_BASICS-C@2` | `hydrology-basics` |
| 099 | `CLM-HYDROPOWER_BASICS-A@1` | `hydropower-basics` |
| 100 | `CLM-M5-ENERGY-GRID-RESILIENCE-D@1` | `energy-systems-basics` |

## Progress

- Rows 001–027 have separate passage-review reports and explicit D/E/B scores.
- Rows 028–100 remain pending; do not infer clearance from the candidate's presence in this frozen list.
- Batch closure requires all 100 reports, reconciled score-ledger regression expectations, then the planned exact-head checkpoint checks. No full CI is run after each individual report.
