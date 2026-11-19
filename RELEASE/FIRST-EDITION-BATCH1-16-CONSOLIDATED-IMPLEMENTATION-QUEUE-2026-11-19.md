# First Edition — Consolidated Implementation Queue for Research Batches 1–16

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Purpose: convert completed research into a controlled, non-duplicative implementation queue.  
Status: **RESEARCH CONSOLIDATED; NO NEW CANONICAL AUTHORIZATION; ALL UNAPPROVED CANDIDATE SLICES REMAIN HOLD**

## 1. Executive state

The research dossiers and bounded authorizations now cover the following workstreams:

- Batches 1–3: residual Claim dependency and source-fit research, including SI locator remediation under its separate bounded authorization.
- Batches 4–6: residual locator/source-fit research for accounting, calculus, climate science, computer networks, democratic institutions and demography.
- Batches 7–9: source/locator research and a consolidated bounded remediation decision packet.
- Batch 10: 20 Claims / 24 EUs across Agrifood Systems, Ecophysiology, Food Distribution, Infrastructure Resilience, Magnetism and Agricultural Engineering.
- Batch 10 supplement: Water Security, 3 Claims / 4 EUs.
- Batch 11: 15 Claims / 15 EUs across Astronomy Observation, Matter, Optics, Temperature and Waves/Sound.
- Batch 12: 15 Claims / 15 EUs across Macroeconomics, Microeconomics, Money and Banking, Organizational Behavior and Public Budgeting; followed by a source/rights correction addendum.
- International Law v2: 13-record substantive re-review and version-drift review.

The exact-version master remains **1,129 rows = 1,058 candidate keys + 71 dependency records**. Part II slice coverage remains **124/385**. The 30 additional current Claims reconciled on 2026-11-19 and discovered outside the candidate-key master remain outside the denominator pending explicit scope triage. No candidate denominator is expanded by this queue.

### Bounded authorizations already present in the project record

The following authorizations are distinct from this implementation queue and must be executed only within their stated limits:
- Chemistry Evidence Remediation (six authorized slices).
- Engineering and Computing Remediation (eight authorized slices).
- Human Sciences Remediation (three authorized slices).
- Legal/Trade/Institutional Remediation (six authorized slices plus the explicitly listed cross-slice records).
- Remaining R7 Source Remediation (four slices).
- R9 Evidence Depth and its source-specific addenda (including hydraulic engineering, cultural heritage, archival science, history of mathematics, cartography and related authorized slices).
- SI Units Pinpoint Authorization.

Execution addenda exist for Chemistry, Engineering/Computing, Human Sciences, Legal/Trade/Institutional and R9 work. A spot-check of the current canonical tree confirms the engineering/computing outputs for cybersecurity (v2), databases (v3), distributed systems (v2) and artificial intelligence (v2) are present with version-aligned EUs and Context/Scope. The engineering addendum reports 72 canonical records changed across eight authorized slices and preserves HOLD. Do not repeat these completed changes.

## 2. Implementation lanes

### Lane A — locator-only or metadata-only changes with direct support

These are candidates for the first implementation wave once the owner authorizes the exact record list and the rights screen permits the chosen source. No Claim wording changes are implied.

| Research source | Candidate work | Required guard |
|---|---|---|
| Batch 1–3 follow-up | Astronomy Basics A–C; Cell Basics A–C; Conservation Biology A–C; Evolution A–C; Measurement Uncertainty A–C; Motion A–C; Soil Microbiology A–C; Soil Science A/B; Statistics A (NIST and existing OpenStax EU); Thermodynamics A; Water Resource Management A | Source identity/provenance alignment may require version increments; do not count the 21 extra current Claims as candidates |
| Batch 4–6 residual | Calculus A–C; Democratic Institutions A–C; Demography A/B; Accounting B | Accounting A/C and Demography C are not locator-only without narrowing or a second Source |
| Batch 7 | Cultural Anthropology A/C; Education A/B | AAA CC BY-NC and UNESCO source terms need item-level rights review; Education C is not closed |
| Batch 8 | Electromagnetism and Fluid Mechanics replacement proposals; Geometry source-fit correction; Governance A–C; Historical Geography A–C | The six Electromagnetism/Fluid Mechanics statements are replacement Claims, not locator-only; OECD/LOC reuse terms need review |
| Batch 9 | Antimicrobial Resistance C; Statistics C; Settlement Geography A–C | Settlement Geography manual is CC BY-NC-SA 3.0 IGO; commercial reuse not cleared |
| Batch 10 | Agrifood Systems A–C; Food Distribution A–C/D; Infrastructure Resilience A–C; Water Security A–C; Agricultural Engineering A/B | Agrifood World Bank and FEMA independent EUs need exact locators; preserve city scope for FAO food-distribution manual; EPA support is narrower than UN-Water |
| Batch 11 | Matter A–C; Temperature A–C; Waves/Sound A–C; Astronomy Observation B/C | OpenStax source rights/AI-use restrictions remain open; Astronomy needs additional NASA Sources |
| Batch 12 | Macroeconomics A–C; Money B/C; Microeconomics A/B | IMF article-level locators; Federal Reserve U.S.-scope boundary; OpenStax rights restrictions |

### Lane B — Source identity/URI corrections before Evidence Use changes

| Slice | Exact issue | Required action |
|---|---|---|
| Biodiversity Basics | Existing Source points to OpenStax §47.4 but Claim A needs §47.1; Claim C is broader than the source | Version Source identity to exact Biology 2e publication and decide whether Claim C is narrowed |
| Evolution Basics | URI is correct but Source identity is a generic placeholder | Correct exact OpenStax title/section identity; align provenance and dependent references |
| Immunology Basics | Source title/URI mismatch; current URL is not the named innate/adaptive immunity section | Correct exact book/chapter identity and section graph; replacement Claims A–C require approval |
| Accounting Basics | Generic Source identity; IFRS Conceptual Framework does not cover all bookkeeping/estimation language | Correct exact bibliographic identity and narrow A/C or add further standards |
| Agricultural Engineering | Current FAO land/water Source does not match mechanization/processing scope | Replace/split source profile; do not treat mechanization page as direct evidence for every irrigation/drainage factor |
| Ecophysiology | Current OpenStax Chapter 44 URI is not an adequate ecophysiology source identity; Claim C lacks direct method support | Correct source profile or choose rights-compatible alternative; add measurement-method source for C |
| Food Distribution | WFP Source title says Supply Chain but URI points to procurement infographic | Correct URI to WFP Supply Chain page; FAO city-focused scope remains explicit |
| Water Resource Management | Current UNESCO portal is too broad for surface/groundwater and management claims | Add or split USGS/UN-Water/UNEP sources through canonical ID allocation |
| Optics Basics | OpenStax Physics Chapter 16 URI is a waves chapter | Correct to University Physics Vol. 3 Chapters 1–2; preserve ray-optics approximation boundary |
| Waves/Sound | Source identity/URI does not accurately identify the relevant University Physics sections | Correct exact title and pin §§16.1 and 17.1 |
| Democratic Institutions | Generic International IDEA portal is too broad | Correct to Global State of Democracy Indices Methodology v10 (2026) |
| Macroeconomics | IMF series Source is not a claim-specific locator for GDP and inflation | Keep article identities distinct; do not compress multiple articles into one generic Source |
| Organizational Behavior | APA topic portal is less direct than OpenStax textbook | OpenStax has explicit CC BY-NC-SA and LLM-ingestion restrictions; do not substitute without rights decision |

### Lane C — Source-graph expansions requiring canonical ID allocation

These cannot be completed by merely editing existing locator strings:

1. **Macroeconomics B/C:** separate IMF GDP and Inflation Sources/EUs, unless the owner explicitly approves a single series-level Source model with article-level locators.
2. **Money and Banking A:** separate IMF “What Is Money?” Source/EU for medium of exchange, unit of account and store of value; keep Federal Reserve for U.S. monetary aggregates B/C.
3. **Statistics Basics A:** the independent OpenStax EU already exists; it needs a direct locator, not a new ID.
4. **Marine Biology B:** separate NOAA Aquatic Food Webs Source/EU; current NOAA ecosystem-science EU does not directly support trophic/energy transfer.
5. **Marine Biology C:** direct source for temperature/dissolved oxygen examples or narrower Claim.
6. **Pathology A–C:** current NCBI Bookshelf source is a cell-biology chapter and not an adequate independent pathology source; replace/split with verified pathology sources.
7. **Water Resource Management B/C:** separate UNEP IWRM source/EU if the broader management claims remain.
8. **Astronomy Observation B/C:** separate NASA spectrum and telescope Sources/EUs.
9. **Climate Science B/C:** separate NASA Causes and Effects Sources/EUs; all three existing Claims are editorial placeholders and require substantive replacements.
10. **Computer Networks A–C:** separate NIST glossary term sources and IETF RFC source; all three existing Claims are editorial placeholders and require substantive replacements.
11. **Education Systems C:** either narrow to UNESCO country-tailored review methodology or add distinct comparative sources for law, financing, governance, curriculum and delivery.

No canonical ID is invented in this queue. New IDs must be assigned by the repository's canonical ID allocation process and included in the exact-version master only after the records exist and are verified.

### Lane D — substantive Claim replacements or narrowing requiring editorial approval

| Slice | Issue | Proposed disposition |
|---|---|---|
| Cell Biology | Claims A–C are generic editorial placeholders | Replace with eukaryotic-cell nucleus/organelles, DNA/ribosome and mitochondria/chloroplast propositions; preserve the eukaryote boundary |
| Genetics | Claims A–C are generic placeholders | Replace with gene, inheritance and mutation propositions; preserve germline/somatic distinction |
| Immunology | Claims A–C are generic placeholders | Replace with innate/adaptive immunity, specificity/memory and humoral/cellular response propositions |
| Climate Science | Claims A–C are editorial metadata, not climate facts | Replace with observed evidence, human-caused warming and observed effects propositions from NASA; new Source graph required |
| Computer Networks | Claims A–C are editorial metadata | Replace with network, protocol and Internet protocol-layer propositions; new Source graph required |
| Biodiversity C | Source does not directly establish current three-part wording | Narrow to use of different biodiversity indicators or add a multi-source chain |
| Soil Science C | FAO page only partially supports all listed functions | Narrow to productivity/diversity/ecosystem services or add a separate NRCS chain |
| Accounting A/C | IFRS Framework does not support all operational wording | Narrow to general-purpose financial reporting and conceptual recognition/measurement principles |
| Agricultural Engineering C | Seven listed factors not directly established as one universal rule | Narrow to local technological/economic/social/environmental/cultural context or source each factor |
| Ecophysiology A/B/C | Current claims overgeneralize environmental ranges and methods | Narrow A/B; add a measurement-method source for C |
| Microeconomics C | “chosen market definition” is not supported by the cited equilibrium section | Narrow to quantity demanded equals quantity supplied at equilibrium |
| Organizational Behavior C | Current observation-method wording is not supported by the textbook's levels-of-analysis section | Narrow to individual/group/organization levels and organizational context, or add research-method source |
| Macroeconomics B/C | “market value” and “sustained” are less precise than IMF definitions | Use monetary value of final goods/services; inflation as rate of price-level increase over period |
| Soil Microbiology / Fluid Mechanics / Electromagnetism | Generic/placeholder Claims or scope issues identified in Batch 8 | Use only the exact proposed replacement statements in the Batch 8 dossier after subject/editor approval |

## 3. Rights and attribution gates that block implementation

The following are not merely documentation details; they affect the permissible source set for the first edition:

- OpenStax *Principles of Economics 3e*, *Principles of Microeconomics 3e*, *Organizational Behavior*, *Biology 2e*, and other identified titles carry CC BY-NC-SA terms and explicit restrictions on LLM training/ingestion or generative-AI offerings without prior written permission. Do not use as cleared sources for the project without written permission or a rights-compatible substitute.
- OpenStax Chemistry 2e and other textbooks require exact edition/preface review; no blanket permission is inferred from public access.
- IFRS publications are copyright-controlled; no reproduction/adaptation permission is inferred.
- OECD, ILO, UN, World Bank, ICRC, LOC, WFP, FAO, UNESCO and International IDEA items need item-level reuse and attribution checks. Government or institutional hosting is not itself a licence.
- NIST and U.S. government publications may be public information, but embedded third-party content and logos/graphics remain separately controlled.
- High-consequence content (food distribution, water security, infrastructure resilience, cybersecurity, health, engineering) remains conceptual unless a specific technical standard, qualified review and operational boundary are provided.

## 4. Exact implementation protocol

For each authorized slice, apply this sequence once and only once:

1. Freeze the exact PR branch HEAD and re-fetch every canonical record by exact ID/version/type.
2. Check the active authorization JSON against the proposed file list. If a record, version increment or wording change is not explicitly allowed, stop that change.
3. Prepare a per-record diff table: current ID/version, proposed ID/version, exact field changes, provenance dependencies, and source-rights status.
4. Apply Source version changes first where authorized; then Claims only where wording changes or provenance alignment is explicitly authorized; then EUs; then Context/Scope target references.
5. Do not alter publication_status, completion_status, allowlists, Relations or release-gate semantics unless the exact authorization names them.
6. Re-fetch every changed record and validate exact version references: Claim→EU→Source; Context/Scope→Claim A; any explicitly named Relation participants.
7. Update exact-version master and the slice README only within the authorization.
8. Run focused schema/graph checks, affected-slice tests and the exact-head full release gates.
9. Keep HOLD until rights, editorial review, Human View and all release conditions close.

## 5. Current technical/release boundary

- PR #22 remains OPEN / DRAFT / NOT MERGED.
- Last confirmed 4/4 green content HEAD remains `48c78389fb5345223627a687b22d51ee260b9d7d`.
- Documentation-only HEADs after that commit are not validated by the old 4/4 result. No exact-head CI PASS is inferred.
- No canonical changes are authorized by this queue itself.
- No candidate is promoted to INCLUDE or EXCLUDE; all reviewed candidates remain HOLD.
- No main-branch changes, merge, deployment or release approval are performed.

## 6. Immediate next execution order

1. Build a record-by-record bounded diff packet for the remaining unapproved locator-only items from Batches 1–16.
2. Separate the graph-expansion ID allocation list from locator-only edits.
3. Separate the 9+ placeholder Claim replacement set from source/locator updates and obtain subject-matter/editorial sign-off.
4. Close rights decisions for the OpenStax and other restricted sources before canonical use.
5. After the owner approves the exact packet, apply changes in small coherent slices, re-fetch and test after each slice, and only then run the full exact-head release gates.


## Addendum — Batch 13 research incorporated — 2026-11-19

A current RELEASE-tree check found the already-created `FIRST-EDITION-BATCH13-HISTORY-LITERATURE-RELIGION-OCEANOGRAPHY-RESEARCH-2026-11-19.md`. It covers 15 Claims / 15 EUs across History of Science, History of Technology, Religious Studies, Literature and Oceanography. This work is added to the queue without repeating its research:

- **Locator-only candidates:** History of Technology A/B; Literature A/B; Religious Studies B.
- **Source graph expansions:** History of Science Society source for History of Science A; AHA methodology source(s) for History of Science/Technology C and Literature C; Religious Studies Project source for Religious Studies A/C.
- **Substantive Claim replacements:** Oceanography A–C are editorial placeholders. Proposed replacement propositions concern the scope of oceanography, mechanisms of ocean currents, and CTD measurements; all three require owner/editor approval and separate NOAA source/EU chains.
- **Rights/scope controls:** preserve the U.S.-focused boundary of Harvard Pluralism examples; treat Smithsonian/LOC guides as research navigators rather than proof of every listed item; verify third-party media rights on NOAA pages.
- All five slices remain HOLD; no canonical IDs or records were changed by the Batch 13 research dossier.


## Addendum — Batch 14 research incorporated — 2026-11-19

The new Batch 14 dossier covers the two residual slices identified by the Society and Institutions gap audit: `sociology-basics` and `public-administration-basics` (6 Claims / 6 EUs / 18 records).

- Sociology A–C are editorial/meta placeholders. The ASA *Sociology: A 21st Century Major* brochure (2023), page 1, directly supports three bounded replacement propositions: definition/scope of sociology; research methods; and how research can inform theory and policy. Claim replacements require explicit editor approval.
- Public Administration A–C are substantive. UN ECOSOC Committee of Experts on Public Administration, E/C.16/2006/4 §§III, I and VI provides direct locators for public functions/services, rules/procedures, and jurisdiction/context-dependent institutional arrangements. Claims can retain their wording; Source/EUs/Context/Scope need versioned alignment.
- Exact proposed 18-record scope and prohibited changes are in `FIRST-EDITION-BATCH14-SOCIOLOGY-PUBLIC-ADMINISTRATION-REMEDIATION-RESEARCH-2026-11-19.md`. No canonical changes or new IDs were made; both slices remain HOLD pending bounded authorization and rights review.


## Addendum — Batch 15 hydrology and meteorology — 2026-11-19

The new Batch 15 dossier covers Hydrology and Meteorology only (6 Claims / 6 EUs; exact 12-record bounded authorization proposal). Oceanography is excluded because it is already addressed by Batch 13.

- Hydrology A/B: USGS “What is Hydrology?” provides direct section/paragraph locators. Hydrology C uses the same page plus its linked USGS “Water cycle” page for runoff, infiltration, evaporation/evapotranspiration and the separate transpiration passage.
- Meteorology A: NOAA “Weather and atmosphere” opening definition. B/C: NOAA “Weather observations” → “Observation methods” and “Weather forecasting”. Keep U.S.-specific operational examples within their stated scope.
- Proposed authorization: 12 exact records (Hydrology Source/Claims/EUs/Context/Scope and Meteorology EUs only). No active hydrology/meteorology authorization was found; no canonical changes made. Both slices remain HOLD.
- Dossier: `FIRST-EDITION-BATCH15-HYDROLOGY-METEOROLOGY-LOCATOR-REMEDIATION-RESEARCH-2026-11-19.md`.


## Addendum — Batch 15 law, public administration, social statistics and measurement — 2026-11-19

The separate Batch 15 dossier covers 15 candidate Claims / 15 EUs across Law Basics, Public Administration Basics, Social Statistics Basics, Sociology Basics and Units and Measurement. It is not the Hydrology/Meteorology Batch 15 dossier.

- **Locator-only candidates:** Law A–C (Cornell LII Wex, preserve U.S.-law boundary); Social Statistics A (UN Statistics Division); Units and Measurement B (BIPM SI Brochure / NIST SI Units).
- **Source graph expansions:** Public Administration A–C needs a separate UN Human Rights Council A/HRC/25/27 source; Social Statistics B/C need UN Fundamental Principles of Official Statistics and Statistics Canada; Units and Measurement A/C need BIPM VIM and NIST TN 1297. Do not combine publishers in one Source record.
- **Substantive Claim replacements:** Sociology A–C are editorial placeholders; ASA's 2023 *Sociology: A 21st Century Major* brochure supports three replacement proposals (definition/scope, social structures/change, research methods). Owner/editor approval and rights review required.
- All five slices remain HOLD; no canonical IDs or records were changed. Dossier: `FIRST-EDITION-BATCH15-LAW-ADMINISTRATION-SOCIAL-STATISTICS-MEASUREMENT-RESEARCH-2026-11-19.md`.

## Addendum — Batch 16 migration basics — 2026-11-19

The Batch 16 dossier covers the remaining migration-basics candidate slice: 3 Claims / 3 EUs / 1 current Source. IOM Toolkit glossary and Module 3 provide direct locators for migration definition and drivers. Claim C requires distinct UNHCR Refugee Convention and UN Guiding Principles dependencies to distinguish migrants, refugees and IDPs. The current IOM Source points to a broad WMR landing page; align to the exact Toolkit identity or add a separate Toolkit Source. Legal-status content requires qualified migration/refugee-law review. All Claims remain HOLD; no canonical IDs or records changed. Dossier: `FIRST-EDITION-BATCH16-MIGRATION-BASICS-EVIDENCE-AND-LEGAL-STATUS-RESEARCH-2026-11-19.md`.

## Supplemental P4/P5 pinpoint pass — disaster, water quality and electrical grid — 2026-11-19

This is not a new batch and does not change historical P4/P5 denominators. Fifteen existing Claims / 18 EUs / eight Sources were re-fetched across disaster-response-logistics, disaster-recovery, water-quality and electrical-grid. Exact locators were mapped to FEMA IS-52, WFP Logistics Cluster, FEMA NDRF Third Edition, UNDRR, EPA, WHO 2026 drinking-water guidelines, EIA and DOE. Findings include the OCHA homepage source being too broad for logistics, the FEMA Disaster Recovery source pointing to an IS-2900 course page rather than the NDRF publication, Disaster Recovery B's misleading “separate phase” wording, the U.S. Clean Water Act boundary for Water Quality C, and the need to identify WHO's 2026 fourth edition with three addenda. All four slices remain HOLD. Dossier: `FIRST-EDITION-P4-P5-DISASTER-WATER-QUALITY-ELECTRICAL-GRID-PINPOINT-SUPPLEMENT-2026-11-19.md`.


## Addendum — P4/P5 supplemental pinpoint implementation proposal — 2026-11-19

The P4/P5 supplemental pinpoint review has been converted into an exact bounded authorization proposal: `FIRST-EDITION-P4-P5-DISASTER-WATER-QUALITY-ELECTRICAL-GRID-BOUNDED-AUTHORIZATION-PROPOSAL-2026-11-19.md`.

- Scope: four already-audited slices; 49 existing records in the audited topology; 36 proposed existing-record version changes. No candidate denominator change.
- Disaster Response Logistics: correct the generic OCHA homepage Source to the direct WFP Logistics Cluster page; version Claims A–C only for provenance alignment; pin primary and FEMA EUs; refine Context/Scope. Optional separate FEMA Distribution Management Plan Guide Source/EU for Claim B requires canonical ID allocation and explicit approval.
- Disaster Recovery: correct the FEMA Source to the actual NDRF Third Edition; version Claims A/C only for provenance alignment; revise Claim B to reflect that recovery begins during response and overlaps other phases; pin all four EUs; align Context/Scope.
- Water Quality: narrow Claim A to pollutant-specific criteria; make the U.S. Clean Water Act boundary explicit in Claim C; identify WHO's exact 2026 fourth edition with three addenda; pin all four EUs and align Context/Scope.
- Electrical Grid: version only EUs A–D with EIA/DOE locators; preserve claims and U.S.-specific topology boundary.
- This proposal is not authorization. No canonical changes are permitted until the owner explicitly approves the exact list and the bounded authorization is recorded. All four slices remain HOLD.


## Addendum — R9 Settlement Geography rights-compatible source alternative — 2026-11-19

The earlier Settlement Geography authorization proposal relied on the joint 2021 manual (CC BY-NC-SA 3.0 IGO), whose NonCommercial term does not clear commercial reuse. A better text-only alternative has been verified: Eurostat, *Review and implementation of the degree of urbanisation*, 2026 edition, CC BY 4.0 for EU-owned content with attribution and change indication. Direct locators for Claims A–C: §1.2 p.6 and §2.1 p.7. Third-party cover photography, most maps, other photos and administrative-boundary content are excluded; no visuals are proposed. The report is a Eurostat Statistical Report and is not an official EC position. See `R9-SETTLEMENT-GEOGRAPHY-EUROSTAT-CC-BY-4-0-SOURCE-ALTERNATIVE-2026-11-19.md`. The nine-record v1→v2 proposal remains pending explicit owner authorization; all records remain HOLD.


## Addendum — exact diff packets prepared — 2026-11-19

Two record-level packets were prepared without changing canonical JSON:

1. `R7-CIVIL-SOCIETY-BOUNDED-DIFF-PACKET-2026-11-19.md` — 13 exact current records in `civil-society-basics`, all v1 at inspection HEAD `838c039851eddb281664fce779cfd6be4ef72747`. This is within the existing `REMAINING-R7-SOURCE-REMEDIATION-001` bounded authorization. It specifies OECD/LEGAL/5021 and the UN Civil Society Unit “About us” as primary/independent sources, preserves all Claim statements, and versions Claims only for provenance alignment. Implementation still requires exact-HEAD re-fetch and the rights/editorial/Human View gates; slice remains HOLD.
2. `FIRST-EDITION-BATCH15-LOCATOR-ONLY-DIFF-PACKET-2026-11-19.md` — four candidate EU v1→v2 locator-only changes (Law A/B, Social Statistics A, Units and Measurement B). This is an owner-approval packet, not a bounded authorization. Law C was deliberately excluded because the current Cornell Wex source does not independently establish its broad comparative proposition; the formal “coherent set” qualifier in Units and Measurement B retains a separate BIPM support dependency/wording review.

Both packets are documentation-only. No canonical Claim, Evidence Use, Source, Context, Scope, Relation, status, allowlist, coverage manifest or publication decision changed. All affected slices remain HOLD. No main-branch write or merge occurred.


3. `R7-BOUNDED-AUTHORIZATION-RECONCILIATION-2026-11-19.md` — spot-check reconciliation of already-applied and pending bounded authorizations. R9 sampled Sources and the six Legal/Trade/Institutional primary Sources are already v2; the seven International Law dependent alignment records are already v2. Civil Society remains fully v1 and has a 13-record packet. Labour Economics is blocked by an OpenStax licence/AI-ingestion contradiction in the active authorization; Comparative Civilizations requires a schema-valid supplementary-source mapping and rights decision. This is explicitly a spot-check, not a complete 94-scope certification.


## Additional R7 bounded packets and rights decision — 2026-11-19

4. `R7-COMPARATIVE-CIVILIZATIONS-BOUNDED-DIFF-PACKET-2026-11-19.md` — all nine current records re-fetched at inspection HEAD `820125dc1b470b79f2d49eb3bee2be9af2383ef0`; proposes AHA as primary Source v2, three claim-specific EU v2 locators, provenance-only Claim v2 alignment, and MOE's chronology/causation distinction as a supplementary `provenance.external_sources` entry on EU-C. Existing schema supports this representation; no new Source ID or schema change. Rights review remains open; slice HOLD.
5. `R7-LABOUR-ECONOMICS-OPENSTAX-RIGHTS-DECISION-2026-11-19.md` — owner decision packet for the incorrect CC BY 4.0 assertion in `remaining_r7_remediation_2026_11_19.basis.rights_boundary`. Official OpenStax terms specify CC BY-NC-SA 4.0 and prior written permission for LLM training/ingestion and generative-AI offerings. Labour Economics canonical records remain v1; no implementation until rights path is decided and authorization corrected.

The Comparative Civilizations schema blocker noted in the initial reconciliation is superseded by the exact schema inspection and packet above. The Labour Economics licensing conflict remains unresolved and is now documented as a separate owner decision. All affected slices remain HOLD.


## Batch 16 authorization preparation — 2026-11-19

6. `FIRST-EDITION-BATCH16-MIGRATION-BASICS-BOUNDED-AUTHORIZATION-REQUEST-2026-11-19.md` — exact seven-record SHA inventory; proposes IOM Toolkit source alignment and claim-specific EUs A/B/C; requests two separate canonical Source IDs and two separate Evidence Use IDs for UNHCR/1951 Convention and UN Guiding Principles Claim C dependencies. This is an owner authorization request, not an existing authorization. No IDs allocated and no canonical changes made. Migration Basics remains HOLD.


## Exact-head continuation — R7 rights and dependency closure (2026-11-19)

Inspection baseline before this documentation-only update: PR #22 HEAD `531d4f57c8aed106e1f2b42bd5295752740e3545`.

- Civil Society Basics: re-fetched all 13 canonical records; every blob SHA still matches the existing bounded diff packet. OECD/UN rights recheck is recorded in the Legal/Trade/Institutional rights screen. No implementation until project licence/distribution compatibility is decided.
- Comparative Civilizations Basics: re-fetched all nine canonical records; every blob SHA still matches its bounded diff packet. AHA and MOE source substance/locators are confirmed; rights terms remain restrictive/unclear for the intended project distribution. No implementation until owner decision.
- Labour Economics Basics: re-fetched all 13 canonical records; all remain v1 and the Claim→EU→Source plus Context/Scope target graph is aligned. OpenStax's official HTML Preface and help pages state CC BY-NC-SA 4.0 and an LLM-ingestion restriction, while a separate official PDF asset displays CC BY 4.0. Exact-asset clarification is required; do not use the authorization's inaccurate blanket CC BY 4.0 statement.
- The R7 reconciliation, rights screen, owner decision register and dedicated Labour Economics decision packet were updated. No canonical Content/Reference record changed.
- Part II exact-version master was inspected: its table contains 1,129 distinct exact-version rows (1,058 candidate keys + 71 dependency records). The ten-record dependency supplement explains the progression from the earlier 1,119-row table; the current table count is 1,129. Part II slice coverage remains 124/385, while candidate-slice accounting separately classifies all 121 first-edition candidate slices. These denominators describe different universes and must not be conflated.
- GitHub compare from the pre-supplement dependency HEAD `cbb620b1b2fc714414b57dc53ac7b8faba8980e1` to the current documentation HEAD showed 33 changed paths, all under `RELEASE/`, with zero `CONTENT/` and zero `REFERENCE/` changes. Thus the previously exact-verified dependency records were not altered by this documentation follow-up.

### Current blocker order

1. Owner-level rights/distribution decision for Civil Society and Comparative Civilizations.
2. OpenStax exact-asset clarification and correction of the Labour Economics authorization rights boundary, or approval of a rights-compatible source replacement.
3. Owner authorization for any Batch 16 canonical dependency IDs before graph expansion.
4. Continue only the next uncovered exact-version/dependency audit items; do not repeat completed domain remediation.
5. Run all exact-head workflows after the current documentation commits settle; preserve HOLD and Draft state.


## Exact-head continuation — out-of-master Claim and Relation dependency reconciliation — 2026-11-19

Inspection baseline: PR #22 HEAD `d77c3f6bda3b9d8102f63b91198b7a3454ce3158`.

- Re-fetched all **30** known current out-of-master Claim JSON records across 14 slices. All 30 have exact expected `record_id`, `record_version=1`, and `record_type=claim`; all 30 unique `record_id@1` keys remain absent from the 1,129-row exact-version master. No candidate denominator change.
- The 30 consist of 21 additional Claims in the Batch 1/3 follow-up table plus nine Climate Adaptation, Hydrology and Meteorology Claims from Batch 14. Corrected the Batch 1/3 follow-up §7 heading from “24” to “30” so it agrees with the 30 table rows and the 21 + 9 explanation.
- Re-fetched six cross-slice Relations and their referenced participant/source records. Four are aligned with their current authorized version state: Library–Archival v3, Mathematics–Engineering History v3, Cartography–Settlement Geography v2, Political Economy–Taxation v2.
- Labour Economics–Social Policy and Migration–Labour Economics remain at Relation v2 and reference Labour Economics Claim C@1. The active bounded authorization's intended v3 alignment depends on Labour Economics Claim C@2; that Claim remains blocked by the OpenStax rights inconsistency. Do not version either Relation early or create a dangling reference.
- Durable report: `reports/agent-work/chief-engineer/out-of-master-claims-and-relation-dependency-reconciliation-2026-11-19.md`.
- No canonical Content/Reference record, candidate membership, allowlist, publication state or INCLUDE/HOLD/EXCLUDE decision changed. All affected candidates remain HOLD. No main-branch write or merge occurred.

### Next action

Keep the 30 Claims outside the candidate denominator pending explicit owner scope decision. Resolve Labour Economics rights/authorization before the two dependent Relation alignments. Continue with another exact bounded authorization scope only where the current tree can be reconciled without owner decisions or repeating completed work.


## Exact-head continuation — R9 bounded-authorization conformance reconciliation — 2026-11-19

Inspection HEAD: `b79080e2e98ad951104f969b8298a1cb66e17d4a`. Durable report: `reports/agent-work/chief-engineer/r9-bounded-authorization-conformance-reconciliation-2026-11-19.md`.

The remaining R9 bounded outputs were re-fetched against the current canonical tree. Hydraulic Engineering, Cultural Heritage, History of Mathematics, Cartography and Food Systems contain the expected bounded remediation outputs; SI Units Evidence Use A/B are v2 with NIST section references and attribution. Food Systems remains the distinct 12-record/two-Source/four-Claim profile. No completed remediation was repeated and no canonical record or coverage field was changed.

Two explicit owner authorization/provenance issues remain:
- History of Mathematics Claim C@2 and Evidence Use C@2 depend on `SRC-HISTORY_OF_MATHEMATICS-CAMBRIDGE@1`. The active `R9-HISTORY-OF-MATHEMATICS-REMEDIATION-001` names MacTutor v2 and one additional Oxford Source, but does not name the Cambridge Source branch. The remediation addendum's description of a three-source slice is not itself authorization.
- Archival Science Claim C@2 and Evidence Use C@2 depend on `SRC-ARCHIVAL_SCIENCE-ICA@1`. The active authorization explicitly preserves this already-present branch but does not retroactively authorize its creation. The README correctly retains this as an unresolved owner authorization/provenance blocker.

Do not delete, rewrite, version, or otherwise alter either branch without a new explicit bounded authorization or owner disposition. Both slices remain HOLD.

The coverage manifest at inspection HEAD reports 4,680 total records, 589 Sources, 479 vertical slices and 19/19 directly covered record types. These are structural coverage counts, not rights or publication clearance. The manifest was not changed.

The previously reported 21 out-of-master Claims is superseded: 30 current Claim records were re-fetched, uniquely identified and reconciled outside the 1,129-row candidate master. They remain outside the denominator pending owner scope decision.

### Current blocker order

1. Owner authorization/provenance decision for History of Mathematics Cambridge Source/Claim C/Evidence Use C.
2. Owner authorization/provenance decision for Archival Science ICA Source/Claim C/Evidence Use C.
3. Separate explicit authorization and rights decision before Settlement Geography canonical source replacement/remediation.
4. Existing R7 Labour Economics/OpenStax rights mismatch before the two Labour-dependent Relations can be aligned.
5. Rights/editorial owner decisions R-01–R-10; no license, rights holder, editor, approver or contact may be inferred.

### Exact-head CI snapshot

For `b79080e2e98ad951104f969b8298a1cb66e17d4a`, Offline Edition and MVP Contribution Form Browser Tests completed successfully; Reference implementation tests and Release Conformance Gate were still in progress at the final check. No full CI PASS is claimed.

### Next action

Keep the candidate denominator and all HOLD dispositions unchanged. Obtain owner decisions for the two R9 authorization/provenance branches, then proceed only within any newly granted bounded scope. Recheck exact-head CI and PR/main boundaries after documentation updates.


## Exact-head continuation — R7 Civil Society and Comparative Civilizations bounded implementation — 2026-11-19

Under the existing `REMAINING-R7-SOURCE-REMEDIATION-001` authorization, two previously prepared bounded packets were implemented against the current branch after re-fetching all canonical records and confirming their v1 starting versions.

### Civil Society Basics

- 13/13 canonical records versioned v1→v2.
- Primary Source now identifies OECD DAC Recommendation OECD/LEGAL/5021; independent Source identifies the UN DGC Civil Society Unit “About us” page.
- Claims A–C were versioned only to align `provenance.created_from`; statement and `claim_type` preserved.
- Primary and independent Evidence Use A–C now contain claim-specific locators and support boundaries, with exact current Claim/Source v2 references.
- Context and Scope target Claim A v2; README and item-level rights screen updated.
- No source text, images, page layout or other expressive assets reproduced.

### Comparative Civilizations Basics

- 9/9 canonical records versioned v1→v2.
- Source now identifies David Smith/AHA, “Introduction to Doing World History” (1998).
- Claims A–C were versioned only for provenance alignment; statements and `claim_type` preserved.
- Evidence Use A–C now contain claim-specific AHA locators and support boundaries.
- EU-C retains one canonical AHA `content.source_ref`; the Singapore MOE 2021 chronology/causation reference is recorded only in schema-supported `provenance.external_sources`.
- Context, Scope and README updated with the educational/methodological limits.
- No source text, syllabus definitions, tables, images or graphics reproduced.

Both slices remain **HOLD**. This implementation does not close project-level rights decisions, item-level permissions, independent editorial review or Human View; it does not change allowlists or assign INCLUDE/EXCLUDE. No other slice or relation was modified.

Validation after implementation confirmed 13/13 Civil Society and 9/9 Comparative Civilizations records are v2, published and complete; all six Civil Society and all three Comparative Civilizations Evidence Use records have non-empty locators and support descriptions. The Claim statements/types and publication/completion states were preserved.

Owner decision register: `RELEASE/FIRST-EDITION-RIGHTS-EDITORIAL-OWNER-DECISION-REGISTER-2026-11-19.md`. Rights screen: `RELEASE/LEGAL-TRADE-INSTITUTIONAL-RIGHTS-AND-ATTRIBUTION-SCREEN-2026-11-19.md`.

### Next action

Keep both slices HOLD pending rights/distribution decisions, independent editorial review and Human View. Continue with the Labour Economics blocker only after the OpenStax rights mismatch is resolved; do not use the incorrect CC BY 4.0 clause in the current R7 authorization.


### Exact-version master synchronization — same implementation pass

After the 22 canonical v1→v2 increments, the Part II exact-version master was synchronized for exactly 22 rows: 13 Civil Society and 9 Comparative Civilizations. The master remains 1,129 rows = 1,058 candidate keys + 71 dependency records, with 1,129 unique compound keys and zero duplicates. All 22 affected rows now reference @2; all 1,129 decisions remain HOLD. No candidate membership, denominator or slice coverage was expanded. Integrity delta is recorded in `reports/agent-work/chief-engineer/part-ii-exact-version-register-integrity-2026-11-19.md`.
