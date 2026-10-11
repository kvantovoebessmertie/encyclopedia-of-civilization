# MVP pilot candidate review — formal methods basics (source-to-Claim pinpoint screen)

Date: 2026-10-11
Branch: `mvp-public-contribution-design-2026-10-11`
Status: **promising low-consequence educational candidate; HOLD for pilot approval until exact evidence pinpoints, rights/attribution and Human View gates are recorded**

## 1. Why this candidate was screened

The formal-methods slice is introductory, non-procedural educational content and is a plausible pilot candidate. It is not approved merely because its records say `published` / `complete` or because CI passes. The current slice contains three Claims, each linked to the same NASA Langley source through a separate Evidence Use record.

## 2. Canonical records inspected

- `CLM-FORMAL_METHODS_BASICS-A@1`: formal methods use mathematically rigorous techniques for specification, design and verification of software and hardware systems.
- `CLM-FORMAL_METHODS_BASICS-B@1`: model checking and theorem proving can verify system properties relative to a formal specification.
- `CLM-FORMAL_METHODS_BASICS-C@1`: full formal verification of large systems is limited by state-space complexity, so abstraction and restricted verification scope are often used.
- Evidence Use records: `EU-FORMAL_METHODS_BASICS-A@1`, `EU-FORMAL_METHODS_BASICS-B@1`, `EU-FORMAL_METHODS_BASICS-C@1`.
- Source: `SRC-FORMAL_METHODS_BASICS@1`, NASA Langley, “What is Formal Methods?”:
  https://shemesh.larc.nasa.gov/fm/fm-what.html

All three Evidence Use records correctly identify their corresponding Claim and the same Source, but each description is generic and contains no reproducible pinpoint.

## 3. Direct source-to-Claim screen

Checked source page: NASA Langley, “What is Formal Methods?”, last updated 2024-03-12.

| Claim | Exact source location | Fit | Boundary / follow-up |
|---|---|---|---|
| A | Heading “What is Formal Methods?”, opening definition (page text, paragraph 1): formal methods are described as mathematically rigorous techniques for specification, design and verification of software and hardware systems. | Strong direct support | Claim closely follows the definition. Keep “mathematically rigorous” and do not imply that use of formal methods guarantees whole-system correctness in practice. |
| B | Same page, paragraph 1 on formal verification as deductions in mathematical logic; paragraph 2 bullet/example on automated verification and a theorem prover (page text around the theorem-prover example). | Partial-to-strong support for the general role of formal verification; pinpoint is needed for the specific “model checking” term. | Current wording combines model checking and theorem proving. The NASA page is direct for theorem-prover examples and state-space examination, but the exact “model checking” terminology should be verified against a specific source passage or a second authoritative source before approval. |
| C | Same page, paragraph 2: real systems have enormous state spaces; listed mitigations include abstraction to requirements/high-level designs, focusing on critical components, reducing model ranges, hierarchical analysis and automation. | Strong direct support | Wording appropriately says “often”; retain the practical limitation and avoid suggesting formal verification is impossible for large systems in all circumstances. |

The source page is a specific technical explanation, unlike a general institutional landing page. The exact HTML paragraph locator should be converted into a stable source pinpoint convention supported by the repository (heading + paragraph/bullet label, or another durable locator) before canonical Evidence Use is changed.

## 4. Rights and attribution

- The pilot would link to and paraphrase the source, not copy its text or diagrams.
- Confirm the rights/attribution basis for the exact NASA-hosted page and any linked material before publication; do not assume that every linked item inherits NASA’s rights status.
- Record the intended edition’s licensing model and the source attribution in the pilot decision log. The project’s own publication license/terms are still a separate release gate.

## 5. Eligibility decision

**Current decision: HOLD — candidate for a reviewed pilot, not yet eligible.**

| Gate | Status | Reason |
|---|---|---|
| Identity and versioned links | PASS for the three inspected Claim/Evidence Use/Source links | Each EU points to its intended Claim and the common Source. |
| Claim/source fit | PARTIAL | A and C have direct support; B needs an explicit model-checking pinpoint or a supplemental source. |
| Exact Evidence Use pinpoint | FAIL | Existing EU descriptions are generic; no stable paragraph/bullet pinpoint is recorded. |
| Rights and attribution | UNKNOWN | Must be recorded for the intended public edition. |
| Human View | UNKNOWN | No release-candidate rendered artifact has been reviewed for this exact real-record bundle. |
| Exact-version manifest / hashes | FAIL | No real-record allowlist has been approved; current reader remains synthetic-fixture-only. |
| Editorial owner approval | UNKNOWN | No named owner sign-off recorded. |

No real-record preview allowlist was created. No canonical Claim, Evidence Use, Source, Context or Scope record was changed.

## 6. Next actions to close this candidate

1. Find and verify an authoritative, claim-specific locator for model checking in Claim B, or narrow the wording only through a separately reviewed versioned change.
2. Record stable claim-specific pinpoints for all three Evidence Use records, preserving the prior versions and audit history.
3. Record rights/attribution and the public edition license decision.
4. Build a preview from exact record versions only after the editorial owner approves them; inspect the rendered page, source navigation, boundaries and language with a non-specialist reviewer.
5. Record exact source revision, record hashes, output hash, Human View findings and sign-off in the candidate register.
6. Re-run the Reference Tests, Release Conformance Gate and Offline Edition on the exact release candidate.

## 7. Release accounting

- Candidate Claims screened: 3.
- Claims approved for public pilot: 0.
- Evidence Uses with exact pinpoints recorded canonically: 0/3.
- Real-record preview allowlist changes: 0.
- Canonical record changes: 0.
