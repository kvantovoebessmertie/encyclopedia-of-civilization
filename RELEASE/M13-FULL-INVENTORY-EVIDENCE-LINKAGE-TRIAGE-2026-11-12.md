# M13 full-inventory evidence-linkage triage and high-consequence remediation worklist

Date: 2026-11-12
Source revision for the machine audit: 2db3995b50c3b26179a341612c3aa1f3438551d1
Source revision for the reconciled score ledger: 0e52a03349a911df3fc12054559fe097e120bf2d
Scope: all 4,834 canonical record files, including 1,494 Claims, 1,670 Evidence Use records and 619 Source records. This report records structural triage only. It does not reject evidence automatically, change canonical records, assign scores, or clear Claims for release.

## 1. Full scored-report coverage

The M13 scored-report reconciliation artifact reports:
- 1,494 canonical Claim records.
- 1,501 scored-report rows.
- 1,494 unique normalized Claim IDs.
- 1,494/1,494 inventory Claims with at least one scored-report match.
- 0 unmatched scored-report rows and 0 inventory Claims without a scored row.
- 7 duplicate report groups (14 rows), all preserved for human adjudication.
- 1 separator-normalized Batch 44 alias requiring manual confirmation.
- 160 separator-only filename/internal-ID variations and 3 genuine filename/internal-ID mismatches.

The three genuine path/ID mismatches are all in `web-systems-basics`:
- `CLM-A.json` → internal ID `CLM-WEB_SYSTEMS_BASICS-A`
- `CLM-B.json` → internal ID `CLM-WEB_SYSTEMS_BASICS-B`
- `CLM-C.json` → internal ID `CLM-WEB_SYSTEMS_BASICS-C`
The associated three Evidence Use files have the same generic filename pattern (`EU-A/B/C.json`) with full internal IDs. These six path/ID issues are high-severity structural mismatches. Do not rename files or rewrite references without bounded authorization, reference/Relation checks and regression tests.

Full coverage means every Claim has at least one historical score row. It does not mean every score is valid, every source is independent, or every Claim is accepted.

## 2. Evidence-linkage audit results

The exact-head evidence-linkage audit examined all 4,834 files:
- Valid JSON files: 4,834/4,834.
- Claims: 1,494.
- Evidence Use records: 1,670.
- Sources: 619.
- Structural finding rows: 1,143.

| Finding | Rows | Interpretation |
|---|---:|---|
| Generic material descriptions | 519 | Evidence Use text is generic/template-like and does not preserve a claim-specific locator. Human source-passage review required; not automatic proof that the cited source is invalid. |
| Separator-only filename/ID aliases | 493 | Hyphen/underscore variation across record types. Comparison-only normalization can match these; stored IDs remain unchanged. |
| Duplicate Source URI candidates | 77 | 33 URI groups. Shared URL does not prove identical source identity or independent evidence. |
| Source identity sentence candidates | 48 | Source identity ends in sentence punctuation; editorial metadata review, not an evidence-validity finding. |
| Genuine filename/internal-ID mismatches | 6 | Three Claims and three Evidence Use records in web-systems-basics. Structural correction requires authorization and regression tests. |

The 493 separator aliases break down as 160 Claims, 164 Evidence Use, 61 Source, 51 Context, 51 Scope and 6 Relation records. They are naming-format variation, not 493 semantic ID failures.

The 77 duplicate Source URI rows form 33 groups. The largest candidate groups include:
- `https://www.nist.gov/itl` — 6 Source records.
- `https://www.nasa.gov/reference/systems-engineering-handbook/` — 4 Source records.
- `https://apps.usgs.gov/thesaurus/thesaurus-full.php` — 3 Source records.
- `https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water` — 3 Source records.
- `https://www.itl.nist.gov/div898/handbook/` — 3 Source records.
- `https://www.nist.gov/building-science` — 3 Source records.
- `https://www.noaa.gov/education/resource-collections/weather-atmosphere` — 3 Source records.

These are candidates for source identity reconciliation. Some may legitimately be the same broad landing page used for distinct subtopics; do not merge or delete them based on URI equality alone.

## 3. High-consequence generic-Evidence-Use worklist

Of the 519 Claims with generic Evidence Use descriptions, 140 carry the machine `high_consequence_screen` routing flag. They span 72 thematic slices. The risk-domain counts below overlap because a Claim may have multiple domains.

| Risk domain | Claims with generic EU and domain flag |
|---|---:|
| Legal/financial | 56 |
| Health/medical | 25 |
| Construction/tools/materials | 18 |
| Communications/information continuity | 15 |
| Water/food/sanitation | 12 |
| Electricity/energy | 11 |
| Transport/access | 9 |
| Emergency/fire/CO | 8 |
| Chemicals/hazards | 5 |
| Shelter/evacuation/access | 4 |

### Priority 1 — water, food, sanitation (12)

`CLM-ENVIRONMENTAL_HEALTH_BASICS-A`; `CLM-FOOD_PRESERVATION_BASICS-A`; `CLM-FOOD_PRESERVATION_BASICS-B`; `CLM-FOOD_PRESERVATION_BASICS-C`; `CLM-FOOD_SAFETY_BASICS-A`; `CLM-FOOD_SAFETY_BASICS-B`; `CLM-FOOD_SAFETY_BASICS-C`; `CLM-WASTEWATER_BASICS-B`; `CLM-WASTEWATER_BASICS-C`; `CLM-WATER_INFRASTRUCTURE_BASICS-A`; `CLM-WATER_INFRASTRUCTURE_BASICS-B`; `CLM-WATER_INFRASTRUCTURE_BASICS-C`.

### Priority 2 — health and occupational safety (25)

`CLM-ACOUSTICS_BASICS-A`; `CLM-ACOUSTICS_BASICS-B`; `CLM-ACOUSTICS_BASICS-C`; `CLM-ANATOMY_BASICS-A`; `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-A`; `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-B`; `CLM-DISASTER_BEHAVIORAL_HEALTH_BASICS-C`; `CLM-ENVIRONMENTAL_HEALTH_BASICS-A`; `CLM-ENVIRONMENTAL_HEALTH_BASICS-B`; `CLM-ENVIRONMENTAL_HEALTH_BASICS-C`; `CLM-HISTORY_OF_MEDICINE-A`; `CLM-HISTORY_OF_MEDICINE-B`; `CLM-HISTORY_OF_MEDICINE-C`; `CLM-INSPECTION_BASICS-A`; `CLM-INSPECTION_BASICS-B`; `CLM-INSPECTION_BASICS-C`; `CLM-OCCUPATIONAL_SAFETY_BASICS-A`; `CLM-OCCUPATIONAL_SAFETY_BASICS-B`; `CLM-OCCUPATIONAL_SAFETY_BASICS-C`; `CLM-SCIENTIFIC_PUBLISHING_BASICS-A`; `CLM-SCIENTIFIC_PUBLISHING_BASICS-B`; `CLM-SCIENTIFIC_PUBLISHING_BASICS-C`; `CLM-SOCIAL_POLICY_BASICS-A`; `CLM-WASTEWATER_BASICS-A`; `CLM-WASTEWATER_BASICS-B`.

### Priority 3 — emergency, electrical, shelter (23 domain memberships; overlapping)

Emergency/fire/CO:
`CLM-ELECTRICAL_SAFETY_BASICS-A`; `CLM-EMERGENCY_MANAGEMENT_BASICS-A`; `CLM-EMERGENCY_MANAGEMENT_BASICS-B`; `CLM-EMERGENCY_MANAGEMENT_BASICS-C`; `CLM-HUMANITARIAN_LOGISTICS_BASICS-C`; `CLM-SHELTER_BASICS-A`; `CLM-SHELTER_BASICS-B`; `CLM-SHELTER_BASICS-C`.

Electricity/energy:
`CLM-ANATOMY_BASICS-A`; `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-A`; `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-B`; `CLM-ELECTRICAL_SAFETY_BASICS-A`; `CLM-ELECTRICAL_SAFETY_BASICS-B`; `CLM-ELECTRICAL_SAFETY_BASICS-C`; `CLM-ELECTRONICS_BASICS-A`; `CLM-ELECTRONICS_BASICS-B`; `CLM-ELECTRONICS_BASICS-C`; `CLM-HYDROPOWER_BASICS-A`; `CLM-VIROLOGY_BASICS-A`.

Shelter/evacuation/access:
`CLM-MIGRATION_AND_MOBILITY_BASICS-A`; `CLM-SHELTER_BASICS-A`; `CLM-SHELTER_BASICS-B`; `CLM-SHELTER_BASICS-C`.

### Priority 4 — construction, materials, transport, chemicals (32)

Construction/tools/materials:
`CLM-CONSERVATION_BIOLOGY_BASICS-C`; `CLM-CONSTRUCTION_BASICS-A`; `CLM-CONSTRUCTION_BASICS-C`; `CLM-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-A`; `CLM-CRYPTOGRAPHY_BASICS-C`; `CLM-ELECTRONICS_BASICS-C`; `CLM-FINANCE_BASICS-C`; `CLM-HISTORY_METHODS_BASICS-A`; `CLM-HISTORY_OF_MEDICINE-C`; `CLM-HOUSING_SYSTEMS_BASICS-C`; `CLM-HUMAN_RIGHTS_BASICS-B`; `CLM-INTERNATIONAL_LAW_BASICS-A`; `CLM-TIMBER_ENGINEERING_BASICS-A`; `CLM-TIMBER_ENGINEERING_BASICS-B`; `CLM-TIMBER_ENGINEERING_BASICS-C`; `CLM-URBAN_PLANNING_BASICS-A`; `CLM-URBAN_PLANNING_BASICS-B`; `CLM-URBAN_PLANNING_BASICS-C`.

Transport/access:
`CLM-ENVIRONMENTAL_HEALTH_BASICS-C`; `CLM-LAND_USE_PLANNING_BASICS-B`; `CLM-MIGRATION_AND_MOBILITY_BASICS-A`; `CLM-PLANT_PHYSIOLOGY_BASICS-B`; `CLM-TRANSPORTATION_INFRASTRUCTURE_BASICS-A`; `CLM-TRANSPORTATION_INFRASTRUCTURE_BASICS-B`; `CLM-TRANSPORTATION_INFRASTRUCTURE_BASICS-C`; `CLM-URBAN_PLANNING_BASICS-A`; `CLM-WASTE_INFRASTRUCTURE_BASICS-A`.

Chemicals/hazards:
`CLM-ENVIRONMENTAL_HEALTH_BASICS-A`; `CLM-MATTER_BASICS-B`; `CLM-MATTER_BASICS-C`; `CLM-VOLCANOLOGY_BASICS-C`; `CLM_WATER_RESOURCES_BASICS_B`.

### Priority 5 — communications and continuity (15)

`CLM-CALIBRATION_BASICS-A`; `CLM-DIGITAL_COMMUNICATIONS_BASICS-A`; `CLM-DIGITAL_COMMUNICATIONS_BASICS-B`; `CLM-DIGITAL_COMMUNICATIONS_BASICS-C`; `CLM-DISASTER_RISK_REDUCTION_BASICS-A`; `CLM-ECOPHYSIOLOGY_BASICS-A`; `CLM-ECOPHYSIOLOGY_BASICS-B`; `CLM-ECOPHYSIOLOGY_BASICS-C`; `CLM-EMERGENCY_MANAGEMENT_BASICS-A`; `CLM-FOOD_SECURITY_BASICS-A`; `CLM-FOOD_SECURITY_BASICS-B`; `CLM-FOOD_SECURITY_BASICS-C`; `CLM-HISTORY_METHODS_BASICS-C`; `CLM-MICROECONOMICS_BASICS-A`; `CLM-WATER_SECURITY-B`.

### Priority 6 — legal and financial (56)

`CLM-ACCOUNTING_BASICS-A`; `CLM-ACCOUNTING_BASICS-B`; `CLM-ACCOUNTING_BASICS-C`; `CLM-ADMINISTRATIVE_LAW_BASICS-A`; `CLM-ANATOMY_BASICS-A`; `CLM-BEHAVIORAL_ECONOMICS_BASICS-A`; `CLM-CELL_BASICS-A`; `CLM-CELL_BASICS-B`; `CLM-CELL_BASICS-C`; `CLM-CIVIL_SOCIETY_BASICS-A`; `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-A`; `CLM-COMPARATIVE_LAW_BASICS-A`; `CLM-COMPUTING_BASICS-A`; `CLM-COMPUTING_BASICS-B`; `CLM-COMPUTING_BASICS-C`; `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-A`; `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-B`; `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-C`; `CLM-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-C`; `CLM-DEVELOPMENT_ECONOMICS_BASICS-A`; `CLM-DIPLOMACY_BASICS-A`; `CLM-DIPLOMACY_BASICS-B`; `CLM-EMERGENCY_MANAGEMENT_BASICS-C`; `CLM-ENERGY_BASICS-A`; `CLM-ENERGY_BASICS-B`; `CLM-ENERGY_BASICS-C`; `CLM-ENVIRONMENTAL_POLICY_BASICS-C`; `CLM-FINANCE_BASICS-A`; `CLM-FINANCE_BASICS-C`; `CLM-FOOD_SYSTEMS-A`; `CLM-FOOD_SYSTEMS-B`; `CLM-FORESTRY_BASICS-C`; `CLM-HOUSING_SYSTEMS_BASICS-A`; `CLM-HUMAN_RIGHTS_BASICS-A`; `CLM-INDUSTRIAL_SAFETY_BASICS-C`; `CLM-INTERNATIONAL_LAW_BASICS-A`; `CLM-INTERNATIONAL_RELATIONS_BASICS-A`; `CLM-LABOR_ECONOMICS_BASICS-A`; `CLM-LABOR_RELATIONS_BASICS-A`; `CLM-MATTER_BASICS-A`; `CLM-MATTER_BASICS-B`; `CLM-MATTER_BASICS-C`; `CLM-MIGRATION_AND_MOBILITY_BASICS-A`; `CLM-MOTION_BASICS-A`; `CLM-MOTION_BASICS-B`; `CLM-MOTION_BASICS-C`; `CLM-POLITICAL_SCIENCE_BASICS-A`; `CLM-POLITICAL_SCIENCE_BASICS-B`; `CLM-POLITICAL_SCIENCE_BASICS-C`; `CLM-PUBLIC_ADMINISTRATION_BASICS-C`; `CLM-PUBLIC_FINANCE_BASICS-A`; `CLM-PUBLIC_FINANCE_BASICS-C`; `CLM-PUBLIC_POLICY_BASICS-A`; `CLM-SCIENTIFIC_PUBLISHING_BASICS-B`; `CLM-TAXATION_BASICS-A`; `CLM-WATER_INFRASTRUCTURE_BASICS-C`.

## 4. Interpretation and safeguards

- The machine high-consequence flag is a routing signal, not a completed human risk assessment. Several risk domains are broad and may be overinclusive; specialist reviewers must confirm the correct route.
- Generic Evidence Use text is a structural warning. It does not establish that the Source itself is irrelevant, false or unreliable. It establishes that the stored evidence description does not make the support reproducible at Claim level.
- E scores in recent desk-review batches remained at 1 where exact locators were absent. The 519 flagged Evidence Use records are a corpus-wide candidate remediation set, not 519 automatically invalid Claims.
- Shared Source URIs do not prove source identity, duplication or independence.
- Filename normalization is comparison-only. No stored IDs, paths or canonical records are rewritten by this report.
- No canonical Claim/Evidence Use/Source JSON was changed. No Claim was accepted or release-cleared.

## 5. Next controlled phase

1. Manually review the 140 high-consequence generic-EU Claims, starting with water/food/sanitation, health, electrical/fire/emergency, shelter and construction/transport.
2. For each selected Claim, inspect the exact Claim statement, Evidence Use record, Source record and exact passage/section/table/figure in the source. Record the precise locator and whether the passage supports the entire Claim.
3. Keep unsupported, partial, outdated, jurisdiction-mismatched or non-independent evidence on HOLD. Do not raise E solely because a source is reputable or topically relevant.
4. Prepare a bounded Evidence Use correction proposal with exact proposed locator text and source/version references. Do not write canonical records until the authorized scope is explicit and regression tests cover Claim/EU/Source linkage and offline export.
5. Separately adjudicate the 7 duplicate score-report groups, the one separator-normalized alias, the three genuine web-systems-basics path/ID mismatches, and the 33 duplicate-URI candidate groups.
6. Only after the high-consequence evidence chain is repaired should the remaining 379 generic-EU candidates be processed in thematic batches. Do not launch another nominal scoring batch: the full Claim inventory already has scored-report coverage.

## 6. Exact CI artifact provenance

The evidence-linkage findings and summary were generated by the Reference implementation tests workflow at commit 2db3995b50c3b26179a341612c3aa1f3438551d1. The scored-claim reconciliation ledger was generated at the same exact revision. The queue automation at that revision selected 0 Claims and left 100 nominal queue slots unfilled. The report files are retained as workflow artifacts; this repository note records the summarized findings and remediation routing.
