# Domain audit — maps, navigation and geographic coordinates

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR: #22  
Audited source revision: `56e44ac9480e4c48d2c1748d942eceaf509a7be2`  
Disposition: **HOLD — two slices screened; no canonical records changed**

## Scope and method

Exact version-1 records were read from both slice directories. The screen covered all listed Claim, Evidence Use, Source, Context and Scope records, including the additional OGC Evidence Use and Source in geographic-coordinates-basics. External source passages were checked against the actual Claim statements. This is a content/evidence screen, not an INCLUDE decision or authorization to rewrite canonical records.

## 87. maps-and-navigation-basics — 9 records

Records:
- `CLM-MAPS_AND_NAVIGATION_BASICS-A/B/C@1`
- `EU-MAPS_AND_NAVIGATION_BASICS-A/B/C@1`
- `SRC-MAPS_AND_NAVIGATION_BASICS@1`
- `CTX-MAPS_AND_NAVIGATION_BASICS@1`
- `SCP-MAPS_AND_NAVIGATION_BASICS@1`

Source: USGS, “Finding Your Way With Map and Compass”  
https://www.usgs.gov/educational-resources/finding-your-way-map-and-compass

Findings:
- Claim A (topographic maps show object locations, distances and terrain features): **directly supported**. USGS says topographic maps locate natural/man-made features, show distance and direction, and describe land shape. The educational page and linked fact sheet also describe contours and elevation.
- Claim B (map scale relates map distance to ground distance): **directly supported**. USGS explicitly defines scale as the ratio between a map measurement and the corresponding ground distance.
- Claim C (navigation conclusions depend on map quality, scale, data currency and field conditions): **only partially supported** by the linked USGS material. Scale and compass/map use are covered, but the complete set of stated dependencies—especially data currency and conditions on the ground—is not established by the current source/EU. Do not treat this as fully evidenced.

Evidence defects:
- All three EUs use the same generic source description and provide no claim-specific section, passage or locator.
- Context and Scope target Claim A only. They cannot be presumed to govern Claims B and C.
- The source is a useful introductory fact sheet, but it is not sufficient by itself to substantiate every dependency in Claim C.

Decision: **HOLD.** Claims A and B are conceptually sound; all three EUs need precise claim-specific locators. Claim C needs additional authoritative evidence or narrower wording through an authorized versioned correction. Preserve existing Claims unless the authorized editor decides a substantive change is required.

## 88. geographic-coordinates-basics — 11 records

Records:
- `CLM-GEOGRAPHIC_COORDINATES_BASICS-A/B/C@1`
- `EU-GEOGRAPHIC_COORDINATES_BASICS-A/B/C@1`
- `EU-GEOGRAPHIC_COORDINATES_OGC@1`
- `SRC-GEOGRAPHIC_COORDINATES_BASICS@1`
- `SRC-OGC-COORDINATE-REFERENCE-SYSTEMS@1`
- `CTX-GEOGRAPHIC_COORDINATES_BASICS@1`
- `SCP-GEOGRAPHIC_COORDINATES_BASICS@1`

Sources:
- Existing USGS reference: https://www.usgs.gov/educational-resources/27-ideas-teaching-topographic-maps-0
- Open Geospatial Consortium, Abstract Specification Topic 2, “Referencing by coordinates” (version 5.0, published 2019-02-08): https://docs.ogc.org/as/18-005r4/18-005r4.html

Findings:
- Claim A (geographic coordinates specify the position of objects on Earth's surface): **conceptually supported** by the OGC coordinate-reference framework, but the current USGS source identity is generic and its linked teaching resource is not a sufficiently precise locator for this proposition.
- Claim B (latitude and longitude form a coordinate system for locating positions): **directly supportable** through OGC §3.1.23, §3.1.32–3.1.35, which define ellipsoidal/geographic coordinate systems and geodetic latitude/longitude. The current EU points only to the generic USGS source, not the OGC source.
- Claim C (coordinate accuracy and CRS choice depend on task and required spatial precision): **partially supported** by OGC's scope and definitions of coordinate reference systems, coordinate operations, metadata and dynamic reference frames. The current statement is broad; it needs a precise locator and a more carefully bounded formulation distinguishing coordinate-system choice, datum/reference frame, coordinate epoch and accuracy requirements.

Evidence defects:
- The three base EUs use generic descriptions with no section or pinpoint.
- The additional OGC EU correctly links Claim C to the OGC Source, but its description remains high-level and does not identify the specific clauses.
- Context and Scope target Claim A only; they do not establish boundaries for Claims B or C.
- The USGS source URL is a teaching-resource page about topographic maps; it is not an adequate sole source for all three coordinate-system Claims.
- OGC is an authoritative technical standard, but its copyright notice and additional-rights statement must be respected. This screen relies on factual propositions and pinpoint references, not reproduction of standard text.

Useful exact OGC locations for an authorized EU correction:
- §1, scope: coordinate reference systems and coordinate operations, including spatial systems and time-dependent systems.
- §3.1.5: coordinate.
- §3.1.23: ellipsoidal/geodetic coordinate system.
- §3.1.32–3.1.35: geodetic latitude, geodetic longitude, geodetic reference frame and geographic coordinate reference system.
- §3.1.19–3.1.20: dynamic coordinate reference system and dynamic reference frame.

Decision: **HOLD.** The basic concepts are valid, but source-to-Claim mapping and pinpoint evidence are incomplete. Use OGC as the direct technical source for the relevant coordinate-system Claims through an authorized versioned correction; retain a suitable USGS source only for map-based practical illustration. Do not silently transfer the OGC EU to Claims A/B without explicit authorized linkage.

## Cross-slice and integrity checks

- The two slices are adjacent subject areas but no new Relation is justified solely by topical proximity.
- No duplicate or unsupported Relation was created.
- All inspected records were version 1 and their local Claim → EU → Source references resolved to the corresponding listed version.
- Context/Scope targeting was checked per record; neither pair is treated as governing sibling Claims.
- No canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON was edited.
- No publication status, allowlist, preview, release inclusion or branch protection setting was changed.
- `main` was not changed. PR #22 remains Draft.

## Group result

| Slice | Records screened | Main finding | Decision |
|---|---:|---|---|
| maps-and-navigation-basics | 9 | A/B supported; C only partial; EUs lack pinpoints | HOLD |
| geographic-coordinates-basics | 11 | OGC supports core terminology; EUs and source mapping need pinpoints | HOLD |

Next inventory sequence after these slices: telecommunications-basics, networks-basics, public-risk-communication-basics, transportation-basics, public-transport-basics and infrastructure-basics.
