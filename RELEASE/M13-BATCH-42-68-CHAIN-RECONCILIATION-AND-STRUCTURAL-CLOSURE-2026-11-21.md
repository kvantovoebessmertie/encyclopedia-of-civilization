# M13 Batch 42 — Closure of remaining 68 canonical Claim → EU → Source chains

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Audit base commit: `dd1cd26fa01578770d8b1cc0454c2d346644698c`  
Scope: Batch 42 report rows 001–068. This document records a structural, identity, version and linkage audit. It is not a new D/E/B evaluation, human review, rights review or release approval.

## Result

**68/68 rows structurally reconciled.** The remaining 68 report rows have now been joined against the current branch's canonical record tree.

- Report rows inspected: **68/68**
- Distinct record IDs represented: **191**
- Chain slots: **206** (68 Claims, 69 Evidence Use records, 69 Source references)
- Claim records directly read: **68**
- Evidence Use records directly read: **69**
- Distinct Source records resolved and directly read: **54**
- Expected record files missing after separator-normalized filename lookup: **0**
- Claim record identity/version mismatches: **0**
- Evidence Use identity/version mismatches: **0**
- Claim → Evidence Use `claim_ref` mismatches: **0**
- Evidence Use → Source `source_ref` mismatches: **0**
- Claim provenance → Source mismatches: **0**
- Evidence Use provenance → Source mismatches: **0**
- Version mismatches within the 68 report chains: **0**
- Multi-EU case: row 016, with two distinct Evidence Use records and two corresponding Source records. Both EUs point to the same Claim@1 and their own Source@1.

All chain records resolve to version `1` at this audit base. The exact `record_id` values in JSON match the IDs in the report chains after filename normalization. Some filenames use hyphens where the record IDs use underscores (or vice versa); this is a path-resolution normalization only. It is not authorization to rename records or rewrite IDs.

## Row-level master crosswalk — Batch 42 rows 001–068

| Row | Claim | Evidence Use record(s) | Source record(s) | Chain shape |
|---:|---|---|---|---|
| 001 | `CLM-FOOD-NO-OUTDOOR-FREEZER@1` | `EU-FOOD-NO-OUTDOOR-FREEZER@1` | `SRC-HEALTH-CANADA-POWER-OUTAGE-2026@1` | 1:1 |
| 002 | `CLM-FIRE-B@1` | `EU-FIRE-B@1` | `SRC-FIRE@1` | 1:1 |
| 003 | `CLM-FLOOD-FOOD-CONTACT@1` | `EU-FLOOD-FOOD-CONTACT@1` | `SRC-CDC-FLOOD-FOOD-2025@1` | 1:1 |
| 004 | `CLM-HOME-FIRE-SMOKE-ALARMS@1` | `EU-HOME-FIRE-SMOKE-ALARMS@1` | `SRC-USFA-HOME-FIRE-2026@1` | 1:1 |
| 005 | `CLM_TOXICOLOGY_BASICS_B@1` | `EU_TOXICOLOGY_BASICS_B@1` | `SRC_TOXICOLOGY_BASICS@1` | 1:1 |
| 006 | `CLM-HANDWASH-20SEC@1` | `EU-HANDWASH-20SEC@1` | `SRC-CDC-HAND-HYGIENE-EMERGENCY-2024@1` | 1:1 |
| 007 | `CLM-WATER-STORAGE-CONTAINER@1` | `EU-WATER-STORAGE-CONTAINER@1` | `SRC-CDC-WATER-STORAGE-2025@1` | 1:1 |
| 008 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-A@1` | `EU-ENVIRONMENTAL_HEALTH_BASICS-A@1` | `SRC-ENVIRONMENTAL_HEALTH_BASICS@1` | 1:1 |
| 009 | `CLM-FIRE-A@1` | `EU-FIRE-A@1` | `SRC-FIRE@1` | 1:1 |
| 010 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-B@1` | `EU-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-B@1` | `SRC-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS@1` | 1:1 |
| 011 | `CLM-LIGHTING-CANDLE-UNATTENDED@1` | `EU-LIGHTING-CANDLE-UNATTENDED@1` | `SRC-USFA-CANDLE-SAFETY-2026@1` | 1:1 |
| 012 | `CLM-FLOOD-CLEAN-DISINFECT@1` | `EU-FLOOD-CLEAN-DISINFECT@1` | `SRC-CDC-FLOOD-CLEANUP-2026@1` | 1:1 |
| 013 | `CLM_WASTEWATER_ENGINEERING_BASICS_B@1` | `EU_WASTEWATER_ENGINEERING_BASICS_B@1` | `SRC_WASTEWATER_ENGINEERING_BASICS@1` | 1:1 |
| 014 | `CLM-IPAWS-ALERT-CONTENT@1` | `EU-IPAWS-ALERT-CONTENT@1` | `SRC-PUBLIC-ALERT-GUIDANCE@1` | 1:1 |
| 015 | `CLM_FIRE_SAFETY_BASICS_A@1` | `EU_FIRE_SAFETY_BASICS_A@1` | `SRC_FIRE_SAFETY_BASICS@1` | 1:1 |
| 016 | `CLM_FIRE_SAFETY_BASICS_B@1` | `EU_FIRE_SAFETY_BASICS_B@1`<br>`EU_FIRE_SAFETY_BASICS_NFPA@1` | `SRC_FIRE_SAFETY_BASICS@1`<br>`SRC_NFPA_FIRE_SAFETY_BASICS@1` | MULTI-EU / MULTI-SOURCE |
| 017 | `CLM-FLOOD-REENTRY-HAZARD-ESCALATION@1` | `EU-FLOOD-REENTRY-HAZARD-ESCALATION@1` | `SRC-EPA-FLOOD-REENTRY-2026@1` | 1:1 |
| 018 | `CLM-GENERATOR-REFUEL-COOL@1` | `EU-GENERATOR-REFUEL-COOL@1` | `SRC-CPSC-GENERATOR-2026@1` | 1:1 |
| 019 | `CLM-TOOL-DEFECTIVE@1` | `EU-TOOL-DEFECTIVE@1` | `SRC-CCOHS-HAND-TOOLS-2026@1` | 1:1 |
| 020 | `CLM-HISTORY_OF_MEDICINE-C@1` | `EU-HISTORY_OF_MEDICINE-C@1` | `SRC-HISTORY_OF_MEDICINE@1` | 1:1 |
| 021 | `CLM-HOME-FIRE-ESCAPE-PLAN@1` | `EU-HOME-FIRE-ESCAPE-PLAN@1` | `SRC-USFA-HOME-FIRE-2026@1` | 1:1 |
| 022 | `CLM-HOME-FIRE-TWO-WAYS-NFPA@1` | `EU-HOME-FIRE-TWO-WAYS-NFPA@1` | `SRC-NFPA-HOME-FIRE-2026@1` | 1:1 |
| 023 | `CLM_POWER_ELECTRONICS_BASICS_C@1` | `EU_POWER_ELECTRONICS_BASICS_C@1` | `SRC_POWER_ELECTRONICS_BASICS@1` | 1:1 |
| 024 | `CLM-FOOD-OUTAGE-THRESHOLD-BOUNDARY@1` | `EU-FOOD-OUTAGE-THRESHOLD-BOUNDARY@1` | `SRC-FDA-POWER-OUTAGE-2026@1` | 1:1 |
| 025 | `CLM_WASTEWATER_TREATMENT_BASICS_A@1` | `EU_WASTEWATER_TREATMENT_BASICS_A@1` | `SRC_WASTEWATER_TREATMENT_BASICS@1` | 1:1 |
| 026 | `CLM-M4-CONSTRUCTION-HAZARDS-A@1` | `EU-CLM-M4-CONSTRUCTION-HAZARDS-A@1` | `SRC-M4-CONSTRUCTION-HAZARDS-OSHA@1` | 1:1 |
| 027 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-D@1` | `EU-DISASTER_BEHAVIORAL_HEALTH_BASICS-D-WHO@1` | `SRC-WHO-MENTAL-HEALTH-EMERGENCIES-2025@1` | 1:1 |
| 028 | `CLM-ELECTRONICS_BASICS-C@1` | `EU-ELECTRONICS_BASICS-C@1` | `SRC-ELECTRONICS_BASICS@1` | 1:1 |
| 029 | `CLM-ALERTS-ENABLE-RESPOND@1` | `EU-ALERTS-ENABLE-RESPOND@1` | `SRC-RED-CROSS-ALERTS-2026@1` | 1:1 |
| 030 | `CLM-LIGHTING-FLASHLIGHT-OUTAGE@1` | `EU-LIGHTING-FLASHLIGHT-OUTAGE@1` | `SRC-NFPA-CANDLE-SAFETY-2026@1` | 1:1 |
| 031 | `CLM-EMERGENCY_MANAGEMENT_BASICS-A@1` | `EU-EMERGENCY_MANAGEMENT_BASICS-A@1` | `SRC-EMERGENCY_MANAGEMENT_BASICS@1` | 1:1 |
| 032 | `CLM_ENVIRONMENTAL_ENGINEERING_BASICS_A@1` | `EU_ENVIRONMENTAL_ENGINEERING_BASICS_A@1` | `SRC_ENVIRONMENTAL_ENGINEERING_BASICS@1` | 1:1 |
| 033 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-C@1` | `EU-ENVIRONMENTAL_HEALTH_BASICS-C@1` | `SRC-ENVIRONMENTAL_HEALTH_BASICS@1` | 1:1 |
| 034 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-A@1` | `EU-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-A@1` | `SRC-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS@1` | 1:1 |
| 035 | `CLM-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-C@1` | `EU-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS-C@1` | `SRC-FIRE_PROTECTION_AND_LIFE_SAFETY_BASICS@1` | 1:1 |
| 036 | `CLM-FOOD_DISTRIBUTION_BASICS-A@1` | `EU-FOOD_DISTRIBUTION_BASICS-A@1` | `SRC-FOOD_DISTRIBUTION_BASICS@1` | 1:1 |
| 037 | `CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1` | `EU_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B@1` | `SRC_WB_HUMAN_SETTLEMENT_SYSTEMS_BASICS@1` | 1:1 |
| 038 | `CLM-MATERIALS_SCIENCE_BASICS-A@1` | `EU-MATERIALS_SCIENCE_BASICS-A@1` | `SRC-MATERIALS_SCIENCE_BASICS@1` | 1:1 |
| 039 | `CLM-MIGRATION_AND_MOBILITY_BASICS-A@1` | `EU-MIGRATION_AND_MOBILITY_BASICS-A@1` | `SRC-MIGRATION_AND_MOBILITY_BASICS@1` | 1:1 |
| 040 | `CLM-NUTRITION_BASICS-C@1` | `EU-NUTRITION_BASICS-C@1` | `SRC-NUTRITION_BASICS@1` | 1:1 |
| 041 | `CLM-PAPERMAKING_BASICS-A@1` | `EU-PAPERMAKING_BASICS-A@1` | `SRC-PAPERMAKING_BASICS-MFA@1` | 1:1 |
| 042 | `CLM-PARTICLE_PHYSICS_BASICS-A@1` | `EU-PARTICLE_PHYSICS_BASICS-A@1` | `SRC-PARTICLE_PHYSICS_BASICS@1` | 1:1 |
| 043 | `CLM_PATHOLOGY_BASICS_A@1` | `EU_PATHOLOGY_BASICS_A@1` | `SRC_PATHOLOGY_BASICS@1` | 1:1 |
| 044 | `CLM-FOOD-FREEZER-48H@1` | `EU-FOOD-FREEZER-48H@1` | `SRC-USDA-POWER-OUTAGE-2024@1` | 1:1 |
| 045 | `CLM-FOOD-REFRIGERATOR-4H@1` | `EU-FOOD-REFRIGERATOR-4H@1` | `SRC-USDA-POWER-OUTAGE-2024@1` | 1:1 |
| 046 | `CLM-PUBLIC_RISK_COMMUNICATION_BASICS-A@1` | `EU-PUBLIC_RISK_COMMUNICATION_BASICS-A@1` | `SRC-PUBLIC_RISK_COMMUNICATION_BASICS@1` | 1:1 |
| 047 | `CLM-SLEEP_BASICS-A@1` | `EU-SLEEP_BASICS-A@1` | `SRC-SLEEP_BASICS@1` | 1:1 |
| 048 | `CLM-SLEEP_BASICS-C@1` | `EU-SLEEP_BASICS-C@1` | `SRC-SLEEP_BASICS@1` | 1:1 |
| 049 | `CLM-CDC-FOOD-GRADE-CONTAINER@1` | `EU-CLAIM-SOURCE@1` | `SRC-CDC-WATER-STORAGE-ATTRIBUTION-2025@1` | 1:1 |
| 050 | `CLM-URBAN_PLANNING_BASICS-A@1` | `EU-URBAN_PLANNING_BASICS-A@1` | `SRC-URBAN_PLANNING_BASICS@1` | 1:1 |
| 051 | `CLM-WASTEWATER_BASICS-B@1` | `EU-WASTEWATER_BASICS-B@1` | `SRC-WASTEWATER_BASICS@1` | 1:1 |
| 052 | `CLM-WATER-FILTER-WHO-PERFORMANCE@1` | `EU-WATER-FILTER-WHO-PERFORMANCE@1` | `SRC-WHO-HWT-EVALUATION@1` | 1:1 |
| 053 | `CLM-LIGHTING-CANDLE-CHILDREN@1` | `EU-LIGHTING-CANDLE-CHILDREN@1` | `SRC-USFA-CANDLE-SAFETY-2026@1` | 1:1 |
| 054 | `CLM-FLOOD-CLEAN-PROTECT@1` | `EU-FLOOD-CLEAN-PROTECT@1` | `SRC-CDC-FLOOD-CLEANUP-2026@1` | 1:1 |
| 055 | `CLM-TOOL-INSPECT@1` | `EU-TOOL-INSPECT@1` | `SRC-OSHA-HAND-TOOLS-2026@1` | 1:1 |
| 056 | `CLM_MEDICAL_IMAGING_BASICS_B@1` | `EU_MEDICAL_IMAGING_BASICS_B@1` | `SRC_MEDICAL_IMAGING_BASICS@1` | 1:1 |
| 057 | `CLM_MEDICAL_IMAGING_BASICS_C@1` | `EU_MEDICAL_IMAGING_BASICS_C@1` | `SRC_MEDICAL_IMAGING_BASICS@1` | 1:1 |
| 058 | `CLM-PAPERMAKING_BASICS-D@1` | `EU-PAPERMAKING_BASICS-D@1` | `SRC-PAPERMAKING_BASICS-TECHNIKMUSEUM@1` | 1:1 |
| 059 | `CLM_CLINICAL_TRIALS_BASICS_A@1` | `EU_CLINICAL_TRIALS_BASICS_A@1` | `SRC_CLINICAL_TRIALS_BASICS@1` | 1:1 |
| 060 | `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-A@1` | `EU-DISASTER_BEHAVIORAL_HEALTH_BASICS-A@1` | `SRC-DISASTER_BEHAVIORAL_HEALTH_BASICS@1` | 1:1 |
| 061 | `CLM-DISASTER_RECOVERY_BASICS-D@1` | `EU-DISASTER_RECOVERY_BASICS-D@1` | `SRC-UNDRR-RECOVERY-2026@1` | 1:1 |
| 062 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A@1` | `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A@1` | `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1` | 1:1 |
| 063 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_B@1` | `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_B@1` | `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1` | 1:1 |
| 064 | `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_C@1` | `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_C@1` | `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1` | 1:1 |
| 065 | `CLM-IPAWS-ALERT-ELEMENTS@1` | `EU-IPAWS-ALERT-ELEMENTS@1` | `SRC-PUBLIC-ALERT-GUIDANCE@1` | 1:1 |
| 066 | `CLM-LIGHTING-EXTINGUISH@1` | `EU-LIGHTING-EXTINGUISH@1` | `SRC-USFA-CANDLE-SAFETY-2026@1` | 1:1 |
| 067 | `CLM-ENVIRONMENTAL_HEALTH_BASICS-D@1` | `EU-ENVIRONMENTAL_HEALTH_BASICS-D-EPA@1` | `SRC-EPA-ENVIRONMENTAL-EXPOSURE-2026@1` | 1:1 |
| 068 | `CLM-EPIDEMIOLOGY_BASICS-D@1` | `EU-EPIDEMIOLOGY_BASICS-D-WHO@1` | `SRC-WHO-EPIDEMIOLOGY-2024@1` | 1:1 |

## Structural interpretation

The join confirms that each row's current Claim version, its Evidence Use record(s), and the Source version(s) referenced by those EUs agree at the identifier and version level. It also confirms that the Claim provenance and EU provenance point to the same Source identities used in the EUs.

This is a **structural chain pass only**. It does not convert the earlier row-level dispositions from HOLD to PASS. It does not imply that the cited page actually supports every clause, that an exact locator exists, or that the source is current, independent, jurisdictionally applicable, rights-cleared, or fit for publication.

## Evidence-fit and source-integrity issues preserved for remediation

The following issues remain open and are not resolved by the structural join:

1. **Rows 001–005:** scope and locator defects remain. Row 001 broadens Health Canada's frozen-food recommendation into refrigerator/outdoor-temperature claims; row 002 combines evacuation routes with shelter and accessibility provisions not mapped to exact passages; row 003 extends floodwater support to sewage water; row 004 compresses USFA's bedroom/sleeping-area placement distinctions; row 005 uses a broad ATSDR landing page while the directly relevant toxicology passages are on separate resources.
2. **Rows 011–020:** row 011's exact USFA URI was not directly retrievable in the previous passage review; row 012's stored CDC URI likewise needs direct inspection; row 013 has a broad EPA overview and generic EU; row 014's FEMA PDF passage supports the summary but the EU has no pinpoint; row 015's USFA landing page does not directly substantiate the full response/evacuation clause; row 016's two sources support only parts of the listed fire-safety categories; row 017 relies on inaccessible interactive detail in the canonical EPA page, with adjacent EPA pages as corroboration; row 018 has a material source mismatch because the linked CPSC page does not contain the refuelling/cooling instruction (a different CPSC release does); row 019's linked CCOHS page supports inspection and repair/replacement but not the stronger removal-from-service clause; row 020's NLM MeSH entry does not establish the primary/interpretive-source distinction.
3. **Rows 021–024:** row 021's current Source identity/URI is the USFA smoke-alarm page while the EU material describes an escape-plan page; row 022's NFPA URI is broad and the EU lacks an exact passage; row 023's DOE page is plausible but does not yet pinpoint every listed power-electronics application domain; row 024's FDA support is plausible/direct at summary level but lacks a canonical exact locator.
4. **Rows 025–043:** wastewater, construction, behavioral health, electronics, emergency-management, environmental-engineering, food-distribution, settlement systems, materials science, migration, nutrition, papermaking, particle physics and pathology claims still require source-specific passage review. Generic descriptions and broad index/landing-page sources must not be treated as pinpoint evidence.
5. **Rows 044–052:** the USDA freezer/refrigerator thresholds and WHO household-water-treatment performance are strong candidate matches, but canonical EU locator precision and source-version history still need to be checked; the risk-communication, sleep, CDC container-attribution, urban-planning and wastewater claims retain varying degrees of generic or broad-source support.
6. **Rows 053–060:** candle/child safety, flood-cleanup PPE, tool inspection, medical-imaging limits and selection, paper-use boundaries, clinical-trial definitions and disaster behavioral-health scope require exact passage locators and/or specialist boundaries as specified in their row reports.
7. **Rows 061–068:** recovery and alert-element claims have plausible official support; disaster-response-logistics EUs currently point to the broad OCHA homepage and need precise supporting pages; row 067's EPA exposure pathway needs an exact section/figure locator; row 068's WHO URI is a participatory-surveillance publication, not an obviously direct epidemiology definition source. Row 068 remains a source-identity/source-fit defect candidate.

## Version and mutation controls

- No canonical Claim, Evidence Use or Source record was modified.
- No current D/E/B assessment was created or imported by this join.
- Historical report scores remain historical and provisional.
- No row received publication or release eligibility.
- `main` remains unchanged at `d58289f319993ede5294a46f4741a506fd2fd710`.
- PR #21 remains Open / Draft / Unmerged.
- This document is an audit artifact only; it does not authorize canonical record correction.

## Next gate

With the 68/68 structural join closed, the unified 200-report crosswalk is now complete in `M13-BATCH-42-43-MASTER-NORMALIZED-CROSSWALK-200-REPORTS-2026-11-21.md`: 200/200 report rows, 200 unique normalized Claim IDs, zero duplicate normalized Claim-ID groups, and 200/200 primary graph matches. The next work is substantive rather than structural: adjudicate the source-fit/locator queue in `M13-BATCH-42-43-TARGETED-SOURCE-FIT-ADJUDICATION-2026-11-21.md`; then complete semantic duplicate and evidence-diversity checks, source-history review, risk/rights/specialist gates and independent Human View. The 200-row crosswalk does not close the broader 1,494-Claim ledger.
