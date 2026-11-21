# M13 bounded correction authorization — astrophysics Stars A/B pinpoints

Date: 2026-11-15
Authorization ID: M13-ASTROPHYSICS-STARS-AB-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `6081775c127999a210a84c39fc1a9fdb80687f82`

## Finding

M13 Package 06 identified direct conceptual support for Astrophysics Claims A and B in the registered NASA Science “Stars” page, but the existing Evidence Use descriptions are generic. Direct inspection of the exact registered page confirms:
- the opening description identifies stars as hot gas composed mostly of hydrogen, with helium and small amounts of other elements;
- the same opening passage states that stars have life cycles and their properties change with age;
- the “Life” section describes changes in luminosity, size and temperature during the main-sequence phase.

Claim C remains PARTIAL/HOLD because the registered page is too narrow for its broader statement about observations of other cosmic objects and astrophysical research.

## Exact authorized changes

On the named M13 branch only:

1. Version `EU-ASTROPHYSICS_BASICS-A` v1→v2, changing only `record_version` and `content.material.description`.
   - Claim: `CLM-ASTROPHYSICS_BASICS-A@1`
   - Source: `SRC-ASTROPHYSICS_BASICS@1`
   - Locator: NASA Science, “Stars”, opening definition, https://science.nasa.gov/universe/stars/
   - Limit: supports stars as hot gas composed mostly of hydrogen, with helium and small amounts of other elements; do not imply all stars have identical compositions.

2. Version `EU-ASTROPHYSICS_BASICS-B` v1→v2, changing only `record_version` and `content.material.description`.
   - Claim: `CLM-ASTROPHYSICS_BASICS-B@1`
   - Source: `SRC-ASTROPHYSICS_BASICS@1`
   - Locator: NASA Science, “Stars”, opening life-cycle summary and “Life” section, same URL.
   - Limit: supports stellar life cycles and age-related changes in properties; do not imply every star follows one identical pathway, since later stages depend strongly on mass.

3. Update only `CONTENT/vertical-slices/astrophysics-basics/README.md` to record these locators and limits.
4. Strengthen only `REFERENCE/tests/test_content_astrophysics_basics_vertical_slice.py` to assert both EU v2 records, exact Claim/Source v1 references, locator markers, unchanged Claim statements, unchanged EU C v1 and nine-record slice structure.
5. Register this authorization and `astrophysics-basics` in `RELEASE/EDITORIAL-CORRECTION.json`.
6. Add one checkpoint document recording the finding, exact changes, exclusions, NASA page-level rights caveat and verification status.

## Explicit exclusions

No Claim wording/version/type, Source identity/version/URI, EU C, Context, Scope, Relation, risk metadata, D/E/B, rights clearance, publication approval, coverage count, schema, release allowlist, other record/slice, `main`, or PR merge change is authorized. No new/deleted Record is authorized; the slice remains at nine records.

NASA's page contains third-party image credits. The Evidence Use descriptions must paraphrase NASA-authored factual text only; do not copy images or third-party content. NASA page-level rights review remains separate. Claim C remains PARTIAL/HOLD pending broader NASA astrophysics and telescope/observatory sources. This correction does not establish independent corroboration, specialist approval, Human View, final D/E/B or publication eligibility.

## Acceptance

Run the dedicated astrophysics regression, content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact field-level diffs, unchanged Claims and Source, Claim/Source links, EU C v1, nine-record slice count, unchanged `main`, and PR #21 Draft/unmerged. M13 remains OPEN / NOT RELEASE-READY.
