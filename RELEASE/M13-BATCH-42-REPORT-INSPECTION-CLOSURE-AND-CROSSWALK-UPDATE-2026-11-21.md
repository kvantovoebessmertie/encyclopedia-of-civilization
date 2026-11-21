# M13 — Batch 42 report inspection closure and crosswalk progress update

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reference revision before this addendum: `7c3f8f5fc399a5791ebd02329f966caea31676d5`

## 1. Purpose

This addendum updates the report-inspection portion of `M13-CURRENT-ASSESSMENT-CROSSWALK-RECONCILIATION-2026-11-18.md`. It does not replace that historical snapshot or rewrite its artifact counts. It records new individually inspected Batch 42 report bodies and separates historical version recovery from current canonical graph verification.

## 2. Batch 42 report-body inspection is complete

Batch 42 contains 100 scored-row reports, rows 001–100.

- Rows 001–020 were already individually inspected in the prior crosswalk sample.
- Rows 021–068 were subsequently individually inspected in six supplementary packages (48 reports total).
- Rows 069–100 were individually inspected in the 32-row supplementary package completed at this checkpoint.

**Result: 100/100 Batch 42 report bodies individually inspected.** This is report-body inspection, not acceptance of historical scores and not release clearance.

The 80 report bodies from rows 021–100 each expose the historical Claim/Evidence Use/Source version chain in the report header. These are 80 report-row occurrences; the number of unique normalized Claim IDs must be computed from the canonical crosswalk before changing unique-Claim recovery counts. No duplicate group is resolved by this inspection.

## 3. Combined Batch 42–43 report-inspection position

The 2026-11-18 crosswalk described 200 Batch 42–43 report files, of which 20 had been individually inspected and 180 remained uninspected.

After the work documented here:
- Individually inspected report files: **100/200** (20 prior sample + 80 additional Batch 42 rows).
- Not-yet-individually-inspected report files: **100/200**.
- Batch 42: **100/100 inspected**.
- Batch 43: **0/100 individually inspected in this report-body sweep**.

The remaining 100 are Batch 43 rows 001–100. The prior crosswalk's “180 uninspected” figure is therefore superseded for current progress accounting by 100, subject to the same row-occurrence vs unique-Claim distinction.

## 4. Current canonical graph comparison completed in this checkpoint

For Batch 42 rows 069–100, all 32 historical Claim/Evidence Use/Source chains were compared to the current canonical graph at the inspected branch tree.

Result:
- 32/32 current Claim IDs and versions match the historical report headers.
- 32/32 current Evidence Use IDs and versions match the historical report headers.
- 32/32 current Source IDs and versions match the historical report headers.
- All current Claim provenance Source references and current Evidence Use Claim/Source references agree at version 1.
- No missing record or ID/version/link mismatch was observed in these 32 chains.

This is an exact ID/version graph match only. It does not establish passage-level evidence. The 32 current EU records have no accepted reproducible passage locator in this comparison; all 32 remain HOLD and current accepted D/E/B remains zero. The other 68 Batch 42 report chains (rows 001–068) have not been fully compared against current canonical graph by this addendum.

## 5. Updated accounting instructions

For the master crosswalk:
1. Replace the old Batch42–43 report-body count of 20 inspected / 180 uninspected with 100 inspected / 100 uninspected.
2. Retain separate counts for report occurrences and unique normalized Claim IDs. Do not subtract 80 from unique-Claim totals until exact normalized-ID deduplication is performed.
3. Preserve historical report versions from rows 021–100 as historical version-header recovery, not current version verification.
4. Mark rows 069–100 as current canonical ID/version graph verified, but not source-passage reviewed or current-score accepted.
5. Do not modify the current worksheet's D/E/B blanks or `NOT_YET_REVIEWED` statuses.
6. Continue with Batch 43 rows 001–100 report-body inspection, then reconcile current canonical Claim/EU/Source chains in controlled batches.

## 6. No-change declaration

No canonical Claim, Evidence Use, Source, Assessment, Relation, risk record, queue state, or worksheet status was changed. No historical D/E/B score was transferred. PR #21 remains Draft / Open / unmerged; `main` remains untouched.
