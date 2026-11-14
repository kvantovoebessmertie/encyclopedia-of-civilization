# M13 — water-quality aquatic-life evidence verification

Date: 2026-11-14
Branch: `m13-system-wide-depth-audit-2026-10-09`
Claim: `CLM_WATER_QUALITY_BASICS_B@1`
Evidence Use: `EU_WATER_QUALITY_BASICS_B@1`
Source: `SRC_WATER_QUALITY_BASICS@1`

## 1. Retrieval correction

The second preliminary screen reported that the linked Source record could not be retrieved during that pass. A subsequent exact-branch tree inspection located the record at:

`CONTENT/vertical-slices/water-quality-basics/records/SRC-WATER_QUALITY_BASICS.json`

The record exists at the audited revision and identifies the U.S. EPA page *Basic Information on Water Quality Criteria*:
https://www.epa.gov/wqc/basic-information-water-quality-criteria

This resolves the earlier retrieval uncertainty. It does not, by itself, establish full semantic support.

## 2. Claim and evidence chain inspected

- Claim v1: “Aquatic-life criteria consider the concentration or condition at which pollutants are expected to harm aquatic organisms under specified exposure assumptions.”
- EU v1: role `supports`; links the Claim v1 to Source v1. Its material description is a generic boundary statement and contains no exact passage locator.
- Source v1: U.S. EPA, *Basic Information on Water Quality Criteria*.

The current EPA page states that aquatic-life criteria are based on how much of a chemical can be present in surface water before it is likely to harm plant and animal life, and that the criteria are designed to protect freshwater and saltwater organisms from short-term and long-term exposure.

The EPA page therefore directly supports the concentration / pollutant / aquatic-organism / short- and long-term exposure components. The Claim's phrase “or condition” is broader and less precise than the cited page's explanation. The page also sits within the U.S. EPA / Clean Water Act context; it should not be presented as a universal legal standard for all jurisdictions.

## 3. Disposition

**Evidence relevance: direct but bounded.** The Source is relevant and supports the central concentration-and-harm proposition. The prior “source path unavailable” note is superseded by this retrieval check.

**Open editorial issue:** the phrase “or condition” is not clearly supported by the linked page as written. A narrowly scoped formulation focused on pollutant concentration in surface water and short-/long-term exposure would fit the current Source more closely. This is a proposed editorial direction only, not a canonical correction.

**Locator issue:** the EU material currently has no exact section / passage locator. Add one only through a separately authorized EU version update with a regression test.

## 4. Required next action

1. Keep Claim and EU unchanged pending bounded authorization.
2. Obtain authorization for either (a) a narrow Claim wording update, or (b) an additional independently suitable Source that directly supports the “condition” wording.
3. If authorized, update the EU material with a stable pinpoint to the EPA “Aquatic Life Criteria” section and test the exact Claim → EU → Source chain.
4. Preserve the U.S. jurisdictional context and distinguish EPA criteria recommendations from state / Tribal water-quality standards.

## 5. Integrity

- Source record retrieval: verified.
- External Source page: checked.
- Central proposition: directly supported within the stated scope.
- Wording boundary (“or condition”): unresolved.
- Exact passage locator in EU: absent.
- Canonical records changed: 0.
- Risk metadata assigned: 0.
- D/E/B scores changed: 0.
- Independent specialist review: 0.
- M13 closure / publication approval: 0.

This is an evidence-chain verification note, not risk clearance or M13 closure.
