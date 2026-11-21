# M13 bounded correction authorization — astronomy basics Solar System and distance locators

Date: 2026-11-15
Authorization ID: M13-ASTRONOMY-SOLAR-SYSTEM-AU-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `1fbaaf0eb5d3f7c6e3955ed3fb0663d1fb63cbc5`

## Finding

M13 Package 06 identified direct conceptual support for Astronomy Claims A and C in the registered NASA Science “The Solar System” chapter, but both existing Evidence Use descriptions are generic and contain no reproducible pinpoint. Direct inspection of the exact registered page confirms the relevant passages:
- “Knowledge of the Solar System” describes the Sun, heliosphere and objects orbiting the Sun, and the Sun's gravitational dominance.
- “Distances Within the Solar System” and “Light Time” identify the astronomical unit and light-year as distance scales.

Claim B remains PARTIAL/HOLD: the current chapter does not establish all physical and orbital distinctions among planets, dwarf planets, asteroids and comets. It is expressly excluded from this authorization.

## Exact authorized changes

On the named M13 branch only:

1. Version `EU-ASTRONOMY_BASICS-A` v1→v2, changing only `record_version` and `content.material.description`. Preserve Claim A v1, Source v1, evidence role, provenance, ID, status and every other field.
   - Claim: `CLM-ASTRONOMY_BASICS-A@1`
   - Source: `SRC-ASTRONOMY_BASICS@1`
   - Locator: NASA Science, *Chapter 1: The Solar System*, “Knowledge of the Solar System” and “Mass” passages, https://science.nasa.gov/learn/basics-of-space-flight/chapter1-1/
   - Limit: supports the Sun and objects orbiting it, and the Sun's dominant gravitational influence. Do not imply the chapter is a complete inventory of every solar-system object or that every object has an identical orbit.

2. Version `EU-ASTRONOMY_BASICS-C` v1→v2, changing only `record_version` and `content.material.description`. Preserve Claim C v1, Source v1, evidence role, provenance, ID, status and every other field.
   - Claim: `CLM-ASTRONOMY_BASICS-C@1`
   - Source: `SRC-ASTRONOMY_BASICS@1`
   - Locator: NASA Science, *Chapter 1: The Solar System*, “Distances Within the Solar System” and “Light Time” passages, same URL.
   - Limit: supports the astronomical unit as the mean Earth–Sun distance and the light-year/light-time scale. Do not imply that the astronomical unit and light-year are interchangeable or equally suited to all distance ranges.

3. Update only `CONTENT/vertical-slices/astronomy-basics/README.md` to record these exact locators and scope boundaries.
4. Strengthen only `REFERENCE/tests/test_content_astronomy_basics_vertical_slice.py` to assert both EU v2 records, exact Claim/Source v1 references, section markers, unchanged Claim statements, and unchanged nine-record slice structure.
5. Register this authorization and `astronomy-basics` in `RELEASE/EDITORIAL-CORRECTION.json`.
6. Add one checkpoint document recording findings, exact changes, exclusions, NASA page-level rights caveat and verification status.

## Explicit exclusions

No change to Claim wording/version/type, Source identity/version/URI, EU B, Context, Scope, Relation, risk metadata, D/E/B score, rights clearance, publication approval, coverage count, schema, release allowlist, other record/slice, `main`, or PR merge is authorized. No new/deleted Record is authorized; the slice remains at nine records.

NASA's page includes third-party image/credit material. The authorized Evidence Use descriptions must paraphrase NASA-authored factual text only; do not copy images or third-party content. NASA page-level rights review remains separate. This correction does not establish independent corroboration or final assessment. Claim B remains PARTIAL/HOLD pending NASA/IAU classification and orbital-property evidence.

## Acceptance

Run the dedicated astronomy regression, content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact field-level diffs, unchanged Claims and Source, Claim/Source links, nine-record slice count, unchanged `main`, and PR #21 Draft/unmerged. M13 remains OPEN / NOT RELEASE-READY.
