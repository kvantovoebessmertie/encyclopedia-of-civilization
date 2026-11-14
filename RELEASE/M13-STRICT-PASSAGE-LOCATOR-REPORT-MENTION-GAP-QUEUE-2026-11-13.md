# M13 — strict generic Evidence Use passage/locator report-mention gap queue

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Current source revision: `04ef30d5cb8a48654d03607a6ba5b01eb01bc87c`  
State: **machine-derived routing aid; no canonical edits, no D/E/B changes, no closure.**

## 1. Corrected classification

The first-pass 40-item queue and the subsequent 50-item strict queue were intermediate snapshots. The current successful full-corpus scan supersedes both. The strict classifier counts only filenames explicitly indicating `SOURCE-PASSAGE`, `SOURCE-PINPOINT`, `EVIDENCE-LOCATOR` or `SOURCE-FIT`. It excludes generic-EU inventory/remediation registers and source-identity-only reviews.

The three electrical-safety Evidence Use records were corrected from generic descriptions to Claim-specific NIOSH section pinpoints (v1 → v2). They are no longer generic-description candidates. This reduces the full-corpus generic-EU count from 519 to 516 and reduces the no-passage/locator-filename-signal queue from 50 to 47.

## 2. Current exact scan results

- Generic Evidence Use candidates: **516**.
- Mapped to a Claim: **516/516**; unmapped: **0**.
- Conflicting EU-to-Claim worksheet mappings: **0**.
- Candidates with any M13 report text mention: **516/516**.
- Candidates with a passage/pinpoint/locator/source-fit filename signal: **469/516**.
- Candidates without that filename signal: **47/516**.
- Candidate-level semantic review confirmation from this scan: **0**.
- Canonical Evidence Use locator records corrected in the electrical-safety package: **3**.

The 469 filename signals are discovery hints only. They do not establish that the report substantively reviewed the exact Claim/EU/Source chain. Absence of a signal is not proof that no review exists in a broader report.

## 3. Exact 47-candidate gap-routing list

These are the 47 Claim/EU/Source triples with no matching passage/pinpoint/locator/source-fit filename signal in the scanned M13 report set. Grouping is alphabetical by slice, not risk-ranked.

| Slice | Claim | Evidence Use | Source |
|---|---|---|---|
| acoustics-basics | `CLM-ACOUSTICS_BASICS-C` | `EU-ACOUSTICS_BASICS-C` | `SRC-ACOUSTICS_BASICS` |
| algebra-basics | `CLM-ALGEBRA_BASICS-A` | `EU-ALGEBRA_BASICS-A` | `SRC-ALGEBRA_BASICS` |
| algebra-basics | `CLM-ALGEBRA_BASICS-B` | `EU-ALGEBRA_BASICS-B` | `SRC-ALGEBRA_BASICS` |
| algebra-basics | `CLM-ALGEBRA_BASICS-C` | `EU-ALGEBRA_BASICS-C` | `SRC-ALGEBRA_BASICS` |
| anatomy-basics | `CLM-ANATOMY_BASICS-A` | `EU-ANATOMY_BASICS-A` | `SRC-ANATOMY_BASICS` |
| anatomy-basics | `CLM-ANATOMY_BASICS-B` | `EU-ANATOMY_BASICS-B` | `SRC-ANATOMY_BASICS` |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-A` | `EU-ARCHIVAL_SCIENCE-A` | `SRC-ARCHIVAL_SCIENCE` |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-B` | `EU-ARCHIVAL_SCIENCE-B` | `SRC-ARCHIVAL_SCIENCE` |
| archival-science-basics | `CLM-ARCHIVAL_SCIENCE-C` | `EU-ARCHIVAL_SCIENCE-C` | `SRC-ARCHIVAL_SCIENCE` |
| asset-management-basics | `CLM-ASSET_MANAGEMENT_BASICS-A` | `EU-ASSET_MANAGEMENT_BASICS-A` | `SRC-ASSET_MANAGEMENT_BASICS` |
| asset-management-basics | `CLM-ASSET_MANAGEMENT_BASICS-B` | `EU-ASSET_MANAGEMENT_BASICS-B` | `SRC-ASSET_MANAGEMENT_BASICS` |
| asset-management-basics | `CLM-ASSET_MANAGEMENT_BASICS-C` | `EU-ASSET_MANAGEMENT_BASICS-C` | `SRC-ASSET_MANAGEMENT_BASICS` |
| behavioral-biology-basics | `CLM-BEHAVIORAL_BIOLOGY_BASICS-A` | `EU-BEHAVIORAL_BIOLOGY_BASICS-A` | `SRC-BEHAVIORAL_BIOLOGY_BASICS` |
| behavioral-biology-basics | `CLM-BEHAVIORAL_BIOLOGY_BASICS-B` | `EU-BEHAVIORAL_BIOLOGY_BASICS-B` | `SRC-BEHAVIORAL_BIOLOGY_BASICS` |
| behavioral-biology-basics | `CLM-BEHAVIORAL_BIOLOGY_BASICS-C` | `EU-BEHAVIORAL_BIOLOGY_BASICS-C` | `SRC-BEHAVIORAL_BIOLOGY_BASICS` |
| behavioral-economics-basics | `CLM-BEHAVIORAL_ECONOMICS_BASICS-B` | `EU-BEHAVIORAL_ECONOMICS_BASICS-B` | `SRC-BEHAVIORAL_ECONOMICS_BASICS` |
| behavioral-economics-basics | `CLM-BEHAVIORAL_ECONOMICS_BASICS-C` | `EU-BEHAVIORAL_ECONOMICS_BASICS-C` | `SRC-BEHAVIORAL_ECONOMICS_BASICS` |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-A` | `EU-BIODIVERSITY_BASICS-A` | `SRC-BIODIVERSITY_BASICS` |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-B` | `EU-BIODIVERSITY_BASICS-B` | `SRC-BIODIVERSITY_BASICS` |
| calibration-basics | `CLM-CALIBRATION_BASICS-A` | `EU-CALIBRATION_BASICS-A` | `SRC-CALIBRATION_BASICS` |
| calibration-basics | `CLM-CALIBRATION_BASICS-B` | `EU-CALIBRATION_BASICS-B` | `SRC-CALIBRATION_BASICS` |
| calibration-basics | `CLM-CALIBRATION_BASICS-C` | `EU-CALIBRATION_BASICS-C` | `SRC-CALIBRATION_BASICS` |
| cell-basics | `CLM-CELL_BASICS-A` | `EU-CELL_BASICS-A` | `SRC-CELL_BASICS` |
| cell-basics | `CLM-CELL_BASICS-B` | `EU-CELL_BASICS-B` | `SRC-CELL_BASICS` |
| cell-basics | `CLM-CELL_BASICS-C` | `EU-CELL_BASICS-C` | `SRC-CELL_BASICS` |
| civil-society-basics | `CLM-CIVIL_SOCIETY_BASICS-A` | `EU-CIVIL_SOCIETY_BASICS-A` | `SRC-CIVIL_SOCIETY_BASICS` |
| digital-communications-basics | `CLM-DIGITAL_COMMUNICATIONS_BASICS-A` | `EU-DIGITAL_COMMUNICATIONS_BASICS-A` | `SRC-DIGITAL_COMMUNICATIONS_BASICS` |
| digital-communications-basics | `CLM-DIGITAL_COMMUNICATIONS_BASICS-B` | `EU-DIGITAL_COMMUNICATIONS_BASICS-B` | `SRC-DIGITAL_COMMUNICATIONS_BASICS` |
| digital-communications-basics | `CLM-DIGITAL_COMMUNICATIONS_BASICS-C` | `EU-DIGITAL_COMMUNICATIONS_BASICS-C` | `SRC-DIGITAL_COMMUNICATIONS_BASICS` |
| electronics-basics | `CLM-ELECTRONICS_BASICS-B` | `EU-ELECTRONICS_BASICS-B` | `SRC-ELECTRONICS_BASICS` |
| electronics-basics | `CLM-ELECTRONICS_BASICS-C` | `EU-ELECTRONICS_BASICS-C` | `SRC-ELECTRONICS_BASICS` |
| emergency-management-basics | `CLM-EMERGENCY_MANAGEMENT_BASICS-B` | `EU-EMERGENCY_MANAGEMENT_BASICS-B` | `SRC-EMERGENCY_MANAGEMENT_BASICS` |
| emergency-management-basics | `CLM-EMERGENCY_MANAGEMENT_BASICS-C` | `EU-EMERGENCY_MANAGEMENT_BASICS-C` | `SRC-EMERGENCY_MANAGEMENT_BASICS` |
| history-of-medicine-basics | `CLM-HISTORY_OF_MEDICINE-A` | `EU-HISTORY_OF_MEDICINE-A` | `SRC-HISTORY_OF_MEDICINE` |
| history-of-medicine-basics | `CLM-HISTORY_OF_MEDICINE-B` | `EU-HISTORY_OF_MEDICINE-B` | `SRC-HISTORY_OF_MEDICINE` |
| history-of-medicine-basics | `CLM-HISTORY_OF_MEDICINE-C` | `EU-HISTORY_OF_MEDICINE-C` | `SRC-HISTORY_OF_MEDICINE` |
| humanitarian-logistics-basics | `CLM-HUMANITARIAN_LOGISTICS_BASICS-C` | `EU-HUMANITARIAN_LOGISTICS_BASICS-C` | `SRC-HUMANITARIAN_LOGISTICS_BASICS` |
| hydropower-basics | `CLM-HYDROPOWER_BASICS-A` | `EU-HYDROPOWER_BASICS-A` | `SRC-HYDROPOWER_BASICS` |
| migration-and-mobility-basics | `CLM-MIGRATION_AND_MOBILITY_BASICS-A` | `EU-MIGRATION_AND_MOBILITY_BASICS-A` | `SRC-MIGRATION_AND_MOBILITY_BASICS` |
| scientific-publishing-basics | `CLM-SCIENTIFIC_PUBLISHING_BASICS-A` | `EU-SCIENTIFIC_PUBLISHING_BASICS-A` | `SRC-SCIENTIFIC_PUBLISHING_BASICS` |
| scientific-publishing-basics | `CLM-SCIENTIFIC_PUBLISHING_BASICS-B` | `EU-SCIENTIFIC_PUBLISHING_BASICS-B` | `SRC-SCIENTIFIC_PUBLISHING_BASICS` |
| scientific-publishing-basics | `CLM-SCIENTIFIC_PUBLISHING_BASICS-C` | `EU-SCIENTIFIC_PUBLISHING_BASICS-C` | `SRC-SCIENTIFIC_PUBLISHING_BASICS` |
| shelter-basics | `CLM-SHELTER_BASICS-A` | `EU-SHELTER_BASICS-A` | `SRC-SHELTER_BASICS` |
| shelter-basics | `CLM-SHELTER_BASICS-B` | `EU-SHELTER_BASICS-B` | `SRC-SHELTER_BASICS` |
| shelter-basics | `CLM-SHELTER_BASICS-C` | `EU-SHELTER_BASICS-C` | `SRC-SHELTER_BASICS` |
| urban-planning-basics | `CLM-URBAN_PLANNING_BASICS-A` | `EU-URBAN_PLANNING_BASICS-A` | `SRC-URBAN_PLANNING_BASICS` |
| water-security-basics | `CLM-WATER_SECURITY-B` | `EU-WATER_SECURITY-B` | `SRC-WATER_SECURITY` |

## 4. Review order

1. Reconcile safety/high-consequence candidates first: emergency management, shelter, water security, hydropower, calibration and electronics. Electrical safety A/B/C have now received v2 Evidence Use pinpoints; Claim C remains partially supported/HOLD.
2. Reconcile algebra, asset management, cell biology and civil society; verify exact Claim/EU/Source versions, source rights and the source passage.
3. For every candidate, record the exact report section that reviewed it, source edition and passage, support/partial/unsupported disposition, and whether a canonical locator exists.
4. Keep Source identity correction, passage support, rights clearance, independent adjudication and Human View as separate states.
5. Only then create bounded correction packages with exact paths, record versions, regression tests and authorization.

## 5. Limitations and integrity

- The 516 candidates are structural generic-description flags, not 516 false Claims.
- The 469 filename signals do not establish direct support.
- The 47 listed candidates are a manual-review routing queue, not 47 confirmed failures.
- The scan does not fetch source pages, verify rights, assign D/E/B, modify canonical records or authorize publication.
- The 47-item count is tied to the successful full-corpus artifact on source revision `04ef30d5cb8a48654d03607a6ba5b01eb01bc87c`; rerun after further classifier or report-corpus changes.

This is a corrected current routing baseline, not M13 completion.
