# M13 Relation Graph Audit — Structural and Cross-Slice Integrity

Branch: `m13-system-wide-depth-audit-2026-10-09`
Scope: all Relation JSON records in the current branch tree.
Status: in progress. This is a structural graph audit; it does not by itself validate the scientific meaning or independence of linked evidence.

## Method
For each Relation record, inspect `record_id`, `relation_type`, participants, roles, direction, `frame_ref`, and provenance `created_from`. Check that every participant, frame/context and provenance Source pointer resolves to a record path in the corpus using comparison-only separator normalization. Check role cardinality against participant cardinality. Do not rewrite identifiers or records.

## Relation ledger
| # | Relation path | internal record_id | relation_type | participants | roles/direction | frame_ref | source provenance | Structural assessment |
|---:|---|---|---|---|---|---|---|---|
| 1 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-AIR-POWER-SYSTEMS.json` | pending | pending | pending | pending | pending | pending |
| 2 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-ALERTS-WILDFIRE-SMOKE.json` | pending | pending | pending | pending | pending | pending |
| 3 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-AMR-PLANT-HEALTH.json` | pending | pending | pending | pending | pending | pending |
| 4 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY.json` | pending | pending | pending | pending | pending | pending |
| 5 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CLIMATE-INFRASTRUCTURE-RESILIENCE.json` | pending | pending | pending | pending | pending | pending |
| 6 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CO-EMERGENCY-ESCALATION.json` | pending | pending | pending | pending | pending | pending |
| 7 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CO-PREVENTION.json` | pending | pending | pending | pending | pending | pending |
| 8 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-DISASTER-BUILDING-SERVICES.json` | pending | pending | pending | pending | pending | pending |
| 9 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-EARTHQUAKE-AFTERSHOCK.json` | pending | pending | pending | pending | pending | pending |
| 10 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-ETHNOBOTANY-AGRIFOOD.json` | pending | pending | pending | pending | pending | pending |
| 11 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-FLOOD-HAZARDOUS-WASTE.json` | pending | pending | pending | pending | pending | pending |
| 12 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-FLOOD-SAFETY.json` | pending | pending | pending | pending | pending | pending |
| 13 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-FOOD-DISTRIBUTION-LOGISTICS.json` | pending | pending | pending | pending | pending | pending |
| 14 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-FOOD-PUBLIC-HEALTH.json` | pending | pending | pending | pending | pending | pending |
| 15 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-GEODESY-SURVEYING.json` | pending | pending | pending | pending | pending | pending |
| 16 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY.json` | pending | pending | pending | pending | pending | pending |
| 17 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-HISTORY-GEOGRAPHY-ECONOMIC-HISTORY.json` | pending | pending | pending | pending | pending | pending |
| 18 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-HOME-FIRE-ALERTS.json` | pending | pending | pending | pending | pending | pending |
| 19 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-INDUSTRIAL-PROCUREMENT.json` | pending | pending | pending | pending | pending | pending |
| 20 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY.json` | pending | pending | pending | pending | pending | pending |
| 21 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION.json` | pending | pending | pending | pending | pending | pending |
| 22 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-LIGHTING-HOME-FIRE.json` | pending | pending | pending | pending | pending | pending |
| 23 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-AGRICULTURE-SOIL.json` | pending | pending | pending | pending | pending | pending |
| 24 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-ENERGY-SECURITY-RESILIENCE.json` | pending | pending | pending | pending | pending | pending |
| 25 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-GEOGRAPHIC-COORDINATES-GEODESY.json` | pending | pending | pending | pending | pending | pending |
| 26 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-MEASUREMENT-UNCERTAINTY-SCIENCE.json` | pending | pending | pending | pending | pending | pending |
| 27 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-RISK-MANAGEMENT-ANALYSIS.json` | pending | pending | pending | pending | pending | pending |
| 28 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-M2-STATISTICS-RESEARCH.json` | pending | pending | pending | pending | pending | pending |
| 29 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MANUFACTURING-HUMAN-FACTORS.json` | pending | pending | pending | pending | pending | pending |
| 30 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MATH-ENGINEERING-HISTORY.json` | pending | pending | pending | pending | pending | pending |
| 31 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MEASUREMENT-CALIBRATION.json` | pending | pending | pending | pending | pending | pending |
| 32 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MECHANICAL-METALLURGY.json` | pending | pending | pending | pending | pending | pending |
| 33 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-MIGRATION-LABOR-ECONOMICS.json` | pending | pending | pending | pending | pending | pending |
| 34 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-PLANTPATH-ENTOMOLOGY.json` | pending | pending | pending | pending | pending | pending |
| 35 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-POLITICAL-ECONOMY-TAXATION.json` | pending | pending | pending | pending | pending | pending |
| 36 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-QUANTUM-MEASUREMENT.json` | pending | pending | pending | pending | pending | pending |
| 37 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-RESEARCH-STATISTICS.json` | pending | pending | pending | pending | pending | pending |
| 38 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SANITATION-HYGIENE.json` | pending | pending | pending | pending | pending | pending |
| 39 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SANITATION-WASTEWATER.json` | pending | pending | pending | pending | pending | pending |
| 40 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SEPTIC-FLOOD-SANITATION.json` | pending | pending | pending | pending | pending | pending |
| 41 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-ENERGY.json` | pending | pending | pending | pending | pending | pending |
| 42 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-HOUSING.json` | pending | pending | pending | pending | pending | pending |
| 43 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-INFRASTRUCTURE.json` | pending | pending | pending | pending | pending | pending |
| 44 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-PUBLIC-HEALTH.json` | pending | pending | pending | pending | pending | pending |
| 45 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-TRANSPORTATION.json` | pending | pending | pending | pending | pending | pending |
| 46 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-SETTLEMENT-WATER.json` | pending | pending | pending | pending | pending | pending |
| 47 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-STANDARDS-QUALITY.json` | pending | pending | pending | pending | pending | pending |
| 48 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-TELECOM-ENERGY-RESILIENCE.json` | pending | pending | pending | pending | pending | pending |
| 49 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-WATER-CHEMICAL.json` | pending | pending | pending | pending | pending | pending |
| 50 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-WATER-CLIMATE-ADAPTATION.json` | pending | pending | pending | pending | pending | pending |
| 51 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-WATER-FILTER.json` | pending | pending | pending | pending | pending | pending |
| 52 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-WATER-QUALITY-TREATMENT.json` | pending | pending | pending | pending | pending | pending |
| 53 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-CONSTRUCTION-SAFETY-ENGINEERING.json` | pending | pending | pending | pending | pending | pending |
| 54 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-INFORMATION-CRITICAL-THINKING.json` | pending | pending | pending | pending | pending | pending |
| 55 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING.json` | pending | pending | pending | pending | pending | pending |
| 56 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-RISK-COMMUNICATION.json` | pending | pending | pending | pending | pending | pending |
| 57 | `CONTENT/vertical-slices/cross-slice-linkage/records/REL-P11-RISK-SYSTEMS-THINKING.json` | pending | pending | pending | pending | pending | pending |
| 58 | `CONTENT/vertical-slices/emergency-management-basics/records/REL-M3-EMERGENCY-INFRASTRUCTURE.json` | pending | pending | pending | pending | pending | pending |
| 59 | `CONTENT/vertical-slices/emergency-water-storage-state/records/REL-CONTAINER-WATER-STORAGE.json` | pending | pending | pending | pending | pending | pending |
| 60 | `CONTENT/vertical-slices/fire-safety-basics/records/REL-M3-FIRE-SAFETY-EMERGENCY-MANAGEMENT.json` | pending | pending | pending | pending | pending | pending |
| 61 | `CONTENT/vertical-slices/food-preservation-basics/records/REL-M3-FOOD-PRESERVATION-SAFETY.json` | pending | pending | pending | pending | pending | pending |
| 62 | `CONTENT/vertical-slices/scientific-method-basics/records/REL-M3-SCIENTIFIC-METHOD-RESEARCH.json` | pending | pending | pending | pending | pending | pending |
| 63 | `CONTENT/vertical-slices/shelter-basics/records/REL-M3-SHELTER-SETTLEMENT.json` | pending | pending | pending | pending | pending | pending |
| 64 | `CONTENT/vertical-slices/water-resources-basics/records/REL-M3-WATER-RESOURCES-HYDROLOGY.json` | pending | pending | pending | pending | pending | pending |

## Interpretation limits
- Endpoint existence does not prove the relation is substantively justified.
- A Relation that links domains is not itself evidence that the underlying Claims share a source or are independent.
- Source independence, claim-level support, and relation semantics require a separate pass.
- No Claim, Evidence Use, Source, or Relation JSON edits are authorized by this audit.
- Keep PR #21 open as Draft and leave `main` unchanged.
