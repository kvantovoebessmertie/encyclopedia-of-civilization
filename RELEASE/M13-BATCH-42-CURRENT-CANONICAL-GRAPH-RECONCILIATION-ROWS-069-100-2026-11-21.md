# M13 Batch 42 — current canonical graph reconciliation, rows 069–100

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reconciliation base: branch tree at `f419db7780574aa99dc7bc429e8becc49f32c148`  
Scope: all 32 historical scored report rows 069–100 and their current canonical Claim, Evidence Use and Source records.  
Method: resolved canonical paths from the recursive Git tree; fetched and read each Claim and Evidence Use record; fetched each distinct Source record; compared record IDs, record versions, Claim↔EU references, EU↔Source references, and Claim provenance source references.  
Mutation boundary: **read-only canonical reconciliation. No canonical record changed.**

## 1. Executive result

**32/32 rows have an exact current canonical ID-and-version chain at the inspected branch revision.**

For each row:
- historical report Claim ID and version match the current canonical Claim record ID and `record_version=1`;
- historical report Evidence Use ID and version match the current canonical Evidence Use record ID and `record_version=1`;
- historical report Source ID and version match the current canonical Source record ID and `record_version=1`;
- current EU `claim_ref` points to the corresponding Claim at version 1;
- current EU `source_ref` points to the corresponding Source at version 1;
- current Claim provenance `created_from` points to the same Source at version 1.

This establishes **exact-version graph identity**, not evidence adequacy. It does not authorize reuse or acceptance of any historical D/E/B score. All current Evidence Use records inspected remain non-pinpointed: their `material.description` is generic or a high-level summary, while the Source records generally preserve only source identity and a broad URI. Therefore, the rows remain **HOLD / current E locator remediation pending**.

## 2. Row-by-row exact chain

| Row | Current Claim ID @version | Current Evidence Use ID @version | Current Source ID @version | Graph result | Main current evidence limitation |
|---|---|---|---|---|---|
| 069 | `CLM_EPIGENETICS_BASICS_B@1` | `EU_EPIGENETICS_BASICS_B@1` | `SRC_EPIGENETICS_BASICS@1` | EXACT | EU says only “within claimed material”; no glossary definition locator. |
| 070 | `CLM-HEAT-EXHAUSTION-SIGNS@1` | `EU-HEAT-EXHAUSTION-SIGNS@1` | `SRC-CDC-EXTREME-HEAT-2026@1` | EXACT | EU summary names heavy sweating, nausea, fainting and worsening symptoms; dizziness absent; no CDC section locator. |
| 071 | `CLM-HEAT-HEATSTROKE-EMERGENCY@1` | `EU-HEAT-HEATSTROKE-EMERGENCY@1` | `SRC-NWS-EXTREME-HEAT-2026@1` | EXACT | EU only supports emergency nature and rapid cooling; no symptom/action-sequence pinpoint. |
| 072 | `CLM-HEAT-STAY-COOL-HYDRATED@1` | `EU-HEAT-STAY-COOL-HYDRATED@1` | `SRC-CDC-EXTREME-HEAT-2026@1` | EXACT | EU summarizes cool/hydrated advice but has no exact CDC locator. |
| 073 | `CLM_FIRE_SAFETY_BASICS_C@1` | `EU_FIRE_SAFETY_BASICS_C@1` | `SRC_FIRE_SAFETY_BASICS@1` | EXACT | EU is generic; broad USFA prevention URI does not map the full multi-factor list. |
| 074 | `CLM-FLOOD-A@1` | `EU-FLOOD-A@1` | `SRC-FLOOD@1` | EXACT | EU identifies Ready.gov/FEMA generally; no passages for both official alerts and safe locations. |
| 075 | `CLM-FLOOD-REENTRY-SAFE@1` | `EU-FLOOD-REENTRY-SAFE@1` | `SRC-EPA-FLOOD-REENTRY-2026@1` | EXACT | EU summarizes re-entry assessment/protection but has no electrical, structural or PPE passage locators. |
| 076 | `CLM-FLOOD-FOOD-OPEN-PACKAGE@1` | `EU-FLOOD-FOOD-OPEN-PACKAGE@1` | `SRC-CDC-FLOOD-FOOD-2025@1` | EXACT | EU supports non-waterproof packaging/floodwater; Claim adds sewage water and “not hermetically sealed.” |
| 077 | `CLM_GENETIC_ENGINEERING_BASICS_B@1` | `EU_GENETIC_ENGINEERING_BASICS_B@1` | `SRC_GENETIC_ENGINEERING_BASICS@1` | EXACT | EU generic; WHO human-genome-editing page is narrower than all genetic-engineering application domains. |
| 078 | `CLM_GEOCHEMISTRY_BASICS_A@1` | `EU_GEOCHEMISTRY_BASICS_A@1` | `SRC_GEOCHEMISTRY_BASICS@1` | EXACT | EU generic; broad USGS geochemistry URI has no definition passage locator. |
| 079 | `CLM_GEOCHEMISTRY_BASICS_C@1` | `EU_GEOCHEMISTRY_BASICS_C@1` | `SRC_GEOCHEMISTRY_BASICS@1` | EXACT | EU generic; no passage maps sampling context, analytical methods and elemental behaviour. |
| 080 | `CLM_GEOTECHNICAL_ENGINEERING_BASICS_C@1` | `EU_GEOTECHNICAL_ENGINEERING_BASICS_C@1` | `SRC_GEOTECHNICAL_ENGINEERING_BASICS@1` | EXACT | EU generic; FHWA landing page does not pinpoint technical evidence for the full list. |
| 081 | `CLM-TOOL-PPE@1` | `EU-TOOL-PPE@1` | `SRC-OSHA-HAND-TOOLS-2026@1` | EXACT | EU gives general OSHA summary; no task/hazard-specific passage locator. |
| 082 | `CLM_HEALTH_SYSTEMS_BASICS_A@1` | `EU_HEALTH_SYSTEMS_BASICS_A@1` | `SRC_HEALTH_SYSTEMS_BASICS@1` | EXACT | EU generic; exact WHO “primary intent” definition passage not recorded. |
| 083 | `CLM_HEALTH_SYSTEMS_BASICS_B@1` | `EU_HEALTH_SYSTEMS_BASICS_B@1` | `SRC_HEALTH_SYSTEMS_BASICS@1` | EXACT | EU generic; no WHO framework/table locator for the complete functions list. |
| 084 | `CLM_HEALTH_SYSTEMS_BASICS_C@1` | `EU_HEALTH_SYSTEMS_BASICS_C@1` | `SRC_HEALTH_SYSTEMS_BASICS@1` | EXACT | EU generic; no passage for component interaction/context/performance relationship. |
| 085 | `CLM-HOME-FIRE-LEAVE-STAY-OUT@1` | `EU-HOME-FIRE-LEAVE-STAY-OUT@1` | `SRC-NFPA-HOME-FIRE-2026@1` | EXACT | EU summary matches core instruction but has no exact NFPA section locator. |
| 086 | `CLM_INDUSTRIAL_PROCESS_SAFETY_BASICS_A@1` | `EU_INDUSTRIAL_PROCESS_SAFETY_BASICS_A@1` | `SRC_INDUSTRIAL_PROCESS_SAFETY_BASICS@1` | EXACT | EU generic; no OSHA PSM passage locator for scope and terminology. |
| 087 | `CLM_MEDICAL_IMAGING_BASICS_A@1` | `EU_MEDICAL_IMAGING_BASICS_A@1` | `SRC_MEDICAL_IMAGING_BASICS@1` | EXACT | EU generic; no FDA passage for both internal structures and body functions. |
| 088 | `CLM_NUTRITION_SCIENCE_BASICS_A@1` | `EU_NUTRITION_SCIENCE_BASICS_A@1` | `SRC_NUTRITION_SCIENCE_BASICS@1` | EXACT | EU generic; NIH ODS portal is not a pinpointed disciplinary definition. |
| 089 | `CLM_NUTRITION_SCIENCE_BASICS_B@1` | `EU_NUTRITION_SCIENCE_BASICS_B@1` | `SRC_NUTRITION_SCIENCE_BASICS@1` | EXACT | EU generic; no specific NIH fact-sheet passages for all listed nutrient roles. |
| 090 | `CLM_NUTRITION_SCIENCE_BASICS_C@1` | `EU_NUTRITION_SCIENCE_BASICS_C@1` | `SRC_NUTRITION_SCIENCE_BASICS@1` | EXACT | EU generic; no direct guidance passage for all listed contextual factors. |
| 091 | `CLM_OCCUPATIONAL_HEALTH_BASICS_A@1` | `EU_OCCUPATIONAL_HEALTH_BASICS_A@1` | `SRC_OCCUPATIONAL_HEALTH_BASICS@1` | EXACT | EU generic; WHO Overview is the apparent match but the heading locator is absent. |
| 092 | `CLM_OCCUPATIONAL_HEALTH_BASICS_B@1` | `EU_OCCUPATIONAL_HEALTH_BASICS_B@1` | `SRC_OCCUPATIONAL_HEALTH_BASICS@1` | EXACT | EU generic; WHO Overview discipline list needs reproducible pinpoint. |
| 093 | `CLM_OCCUPATIONAL_HEALTH_BASICS_C@1` | `EU_OCCUPATIONAL_HEALTH_BASICS_C@1` | `SRC_OCCUPATIONAL_HEALTH_BASICS@1` | EXACT | EU generic; WHO objectives are relevant but “depends on” is a synthesis without pinpoint. |
| 094 | `CLM-PARTICLE_PHYSICS_BASICS-C@1` | `EU-PARTICLE_PHYSICS_BASICS-C@1` | `SRC-PARTICLE_PHYSICS_BASICS@1` | EXACT | EU generic; CERN “Forces and carrier particles” locator is absent. |
| 095 | `CLM_PHARMACOVIGILANCE_BASICS_A@1` | `EU_PHARMACOVIGILANCE_BASICS_A@1` | `SRC_PHARMACOVIGILANCE_BASICS@1` | EXACT | EU generic; WHO “What is Pharmacovigilance?” section locator is absent. |
| 096 | `CLM_PHARMACOVIGILANCE_BASICS_B@1` | `EU_PHARMACOVIGILANCE_BASICS_B@1` | `SRC_PHARMACOVIGILANCE_BASICS@1` | EXACT | EU generic; multiple-source/signal-detection proposition lacks pinpoint. |
| 097 | `CLM_PHARMACOVIGILANCE_BASICS_C@1` | `EU_PHARMACOVIGILANCE_BASICS_C@1` | `SRC_PHARMACOVIGILANCE_BASICS@1` | EXACT | EU generic; five-part benefit-risk decision list lacks claim-specific passages. |
| 098 | `CLM-PLANT_BIOLOGY_BASICS-B@1` | `EU-PLANT_BIOLOGY_BASICS-B@1` | `SRC-PLANT_BIOLOGY_BASICS@1` | EXACT | Source URI is already OpenStax §30.5; EU still lacks locator/quotation context; CC BY-NC-SA rights review separate. |
| 099 | `CLM-PLANT_BIOLOGY_BASICS-C@1` | `EU-PLANT_BIOLOGY_BASICS-C@1` | `SRC-PLANT_BIOLOGY_BASICS@1` | EXACT | Source URI is already OpenStax §30.5; EU lacks pinpoint; CC BY-NC-SA rights review separate. |
| 100 | `CLM_POWER_ELECTRONICS_BASICS_A@1` | `EU_POWER_ELECTRONICS_BASICS_A@1` | `SRC_POWER_ELECTRONICS_BASICS@1` | EXACT | EU generic; DOE URI is photovoltaic inverter-focused and narrower than the general Claim. |

## 3. Canonical graph validation details

The fetched records show the same structural pattern across the cohort:
- Claim: `record_type=claim`, `record_version=1`, `publication_status=published`, `completion_status=complete`.
- Evidence Use: `record_type=evidence_use`, `record_version=1`, `publication_status=published`, `completion_status=complete`.
- Source: `record_type=source`, `record_version=1`, `publication_status=published`, `completion_status=complete`.
- EU `claim_ref.version=1` and `source_ref.version=1`; both IDs match the row's Claim and Source.
- Claim provenance `created_from[0].version=1`; Source ID matches the row's Source.
- No missing canonical record, version mismatch, Claim↔EU mismatch or EU↔Source mismatch was observed in the 32 inspected chains.

**Important distinction:** record-level `completion_status=complete` and `publication_status=published` are schema/workflow metadata. They do not prove M13 assessment acceptance, source-passage verification, formal risk assessment, independent Human View, specialist clearance, rights clearance or release approval.

## 4. Reconciliation disposition

| Classification | Count | Meaning |
|---|---:|---|
| Exact historical-to-current Claim/EU/Source ID+version chain | 32 | All three records exist at the exact versions named in the historical report and current cross-links agree. |
| Current EU pinpoint present and independently verified in this pass | 0 | No current EU locator was accepted as a reproducible passage-level pinpoint in this reconciliation. |
| Historical D/E/B accepted into current worksheet | 0 | No score transfer performed. |
| Canonical records changed | 0 | Read-only audit. |
| Rows cleared for release | 0 | All remain HOLD pending evidence, review and release gates. |

The 32 rows can now be marked **exact-version chain recovered/confirmed** in a future controlled reconciliation ledger. They must not be counted as source-passage-reviewed or accepted current assessments. Do not alter the current worksheet's `NOT_YET_REVIEWED` status or blank D/E/B fields based solely on this graph match.

## 5. Prioritized remediation

1. **Safety-critical passage remediation:** rows 070–076, 080–081, 085–086. Verify the exact official source passages, reconcile all words and actions, add reproducible section/page/paragraph locators through authorized canonical change control, and obtain qualified independent Human View.
2. **Source identity/scope correction:** row 077 (WHO human genome editing vs broad genetic engineering); 088–090 (NIH ODS portal vs direct definition/fact-sheet/guidance sources); 100 (photovoltaic inverter page vs general power-electronics statement).
3. **Framework/definition pinpointing:** rows 069, 078–079, 082–084, 087, 091–097.
4. **Rights gate:** rows 098–099 require explicit OpenStax CC BY-NC-SA attribution and commercial/reuse scope review before MVP distribution.
5. Reconcile these 32 exact chains with the master M13 crosswalk and the outstanding Batch42–43 report list. Reduce the outstanding report count only after confirming each row's unique Claim ID and no overlap with already-counted sample/spot-check rows.

## 6. Explicit non-actions

- No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record edited.
- No historical D/E/B copied into the current worksheet.
- No row marked `CONTENT_SCREENED`, `SOURCE_PASSAGE_REVIEWED`, `FORMAL_RISK_ASSESSED`, `HUMAN_VIEW_APPROVED` or release-cleared.
- No queue exclusions or priority changes made.
- No changes to `main`; PR #21 remains Draft and unmerged.
