# M11 Controlled Correction Scope Lock — 2026-10-09

## Status

**SCOPE LOCKED FOR AUDIT; NO CONTENT CORRECTION AUTHORIZED YET.** M11 is isolated on `m11-human-centered-design-2026-10-09`, based on M10 CLEAN HEAD `063fc412a3c72ccccf7d7e298970493a3d448333`. M10 remains accepted CLEAN on its own branch/PR state; `main` and prior accepted checkpoints must remain unchanged.

## Locked targets

1. `accessibility-basics`
2. `ergonomics-basics`
3. `human-factors-basics`

The candidate verification and initial findings are recorded in `M11-INITIAL-GAP-AUDIT-2026-10-09.md`.

## Authorized audit questions

For every existing Claim and its linked Evidence Use:

1. Does the source directly support the Claim at the wording and level of generality used?
2. Does Evidence Use identify the source's relevant contribution rather than merely name the source?
3. Are the inference limits, context and applicability boundaries explicit where needed?
4. Does the Russian-facing README explain the subject and its limits without requiring knowledge of the record architecture?
5. Do dedicated regressions protect the content properties that the audit identifies as material?
6. Does any proposed cross-slice relation express a real, source-bounded dependency rather than topical proximity?

The current evidence-independence screen is a question to resolve, not a requirement to add a second Source to every slice. Any additional source must be independently relevant to a specific Claim and demonstrably improve support. A Claim may be narrowed to fit the existing source instead.

## Permitted correction surface after findings are confirmed

- Existing Claims in the three locked slices, only where the substantive audit confirms a wording, source-fit or applicability defect.
- The nine existing Evidence Use `content.material.description` fields, where claim-specific explanations and limits need correction.
- The three target READMEs, to provide a consistent Russian-facing introduction, a bounded example where useful, and visible applicability limits.
- The three dedicated regression tests, preserving all existing schema, count, provenance and linkage assertions while adding targeted checks for confirmed content requirements.
- The required M11 entry in `RELEASE/EDITORIAL-CORRECTION.json` and M11 planning/audit/debt documents.

## Explicit exclusions and invariants

- No new vertical slice or Record type.
- No new Source, Evidence Use, Context, Scope or Relation in this locked pass. If a substantive/evidence finding cannot be resolved by accurately narrowing or explaining the existing Claims, stop and propose a documented scope amendment before adding records.
- Do not modify existing Context/Scope records, canonical source identities/URLs, record IDs, provenance methods, Claim/source references, evidence roles, target references or Relation participants.
- Preserve `REL-CROSS-MANUFACTURING-HUMAN-FACTORS` exactly.
- No changes to unrelated slices, global architecture, `main`, or accepted M4/M5/M7/M8/M9/M10 checkpoints.
- No source-count quota, unsupported legal/technical requirements, universal ergonomics prescriptions, individualized occupational advice or site-specific accessibility certification.
- No weakened tests, schemas, semantic checks, release gates or offline checks.

## Required sequence

1. Complete claim-by-claim substantive/source-fit audit.
2. Complete Evidence Use/source-boundary audit.
3. Complete Human View/adversarial review for ordinary-reader interpretation.
4. Re-scan all Relation endpoints and confirm the permitted Relation delta is zero.
5. Record confirmed findings only in `M11-UNIFIED-DEBT-MAP-2026-10-09.md`.
6. Implement only the locked corrections; add the exact M11 editorial authorization before changing published records.
7. Re-read all changed records and regression contracts; verify tree counts, coverage, README registry, provenance and exact diff.
8. Run targeted regressions, then Reference implementation tests, Release Conformance Gate and Offline Edition on one identical final HEAD.
9. Independently verify exact HEAD, PR base/head/state, changed-file list, Relation delta and `main`.
10. Record M11 CLEAN only if all substantive and boundary findings are resolved and all three CI workflows pass on the same exact HEAD. Any later commit invalidates the gate and requires a fresh 3/3 run.

PRs remain draft/open/unmerged at checkpoints. A CLEAN acceptance does not authorize merging.
