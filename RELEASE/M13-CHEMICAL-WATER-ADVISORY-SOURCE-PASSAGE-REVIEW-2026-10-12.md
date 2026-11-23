# M13 Chemical Water Advisory Source-Passage Review — 2026-10-12

Status: **bounded source-passage review; no D/E/B score change, no canonical record edits, no publication clearance.**

Branch: `m13-system-wide-depth-audit-2026-10-09`

Review scope: `CLM-CHEM-WATER-NO-BOIL` v1 and `CLM-CHEM-WATER-NO-DRINK` v1; their current Evidence Use records; the CDC and EPA Source records currently linked to these Claims. Official CDC and EPA pages were checked on 2026-10-12. This is not a specialist Human View.

## Results

| Claim ID/version | Evidence Use ID/version | Source ID/version | Passage-level result | Disposition |
|---|---|---|---|---|
| `CLM-CHEM-WATER-NO-BOIL` v1 | `EU-CHEM-WATER-NO-BOIL` v1 | `SRC-CDC-CHEMICAL-WATER-ADVISORY-2024` v1 | **Direct support.** CDC's “Drinking Water Advisories: An Overview,” subsection “Do not drink water advisory,” says that boiling water containing harmful chemicals or toxins will not make it safe to use. This matches the Claim's narrow proposition. | Provisionally supported. Add a reproducible subsection locator to a versioned Evidence Use correction under the established process. |
| `CLM-CHEM-WATER-NO-BOIL` v1 | `EU-CHEM-WATER-NO-BOIL-EPA` v1 | `SRC-EPA-EMERGENCY-DISINFECTION-WATER` v1 | **Direct support for the limited mechanism.** EPA's “Emergency Disinfection of Drinking Water” says boiling/disinfection can kill microorganisms but does not destroy other contaminants such as heavy metals, salts and most other chemicals. It supports the broad limitation, but is emergency disinfection guidance and should not replace local chemical-advisory instructions. | Provisionally supported as complementary evidence. Add the exact relevant paragraph locator; do not overstate it as product- or contaminant-specific evidence. |
| `CLM-CHEM-WATER-NO-DRINK` v1 | `EU-CHEM-WATER-NO-DRINK` v1 | `SRC-CDC-CHEMICAL-WATER-ADVISORY-2024` v1 | **Direct support.** CDC's “Do not drink water advisory” subsection says officials typically issue this advisory when tap water is or could be contaminated with harmful chemicals or toxins, and recommends commercially bottled water for drinking and cooking. | Provisionally supported. Add a reproducible subsection/list locator to a versioned Evidence Use correction. |

## Exact passage locators reviewed

### CDC — “Drinking Water Advisories: An Overview”

URL: https://www.cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html

- Section **“Do not drink water advisory”**, opening paragraph: advisories are typically issued when tap water is or could be contaminated with harmful chemicals or toxins; boiling water containing harmful chemicals or toxins will not make it safe to use.
- The same subsection, list beginning **“During a do not drink water advisory, use commercially bottled water for:”**: lists drinking and cooking, brushing teeth, washing fruits and vegetables, preparing food, mixing baby formula, making ice and giving water to pets.
- The Claim currently covers only drinking and cooking. This is appropriately narrower than the full CDC list. The exact local advisory remains controlling for additional uses and restrictions.
- Scope distinction: CDC separately defines “do not use” advisories as prohibiting tap water for any purpose. Do not broaden this Claim from “do not drink” to “do not use.”

### EPA — “Emergency Disinfection of Drinking Water”

URL: https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water

- Opening explanatory paragraph: boiling/disinfection is discussed as a way to kill disease-causing microorganisms, but does not destroy other contaminants, including heavy metals, salts and most other chemicals.
- This is useful for the limitation that boiling is not a universal chemical-removal method. It does not establish that every chemical behaves identically, nor does it replace an official local advisory or contaminant-specific instructions.

## Structural and evidence-quality findings

1. All three Evidence Use records resolve to the intended current Claim and Source IDs and versions in this slice.
2. The current Evidence Use descriptions explain the support but do not provide a sufficiently reproducible page/section locator. Structural linkage passes; pinpoint completeness remains open.
3. CDC directly supports both Claim wordings within the stated scope. EPA complements the boiling/disinfection limitation but is broader emergency guidance.
4. Different agencies and URLs do not, by themselves, prove independent corroboration. This review records passage fit only and does not assign an independence rating.
5. Because the subject concerns potentially chemically contaminated drinking water, both Claims remain **HOLD for public-pilot clearance** until locators are corrected through the authorized versioned process, record history is preserved, and independent Human View reviews the emergency-use boundaries.

## Decision

- Source-fit: both Claims are provisionally supported within their current narrow wording.
- D/E/B: no scores assigned or changed by this report.
- Canonical Claim/Evidence Use/Source JSON: unchanged.
- Public MVP allowlist: do not add these records on the strength of this report alone.
- Next bounded action: prepare proposed versioned locator corrections and targeted regressions after the established authorization/review step; then rerun exact-head CI and obtain the required Human View.
