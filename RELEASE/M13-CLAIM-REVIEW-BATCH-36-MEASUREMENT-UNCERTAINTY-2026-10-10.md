# M13 Claim Review Batch 36 — Measurement Uncertainty
Date: 2026-10-10
Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **3 additional Claims reviewed. Bounded batch only; no domain closure is implied.**

## Method
Reviewed the three Claims in `measurement-uncertainty-basics`, their linked Evidence Use records, source identity, Context and Scope. D = explanatory depth, E = claim-specific evidence fit, B = boundary discipline; each is scored 0–3. Scores assess the corpus representation and traceability, not the quality of NIST guidance as a whole.

## Claim-level results

| Claim ID | D | E | B | Rationale and disposition |
|---|---:|---:|---:|---|
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A` | 2 | 1 | 2 | Correctly communicates that a measurement result should be interpreted alongside its uncertainty, but does not show how the uncertainty accompanies a reported value or how it affects decisions and comparisons. The Evidence Use record provides no section, equation, worked example or passage locator within NIST Technical Note 1297. The slice Scope appropriately identifies this as basic education, not an exhaustive reference. |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-B` | 2 | 1 | 2 | The distinction between uncertainty and error is important, and the statement is directionally consistent with metrology terminology. However, “разброс значений” can be read too narrowly as simple observed scatter; uncertainty evaluation can include Type A and Type B components and depends on the measurement model and available information. The linked Evidence Use text is generic and does not locate the specific definition. Add an explanatory example and clarify that uncertainty is not simply the known error or a guarantee that the true value lies within an interval. |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-C` | 2 | 1 | 2 | Defining the measurand and measurement model is a sound starting point, but the Claim does not explain inputs, corrections, influence quantities, sensitivity coefficients or propagation of uncertainty. The Evidence Use description does not identify a specific NIST TN 1297 section or equation. Keep this as a starting principle, not a complete uncertainty-budget procedure. |

## Findings
1. **Confirmed generic Evidence Use debt:** all three Evidence Use records repeat the same general sentence and link to NIST Technical Note 1297 without identifying a supporting section, equation, table or passage for each Claim.
2. **Technical clarification needed in a future authorized correction:** uncertainty is not interchangeable with measurement error, and it should not be reduced to the observed spread of repeated readings. A complete explanation needs the measurand, measurement model, input quantities, evaluation method, uncertainty components and assumptions appropriate to the case.
3. **Practical depth gap:** no worked example demonstrates how to define the measurand, identify contributors, combine components, report a result with units and uncertainty, choose significant digits, or compare results using uncertainty. These are audit findings, not authorization to edit content now.
4. **Boundary:** uncertainty estimates depend on the measurement model, calibration information, method, environment and assumptions. A numerical uncertainty statement does not by itself establish fitness for purpose, traceability, calibration validity, or compliance with a decision threshold.
5. **No content Records were changed.** Three additional Claims now have explicit D/E/B scores and rationales. The denominator remains frozen at 1,494 Claims; 105/1,494 (7.03%) have explicit scores in tracked batches. This is scoring coverage only; M13 remains incomplete.

## Records inspected
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/CLM-MEASUREMENT_UNCERTAINTY_BASICS-A.json`
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/CLM-MEASUREMENT_UNCERTAINTY_BASICS-B.json`
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/CLM-MEASUREMENT_UNCERTAINTY_BASICS-C.json`
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/EU-MEASUREMENT_UNCERTAINTY_BASICS-A.json`
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/EU-MEASUREMENT_UNCERTAINTY_BASICS-B.json`
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/EU-MEASUREMENT_UNCERTAINTY_BASICS-C.json`
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/SRC-MEASUREMENT_UNCERTAINTY_BASICS.json`
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/CTX-MEASUREMENT_UNCERTAINTY_BASICS.json`
- `CONTENT/vertical-slices/measurement-uncertainty-basics/records/SCP-MEASUREMENT_UNCERTAINTY_BASICS.json`

## Source identity reviewed
- NIST Technical Note 1297: https://www.nist.gov/pml/nist-technical-note-1297

## Acceptance status
Three additional Claims have explicit D/E/B scores and rationales. Before any content correction, lock a bounded correction scope, locate source passages, and define regression tests. Continue the remaining Claim scoring and continuous high-consequence checks; perform methodology calibration at 747/1,494; after all Claims are scored, conduct the integrated defect, Relation, evidence-diversity/independence, Human View/adversarial, independent-review, authorized-correction/regression and final exact-head 3/3 CI passes. Survival/offline readiness remains a separate post-M13 phase. M13 remains open and is not CLEAN.
