# M13 — Unassessed Risk Content Screen — Package 25

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Queue source revision: `0585e75fc447e46bd340dd367fa5f7f3de1853cd`
Queue workflow run: `43680061942`
Queue artifact: `14148176380` (`m13-review-queue-0585e75fc447e46bd340dd367fa5f7f3de1853cd`)
Artifact SHA-256: `ae59d87366baf8a7c48d9024f01363bba4b4ebe0e4632d975003edbef76ffac4`

## 1. Queue integrity and scope

- 4,834 records scanned; 1,494 Claims inventoried.
- 1,501 scored-report rows reconciled; zero Claims without a scored-report match.
- 1,140 structural finding rows: 1,134 medium and 6 high.
- 132 candidate unassessed-risk Claims remained after exclusions.
- 577 previously screened Claim IDs excluded.
- 17 unreconciled holdout Claims excluded; 15 overlap with reviewed holdouts; 579 unique exclusions.
- 100 Claims selected in five lanes of 20; all 100 IDs unique; zero unfilled slots.
- Lane 1 contains 20 unique Claims and 20 Evidence Use links.
- The queue and evidence packet leave D/E/B scores blank; no score or low-risk status is inferred.
- Machine preparation took 35.617 seconds. Human review time was not measured; no speedup claim is authorized.

## 2. Record-chain verification

The 20 selected Claim records and 20 linked Evidence Use records were inspected at version 1, together with their referenced Source records. The ordinary chains resolve to the expected Claim and Source versions. Evidence Use descriptions remain generic and contain no passage-level pinpoint, so structural resolution is not treated as substantive evidence sufficiency.

### Specific cross-record exception

`CLM_WATER_RESOURCES_BASICS_C@1` has provenance entries for both `SRC-WATER_RESOURCES_BASICS@1` and `SRC_EPA_WATER_RESOURCES@1` (normalized source identity corresponds to the repository's `SRC-EPA-WATER-RESOURCES.json`). However:
- its selected packet contains only `EU-WATER_RESOURCES_BASICS-C` → USGS;
- the separate `EU-WATER_RESOURCES_BASICS-EPA` points to `CLM_WATER_RESOURCES_BASICS_A@1`, not Claim C.

Treat the EPA provenance on Claim C as an unresolved cross-record discrepancy. Do not count the EPA Evidence Use as support for Claim C unless the record owner verifies the intended relationship and applies the authorized versioned correction process.

## 3. Results — 20 Claims

**9 Claims have direct conceptual support in the registered source material or its clearly identified chapter-level material, subject to exact locator capture. 11 remain partial.** The direct-support label is not a D/E/B score and does not close source-rights, locator, Human View or editorial gates.

| Claim ID | Result | Finding and required follow-up |
|---|---|---|
| `CLM_WATER_RESOURCES_BASICS_C` | PARTIAL — LINKAGE HOLD | USGS describes monitoring/assessment of streamflow, groundwater, water quality, water use and availability. The Claim's spatial/temporal interpretation is better supported by USGS “Understanding Water Availability” (`https://www.usgs.gov/mission-areas/water-resources/science/understanding-water-availability`). Resolve the unmatched EPA provenance/EU relationship described above; record precise USGS locator. |
| `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-A` | PARTIAL | The USGS mission-area page covers water quantity-related streams, groundwater, quality, use and availability, but does not fully establish the Claim's distribution and variability dimensions as a management requirement. Candidate: USGS “Understanding Water Availability”; capture spatial/temporal distribution and quantity/quality locator. |
| `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-B` | DIRECT CONCEPTUAL SUPPORT | USGS identifies streamflow and groundwater as monitored/assessed water-resource conditions and exposes water-data tools. Record the exact mission-area and relevant data-portal locators. |
| `CLM-WATER_RESOURCES_MANAGEMENT_BASICS-C` | PARTIAL | The registered USGS overview does not establish the complete decision set of natural conditions, user needs, infrastructure and applicable rules. Add authoritative water-management planning/regulatory material with exact locators. |
| `CLM-WATER_SECURITY-C` | PARTIAL | UN-Water's working definition includes adequate quantity and quality, livelihoods, well-being, socio-economic development, pollution/disaster protection and ecosystems; it also identifies biophysical, infrastructural, institutional, political, social and financial factors. It does not explicitly establish the complete water-cycle clause in the Claim. The registered UN-Water landing page currently returns 403, but the same official Analytical Brief is available as a UN Digital Library PDF: `https://digitallibrary.un.org/record/4068710/files/watersecurity_analyticalbrief.pdf`. Add that PDF as an alternate canonical locator and record “Summary for Decision-Makers,” paragraphs 2–3; retain PARTIAL until the water-cycle wording is supported. |
| `CLM-WEATHER_BASICS-A` | DIRECT CONCEPTUAL SUPPORT | NOAA defines weather as the state of the atmosphere at a given time and geographic location. Record the opening definition locator. |
| `CLM-WEATHER_BASICS-B` | DIRECT CONCEPTUAL SUPPORT | NOAA's weather-observations material identifies temperature, humidity, precipitation, air pressure, wind speed and direction as key atmospheric observations. Record the NOAA observation-page locator; the registered collection page alone is a hub. |
| `CLM-WEATHER_BASICS-C` | DIRECT CONCEPTUAL SUPPORT | NOAA states that forecasts estimate conditions expected in the near future and are based on statistical models. Record the forecast sentence locator. |
| `CLM-ZOOLOGY_BASICS-B` | PARTIAL — RIGHTS HOLD | The registered OpenStax Biology 2e chapter discusses animal diversity, body plans and phylogenetic relationships, but the book preface expressly prohibits ingestion into LLMs/generative-AI offerings without prior written permission. Do not use OpenStax content in this AI-assisted workflow absent permission. Replace with a rights-compatible zoology/evolution source. |
| `CLM-ZOOLOGY_BASICS-C` | PARTIAL — RIGHTS HOLD | OpenStax Chapter 27 discusses morphology, developmental pathways and genetic affinities as classification features, but the same AI-use restriction applies. Rights-compatible replacement required before evidence use. Also correct the Source record's `source_identity`: it currently contains a descriptive sentence rather than the actual source title. |
| `CLM-CHRONOLOGY_METHODS-B` | PARTIAL | The registered NPS “About Archeology” page describes reconstructing chronologies but does not distinguish relative from absolute dating. Candidate replacement: NPS “How Do Archeologists Date Sites and Artifacts?” (`https://home.nps.gov/articles/000/how-do-archeologists-date-sites-and-artifacts.htm`), which explicitly defines both classes. Add a specific Source and pinpoint. |
| `CLM-CHRONOLOGY_METHODS-C` | PARTIAL | The registered NPS hub does not establish the method/material/context/quality dependence. The NPS dating article explains that relative dating relies on in-situ context and that absolute dates are often ranges rather than perfectly precise dates. Add the article as a specific Source and capture the relevant caveats. |
| `CLM-COMPILER_BASICS-A` | DIRECT CONCEPTUAL SUPPORT | The LLVM tutorial is a chapter-based learning resource: lexer (Chapter 1), parser/AST (Chapter 2) and code generation to LLVM IR (Chapter 3). Record the exact chapter locators instead of the tutorial index alone. |
| `CLM-COMPILER_BASICS-B` | DIRECT CONCEPTUAL SUPPORT | LLVM Chapter 2 explicitly introduces the AST as a representation of program behavior for later compiler stages. Record the AST definition and construction sections. |
| `CLM-COMPILER_BASICS-C` | PARTIAL | LLVM Chapter 4 covers optimizer support and Chapter 8 object-code compilation, but the registered tutorial does not by itself establish the general correctness-preservation assertion across representations. Add a compiler-correctness/semantics source or narrow the Claim to the documented LLVM pipeline. |
| `CLM-CONFLICT_RESOLUTION_BASICS-A` | DIRECT CONCEPTUAL SUPPORT | Harvard Law School Program on Negotiation defines conflict resolution as formal or informal processes for addressing disagreements and reaching workable solutions; it describes approaches as dependent on complexity, stakes and relationship dynamics. Record the definition and process-selection locators. |
| `CLM-CONFLICT_RESOLUTION_BASICS-B` | DIRECT CONCEPTUAL SUPPORT | The Harvard PON source directly distinguishes negotiation from mediation and describes mediation as involving a trained neutral third party who facilitates dialogue without imposing a decision. Record the negotiation and mediation passages. |
| `CLM-CONFLICT_RESOLUTION_BASICS-C` | DIRECT CONCEPTUAL SUPPORT | The Harvard PON source says process choice depends on complexity, stakes and relationship dynamics, and describes mediation outcomes as voluntary/nonbinding. Record the “Choosing the Right Conflict Resolution Process” and mediation passages; retain the caveat that a method description cannot guarantee a particular outcome. |
| `CLM-CONSTITUTIONAL_LAW_BASICS-B` | PARTIAL | International IDEA states that constitutions determine how power is shared and how rights are protected, but the registered overview does not adequately compare constitutional procedures and institutional mechanisms across systems. Add a specific comparative constitutional design source and pinpoint. |
| `CLM-CONSUMER_PROTECTION_BASICS-C` | PARTIAL | The registered OECD Consumer Policy page is a topic hub and does not establish how a particular dispute must be assessed under transaction terms and applicable jurisdictional law. Add an authoritative consumer-contract/dispute-resolution source and jurisdiction-specific legal caveat; do not generalize across legal systems. |

## 4. Cross-record, rights and source-quality findings

1. The Water Resources Claim C provenance contains an additional EPA Source reference without a matching EPA Evidence Use for that Claim. The existing EPA Evidence Use points to Claim A. This remains a linkage HOLD, not a silent inference.
2. All 20 Evidence Use records use generic descriptions and omit exact passage locators. A valid Claim → Evidence Use → Source reference chain does not prove complete support.
3. `SRC-ZOOLOGY_BASICS` has a descriptive sentence in `source_identity` rather than a bibliographic title; its OpenStax source also carries an explicit AI-ingestion restriction.
4. The NPS chronology Source is a broad archeology hub; the specific dating article is the better candidate for both chronology Claims.
5. The LLVM Source is a tutorial index. Claim A/B can be supported by the specific lexer/parser/AST/IR chapters; Claim C's correctness-preservation clause needs additional support or narrower wording.
6. The registered USGS and OECD pages are broad hubs. Claim-level support requires exact child pages/sections rather than treating a topic landing page as a pinpoint.
7. Legacy `publication_status=published` and `completion_status=complete` fields remain distinct from M13 risk status. All 20 selected Claims remain `UNASSESSED`; no publication authorization is inferred.
8. `SRC-WATER_RESOURCES_BASICS@1` and `SRC-WATER_RESOURCES_MANAGEMENT_BASICS@1` have the same external URI (`https://www.usgs.gov/mission-areas/water-resources`). They are duplicate source identities, not independent corroboration. Reconcile them through an authorized versioned Source correction; do not count the duplicate records as independent evidence.
9. The UN-Water report landing page is not reliably accessible in the current check, but the exact same Analytical Brief is available from the official UN Digital Library PDF. Prefer the PDF as the preserved locator after a versioned Source update.

## 5. Decision

- 20 Claim → Evidence Use chains were checked; 20 Evidence Use links were present in the selected packets.
- 9 Claims: direct conceptual support, subject to exact locator capture.
- 11 Claims: partial support or rights/linkage hold.
- Two Zoology Claims: RIGHTS HOLD pending written permission or replacement sources.
- Water Resources Claim C: unresolved EPA provenance/Evidence Use mismatch.
- No D/E/B scores assigned or inferred.
- No canonical Claim, Evidence Use, Source, Context, Scope, Relation or risk metadata modified.
- No publication, release or public-pilot approval granted.
- Package 25 closes only this 20-Claim screening pass. Package 26 must be selected from a newly generated queue after this commit, not from the current artifact.
