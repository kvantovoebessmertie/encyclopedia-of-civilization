# First Edition — Part II Claim Dependency Closure Batch 8

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `846cefd71ae320f0aa8d39b93507ac78f2d591bf`  
Status: **15/15 CLAIM → EVIDENCE USE → SOURCE CHAINS ID/VERSION/TYPE MATCH; 0/15 EUS HAVE PINPOINTS; ALL HOLD**

## 1. Scope and result

This batch closes dependency graphs for electromagnetism, fluid mechanics, geometry, governance and historical geography.

| Check | Result |
|---|---:|
| Claims fetched and parsed | 15/15 |
| Evidence Use records fetched and parsed | 15/15 |
| Source records fetched and parsed | 5/5 |
| Claim ID/version/type matches | 15/15 |
| Evidence Use `claim_ref` matches exact Claim | 15/15 |
| Evidence Use `source_ref` matches exact Source | 15/15 |
| Claim provenance source identity matches EU source target | 15/15 |
| Evidence Use records with claim-specific locators | 0/15 |
| Source records with exact pinpoint locator | 0/5 |
| New exact-version dependencies absent from master | 0 |

All exact-version records were already present in the master register. No new dependency keys were discovered.

## 2. Exact chains

| Slice | Claim/version | Evidence Use/version | Source/version | Graph result |
|---|---|---|---|---|
| electromagnetism-basics | `CLM-ELECTROMAGNETISM_BASICS-A@1` | `EU-ELECTROMAGNETISM_BASICS-A@1` | `SRC-ELECTROMAGNETISM_BASICS@1` | MATCH |
| electromagnetism-basics | `CLM-ELECTROMAGNETISM_BASICS-B@1` | `EU-ELECTROMAGNETISM_BASICS-B@1` | `SRC-ELECTROMAGNETISM_BASICS@1` | MATCH |
| electromagnetism-basics | `CLM-ELECTROMAGNETISM_BASICS-C@1` | `EU-ELECTROMAGNETISM_BASICS-C@1` | `SRC-ELECTROMAGNETISM_BASICS@1` | MATCH |
| fluid-mechanics-basics | `CLM-FLUID_MECHANICS_BASICS-A@1` | `EU-FLUID_MECHANICS_BASICS-A@1` | `SRC-FLUID_MECHANICS_BASICS@1` | MATCH |
| fluid-mechanics-basics | `CLM-FLUID_MECHANICS_BASICS-B@1` | `EU-FLUID_MECHANICS_BASICS-B@1` | `SRC-FLUID_MECHANICS_BASICS@1` | MATCH |
| fluid-mechanics-basics | `CLM-FLUID_MECHANICS_BASICS-C@1` | `EU-FLUID_MECHANICS_BASICS-C@1` | `SRC-FLUID_MECHANICS_BASICS@1` | MATCH |
| geometry-basics | `CLM-GEOMETRY_BASICS-A@1` | `EU-GEOMETRY_BASICS-A@1` | `SRC-GEOMETRY_BASICS@1` | MATCH |
| geometry-basics | `CLM-GEOMETRY_BASICS-B@1` | `EU-GEOMETRY_BASICS-B@1` | `SRC-GEOMETRY_BASICS@1` | MATCH |
| geometry-basics | `CLM-GEOMETRY_BASICS-C@1` | `EU-GEOMETRY_BASICS-C@1` | `SRC-GEOMETRY_BASICS@1` | MATCH |
| governance-basics | `CLM-GOVERNANCE_BASICS-A@1` | `EU-GOVERNANCE_BASICS-A@1` | `SRC-GOVERNANCE_BASICS@1` | MATCH |
| governance-basics | `CLM-GOVERNANCE_BASICS-B@1` | `EU-GOVERNANCE_BASICS-B@1` | `SRC-GOVERNANCE_BASICS@1` | MATCH |
| governance-basics | `CLM-GOVERNANCE_BASICS-C@1` | `EU-GOVERNANCE_BASICS-C@1` | `SRC-GOVERNANCE_BASICS@1` | MATCH |
| historical-geography-basics | `CLM-HISTORICAL_GEOGRAPHY-A@1` | `EU-HISTORICAL_GEOGRAPHY-A@1` | `SRC-HISTORICAL_GEOGRAPHY@1` | MATCH |
| historical-geography-basics | `CLM-HISTORICAL_GEOGRAPHY-B@1` | `EU-HISTORICAL_GEOGRAPHY-B@1` | `SRC-HISTORICAL_GEOGRAPHY@1` | MATCH |
| historical-geography-basics | `CLM-HISTORICAL_GEOGRAPHY-C@1` | `EU-HISTORICAL_GEOGRAPHY-C@1` | `SRC-HISTORICAL_GEOGRAPHY@1` | MATCH |

## 3. Substantive findings

- **Electromagnetism:** all three Claims are generic editorial scaffolding (topic introduction, context/source caveat, specialist-verification caveat), not falsifiable electromagnetism propositions. The OpenStax University Physics Vol. 2 §13 introduction is about electromagnetic induction and does not substantiate these meta-statements. Rewrite the Claims into actual subject-matter propositions.
- **Fluid mechanics:** all three Claims are generic scaffolding of the same kind. OpenStax University Physics Vol. 1 §14.5 covers fluid dynamics but does not substantiate the generic slice-introduction and source-context statements. Replace the placeholders with actual fluid-mechanics Claims.
- **Geometry:** the three Claims are substantive (geometric primitives; perimeter versus area; definitions and units). However, the Source identity is a paraphrased definition rather than a publication title, and its URL points to OpenStax Precalculus 2e Chapter 10 introduction, not a suitable general-geometry source. Replace or supplement the Source and add direct locators.
- **Governance:** the OECD Policy Framework on Sound Public Governance is relevant and authoritative. The three EUs have no pinpoints; cite the exact OECD framework sections for public decision-making, values/enablers/instruments and context variation.
- **Historical geography:** the Library of Congress Maps Collections portal is a useful collection but not a pinpoint source for the three interpretive Claims. Identify the specific historical map(s), metadata/catalog records or an authoritative cartographic guide and add locators.

## 4. Decision

- All 15 Claim → Evidence Use → Source chains match exact canonical ID/version/type.
- No Evidence Use has a claim-specific locator.
- Six Claims (electromagnetism and fluid mechanics) are editorial placeholders and require substantive rewriting.
- Geometry has a source-fit mismatch; governance and historical geography need exact source pinpoints.
- All 15 Claims remain **HOLD**. No canonical JSON changed and no INCLUDE/EXCLUDE or allowlist decision was created.


## Evidence and Claim remediation research closure — 2026-11-19 (research only)

A bounded research dossier now covers all 15 Batch 8 EUs and Claims: `FIRST-EDITION-BATCH8-EVIDENCE-AND-CLAIM-REMEDIATION-RESEARCH-2026-11-19.md`.

- Electromagnetism: direct OpenStax §13.1–13.3 locator candidates; three substantive replacement Claim proposals for Faraday’s law, Lenz’s law and motional EMF.
- Fluid Mechanics: direct OpenStax §14.5–14.7 locator candidates; three substantive replacement Claim proposals for flow/continuity, Bernoulli’s equation and viscosity/flow regimes.
- Geometry: direct OpenStax Contemporary Mathematics §§10.1, 10.2, 10.4 and 10.6; current Source identity/URL is mismatched and Claim C is too abstract.
- Governance: exact OECD framework locators identified; Claim C needs a narrower statement about national conditions and government-specific strengths.
- Historical Geography: LOC “Maps from the World Digital Library — Teacher’s Guide” provides direct passages for maps as primary sources, map content, and date/scale/author/purpose interpretation. Rights remain item-specific.

This closes the **research discovery route for 15/15 locator/Claim issues**, not canonical remediation. Six metadata placeholder Claims have proposed replacements. All 15 Claims remain HOLD; no canonical JSON, version, allowlist or publication state changed. OpenStax non-commercial/share-alike terms and LLM-ingestion restrictions, OECD terms, and LOC classroom-use/copyright conditions remain rights blockers.
