# M13 — unassessed-risk content screen package 07

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue source revision: `f26820e59b08b4036ad78302dad8118c51dac540`  
Input artifact: workflow run `43496934373`, artifact `14071268296`  
Scope: 20 additional exact Claim v1 records from the 711-row UNASSESSED risk-metadata queue.  
State: **content-level risk routing only; no canonical Claim/Evidence Use/Source JSON, risk metadata, or D/E/B scores changed.**

## 1. Selection and non-duplication controls

The 711-row CSV was inspected directly. This package selects the next 20 queue rows after excluding:
- 216 exact Claim IDs already explicitly enumerated in the prior M13 Batch 53/54 and 14 November Packages 01–06 risk-screen reports;
- the complete disaster-response, disaster-risk-reduction, hydropower, industrial-safety, public-health-surveillance, safety-engineering and infrastructure-resilience slice families, conservatively held out because the preliminary 17-Claim report describes 14 inspected Claims without naming their IDs.

The 14 unnamed historical observations remain unreconciled. They are not guessed, substituted, or counted as exact IDs. The package therefore avoids reopening those topic families until their original selection can be reconstructed.

The 20 selected Claim IDs are unique, are present in the exact 711-row CSV, and do not overlap the 216 explicitly identified prior risk-screen IDs. They are:
- Behavioral economics: `CLM-BEHAVIORAL_ECONOMICS_BASICS-B@1`, `CLM-BEHAVIORAL_ECONOMICS_BASICS-C@1`
- Biodiversity: `CLM-BIODIVERSITY_BASICS-A@1`, `CLM-BIODIVERSITY_BASICS-B@1`, `CLM-BIODIVERSITY_BASICS-C@1`
- Building envelope: `CLM-BUILDING_ENVELOPE_BASICS-A@1`, `CLM-BUILDING_ENVELOPE_BASICS-B@1`, `CLM-BUILDING_ENVELOPE_BASICS-C@1`
- Building services engineering: `CLM-BUILDING_SERVICES_ENGINEERING_BASICS-C@1`
- Calculus: `CLM-CALCULUS_BASICS-A@1`, `CLM-CALCULUS_BASICS-B@1`, `CLM-CALCULUS_BASICS-C@1`
- Calibration: `CLM-CALIBRATION_BASICS-B@1`, `CLM-CALIBRATION_BASICS-C@1`
- Cartography: `CLM-CARTOGRAPHY-A@1`, `CLM-CARTOGRAPHY-B@1`, `CLM-CARTOGRAPHY-C@1`
- Causal inference: `CLM-CAUSAL_INFERENCE_BASICS-B@1`, `CLM-CAUSAL_INFERENCE_BASICS-C@1`
- Chronology methods: `CLM-CHRONOLOGY_METHODS-A@1`

## 2. Method and boundary

For every selected Claim, the exact v1 Claim statement, linked v1 Evidence Use record and linked v1 Source identity/URI were inspected on the M13 branch. Prior M13 source-passage and score reports were checked where they exist and are reused below; their work is not repeated or counted as new passage review.

This screen determines review routing only. It does not assign likelihood, severity, exposure, risk-domain metadata, final risk class, D/E/B scores, specialist approval, Human View, or publication clearance. A low-direct-consequence route is not a declaration that a Claim is universally safe or fully evidenced.

## 3. Risk routing

### HIGH CONSEQUENCE — 4 Claims

| Claim | Evidence chain | Finding and required route |
|---|---|---|
| `CLM-BUILDING_ENVELOPE_BASICS-A@1` | `EU-BUILDING_ENVELOPE_BASICS-A@1` → `SRC-BUILDING_ENVELOPE_BASICS@1` | Building-envelope performance affects heat/moisture exchange and occupied-building conditions. Route to building-science / building-physics review before design, retrofit, moisture-control or health recommendations are derived. The Claim is foundational, not a design instruction. |
| `CLM-BUILDING_ENVELOPE_BASICS-B@1` | `EU-BUILDING_ENVELOPE_BASICS-B@1` → same Source | Air and moisture movement can affect durability and indoor conditions. Route to building-envelope / moisture-control specialist review; do not infer a universal ventilation, condensation or remediation prescription. |
| `CLM-BUILDING_ENVELOPE_BASICS-C@1` | `EU-BUILDING_ENVELOPE_BASICS-C@1` → same Source | Climate, materials, junctions and workmanship affect envelope behaviour. Route to building-science / construction-quality review before component selection or retrofit use. Site-specific calculations and applicable codes remain necessary. |
| `CLM-BUILDING_SERVICES_ENGINEERING_BASICS-C@1` | `EU-BUILDING_SERVICES_ENGINEERING_BASICS-C@1` → `SRC-BUILDING_SERVICES_ENGINEERING_BASICS@1` | The Claim correctly says building systems must be coordinated with architecture and operation and that design requires calculations, standards and coordination. Route to qualified building-services engineering review; do not derive system sizing, safety limits or code compliance from this overview. |

### ELEVATED — 2 Claims

| Claim | Evidence chain | Finding and required route |
|---|---|---|
| `CLM-CALIBRATION_BASICS-B@1` | `EU-CALIBRATION_BASICS-B@1` → `SRC-CALIBRATION_BASICS@1` | Calibration and metrological traceability support measurement confidence and documented quality systems. Route to metrology / calibration specialist review before use in safety-critical, clinical, regulatory or industrial decisions. A calibration certificate alone does not establish fitness for every intended use. |
| `CLM-CALIBRATION_BASICS-C@1` | `EU-CALIBRATION_BASICS-C@1` → same Source | The Claim appropriately states that calibration does not make an instrument suitable for every task. Route to metrology review; suitability depends on required uncertainty, range, conditions, method and decision tolerance. |

### MODERATE — 10 Claims

| Claim | Evidence chain | Finding and required route |
|---|---|---|
| `CLM-BEHAVIORAL_ECONOMICS_BASICS-B@1` | `EU-BEHAVIORAL_ECONOMICS_BASICS-B@1` → `SRC-BEHAVIORAL_ECONOMICS_BASICS@1` | Prospect theory is a model of decisions under uncertainty. Route to behavioural-economics review; do not present one theory or one Nobel-recognized contribution as a complete account of decision-making. |
| `CLM-BEHAVIORAL_ECONOMICS_BASICS-C@1` | `EU-BEHAVIORAL_ECONOMICS_BASICS-C@1` → same Source | The Claim compares observed decisions with standard economic-model predictions. Route to behavioural-economics review; preserve the distinction between empirical regularities, model assumptions and universal predictions. |
| `CLM-BIODIVERSITY_BASICS-A@1` | `EU-BIODIVERSITY_BASICS-A@1` → `SRC-BIODIVERSITY_BASICS@1` | Species, genetic and ecosystem diversity are foundational ecological concepts. Route to ecology / conservation-methods review before policy, monitoring or conservation-priority recommendations. |
| `CLM-BIODIVERSITY_BASICS-B@1` | `EU-BIODIVERSITY_BASICS-B@1` → same Source | Species richness changes through speciation and extinction. Route to biodiversity / evolutionary ecology review; do not reduce biodiversity trends to these two processes alone where abundance, distribution, sampling and time scale matter. |
| `CLM-BIODIVERSITY_BASICS-C@1` | `EU-BIODIVERSITY_BASICS-C@1` → same Source | Assessment depends on spatial scale, time and observation method. Route to ecological monitoring / assessment review; preserve the measurement-method and sampling boundary. |
| `CLM-CARTOGRAPHY-A@1` | `EU-CARTOGRAPHY-A@1` → `SRC-CARTOGRAPHY@1` | Mapping represents spatial information and can support land, navigation and infrastructure decisions. Route to cartography / geospatial review before operational mapping or boundary use. |
| `CLM-CARTOGRAPHY-B@1` | `EU-CARTOGRAPHY-B@1` → same Source | Topographic symbols and contour lines communicate mapped features and relief. Route to cartography review; retain product- and map-series-specific symbol conventions rather than treating every map legend as interchangeable. |
| `CLM-CARTOGRAPHY-C@1` | `EU-CARTOGRAPHY-C@1` → same Source | Map scale relates map distance to ground distance. Route to cartography / surveying review if used for measurement, engineering or legal-boundary decisions; projection, scale variation and datum remain relevant. |
| `CLM-CAUSAL_INFERENCE_BASICS-B@1` | `EU-CAUSAL_INFERENCE_BASICS-B@1` → `SRC-CAUSAL_INFERENCE_BASICS@1` | The Claim correctly states that association alone does not establish a causal effect and that confounding can create non-causal associations. Route to causal-inference / epidemiology methods review before health, policy or programme evaluation use. |
| `CLM-CAUSAL_INFERENCE_BASICS-C@1` | `EU-CAUSAL_INFERENCE_BASICS-C@1` → same Source | Causal diagrams and counterfactual definitions help represent interventions, outcomes and potential confounding. Route to causal-inference review; do not imply that a diagram or counterfactual definition alone identifies a causal effect without assumptions and a valid design. |

### LOW DIRECT CONSEQUENCE — 4 Claims

| Claim | Evidence chain | Finding and required route |
|---|---|---|
| `CLM-CALCULUS_BASICS-A@1` | `EU-CALCULUS_BASICS-A@1` → `SRC-CALCULUS_BASICS@1` | Basic definition of a limit. Foundational mathematics; no direct operational hazard in the statement. Preserve the mathematical conditions and rights restrictions on the linked textbook source. |
| `CLM-CALCULUS_BASICS-B@1` | `EU-CALCULUS_BASICS-B@1` → same Source | Basic definition of a derivative as an instantaneous rate of change where the required conditions hold. Keep the existence conditions explicit. |
| `CLM-CALCULUS_BASICS-C@1` | `EU-CALCULUS_BASICS-C@1` → same Source | Definite integral as accumulated quantity under suitable conditions. Keep integrability and interpretation conditions explicit. |
| `CLM-CHRONOLOGY_METHODS-A@1` | `EU-CHRONOLOGY_METHODS-A@1` → `SRC-CHRONOLOGY_METHODS@1` | Chronology orders events and evidence in time and supports comparison of change. Foundational historical method; preserve the distinction between temporal order and causal explanation. |

## 4. Reuse of prior source-passage and score work — no duplicate research

The following existing reports were inspected and are reused as prior work, not re-counted as new source-passage reviews:

- Building envelope A/B/C and building services engineering: `M13-CLAIM-REVIEW-BATCH-39-BUILT-ENVIRONMENT-AND-CALIBRATION-2026-10-10.md`; `M13-NIST-IT-NASA-SYSTEMS-ENGINEERING-NIST-BUILDING-SCIENCE-ADJUDICATION-2026-11-13.md`. The NIST Building Science URI in the current Source record is reported as unavailable/404. NIST TN 1869 and a separate infiltration/ventilation publication are candidate sources, not yet canonical replacements. No Source/EU/Claim record has been changed.
- Calibration B/C: the same Batch 39 report reviewed the three calibration Claims and NIST Calibration Services source. The current Evidence Use descriptions remain generic and do not contain reproducible Claim-specific locators.
- Calculus A/B/C: `M13-CLAIM-AUDIT-BATCH-41-SCORED-BLOCK-06-BIOCHEMISTRY-BIODIVERSITY-BIOINFO-BIOMED-CALCULUS-CARTOGRAPHY-CIVIL-SOCIETY-2026-10-11.md` and `M13-CALCULUS-BASICS-OPENSTAX-SOURCE-PASSAGE-AND-RIGHTS-REASSESSMENT-2026-11-13.md`. The review found direct mathematical passage support, but canonical EU locators remain absent and the OpenStax rights restriction for AI ingestion remains unresolved. No written permission or canonical locator correction is recorded.
- Cartography A/B/C: the Batch 41 scored block and `M13-CARTOGRAPHY-BASICS-SOURCE-PASSAGE-REASSESSMENT-2026-11-13.md`. Passage support was found, but exact canonical locators and additional sources for map symbols/scale remain pending. No canonical correction was made.
- Causal inference B/C and chronology A: `M13-CLAIM-REVIEW-BATCH-40-CAUSAL-BIOLOGY-CHEMISTRY-AND-CHRONOLOGY-2026-10-10.md`. Existing score/source review work is reused; this package adds only risk routing.
- Biodiversity A/B/C: the Batch 41 scored block and `M13-OPENSTAX-BIOLOGY-CELLS-BEHAVIOR-ECOLOGY-BIODIVERSITY-ADJUDICATION-2026-11-13.md`. A/B were assessed as directly supported; C needs a more direct monitoring/measurement source. OpenStax rights and exact canonical locator issues remain open.
- Behavioral economics B/C: current local links point to the Nobel Prize 2002 Daniel Kahneman / Prospect Theory press-release page, while both Evidence Use descriptions remain generic. These Claims remain in the strict 47-item source-review filename-gap routing list; no passage-level clearance is inferred here.

## 5. Updated routing ledger and integrity

- Additional Claims screened in this package: **20**.
- Risk routing: high consequence 4; elevated 2; moderate 10; low direct consequence 4.
- Explicitly enumerated prior unique risk-screen IDs in the 711-row queue: 216.
- Explicitly enumerated unique risk-screen IDs after this package: **236/711**.
- Fourteen historical observations from the preliminary screen remain unnamed and are not included in the 236 exact-ID count; they may overlap this set.
- **475** queue IDs are not explicitly named in the enumerated risk-screen ledger after this package. Because the 14 unnamed historical observations may overlap the 236 explicit IDs or may be additional distinct queue IDs, the exact number of remaining unique Claims is currently bounded between **461 and 475**; do not publish a single definitive remainder until those 14 IDs are recovered.
- Risk metadata assigned or changed: 0.
- D/E/B scores assigned or overwritten: 0.
- Canonical Claim/Evidence Use/Source records changed: 0.
- Independent specialist adjudications: 0.
- Human View / publication approval: 0.

This package is a content-level routing screen, not a complete risk assessment, source certification, evidence locator correction, release approval or M13 closure.
