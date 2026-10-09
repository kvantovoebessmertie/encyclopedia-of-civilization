# M11 Scope Amendment — Human Factors Deferred — 2026-10-09

## Decision

**Approved scope amendment for M11 acceptance only.** The M11 acceptance scope is limited to the two source-verified, authorized correction candidates:

- `accessibility-basics`
- `ergonomics-basics`

The audited candidate `human-factors-basics` is explicitly deferred from M11 acceptance and carried forward as open debt for the next Gap Map / audit wave. This is a scope decision, not a claim that the human-factors content is correct, complete, or accepted.

## Basis

The recorded canonical locator `https://www.nasa.gov/reference/human-factors/` could not be independently retrieved in the source review. Official NASA Human Factors material is available at other URLs, including `https://sma.nasa.gov/sma-disciplines/human-factors` and `https://www.nasa.gov/reference/jsc-human-factors-performance/`, but neither is silently substituted for the recorded Source. Their subject coverage is not treated as proof that the existing Source record's identity and locator have been verified.

The limitation is unresolved, not a confirmed broken URL. Rewriting the existing human-factors Evidence Use descriptions without verified source fit would risk asserting support that has not been established.

## Explicit scope boundary

1. No file under `CONTENT/vertical-slices/human-factors-basics/` is changed by this amendment.
2. Preserve `SRC-HUMAN_FACTORS_BASICS`, its source identity and canonical URL, all existing Claims/Evidence Use records, provenance and references.
3. Preserve Relation `REL-CROSS-MANUFACTURING-HUMAN-FACTORS` exactly; Relation delta remains zero.
4. Keep findings `M11-HF-001`, `M11-HF-002`, `M11-HF-003` and limitation `M11-HF-LIMIT-004` OPEN and explicitly carried forward. They are not counted as resolved by M11.
5. No new Records, Sources, Relations, record types, or content-slice changes are authorized.
6. This amendment does not authorize merging, promotion, edits to `main`, or changes to protected M10 or earlier accepted checkpoints.

## M11 acceptance after amendment

M11 may be marked CLEAN only for its amended, bounded acceptance scope if:

- all eight authorized accessibility/ergonomics findings are substantively corrected and independently reviewed;
- all changed files match the original authorization plus this scope-amendment record and the documentation updates needed to register it;
- corpus coverage, record shapes/counts, source identity/URLs, provenance/linkage, Context/Scope, and Relation tree remain unchanged;
- all three required CI workflows pass on the same exact final HEAD;
- independent final verification confirms PR #19 base/head/state and that `main` is unchanged.

Any later commit invalidates the exact-head CI gate and requires all three workflows to pass again. PR #19 must remain open, Draft, and unmerged.

**Disposition:** M11 human-factors candidate deferred, debt retained; M11 acceptance scope amended, not silently weakened.