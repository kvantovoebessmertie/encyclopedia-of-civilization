# Relation Context Isolation — Implementation Report

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Branch: `mvp-public-contribution-design-2026-10-11`  
Implementation base HEAD: `158b9eafef93e59d28f335cfb2619db3fdbe325a`  
Status: **61/61 target-specific Context records created; 61/61 Relation frame references versioned and redirected; 2 intentional exceptions preserved.**

## Owner decision

On 2026-11-20 the owner approved Option A:
- create one target-specific Context record for each Relation that had reused the shared `CTX-CROSS-SLICE-LINKAGE@1`;
- retain the existing shared Context for its own target Relation only;
- preserve the independent local Context of the water-storage Relation;
- do not change Relation semantics, participants, roles, direction, relation type, or HOLD/release decisions.

## Implementation

For each of the 61 affected Relations:
1. Created one new Context record `CTX-<Relation record_id>@1` in the same vertical-slice `records/` directory.
2. Set the new Context `target_ref` to the incremented exact version of its one Relation.
3. Copied that Relation's existing `provenance.created_from` references exactly into the Context provenance. No new sources, claims, evidence, or factual assertions were introduced.
4. Used the bounded context statement: “связь между участниками фиксируется только в пределах явно указанного типа Relation и не заменяет исходные Claim, Scope или Evidence Use”.
5. Incremented the Relation record version by one and changed only `content.frame_ref` to the new Context @1.

The change is structural and versioned. The Relation proposition itself was not rewritten.

## Target-specific Context records

- `CTX-REL-CROSS-AIR-POWER-SYSTEMS@1`
- `CTX-REL-CROSS-ALERTS-WILDFIRE-SMOKE@1`
- `CTX-REL-CROSS-AMR-PLANT-HEALTH@1`
- `CTX-REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY@1`
- `CTX-REL-CROSS-CLIMATE-INFRASTRUCTURE-RESILIENCE@1`
- `CTX-REL-CROSS-CO-EMERGENCY-ESCALATION@1`
- `CTX-REL-CROSS-CO-PREVENTION@1`
- `CTX-REL-CROSS-DISASTER-BUILDING-SERVICES@1`
- `CTX-REL-CROSS-EARTHQUAKE-AFTERSHOCK@1`
- `CTX-REL-CROSS-ETHNOBOTANY-AGRIFOOD@1`
- `CTX-REL-CROSS-FLOOD-HAZARDOUS-WASTE@1`
- `CTX-REL-CROSS-FLOOD-SAFETY@1`
- `CTX-REL-CROSS-FOOD-DISTRIBUTION-LOGISTICS@1`
- `CTX-REL-CROSS-FOOD-PUBLIC-HEALTH@1`
- `CTX-REL-CROSS-GEODESY-SURVEYING@1`
- `CTX-REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@1`
- `CTX-REL-CROSS-HISTORY-GEOGRAPHY-ECONOMIC-HISTORY@1`
- `CTX-REL-CROSS-HOME-FIRE-ALERTS@1`
- `CTX-REL-CROSS-INDUSTRIAL-PROCUREMENT@1`
- `CTX-REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY@1`
- `CTX-REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@1`
- `CTX-REL-CROSS-LIGHTING-HOME-FIRE@1`
- `CTX-REL-CROSS-M2-AGRICULTURE-SOIL@1`
- `CTX-REL-CROSS-M2-ENERGY-SECURITY-RESILIENCE@1`
- `CTX-REL-CROSS-M2-GEOGRAPHIC-COORDINATES-GEODESY@1`
- `CTX-REL-CROSS-M2-MEASUREMENT-UNCERTAINTY-SCIENCE@1`
- `CTX-REL-CROSS-M2-RISK-MANAGEMENT-ANALYSIS@1`
- `CTX-REL-CROSS-M2-STATISTICS-RESEARCH@1`
- `CTX-REL-CROSS-MANUFACTURING-HUMAN-FACTORS@1`
- `CTX-REL-CROSS-MATH-ENGINEERING-HISTORY@1`
- `CTX-REL-CROSS-MEASUREMENT-CALIBRATION@1`
- `CTX-REL-CROSS-MECHANICAL-METALLURGY@1`
- `CTX-REL-CROSS-MIGRATION-LABOR-ECONOMICS@1`
- `CTX-REL-CROSS-PLANTPATH-ENTOMOLOGY@1`
- `CTX-REL-CROSS-POLITICAL-ECONOMY-TAXATION@1`
- `CTX-REL-CROSS-QUANTUM-MEASUREMENT@1`
- `CTX-REL-CROSS-RESEARCH-STATISTICS@1`
- `CTX-REL-CROSS-SANITATION-HYGIENE@1`
- `CTX-REL-CROSS-SANITATION-WASTEWATER@1`
- `CTX-REL-CROSS-SEPTIC-FLOOD-SANITATION@1`
- `CTX-REL-CROSS-SETTLEMENT-ENERGY@1`
- `CTX-REL-CROSS-SETTLEMENT-HOUSING@1`
- `CTX-REL-CROSS-SETTLEMENT-INFRASTRUCTURE@1`
- `CTX-REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@1`
- `CTX-REL-CROSS-SETTLEMENT-TRANSPORTATION@1`
- `CTX-REL-CROSS-SETTLEMENT-WATER@1`
- `CTX-REL-CROSS-STANDARDS-QUALITY@1`
- `CTX-REL-CROSS-WATER-CLIMATE-ADAPTATION@1`
- `CTX-REL-CROSS-WATER-FILTER@1`
- `CTX-REL-CROSS-WATER-QUALITY-TREATMENT@1`
- `CTX-REL-P11-CONSTRUCTION-SAFETY-ENGINEERING@1`
- `CTX-REL-P11-INFORMATION-CRITICAL-THINKING@1`
- `CTX-REL-P11-INFRASTRUCTURE-SYSTEMS-THINKING@1`
- `CTX-REL-P11-RISK-COMMUNICATION@1`
- `CTX-REL-P11-RISK-SYSTEMS-THINKING@1`
- `CTX-REL_M3_EMERGENCY_INFRASTRUCTURE@1`
- `CTX-REL_M3_FIRE_SAFETY_EMERGENCY_MANAGEMENT@1`
- `CTX-REL_M3_FOOD_PRESERVATION_SAFETY@1`
- `CTX-REL_M3_SCIENTIFIC_METHOD_RESEARCH@1`
- `CTX-REL_M3_SHELTER_SETTLEMENT@1`
- `CTX-REL_M3_WATER_RESOURCES_HYDROLOGY@1`

## Preserved exceptions

- `REL-CROSS-WATER-CHEMICAL@1` retains `CTX-CROSS-SLICE-LINKAGE@1`; that shared Context remains targeted only to this Relation.
- `REL-CONTAINER-WATER-STORAGE@1` retains its existing `CTX-WATER-STORAGE-EMERGENCY@1`. Its separate semantic HOLD issue is not resolved by this architecture change.

## Explicitly unchanged

- Relation types, participants, participant versions, roles, direction, and relation semantics.
- Claim, Source, Evidence Use, Scope, Event, Object, and State records.
- Publication/HOLD/INCLUDE/EXCLUDE status, allowlists, deployment, release eligibility, and Human View decisions.
- `main`; no merge or release action.

All 63 Relations remain on HOLD pending their separate semantic, evidence, rights, and independent-review gates. This implementation closes only the shared-Context target-applicability defect; it does not clear the earthquake Event or water-storage State semantic holds.

## Verification required after commit

- Exact-head JSON/schema and reference tests.
- Confirm 61 new Context records, each with exactly one Relation target.
- Confirm each of the 61 Relations points to its matching Context @1.
- Confirm the two preserved exceptions above.
- Confirm all Relation semantics/participants/roles/direction are byte-for-byte unchanged apart from record version and `frame_ref`.
- Confirm PR remains OPEN · DRAFT · NOT MERGED and `main` is unchanged.
