# M13 — Current Assessment Crosswalk Reconciliation

Date: 2026-11-18  
Source inspection HEAD: `5a8f01f6ac62cf0c53dd1996c96224577717d400`  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
PR #21: Draft / Open / unmerged

## 1. Reproduced corpus join

Source artifacts:
- Claim Audit Worksheet: artifact `14438475109`, source revision `7123b44ce344190027c20e33c0d83675d5aa0768`.
- Scored Claim Row Ledger: artifact `14437300274`, source revision `a4f3f61c8338a28b76b6594f2215439eebe805cc`.

The worksheet contains 1,494 Claims. The historical ledger contains 1,501 rows and 1,494 unique normalized Claim IDs. All 1,501 rows join to the current inventory by canonical path; there are zero unmatched rows. Seven repeated groups / 14 rows are retained separately. This is an accounting join, not score acceptance.

Comparison of both artifact source revisions to source inspection HEAD `5a8f01f6` found only RELEASE Markdown changes; no canonical CONTENT JSON changed.

## 2. Current crosswalk classification

| Classification | Claims |
|---|---:|
| REUSABLE PRIOR ASSESSMENT CANDIDATE | 889 |
| PARTIAL REVALIDATION REQUIRED | 596 |
| HISTORICAL ROW ONLY | 9 |
| **Total** | **1,494** |

The original 888 exact-ID/exact-version candidates remain. One additional case, `CLM-HYDROLOGY_BASICS-C@2`, is promoted after direct inspection of Batch 43 row 098: the report explicitly states Claim@2 / EU@2 / Source@2, matching the current canonical chain and preserving a claim-specific USGS passage and D/E/B rationale. It remains HOLD for separate rights and independent review.

The nine historical-only rows assess Claim@1 while the current Claim is @2; no historical score is transferred:
- ENERGY A/B/C
- HUMAN_COMPUTER_INTERACTION A/B/C
- HYDROLOGY A/B
- MOTION B

Three path/internal-ID cases remain partial pending an explicit mapping:
- `CLM_POWER_ELECTRONICS_BASICS_B@1`
- `CLM_PATHOLOGY_BASICS_C@1`
- `CLM_PUBLIC_HEALTH_SURVEILLANCE_BASICS_C@1`

## 3. Version recovery from versionless ledger rows

The 601 versionless row occurrences map to 594 unique Claims. Their current evidence state is:

| Recovery state | Claims |
|---|---:|
| Batch 42–43: individually inspected sample; report explicitly states Claim/EU/Source versions | 20 |
| Batch 42–43: reports not yet individually inspected | 180 |
| Batch 41: exact Claim@1 / EU@1 / Source@1 recovered from Git snapshots | 6 |
| Seven repeated-score groups: Claim@1 / EU@1 / Source@1 provenance established | 7 |
| Batch 53–54: Claim@1 confirmed at exact historical snapshots; EU/Source versions pending | 142 |
| Other Claims with no per-ID historical version yet recovered | 239 |
| **Total** | **594** |

Batch 42–43 report inspection: 20 of 200 individual report files were sampled and fetched, not a complete sweep. All 20 sampled reports explicitly state Claim/EU/Source versions; four sampled files use plural or unformatted version-header syntax. The remaining 180 reports have not yet been individually inspected. Current EU/Source version comparison remains open for the sampled records; historical E scores are not automatically transferred.

Batch 41 six-record recovery:
- Asset Management A/B/C: snapshot `cd1a9e2cf2640b1a1da39af0d2710da547ef302d`, Block 04 rows 56–58.
- Behavioral Biology A/B/C: snapshot `14078b3994edec546f88e6d0f1181c7586611bc9`, Block 05 rows 74–76.
All six historical chains are Claim@1 / EU@1 / Source@1. Claim wording is unchanged in current Claim@2; D/B are candidates only, while current EU@3 / Source@2 require E revalidation.

Batch 53 snapshot: `33ef97e7ba6a9e91aebaee198cfead532faa4185` — 100/100 Claims record_version 1.  
Batch 54 snapshot: `bf2fd96579446c7c26fdbb5dcfabd15098d242f4` — 42/42 Claims record_version 1.  
For these 142 records, historical EU/Source versions are not yet recovered.

The seven repeated groups retain their existing adjudications. Do not repeat them: five previously resolved score dimensions remain closed; Water A/C historical E remains unresolved; Emergency-water D retains both identical score rows and rationales.

A separate earlier checkpoint reports 105 unique Claim@1 records and linked Sources@1 on snapshot `1b8bd3f5889e731b782c9d1e4dededf1ea7984be`, with Evidence Use@1 verified for Batches 12–18, 21 and 27. Its row-level list of 105 Claim/EU/Source IDs was not recovered. Do not infer membership or repeat completed source checks; recover the primary row-level manifest and reconcile it before changing the 239 count. That checkpoint also names 13 unresolved Claims only by batch/topic/count (Batch 21: 11; Batch 24: 1; Batch 30: 1), without exact IDs.

## 4. Prior D/B candidates and separate gates

Historical D/B candidate or carry-forward inputs: 1,063 (888 exact-version rows + 20 individually inspected Batch 42–43 report-header cases + 6 Batch 41 cases + 142 Batch 53–54 Claim@1 cases + 7 existing repeated-group dispositions). These are candidates, not accepted current assessments. The 180 uninspected Batch 42–43 reports are excluded until verified.

The current worksheet has blank D/E/B fields and `NOT_YET_REVIEWED` for all 1,494 Claims. Current accepted D/E/B assessments: **0**.

The generic-EU cohort remains 496 exact Claim/EU mappings, with 356 residual remediation rows. The prior residual-356 check covered 14 rows only; 342 still require fresh canonical cross-check. Filename mentions do not establish substantive review.

## 5. Technical state and change boundary

On source inspection HEAD `5a8f01f6ac62cf0c53dd1996c96224577717d400`, core CI is 3/3 PASS:
- Reference implementation tests: run `44349246488`
- Release Conformance Gate: run `44349242911`
- Offline Edition: run `44349243053`

This reconciliation changes no canonical Claim, Evidence Use, Source, Assessment, Relation or risk record. It starts no Batch 55, launches no agents, and does not change `main`. PR #21 remains Draft / unmerged.

## 6. Next ordered work

1. Recover the 105-Claim prior-snapshot row-level manifest; do not repeat source reviews.
2. Recover historical EU/Source versions for the 142 Batch 53–54 Claims.
3. Compare current EU/Source versions for the 200 Batch 42–43 report-header cases and the 888 exact-version candidates.
4. Resolve the remaining 239 per-ID version gaps, including the remaining 94 Batch 41 records and 145 earlier records.
5. Reconcile the 496 generic-EU cohort and 356 residual ledger, then continue high-consequence, Relations, Human View, rights, specialist and independent-review gates separately.

The companion 1,494-row CSV is retained as a working export for this inspection. It preserves current Claim IDs/versions, paths, linked EU/Source IDs, historical report paths/lines, score rows and rationales, recovery state, and the prohibition on treating historical scores as current accepted D/E/B.
