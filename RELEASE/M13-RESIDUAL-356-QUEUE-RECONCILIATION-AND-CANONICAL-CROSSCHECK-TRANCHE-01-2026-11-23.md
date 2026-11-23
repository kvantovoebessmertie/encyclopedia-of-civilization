# M13 — residual 356 generic Evidence Use queue reconciliation and canonical cross-check tranche 01

Date: 2026-11-23
Branch: m13-system-wide-depth-audit-2026-10-09
Comparison HEAD for fresh canonical reads: 4f92b64e30f91f000574193de13a6c7997cc721c

## 1. Exact reconstruction of the 356-row residual queue

The residual queue was reconstructed from two exact workflow artifacts and the source-passage priority review, rather than relying on arithmetic alone.

Inputs:
- Workflow run 43748097686, artifact 14174823129: m13-generic-eu-report-coverage.json (496 candidate Claim/EU mappings; source revision 8cf14e5045f).
- Workflow run 43748097686, artifact 14174388824: M13-CLAIM-AUDIT-WORKSHEET.csv (1,494 Claim rows; source revision 23e1b243...).
- M13-REMAINING-379-PRIORITY-20-CLAIM-SOURCE-PASSAGE-REVIEW-2026-11-12.md (20 exact priority Claims).

Independent reconciliation:

| Control | Result |
|---|---:|
| Generic-EU coverage candidates | 496 |
| Candidate Claim IDs matched to worksheet | 496/496 |
| Candidate EU IDs present in worksheet EU link list | 496/496 |
| Worksheet rows with multiple EU links | 25 (candidate EU is still present in each row) |
| High-consequence screen flags | 120 |
| Priority second-pass Claims | 20 |
| Overlap between high-consequence and priority sets | 0 |
| Residual generic-EU queue | **356** |
| Unique Claim IDs / EU IDs / canonical paths in residual | 356 / 356 / 356 |
| Slices represented | 135 |
| Unique Source IDs in residual | 135 |
| Missing key fields / duplicate rows / multi-Source rows | 0 / 0 / 0 |

The 120 high-consequence rows are derived from the worksheet's explicit high_consequence_screen machine-triage flag. The 20 priority Claims are the exact Claim IDs in the priority source-passage review. These sets are disjoint and both are members of the 496-candidate population. Therefore 496 − 120 − 20 = 356.

## 2. Residual queue controls

| Control | Result |
|---|---:|
| Rows with at least one source-review report filename mention | 356/356 |
| Rows with one / two / three report filename mentions | 260 / 75 / 21 |
| Source version snapshot @1 | 356/356 |
| Human confirmation required | 356/356 |
| D/E/B fields populated | 0/356 |
| Canonical write authorized | 0/356 |
| Rows with no machine triage flag | 330 |
| Very-short-Claim review flag | 15 |
| Actionable/prescriptive review flag | 11 |

Report filename mentions are routing hints, not proof of exact report-body coverage or passage support. Machine flags are routing signals, not expert decisions. No score, inclusion, or publication permission is implied.

## 3. Fresh canonical cross-check

The earlier strict-locator packages had already directly checked 14 rows. Those 14 canonical EU paths were not modified between their reviewed HEAD and the current comparison HEAD.

This tranche adds **100 fresh EU record fetches** and **85 distinct Source record fetches** from the current comparison HEAD.

Fresh EU validation for each of the 100 rows:
- canonical path equals the coverage artifact path;
- record_id equals the exact EU ID;
- record_version is 1;
- content.claim_ref record ID and version match the exact Claim@1;
- content.source_ref record ID and version match the exact Source@1.

Result: **100/100 exact structural matches; 0 mismatches**.

Fresh Source validation:
- 85 distinct Source JSON records were fetched at their exact canonical paths;
- record_id matched the expected Source ID;
- record_version was 1 in all 85 records.

Result: **85/85 exact structural matches; 0 mismatches**.

Combined EU canonical cross-check: **114/356** (14 previously checked + 100 fresh). Remaining EU files for this pass: **242/356**.
Source canonical cross-check: **85/135** distinct Source records. Remaining distinct Source files: **50/135**.

## 4. Fresh EU IDs checked in this tranche

The following 100 Evidence Use records were fetched and validated at the exact current comparison HEAD:

EU-DEMOGRAPHIC_METHODS_BASICS-A, EU-FOOD_SYSTEMS-C, EU-FORESTRY_BASICS-A, EU-GEOLOGIC_MAPPING_BASICS-A, EU-GEOMETRY_BASICS-A, EU-GEOMORPHOLOGY_BASICS-A, EU-GEOSPATIAL_ANALYSIS_BASICS-A, EU-HISTORICAL_GEOGRAPHY-A, EU-ANATOMY_BASICS-C, EU-ARCHIVAL_DESCRIPTION_BASICS-C, EU-CARTOGRAPHY-C, EU-CLIMATE_ADAPTATION-A, EU-CLIMATE_BASICS-A, EU-CLOUD_COMPUTING_BASICS-A, EU-COMBINATORICS_BASICS-A, EU-COMPARATIVE_CIVILIZATIONS_BASICS-B, EU-COMPUTER_ARCHITECTURE_BASICS-A, EU-COMPUTER_GRAPHICS_BASICS-A, EU-CONSERVATION_BIOLOGY_BASICS-A, EU-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS-B.

EU-DEMOGRAPHIC_METHODS_BASICS-B, EU-FORESTRY_BASICS-B, EU-GEOLOGIC_MAPPING_BASICS-B, EU-GEOMETRY_BASICS-B, EU-GEOMORPHOLOGY_BASICS-B, EU-GEOSPATIAL_ANALYSIS_BASICS-B, EU-HISTORICAL_GEOGRAPHY-B, EU-CLIMATE_ADAPTATION-B, EU-CLIMATE_BASICS-B, EU-CLOUD_COMPUTING_BASICS-B, EU-COMBINATORICS_BASICS-B, EU-COMPARATIVE_CIVILIZATIONS_BASICS-C, EU-COMPUTER_ARCHITECTURE_BASICS-B, EU-COMPUTER_GRAPHICS_BASICS-B, EU-CONSERVATION_BIOLOGY_BASICS-B, EU-CRYPTOGRAPHY_BASICS-A, EU-CULTURAL_ANTHROPOLOGY-A, EU-CULTURAL_HERITAGE-A, EU-CYBERSECURITY_BASICS-A, EU-DATABASES_BASICS-A.

EU-DEVELOPMENT_ECONOMICS_BASICS-B, EU-DEVELOPMENTAL_BIOLOGY_BASICS-C, EU-DIPLOMACY_BASICS-C, EU-DISTRIBUTED_SYSTEMS_BASICS-A, EU-EARTH_SYSTEM_BASICS-A, EU-ECONOMIC_HISTORY-A, EU-ECONOMICS_BASICS-A, EU-EDUCATION_SCIENCE_BASICS-A, EU-EMBEDDED_SYSTEMS_BASICS-A, EU-ENERGY_SECURITY_BASICS-A, EU-ENGINEERING_DESIGN_BASICS-A, EU-ENVIRONMENTAL_MONITORING_BASICS-A, EU-ENVIRONMENTAL_POLICY_BASICS-A, EU-FISHERIES_BASICS-A, EU-FOOD_FERMENTATION_BASICS-A, EU-HYDROPOWER_BASICS-B, EU-INFRASTRUCTURE_GOVERNANCE_BASICS-A, EU-MEASUREMENT_UNCERTAINTY_BASICS-A, EU-STATISTICS_INFERENCE_BASICS-A, EU-WASTE_INFRASTRUCTURE_BASICS-B.

EU-WATER_RESOURCES_BASICS-A, EU-WATER_RESOURCES_MANAGEMENT_BASICS-A, EU-AGRICULTURE_BASICS-A, EU-AI_ETHICS_BASICS-A, EU-ARTIFICIAL_INTELLIGENCE_BASICS-A, EU-ATMOSPHERIC_SCIENCE_BASICS-A, EU-BIODIVERSITY_BASICS-C, EU-BUILDING_ENVELOPE_BASICS-A, EU-CALCULUS_BASICS-A, EU-FINANCE_BASICS-B, EU-HISTORY_OF_ENGINEERING-A, EU-HISTORY_OF_MATHEMATICS-A, EU-HISTORY_OF_SCIENCE-A, EU-HISTORY_OF_TECHNOLOGY-A, EU-HOUSING_SYSTEMS_BASICS-B, EU-HUMAN_AI_INTERACTION_BASICS-A, EU-HUMAN_RIGHTS_BASICS-C, EU-HUMANITARIAN_LOGISTICS_BASICS-A, EU-INFORMATION_RETRIEVAL_BASICS-A, EU-INTERNATIONAL_RELATIONS_BASICS-B.

EU-LABOR_RELATIONS_BASICS-B, EU-LAND_USE_PLANNING_BASICS-A, EU-LIBRARY_SCIENCE-A, EU-LINEAR_ALGEBRA_BASICS-A, EU-LINGUISTIC_TYPOLOGY_BASICS-A, EU-LITERATURE-A, EU-LIVESTOCK_SYSTEMS_BASICS-A, EU-MACROECONOMICS_BASICS-A, EU-MANUFACTURING_PROCESSES_BASICS-A, EU-MARKET_DESIGN_BASICS-A, EU-MEASUREMENT_INSTRUMENTATION_BASICS-A, EU-MEASUREMENT_SCIENCE_BASICS-A, EU-METEOROLOGY_BASICS-A, EU-MICROBIOME_BASICS-A, EU-MICROECONOMICS_BASICS-B, EU-MINERALOGY_BASICS-A, EU-MOTION_BASICS-A, EU-NETWORK_ANALYSIS_BASICS-A, EU-NUMBER_THEORY_BASICS-A, EU-NUMERICAL_METHODS_BASICS-A.

## 5. Distinct Source IDs directly checked in this tranche

85 distinct Source records were fetched; all had the expected record ID and version @1:

SRC-AGRICULTURE_BASICS, SRC-AI_ETHICS_BASICS, SRC-ANATOMY_BASICS, SRC-ARCHIVAL_DESCRIPTION_BASICS, SRC-ARTIFICIAL_INTELLIGENCE_BASICS, SRC-ATMOSPHERIC_SCIENCE_BASICS, SRC-BIODIVERSITY_BASICS, SRC-BUILDING_ENVELOPE_BASICS, SRC-CALCULUS_BASICS, SRC-CARTOGRAPHY, SRC-CLIMATE_ADAPTATION, SRC-CLIMATE_BASICS, SRC-CLOUD_COMPUTING_BASICS, SRC-COMBINATORICS_BASICS, SRC-COMPARATIVE_CIVILIZATIONS_BASICS, SRC-COMPUTER_ARCHITECTURE_BASICS, SRC-COMPUTER_GRAPHICS_BASICS, SRC-CONSERVATION_BIOLOGY_BASICS, SRC-CONSTRUCTION_PROJECT_MANAGEMENT_BASICS, SRC-CRYPTOGRAPHY_BASICS, SRC-CULTURAL_ANTHROPOLOGY, SRC-CULTURAL_HERITAGE, SRC-CYBERSECURITY_BASICS, SRC-DATABASES_BASICS, SRC-DEMOGRAPHIC_METHODS_BASICS, SRC-DEVELOPMENTAL_BIOLOGY_BASICS, SRC-DEVELOPMENT_ECONOMICS_BASICS, SRC-DIPLOMACY_BASICS, SRC-DISTRIBUTED_SYSTEMS_BASICS, SRC-EARTH_SYSTEM_BASICS, SRC-ECONOMIC_HISTORY, SRC-ECONOMICS_BASICS, SRC-EDUCATION_SCIENCE_BASICS, SRC-EMBEDDED_SYSTEMS_BASICS, SRC-ENERGY_SECURITY_BASICS, SRC-ENGINEERING_DESIGN_BASICS, SRC-ENVIRONMENTAL_MONITORING_BASICS, SRC-ENVIRONMENTAL_POLICY_BASICS, SRC-FINANCE_BASICS, SRC-FISHERIES_BASICS, SRC-FOOD_FERMENTATION_BASICS, SRC-FOOD_SYSTEMS, SRC-FORESTRY_BASICS, SRC-GEOLOGIC_MAPPING_BASICS, SRC-GEOMETRY_BASICS, SRC-GEOMORPHOLOGY_BASICS, SRC-GEOSPATIAL_ANALYSIS_BASICS, SRC-HISTORICAL_GEOGRAPHY, SRC-HISTORY_OF_ENGINEERING, SRC-HISTORY_OF_MATHEMATICS, SRC-HISTORY_OF_SCIENCE, SRC-HISTORY_OF_TECHNOLOGY, SRC-HOUSING_SYSTEMS_BASICS, SRC-HUMANITARIAN_LOGISTICS_BASICS, SRC-HUMAN_AI_INTERACTION_BASICS, SRC-HUMAN_RIGHTS_BASICS, SRC-HYDROPOWER_BASICS, SRC-INFORMATION_RETRIEVAL_BASICS, SRC-INFRASTRUCTURE_GOVERNANCE_BASICS, SRC-INTERNATIONAL_RELATIONS_BASICS, SRC-LABOR_RELATIONS_BASICS, SRC-LAND_USE_PLANNING_BASICS, SRC-LIBRARY_SCIENCE, SRC-LINEAR_ALGEBRA_BASICS, SRC-LINGUISTIC_TYPOLOGY_BASICS, SRC-LITERATURE, SRC-LIVESTOCK_SYSTEMS_BASICS, SRC-MACROECONOMICS_BASICS, SRC-MANUFACTURING_PROCESSES_BASICS, SRC-MARKET_DESIGN_BASICS, SRC-MEASUREMENT_INSTRUMENTATION_BASICS, SRC-MEASUREMENT_SCIENCE_BASICS, SRC-MEASUREMENT_UNCERTAINTY_BASICS, SRC-METEOROLOGY_BASICS, SRC-MICROBIOME_BASICS, SRC-MICROECONOMICS_BASICS, SRC-MINERALOGY_BASICS, SRC-MOTION_BASICS, SRC-NETWORK_ANALYSIS_BASICS, SRC-NUMBER_THEORY_BASICS, SRC-NUMERICAL_METHODS_BASICS, SRC-STATISTICS_INFERENCE_BASICS, SRC-WASTE_INFRASTRUCTURE_BASICS, SRC-WATER_RESOURCES_BASICS, SRC-WATER_RESOURCES_MANAGEMENT_BASICS.

## 6. Boundaries and next actions

- The 356 queue is now exactly reconstructed and independently reconciled to the coverage artifact, claim worksheet, and 20-Claim priority review.
- 114/356 EU files have fresh or previously documented direct canonical checks; 242 remain.
- 85/135 distinct Source files have been directly fetched; 50 remain.
- All checks are structural identity/version/link checks. They do not establish source passage support, locator reproducibility, source independence, rights clearance, or expert acceptance.
- Source-review filename mentions still require exact report-body Claim/EU/Source/version matching before any findings are imported.
- No canonical Claim, EU, Source, Assessment, Relation, risk, allowlist, or publication record was modified.
- No D/E/B score was assigned or transferred. No write permission was created.
- PR #21 remains Draft/unmerged; main remains untouched.
