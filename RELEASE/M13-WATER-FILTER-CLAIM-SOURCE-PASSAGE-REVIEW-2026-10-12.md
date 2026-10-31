# M13 Water-Filter Claim Source-Passage Review — 2026-10-12

Status: **bounded source-passage review; no D/E/B score change, no canonical record edits, no publication clearance.**

Branch: `m13-system-wide-depth-audit-2026-10-09`
Review scope: the two existing Claims in `water-filter-assessment`, their version-1 Evidence Use records, and the version-1 Source records.
Review basis: current official CDC and WHO pages checked on 2026-10-12. This is a focused source-fit check, not a specialist Human View.

## Results

| Claim ID/version | Evidence Use ID/version | Source ID/version | Source-fit result | Remaining disposition |
|---|---|---|---|---|
| `CLM-WATER-FILTER-LIMITS` v1 | `EU-WATER-FILTER-LIMITS` v1 | `SRC-CDC-WATER-FILTER-2025` v1 | **Direct support found for the stated substance.** CDC's “Filter” section says portable filters will not remove viruses, and gives absolute pore-size thresholds of 0.3 micron or smaller for bacteria and 1 micron or smaller for parasites. | Keep provisional. Add a versioned, reproducible section locator to the Evidence Use record under the established authorization process. Preserve the current record history. |
| `CLM-WATER-FILTER-WHO-PERFORMANCE` v1 | `EU-WATER-FILTER-WHO-PERFORMANCE` v1 | `SRC-WHO-HWT-EVALUATION` v1 | **Direct support found for the stated substance.** WHO's International Scheme page says the scheme evaluates microbial performance against health-based criteria and explains that methods vary in removal of bacteria, viruses and protozoa. | Keep provisional. Add a versioned locator to the scheme overview/performance-classification section under the established authorization process. Preserve the current record history. |

## Passage-level source notes

### CDC — portable filter limitations

- Source identity currently stored: “CDC — How to Make Water Safe in an Emergency”.
- Stored URI: https://www.cdc.gov/water-emergency/about/index.html
- Canonical page reviewed: https://www.cdc.gov/water-emergency/about/
- Exact locator: section heading **“Filter”**, under “Portable filters”; the bullets state that portable filters will not remove viruses, need an absolute pore size of 0.3 micron or smaller to remove bacteria, and 1 micron or smaller to remove parasites such as Giardia or Cryptosporidium.
- Scope note: this is CDC emergency-water guidance for portable filters. It should not be generalized to all filtration technologies, all contaminants, or all household filter systems. CDC separately notes that after filtering, a chemical disinfectant can kill viruses and bacteria; the Claim does not currently give a full treatment protocol, so the review does not add one.

### WHO — household water-treatment evaluation

- Source identity currently stored: “WHO — International Scheme to Evaluate Household Water Treatment Technologies”.
- Stored URI: https://www.who.int/tools/international-scheme-to-evaluate-household-water-treatment-technologies
- Exact locator: overview paragraph beginning **“The WHO International Scheme to Evaluate Household Water Treatment Technologies…”** and the following paragraph on differences among methods for removing bacteria, viruses and protozoa; the same page describes the performance-classification scheme.
- Scope note: the page supports the statement about evaluation and differing pathogen-removal performance. It does not prove that every technology has been evaluated or that a particular product is safe. Product-specific conclusions require the corresponding WHO test result and correct-use conditions.

## Structural and evidence-quality findings

1. Both Evidence Use records resolve to the exact current Claim and Source IDs and versions in this slice.
2. Both Evidence Use descriptions currently lack a reproducible section locator. Structural linkage therefore passes, but the evidence trail is not yet sufficiently pinpointed for final closure.
3. CDC and WHO are different institutional sources, but this review does **not** label them independent corroboration of the same proposition: they support two different Claims and answer different questions.
4. Source version 1 and Evidence Use version 1 must not be silently overwritten. Add a versioned correction only through the normal bounded correction and regression process.
5. Because water safety is high-consequence, the pair remains **HOLD for public-pilot clearance** until locator updates are authorized, source/version history is preserved, and an appropriate independent Human View checks the exact wording and emergency-use boundaries.

## Decision

- Source-fit: **provisionally supported for both current Claim wordings**.
- D/E/B: **not assigned or changed by this note**.
- Canonical Claim/Evidence Use/Source JSON: **unchanged**.
- Public MVP allowlist: **do not add these records on the strength of this note alone**.
- Next bounded action: prepare versioned Evidence Use locator corrections and tests after explicit review/authorization; then rerun exact-head CI and obtain the required Human View.
