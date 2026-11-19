# R9 Evidence-Depth Remediation Addendum — 2026-11-19

Date: 2026-11-19  
Authorization: `R9-EVIDENCE-DEPTH-REMEDIATION-001`  
Audit: `RELEASE/R9-FIRST-EDITION-EVIDENCE-DEPTH-FOLLOWUP-2026-11-19.md`  
Register: `RELEASE/FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md`  
Branch: `mvp-public-contribution-design-2026-10-11`

## Scope

Three priority R9 slices were remediated under the bounded authorization:

1. `history-of-medicine-basics`
2. `history-of-engineering-basics`
3. `library-science-basics`

This work follows the R9 evidence-depth follow-up and does not repeat the prior structural/Claim audit. It uses factual paraphrase and pinpoint citation only. No source prose, tables, photographs, figures, diagrams or page layouts were copied.

## Exact record changes

| Slice | Source | Claims | Evidence Use | Context | Scope | Total |
|---|---:|---:|---:|---:|---:|---:|
| history-of-medicine-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| history-of-engineering-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| library-science-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| **Total** | **3** | **9** | **9** | **3** | **3** | **27** |

All 27 records were versioned v1→v2. Publication and completion states were preserved.

### history-of-medicine-basics

- Source v2 identifies the National Library of Medicine, *Collection Development Guidelines*, “History of Medicine” (updated 2022-09-30), with Definition, Discussion and Scope and emphasis locators.
- Claims A and B were versioned without wording changes to align provenance with Source v2.
- Claim C was narrowed from a general statement about primary and secondary sources to the NLM-supported proposition that historical study uses interpretive, analytical and biographical secondary literature.
- Evidence Use A–C now point to exact NLM sections and Claim/Source v2.
- Context and Scope now explicitly exclude clinical recommendations and medical guidance.

### history-of-engineering-basics

- Source v2 identifies the Smithsonian Institution, “Explore Technology & Innovation”, with exact featured-story and collection locators.
- Claims A–C were versioned and narrowed to documented objects and interpretive stories actually presented by the Smithsonian page:
  - technologies, inventions, artifacts and collections as historical material;
  - illustrative engineering/technology examples across roads, aviation, computing and communications;
  - Smithsonian presentation through both object collections and interpretive stories.
- Evidence Use A–C identify the relevant introduction, featured stories and “From the Collections” entries.
- Context and Scope now state that the page is a specific museum collection/story selection, not a complete or globally representative history and not evidence of causation.

### library-science-basics

- Source v2 identifies IFLA and UNESCO, *IFLA-UNESCO Public Library Manifesto 2022*, with page and section locators.
- Claims A–C were narrowed explicitly to public libraries:
  - equal access to information, knowledge, collections and services;
  - missions involving education, lifelong learning, literacy, scientific and community information;
  - preservation/access for local and Indigenous knowledge, heritage, oral tradition and digital materials.
- Evidence Use A–C cite “The Public Library” and “Missions of the Public Library”, pp. 1–3.
- Context and Scope clarify that the Manifesto is normative/advocacy guidance, not empirical proof of service effectiveness or a complete description of all library types.

## Rights and attribution boundary

- NLM: use is limited to independent factual paraphrase and citation; no NLM images, collection objects or third-party material are reproduced. Item-level rights and project distribution compatibility remain open.
- Smithsonian: the page contains links and images for individual objects/stories; no photographs, object images, expressive text or page design are copied. The rights status of the exact linked content and project-level reuse remains open.
- IFLA/UNESCO: the Manifesto is cited by title, organization, edition and page/section. No text, poster, image or layout is reproduced. Exact item-level reuse terms and project-licence compatibility remain open.
- Public accessibility is not treated as permission to reproduce source expression. This addendum does not grant rights clearance.

## Validation and disposition

- All 27 updated records preserve `publication_status` and `completion_status`.
- Claims and Evidence Use records point to current Source/Claim versions; Context and Scope target current Claim A v2.
- The changes are limited to the three authorized slices and their READMEs.
- All three slices remain **HOLD**.
- No INCLUDE/EXCLUDE decision or first-edition allowlist change was made.
- No main-branch change, merge, deployment, publication or release action was performed.

## Remaining work

1. Complete item-level rights review and project-owner licence/distribution decisions.
2. Obtain independent editorial review and Human View of the rendered reader presentation.
3. Continue R9 source-depth remediation in the remaining priority slices: hydraulic engineering, cultural heritage, archival science and other slices identified in the R9 follow-up.
4. Reconcile exact-version candidate register entries to v2 and rerun exact-head Reference Tests, Release Conformance Gate, Offline Edition and MVP Contribution Form Browser Tests.
5. Keep all three slices HOLD until every applicable gate is closed.


## Cross-slice relation reference alignment

The exact-head preflight after the three slice remediations identified four stale references in two existing cross-slice Relations. Under the explicit two-record extension to `R9-EVIDENCE-DEPTH-REMEDIATION-001`, the following relations were versioned v1→v2:

- `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION`: updated only the Library Science Source and Claim A references to v2.
- `REL-CROSS-MATH-ENGINEERING-HISTORY`: updated only the History of Engineering Source and Claim A references to v2.

Both relation types, participant identities and order, roles, undirected direction, the other participants/source references, and `CTX-CROSS-SLICE-LINKAGE@1` frame references were preserved. These remain contextual links only; they do not establish evidence or causality. This adds two relation records to the 27 slice records corrected above; it does not change the 93-record R9 vertical-slice inventory or any slice decision.


## Next bounded R9 package — hydraulic engineering

Under the separate `R9-HYDRAULIC-ENGINEERING-REMEDIATION-001` authorization, `hydraulic-engineering-basics` was updated with a deliberate two-source profile:

- HEC-RAS Hydraulic Reference Manual v6.5 as `SRC-HYDRAULIC_ENGINEERING@2`.
- HEC-HMS Application Guide as the additional `SRC-HYDRAULIC_ENGINEERING-HMS@1`.
- Claims A/C and Evidence Use A/C reference HEC-HMS; Claim B and Evidence Use B reference HEC-RAS.
- All three Claims, all three Evidence Use records, Context and Scope are v2. The new Source adds one canonical record; the slice now contains ten records.
- No design equations, flood forecasting, dam/levee operations or site-specific engineering instructions were added. Rights remain unresolved; slice HOLD.

The ten-slice R9 inventory is now 94 records, not 93, because the hydraulic slice has two distinct Source branches. No record was removed to preserve the historical target count.


## Cultural heritage two-source remediation

Under `R9-CULTURAL-HERITAGE-REMEDIATION-001`, the `cultural-heritage-basics` slice now has two distinct Sources: the 1972 World Heritage Convention (Articles 1 and 3) and the 2003 Intangible Cultural Heritage Convention (Article 2(1)). Claims A/B and Evidence Use A/B map to the 1972 Convention; Claim C and Evidence Use C map to the 2003 Convention. All nine existing slice records were versioned v1→v2 and one additional Source was created at v1, bringing the slice to 10 records. Community recognition, consent, cultural protocols and item-level rights remain open. The slice remains HOLD.

The R9 inventory is now 95 records across ten slices. No records were removed to meet the historic 90-record target.


## Archival science source and dependency review

The current `archival-science-basics` graph contains two source branches:

- `SRC-ARCHIVAL_SCIENCE@2`: SAA “Archives 101: Basic Principles”, explicitly a preliminary community-archives guide, with processing/provenance locators.
- `SRC-ARCHIVAL_SCIENCE-ICA@1`: ICA ISAD(G), Second Edition, with provenance and multilevel-description locators.

The current bounded authorization `R9-ARCHIVAL-SCIENCE-REMEDIATION-001` preserves the already-present ICA Source and Claim C/Evidence Use C branch, but expressly does **not** retroactively authorize creation of that ICA Source. This is an unresolved authorization/provenance blocker, not a rights clearance. The ICA branch remains HOLD pending an explicit project-owner disposition; do not advance the slice to INCLUDE while this remains open.

The currently authorized corrective pass is limited to:
- Claim B v2→v3, retaining SAA Source v2 and narrowing the statement to provenance plus discernible original order.
- Evidence Use B v2→v3, pointing to Claim B v3 and SAA Source v2, with exact “Principle of Provenance” and “Arrangement” locators and an explicit PRELIMINARY DRAFT support boundary.
- Context and Scope v1→v2, with the SAA preliminary-draft limitation and privacy, donor, access-restriction and community-archive boundaries.
- README and R9 documentation/register/rights-screen updates.

The current graph has 10 records: two Sources, three Claims, three Evidence Use, Context and Scope. Publication/completion states remain unchanged. No source prose, standard text, diagrams, tables, finding aids or archival examples are reproduced. The slice remains HOLD.

The exact R9 inventory is **96 records** across ten slices: six 9-record profiles, food systems 12 records, and hydraulic engineering, cultural heritage and archival science at 10 records each. The initial 31 generic Evidence Use records have been reduced by 18 across the completed remediation packages; **13 Evidence Use records remain without claim-specific pinpoints** in history of mathematics, cartography, food systems and settlement geography. No first-edition allowlist or decision was changed.

## Remaining R9 source-depth order

1. History of mathematics — pin exact cross-cultural historical examples and add independent support for the methodology Claim.
2. Cartography — pin USGS Mapping 101 sections and retain boundaries for U.S. examples versus global conventions.
3. Food systems — pin FAO and World Bank sources separately; preserve the 12-record profile.
4. Settlement geography — pin UN-Habitat methodology, grid classification, aggregation and national-definition limits.

All ten R9 slices remain HOLD pending item-level rights, independent domain editorial review, Human View and exact-head CI.


## Archival cross-slice relation reference alignment

Under `R9-ARCHIVAL-CROSS-SLICE-RELATION-ALIGNMENT-001`, `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION` was versioned v2→v3. Only the archival participant references were advanced from `SRC-ARCHIVAL_SCIENCE@1` and `CLM-ARCHIVAL_SCIENCE-A@1` to the current v2 records. The Library Science references remain at v2; relation type, participant identities/order, roles, undirected direction and frame reference were preserved. This is a dependency-reference correction only; the relation remains a contextual link, not evidence or causality. The relation is outside the 96-record ten-slice R9 vertical inventory.


## History of mathematics three-source remediation

Under `R9-HISTORY-OF-MATHEMATICS-REMEDIATION-001`, the slice now has three Source records: MacTutor v2, Oxford regional history v1 and Cambridge scholarly chapter v1. Claims A–C, Evidence Use A–C, Context and Scope are v2. MacTutor is used only for notation/communication and historical-context sections; Oxford supplies the cross-cultural regional examples; Cambridge supplies the narrower historical calculus example. The slice now contains 11 records. No source text, diagrams, images, equations in source-specific layout or Cambridge chapter content is reproduced. Rights remain open; the slice remains HOLD.

The R9 inventory now contains 98 vertical-slice records. No record was removed to meet the historic 90-record target.


## Cartography two-source remediation

Under `R9-CARTOGRAPHY-REMEDIATION-001`, the `cartography-basics` slice was updated:

- `SRC-CARTOGRAPHY@2` now identifies USGS Mapping 101 and pins “Why a map?” and the cartography definition.
- Added `SRC-CARTOGRAPHY-TOPO@1` for USGS Fact Sheet 035-01, *Finding Your Way with Map and Compass* (2001), with exact topographic-map, contour, contour-interval, symbol and map-scale locators.
- Claims A–C and Evidence Use A–C advanced v1→v2. Claim A/EU-A use Mapping 101; Claims B/C and EU-B/C use the Fact Sheet. All current Claim/Source references align.
- Context and Scope advanced v1→v2 and distinguish USGS examples from global conventions, retaining map-projection trade-offs and excluding professional GIS/geodetic specifications.
- The slice now has 10 records (2 Sources + 3 Claims + 3 Evidence Use + Context + Scope). Publication/completion states remain unchanged. No maps, symbol sheets, photographs or graphics were copied.
- The Mapping 101 page marks its Sources/Usage as Public Domain; the Fact Sheet is a U.S. federal publication. Third-party materials linked from USGS pages are not assumed to share the same status. Independent cartographic/editorial review and Human View remain open. The slice remains HOLD.

The exact R9 inventory is now **99 records** across ten slices: four 9-record profiles, food systems 12 records, hydraulic engineering/cultural heritage/archival science/cartography 10 records each, and history of mathematics 11 records. The initial 31 generic Evidence Use records have been reduced by 24; **7 remain without claim-specific pinpoints** in food systems and settlement geography. No first-edition allowlist or decision was changed.

## Remaining R9 source-depth order

1. Food systems — pin FAO and World Bank sources separately; preserve the 12-record profile and its two-source/four-Claim structure.
2. Settlement geography — pin UN-Habitat methodology sections, grid classification, aggregation and national-definition boundaries.

All ten R9 slices remain HOLD pending item-level rights, independent domain editorial review, Human View and exact-head CI.
