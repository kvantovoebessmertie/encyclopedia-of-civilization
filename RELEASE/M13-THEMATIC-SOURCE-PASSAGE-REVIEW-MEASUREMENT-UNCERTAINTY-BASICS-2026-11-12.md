# M13 Thematic Source-Passage Review — Measurement Uncertainty Basics

Date: 2026-11-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Scope: Claims A–C in `measurement-uncertainty-basics`, their linked Evidence Use records, and the currently linked NIST/BIPM Sources.

## Status and limits

This is a source-passage desk review. It is not an independent metrology review, final D/E/B scoring, canonical correction, or publication decision. All three Claims remain **HOLD** pending versioned claim-specific locators in Evidence Use records, rights/attribution review, and qualified editorial review.

No canonical Claim, Evidence Use, Source, Context/Scope, Relation, manifest, or score record was changed.

## Claim A — result interpreted with uncertainty

Claim: `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1`  
Current Evidence Use: `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1`  
Current Source: `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1` (NIST TN 1297 landing page)

**Direct passage located:** NIST TN 1297 §2.1 states that a measurement result is an approximation/estimate and is complete only when accompanied by a quantitative statement of its uncertainty. NIST's official page identifies the document and its section structure. This directly supports the Claim's central idea.

**Finding:** Source identity is appropriate, but the current Evidence Use has only a generic description and no §2.1 pinpoint. The claim wording “должен интерпретироваться вместе” is a reasonable plain-language compression of NIST's completeness statement, but should not be expanded into a universal reporting rule for every context without scope qualification.

**Required follow-up:** Version the Evidence Use with an exact locator to NIST TN 1297 §2.1 and a concise description of the support and scope.

## Claim B — uncertainty is not automatically error

Claim: `CLM-MEASUREMENT_UNCERTAINTY_BASICS-B@1`  
Current Evidence Uses: `EU-MEASUREMENT_UNCERTAINTY_BASICS-B@1` and `EU-MEASUREMENT_UNCERTAINTY_BIPM@1`  
Current Sources: NIST TN 1297 and BIPM/JCGM VIM

**Direct passages located:**
- VIM 2.26 defines measurement uncertainty as a non-negative parameter characterizing dispersion of quantity values attributed to a measurand based on the information used; Notes 1–4 explain systematic effects, Type A/Type B components, and association with a stated quantity value.
- VIM 2.16 defines measurement error as the measured quantity value minus a reference quantity value.
- NIST TN 1297 §2.3 explicitly says the difference between error and uncertainty should be borne in mind and gives an example where corrected result may have negligible error while uncertainty remains large.

**Finding:** The distinction is directly supported by two authoritative metrology sources. However, the Claim phrase “разброс значений, обоснованно приписываемых измеряемой величине” is closer to the earlier VIM/GUM formulation; the current VIM 2.26 wording is “quantity values ... attributed to a measurand, based on the information used.” The current linked BIPM Evidence Use describes independent corroboration but does not provide VIM 2.26 or 2.16 locators. The NIST Evidence Use is generic.

**Required follow-up:** Add exact locators to NIST TN 1297 §2.3 and VIM 2.16/2.26. Review whether the Claim should use the current VIM definition verbatim or preserve its simplified explanatory formulation with an explicit source-aligned wording note.

## Claim C — measurand and measurement model

Claim: `CLM-MEASUREMENT_UNCERTAINTY_BASICS-C@1`  
Current Evidence Use: `EU-MEASUREMENT_UNCERTAINTY_BASICS-C@1`  
Current Source: NIST TN 1297

**Direct passages located:**
- VIM 2.3 defines the measurand as the quantity intended to be measured. Note 1 states that specification requires knowledge of the kind of quantity and relevant state/description details.
- VIM 2.48 defines a measurement model as the mathematical relation among all quantities known to be involved in a measurement; Note 1 identifies the measurand as the output quantity inferred from information about input quantities.
- NIST TN 1297 Appendix A.1–A.2 explains that a measurand may be determined from other quantities through a functional relation and that the measurement function should include quantities contributing significant uncertainty.

**Finding:** The substantive idea is well supported. The currently linked NIST Source page is a broad document landing page and the Evidence Use has no pinpoint. The strongest conceptual definition for “measurement model” is in VIM 2.48, which is not currently linked to this Claim's Evidence Use. NIST Appendix A supplies a practical uncertainty-propagation treatment, but should not be treated as the sole definition of a measurement model.

**Required follow-up:** Add a distinct versioned BIPM/JCGM VIM Source identity if the existing Source record does not identify that vocabulary entry, then version the Evidence Use with VIM 2.3 and 2.48 plus NIST TN 1297 Appendix A.1–A.2. Do not silently repurpose the NIST Source identity.

## Cross-claim findings

1. All three primary Evidence Use records currently contain the same generic material description and no reproducible section/paragraph locator. This prevents a reviewer from verifying the specific support from the record itself.
2. Claim B already has a second BIPM/JCGM Evidence Use, but it too lacks exact entry locators and currently corroborates only Claim B.
3. The existing Source identities are broad landing-page references. They are not substitutes for claim-specific locators.
4. The direct passages located support the core ideas, but Claim B's phrasing should be reconciled carefully with the current VIM definition and the distinction between measurement error and uncertainty.
5. No D/E/B score is assigned in this report. No historical score is replaced or inferred.

## Review disposition

| Claim | Direct source passage found | Current Evidence Use pinpoint | Disposition |
|---|---|---|---|
| A | NIST TN 1297 §2.1 | Missing | HOLD |
| B | VIM 2.16 and 2.26; NIST TN 1297 §2.3 | Missing | HOLD |
| C | VIM 2.3 and 2.48; NIST TN 1297 Appendix A.1–A.2 | Missing | HOLD |

## Sources checked

- NIST, *Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results*, TN 1297, §2.1, §2.3, Appendix A.1–A.2: https://www.nist.gov/pml/nist-technical-note-1297
- BIPM/JCGM, *International Vocabulary of Metrology (VIM)*, 2.3 Measurand: https://jcgm.bipm.org/vim/en/2.3.html
- BIPM/JCGM, *International Vocabulary of Metrology (VIM)*, 2.16 Measurement error: https://jcgm.bipm.org/vim/en/2.16.html
- BIPM/JCGM, *International Vocabulary of Metrology (VIM)*, 2.26 Measurement uncertainty: https://jcgm.bipm.org/vim/en/2.26.html
- BIPM/JCGM, *International Vocabulary of Metrology (VIM)*, 2.48 Measurement model: https://jcgm.bipm.org/vim/en/2.48.html

**Final state:** 3/3 Claims source-passage desk-reviewed; 0 canonical record changes; 0 score changes; 3/3 remain HOLD.
