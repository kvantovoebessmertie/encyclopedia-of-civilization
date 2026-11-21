# M13 Package 11 erratum — Environmental Engineering B record identity

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Applies to: `RELEASE/M13-UNASSESSED-RISK-CONTENT-SCREEN-PACKAGE-11-2026-11-14.md`

## Correction

The original Package 11 table used punctuation aliases for the Environmental Engineering B Claim, Evidence Use and Source IDs. The canonical JSON records were inspected directly and the Package 11 row has now been corrected to these exact IDs:

- Claim: `CLM_ENVIRONMENTAL_ENGINEERING_BASICS_B@1`
- Evidence Use: `EU_ENVIRONMENTAL_ENGINEERING_BASICS_B@1`
- Evidence Use: `EU-M5-AAEES-ENVIRONMENTAL-ENGINEERING-B@1`
- Source: `SRC_ENVIRONMENTAL_ENGINEERING_BASICS@1`
- Source: `SRC-M5-AAEES-ENVIRONMENTAL-ENGINEERING@1`

The canonical Claim statement was also checked verbatim. The prior Package 11 prose paraphrase overstated the recorded wording (including an explicit reference to soil protection). The corrected package now quotes the canonical Claim exactly:

> Экологическая инженерия включает подходы к управлению качеством воды, обработке сточных вод, контролю загрязнения воздуха и обращению с отходами.

## Effect on findings

The previous desk-level finding remains **PARTIAL / HOLD**: the registered EPA environmental-topics portal and AAEES careers page are broad public references, not a precise disciplinary passage or technical standard. The correction does not establish stronger source support and does not clear the Claim.

## Integrity boundary

- Canonical Claim, Evidence Use and Source JSON: unchanged.
- Risk metadata: unchanged.
- D/E/B scores: unchanged.
- Publication status and rights permissions: unchanged.
- Specialist approval and M13 closure: not granted.

The queue deduplication matcher is separately being hardened to recognize hyphen/underscore aliases, with a regression test for this exact historical mismatch. Until the updated queue artifact confirms exclusion, do not treat the repeated row as a new review.
