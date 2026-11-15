# M13 — risk-screen false-positive correction: OpenStax / tax substring

Date: 2026-11-15
Branch: m13-system-wide-depth-audit-2026-10-09
Correction commits:
- b3898d3f07d90639bc86778691c13d2fa7e0f9a2 — risk-screen regex correction
- bcb3666fc052a4aa1a18e8118151d7cada17cbae — regression test

## Finding

A current worksheet generated from PR merge-tree revision 87a78a69f89700f4cf06dac7bfb2f21f1045d8d0 classified the three Claims below as legal_financial and consequently applied high_consequence_screen:

- CLM-BEHAVIORAL_BIOLOGY_BASICS-A
- CLM-BEHAVIORAL_BIOLOGY_BASICS-B
- CLM-BEHAVIORAL_BIOLOGY_BASICS-C

The false positive came from the unbounded English regex token tax in RISK_TERMS[legal_financial]: it matched the substring in the source identity OpenStax, Biology 2e, §45.7. The Claims' statements are not tax/legal/financial content. The source title alone caused the erroneous domain classification.

## Correction

- Added word boundaries around the English legal/financial terms: legal, jurisdiction, tax, loan, contract, financial, investment, accounting, financial reporting.
- Kept Russian morphological stems unchanged.
- Added regression coverage asserting that OpenStax Biology 2e does not match the legal/financial classifier while genuine text such as tax liability under a legal contract still matches.
- No Claim, Evidence Use, Source, Context, Scope, Relation, risk metadata or D/E/B record was changed.

## Queue reconciliation

The prior 516-candidate generic-EU reconciliation used 137 high-consequence candidates, 20 already deep-reviewed priority Claims, and 359 remaining residual Claims:

516 - 137 - 20 = 359.

The newer worksheet incorrectly raised the high-consequence count to 140 solely because of the three OpenStax false positives. The correction is expected to restore the 137 / 379 / 359 routing arithmetic. This expectation is not treated as verified until the worksheet is regenerated on one exact post-correction HEAD and the three Claims no longer carry the false-positive flag.

The three behavioural-biology Claims remain on their existing HOLD/partial-support path. Removing an erroneous machine triage flag is not a risk clearance, D/E/B assessment, specialist approval or publication decision.

## Required verification

1. Run the focused test_m13_claim_audit_inventory.py regression.
2. Regenerate the M13 claim audit worksheet and verify the three Claims no longer contain legal_financial or high_consequence_screen solely due to the OpenStax identity.
3. Recompute the 516-candidate generic-EU intersection and confirm the 137 high-consequence / 20 priority / 359 residual partition.
4. Run Reference Tests, Release Conformance Gate and Offline Edition on the same exact final HEAD.
5. Confirm PR #21 remains Draft/unmerged and main remains unchanged.

M13 remains OPEN / NOT RELEASE-READY until all substantive, rights, specialist, Human View and release gates are independently satisfied.