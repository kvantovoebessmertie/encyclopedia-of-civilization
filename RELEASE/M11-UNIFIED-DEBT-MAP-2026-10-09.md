# M11 Unified Debt Map — 2026-10-09

## Status

**ACCESSIBILITY AND ERGONOMICS CORRECTIONS IMPLEMENTED; FINAL VERIFICATION PENDING. HUMAN-FACTORS FINDINGS REMAIN OPEN AND ARE DEFERRED FROM M11 ACCEPTANCE BY EXPLICIT SCOPE AMENDMENT.** Baseline is the M10 Human View follow-up HEAD `313b5dc663e032da0e7499829fd55aaf2a1ee157`. Working branch: `m11-gap-map-after-m10-human-view-2026-10-09`. Correction surface is defined by `M11-CORRECTION-AUTHORIZATION-2026-10-09.md` and `M11-SCOPE-AMENDMENT-HUMAN-FACTORS-DEFERRED-2026-10-09.md`.

## Confirmed findings

### M11-ACC-001 — accessibility README does not orient an ordinary reader
**Status: CORRECTION IMPLEMENTED; POST-CORRECTION VERIFICATION PENDING.** Add a concise Russian explanation, one clearly illustrative example and the international-framework/local-criteria boundary.

### M11-ACC-002 — accessibility Evidence Use is generic
**Status: CORRECTION IMPLEMENTED; POST-CORRECTION VERIFICATION PENDING.** Rewrite each of the three existing descriptions to identify its claim-specific support and limitations.

### M11-ACC-003 — international framework versus local criteria is not explained
**Status: CORRECTION IMPLEMENTED; POST-CORRECTION VERIFICATION PENDING.** Explain that the Convention supplies an international framework and calls for standards/guidelines, but does not certify a particular local design or exhaust applicable technical requirements. Do not change the existing Claim in this pass.

### M11-ACC-004 — accessibility regression lacks content contracts
**Status: CORRECTION IMPLEMENTED; POST-CORRECTION VERIFICATION PENDING.** Preserve all existing assertions and add tests for the README explanation, claim-specific Evidence Use and local-applicability boundary.

### M11-ERG-001 — ergonomics README is not a reader-facing Russian introduction
**Status: CORRECTION IMPLEMENTED; POST-CORRECTION VERIFICATION PENDING.** Explain the fit between work demands and worker capabilities, and mark the slice as educational rather than a complete workplace assessment.

### M11-ERG-002 — ergonomics Evidence Use is generic
**Status: CORRECTION IMPLEMENTED; POST-CORRECTION VERIFICATION PENDING.** Explain the source contribution and limits separately for each Claim.

### M11-ERG-003 — ergonomics Claim C exceeds the recorded overview
**Status: CORRECTION IMPLEMENTED; POST-CORRECTION VERIFICATION PENDING.** Narrow Claim C to identifying, analyzing and controlling workplace risk factors. The source's overview does not itself define an effectiveness-evaluation protocol.

### M11-ERG-004 — ergonomics regression lacks content contracts
**Status: CORRECTION IMPLEMENTED; POST-CORRECTION VERIFICATION PENDING.** Retain structural/linkage assertions and add checks for claim-specific evidence, bounded Claim C and the README boundary.

### M11-HF-001 — human-factors README lacks an accessible reader journey
**Status: OPEN — DEFERRED FROM M11 ACCEPTANCE; NOT AUTHORIZED IN THIS PASS.** Do not edit the human-factors slice in M11. The explicit scope amendment carries this debt forward without asserting source fit or changing the recorded Source.

### M11-HF-002 — human-factors Evidence Use is generic
**Status: OPEN — DEFERRED FROM M11 ACCEPTANCE; NOT AUTHORIZED IN THIS PASS.** The descriptions remain generic and require a future evidence-preserving correction after source fit is established.

### M11-HF-003 — human-factors regression lacks content contracts
**Status: OPEN — DEFERRED FROM M11 ACCEPTANCE; NOT AUTHORIZED IN THIS PASS.** Do not add assertions that imply source support before the source-fit issue is resolved.

## Source-verification limitation

### M11-HF-LIMIT-004 — exact NASA locator not independently retrieved
**Status: OPEN LIMITATION; NOT A CONFIRMED SOURCE FAILURE.** Preserve the recorded canonical URL and source identity. Related official NASA Human Factors pages are available, but none is silently substituted for the recorded Source. This limitation and findings M11-HF-001/002/003 are explicitly deferred by `M11-SCOPE-AMENDMENT-HUMAN-FACTORS-DEFERRED-2026-10-09.md` and remain open for the next wave.

## Structural and protected invariants

- Two slices authorized for correction and M11 acceptance: `accessibility-basics` and `ergonomics-basics`. `human-factors-basics` is explicitly deferred from this wave's acceptance; its debts remain open and are not counted as resolved.
- No new/deleted Records, Sources, Context, Scope, Relations or record types. No human-factors slice file may be changed in this pass. The scope-amendment document is audit metadata only.
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
7. Record CLEAN only if every finding in the amended M11 acceptance scope is resolved, the deferred human-factors debts are explicitly retained as OPEN, and all three workflows pass on the same exact HEAD. Any later commit invalidates that gate.

**Current decision: amended M11 scope awaits final verification. Accessibility/ergonomics corrections are implemented. Human-factors debts remain OPEN and deferred, not resolved or accepted. No CLEAN decision until exact-head 3/3 CI and independent verification pass.**
