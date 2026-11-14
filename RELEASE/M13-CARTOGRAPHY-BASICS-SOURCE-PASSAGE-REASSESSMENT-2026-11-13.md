# M13 — cartography basics: source-passage reassessment

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Records: `CLM-CARTOGRAPHY-A/B/C@1`, `EU-CARTOGRAPHY-A/B/C@1`, `SRC-CARTOGRAPHY@1`
Status: **source-passage desk review and bounded Source/EU proposal; no canonical record or D/E/B score changed.**

## 1. Current canonical chain and source fit

All three Claims and Evidence Uses are version 1 and point to `SRC-CARTOGRAPHY@1`. Each EU contains a generic description with no exact section/paragraph locator.

The Source is identified as “U.S. Geological Survey — Mapping 101” and points to:
https://www.usgs.gov/science/science-explorer/maps-and-mapping/mapping-101

The current page contains a short introductory explanation of maps and cartography, but it is also a broad USGS landing page with multiple map collections, products, FAQs and publications. It is not the best single locator for the three specific propositions. The page itself marks its sources/usage as Public Domain.

## 2. Claim-level passage review

### Claim A — `CLM-CARTOGRAPHY-A@1`

Claim: “Картография занимается созданием и использованием карт для представления пространственной информации.”

Current USGS “Mapping 101” passage:
- “Why a map?” explains that a map is a representation of a particular area.
- The following paragraph defines cartography as the science of making maps and describes USGS scientists making and using maps to represent and understand geographic data and natural resources.
- Locator: “Mapping 101”, “Why a map?” paragraph, lines/paragraphs immediately following the heading.

Assessment:
- Direct support for the core proposition.
- Precision: “spatial information” is an appropriate general summary of maps representing geographic data; the source example is USGS and U.S. natural resources, not a complete definition of all cartographic methods or applications.
- Passage status: **DIRECT**.
- Rights: page indicates Public Domain.

### Claim B — `CLM-CARTOGRAPHY-B@1`

Claim: “Топографические карты используют условные обозначения и горизонтали для представления природных и созданных человеком объектов и рельефа.”

Direct USGS passage:
- “US Topo Cartographic Specifications — Map Symbol Guide”, “Symbols on US Topo maps”: features are represented as points, lines and polygons using colors/patterns; examples include roads, rivers, boundaries, structures and hydrography.
- The same section defines contours as lines joining points of equal elevation and explains that they reveal land shape and slope.
- “Topographic Mapping”, “What is a Topographic Map?” separately says topographic maps show both natural and manmade features and use contours to portray land shape/elevation.

Assessment:
- Direct support for both symbols and contours, including natural and human-made feature classes and relief.
- Precision: symbols are standardized within specific map products/series, but symbol sets may evolve and differ across products; do not imply every topographic map worldwide uses one identical legend.
- Proposed locators:
  - USGS, “US Topo Cartographic Specifications — Map Symbol Guide”, “Symbols on US Topo maps”: https://www.usgs.gov/ngp-standards-and-specifications/us-topo-map-symbol-guide
  - USGS, “Topographic Mapping”, “What is a Topographic Map?”: https://www.usgs.gov/educational-resources/topographic-mapping
- Passage status: **DIRECT, with map-series boundary note**.
- Rights: USGS pages identify relevant map/media content as Public Domain.

### Claim C — `CLM-CARTOGRAPHY-C@1`

Claim: “Масштаб карты задаёт отношение между расстоянием на карте и соответствующим расстоянием на местности.”

Direct USGS passage:
- “Finding Your Way With Map and Compass”, Introduction: states that maps are made to scale and that scale is a ratio between a unit of measurement on the map and the actual distance that same unit represents on the ground; gives a numerical example.
- Locator: Introduction, paragraph beginning “Maps are made to scale…”.
- URI: https://www.usgs.gov/educational-resources/finding-your-way-map-and-compass

Assessment:
- Direct support for the definition.
- Precision: a scale is a ratio between corresponding map and ground distances; units must be expressed consistently when calculating the representative fraction.
- Passage status: **DIRECT**.

## 3. Source identity and rights treatment

The current `SRC-CARTOGRAPHY` should remain a source for the USGS “Mapping 101” page only. It should not be treated as a stand-in for the separate Map Symbol Guide or Finding Your Way fact sheet.

If separately authorized, add distinct Source records for:
1. USGS, “US Topo Cartographic Specifications — Map Symbol Guide”.
2. USGS, “Topographic Mapping” (use the page's specific “What is a Topographic Map?” passage; note that the page labels its online edition as historical reference, so prefer the current Map Symbol Guide for core support).
3. USGS, “Finding Your Way With Map and Compass”.

The relevant pages identify public-domain use for the USGS material reviewed. Retain issuing organization, exact title, URL, access date and the specific product context. Do not infer that every third-party image or linked map layer on a USGS page is public domain merely because the surrounding page is; check item-level media/source notices.

## 4. Proposed Evidence Use remediation

If separately authorized:
- Claim A: create a versioned EU pinpointing “Mapping 101” / “Why a map?” and the cartography definition paragraph.
- Claim B: create a versioned EU pinpointing the US Topo Map Symbol Guide sections “Symbols on US Topo maps” and contour explanation; optionally a separate EU for the “What is a Topographic Map?” section.
- Claim C: create a versioned EU pinpointing the “Maps are made to scale…” paragraph in “Finding Your Way With Map and Compass”.
- Keep all Sources distinct; do not attach the map-scale fact sheet or map-symbol guide to the existing Source ID.
- Preserve U.S. USGS product context where relevant; do not generalize product-specific symbology to every national mapping authority.
- Run Claim/EU/Source linkage, source identity, offline edition and release-conformance regressions.

## 5. Disposition

| Claim | Passage result | Current canonical locator | Status |
|---|---|---|---|
| A | Direct | Missing | HOLD |
| B | Direct, product/series boundary note | Missing | HOLD |
| C | Direct | Missing | HOLD |

- Generic EU records reviewed: 3/3.
- Source fit issue: one broad Mapping 101 page is not a sufficient pinpoint for all three claims.
- Canonical Evidence Use locators added: 0.
- New Source records added: 0.
- Canonical Claim/EU/Source records changed: 0.
- Historical D/E/B assessments changed: 0.
- Independent cartography specialist review, Human View and publication clearance: 0.

All three Claims remain **HOLD** pending authorized versioned Source/EU registration and regression coverage. This is a desk review, not independent specialist certification or release approval.
