# M13 Corpus Inventory Baseline — 2026-10-09

## Status

**INITIAL TREE CENSUS VERIFIED; semantic/type/registry reconciliation remains OPEN.** This file records what has actually been counted and what remains to be inspected. It does not claim that all Record types or the audit findings have been independently validated.

## Frozen baseline

- Starting candidate SHA: `e87e5bba60c9ed1101ecd4d53493c968c4760dac`
- Tree API response SHA: the same exact SHA; `truncated=false`.
- M13 branch: `m13-system-wide-depth-audit-2026-10-09`
- Parent branch: `m12-human-factors-source-and-human-view-2026-10-09`
- M12 PR #20: open, draft, unmerged; head is `e87e5bba60c9ed1101ecd4d53493c968c4760dac`; base is `d4b4b88d4a6cb1214e5fd1c87b42a468f4b117bb`.
- `main`: `203a7028e08da394fd44630fe38727be07bc8849`; unchanged at baseline.
- Starting SHA has successful PR-triggered workflows on the same exact HEAD:
  - Reference implementation tests: run #37956929834 — success.
  - Release Conformance Gate: run #37956929827 — success.
  - Offline Edition: run #37956929835 — success.
- These runs validate the frozen starting candidate only. Any M13 commit requires fresh exact-head results before M13 closure.

## Independently counted from the recursive Git tree

The recursive tree for the frozen SHA was complete (`truncated=false`). Path-pattern census:

| Inventory item | Count | Basis |
|---|---:|---|
| Direct slice directories under `CONTENT/vertical-slices/` | 483 | Tree paths |
| Slice README files | 483 | Tree paths |
| JSON files directly under each slice's `records/` directory | 4,831 | Tree paths |
| `RELEASE/` files | 291 | Tree paths; includes historical audit artifacts |
| Claim-named files with `CLM-` prefix | 1,494 | Filename prefix only; actual JSON `type` still must be read |
| Context-named files with `CTX-` prefix | 484 | Filename prefix only |
| Scope-named files with `SCP-` prefix | 483 | Filename prefix only |
| Relation-named files with `REL-` prefix | 64 | Filename prefix only |
| Source-named files with `SRC-` prefix | 608 | Filename prefix only; not a Record-type census |
| Evidence-Use-named files with `EU-` prefix | 1,645 | Filename prefix only; not a Record-type census |

**Important:** filename prefixes are useful for inventory only; they are not authoritative Record types. There are 33 record JSON filenames whose prefixes do not match the simple prefix map used in this first pass. This is not automatically a defect: actual JSON `type` fields must be inspected before determining whether the names are valid, exceptional, or erroneous. The 608 `SRC-` and 1,645 `EU-` filename counts therefore must not be mistaken for Source/Evidence Use type counts.

## Coverage registry as currently recorded

`RELEASE/CONTENT-COVERAGE.json` declares:

- 483 vertical slices;
- 4,831 total records;
- 19 Record types, with all 19 declared as directly covered;
- 1,494 Claims;
- 617 Sources;
- 1,669 Evidence Use records;
- 64 Relations;
- 484 Context records;
- 483 Scope records.

The tree count confirms the top-line slice and JSON totals. The per-type counts above remain **declared registry values, not yet independently reconciled against every JSON `type` field**. The file's `content_corpus_version` is `3.53-m8-post-correction-audit-candidate` and its `audit_touch` field ends with M8 activity. Since M9–M12 contain later audit/correction work, M13 must determine whether these fields are intended as historical provenance or are stale release metadata. Do not edit the coverage file merely to make its labels look current; first establish its governing contract and whether a real discrepancy exists.

## Prior audit authority reviewed

The following current-branch documents were read as context for the new audit:

- `RELEASE/READINESS-ROADMAP-2026-10-05.md`: depth, evidence diversity, integration and Human View precede new breadth; no single completion percentage.
- `RELEASE/M8-DEPTH-MEASUREMENT-PROTOCOL-2026-10-09.md`: D/E/B scoring and claim-level denominator; previous 12-slice/43-Claim audit is diagnostic only.
- `RELEASE/M8-DEPTH-AND-COVERAGE-GAP-MAP-2026-10-09.md`: historical M8 status and correction evidence; its pending-state text must not be treated as current M13 state.
- `RELEASE/M9-UNIFIED-DEBT-MAP-2026-10-09.md`, `M10-UNIFIED-DEBT-MAP-2026-10-09.md`, `M11-UNIFIED-DEBT-MAP-2026-10-09.md`, and `M12-UNIFIED-DEBT-MAP-2026-10-09.md`: findings, scoped dispositions, residual limitations and exact-head acceptance rules.
- `RELEASE/M10-POST-CORRECTION-AUDIT-2026-10-09.md`, `M11-INITIAL-GAP-AUDIT-2026-10-09.md`, and `M12-POST-CORRECTION-AUDIT-HUMAN-FACTORS-2026-10-09.md`: concrete audit examples and explicit limitations, including desk-based rather than live usability review.

Historical records contain status statements for earlier SHAs and branches. M13 must use the actual current tree and current workflow/PR state, not copy forward an old “CLEAN”, “OPEN”, or “pending” label without revalidation.

## Open reconciliation tasks

1. Read each of the 4,831 JSON files (or an equivalently complete machine-verifiable export) and tally the actual `type` field; validate required fields and schema where the existing test contract permits.
2. Build a per-slice manifest of all record IDs/types and count Claims, Sources, Evidence Use, Context, Scope and Relations by actual JSON type.
3. Resolve the 33 nonstandard filename-prefix cases by inspecting their JSON type and ID; classify each as valid naming variation or confirmed mismatch.
4. Reconcile actual type totals to `CONTENT/CONTENT-COVERAGE.json`, all slice/record registries and the relevant Standard/implementation checks.
5. Inventory each Claim's linked Evidence Use and Source references; identify orphaned, duplicate, missing or cross-slice references without assuming that every unlinked record is invalid.
6. Build a source-to-claim linkage manifest, preserving Source identity, canonical locator, provenance and the scope of the actual source.
7. Inventory all Context/Scope targets and all 64 Relation endpoints/justifications; identify missing or ambiguous targets.
8. Reconcile the current editorial authorization registry and dedicated regressions against the later M9–M12 changed slices and their actual diffs.
9. Review all M9–M12 debt maps against current content; distinguish resolved items, open residuals, historical process notes and claims that still need independent verification.
10. Produce a frozen risk-screen candidate list and fixed, non-overlapping Claim audit batches before assigning D/E/B scores.

## Current conclusion

The tree establishes that the corpus has 483 slice directories, 483 slice READMEs and 4,831 record JSON files at the frozen SHA. It does **not yet establish** that all 4,831 JSON records conform semantically, that all type counts are correct, that every Claim is adequately explained/supported/bounded, or that the reader-facing material is usable. Those are the questions M13 is authorized to investigate.
