# First Edition — Climate Basics and Measurement Uncertainty: Combined 20-Record Audit and Source Refresh

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Inspection HEAD: `abcc8c9823a6c4ebeb9de0c15d2234a24c5caa59`  
Status: BOUNDED RECORD / SOURCE / RIGHTS REVIEW — NO CANONICAL WRITES

## 1. Scope and method

This package re-fetched all 20 canonical records in the Climate Basics (9 records) and Measurement Uncertainty Basics (11 records) slices at the inspection HEAD. It checked exact record versions, Claim→Evidence Use→Source relationships, Context/Scope targets, claim semantics, official source pinpoints, currentness and publication-rights notices.

This is not a complete scientific peer review, legal opinion, full corpus graph audit, release approval, or permission to edit canonical records. No canonical JSON, status, candidate register, selection allowlist or release manifest was changed. All six Claims remain HOLD.

## 2. Climate Basics — nine-record slice

### 2.1 Exact record identities

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-CLIMATE_BASICS-A | 1 | Claim | `83e86389e2c7e122ddce0b1e9d066c15147c9cec` |
| CLM-CLIMATE_BASICS-B | 1 | Claim | `f4788544fbf941acca40ca887a16e7fd06313094` |
| CLM-CLIMATE_BASICS-C | 1 | Claim | `f93a363b1130194df4235dc7e43690b49d0ee458` |
| EU-CLIMATE_BASICS-A | 1 | Evidence Use | `7356d5b6c7c2c49f0fa119f60726135229d9033e` |
| EU-CLIMATE_BASICS-B | 1 | Evidence Use | `565862828b9ae0c183e6c1a0d53be51419f2b7c6` |
| EU-CLIMATE_BASICS-C | 1 | Evidence Use | `ac2ce380542c9cd59e74db4dace7fd84b60df26c` |
| SRC-CLIMATE_BASICS | 1 | Source | `a5bee4f54821f6e4163d917a9a85d9848118f065` |
| CTX-CLIMATE_BASICS | 1 | Context | `224e05a1b35b3bfc94545069685076b93e69fb2a` |
| SCP-CLIMATE_BASICS | 1 | Scope | `11e44bf4c54c433c5083a198bc213231e8e644a9` |

### 2.2 Claim-level findings

**Claim A — climate as long-term characteristics and changes in weather conditions**

Canonical wording: «Климат описывает долгосрочные характеристики и изменения погодных условий в системе Земли.»

- NASA's current “What's the difference between weather and climate?” explains climate as long-term averages, commonly weather averaged over several decades.
- NOAA's explainer independently defines climate as longer-term average weather patterns, generally 30 years or more, and notes that climate variables include temperature, precipitation, humidity and wind.
- The phrase “в системе Земли” is broader than the narrow weather-average definition. NOAA's climate monitoring overview adds that atmospheric conditions are influenced by ocean, land, sun and atmospheric chemistry. If the Claim retains “Earth system”, the EU should point to an Earth-system source rather than only a weather/climate definition.
- Existing EU-A points only to NASA's broad Climate Change portal, not the exact explanatory page.

**Finding:** core concept well supported; exact locator and “Earth system” breadth need editorial/source alignment.

**Claim B — observations, measurements and models over long time scales**

Canonical wording: «Климатические выводы опираются на наблюдения, измерения и модели, рассматриваемые на длительных временных масштабах.»

- NOAA's Climate Data Resources page identifies historical observations and predictive models as distinct climate resources; its climate monitoring material describes observing and measuring climate variables.
- NASA's “What Is Climate Change?” describes climate data records and indicators based on land/ocean temperature, sea level, ice, extreme weather and precipitation.
- The current canonical EU-B points to the general NASA Climate Change portal and does not pin these components.
- “модели” and “длительные временные масштабы” should not be collapsed into a single assertion: observational climatologies and future projections are different evidence products. A future EU should state whether it supports observations, modeled projections, or both, and should not imply that all climate conclusions are model outputs.

**Finding:** supported in broad outline, but the claim bundles distinct evidence modes and needs more exact wording/locator.

**Claim C — individual weather event does not describe the whole climate**

Canonical wording: «Климат и отдельная погода относятся к разным временным масштабам, поэтому единичное погодное событие само по себе не описывает весь климат.»

- NASA and NOAA both distinguish short-term weather from long-term climate averages.
- NOAA explains climate normals are calculated from long-term observations, commonly 30-year periods.
- This is a strong, well-bounded introductory proposition. It does not mean a single event is irrelevant to climate attribution or that extreme events cannot be studied in a climate context; it means one isolated event alone is not a sufficient description of the climate.

**Finding:** direct support available; EU-C needs exact locator and an explicit limit against the stronger inference that individual events cannot be climate-related.

### 2.3 Source and rights strategy

Current Source v1 is a broad NASA Climate Change portal. Better exact source candidates for a future versioned Source/EU package:

1. NASA, “What’s the difference between weather and climate?” — direct weather/climate timescale explanation.
2. NOAA, “What’s the difference between climate and weather?” — independent government explanation and 30-year norm framing.
3. NOAA, “Climate data monitoring” — observations and monitoring.
4. NOAA, “Climate data resources” — historical data and predictive models.

NASA/NOAA pages are public information portals, but individual images, visualizations, third-party credits and other marked assets may carry separate terms. This package proposes no image, graphic, table or copied prose reuse. Any publication should use original factual paraphrase, link to the exact source and retain attribution; item-specific terms still require a check. Do not infer that every linked asset is unrestricted merely because the agency page is public.

### 2.4 Context, Scope and disposition

CTX-CLIMATE_BASICS and SCP-CLIMATE_BASICS both target Claim A v1 only. They must not be displayed as though they automatically govern B and C. The slice is a 3×(Claim→EU) graph to one Source, with Context/Scope only on A.

**Disposition: all three Claims HOLD.** The main remediation is versioned EU pinpointing and claim/source alignment, not wholesale rewriting. No canonical edits are authorized.

## 3. Measurement Uncertainty Basics — eleven-record slice

### 3.1 Exact record identities

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| CLM-MEASUREMENT_UNCERTAINTY_BASICS-A | 1 | Claim | `c352d4f41e7a0f96163cc81e9f3e8a30fed273e0c5` |
| CLM-MEASUREMENT_UNCERTAINTY_BASICS-B | 1 | Claim | `580c2f72052c78f72cd663b5938162618af8e120` |
| CLM-MEASUREMENT_UNCERTAINTY_BASICS-C | 1 | Claim | `140664cc6c983eb7ff0f2b21c0d7456c0836f1b8` |
| EU-MEASUREMENT_UNCERTAINTY_BASICS-A | 1 | Evidence Use | `34d962fe7a0f96163cc81e9f3e8a30fed273e0c5` |
| EU-MEASUREMENT_UNCERTAINTY_BASICS-B | 1 | Evidence Use | `485a56b870095de148ed6b02866d780916694007` |
| EU-MEASUREMENT_UNCERTAINTY_BASICS-C | 1 | Evidence Use | `df75bec968abef21569aba8784d56163f0041a44` |
| EU-MEASUREMENT_UNCERTAINTY_BIPM | 1 | Evidence Use | `d47895b8c3b675724ed26ba1eb6c84ecc0f0e81a` |
| SRC-MEASUREMENT_UNCERTAINTY_BASICS | 1 | Source | `f167d0df955e8ec99a26f64fca9a5a4df49164fd` |
| SRC-BIPM-VIM-MEASUREMENT-UNCERTAINTY | 1 | Source | `6f5b0a4c221942134f2d7dfeb1e5ed169d26c7e1` |
| CTX-MEASUREMENT_UNCERTAINTY_BASICS | 1 | Context | `fdfefe7f5632413306291f947e4ff72049fa1bcd` |
| SCP-MEASUREMENT_UNCERTAINTY_BASICS | 1 | Scope | `9a38ab3081c7b124a488be68f3d8750b38166806` |

### 3.2 Claim-level findings

**Claim A — result must be interpreted with its uncertainty**

Canonical wording: «Результат измерения должен интерпретироваться вместе с оценкой его неопределённости.»

- NIST TN 1297 §2.1 states that a measurement result is complete only when accompanied by a quantitative statement of its uncertainty.
- VIM 2.9 says a measurement result is generally expressed as a measured quantity value and a measurement uncertainty; it allows a single value where uncertainty is negligible for the purpose.
- This makes the canonical “должен” potentially too absolute. A more source-faithful formulation would preserve the “generally / for the intended purpose” qualification rather than assert an unconditional rule for every measurement context.
- Existing EU-A is generic and has no §2.1 or VIM 2.9 locator.

**Finding:** strong support, but absolute wording needs qualification and a pinpointed EU.

**Claim B — uncertainty is dispersion, not automatically error**

Canonical wording: «Неопределённость характеризует разброс значений, обоснованно приписываемых измеряемой величине, и не равна автоматически ошибке.»

- VIM 2.26 defines measurement uncertainty as a non-negative parameter characterizing dispersion of quantity values attributed to a measurand based on the information used.
- VIM 2.16 separately defines measurement error as a measured quantity value minus a reference quantity value.
- NIST TN 1297 §2.3 explicitly warns against confusing uncertainty with error and explains why “random/systematic uncertainty” labels can mislead.
- The canonical wording is directionally accurate. “не равна автоматически ошибке” is less precise than saying the concepts are distinct and related in different ways; a future editor should preserve that distinction and avoid implying uncertainty is simply a spread of repeated observations. Type B components may be evaluated from other information, not just a repeated-data distribution.
- The existing BIPM EU corroborates Claim B, but the existing EU is generic and does not cite VIM 2.26 or 2.16.

**Finding:** strongest of the three current claims; pinpoints and careful treatment of Type A/Type B components required.

**Claim C — measurand and measurement model**

Canonical wording: «Оценка неопределённости требует определения измеряемой величины и модели измерения.»

- VIM 2.6 defines a measurement procedure as based on a measurement model and including calculations to obtain a result.
- VIM 2.3 defines the measurand; VIM 2.1 notes that measurement presupposes a description of the quantity commensurate with intended use, a procedure and a calibrated measuring system.
- JCGM GUM-6:2020 is specifically about developing and using measurement models; JCGM GUM-1:2023 explains the rationale for evaluating, expressing and using uncertainty.
- The current claim is plausible but “requires” is too compressed: the measurand must be specified sufficiently for the intended purpose, and the model represents the measurement process. The model need not be treated as a single universal formula.
- Existing EU-C has no locator; the BIPM EU is attached only to Claim B.

**Finding:** relevant primary terminology exists, but the current Source/EU topology does not actually support C. A dedicated versioned EU/source relation is needed.

### 3.3 Major source-currentness update

The previous candidate notes treated NIST TN 1297 as a legacy source and BIPM GUM 2008 as the main GUM reference. The current BIPM Guides in Metrology page now lists a broader and updated suite:

- JCGM GUM-1:2023 — introductory guide.
- JCGM GUM-6:2020 — developing and using measurement models.
- JCGM 100:2008 and its Amendment 1:2026 — nonlinearity in measurement models.
- JCGM GUM-5:2026 — examples.
- VIM JCGM 200:2012 remains the terminology reference listed.

This materially updates the currentness review: GUM 2008 should not be described as the only current GUM guidance. The 2026 amendment and new 2026 examples must be checked before any technical claim is represented as current.

### 3.4 BIPM/JCGM rights finding

The official GUM-1:2023 document states that copyright is jointly held by JCGM member organizations, and that reproduction, translation and online use of JCGM publications require written permission. The official GUM 2008 page states similar restrictions. Publicly downloadable or browser-readable is not equivalent to permission to reproduce or republish.

The VIM online browser is an abridged, interactive version of JCGM 200:2012 and states its definitions/notes are taken from VIM3 without modification. It is useful for checking terminology, but not a general redistribution licence. This package proposes no reproduction, translation, tables, diagrams or copied paragraphs from JCGM materials.

A public edition could potentially state independently authored, short factual explanations with citations and links, but the project should obtain rights-holder guidance for its intended use, particularly because it uses AI assistance and intends long-term preservation. This is not a legal determination. Rights clearance remains open.

### 3.5 Context, Scope and disposition

CTX-MEASUREMENT_UNCERTAINTY_BASICS and SCP-MEASUREMENT_UNCERTAINTY_BASICS target Claim A v1 only. They do not automatically govern B or C. The two Sources have separate EU relationships: NIST primary EUs for A/B/C and one BIPM EU for B only. No BIPM EU currently supports Claim C.

**Disposition: all three Claims HOLD.** Required remediation: exact locators, a versioned BIPM EU for C if authorized, a qualified Claim A wording review, and explicit rights review. Do not treat open access to JCGM files as redistribution permission.

## 4. Combined conclusions and next steps

Across the two slices, 20 records and six Claims were re-fetched and checked. The work produced a more actionable source map but no publication-ready selection.

1. Climate: version EU-A/B/C with exact NASA/NOAA locators; clarify the Earth-system phrase in A and separate observational data from model projections in B.
2. Metrology: pin NIST TN 1297 §2.1, §2.3 and relevant model sections; pin VIM 2.26, 2.16, 2.9 and 2.6 as applicable; do not conflate uncertainty with error or Type A with all uncertainty.
3. Metrology: inspect JCGM GUM-1:2023, GUM-6:2020 and the 2026 amendment/examples before treating the 2008 GUM as current complete guidance.
4. For both domains, preserve exact record versions and target-specific Context/Scope; use new versioned EU records rather than silently modifying v1.
5. Keep rights review separate from factual support. Free access, government hosting, or a public URL is not itself an affirmative licence for every asset or reproduction.
6. No Claim is eligible for INCLUDE on the basis of this package alone.

**Final disposition: 20 records inspected; 6 Claims remain HOLD; zero canonical writes; zero INCLUDE decisions.**
