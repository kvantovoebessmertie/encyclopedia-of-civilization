# M13 — Package 31 materials classification source-fit erratum

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis: Package 31 source-fit/rights follow-up and direct inspection of the exact Claim, Evidence Use and Source records at HEAD `8c479a94d49cc033514ff6e59f25f1d81518bd8f`.

## 1. Finding

Package 31 correctly states that the NSF Materials Research page names metals, ceramics, polymers and semiconductors, but does not explicitly list composites. The current canonical Evidence Use record `EU-M5-MATERIALS-SCIENCE-NSF-B@1`, however, says:

> NSF explicitly lists metals, ceramics, polymers, semiconductors and composites as materials studied in the field.

That sentence overstates the source. The NSF page does not support the composite clause. The source-fit follow-up identifies NIST Mechanical Performance Group as a separate candidate that explicitly includes composites.

## 2. Required bounded remediation

- Correct only the unsupported composite assertion in the existing NSF Evidence Use, using a versioned Evidence Use update and a precise locator for the four classes actually named by NSF.
- Add a separate NIST Source and claim-specific Evidence Use for the composites component, after verifying the exact NIST page passage and page-level rights notices.
- Keep the Claim's phrase “в частности” and its non-exhaustive classification framing. Do not imply that the five classes are mutually exclusive.
- Keep the application-suitability caveat separate: NSF DMREF is a candidate for the composition/processing/structure/property/performance design relationship, but its exact passage and rights page must be verified before registration.
- Do not infer a final D/E/B score or clear the Claim for publication.

## 3. Scope exclusions

This erratum does not authorize canonical writes. It does not authorize Claim wording changes, changes to other Evidence Use records, edits to unrelated Sources, D/E/B assignments, publication status changes, or use of copyrighted material. A separate authorization must name every exact path, version increment, permitted field, README/coverage change and regression assertion before any canonical modification.

## 4. Disposition

`CLM-MATERIALS_SCIENCE_BASICS-B@1` remains PARTIAL/HOLD. The prior Package 31 screen remains valid as a source-fit triage, but the existing NSF Evidence Use description contains a specific unsupported clause and must not be treated as verified evidence for composites.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft/unmerged; `main` remains unchanged.
