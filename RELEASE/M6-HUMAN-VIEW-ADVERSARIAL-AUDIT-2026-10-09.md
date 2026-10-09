# M6 Human View and Adversarial Audit — 2026-10-09

## Status
**HUMAN VIEW AUDIT RECORDED — M6 NOT CLEAN.** Review is limited to the six scope-locked slices and their current Claims, Context, Scope, and Evidence Use records. No content was changed in this pass.

## Findings

| ID | Slice / surface | Finding | Severity / disposition |
|---|---|---|---|
| M6-HV-01 | `demography-basics` Context | One Context sentence mixes Russian and English (“projections are not observations”). | Confirmed editorial defect. Normalize to one language during controlled correction. |
| M6-HV-02 | All six slices | Claims are in English while Context/Scope and Evidence Use descriptions are in Russian. This may be intentional bilingual metadata, but the language policy is not explicit in the slice itself. | Policy ambiguity, not yet a defect. Check corpus language conventions before changing; do not translate individual records inconsistently. |
| M6-HV-03 | All six slices | Scope text is generic (“basic educational slice; not exhaustive”) and targets Claim A only. A reader may not discover limitations that specifically affect Claims B/C from the Scope record alone. | Needs usability check against corpus conventions. Do not mechanically duplicate Scope/Context records; revise only if the architecture expects claim-specific navigation. |
| M6-HV-04 | `sleep-basics` | Context says individual sleep disorders require separate medical assessment and should not be inferred from general signs. | Good safety boundary; preserve. |
| M6-HV-05 | `learning-basics` | Context explicitly warns not to convert general mechanisms into universal individual instructions. | Good epistemic boundary; preserve. |
| M6-HV-06 | `law-basics` | Context identifies Cornell LII/Wex as a US-law teaching example and requires applicable jurisdiction/date for real questions. | Good legal boundary; preserve. |
| M6-HV-07 | `demography-basics` | Context requires territory, period, and reference date and distinguishes projections from observations, but language mixing weakens readability. | Preserve content, normalize language. |
| M6-HV-08 | `governance-basics` | Context states descriptive intent and says the slice does not recommend or rank forms of government. | Good neutrality boundary; preserve. |
| M6-HV-09 | `education-systems` | Context requires country, period, and applicable law for concrete obligations. | Good legal/context boundary; preserve. |

## Adversarial questions
- Could a reader mistake the sleep overview for diagnosis or treatment guidance? Current Context directly warns against this; preserve the boundary and avoid adding advice.
- Could a reader turn learning mechanisms into universal study instructions? Current Context warns against this; preserve it.
- Could a reader apply US jurisdiction examples as universal law? Current Context explicitly blocks this.
- Could a reader mistake a population projection for an observation? Context addresses this, but mixed language makes the warning less accessible.
- Could the OECD governance framework be mistaken for a universal ranking? Current Context explicitly blocks ranking; retain clear attribution.
- Could UNESCO's human-rights framing be mistaken for identical legal duties in every country and period? Current Context requires country, period, and applicable law.

## Required actions
1. Fix M6-HV-01 in the single controlled correction pass.
2. Compare language conventions with adjacent corpus slices before changing bilingual presentation.
3. Verify whether the generic Scope/Context anchor convention is intentional and usable; do not inflate the record count to solve a navigation issue.
4. Preserve the five domain-specific boundaries above during any edits.
5. The corpus-wide Relation endpoint/duplicate audit remains separate and mandatory; this Human View pass does not imply it is complete.
