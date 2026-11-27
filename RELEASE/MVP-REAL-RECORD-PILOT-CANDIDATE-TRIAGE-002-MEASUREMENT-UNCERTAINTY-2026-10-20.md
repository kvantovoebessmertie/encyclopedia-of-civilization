# MVP real-record pilot — candidate triage 002: measurement uncertainty

Date: 2026-10-20  
Branch: `mvp-reader-prototype-2026-10-11`  
State: **HOLD — candidate review only; not approved for pilot**

## Candidate identity

- Claim: `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- Evidence Use: `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- Source: `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1`
- Additional independent terminology reference: `SRC-BIPM-VIM-MEASUREMENT-UNCERTAINTY@1` is linked through `EU-MEASUREMENT_UNCERTAINTY_BIPM@1` to Claim B, not to Claim A. Do not silently count that separate chain as support for Claim A.

Claim statement:

> Результат измерения должен интерпретироваться вместе с оценкой его неопределённости.

## Passage-level review

The currently linked NIST source record points to the general landing page for NIST Technical Note 1297. The direct, claim-relevant passage is in NIST TN 1297, section 2.1, “Classification of Components of Uncertainty”:

https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty

Section 2.1 states that a measurement result is an approximation or estimate of the measurand and is complete only when accompanied by a quantitative statement of its uncertainty. This directly supports the core of the Claim. NIST section 7 also specifies how uncertainty should be reported:

https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty

The BIPM/JCGM VIM definition separately describes measurement uncertainty as a non-negative parameter characterizing the dispersion of values attributed to a measurand, based on the information used:

https://jcgm.bipm.org/vim/en/2.26.html

However, the VIM Source and Evidence Use currently link to Claim B, so this is context for the topic, not a valid additional evidence link for Claim A without an authorized record change.

## Preliminary D/E/B assessment

- **D=1** — foundational metrology concept; the Claim is explanatory rather than an operational safety instruction.
- **E=2** — the NIST primary source contains a direct passage supporting the core proposition, but the canonical Source record points only to the broader TN 1297 landing page and the canonical Evidence Use has no section locator.
- **B=1** — the statement is concise and plausible, but the stored evidence chain does not preserve the exact passage and the separate BIPM chain belongs to a different Claim.

These are candidate-screening scores, not an independent final adjudication.

## Decision

**HOLD — promising low-complexity candidate; not approved for a real-record pilot.**

Required before reconsideration:

1. Add an exact NIST section locator to the appropriate Evidence Use record only through the authorized, versioned correction workflow.
2. Confirm the precise wording and scope in the final reader view, with a visible source link and no stronger claim than the passage supports.
3. Record the project's rights/attribution determination for this NIST material and intended distribution model; do not infer legal clearance solely from public accessibility.
4. Obtain independent review against the exact candidate commit.
5. Add the exact ID/version to a pilot allowlist only after approval; then run reproducible build and release gates on the exact candidate commit.

No canonical Claim, Evidence Use, or Source JSON was changed during this triage. This report does not authorize publication or inclusion in the pilot allowlist.
