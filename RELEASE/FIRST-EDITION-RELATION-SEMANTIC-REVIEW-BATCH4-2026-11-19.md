# First Edition — Cross-Slice Relation Semantic Review — Batch 4

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `81a2e174d69c206d8b2ade2b776479de8c23f84e`

## Scope and method

Eight additional Relations not covered by Batches 1–3 were fetched from canonical JSON. Both exact participant Claims and both provenance Source records were fetched from their owning slices. Identity, version, record type, Claim provenance, Relation provenance, role structure, direction, and frame references were checked.

This review evaluates only whether the Relation is a defensible cross-slice navigation link. It does not treat a Relation as evidence, causation, or proof. No canonical JSON, candidate decision, or allowlist was changed. All endpoint Claims remain HOLD.

## Exact verification

- 8/8 Relation records: exact ID, version, and `record_type=relation`.
- 16/16 participant Claims: exact ID, version, and `record_type=claim`.
- 16/16 provenance Source references fetched; 15 unique Source records because the infrastructure-resilience Source is shared by two Relations.
- All fetched Sources match their declared exact IDs, versions, and `record_type=source`.
- Claim provenance Source identities match the corresponding Relation `created_from` references.
- 8/8 Relations use `CTX-CROSS-SLICE-LINKAGE@1`; both participant roles and undirected direction fields were inspected.

## Relation-by-relation semantic findings

| Relation/version | Exact participant pair | Semantic assessment | Release-use disposition |
|---|---|---|---|
| `REL-CROSS-FLOOD-HAZARDOUS-WASTE@1` | Flood re-entry hazard escalation; hazardous-waste segregation | Both apply to safe flood cleanup but address distinct hazard boundaries: unsafe re-entry pending professional inspection versus identification and separate handling of hazardous waste. Useful as adjacent safety controls, not interchangeable instructions. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; keep the two hazard controls distinct and retain HOLD for publication eligibility. |
| `REL-CROSS-FOOD-DISTRIBUTION-LOGISTICS@1` | Food distribution chain; humanitarian logistics | Food distribution explicitly includes procurement, storage, transport, and delivery; humanitarian logistics addresses constraints in delivering aid to affected populations. The operational intersection is direct and useful. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |
| `REL-CROSS-FOOD-PUBLIC-HEALTH@1` | Household food security; public-health purpose | Household access to adequate food is relevant to population health, but the selected public-health Claim is only a broad definition of public health. The pair does not establish the specific food-security/population-health relationship implied by the Relation label. | HOLD — the public-health endpoint is too generic to support the named relationship. |
| `REL-CROSS-M2-AGRICULTURE-SOIL@1` | Agricultural productivity factors; soil as a natural system | The agriculture Claim explicitly lists soil among the interacting determinants of productivity; the soil Claim defines the system's components. This is a direct conceptual dependency. The Relation is nevertheless marked undirected, so it must not be interpreted as a directed causal edge. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; no causal/directional inference; retain HOLD for publication eligibility. |
| `REL-CROSS-M2-ENERGY-SECURITY-RESILIENCE@1` | Energy security; community resilience | Energy security includes reliability and resistance to supply disruption; community resilience includes preparing for hazards, withstanding disruption, and recovery. A useful resilience-planning intersection exists, but the selected resilience Claim is community-wide rather than specifically about energy infrastructure. | ACCEPT WITH RESTRICTION — contextual navigation only at the community-resilience level; do not imply an energy-specific infrastructure dependency; retain HOLD for publication eligibility. |
| `REL-CROSS-M2-GEOGRAPHIC-COORDINATES-GEODESY@1` | Coordinate-system/accuracy selection; geodetic measurement foundation | The coordinate Claim makes reference-system choice and accuracy task-dependent; the geodesy Claim describes consistent coordinate definition and spatial reference foundations. The two are complementary and closely aligned. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |
| `REL-CROSS-M2-MEASUREMENT-UNCERTAINTY-SCIENCE@1` | Measurement-result uncertainty; metrology | Interpreting a measurement with its uncertainty is a direct foundational application of metrology. The link is conceptually sound, but the metrology Claim is broad and does not itself define uncertainty evaluation. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; do not treat the broad metrology Claim as a substitute for uncertainty guidance; retain HOLD for publication eligibility. |
| `REL-CROSS-M2-RISK-MANAGEMENT-ANALYSIS@1` | Risk-management definition; risk-analysis assessment boundary | Both Claims center risk assessment on objectives and context: risk is the effect of uncertainty on objectives, while analysis requires defining objectives, scope, assumptions, constraints, and information sources. The link is coherent and useful as a conceptual sequence, but both records remain independent Claims. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |

## Cross-cutting frame limitation

All eight Relations reference `CTX-CROSS-SLICE-LINKAGE@1`. The previously identified target-scope ambiguity remains open: the Context record's `target_ref` names `REL-CROSS-WATER-CHEMICAL@1` specifically. A matching frame ID/version is not, by itself, proof that this Context is applicable to every Relation. Do not interpret the target reference as a wildcard. This remains a release blocker until schema and Context applicability are resolved.

## Result

- Structurally exact: 8 Relations, 16 Claims, 16 Source-reference edges (15 unique Source records).
- Semantic dispositions: 7 contextual-navigation candidates (one restricted); 1 HOLD for release use due to an overly generic endpoint.
- No canonical records changed.
- No Claim or Relation promoted to INCLUDE.
- No Relation approved for release.

## Remaining work

Continue the remaining unreviewed Relations in bounded batches. Keep contextual links separate from evidence and causal claims. Resolve the shared Context target-scope ambiguity before any Relation can be considered release-eligible.
