# First Edition — Consolidated Implementation Queue for Research Batches 1–12

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

The exact-version master remains **1,129 rows = 1,058 candidate keys + 71 dependency records**. Part II slice coverage remains **124/385**. The 21 additional current Claims discovered outside the candidate-key master remain outside the denominator pending explicit scope triage. No candidate denominator is expanded by this queue.

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

1. Build a record-by-record bounded diff packet for the remaining unapproved locator-only items from Batches 1–12.
2. Separate the graph-expansion ID allocation list from locator-only edits.
3. Separate the 9+ placeholder Claim replacement set from source/locator updates and obtain subject-matter/editorial sign-off.
4. Close rights decisions for the OpenStax and other restricted sources before canonical use.
5. After the owner approves the exact packet, apply changes in small coherent slices, re-fetch and test after each slice, and only then run the full exact-head release gates.
