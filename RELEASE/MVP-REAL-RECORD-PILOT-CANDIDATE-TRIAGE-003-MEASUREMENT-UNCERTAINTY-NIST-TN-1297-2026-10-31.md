# MVP real-record pilot — candidate triage 003: measurement uncertainty

Date: 2026-10-31  
Branch: `mvp-reader-prototype-2026-10-11`  
State: **HOLD — candidate review only; not approved for pilot**

## Candidate identity

- Claim: `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- Evidence Use: `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- Source: `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1`
- Review target: the exact records present on the current MVP prototype branch; no canonical record is modified by this triage.

Claim statement:

> Результат измерения должен интерпретироваться вместе с оценкой его неопределённости.

## Passage-level assessment

The current Source record points to the general landing page for NIST Technical Note 1297 and the current Evidence Use contains only a generic description. The NIST source itself contains a directly relevant passage in section 2.1, “Classification of Components of Uncertainty,” stating that a measurement result is complete only when accompanied by a quantitative statement of its uncertainty. Section 7, “Reporting Uncertainty,” describes reporting requirements.

Relevant authoritative locators:
- NIST TN 1297 section 2.1: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty
- NIST TN 1297 section 7: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty

The section 2.1 passage directly supports the core of the Claim. However, the exact locator is not preserved in the current canonical Evidence Use, so the reader would not yet have the required claim-specific evidence trail. The additional BIPM/JCGM VIM chain elsewhere in the corpus is linked to a different Claim and is not counted as evidence for this candidate.

## Preliminary D/E/B screening

- **D=1** — foundational metrology concept; the Claim is explanatory, not an operational safety instruction.
- **E=2** — NIST TN 1297 has direct supporting text, but the current canonical Source record is broad and Evidence Use has no pinpoint.
- **B=1** — the proposition is narrow and plausible, but the stored evidence chain is not yet precise enough for release.

These are screening scores, not an independent final adjudication.

## Rights, attribution and distribution

No NIST text or graphic is copied into the reader by this triage. Public accessibility alone is not recorded as legal clearance. The project still needs a documented determination covering the intended use, attribution/linking, any copied or adapted material, and the planned distribution model. No rights determination is inferred here.

## Decision

**HOLD — promising low-complexity candidate; not approved for a real-record pilot.**

Before reconsideration:
1. Use the authorized, versioned correction workflow to add a precise NIST section locator to the appropriate Evidence Use, if that change is approved.
2. Verify that the reader summary preserves the limited meaning of the source and visibly links to it.
3. Record the rights/attribution decision for the actual distribution model.
4. Obtain independent review against the exact candidate commit.
5. Add the exact ID/version to a pilot allowlist only after every applicable gate passes; rebuild and run all release checks on that exact commit.

No canonical Claim, Evidence Use or Source JSON changed in this triage. This report does not authorize a pilot allowlist, publication, or public release.
