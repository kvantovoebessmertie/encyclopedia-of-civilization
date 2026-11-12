# M13 thematic source-passage review — Geographic Coordinates Basics — 2026-11-12

## Status and boundary

Reviewed the three Claims and all four Evidence Use records in `geographic-coordinates-basics` against the exact M13 branch content at parent revision `3900b9f3576426ecdf23af0b64f2b777bd5da38c`.

**Disposition: all three Claims remain HOLD.** The review found a material Source identity/scope defect: `SRC-GEOGRAPHIC_COORDINATES_BASICS@1` is described as an authoritative source for geographic coordinates, but its URI points to a USGS teaching-ideas page about topographic maps, not to a definitional geographic-coordinate reference. The existing three Evidence Uses are generic and do not identify passages. No canonical records, manifests, scores, or publication states were changed.

## Claim-by-claim findings

### CLM-GEOGRAPHIC_COORDINATES_BASICS-A@1

**Claim:** Geographic coordinates allow positions of objects on Earth's surface to be specified.

- Direct official-source support located in NOAA National Ocean Service's “What are latitude and longitude?” and USGS's “Specifications for Geographic Point Location Systems”, §2.1. Both describe latitude/longitude as a coordinate representation for locating positions on Earth's surface.
- OGC Abstract Specification Topic 2, “Referencing by coordinates”, Introduction and §1 Scope, defines coordinate-based spatial referencing and the data required to define coordinate reference systems.
- Existing Source @1 points instead to USGS “27 Ideas for Teaching Topographic Maps”, which is not an adequate identity/locator for the Claim's definition.
- Existing `EU-GEOGRAPHIC_COORDINATES_BASICS-A@1` says only “the indicated source is used within the stated material”; it contains no substantive passage or pinpoint.
- **Disposition: HOLD.** The Claim is well supported by official alternatives, but the linked Source and Evidence Use do not establish that support.

### CLM-GEOGRAPHIC_COORDINATES_BASICS-B@1

**Claim:** Latitude and longitude form a coordinate system for determining position.

- NOAA's National Ocean Service explicitly explains that latitude measures north/south from the equator and longitude measures east/west from the prime meridian. The NOAA nautical charts tutorial covers both together and explains their role in determining position.
- USGS Circular 878-B, §2.1, states that latitude and longitude are coordinate representations locating points on Earth's surface, with the equator and prime meridian as origins.
- Existing `EU-GEOGRAPHIC_COORDINATES_BASICS-B@1` is generic and the linked USGS Source @1 is mismatched to the proposition.
- **Disposition: HOLD.** Strong direct support exists, but the current record chain does not point to it. The Claim's wording is introductory; do not overextend it to imply that latitude/longitude alone fully specify every modern coordinate reference without datum/reference-frame context.

### CLM-GEOGRAPHIC_COORDINATES_BASICS-C@1

**Claim:** Coordinate accuracy and choice of coordinate system depend on the task and required spatial accuracy.

- OGC Topic 2, Introduction and §1 Scope, directly supports the importance of a fully specified coordinate reference system. It states that without the CRS reference, coordinate descriptions are ambiguous; its scope describes different CRS types for geodetic, regional, local, image, and moving-platform applications.
- OGC §7.1 explains that coordinates and coordinate metadata are linked to a CRS; coordinate sets must share a CRS, and dynamic systems also require a common coordinate epoch. Annex C.1.1 explains that latitude/longitude are not unique without full CRS specification.
- NOAA's NGS NCAT tool illustrates practical dependence on reference frame/datum and input/output coordinate type, but the current Source @1 is not this tool and the OGC source is the stronger normative model source.
- Existing `EU-GEOGRAPHIC_COORDINATES_OGC@1` identifies OGC and says it supports the CRS/task-dependent boundary, but gives no clause/section pinpoint. Existing `EU-GEOGRAPHIC_COORDINATES_BASICS-C@1` is generic and points to the mismatched USGS Source.
- **Disposition: HOLD.** OGC provides direct support for CRS selection and coordinate interpretation. The phrase “accuracy depends on the task and required spatial accuracy” is broader than the exact passages reviewed and should be narrowed or separately supported with a measurement/accuracy source before any versioned correction.

## Cross-record findings

1. The three Claims each have an Evidence Use with correct Claim refs, but all three are generic.
2. The OGC Evidence Use is correctly linked to Claim C and to `SRC-OGC-COORDINATE-REFERENCE-SYSTEMS@1`; its description is directionally relevant but lacks an exact locator.
3. The USGS Source identity “Authoritative reference source for geographic-coordinates-basics” is not a meaningful source identity. Its URL points to a teaching resource about topographic maps, not a coordinate definition. This is a high-priority source-identity defect, not just a missing pinpoint.
4. The OGC document is an authoritative technical specification, but it is not a beginner's teaching source. Use it for CRS/reference-frame concepts, not as the sole plain-language explanation of latitude and longitude.
5. Context and Scope are generic and targeted only at Claim A. They do not add claim-specific support and should not be treated as evidence.

## Required next steps

- Replace the mismatched USGS Source only under an explicit bounded authorization. Candidate official references include NOAA National Ocean Service's latitude/longitude explanations and USGS Circular 878-B §2.1. Select one source identity and stable locator per intended proposition; do not silently repoint a published Source.
- Version the related Evidence Uses with claim-specific descriptions and exact sections: NOAA's latitude/longitude tutorial or USGS Circular 878-B §2.1 for A/B; OGC Introduction, §1, §7.1 and Annex C.1.1 for the CRS ambiguity/selection boundary in C.
- Either narrow Claim C to the directly supported CRS/reference-frame proposition or add a separate source passage addressing positional accuracy and task requirements. Do not infer measurement accuracy solely from a CRS definition.
- Preserve the distinction between a coordinate tuple, a coordinate system, and a coordinate reference system. Avoid saying that latitude/longitude alone are always sufficient to identify a position unambiguously.
- Any canonical edit requires bounded authorization, versioned record changes, required test/manifest updates, and exact-head CI. This desk review does not authorize such changes.

## Sources reviewed

- NOAA National Ocean Service, “What are latitude and longitude?”: https://oceanservice.noaa.gov/education/tutorial_nautical_charts/nautical_charts02_information_2b.html
- NOAA National Ocean Service, “What is latitude?”: https://oceanservice.noaa.gov/facts/latitude.html
- NOAA National Ocean Service, “What is longitude?”: https://oceanservice.noaa.gov/facts/longitude.html
- USGS Circular 878-B, “Specifications for Geographic Point Location Systems”, §2.1: https://pubs.usgs.gov/circ/1983/0878b/report.pdf
- OGC Abstract Specification Topic 2: Referencing by coordinates, Introduction, §1, §7.1, Annex C.1.1: https://docs.ogc.org/as/18-005r4/18-005r4.html
