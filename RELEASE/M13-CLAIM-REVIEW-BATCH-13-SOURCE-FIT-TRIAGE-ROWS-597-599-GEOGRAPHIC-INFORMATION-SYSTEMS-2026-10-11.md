# M13 Batch 13 — Source-fit and identifier triage (rows 597–599): geographic information systems

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional triage; Claims A/B have strong topical fit, Claim C is broader than the linked source**

Scoring rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). These are provisional audit notes, not finalized scored-ledger rows. No canonical JSON changed.

## Source trail and identifier check

The Claim and Evidence Use records reference `SRC_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS` (record file `SRC-GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS.json`) with locator https://www.usgs.gov/programs/national-geospatial-program/geographic-information-systems-gis. The exact locator was not accessible through the current page check. A current USGS GIS educational resource at https://www.usgs.gov/centers/wetland-and-aquatic-research-center/science/usgs-geographic-information-systems-gis provides directly relevant definitions and examples: GIS manipulates, analyzes, and displays geographic data in a digital map; multiple datasets/layers can be combined; and spatial data can be vector or raster. USGS's GIS dataset review checklist also emphasizes checking precision, projection, datum, attributes, missing values, and data quality constraints.

**Identifier issue:** the three Claim JSON file names use hyphenated IDs, e.g. `CLM-GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS-A.json`, while each record's internal `record_id` and its EU `claim_ref.record_id` use underscores, e.g. `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_A`. The same underscore convention appears in EU and Source internal IDs. These are not byte-for-byte identical file-stem and internal identifiers. Do not assume a harmless alias: record it for the ID/linkage reconciliation pass and verify all consumers resolve it consistently.

## 1. `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_A` — **D2 / E3 / B2**

**Claim:** “A geographic information system manages, analyzes, and displays information associated with locations on Earth.”

**Assessment:** The claim names the main functions of GIS, but offers little detail about data structures or analytical workflow (D2). The USGS definition explicitly says GIS manipulates, analyzes, and displays geographic data in a digital computer-based map, directly supporting the core statement (E3). The phrase “information associated with locations on Earth” is a reasonable summary, but the current Evidence Use contains no pinpoint and the stored source locator needs to be rechecked (B2).

**Disposition:** Source content fits. Resolve the stored locator and add an exact section/quote to Evidence Use during an authorized content-editing pass. Reconcile filename/internal-ID aliases.

## 2. `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_B` — **D2 / E3 / B2**

**Claim:** “GIS work can combine spatial data with descriptive attributes to support mapping and analysis.”

**Assessment:** This describes a central GIS capability but does not explain data models or how attributes affect analysis (D2). The USGS page describes geographic data in GIS, vector features with attributes, and combining multiple datasets/layers to understand relationships; the linked USGS GIS review guidance also treats attributes and metadata as core data properties. That directly supports the core statement (E3). The Evidence Use is generic, with no pinpoint or explicit indication of which part supports “descriptive attributes” (B2).

**Disposition:** Retain provisionally; add a source-specific pinpoint. Reconcile filename/internal-ID aliases.

## 3. `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_C` — **D2 / E2 / B2**

**Claim:** “GIS results depend on the quality, scale, coordinate reference, completeness, and suitability of the underlying data.”

**Assessment:** This is a useful data-quality warning, but it does not explain the direction or mechanism of each dependency (D2). The USGS GIS dataset review checklist directly supports the importance of precision, projection/datum, attributes, missing or nonsensical values, and data-quality constraints. Scale and suitability are plausible but need a pinpointed source or narrower wording; the exact stored source locator itself also needs verification (E2). The claim appropriately signals dependence on input data but does not define how a user should evaluate these factors (B2).

**Disposition:** Keep provisional. Add a specific source for scale/suitability or narrow the list to factors explicitly documented by the selected USGS sources. Reconcile filename/internal-ID aliases.

## Batch accounting

- Individual Claims triaged in this checkpoint: **3**.
- Source content match: strong for A/B; partial for C.
- Identifier reconciliation issue: filename stem uses hyphens, internal Claim/EU/Source IDs use underscores.
- Stored source locator: needs revalidation; alternate current USGS resource inspected for topical comparison.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
