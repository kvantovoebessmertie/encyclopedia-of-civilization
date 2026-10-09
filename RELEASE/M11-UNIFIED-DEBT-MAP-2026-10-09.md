# M11 Unified Debt Map — 2026-10-09

## Status

**AUDITS COMPLETE; CONTROLLED CORRECTION REQUIRED. M11 IS NOT CLEAN.** This map consolidates only findings confirmed by the M11 candidate, substantive, evidence and Human View reviews. All corrections must remain inside `M11-CORRECTION-SCOPE-LOCK-2026-10-09.md`.

## Finding ledger

### M11-SUB-001 — accessibility Claim C needs a clearer international/local boundary
**Status: CONFIRMED — OPEN.**
Clarify that the UN Convention supplies an international framework and does not itself certify a specific local design or exhaust applicable technical/legal requirements.

### M11-SUB-002 — ergonomics Claim C exceeds the directly described process
**Status: CONFIRMED — OPEN.**
Narrow the Claim to identifying, analyzing and controlling ergonomic risk factors, which is the process directly described by the recorded NIOSH overview.

### M11-EV-003 — generic Evidence Use across three human-centered slices
**Status: CONFIRMED — OPEN.**
All nine existing Evidence Use descriptions use generic formulae and do not distinguish claim-specific support and limits. Rewrite the descriptions without changing IDs, refs, roles, provenance, source identities or URLs.

### M11-HV-004 — READMEs do not provide consistent Russian-facing orientation
**Status: CONFIRMED — OPEN.**
Accessibility and human-factors READMEs are English-only; ergonomics README is predominantly English. Add short Russian orientation and explicit educational/applicability limits.

### M11-REG-005 — regressions protect structure but not explanatory quality
**Status: CONFIRMED — OPEN.**
The three dedicated regressions validate counts/types/linkage but do not guard the content properties found by this audit. Strengthen them without weakening any existing assertions.

### M11-SOURCE-LIMIT-006 — direct NASA locator not independently retrieved
**Status: LIMITATION RECORDED; NOT A CONFIRMED SOURCE FAILURE.**
The current external fetch could not retrieve the recorded NASA locator. This is not evidence that the URL is broken. Preserve the locator in this pass; if source fit cannot be established during post-correction review, stop and propose a separate scope amendment rather than asserting support or silently replacing the source.

## Scope and structural invariants

- Three existing slices only: `accessibility-basics`, `ergonomics-basics`, `human-factors-basics`.
- No new/deleted Records, Sources, Context, Scope, Relations or Record types are authorized.
- No Relation participants change; preserve `REL-CROSS-MANUFACTURING-HUMAN-FACTORS`.
- No canonical source identity/URL, record ID, provenance method, claim/source reference, evidence role or target reference changes.
- Corpus structure and coverage must remain unchanged by the correction pass.
- Human View remains a desk audit; no live novice study is claimed.

## Acceptance gates

1. Resolve all confirmed findings above and re-read every changed Claim, Evidence Use, README and regression.
2. Confirm the direct NASA locator limitation has not been converted into an unsupported source claim; if it blocks source fit, amend scope before proceeding.
3. Confirm the exact changed-file list contains only the authorized three slices, their dedicated regressions, the required M11 editorial authorization and M11 audit records.
4. Verify unchanged coverage, source identity/URLs, provenance/linkage, Context/Scope and Relation tree.
5. Run the three targeted regressions, then Reference implementation tests, Release Conformance Gate and Offline Edition on one identical final HEAD.
6. Independently verify PR base/head/state, diff, Relations and unchanged `main`.
7. Record CLEAN only if every substantive finding is resolved and all three CI workflows pass on the same exact HEAD. Any later commit invalidates that gate.
