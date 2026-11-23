# M13 astronomy-basics — NASA Solar System and distance locator checkpoint

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Authorization: `M13-ASTRONOMY-SOLAR-SYSTEM-AU-001`
Basis HEAD: `1fbaaf0eb5d3f7c6e3955ed3fb0663d1fb63cbc5`
State: **Evidence Use A/C versioned with exact NASA locators; exact-head verification pending**

## Passage review

The registered NASA Science chapter *Chapter 1: The Solar System* was retrieved at its exact canonical URI:
https://science.nasa.gov/learn/basics-of-space-flight/chapter1-1/

- Claim A: “Knowledge of the Solar System” describes the Sun, heliosphere and objects orbiting the Sun; the “Mass” passage states that the Sun dominates the solar system's gravitational field and the motion of nearby objects. This directly supports the Claim's core description.
- Claim C: “Distances Within the Solar System” defines the astronomical unit by the mean Earth–Sun distance; “Light Time” provides distances at light-time and light-year scales. This directly supports the use of distinct scales.

Claim B remains PARTIAL/HOLD. The chapter provides object categories and some physical/orbital context, but it does not by itself establish all physical and orbital distinctions among planets, dwarf planets, asteroids and comets. NASA/IAU classification and orbital-property evidence remains required.

## Exact changes

- `EU-ASTRONOMY_BASICS-A@2`: versioned from v1, changing only `record_version` and `content.material.description`; Claim A v1 and Source v1 references are preserved.
- `EU-ASTRONOMY_BASICS-C@2`: versioned from v1, changing only `record_version` and `content.material.description`; Claim C v1 and Source v1 references are preserved.
- Updated the astronomy README with exact section locators and the Claim B limitation.
- Strengthened the dedicated regression to assert A/C locators, unchanged Claim statements, unchanged Source links, Claim B/EU B v1 and the nine-record slice structure.
- Registered the bounded authorization and added this checkpoint.

No Claim, Source, EU B, Context, Scope, Relation, risk metadata, D/E/B, record count, schema or publication status was changed. The slice remains at nine records.

## Rights and release limitations

NASA pages may contain third-party images, credits or other content. The Evidence Use descriptions paraphrase factual NASA-authored text only; no image or third-party material is copied. Page-level rights review remains separate. This correction does not establish independent corroboration, specialist approval, Human View, final D/E/B or publication eligibility.

## Verification still required

Run the dedicated astronomy regression, content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact field-level diffs, Claim/Source references, unchanged Claim statements and Source record, nine-record slice count, unchanged `main`, and PR #21 Draft/unmerged. M13 remains OPEN / NOT RELEASE-READY.
