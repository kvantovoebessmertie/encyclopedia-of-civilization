# M13 Phase 3 — Batch 18–40 historical Claim-version recovery addendum

Date: 2026-11-22  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Comparison HEAD: `fde5b351cf2310d7152c5873e25624420c98f56b`

## Result

**All 133 remaining historical Claim-version labels are now identified from exact report-parent Git snapshots. 132/133 also have exact historical/current path and Blob SHA equality. One Claim has a same-version content-drift exception and remains an integrity HOLD.**

| Measure | Result |
|---|---:|
| Phase 2 historical score-row occurrences | 1,501 |
| Unique normalized Claim IDs | 1,494 |
| Phase 2 historical Claim-version gaps before this addendum | 133 |
| Rows inspected in this addendum | 133 |
| Unique Claims inspected | 133 |
| Historical Claim version identified | 133/133 |
| Exact historical/current path + Blob SHA matches | **132/133** |
| Same-version content-drift exceptions | **1** |
| Historical Claim versions still unknown | **0** |
| Current accepted D/E/B assessments | **0/1,494** |

Combined with the earlier Phase 3 packages (Batch 41: 94; Batches 17 and 21: 12), the full original 239-row historical Claim-version gap now has no unknown version labels. Across those 239 rows, 238 have exact current/historical Claim path and Blob SHA equality; one has a documented same-version content-drift exception.

This is a Claim-version provenance result only. It does not accept or transfer historical D/E/B scores, recover all historical Evidence Use/Source versions, validate source passages, or confer publication eligibility.

## Method

For every remaining report cohort (B18–B20, B22–B26, B28–B40):

1. Retrieved the exact commit that introduced the original scored report.
2. Used that report commit's first parent as the pre-report historical snapshot.
3. Retrieved the complete recursive Git tree for that exact parent snapshot; every tree response was non-truncated.
4. Located the Claim file by its repository path, preserving canonical internal IDs and filenames. Deterministic filename-alias handling covered the existing `CLM-` / `CLM_` prefix and terminal A/B/C filename variants; no stored identifier or path was rewritten.
5. Compared the historical Blob SHA with the same path at comparison HEAD `fde5b351cf2310d7152c5873e25624420c98f56b`.
6. Cross-checked the 133 IDs against the Phase 1 Claim inventory. None belongs to the inventory's 16 version-2 Claims; the 133 historical Claim records are therefore version 1. The exception record was additionally fetched as JSON at both refs and directly confirmed as `record_version: "1"` in both snapshots.

The four CSV companions preserve one row per Claim, including report code/line, historical D/E/B, report commit, snapshot-parent commit, historical/current path, both Blob SHAs, version, reconciliation status, and the prohibition on score reuse.

## Row-level crosswalks

- `M13-PHASE-3-BATCH-18-24-HISTORICAL-CLAIM-SNAPSHOT-CROSSWALK-2026-11-22.csv` — 40 rows; 39 exact matches and one content-drift exception.
- `M13-PHASE-3-BATCH-25-30-HISTORICAL-CLAIM-SNAPSHOT-CROSSWALK-2026-11-22.csv` — 24/24 exact matches.
- `M13-PHASE-3-BATCH-31-34-HISTORICAL-CLAIM-SNAPSHOT-CROSSWALK-2026-11-22.csv` — 12/12 exact matches.
- `M13-PHASE-3-BATCH-35-40-HISTORICAL-CLAIM-SNAPSHOT-CROSSWALK-2026-11-22.csv` — 57/57 exact matches.

All 133 rows retain `HISTORICAL_ONLY_NOT_ACCEPTED`; score reuse is `NOT_AUTHORIZED`. The original Phase 2 ledger and its historical report rows remain unchanged.

## Exception — generator CO emergency Claim

Claim: `CLM-GENERATOR-CO-ALARM-EMERGENCY`  
Report: Batch 19, line 13, row 1  
Historical D/E/B: 2/3/3  
Historical snapshot parent: `18d9c1ba150c5b9d4e6d8f4a5b2923cf47ac13d5`  
Report commit: `8e8ac8e7aa6a8a278712d0300b92e23289c60bed`

| Field | Historical snapshot | Comparison HEAD |
|---|---|---|
| Claim version | 1 | 1 |
| Path | Same | Same |
| Blob SHA | `29c7f166b28510e323f0b391f2bcc37506839ce2` | `743a7c0ee1003b7b22b80a01f3372b728587820b` |

The exact content-changing commit is `a58294e3af144077d37075d0e73da9f73438101b`, titled “Narrow generator CO emergency claim to CDC-supported advice” (2026-10-10 19:00:18Z). Its diff removes the sentence:

> в помещение нельзя возвращаться до проверки безопасности.

The commit leaves `record_version` at `"1"`. Thus the historical Claim@1 is known, and the current Claim is also labelled @1, but the contents differ under the same version. This is not an exact path/blob match and must not be silently treated as an ordinary resolved row.

Disposition:
- preserve both historical and current Blob SHAs;
- retain the row as `SAME_VERSION_CONTENT_DRIFT` / integrity HOLD;
- do not rewrite the historical score or accept it as a current assessment;
- do not edit the canonical Claim in this package;
- require a separate bounded versioning/provenance review before any correction or version increment.

Because the Claim concerns CO emergency response, the removed return-to-building boundary also requires high-consequence and source-fit review. This finding does not itself determine the correct current wording.

## Accounting and non-transfer boundary

- The original 239 unresolved rows now have 239 historical Claim-version labels identified.
- 238/239 have exact historical/current Claim Blob equality.
- One remains a same-version content-drift exception.
- Historical D/E/B remains historical-only; current accepted D/E/B remains 0/1,494.
- Historical Evidence Use/Source version provenance remains a separate task, including the 141/142 Batch 53–54 EU/Source gaps already recorded in Phase 2.
- Seven repeated-assessment groups remain preserved and separately governed; this package does not adjudicate them.
- Source passage fit, locator reproducibility, independence, high-consequence specialist review, Human View/adversarial review, rights, and release decisions remain open.

No canonical Claim, Evidence Use, Source, Assessment, Relation, risk record, or `main`-branch file was modified. This addendum and its CSV companions are noncanonical audit evidence. PR #21 remains Draft and unmerged. M13 remains OPEN / NOT CLEAN.


---

## Follow-up disposition after the authorized Generator CO version-lineage correction — 2026-11-23

The earlier comparison at `fde5b351cf2310d7152c5873e25624420c98f56b` correctly identified a same-version content-drift exception for Generator CO Emergency at that historical comparison point. The subsequent, separately authorized correction has now resolved that defect without rewriting Claim@1.

Verified current lineage on the M13 branch:
- Historical Claim@1 Blob SHA remains `29c7f166b28510e323f0b391f2bcc37506839ce2`.
- Current Claim@2 Blob SHA is `973ab535fd2fc681e3f9731ec88bb3b87fd184d2`.
- CDC Evidence Use is @2 and limited to immediate fresh-air response / emergency medical assistance.
- Separate CPSC Evidence Use is @1 and limited to the no-re-entry-until-emergency-services-permit instruction.
- Cross-slice Relation is @2 and points to Claim@2.
- The targeted regression verifies the exact references, versions and non-overlapping CDC/CPSC evidence scopes.

The old same-version drift status is superseded by VERSIONED_SUCCESSOR_CURRENT_V2 in the final 239-row consolidated crosswalk. Historical D/E/B remains HISTORICAL_ONLY_NOT_ACCEPTED; score reuse remains NOT_AUTHORIZED. This closes version lineage only, not high-consequence Human View or public-pilot clearance.
