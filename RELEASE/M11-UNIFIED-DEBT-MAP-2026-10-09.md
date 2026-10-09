# M11 Unified Debt Map — 2026-10-09

## Status

**CONTROLLED CORRECTION AUTHORIZED; M11 IS OPEN AND NOT CLEAN.** Baseline is the M10 Human View follow-up HEAD `313b5dc663e032da0e7499829fd55aaf2a1ee157`. Working branch: `m11-gap-map-after-m10-human-view-2026-10-09`. The exact correction surface is defined by `M11-CORRECTION-AUTHORIZATION-2026-10-09.md`.

## Confirmed findings

### M11-ACC-001 — accessibility README does not orient an ordinary reader
**Status: OPEN — AUTHORIZED.** Add a concise Russian explanation, one clearly illustrative example and the international-framework/local-criteria boundary.

### M11-ACC-002 — accessibility Evidence Use is generic
**Status: OPEN — AUTHORIZED.** Rewrite each of the three existing descriptions to identify its claim-specific support and limitations.

### M11-ACC-003 — international framework versus local criteria is not explained
**Status: OPEN — AUTHORIZED.** Explain that the Convention supplies an international framework and calls for standards/guidelines, but does not certify a particular local design or exhaust applicable technical requirements. Do not change the existing Claim in this pass.

### M11-ACC-004 — accessibility regression lacks content contracts
**Status: OPEN — AUTHORIZED.** Preserve all existing assertions and add tests for the README explanation, claim-specific Evidence Use and local-applicability boundary.

### M11-ERG-001 — ergonomics README is not a reader-facing Russian introduction
**Status: OPEN — AUTHORIZED.** Explain the fit between work demands and worker capabilities, and mark the slice as educational rather than a complete workplace assessment.

### M11-ERG-002 — ergonomics Evidence Use is generic
**Status: OPEN — AUTHORIZED.** Explain the source contribution and limits separately for each Claim.

### M11-ERG-003 — ergonomics Claim C exceeds the recorded overview
**Status: OPEN — AUTHORIZED.** Narrow Claim C to identifying, analyzing and controlling workplace risk factors. The source's overview does not itself define an effectiveness-evaluation protocol.

### M11-ERG-004 — ergonomics regression lacks content contracts
**Status: OPEN — AUTHORIZED.** Retain structural/linkage assertions and add checks for claim-specific evidence, bounded Claim C and the README boundary.

### M11-HF-001 — human-factors README lacks an accessible reader journey
**Status: OPEN — AUTHORIZED.** Add a plain-language Russian orientation and a boundary against treating spaceflight-oriented material as universal requirements.

### M11-HF-002 — human-factors Evidence Use is generic
**Status: OPEN — AUTHORIZED.** Clarify the intended contribution and limits for each Claim without expanding beyond verifiable source support.

### M11-HF-003 — human-factors regression lacks content contracts
**Status: OPEN — AUTHORIZED.** Retain current shape/linkage checks and add checks for claim-specific explanations and domain/applicability boundaries.

## Source-verification limitation

### M11-HF-LIMIT-004 — exact NASA locator not independently retrieved
**Status: LIMITATION RECORDED; NOT A CONFIRMED SOURCE FAILURE.** Preserve the recorded canonical URL and source identity. A related official NASA Human Factors & Performance page is available, but it is not silently substituted for the recorded Source. If source fit cannot be established in post-correction review, stop and request a scope amendment.

## Structural and protected invariants

- Three existing slices only: `accessibility-basics`, `ergonomics-basics`, `human-factors-basics`.
- No new/deleted Records, Sources, Context, Scope, Relations or record types.
- No Relation participant changes; preserve `REL-CROSS-MANUFACTURING-HUMAN-FACTORS`.
- No source identity/URL, record ID, provenance method, claim/source reference, evidence role or target reference changes.
- Corpus structure and coverage must remain unchanged.
- Human View review is desk-based; no live novice study is claimed.
- No source-count quota or unsupported site-specific, legal, medical or workplace-risk advice.

## Acceptance gates

1. Resolve all authorized findings and re-read every changed Claim, Evidence Use, README and regression.
2. Confirm the NASA limitation has not been converted into an unsupported source claim.
3. Confirm the exact changed-file list matches the authorization.
4. Verify unchanged coverage, source identity/URLs, provenance/linkage, Context/Scope and Relation tree.
5. Run the three targeted regressions, then Reference implementation tests, Release Conformance Gate and Offline Edition on one identical final HEAD.
6. Independently verify PR base/head/state, exact diff, Relation delta and unchanged `main`.
7. Record CLEAN only if every substantive finding is resolved and all three workflows pass on the same exact HEAD. Any later commit invalidates that gate.

**Current decision: M11 OPEN; correction scope authorized; no correction is yet accepted as complete.**
