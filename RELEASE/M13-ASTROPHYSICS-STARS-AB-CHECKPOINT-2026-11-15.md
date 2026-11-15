# M13 astrophysics-basics — NASA Stars A/B locator checkpoint

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Authorization: `M13-ASTROPHYSICS-STARS-AB-001`
Basis HEAD: `6081775c127999a210a84c39fc1a9fdb80687f82`
State: **Evidence Use A/B versioned with exact NASA locators; exact-head verification pending**

## Passage review

The registered NASA Science “Stars” page was retrieved at:
https://science.nasa.gov/universe/stars/

- Claim A: the opening definition describes stars as hot gas composed mostly of hydrogen, with some helium and small amounts of other elements. This directly supports the Claim's introductory composition statement.
- Claim B: the opening life-cycle summary states that stars have life cycles and their properties change with age. The “Life” section describes changes in luminosity, size and temperature during the main-sequence phase. Later evolutionary pathways depend on stellar mass.

Claim C remains PARTIAL/HOLD: the registered Stars page alone is too narrow for the broader statement about observations of other cosmic objects and astrophysical research. A NASA astrophysics overview and telescope/observatory sources remain required.

## Exact changes

- `EU-ASTROPHYSICS_BASICS-A@2`: versioned from v1, changing only `record_version` and `content.material.description`; Claim A v1 and Source v1 references are preserved.
- `EU-ASTROPHYSICS_BASICS-B@2`: versioned from v1, changing only `record_version` and `content.material.description`; Claim B v1 and Source v1 references are preserved.
- Updated the slice README with exact locators and the Claim C limitation.
- Strengthened the dedicated regression to assert A/B locators, unchanged Claim statements, unchanged Source links, Claim C/EU C v1 and the nine-record slice structure.
- Registered the bounded authorization and added this checkpoint.

No Claim, Source, EU C, Context, Scope, Relation, risk metadata, D/E/B, record count, schema or publication status was changed. The slice remains at nine records.

## Rights and release limitations

NASA pages may contain third-party images and credits. The Evidence Use descriptions paraphrase NASA-authored factual text only; no image or third-party material is copied. Page-level rights review remains separate. This correction does not establish independent corroboration, specialist approval, Human View, final D/E/B or publication eligibility.

## Verification still required

Run the dedicated astrophysics regression, content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact field-level diffs, Claim/Source references, unchanged Claim statements and Source record, EU C v1, nine-record slice count, unchanged `main`, and PR #21 Draft/unmerged. M13 remains OPEN / NOT RELEASE-READY.
