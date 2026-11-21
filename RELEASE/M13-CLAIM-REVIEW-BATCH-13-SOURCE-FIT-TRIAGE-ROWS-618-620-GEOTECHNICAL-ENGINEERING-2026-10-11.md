# M13 Batch 13 — source-fit triage (rows 618–620): geotechnical engineering

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; FHWA topic fit is strong, but canonical Evidence Use records are boilerplate and lack claim-specific pinpoints**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). Scores below are provisional triage estimates, not finalized ledger scores. Canonical Claim/Evidence Use/Source JSON remains unchanged.

## Source trail

The three Claims reference `SRC-GEOTECHNICAL_ENGINEERING_BASICS@1`, which points to the Federal Highway Administration (FHWA) geotechnical engineering topic page:
https://www.fhwa.dot.gov/engineering/geotech/

The source is a topical landing page, not a single claim-level technical passage. The FHWA “Subsurface Investigation” page identifies methods for subsurface characterization including in-situ tests, geophysical tests, and laboratory test selection to establish soil and rock design/construction parameters:
https://www.fhwa.dot.gov/engineering/geotech/subsurface/

Further direct topical support is available in FHWA's *Geotechnical Site Characterization* (GEC 5, FHWA-NHI-16-072), particularly Chapter 10 on groundwater conditions and hydraulic properties:
https://www.fhwa.dot.gov/engineering/geotech/pubs/nhi16072.pdf

The existing three Evidence Use records all contain the generic description “Источник используется в пределах заявленного материала.” None records a specific section, chapter, page, table, or claim-specific support. Thus the public source can be assessed for fit, but the canonical evidence chain is not yet release-grade.

## 1. `CLM-GEOTECHNICAL_ENGINEERING_BASICS-A` — provisional **D2 / E3 / B2**

**Claim:** “Geotechnical engineering applies knowledge of soil and rock behavior to the design and performance of infrastructure.”

**Assessment:** This is a compact introductory definition and does not explain characterization methods, uncertainty, or the range of engineering applications (D2). FHWA's geotechnical engineering topic and subsurface-investigation guidance directly connect soil/rock characterization and engineering parameters to design and construction (E3). The wording is broad but appropriately avoids claiming that soil and rock behavior alone determines infrastructure performance (B2).

**Disposition:** Strong candidate to retain provisionally. Add a pinpoint to the FHWA geotechnical engineering overview or a relevant introductory section of a technical FHWA manual; replace the boilerplate Evidence Use description with a claim-specific summary.

## 2. `CLM-GEOTECHNICAL_ENGINEERING_BASICS-B` — provisional **D2 / E3 / B2**

**Claim:** “Site characterization provides information about subsurface materials and conditions needed to support engineering decisions.”

**Assessment:** The claim captures the purpose but does not distinguish investigation, interpretation, and design use (D2). FHWA's Subsurface Investigation page explicitly covers subsurface exploration methods and the establishment of soil/rock design and construction parameters; GEC 5 describes characterization of groundwater and soil/rock properties for design and construction (E3). The wording “needed to support” is appropriately bounded: it does not say site characterization removes uncertainty or guarantees a safe design (B2).

**Disposition:** Strong source fit. Pinpoint the FHWA Subsurface Investigation description and/or GEC 5's site-characterization objectives in Evidence Use.

## 3. `CLM-GEOTECHNICAL_ENGINEERING_BASICS-C` — provisional **D2 / E2 / B2**

**Claim:** “Foundation and earthwork behavior depends on material properties, groundwater conditions, loading, geometry, and construction conditions.”

**Assessment:** The list is a useful introductory synthesis but does not explain the interaction between factors or specify which behaviors (settlement, bearing capacity, stability, seepage, etc.) are in scope (D2). FHWA references support soil/rock properties, groundwater and construction conditions, and design-related subsurface profiles. However, the current source record points only to a broad landing page, while the Evidence Use is generic; it does not pinpoint one source passage that directly substantiates the entire list (E2). The statement is appropriately non-numeric and avoids predicting outcomes without site-specific investigation, but “geometry” and “loading” should be pinned to a foundation/design source rather than assumed from the landing page (B2).

**Disposition:** Retain provisionally; strengthen the evidence trail with a technical foundation/earthwork source passage that directly names loading and geometry, and add a pinpoint for groundwater and construction conditions.

## Batch accounting

- Individual Claims reviewed in this note: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Canonical Evidence Use records with exact claim-specific pinpoints: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.

## Relation to the earlier mislabelled report

The separate file `M13-CLAIM-REVIEW-BATCH-13-SOURCE-FIT-TRIAGE-ROWS-618-620-GEODESY-2026-10-11.md` assesses geodesy Claims from rows 591–593 despite its filename. It is not evidence for these three geotechnical-engineering rows. This report reviews the actual inventory rows 618–620 and corrects the worklist accounting without overwriting the earlier artifact.
