# MVP real-record pilot — rights and locator screen 005: measurement uncertainty

Date: 2026-11-13  
Branch: `mvp-reader-prototype-2026-10-11`  
State: **CONDITIONAL RIGHTS SCREEN — candidate remains HOLD; no pilot authorization**

## Candidate identity
- Claim: `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- Evidence Use: `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1`
- Source: `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1`
- Claim text: «Результат измерения должен интерпретироваться вместе с оценкой его неопределённости.»

## Exact source fit
The current Source points to the NIST TN 1297 overview. The directly relevant official section is:
- Section 2.1, “Classification of Components of Uncertainty”: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty
- Section 7, “Reporting Uncertainty”: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty

Section 2.1 states that a measurement result is complete only when accompanied by a quantitative statement of its uncertainty. This directly supports the core Claim. Section 7 explains what should be reported with the measurement result. The existing Evidence Use still lacks these pinpoint locators; the source-fit defect remains in the canonical chain.

## Rights and attribution screen
Official NIST guidance says NIST publications, as publications of the U.S. federal government, are generally in the public domain and not subject to copyright in the United States, and recommends crediting NIST with the credit line: “Reprinted courtesy of the National Institute of Standards and Technology, U.S. Department of Commerce. Not copyrightable in the United States.”
- NIST Research Library FAQ: https://www.nist.gov/nist-research-library/library-faqs
- NIST copyrights and disclaimers: https://www.nist.gov/copyrights-disclaimers

The general rule is not unlimited: NIST says material marked as copyrighted may have separate terms. U.S. government-work status also does not itself settle copyright treatment in every foreign jurisdiction. See 17 U.S.C. §105 and the U.S. Government Publishing Office explanation:
- https://www.govinfo.gov/about/policies
- https://www.govinfo.gov/content/pkg/USCODE-2024-title17/html/USCODE-2024-title17-chap1-sec105.htm

For this candidate, the proposed MVP treatment should therefore be limited to:
1. Displaying the project's own short Russian paraphrase of the Claim, not copying NIST paragraphs, figures, tables, or PDF pages.
2. Linking directly to the official NIST section and identifying the source as NIST Technical Note 1297, 1994 Edition, by Barry N. Taylor and Chris E. Kuyatt.
3. Including a clear source attribution and a note that NIST is the source, not a project sponsor or endorser.
4. Rechecking the specific source page for any third-party marked content before reproducing anything beyond a link and bibliographic metadata.

This is a documented preliminary rights screen, not legal advice or a final project-wide rights policy. It does not resolve territorial rights outside the United States, all project licensing questions, or the rights status of unrelated records.

## Reader and data-chain consequences
- The current Source identity text is not a bibliographic identity; it is a paraphrase of the subject matter. A versioned correction should use the actual title, authors, institution, edition/date and official URL.
- The current Evidence Use description is generic. A versioned correction should identify section 2.1 as the direct pinpoint and section 7 only as supplementary reporting guidance.
- No canonical record change is authorized by this report. Use the existing bounded editorial authorization process before changing Source or Evidence Use records.
- The reader preview may not include this record as an approved pilot record until the exact record chain is corrected, the exact ID/version is explicitly allowlisted, and an independent reviewer signs off against the same commit.

## Decision
**HOLD — technically and substantively promising, with a comparatively favorable U.S. government-source rights position, but not approved for a real-record pilot or public release.**

Remaining gates:
1. Bounded authorization and versioned Source/Evidence Use correction.
2. Regression test for exact Claim → Evidence Use → Source links and pinpoint.
3. Exact-version preview allowlist and reproducible build.
4. Rendered artifact inspection confirming attribution, source link, scope and no loss of the technical record view.
5. Independent reviewer sign-off and project-level editorial/territorial rights decision.
6. Exact-head Reference Tests, Release Conformance Gate, Offline Edition and preview workflow success.

## Change log
- Canonical Claim/Evidence Use/Source JSON changed: no.
- Real-record preview allowlist changed: no.
- Public or hosted deployment: no.
- Publication approval: no.
