# M13 — current E-score recalibration review for 38 high-consequence Claims

Date: 2026-11-12
Basis: full-inventory evidence-linkage audit and exact-head scored-report ledger artifact generated during the 2026-11-12 Reference implementation workflow.
Scope: 140 Claims carrying the machine high-consequence routing flag and one generic Evidence Use record each. All 140 now have source-passage review report coverage.

## 1. Result

The 140-Claim high-consequence set has:
- Source-passage review reports: 140/140.
- Generic Evidence Use records: 140/140.
- Canonical pinpoint locators added in the source-passage desk reports: 0.
- Latest historical E=1: 102 Claims.
- Latest historical E=2: 33 Claims.
- Latest historical E=3: 5 Claims.
- Historical E=2/3 requiring current-rubric recalibration: 38 Claims.

The current M13 evidence-fit rule used in Batches 52–54 requires a reproducible Claim-specific locator in the canonical Evidence Use chain. A source may be reputable and directly relevant, and a desk report may quote or identify the right passage, but if the canonical EU still has only generic material text and no section/page/table/figure locator, E cannot be treated as current E=2 or E=3.

This is a rubric-version reconciliation, not a claim that earlier reviewers acted improperly. Preserve historical rows and scores as historical assessments. Do not overwrite them or silently promote a later report. Record a new current-rubric adjudication only after the canonical Evidence Use has a verified locator or the source chain has been corrected.

## 2. Required disposition

For the 38 rows below:
1. Retain the historical D/E/B row and original report unchanged.
2. Mark the current evidence-fit state as REASSESS / HOLD.
3. Current-rule E is provisionally 1 while the canonical EU lacks a reproducible locator.
4. If the source passage does not support the entire Claim, keep HOLD and propose a distinct Source/EU or a bounded Claim wording correction; do not force E upward by adding a locator to an irrelevant passage.
5. Only after authorized, versioned canonical EU correction and independent passage verification may a new current-rubric score be recorded.

The other 102 high-consequence Claims already have latest historical E=1. They still remain HOLD until the exact locator/source remediation and other release gates are complete.

## 3. The 38 historical E=2/3 rows

| Claim ID | Last scored batch | Historical E | Evidence Use ID | Latest historical report |
|---|---:|---:|---|---|
| `CLM-ACOUSTICS_BASICS-A` | 41 | 2 | `EU-ACOUSTICS_BASICS-A` | `RELEASE/M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-01-ACID-BASE-ACOUSTICS-2026-10-11.md` |
| `CLM-ACOUSTICS_BASICS-C` | 41 | 2 | `EU-ACOUSTICS_BASICS-C` | `RELEASE/M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-01-ACID-BASE-ACOUSTICS-2026-10-11.md` |
| `CLM-ADMINISTRATIVE_LAW_BASICS-A` | 41 | 2 | `EU-ADMINISTRATIVE_LAW_BASICS-A` | `RELEASE/M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-02-ADMIN-AGRI-AGRIFOOD-AI-ALGEBRA-2026-10-11.md` |
| `CLM-ANATOMY_BASICS-A` | 41 | 2 | `EU-ANATOMY_BASICS-A` | `RELEASE/M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-03-ALGEBRA-ANALYTICAL-ANATOMY-ANCIENT-ANTHRO-AMR-ARCHAEOLOGY-2026-10-11.md` |
| `CLM-BEHAVIORAL_ECONOMICS_BASICS-A` | 41 | 2 | `EU-BEHAVIORAL_ECONOMICS_BASICS-A` | `RELEASE/M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-05-ASTRONOMY-ATMOSPHERE-BEHAVIOR-BIOCHEMISTRY-2026-10-11.md` |
| `CLM-CELL_BASICS-A` | 40 | 2 | `EU-CELL_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-40-CAUSAL-BIOLOGY-CHEMISTRY-AND-CHRONOLOGY-2026-10-10.md` |
| `CLM-CELL_BASICS-B` | 40 | 3 | `EU-CELL_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-40-CAUSAL-BIOLOGY-CHEMISTRY-AND-CHRONOLOGY-2026-10-10.md` |
| `CLM-CELL_BASICS-C` | 40 | 2 | `EU-CELL_BASICS-C` | `RELEASE/M13-CLAIM-REVIEW-BATCH-40-CAUSAL-BIOLOGY-CHEMISTRY-AND-CHRONOLOGY-2026-10-10.md` |
| `CLM-CIVIL_SOCIETY_BASICS-A` | 41 | 2 | `EU-CIVIL_SOCIETY_BASICS-A` | `RELEASE/M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-06-BIOCHEMISTRY-BIODIVERSITY-BIOINFO-BIOMED-CALCULUS-CARTOGRAPHY-CIVIL-SOCIETY-2026-10-11.md` |
| `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-A` | 43 | 2 | `EU-DEVELOPMENTAL_BIOLOGY_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-088-DEVELOPMENT-AS-A-SEQUENCE-OF-BIOLOGICAL-CHANGES-2026-10-31.md` |
| `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-B` | 43 | 2 | `EU-DEVELOPMENTAL_BIOLOGY_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-089-CELL-DIFFERENTIATION-AND-SPECIALIZED-FUNCTIONS-2026-10-31.md` |
| `CLM-DIGITAL_COMMUNICATIONS_BASICS-B` | 31 | 2 | `EU-DIGITAL_COMMUNICATIONS_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-31-DIGITAL-COMMUNICATIONS-2026-10-10.md` |
| `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-B` | 43 | 2 | `EU-DISASTER_BEHAVIORAL_HEALTH_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-014-DISASTER-BEHAVIORAL-HEALTH-ALL-PHASES-2026-10-20.md` |
| `CLM-ELECTRICAL_SAFETY_BASICS-A` | 21 | 2 | `EU-ELECTRICAL_SAFETY_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md` |
| `CLM-ELECTRICAL_SAFETY_BASICS-B` | 21 | 2 | `EU-ELECTRICAL_SAFETY_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md` |
| `CLM-ELECTRICAL_SAFETY_BASICS-C` | 21 | 2 | `EU-ELECTRICAL_SAFETY_BASICS-C` | `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md` |
| `CLM-EMERGENCY_MANAGEMENT_BASICS-B` | 43 | 2 | `EU-EMERGENCY_MANAGEMENT_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-004-EMERGENCY-MANAGEMENT-PARTNERS-2026-10-20.md` |
| `CLM-ENVIRONMENTAL_HEALTH_BASICS-A` | 42 | 2 | `EU-ENVIRONMENTAL_HEALTH_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-42-SCORED-ROW-008-ENVIRONMENTAL-HEALTH-2026-10-16.md` |
| `CLM-FOOD_PRESERVATION_BASICS-A` | 20 | 2 | `EU-FOOD_PRESERVATION_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-20-FOOD-GRID-CO-2026-10-10.md` |
| `CLM-FOOD_PRESERVATION_BASICS-B` | 20 | 3 | `EU-FOOD_PRESERVATION_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-20-FOOD-GRID-CO-2026-10-10.md` |
| `CLM-FOOD_PRESERVATION_BASICS-C` | 20 | 2 | `EU-FOOD_PRESERVATION_BASICS-C` | `RELEASE/M13-CLAIM-REVIEW-BATCH-20-FOOD-GRID-CO-2026-10-10.md` |
| `CLM-FOOD_SAFETY_BASICS-C` | 20 | 2 | `EU-FOOD_SAFETY_BASICS-C` | `RELEASE/M13-CLAIM-REVIEW-BATCH-20-FOOD-GRID-CO-2026-10-10.md` |
| `CLM-HISTORY_OF_MEDICINE-A` | 43 | 2 | `EU-HISTORY_OF_MEDICINE-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-027-HISTORY-OF-MEDICINE-DEFINITION-2026-10-20.md` |
| `CLM-HYDROPOWER_BASICS-A` | 43 | 3 | `EU-HYDROPOWER_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-099-HYDROPOWER-FROM-MOVING-WATER-2026-10-31.md` |
| `CLM-INSPECTION_BASICS-C` | 43 | 2 | `EU-INSPECTION_BASICS-C` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-031-INSPECTION-TECHNICAL-OPINION-BOUNDARY-2026-10-20.md` |
| `CLM-MIGRATION_AND_MOBILITY_BASICS-A` | 42 | 2 | `EU-MIGRATION_AND_MOBILITY_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-42-SCORED-ROW-039-MIGRATION-DEFINITION-2026-10-18.md` |
| `CLM-OCCUPATIONAL_SAFETY_BASICS-A` | 43 | 2 | `EU-OCCUPATIONAL_SAFETY_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-045-OCCUPATIONAL-SAFETY-A-2026-10-27.md` |
| `CLM-OCCUPATIONAL_SAFETY_BASICS-B` | 43 | 2 | `EU-OCCUPATIONAL_SAFETY_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-046-OCCUPATIONAL-SAFETY-B-2026-10-27.md` |
| `CLM-OCCUPATIONAL_SAFETY_BASICS-C` | 43 | 2 | `EU-OCCUPATIONAL_SAFETY_BASICS-C` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-047-OCCUPATIONAL-SAFETY-C-2026-10-27.md` |
| `CLM-SCIENTIFIC_PUBLISHING_BASICS-B` | 43 | 3 | `EU-SCIENTIFIC_PUBLISHING_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-058-AUTHORSHIP-AND-ACCOUNTABILITY-2026-10-27.md` |
| `CLM-SCIENTIFIC_PUBLISHING_BASICS-C` | 43 | 2 | `EU-SCIENTIFIC_PUBLISHING_BASICS-C` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-059-DISTINGUISHING-AUTHOR-AND-CONTRIBUTOR-ROLES-2026-10-27.md` |
| `CLM-SHELTER_BASICS-A` | 22 | 2 | `EU-SHELTER_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-22-PUBLIC-HEALTH-SHELTER-2026-10-10.md` |
| `CLM-SOCIAL_POLICY_BASICS-A` | 43 | 2 | `EU-SOCIAL_POLICY_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-060-SCOPE-OF-SOCIAL-POLICY-2026-10-27.md` |
| `CLM-WASTEWATER_BASICS-A` | 43 | 2 | `EU-WASTEWATER_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-068-WASTEWATER-COLLECTION-TREATMENT-AND-THE-WATER-CYCLE-2026-10-27.md` |
| `CLM-WATER_INFRASTRUCTURE_BASICS-A` | 43 | 2 | `EU-WATER_INFRASTRUCTURE_BASICS-A` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-084-COMPONENTS-OF-DRINKING-WATER-DISTRIBUTION-SYSTEMS-2026-10-31.md` |
| `CLM-WATER_INFRASTRUCTURE_BASICS-B` | 43 | 2 | `EU-WATER_INFRASTRUCTURE_BASICS-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-085-DISTRIBUTION-SYSTEMS-AS-A-BARRIER-AGAINST-CONTAMINATION-2026-10-31.md` |
| `CLM-WATER_INFRASTRUCTURE_BASICS-C` | 43 | 2 | `EU-WATER_INFRASTRUCTURE_BASICS-C` | `RELEASE/M13-CLAIM-REVIEW-BATCH-43-SCORED-ROW-086-CONDITIONS-AFFECTING-DISTRIBUTION-SYSTEM-WATER-QUALITY-2026-10-31.md` |
| `CLM-WATER_SECURITY-B` | 21 | 3 | `EU-WATER_SECURITY-B` | `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md` |

## 4. Important interpretation

- 38 is the number of unique Claims whose latest historical E score is 2 or 3 while the current canonical EU remains structurally generic.
- The 33 E=2 and 5 E=3 values are historical. They are not erased, and the original reports remain part of the audit trail.
- The 102 E=1 rows are already aligned with the current locator rule, but remain HOLD because the locator is still absent.
- A source-passage report that names a section or passage does not by itself fix the canonical Evidence Use record. The locator must be stored in the linked EU record and validated against the exact source version.
- Source fit, independence, jurisdiction, rights/attribution, specialist review and Human View remain separate gates.

## 5. Specific wording issue — motion Claim B

The canonical Russian statement for CLM-MOTION_BASICS-B is: “Средняя скорость определяется отношением изменения положения к соответствующему интервалу времени.”

The OpenStax source distinguishes:
- average speed = total distance travelled / elapsed time (scalar);
- average velocity = displacement / elapsed time (vector).

The Claim's numerator, “изменение положения” (displacement), corresponds to average velocity. Russian “средняя скорость” is commonly used for velocity in physics, but the statement should explicitly preserve the vector meaning to prevent confusion with “средняя путевая скорость”. Proposed bounded wording:
- “Средняя векторная скорость определяется отношением перемещения к соответствующему интервалу времени.”

Alternative if scalar path speed is intended:
- “Средняя путевая скорость определяется отношением длины пройденного пути к соответствующему интервалу времени.”

No canonical Claim text was changed.

## 6. Next controlled actions

1. Prepare a per-record locator correction proposal for the 140 high-consequence EU records, starting with water/food/sanitation, electrical safety, shelter and occupational safety.
2. Separate pure locator additions from source replacement/addition and Claim wording corrections.
3. Preserve version 1 records; any correction must create a versioned successor and include regression tests for Claim→EU→Source resolution, relations, offline export and release conformance.
4. Do not edit canonical EU records until the bounded authorization scope is explicit.
5. After high-consequence remediation, continue the remaining 379 generic-EU candidates in thematic batches.

## 7. Acceptance boundary

This report identifies the exact 38-row historical score recalibration set. It does not change any score, canonical record, risk metadata or release status. All 140 Claims remain HOLD. M13 remains open.
