# PR #22 — Exact-Head CI Failure Analysis and Bounded Remediation

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Failing inspection HEAD: `47f65a506bd13eaa913ba7ce1414c67e11d3714a`  
PR #22: OPEN / DRAFT / NOT MERGED

## Result

The exact-head CI run completed with two workflows passing and two failing:

- Offline Edition — PASS.
- MVP Contribution Form Browser Tests — PASS.
- Reference implementation tests — FAIL: 1,002 passed, 4 failed.
- Release Conformance Gate — FAIL; final conformance state PARTIAL.

The Release Gate preflight passed with 4,742 records, 479 slices, 4,742 unique record identities and 19 record types. The failures occurred in four pytest assertions, not in JSON parsing, schema validation or content preflight.

## Four failing assertions

1. `test_adversarial_full_corpus_is_schema_and_semantically_clean` and
   `test_full_corpus_has_no_duplicate_ids_and_expected_shape` compared the number of unique `record_id` values with the total record count. The canonical record model is versioned: identity is the pair `(record_id, record_version)`. The corpus intentionally preserves the historical FEMA Source @1 alongside the corrected Source @2, so the same logical record ID occurs at two distinct versions. Preflight correctly counted 4,742 unique versioned record identities. The tests are corrected to assert uniqueness of the pair, not to remove a historical version or weaken schema validation.

2. `test_relation_context_frames_are_target_specific` assumed every target-specific Context remained at version 1. The Library/Archival Relation has been validly versioned to Relation @6 with Context @3. The regression now resolves the exact Context version named by each Relation's `frame_ref` and checks its exact target, rather than hard-coding @1.

3. `test_cross_slice_audit_artifact_matches_current_corpus` found a stale audit count of 4,741. The coverage manifest and actual corpus both contain 4,742 records / 479 slices. The audit artifact count and its scope description are synchronized.

## Bounded changes in the remediation commit

- Corrected two corpus identity assertions to use `(record_id, record_version)`.
- Corrected the Relation/Context regression to resolve the exact referenced Context version.
- Synchronized `CONTENT-CROSS-SLICE-AUDIT.json` with the 4,742-record corpus.
- Recorded owner decisions E-Q1 and W-Q3 in the owner decision packet and Priority Closure Board.

## Explicit non-changes

- No canonical JSON records were changed.
- No historical Source snapshot was rewritten or deleted.
- No Standard or JSON Schema requirement was relaxed.
- No Event, Object, State, Relation, Context, Claim, Source or Evidence Use semantics were changed.
- No INCLUDE/HOLD/EXCLUDE state was changed beyond recording the owner's explicit release-scope exclusions for the two specified Relations/Event.
- No first-edition allowlist was created or modified.
- `main` remains untouched; PR #22 remains Draft.

## Required verification

Run Reference Tests, Release Conformance Gate, Offline Edition and MVP Contribution Form Browser Tests on one exact immutable post-remediation HEAD. Do not claim conformance until all four report PASS on that same SHA.
