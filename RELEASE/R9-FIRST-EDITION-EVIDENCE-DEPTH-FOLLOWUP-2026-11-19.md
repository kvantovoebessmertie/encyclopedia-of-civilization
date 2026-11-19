# R9 First-Edition Evidence-Depth Follow-up — 2026-11-19

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR workstream: #22, Work Package 1 — first-edition candidate selection  
Prior audit: `RELEASE/WAVE-9-SUBSTANTIVE-AUDIT-2026-10-03.md`  
Purpose: close part of the R9 non-blocking debt without repeating the completed R9 structural/Claim audit.

## Scope and duplicate control

The R9 audit already reviewed the ten domains' structure, Claim statements/provenance, safety boundaries and three cross-slice relations. It recorded non-blocking debt: content depth, independent-source triangulation, broader linkage and domain-specific editorial evidence.

This follow-up does **not** repeat those passes. It screens the exact current Source/Evidence Use graph, source specificity, claim-level locators, independent support needs and first-edition record inventory for the same ten R9 slices:

1. `history-of-medicine-basics`
2. `history-of-mathematics-basics`
3. `history-of-engineering-basics`
4. `cartography-basics`
5. `hydraulic-engineering-basics`
6. `food-systems-basics`
7. `cultural-heritage-basics`
8. `library-science-basics`
9. `archival-science-basics`
10. `settlement-geography-basics`

The R9 cross-slice links remain context links only. They do not constitute evidence, establish causality, or create a Claim dependency.

## Exact inventory

Nine slices currently use the 9-record profile (1 Source + 3 Claims + 3 Evidence Use + Context + Scope). The current `food-systems-basics` README explicitly defines a different profile: **2 Sources + 4 Claims + 4 Evidence Use + Context + Scope = 12 records**.

| Slice | Sources | Claims | Evidence Use | Context | Scope | Total |
|---|---:|---:|---:|---:|---:|---:|
| history-of-medicine-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| history-of-mathematics-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| history-of-engineering-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| cartography-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| hydraulic-engineering-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| food-systems-basics | 2 | 4 | 4 | 1 | 1 | 12 |
| cultural-heritage-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| library-science-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| archival-science-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| settlement-geography-basics | 1 | 3 | 3 | 1 | 1 | 9 |
| **Total** | **11** | **31** | **31** | **10** | **10** | **93** |

All inspected records are version 1, published and complete. Those states are not first-edition approval.

**Inventory reconciliation finding:** the R9 gap-map summary describes each of ten slices as a 9-record unit (90 records), while the current food-systems README and canonical records define a 12-record profile. The current content is internally coherent (two source-specific Claim/Evidence branches), but the R9 historical target/count must be reconciled with the later food-systems expansion. Do not delete or collapse the additional records to force the old count.

## Source and Evidence Use findings

### 1. history-of-medicine-basics — HOLD

- The current Source is a MeSH descriptor (“History of Medicine”), a controlled-vocabulary/collection-development reference, not a full historical evidence source.
- Claims A/B are supported more directly by the NLM Collection Development Guidelines, which define the field as study of past events, thought and practice and explain that medicine's boundaries change over time and that social, political, economic and religious context matters.
- Claim C's distinction between primary documents and interpretive literature needs a dedicated source-literacy/historical-methods reference.
- All three Evidence Use records are generic and have no exact locator.

Remediation target: normalize Source identity to the exact NLM guideline/MeSH resource; pin the definition/discussion sections; add a source-method locator for primary versus secondary evidence. Do not use the MeSH descriptor alone to substantiate all three Claims.

### 2. history-of-mathematics-basics — HOLD

- MacTutor's History Overview is a strong substantive source. It gives historical examples from Babylonia, Greece, India and Islamic societies and describes transmission of mathematical knowledge into Europe.
- Claims A/B are well aligned with the source. Claim C's warning against assigning an idea to one author/date is plausible but needs specific historical examples or a methodology source.
- All three Evidence Use records lack exact section/example locators; one source is not independent triangulation.

Remediation target: add precise MacTutor headings/periods/examples for A/B and a second independent scholarly/institutional source for C. Preserve the cross-cultural scope and avoid a linear single-civilization narrative.

### 3. history-of-engineering-basics — HOLD

- The Smithsonian Technology & Innovation page provides a broad portal to invention, technology, collections and stories, including specific engineering-related examples.
- Claims A/B are broadly compatible with the portal, but Claim B is a specific institutional-collection proposition and requires a named collection/story locator.
- Claim C's context-versus-causality boundary is methodological and is not directly established by a general Smithsonian topic page.
- All Evidence Use records are generic.

Remediation target: pin the exact Smithsonian collection/stories supporting A/B; add a specialist history-of-technology/engineering methodology source for C; distinguish artifact, invention, adoption, diffusion and social impact.

### 4. cartography-basics — HOLD

- USGS “Mapping 101” is a directly relevant source family for map purposes, topographic maps, contour lines, scale and map interpretation.
- Claims A–C appear well aligned with the subject and likely supportable from the page, but all Evidence Use records lack the exact heading/diagram/definition locator.
- USGS is a U.S. federal source; the basic cartographic concepts are general, but examples and conventions should not be treated as globally exhaustive.
- The R9 cartography ↔ settlement geography relation is a context link only.

Remediation target: pin the exact Mapping 101 headings for map representation, topographic symbols/contours and scale; add an independent cartographic source for international conventions or projection/distortion if later claims require them.

### 5. hydraulic-engineering-basics — HOLD

- The Source is a USACE Hydrology and Hydraulics page, relevant to water engineering and modeling.
- Claims B/C are plausible applications, but the current landing page is not a technical manual or a direct model-specific source. Claim A's distinction between hydrology and hydraulics requires a precise technical definition.
- All Evidence Use records are generic and have no manual, section, equation, model or application locator.
- Context and Scope do not explicitly exclude design calculations or operational flood-control decisions.

Remediation target: add direct USACE/USGS engineering manuals or standards for hydrology/hydraulics definitions and model applications; pin the exact chapters and limitations. Preserve the educational-only boundary; no engineering design or flood-risk instruction is authorized by this audit.

### 6. food-systems-basics — HOLD

- This is the only R9 slice with an explicit 12-record profile: two Sources, four Claims and four Evidence Use records.
- FAO's Agrifood Systems page directly describes the people, activities, investments and choices involved in producing and delivering food/agricultural goods, and the sequence from growing/harvesting through processing, packaging, transport, distribution, trade, purchase, preparation, consumption and disposal. This is strong direct support for Claims A–C.
- The World Bank “The Future of Food” page directly supports Claim D's extended chain: storage, processing, distribution, transport, logistics, retailing and other services.
- All four Evidence Use records remain generic and lack precise section/page locators. The two source branches are correctly distinct: A–C reference FAO; D references the World Bank Source.
- Context/Scope are more specific than the generic R9 boilerplate and correctly exclude current operational/policy/investment decisions.

Remediation target: pin the exact FAO definition and value-chain sequence for A–C; pin the World Bank “Story Highlights”/food-system value-chain passage for D. Preserve the 12-record profile and both independent source branches; reconcile the historical Gap Map count without dropping any record.

### 7. cultural-heritage-basics — HOLD

- UNESCO's Cultural Heritage topic page is a relevant institutional portal, but it is not a precise primary source for the three Claims.
- Claims A/B require exact references to the 1972 World Heritage Convention for tangible heritage and related UNESCO definitions; Claim C requires the 2003 Convention's definition of intangible cultural heritage, including knowledge, skills and practices recognized by communities.
- The current Source identity is generic and all Evidence Use records lack exact convention/article/paragraph locators.
- The claims should not imply that every community's heritage is defined only by UNESCO categories or that recognition is independent of community participation.

Remediation target: cite the 1972 and 2003 UNESCO conventions separately, with exact Articles 1–2 and 2 respectively where applicable; record the distinction between tangible and intangible heritage and the community-recognition requirement.

### 8. library-science-basics — HOLD

- IFLA's Access & Preservation page is directly relevant to access and preservation but is too narrow for the broader claims about collecting, organizing, service provision and information use.
- Claims A/C may be supported by IFLA access/preservation materials; Claim B needs direct support about library services and user needs.
- All Evidence Use records are generic and lack exact sections, policy statements or manifesto locators.
- The R9 library science ↔ archival science relation remains a contextual link, not proof that libraries and archives have identical functions.

Remediation target: add the IFLA-UNESCO Public Library Manifesto and relevant preservation statements; pin collection, access, services and digital preservation sections. Clarify the differences between library collections, archival fonds and other information institutions.

### 9. archival-science-basics — HOLD

- The Society of American Archivists' “Archives 101: Basic Principles” page directly describes appraisal, arrangement, description and preservation. It supports much of Claim A and the context/structure aspect of Claim C.
- Claim B (respect des fonds/provenance) and the full implications of original order need exact SAA/ICA archival principles and a pinpoint; the current page is a community-archives guide, not a comprehensive professional standard.
- All Evidence Use records are generic and lack exact subheading locators.
- Context/Scope do not identify ethical and legal access restrictions, privacy or donor restrictions.

Remediation target: pin the SAA page's appraisal, arrangement, description and preservation sections; add the ICA/archival principles for provenance and original order; include privacy, access restriction and community-archives context boundaries.

### 10. settlement-geography-basics — HOLD

- UN-Habitat's *Applying the Degree of Urbanisation* (2021) is a direct, methodologically specific source.
- Claims A/B/C align with the manual: a harmonized urban-rural continuum, categories of cities/towns/semi-dense/rural areas, and a method intended for international statistical comparison rather than replacing national definitions.
- The current Evidence Use records do not pin the exact manual sections. Claim B should cite the grid classification and settlement thresholds; Claim C should cite the manual's statement that it complements rather than replaces national statistical-office definitions.
- The R9 settlement geography ↔ cartography relation remains a contextual link only.

Remediation target: pin the 2021 manual's classification framework, grid-cell classification and small-spatial-unit aggregation sections (including §6.4); preserve the explicit non-replacement of national definitions.

## Cross-slice findings

1. **Evidence Use debt remains universal:** all 31 Evidence Use records lack precise page/section/article/paragraph locators. Generic descriptions identify a source family but not the material that supports the Claim.
2. **Independent triangulation:** each normal 9-record slice still relies on one Source. Food systems has two independent Source branches. The R9 audit accepted single-source introductory coverage as non-blocking debt; first-edition selection still requires stronger triangulation where claims are methodological, contested, high-consequence or broad.
3. **Source identity:** history of medicine uses a MeSH descriptor; history of mathematics has a substantive MacTutor overview; history of engineering uses a general Smithsonian portal; cartography uses USGS Mapping 101; hydraulic engineering uses a USACE topic page; cultural heritage uses a UNESCO topic portal; library science uses IFLA access/preservation; archival science uses SAA Archives 101; settlement geography uses a specific UN-Habitat methodology manual.
4. **Food systems structure:** the current README explicitly documents 2 Sources → 4 Claims → 4 Evidence Use → Context → Scope. This is a deliberate 12-record profile, not an error to be reduced to nine. The R9 historical count must be reconciled to this current profile.
5. **Cross-slice links:** the three R9 relations remain contextual links only. They do not create evidence or causal claims.
6. **Rights and editorial:** source rights are item-specific; no rights clearance is asserted. The NLM historical collections include third-party material; Smithsonian linked collections have separate rights; FAO and World Bank works have source-specific reuse terms; UNESCO/IFLA/SAA materials require exact item-level checks.
7. **Selection:** all ten slices remain HOLD. Existing published/complete states and the earlier R9 “clean with non-blocking debt” audit do not automatically establish first-edition eligibility.

## Group result

**93/93 current records screened; 0 INCLUDE / 10 HOLD / 0 EXCLUDE.**

This is a first-edition evidence-depth follow-up to the R9 audit, not a re-run of the prior R9 structural/Claim pass. No canonical JSON, Source, Claim, Evidence Use, Context or Scope version was changed. No publication state, completion state, allowlist or release decision was changed. No main-branch change, merge, deployment or release action was performed.

## Next work under the first-edition plan

1. Reconcile the R9 historical target/count with the current 12-record food-systems profile; preserve both World Bank and FAO evidence branches.
2. Authorize only bounded Evidence Use/source-identity corrections after exact locators and rights conditions are established.
3. Prioritize NLM history-of-medicine direct sources, Smithsonian history-of-engineering collection locators, USACE technical manual sections, UNESCO convention Articles, IFLA library-service sources and SAA/ICA provenance standards.
4. Keep all ten slices HOLD until independent-source needs, rights, domain editorial review, Human View and exact-head CI are closed.
5. Continue to the next Gap Map family only after the R9 inventory discrepancy and source-depth debt are recorded in the candidate register.

## Source references consulted

- NLM, “History of Medicine” definition and scope: https://www.ncbi.nlm.nih.gov/sites/books/NBK518766/
- NLM, “The Story of NLM Collections”: https://www.nlm.nih.gov/hmd/about/collection-history.html
- MacTutor, “An overview of the history of mathematics”: https://mathshistory.st-andrews.ac.uk/HistTopics/History_overview/
- Smithsonian, “Explore Technology & Innovation”: https://www.si.edu/explore/technology
- USGS, “Mapping 101”: https://www.usgs.gov/science/science-explorer/maps-and-mapping/mapping-101
- USACE, “Hydrology and Hydraulics”: https://www.nws.usace.army.mil/Missions/Civil-Works/Engineering/Hydrology-and-Hydraulics/
- FAO, “Agrifood Systems”: https://www.fao.org/food-systems/en
- World Bank, “The Future of Food”: https://www.worldbank.org/en/topic/agriculture/publication/the-future-of-food-shaping-the-global-food-system-to-deliver-improved-nutrition-and-health
- UNESCO, “Cultural Heritage”: https://www.unesco.org/en/query-list/c/cultural-heritage
- IFLA, “Access & Preservation”: https://www.ifla.org/access-preservation/
- Society of American Archivists, “Archives 101: Basic Principles”: https://www2.archivists.org/groups/diverse-sexuality-and-gender-section/information-for-community-archives-archives-101-basic-principles
- UN-Habitat, *Applying the Degree of Urbanisation* (2021): https://unhabitat.org/knowledge/publications/applying-the-degree-of-urbanisation-a-methodological-manual-to-define-cities-towns-and-rural-areas


## Subsequent bounded remediation — 2026-11-19

After the 93-record audit snapshot, the first three priority slices were remediated under `R9-EVIDENCE-DEPTH-REMEDIATION-001`:

- `history-of-medicine-basics`: all 9 records advanced v1→v2; NLM Collection Development Guidelines locators added; Claim C narrowed to the NLM-supported role of interpretive, analytical and biographical secondary literature.
- `history-of-engineering-basics`: all 9 records advanced v1→v2; Smithsonian story/object locators added; Claims narrowed to the documented examples on the Smithsonian Technology & Innovation page.
- `library-science-basics`: all 9 records advanced v1→v2; IFLA-UNESCO Public Library Manifesto 2022 locators added; Claims narrowed to public-library missions.

The R9 inventory remains **93 canonical records**: 27 records are now v2 and 66 remain v1. The register was updated to the exact current versions. All ten slices remain HOLD; the 27 v2 records are not first-edition approvals.

The initial audit found 31 Evidence Use records without pinpoint locators. The nine Evidence Use records in these three remediated slices now contain claim-specific locators; **22 Evidence Use records remain without pinpoint locators** across the other seven slices. This updated count does not include the separate 12-record food-systems profile discrepancy, which remains reconciled at 93 total records and must not be collapsed to 90.

### Updated next work order

1. Continue with `hydraulic-engineering-basics`: identify and pin USACE HEC-RAS/HEC-HMS technical references; do not add design or flood-operation instructions.
2. Continue with `cultural-heritage-basics`: keep the 1972 World Heritage Convention and 2003 Intangible Cultural Heritage Convention as distinct sources; preserve community recognition, consent and cultural-protocol boundaries.
3. Continue with `archival-science-basics`: use ICA/SAA standards for provenance, original order, appraisal, description and preservation; add privacy, donor and access restrictions.
4. Then address the remaining history-of-mathematics, cartography, food-systems, settlement-geography and other R9 evidence-depth items in the documented order.
5. Keep all slices HOLD until rights, independent editorial/Human View and exact-head CI are closed.


## Subsequent hydraulic engineering remediation — 2026-11-19

The next R9 priority slice, `hydraulic-engineering-basics`, was remediated under `R9-HYDRAULIC-ENGINEERING-REMEDIATION-001`:

- Existing Source v1→v2 now identifies the USACE HEC-RAS Hydraulic Reference Manual v6.5.
- One additional Source `SRC-HYDRAULIC_ENGINEERING-HMS@1` was added for the USACE HEC-HMS Application Guide.
- Claims A–C, Evidence Use A–C, Context and Scope were versioned v1→v2. Claim A distinguishes watershed hydrologic modelling from hydraulic modelling needs; Claim B describes bounded HEC-RAS 1D/2D capability; Claim C describes the use of hydrologic runoff outputs as inputs to hydraulic/consequence models.
- The slice now has 10 records (2 Sources + 3 Claims + 3 Evidence Use + Context + Scope), an explicit source-depth expansion. The exact-version register now contains **94 records** across the ten R9 slices: eight 9-record profiles, food systems at 12 records, and hydraulic engineering at 10 records.
- All ten R9 slices remain HOLD. No publication state or allowlist was changed.

The R9 evidence-depth follow-up initially found 31 generic Evidence Use records; the first three slice remediations corrected nine, and the hydraulic package corrected three more. **19 Evidence Use records remain without claim-specific pinpoint locators** across the other six slices. The cross-slice relation updates are maintained separately from the 94-record vertical-slice inventory.

### Updated next work order

1. Continue with `cultural-heritage-basics`, maintaining separate 1972 and 2003 UNESCO Convention sources and community-consent/cultural-protocol boundaries.
2. Continue with `archival-science-basics`, using ICA/SAA standards for provenance, original order, appraisal, description and preservation, with privacy/donor/access restrictions.
3. Continue with `history-of-mathematics-basics`, `cartography-basics`, `food-systems-basics` and `settlement-geography-basics` according to the remaining source-depth register.
4. Keep all slices HOLD until rights, independent editorial/Human View and exact-head CI are closed.


## Subsequent cultural heritage remediation — 2026-11-19

The next R9 priority slice, `cultural-heritage-basics`, was remediated under `R9-CULTURAL-HERITAGE-REMEDIATION-001`:

- Source v1→v2 now identifies the 1972 UNESCO World Heritage Convention (Articles 1 and 3).
- Added a separate Source `SRC-CULTURAL_HERITAGE-ICH@1` for the 2003 UNESCO Intangible Cultural Heritage Convention (Article 2(1)).
- Claims A/B and Evidence Use A/B now point to the 1972 instrument; Claim C and Evidence Use C point to the 2003 instrument. Claims, Evidence Use, Context and Scope are v2.
- The slice now has 10 records; the exact R9 inventory is **95 records**: seven 9-record profiles, food systems 12, hydraulic engineering 10 and cultural heritage 10.
- All ten R9 slices remain HOLD. The added Source is a controlled evidence-depth expansion, not a first-edition approval.

The initial 31 Evidence Use records without pinpoint locators have been reduced by 15 across the three NLM/Smithsonian/IFLA slices, hydraulic engineering and cultural heritage. **16 Evidence Use records remain without pinpoint locators** in the remaining five slices. The two additional Sources in hydraulic engineering and cultural heritage are separately registered; the historic 90-record target is not used to justify deleting them.

### Updated next work order

1. Continue with `archival-science-basics`: align ICA/SAA sources for appraisal, arrangement, provenance, original order, description and preservation; preserve privacy, donor, access and community-archive boundaries.
2. Continue with `history-of-mathematics-basics`, `cartography-basics`, `food-systems-basics` and `settlement-geography-basics` in the documented source-depth order.
3. Keep all ten slices HOLD until item-level rights, independent editorial/Human View and exact-head CI are closed.


## Subsequent archival science remediation — 2026-11-19

The next R9 priority slice, `archival-science-basics`, was remediated under `R9-ARCHIVAL-SCIENCE-REMEDIATION-001`:

- Existing Source v1→v2 now identifies the Society of American Archivists “Archives 101: Basic Principles” page and exact processing/provenance locators. Its community-archives and preliminary-draft status is explicitly retained.
- Added `SRC-ARCHIVAL_SCIENCE-ICA@1` for ICA ISAD(G), Second Edition, with the provenance glossary and multilevel-description locators.
- Claims A/B and Evidence Use A/B map to the SAA page; Claim C and Evidence Use C map to ICA ISAD(G). Claims A–C, Evidence Use A–C, Context and Scope are v2.
- Context and Scope now distinguish the community-archives guide from the international descriptive standard and explicitly retain privacy, donor, access-restriction and cultural-sensitivity boundaries.
- The slice now has 10 records (2 Sources + 3 Claims + 3 Evidence Use + Context + Scope). The exact R9 inventory is **96 records**: six 9-record profiles, food systems 12 records, and hydraulic engineering, cultural heritage and archival science 10 records each.
- All ten slices remain HOLD. The additional ICA Source is a bounded source-depth expansion, not a first-edition approval.

The original 31 generic Evidence Use records have now been reduced by 18 across the three NLM/Smithsonian/IFLA slices, hydraulic engineering, cultural heritage and archival science. **13 Evidence Use records remain without claim-specific pinpoint locators** across history of mathematics, cartography, food systems and settlement geography. All 10 R9 slices remain HOLD pending item-level rights, independent editorial/Human View and exact-head CI.

### Updated next work order

1. Continue with `history-of-mathematics-basics`: add exact historical-example locators and independent scholarly/institutional support for Claim C; preserve cross-cultural scope and avoid a linear single-civilization narrative.
2. Continue with `cartography-basics`: pin USGS Mapping 101 headings/definitions/diagrams and retain explicit U.S.-example versus global-convention boundaries.
3. Continue with `food-systems-basics`: pin the FAO and World Bank passages separately; preserve the 12-record, two-source/four-Claim profile.
4. Continue with `settlement-geography-basics`: pin UN-Habitat methodology sections, grid classification, aggregation and national-definition boundary.
5. Keep all ten slices HOLD until item-level rights, independent editorial/Human View and exact-head CI are closed.
