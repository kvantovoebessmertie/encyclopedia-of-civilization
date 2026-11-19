# First Edition — Part II Claim Dependency Closure Batch 9

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `846cefd71ae320f0aa8d39b93507ac78f2d591bf`  
PR head at reconciliation: `c209b90fbe542eeff08f46e6598ac1666b8dbaaa` (the two intervening commits changed only the Batch 8 report and master register; canonical JSON was unchanged)  
Status: **27/27 CLAIM → EVIDENCE USE → SOURCE CHAINS ID/VERSION/TYPE MATCH; 22/27 EUS HAVE CLAIM-SPECIFIC LOCATORS; ALL HOLD**

## 1. Scope

This batch closes the remaining 27 Claim rows still marked current-head identity-only in the master at the inspection HEAD. It covers ten slices:

- cartography-basics (3 Claims)
- food-systems-basics (4)
- history-of-engineering-basics (3)
- history-of-mathematics-basics (3)
- history-of-medicine-basics (3)
- hydraulic-engineering-basics (3)
- library-science-basics (3)
- settlement-geography-basics (3)
- antimicrobial-resistance-basics (1)
- statistics-basics (1)

Each Claim, exact Evidence Use record and referenced Source was fetched from canonical JSON. Context and Scope were additionally fetched and target-checked for seven slices: cartography, food systems, history of engineering, history of medicine, hydraulic engineering, library science and settlement geography.

No canonical JSON was changed. No decision was promoted. All 27 Claims remain HOLD.

## 2. Exact graph results

| Check | Result |
|---|---:|
| Claims fetched and parsed | 27/27 |
| Evidence Use records fetched and parsed | 27/27 |
| Source records fetched and parsed | 15/15 |
| Claim ID/version/type matches | 27/27 |
| Evidence Use `claim_ref` exact match | 27/27 |
| Evidence Use `source_ref` exact match | 27/27 |
| Claim provenance Source identity matches the Evidence Use Source target | 27/27 |
| Evidence Use records with claim-specific locator | 22/27 |
| Evidence Use records without claim-specific locator | 5/27 |
| Sources with explicit external locator metadata | 12/15 |
| Sources without explicit external locator metadata | 3/15 |
| Context/Scope records fetched and target-checked | 14/14 across 7 slices |
| Previously absent exact-version dependencies discovered | 2 |

The two previously absent Evidence Use dependencies are added once to the master register:

- `EU-ANTIMICROBIAL_RESISTANCE_BASICS-C@1`
- `EU-STATISTICS_BASICS-C@1`

Both were fetched from canonical JSON and have exact version-1 Claim and Source references.

## 3. Slice-level findings

| Slice | Graph | Locator status | Source / scope finding | Decision |
|---|---|---|---|---|
| cartography-basics | 3/3 exact | 3/3 pinpointed | USGS Mapping 101 and Fact Sheet 035-01 support the bounded propositions. Context/Scope limit USGS conventions to the U.S. example and note projection trade-offs. | HOLD |
| food-systems-basics | 4/4 exact | 4/4 pinpointed | FAO FAQ supports terminology and system-interaction claims; World Bank supports off-farm value-chain functions. Context distinguishes agrifood from food systems; Scope excludes current market, food-safety and operational advice. | HOLD |
| history-of-engineering-basics | 3/3 exact | 3/3 pinpointed | Smithsonian stories and collections support descriptive claims only. Context/Scope state that this curated selection is not a complete or globally representative history. | HOLD |
| history-of-mathematics-basics | 3/3 exact | 3/3 pinpointed | MacTutor is limited to notation/communication and historical context; Oxford supplies regional examples with interpretive cautions; Cambridge supplies a narrow calculus-history chapter. No linear or cultural-ranking narrative is inferred. | HOLD |
| history-of-medicine-basics | 3/3 exact | 3/3 pinpointed | NLM Collection Development Guidelines support the subject definition, historical contextualization and use of interpretive/analytical/biographical secondary literature. Context/Scope explicitly exclude clinical advice. | HOLD |
| hydraulic-engineering-basics | 3/3 exact | 3/3 pinpointed | HEC-HMS and HEC-RAS are separated by hydrologic versus hydraulic model role. Context/Scope exclude design calculations, site-specific advice, forecasting and facility operation. | HOLD |
| library-science-basics | 3/3 exact | 3/3 pinpointed | IFLA-UNESCO Public Library Manifesto 2022 supports the claims. Context treats it as normative guidance, not empirical proof; Scope is limited to public libraries. | HOLD |
| settlement-geography-basics | 3/3 exact | 0/3 pinpointed | UN-Habitat manual is identified, but no EU has a locator and the Source has no locator metadata. Add exact manual sections/pages and preserve the distinction from national legal definitions. | HOLD |
| antimicrobial-resistance-basics | 1/1 exact | 0/1 pinpointed | WHO fact sheet is identified but the EU and Source contain no pinpoint. Add the exact One Health / multisectoral passage before judging evidence sufficiency. | HOLD |
| statistics-basics | 1/1 exact | 0/1 pinpointed | NIST/SEMATECH handbook is identified but the EU and Source contain no pinpoint. Locate the experimental-design / study-planning passage and assess direct support. | HOLD |

## 4. Master-register reconciliation

- 27 Claim rows and 27 Evidence Use rows were fetched and matched.
- 15 Source rows and 14 Context/Scope rows were fetched and matched.
- 80 existing rows advanced from `canonical_json_verified_current_head_hold` to `canonical_json_dependency_verified_hold`.
- `SRC-STATISTICS_BASICS@1` was already dependency-verified and retained its status.
- Two missing Evidence Use rows were added exactly once.
- The dependency-record count therefore increases from 55 to 57, and the master total from 1,113 to 1,115 exact-version rows.
- All decisions remain HOLD; no ID or canonical JSON was changed.

## 5. Remaining blockers

1. Add direct locators to the five unpinned EUs in settlement geography, antimicrobial resistance and statistics; add external locator metadata to their three Source records.
2. Complete source-specific rights/attribution review for every candidate source. Public access and factual paraphrase do not by themselves establish redistribution permission.
3. Finish exact Context/Scope target coverage for the wider master; this batch checked 14 records across seven of its ten slices.
4. Continue the separate 97 non-candidate Relation endpoint version/type and semantic review; this batch does not close that Relation workstream.
5. Complete Human View, high-consequence review, project-owner decisions and final exact-head CI before any allowlist or release.

## 6. Decision

- 27/27 Claim → Evidence Use → Source identity/version/type chains: **MATCH**.
- 22/27 Evidence Use records have claim-specific locators; five do not.
- All 27 Claims remain **HOLD**.
- No INCLUDE/EXCLUDE decision, canonical content change, public allowlist or publication authorization was made.
