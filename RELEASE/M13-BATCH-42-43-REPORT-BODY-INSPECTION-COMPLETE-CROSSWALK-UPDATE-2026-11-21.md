# M13 — Batch 42–43 report-body inspection complete: crosswalk update

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Prior crosswalk: `M13-CURRENT-ASSESSMENT-CROSSWALK-RECONCILIATION-2026-11-18.md` (source inspection HEAD `5a8f01f6ac62cf0c53dd1996c96224577717d400`)  
Current inspection checkpoint before this update: Batch 43 row-body inspection commit `ec16a1baf0afac42c487d7dff674b6cd53df2a6b`.

## 1. Report-body inspection count — complete

The prior crosswalk recorded 20 individually inspected Batch 42–43 reports and 180 reports not yet individually inspected.

The full report-body sweep is now complete:
- Batch 42 rows 001–100: 100/100 report bodies inspected.
- Batch 43 rows 001–100: 100/100 report bodies inspected.
- Combined: **200/200 report bodies inspected; 0 report bodies remain uninspected.**

The 20 previously inspected reports remain counted once. The 180 formerly uninspected report files are now inspected: Batch 42 rows 021–100 (80 files) and Batch 43 rows 001–100 (100 files).

Supporting artifacts:
- Batch 42 rows 021–068: six supplementary spot-check packages covering 48 report bodies.
- Batch 42 rows 069–100: `M13-BATCH-42-SUPPLEMENTARY-REPORT-BODY-SPOT-CHECK-ROWS-069-100-2026-11-21.md`.
- Batch 43 rows 001–100: `M13-BATCH-43-SUPPLEMENTARY-REPORT-BODY-SPOT-CHECK-ROWS-001-100-2026-11-21.md`.

## 2. Historical version-header recovery

All 200 report bodies have now been individually read. Each report contains explicit historical Claim/Evidence Use/Source version information, although some reports list multiple Evidence Use versions or more than one linked Source, and the version-header syntax is not uniform.

This establishes report-level historical version-header recovery for the 200 report occurrences. It does **not** automatically establish:
- 200 unique normalized Claim IDs;
- one-to-one Claim/EU/Source chains where multiple EU/source versions are listed;
- exact current canonical ID/version equality;
- passage-level verification from the current canonical Evidence Use;
- accepted current D/E/B scores.

The master crosswalk must rerun normalized-ID deduplication and preserve all multi-EU/multi-Source cases. Do not rewrite stored IDs or paths based on normalized comparison.

## 3. Current canonical graph comparison — separate count

Current canonical graph reconciliation has been completed and documented for Batch 42 rows 069–100 only:
- 32/32 current Claim/EU/Source ID+version chains matched the historical report headers;
- all cross-links and Claim provenance references matched;
- no current EU passage locator was accepted in that reconciliation;
- all 32 remain HOLD.

The remaining report rows requiring current canonical graph comparison are:
- Batch 42 rows 001–068: 68 report rows.
- Batch 43 rows 001–100: 100 report rows.
- Total: **168 report rows**.

These are report-row occurrences, not yet deduplicated unique Claim IDs. Some reports contain multiple Evidence Use versions or Source references; preserve them separately.

## 4. Updated crosswalk figures and guardrails

| Measure | Prior 2026-11-18 crosswalk | Current after this sweep |
|---|---:|---:|
| Batch 42–43 report files | 200 | 200 |
| Individually inspected report bodies | 20 | **200** |
| Not-yet-inspected report bodies | 180 | **0** |
| Current canonical graph chains compared in this sweep | not complete | 32 |
| Report rows still requiring current graph comparison | not enumerated here | **168** |
| Current accepted D/E/B assessments | 0 | **0** |

The prior crosswalk's recovery-state counts (20 inspected / 180 uninspected) are superseded for report-body inspection progress. Do not change its separate counts for 594 unique Claims, 239 other per-ID version gaps, 142 Batch53–54 Claims, generic-EU cohort, residual ledger or duplicate groups until the master normalized-ID and version-chain join is rerun against the actual source artifacts.

## 5. Important Batch 43 findings

The 100 historical report scores distribute as follows:
- D: D1=5, D2=29, D3=66.
- E: E1=26, E2=67, E3=7.
- B: B1=6, B2=61, B3=33.

The strongest direct-match historical E3 cases include NIST manufacturing operations (row 034), ICMJE authorship/accountability (058), CDC POLARIS systems characteristics/feedback (065–066), DOE electric-motor definition (090), USGS hydrology Claim@2 (098), and DOE hydropower (099). E3 does not mean the canonical Evidence Use already stores a pinpoint or that the claim is release-cleared.

Material source-fit/chain issues include:
- inaccessible or mismatched source URI: rows 006, 008, 012, 081, 082;
- a related but unlinked source being more direct than the canonical source: rows 015, 023, 025, 028, 037, 040, 056, 076;
- broad topic pages or source identity too broad for the full proposition: rows 010, 018, 033, 036, 057, 069–071, 077–079, 083, 087–089, 096–097, 100;
- editorial slice-name artifacts in Claim wording: rows 007 and 045–047.

Full row-level findings and historical scores are preserved in the Batch 43 supplementary report.

## 6. Current worksheet and canonical no-change boundary

This update does not accept or transfer any historical score. The current worksheet's D/E/B fields remain blank and `human_review_status=NOT_YET_REVIEWED` unless changed by a separately authorized, evidence-backed assessment workflow.

No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record was changed. No queue exclusions, risk-domain classifications or priority changes were made. No rights/editorial clearance, formal risk assessment, specialist review, independent review or Human View approval is inferred. PR #21 must remain Draft/Open/unmerged; `main` is untouched.

## 7. Next ordered work

1. Rerun the master crosswalk/ledger join for all 200 reports, normalize Claim IDs for comparison only, deduplicate, and explicitly adjudicate repeated groups and multi-EU/multi-Source headers.
2. Complete current canonical Claim/EU/Source graph reconciliation for the 168 outstanding report rows, starting with high-consequence and multi-version chains.
3. Compare current Evidence Use content and source passages, not merely record IDs and versions; record missing, generic, partial, mismatched or inaccessible locators.
4. Only after the full join, update the 594-unique-Claim historical version recovery accounting and the generic-EU 496/356 residual reconciliation.
5. Keep D/E/B acceptance, risk assessment, specialist/independent review, Human View, rights/editorial and release gates separate.
