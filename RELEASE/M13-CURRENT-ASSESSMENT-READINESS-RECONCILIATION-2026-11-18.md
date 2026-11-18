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


## 8. Exact-version crosswalk of the 1,501 historical score rows

The scored-row CSV and Claim worksheet ZIPs from Reference workflow run `44324850558` were downloaded and parsed directly. Both artifacts identify source revision `a4f3f61c8338a28b76b6594f2215439eebe805cc`. The GitHub comparison from that revision to inspection HEAD `b77b4ff` shows no canonical CONTENT JSON or score-ledger generator changes. The worksheet contains 1,494 current Claim rows; all 1,494 have blank D/E/B and `NOT_YET_REVIEWED`.

A row-level join by the ledger's exact canonical inventory path maps all 1,501 score rows to one current Claim file. This path join is for reconciliation only; it does not silently rewrite internal IDs or make a versionless row version-exact.

### 8.1 Explicitly versioned Batch 44–52 rows

Of the 900 Batch 44–52 rows:

- 888 match the current canonical `record_id@record_version` directly.
- 3 have separator/path identity differences and must retain an explicit path-to-internal-ID crosswalk before being treated as canonical exact-ID matches. One is the ledger's separator-normalized manual-confirmation case: `CLM-POWER_ELECTRONICS_BASICS_B@1`; two report IDs match the filename stem while the canonical internal IDs use separator variants.
- 9 explicitly identify Claim `@1`, while the current canonical Claim is `@2`. These are historical version-1 assessments, not current version-2 assessments:
  - `CLM-ENERGY_BASICS-A@1`
  - `CLM-ENERGY_BASICS-B@1`
  - `CLM-ENERGY_BASICS-C@1`
  - `CLM-MOTION_BASICS-B@1`
  - `CLM-HYDROLOGY_BASICS-A@1`
  - `CLM-HYDROLOGY_BASICS-B@1`
  - `CLM-HUMAN_COMPUTER_INTERACTION_BASICS-A@1`
  - `CLM-HUMAN_COMPUTER_INTERACTION_BASICS-B@1`
  - `CLM-HUMAN_COMPUTER_INTERACTION_BASICS-C@1`

The 888 direct matches are exact versioned prior-assessment candidates, not accepted current scores. Their report rationales and source chains still require review against the current canonical EU/Source versions and the current locator rule.

### 8.2 Versionless rows and the 16 current version-2 Claims

The remaining historical rows do not include `@version` in their score-table Claim key:

- Batches 53–54: 142 rows, all mapping to current version-1 Claim files.
- Batches 12–43: 459 rows, including the seven repeated groups. The seven repeated groups account for seven extra row occurrences, leaving 452 unique Claim IDs in this stratum.
- Across the 1,494 unique current Claims, the versionless stratum therefore contains 594 unique Claims: 587 current version-1 Claims and seven current version-2 Claims.

The 16 current version-2 Claims reconcile as follows:

| Current Claim@2 | Historical score-row provenance | Version conclusion |
|---|---|---|
| Asset Management A/B/C | Batch 41, rows without `@version` | Exact historical version not stated in the score rows; snapshot proof still required |
| Behavioral Biology A/B/C | Batch 41, rows without `@version` | Exact historical version not stated in the score rows; snapshot proof still required |
| Energy A/B/C | Batch 44 explicitly records `@1` | Historical v1; not applicable as a v2 assessment |
| Human–Computer Interaction A/B/C | Batch 52 explicitly records `@1` | Historical v1; not applicable as a v2 assessment |
| Hydrology A/B | Batches 52 and 45 explicitly record `@1` | Historical v1; not applicable as a v2 assessment |
| Motion B | Batch 44 explicitly records `@1` | Historical v1; not applicable as a v2 assessment |
| Hydrology C | Batch 43 score ledger row is versionless, but the dedicated Batch 43 row-098 report explicitly identifies Claim@2, EU@2 and Source@2 and supplies a section/paragraph locator | Exact v2 provenance is documented in the dedicated report; candidate for reuse after current-chain verification |

Thus, among the 16 current v2 Claims, nine have explicit v1-only historical score rows, six have versionless Batch 41 rows requiring snapshot reconstruction, and one has a dedicated exact-v2 report. Do not count the six versionless Batch 41 rows as v2 assessments until the exact historical Claim/EU/Source snapshot is recovered.

### 8.3 Revised reuse counts and immediate priorities

The current exact-version crosswalk supports the following bounded counts:

| Classification at this pass | Unique Claims / rows | Meaning |
|---|---:|---|
| Direct exact-ID and exact-version row matches in Batches 44–52 | 888 | Strong prior-assessment candidates; still not accepted current scores |
| Exact-version rows with separator/path crosswalk issue | 3 | Preserve IDs; resolve crosswalk before acceptance |
| Versionless unique Claims requiring historical snapshot confirmation | 594 | Includes 587 current v1 and 7 current v2 |
| Of those versionless current v2 Claims | 6 | Batch 41 Asset Management / Behavioral Biology; unresolved exact historical version |
| Explicit old-version rows | 9 | Current v2 Claims have only historical v1 score rows |
| Dedicated exact-v2 report outside the versionless ledger row | 1 | Hydrology C; candidate for reuse after EU/Source verification |

The 594 versionless unique Claims include the one Hydrology C case whose separate detailed report explicitly proves Claim@2/EU@2/Source@2; the score ledger row itself remains versionless. The table is a provenance crosswalk, not a new score register.

**Operational consequence:** 9 + 6 = 15 of the 16 current v2 Claims do not yet have a verified current-version assessment. The remaining Hydrology C case is only a reusable candidate, not accepted into the current worksheet. The 888 exact versioned rows also remain provisional until their evidence-chain and reviewer gates are checked.

This materially narrows the next work: first recover the six Batch 41 snapshot versions and resolve the three path/ID crosswalk cases; separately mark the nine v1 rows as historical-only for the current v2 Claims. Do not repeat source searches solely to resolve version provenance.
