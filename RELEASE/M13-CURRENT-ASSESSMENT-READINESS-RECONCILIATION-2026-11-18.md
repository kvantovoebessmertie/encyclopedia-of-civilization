# M13 — current assessment readiness and evidence-work reconciliation

Date: 2026-11-18  
Inspection basis before this report: `b77b4ff1f637e6be1033731d39ec3fc2b2568451`  
Prior inventory artifact revision: `7123b44ce344190027c20e33c0d83675d5aa0768`  
Prior scored-ledger artifact revision: `a4f3f61c8338a28b76b6594f2215439eebe805cc`  
Disposition: **current assessment census not yet accepted; no new Batch authorized or created**.

## 1. Executive result

The exact current Claim inventory is 1,494 records (1,478 version 1; 16 version 2). The generated current Claim worksheet has blank D/E/B fields and `NOT_YET_REVIEWED` for all 1,494 rows.

Therefore:

- **Accepted current-version D/E/B assessments in the current worksheet: 0 / 1,494.**
- **Claims requiring a current-version assessment disposition: 1,494 / 1,494.**
- This does **not** mean 1,494 entirely new source searches are required. The repository contains substantial prior desk/source-passage work that can be reused after exact Claim/EU/Source version and report-body verification.
- The number of Claims whose prior D/B work can be reused without re-assessment, and the exact number of unique current Evidence Use records requiring canonical repair, are **not yet established**. Do not infer either from the historical row count or filename mentions.

The distinction is important: the current worksheet is empty because prior scores have not been validated and accepted into the current exact-version register. It does not erase the historical reviews.

## 2. Reconciled Claim and historical-score denominator

The Phase 1 inventory artifact records:

| Measure | Verified count |
|---|---:|
| Record JSON files scanned | 4,851 |
| Vertical slices | 483 |
| Slices containing Claims | 482 |
| Claim records | 1,494 |
| Claim version 1 | 1,478 |
| Claim version 2 | 16 |
| Duplicate internal Claim IDs in inventory | 0 |
| Claims with at least one Evidence Use | 1,494 / 1,494 |
| Claim-to-Evidence Use links | 1,679 |
| Unique Evidence Use IDs | 1,679 |
| Unique Source IDs | 627 |

The inventory artifact was generated at revision `7123b44`. GitHub comparison from that revision to inspection HEAD `b77b4ff` shows only two RELEASE Markdown files changed; no canonical content path changed. The inventory counts therefore remain applicable to the inspected Claim tree.

The scored-row ledger generated at `a4f3f61` reports:

- 1,501 historical scored-report rows;
- 1,494 unique normalized Claim IDs;
- 1,494/1,494 inventory Claims with at least one historical row match;
- seven repeated groups containing 14 row occurrences;
- zero unmatched scored rows;
- one separator-normalized match requiring manual confirmation.

GitHub comparison from `a4f3f61` to `b77b4ff` shows only RELEASE Markdown files changed; no canonical Claim/Evidence Use/Source JSON or scoring-ledger generator changed. The 1,501-row accounting result remains applicable to the inspected content tree. It remains an accounting match, not acceptance of the scores.

## 3. What prior assessment work can be reused

The 1,501 historical rows divide into the following report-origin strata:

| Historical report population | Rows | Current interpretation |
|---|---:|---|
| Batches 12 and 17–43 | 459 | Heterogeneous earlier assessments; require report-by-report provenance/depth classification |
| Batches 44–52 | 900 | Source-passage review/scoring reports |
| Batch 53 | 100 | Five source-passage review/scoring reports |
| Batch 54 | 42 | Two source-passage review/scoring reports |
| **Total** | **1,501** | |

The 1,042 rows from Batches 44–54 are source-passage review inputs, not automatically accepted current assessments. Their score distribution is:

| Population | Rows | E0 | E1 | E2 | E3 |
|---|---:|---:|---:|---:|---:|
| Batches 44–52 | 900 | 1 | 883 | 16 | 0 |
| Batch 53 | 100 | 0 | 100 | 0 | 0 |
| Batch 54 | 42 | 0 | 42 | 0 | 0 |
| **Batches 44–54** | **1,042** | **1** | **1,025** | **16** | **0** |

For Batches 53 and 54, all 142 reviewed Evidence Use records lack reproducible canonical claim-specific locators; the reports explicitly explain why E remained 1 even where the external passage supported the Claim. Batch 44–52 reports also frequently identify missing canonical pinpoints; their 16 E2 and one E0 cases require individual review rather than extrapolation.

The earlier 459 rows are not one homogeneous cohort. They include the seven repeated groups and differ in method, depth, source pinpoint quality and version provenance. They must be classified from their report bodies, not accepted as a block.

### Repeated historical assessments

The five disputed dimensions already adjudicated remain recorded in the separate comparison report:

- Nuclear A D1;
- Nuclear B B3;
- Nuclear C D2/B2;
- Water B D2.

Water A E2/E3 and Water C E2/E3 are now formally carried as `UNRESOLVED — HISTORICAL EVIDENCE NOT RECOVERABLE` by `RELEASE/M13-WATER-A-C-HISTORICAL-EVIDENCE-RECOVERY-DISPOSITION-2026-11-18.md`. Their original rows remain preserved and are excluded from current-version score calculation. The current Claim/EU/Source chains must be assessed independently.

## 4. Evidence-chain repair population — do not conflate cohorts

The latest repository routing checkpoint available for the generic-EU census reports:

| Population | Count |
|---|---:|
| Generic Evidence Use candidates | 496 |
| Exact Claim/EU mappings | 496 |
| Unmapped / ambiguous EU mappings | 0 / 0 |
| High-consequence candidates within the 496 | 120 |
| Previously reviewed priority second-pass Claims | 20 |
| Residual generic-EU remediation population | 356 |

Arithmetic: `496 - 120 - 20 = 356`.

These are **routing populations**, not 496 confirmed canonical defects or 496 unique Claims requiring identical corrections. The 496 artifact's report/filename mentions are retrieval leads, not semantic confirmation. The 120 high-consequence and 20 priority cohorts have prior desk/source-passage work; reuse it. The 356 residual is the remaining work queue, not a new scoring batch.

The separate 47-Claim strict passage/locator cohort was assigned to Packages 01–06 and desk-reviewed 47/47; all 47 remain HOLD. It overlaps the broader generic-EU work and must not be added as another disjoint population.

The 356-row integrity checkpoint reports a fresh per-file canonical cross-check of 14/356 rows; 342 were not freshly fetched in that pass. A previous 359-row master register reports 359/359 report-body coverage and reference validation at its own validation head, but it is an older cohort/revision. Do not silently transfer that result to the current 356 ledger without exact set/version reconciliation. The 356 companion CSV is not committed in the repository tree at the inspection point.

The 496/356 counts originate from the successful generic-EU/queue artifact at revision `8cf14e5`. GitHub comparison to `b77b4ff` shows no canonical CONTENT JSON changes, but it does show later changes to the reference audit scripts. Treat 496/356 as the last verified routing baseline, not a newly rerun exact-HEAD result. Re-run the current coverage generator at the approved HEAD before using it as a final exact count.

## 5. Current classification contract

Every one of the 1,494 exact keys must receive one of these non-exclusive evidence-history classifications before any current score is accepted:

1. **REUSABLE_PRIOR_ASSESSMENT_CANDIDATE** — exact Claim ID@version established; report body gives claim-specific D/B rationale and source-passage scope; current Claim wording and evidence chain have not materially changed. Reuse still requires reviewer confirmation.
2. **PARTIAL_REVALIDATION_REQUIRED** — useful prior D/B or source-passage work exists, but one or more dimensions, exact versions, locators, source lineage, independence or rationale are incomplete.
3. **HISTORICAL_ROW_ONLY** — a score or Claim-ID match exists, but the report body/provenance is insufficient to establish a substantive assessment of the exact current version.
4. **NO_USABLE_PRIOR_ASSESSMENT** — no applicable substantive review is established for the exact Claim version.

These classifications must be separate from current D/E/B values, high-consequence status, Human View, Relations, rights, specialist review and publication status. An assessment can be reusable as a D/B input while its E remains blocked by the canonical locator rule. A historical row never clears a release gate.

For current E scoring, retain the strict project locator rule: no reproducible claim-specific locator in the canonical Evidence Use means E cannot be raised above 1 until the locator and supporting passage are corrected and verified. Do not rewrite historical E2/E3 values to fit the current rule.

## 6. Next execution — no Batch 55

The next operation is a deterministic, noncanonical **1,494-row current-assessment crosswalk**, not another batch:

1. Join every inventory row by exact `Claim ID@version` to all historical report rows and source reports.
2. Import report path, line/table row, source revision/artifact, review date, reviewer if documented, Claim version evidence, D/E/B rationale, passage/locator, current EU/Source refs and limitations.
3. Reconcile the seven repeated groups, the 14 unidentified-ID exception and prior REJECT provenance without inventing missing identities or reviewers.
4. Assign the four history classifications above; count reusable, partial, historical-only and no-usable-prior populations.
5. Separately deduplicate current canonical Evidence Use repair needs by exact EU ID@version. Import prior passage/rights/identity findings; do not repeat source searches already completed.
6. Publish the exact current-HEAD counts and unresolved exceptions before any new scoring batch is considered.

No Batch 55 is created or authorized by this checkpoint. No canonical Claim, Evidence Use, Source, Assessment or Relation record is changed. PR #21 remains Draft/unmerged; `main` remains untouched.

## 7. CI and revision limitation

This report is based on the read-only comparison and artifacts listed above. The recovery-disposition commit and this readiness report are documentation commits. No exact-head workflow result is claimed for either documentation commit. The current branch must be checked again and all required workflows tied to one identical final SHA before any technical acceptance statement.

M13 remains OPEN / NOT RELEASE-READY.
