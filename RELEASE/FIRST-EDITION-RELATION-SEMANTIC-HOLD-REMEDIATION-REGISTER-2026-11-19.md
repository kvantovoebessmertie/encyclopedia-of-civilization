# First Edition — Semantic HOLD Relation Remediation Register

Date: 2026-11-19  
Scope: the 15 Relations retained on semantic HOLD after the 63/63 review.  
Status: **REMEDIATION PROPOSALS ONLY — no canonical changes or decision promotions authorized.**

## Remediation principles

- A Relation can be corrected only by changing its endpoint pair, narrowing its stated semantics, or removing it from the release allowlist.
- Do not broaden a Claim to make a Relation fit.
- Do not infer a mechanism, dependency, causation, or evidence link from shared subject area.
- Any replacement endpoint must be an existing exact-version Claim with its own verified Evidence Use/Source chain, or a newly authorized and independently reviewed record.
- If no direct endpoint pair is available, retain HOLD or exclude the Relation from the release candidate.
- A corrected Relation remains HOLD until its endpoints and the Relation pass all independent release gates.

## Individual remediation register

| Relation | HOLD reason established by audit | Minimum defensible closure path | Required verification |
|---|---|---|---|
| `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3` | Library Claim A is access-focused; it does not state preservation. | Replace the library endpoint with an existing library-preservation Claim, or narrow the Relation to information access/collection stewardship only if the archive endpoint supports that exact meaning. | Exact Claim version/type, source locator, direct semantic overlap; no claim that access equals preservation. |
| `REL-CROSS-CO-EMERGENCY-ESCALATION@1` | Two participant Claims substantially overlap in the same emergency escalation sequence. | Retain only if the two Claims represent materially distinct exposure scenarios or stages; otherwise remove the redundant Relation from the release set. | Side-by-side proposition comparison; distinct contribution from each endpoint; no duplicate support count. |
| `REL-CROSS-AIR-POWER-SYSTEMS@1` | Air-quality monitoring and power-system structure are separate systems; no dependency is stated. | Remove from release use unless an existing Claim directly establishes an air-quality/power-system interaction (e.g. emissions, generation, or monitoring dependency) within the declared scope. | Exact interaction Claim and Source locator; no inferred co-location or general environmental association. |
| `REL-CROSS-AMR-PLANT-HEALTH@1` | AMR Claim C mentions plants/environment, but Plant Pathology Claim A only defines the discipline. | Use a plant-specific antimicrobial resistance, plant pathogen, or One Health endpoint if one exists and directly matches the Relation; otherwise narrow or remove. | Direct plant-health/AMR proposition; exact source and locator; preserve human/animal/plant distinctions. |
| `REL-CROSS-GROUNDWATER-SOIL-MICROBIOLOGY@1` | Both endpoints concern subsurface systems but do not state a groundwater-to-soil-microbiology link. | Select an existing Claim about groundwater–microbe interaction, contaminant transport, recharge ecology, or another explicitly sourced mechanism; otherwise remove. | Exact mechanism in the selected Claims and sources; no inferred hydrobiological effect. |
| `REL-CROSS-FOOD-PUBLIC-HEALTH@1` | Household food security Claim D is paired with a generic public-health definition. | Replace the public-health endpoint with an existing nutrition, foodborne-disease, population nutrition, or health-determinant Claim that directly connects to food security; otherwise narrow to a generic topic index or remove. | Exact endpoint statement and source locator; no causal or population-health claim beyond evidence. |
| `REL-CROSS-M2-STATISTICS-RESEARCH@1` | Statistics Claim C concerns experimental design/data analysis, while Research Methods Claim B concerns reproducibility/repeatability. | Select a research-design or experimental-methods Claim that directly matches the statistical design link, or narrow the Relation to reproducibility only if the statistics endpoint states that concept. | Direct overlap in both statements; exact versions and source locators. |
| `REL-CROSS-MIGRATION-LABOR-ECONOMICS@2` | Migration Claim C measures flows/stocks; Labor Economics Claim C lists labor-market indicators but does not connect them to migration. | Select a migration/labor-market interaction Claim, or narrow the Relation to a documented comparison of migration and labor indicators if both sources support that comparison. | Explicit migration/labor connection; exact locators; no unsupported causal effect on wages/employment. |
| `REL-CROSS-PLANTPATH-ENTOMOLOGY@1` | Both Claims define disciplines; neither states pests, vectors, transmission, or plant–insect interaction. | Select an existing plant-pest, insect-vector, or crop-damage Claim; otherwise remove the Relation. | Specific plant/insect interaction stated by source; avoid treating disciplinary adjacency as a relation. |
| `REL-CROSS-QUANTUM-MEASUREMENT@1` | Quantum Claim A is broad; metrology Claim B is generic and does not address quantum measurement. | Select a Claim about quantum observables, measurement disturbance, quantum uncertainty, or a directly relevant measurement model; otherwise narrow or remove. | Quantum-specific proposition and exact evidence locator; no implied quantum measurement theory from generic metrology. |
| `REL-CROSS-RESEARCH-STATISTICS@1` | Research Methods Claim B concerns reproducibility; Statistical Inference Claim A concerns inference from samples. | Select a research Claim about sampling, inference, statistical analysis, or study design; alternatively narrow the Relation to reproducibility only if the statistics endpoint supports it. | Exact methodological overlap; no equivalence between reproducibility and statistical inference. |
| `REL-CROSS-SETTLEMENT-PUBLIC-HEALTH@1` | Settlement planning Claim C is broad; Public Health Claim A is a generic definition and no concrete mechanism is identified. | Select a settlement-health services, water/sanitation, housing-health, environmental health, or health-determinants Claim; otherwise narrow to a broad policy-domain index or remove. | Exact health-related settlement component; no inferred health outcome or service availability. |
| `REL-CROSS-EARTHQUAKE-AFTERSHOCK@1` | Event record does not identify a definite occurrence; its Context and Scope target a protective-action Claim, not the Event. | If the intent is generic guidance, remove the Event instance and represent the general warning as a Claim/knowledge relation. If an actual occurrence is intended, provide an identified report/observation and occurrence attribution. | Conform to Standard 009 E-01/E-03; resolve Event Context/Scope target applicability; do not invent time/location. |
| `REL-CONTAINER-WATER-STORAGE@1` | Both State participants describe the same container subject; the second is not a water State, despite the role label. Context targets the Claim. | Either add an authorized, source-supported water Object/State and model container-for-water, redefine the Relation to accurately connect two container State representations, or remove the redundant Relation. | Exact subject identity, role/type match, temporal basis if a transition is intended, Context target compatibility. |
| `REL_M3_EMERGENCY_INFRASTRUCTURE@1` | Infrastructure Resilience Claim A states community resilience generally, not infrastructure-specific resilience. | Replace with an existing infrastructure-resilience Claim, or narrow the Relation to emergency management/community resilience if that is the exact supported link. | Endpoint text must explicitly cover infrastructure if the Relation retains that scope; no inference from slice name or Claim ID. |

## Aggregate disposition

| HOLD category | Relations | Closure route |
|---|---:|---|
| Endpoint specificity / semantic mismatch | 11 | Replace endpoint with a direct, existing, evidence-backed Claim or narrow the Relation |
| Redundancy / duplicate content | 1 | Demonstrate distinct endpoint contribution or remove duplicate Relation |
| Event / State / Context modeling | 2 | Correct the represented semantic object and target applicability under bounded authorization |
| Infrastructure-specific endpoint mismatch | 1 | Use infrastructure-specific Claim or narrow the Relation |
| **Total** | **15** | **All remain HOLD until independently re-reviewed** |

## Execution order

1. First resolve model-level items: earthquake Event and container/water State Relation.
2. Then resolve endpoint-specific mismatches using existing Claims only; do not create new Claims without authorization.
3. Handle the CO emergency duplication by an editorial comparison, not by adding more text.
4. Re-fetch every selected Relation and participant at the exact current PR head.
5. Re-run pair semantics, exact-version checks, provenance identity, applicable-frame/Context target validation, and affected slice tests.
6. Keep all 15 Relations HOLD until the revised pair is reviewed and the independent endpoint/evidence/rights/editorial gates are complete.

## Change boundary

This register is an audit/remediation aid only. No Relation, Claim, Source, Evidence Use, Context, Scope, allowlist, or publication state was changed. No item was promoted to INCLUDE. All proposed canonical edits require the applicable bounded authorization.
