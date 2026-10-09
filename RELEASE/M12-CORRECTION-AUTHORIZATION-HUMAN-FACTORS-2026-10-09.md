# M12 Controlled Correction Authorization — Human Factors — 2026-10-09

## Authorization basis

This authorization follows the read-only findings in `M12-INITIAL-GAP-AUDIT-HUMAN-FACTORS-2026-10-09.md` and the exact path lock in `M12-CANDIDATE-VERIFICATION-SCOPE-LOCK-HUMAN-FACTORS-2026-10-09.md`. It authorizes a bounded correction of one pre-existing slice, not slice creation.

## Findings authorized

- `M12-HF-001`: replace the machine-facing README stub with an accessible Russian explanation and applicability boundaries.
- `M12-HF-002`: replace the three generic Evidence Use descriptions with claim-specific descriptions tied to the selected official NASA page.
- `M12-HF-003`: narrow Claim language so it does not exceed the selected source.
- `M12-HF-004`: strengthen the dedicated regression to preserve structure and enforce reader-facing/source-bound content.
- `M12-HF-005`: replace the previously recorded, independently unverified locator with the verified official NASA Johnson Space Center Human Factors & Performance page: https://www.nasa.gov/reference/jsc-human-factors-performance/. The old URL is classified as unverified, not confirmed broken. Preserve Source record ID and source identity; document the locator correction in the audit.

## Authorized behavior

1. Source URL only changes in the existing Source record. Keep `SRC-HUMAN_FACTORS_BASICS`, source identity, record type, provenance method and preservation semantics.
2. Claim A may state that human factors considers human capabilities, limitations and behavior in relation to systems and interfaces, grounded in NASA's description of human-system interactions.
3. Claim B must be narrowed to source-explicit concerns such as workload, usability, fatigue, loss of situation awareness or human error. Do not retain unsupported wording about perception/attention/decision-making unless directly supported by the cited page.
4. Claim C may describe integrating human capabilities and limitations with system design, development and operations, as described by NASA's Human Systems Integration section.
5. Each Evidence Use must specifically describe what the source contributes to its referenced Claim and what it does not establish.
6. README must provide a plain-language Russian entry point, an illustrative example, claim/evidence/source links, and clear educational/applicability boundaries.
7. The regression must check the nine-record profile, IDs/references, source locator, claim-specific Evidence Use, reader-facing text and boundary wording.

## Protected invariants

- Exactly the existing nine Records remain in the slice; no Records are added or deleted.
- No Context, Scope, Relation, cross-slice endpoint, Record type, other slice or architecture changes.
- No record IDs, Claim/Evidence Use refs, evidence roles or provenance methods change.
- The single-source limitation remains explicit. No claim of independent multi-source triangulation is made.
- No changes to `main`, M11's base branch, or protected historical checkpoints.
- PR must remain open/draft/unmerged pending all gates.

## Acceptance gates

1. Review all changed prose against the official NASA page and remove any unsupported claims.
2. Run the dedicated human-factors regression.
3. Verify exact changed paths and all protected invariants against base SHA `d4b4b88d4a6cb1214e5fd1c87b42a468f4b117bb`.
4. Confirm the corpus coverage file is byte-for-byte unchanged and no Relation delta exists.
5. Run Reference implementation tests, Release Conformance Gate and Offline Edition on one identical final HEAD.
6. Independently verify PR state, base/head, exact diff and unchanged `main`.
7. Mark M12 CLEAN only if all findings in this authorized scope are resolved and every gate passes.

**Authorization status: approved for the exact paths in the scope lock. No other files or semantic changes are authorized.**
