# First Edition — Cross-Slice Relation Semantic Review — Batch 3

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `cd6ce793d4e2d540b5167c272a84f702d85686ff`

## Scope and method

Eight previously unreviewed Relation records were re-fetched from canonical JSON at the inspection HEAD. For each relation, both participant Claims and both provenance Source records were fetched from their owning vertical slices. Exact `record_id`, `record_version`, and `record_type` were checked; Claim provenance Source identity was compared with the Relation's `created_from` entries. The shared Context frame was fetched independently.

This is a structural and semantic navigation review only. A Relation is not evidence for either participant Claim, does not establish causation, and does not transfer evidence or release eligibility between slices. No canonical JSON, allowlist, or publication decision was changed. All Claims remain HOLD.

## Exact verification

- 8/8 Relation records: exact ID, version, and `record_type=relation`.
- 16/16 participant Claims: exact ID, version, and `record_type=claim`.
- 16/16 provenance Sources: exact ID, version, and `record_type=source`.
- 16/16 Claim provenance Source references match the corresponding Relation provenance source identity.
- 8/8 Relations use the exact shared frame `CTX-CROSS-SLICE-LINKAGE@1`; the frame itself was fetched and verified as `record_type=context`.
- 8/8 Relations have two `linked_record` roles and `direction=undirected`.

## Relation-by-relation semantic findings

| Relation/version | Exact participant pair | Semantic assessment | Release-use disposition |
|---|---|---|---|
| `REL-CROSS-AIR-POWER-SYSTEMS@1` | Air-quality monitoring Claim A; power-system structure Claim A | The Claims describe two separate systems. Their coexistence is not itself a demonstrated dependency or operational interaction. The relation label is broader than the evidence in the two statements. | HOLD — do not present as a substantive dependency; at most a future editorial navigation link after its intended connection is stated and supported. |
| `REL-CROSS-AMR-PLANT-HEALTH@1` | AMR Claim C; Plant Pathology Claim A | AMR Claim C explicitly names plants and the environment, but the plant-pathology Claim only defines the discipline. It does not state that the cited plant disease topic is antimicrobial resistance or identify a plant AMR mechanism. One Health is a plausible frame, but the endpoint pair does not establish the specific plant-health link claimed by the Relation. | HOLD — semantic endpoint mismatch / insufficient specificity. |
| `REL-CROSS-CLIMATE-INFRASTRUCTURE-RESILIENCE@1` | Climate Adaptation Claim C; Infrastructure Resilience Claim C | Both Claims concern planning under risk and residual effects: adaptation measures require assessment of limits and residual risk; infrastructure resilience planning uses service and recovery objectives. This is a coherent planning-level cross-reference, not evidence that one Claim proves the other. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |
| `REL-CROSS-GEODESY-SURVEYING@1` | Geodesy Claim B; Surveying Claim A | Strong conceptual complementarity: geodetic coordinates provide a consistent spatial reference, while surveying measurements determine positions and geometry of areas. The relation is a legitimate disciplinary navigation link. It does not make the Claims interchangeable. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |
| `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@1` | Groundwater Claim A; Soil Microbiology Claim A | Both concern subsurface environmental systems, but neither statement explicitly connects groundwater conditions to soil microbial communities. The link is useful only as a broad environmental-systems pointer; it must not imply a demonstrated hydrobiological effect. | HOLD — the selected endpoints do not state a specific groundwater-to-soil-microbiology relationship. A broad environmental-systems association is insufficient for the Relation's stated subsurface water/soil biology link. |
| `REL-CROSS-HISTORY-GEOGRAPHY-ECONOMIC-HISTORY@1` | Historical Geography Claim A; Economic History Claim A | Both use historical evidence with a spatial/temporal dimension: historical maps are place- and time-specific sources, while long-run production and income estimates support analysis of economic change. The shared analytical context is defensible. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |
| `REL-CROSS-INDUSTRIAL-PROCUREMENT@1` | Industrial Engineering Claim A; Public Procurement Claim A | Industrial engineering includes integrated systems of people, materials, information, equipment, and energy; procurement is an organized acquisition process. Their interface is plausible in project delivery, but the two Claims do not establish procurement as a component of industrial engineering or a specific systems dependency. | ACCEPT WITH RESTRICTION — contextual navigation only, explicitly framed as an operational interface; retain HOLD for publication eligibility. |
| `REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY@2` | Labor Economics Claim C; Social Policy Claim C | Labor-market indicators (employment, earnings, hours, productivity, underutilization) are relevant inputs for assessing social protection and policy conditions, while social protection varies by country and program. The relationship is relevant at the measurement/policy context level, not a causal claim. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |

## Cross-cutting frame limitation

The shared frame `CTX-CROSS-SLICE-LINKAGE@1` was structurally verified, and its condition describes cross-slice relations as a shared semantic frame that does not replace Claim, Scope, or Evidence Use. However, its own `target_ref` points specifically to `REL-CROSS-WATER-CHEMICAL@1`, not to the eight Relations in this batch. This creates an applicability ambiguity: a correct frame ID/version alone does not prove that the Context record is authorized or semantically scoped for every Relation that references it. Do not silently reinterpret the target reference as a wildcard. Record-level schema/Context applicability must be resolved before any of these Relations can be treated as release-eligible.

## Result

- Structurally exact: 8 Relations, 16 Claims, 16 Sources, and 1 Context frame.
- Semantic dispositions: 5 contextual-navigation candidates (with restrictions where noted); 3 HOLD for release use due to weak or insufficiently specific endpoint relationships.
- No canonical records changed.
- No Claim promoted from HOLD.
- No Relation approved for release.
- The eight relations are counted as semantically reviewed for audit coverage, not as release-approved.

## Remaining work

Continue with the next unreviewed Relations in bounded batches. For each, retain exact-version checks and test the stated semantic link against the actual participant statements, not merely shared subject labels. Separately resolve the shared Context frame's target-scope ambiguity. Keep Relation semantics, participant Claim quality, evidence sufficiency, rights, and release approval as distinct gates.
