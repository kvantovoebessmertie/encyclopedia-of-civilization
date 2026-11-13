# MVP GIS Candidate Remediation — source-to-claim pinpoint map

Date: 2026-10-11  
Canonical corpus revision: `203a7028e08da394fd44630fe38727be07bc8849` (`main`)  
Status: **remediation note only — all three GIS candidates remain HOLD**

## Verified current source

The current USGS educational resource is:

`https://www.usgs.gov/centers/wetland-and-aquatic-research-center/science/usgs-geographic-information-systems-gis`

The page has an explicit “What is GIS?” section defining GIS as technology to manipulate, analyze and display geographic data in digital maps. It has a “GIS Data Types” section describing vector and raster data, followed by an explanation that multiple datasets/layers can be combined in one map. It also labels some media “Sources/Usage: Public Domain”; this label applies to the specific identified media, not automatically to every asset on the page. Source checked: https://www.usgs.gov/centers/wetland-and-aquatic-research-center/science/usgs-geographic-information-systems-gis

The canonical Source record currently stores a different locator:
`https://www.usgs.gov/programs/national-geospatial-program/geographic-information-systems-gis`
The canonical record must not be silently rewritten as part of screening. The chosen authoritative URL and any record repair require an explicit reviewed change.

## Claim-specific map

| Candidate | Current proposition | Evidence available from current USGS page | Remaining gap |
|---|---|---|---|
| GIS-A — `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_A@1` | GIS is a computer-based system for working with geographically located information | “What is GIS?” section; definition and purpose | Confirm exact wording in the canonical Claim and add direct section/paragraph pinpoint to Evidence Use |
| GIS-B — `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_B@1` | GIS can combine spatial data and descriptive attributes/layers | “GIS Data Types” plus multiple-datasets/layers paragraph | “Descriptive attributes” must be explicitly supported or removed/narrowed; identify precise paragraph |
| GIS-C — `CLM_GEOGRAPHIC_INFORMATION_SYSTEMS_BASICS_C@1` | Data quality, scale, accuracy and provenance constrain analysis | Page gives a general GIS introduction and data types | This page does not directly establish the full list; use a technical data-quality source or narrow the Claim to what the selected evidence directly supports |

## Rights and attribution

USGS page: https://www.usgs.gov/centers/wetland-and-aquatic-research-center/science/usgs-geographic-information-systems-gis  
USGS general copyright guidance: https://www.usgs.gov/faqs/are-usgs-reportspublications-copyrighted

For this candidate set, prefer short factual paraphrases, credit “U.S. Geological Survey (USGS),” and link to the exact source section. Do not copy page imagery, embedded media, or third-party material unless its specific rights statement has been checked. A page-level “Public Domain” note for an individual media item is not a blanket license for every element on the page.

## Decision and gates

- GIS-A, GIS-B, GIS-C remain **HOLD**.
- No canonical Claim, Evidence Use or Source JSON changed.
- No real-record preview allowlist was created.
- The reader must remain on synthetic fixtures until an explicit exact-version allowlist, exact evidence pinpoints, rights/attribution checks, rendered navigation, Human View and named editorial approval are recorded.
- This document maps remediation work; it is not a publication approval or a legal determination.
