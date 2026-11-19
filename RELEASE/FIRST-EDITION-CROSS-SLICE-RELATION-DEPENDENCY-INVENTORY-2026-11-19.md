# First Edition — Cross-Slice Relation Dependency Inventory

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `5779c3b2dd6e1276b3c5d7d3b19f83e86ae93aca`  
Status: **INVENTORY IN PROGRESS — NO RELATION APPROVAL OR PUBLICATION DECISION**

## Scope and rules

This is a separate inventory of canonical `relation` records. Relations are not included in the 809-row vertical-slice candidate denominator. This file records exact relation versions and declared participants/frame references; path existence is not proof of participant version correctness, semantic validity, or release eligibility.

- No Relation, Claim, Evidence Use, Source, Context or Scope record is modified.
- All existing HOLD decisions remain unchanged.
- Relation dependencies must be resolved to exact participant record IDs and versions before any candidate allowlist is considered.

## Exact relation records

| Relation/version | Relation type | Declared participants (path lookup only) | Frame reference | Canonical path |
|---|---|---|---|---|
| `REL-CROSS-AIR-POWER-SYSTEMS@1` | air_quality_and_energy_systems_link | CLM-AIR_QUALITY_BASICS-A@1 [path]; CLM-POWER_SYSTEMS_BASICS-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-AIR-POWER-SYSTEMS.json |
| `REL-CROSS-ALERTS-WILDFIRE-SMOKE@1` | public_alerts_and_wildfire_smoke_response | CLM-ALERTS-ENABLE-RESPOND@1 [path]; CLM-WILDFIRE-AIR-QUALITY@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-ALERTS-WILDFIRE-SMOKE.json |
| `REL-CROSS-AMR-PLANT-HEALTH@1` | one_health_plant_health_link | CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1 [path]; CLM-PLANT_PATHOLOGY_BASICS-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-AMR-PLANT-HEALTH.json |
| `REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY@2` | shared_spatial_representation_context | CLM-CARTOGRAPHY-A@2 [path]; CLM-SETTLEMENT_GEOGRAPHY-A@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CARTOGRAPHY-SETTLEMENT-GEOGRAPHY.json |
| `REL-CROSS-CLIMATE-INFRASTRUCTURE-RESILIENCE@1` | adaptation_resilience_planning_link | CLM-CLIMATE_ADAPTATION-C@1 [path]; CLM-INFRASTRUCTURE_RESILIENCE-C@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CLIMATE-INFRASTRUCTURE-RESILIENCE.json |
| `REL-CROSS-CO-EMERGENCY-ESCALATION@1` | shared_carbon_monoxide_emergency_escalation | CLM-CO-HEATING-EMERGENCY@1 [path]; CLM-GENERATOR-CO-ALARM-EMERGENCY@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CO-EMERGENCY-ESCALATION.json |
| `REL-CROSS-CO-PREVENTION@1` | shared_carbon_monoxide_prevention | CLM-GENERATOR-OUTSIDE-20FT@1 [path]; CLM-CO-HEATING-OUTSIDE@1 [path] | `CTX-CROSS-SLICE-LINKAGE@1` | CONTENT/vertical-slices/cross-slice-linkage/records/REL-CROSS-CO-PREVENTION.json |

## Current batch

- Canonical relation JSON files discovered in the repository tree: 63.
- Relation records inspected in this batch: 7.
- Participant references are listed verbatim; bracketed path markers only indicate a matching filename exists somewhere in the corpus tree.
- Remaining relation files: 56.

## Next

Continue the remaining relation inventory, then validate each participant's exact canonical `record_id@record_version`, record type, and slice ownership. Resolve missing/stale references and ensure relations are only included where both endpoint records are eligible and the relation itself is approved.
