# M13 — historical Claim-version recovery worklist (closed)

Date: 2026-11-23  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Worklist status

**CLOSED — 239/239 original gaps resolved; zero unknown historical Claim versions remain.** The former 133-row queue is retained as a closed audit trail, not an open worklist.

| Control | Final result |
|---|---:|
| Phase 2 historical score rows | 1,501 |
| Phase 2 unique normalized Claim IDs | 1,494 |
| Original unresolved rows | 239 |
| Batch 41 recoveries | 94 |
| Batch 17 / 21 recoveries | 12 |
| Batches 18–40 recoveries | 133 |
| **Total resolved** | **239/239** |
| **Remaining unresolved** | **0** |
| Exact historical/current path + Blob matches | 238 |
| Explicitly versioned current successor | 1 |
| Current accepted D/E/B assessments | 0/1,494 |

## Closure conditions

1. Every original worklist row now has a historical Claim version supported by an exact report-parent snapshot and row-level crosswalk.
2. The 238 exact historical/current Blob matches remain byte-for-byte matches.
3. The sole former same-version content-drift case, Generator CO Emergency, is now a versioned lineage: historical Claim@1 is preserved; current Claim@2, CDC EU@2, CPSC EU@1 and cross-slice Relation@2 are linked and covered by targeted regression.
4. Historical score reuse remains NOT_AUTHORIZED for all 239 rows.
5. No current D/E/B value was populated by this recovery.

The companion CSV retains all 133 former queue rows with a closure disposition and points to the complete 239-row master crosswalk. It is no longer an execution queue.

## Separate work remains

This closure does not resolve historical Evidence Use/Source versions, source passage fit, locators, source independence, the repeated-score adjudication boundaries, specialist review, Human View, adversarial review, rights or publication eligibility. The seven repeated score groups remain governed by their separate reconciliation report.

No additional historical Claim-version recovery batch is required. main remains untouched; PR #21 remains Draft and unmerged.
