# M13 — Water A/C historical evidence recovery and disposition

Date: 2026-11-18  
Inspection HEAD: `b77b4ff1f637e6be1033731d39ec3fc2b2568451`  
PR: #21, Draft / unmerged  
Scope: the two remaining historical E-score conflicts for `CLM-WATER_TREATMENT_BASICS-A@1` and `CLM-WATER_TREATMENT_BASICS-C@1`.

**Disposition: `UNRESOLVED — HISTORICAL EVIDENCE NOT RECOVERABLE`.**  
This closes the bounded recovery attempt by recording the limits of the surviving evidence. It does not choose E2 or E3, change a historical row, or assign a current score.

## 1. Decisions already adjudicated — not repeated

The independent AI rubric adjudication in §8 of `RELEASE/M13-REPEATED-ASSESSMENT-COMPARISON-2026-11-18.md` remains authoritative for the five disputed dimensions already resolved:

- Nuclear A — D1.
- Nuclear B — B3.
- Nuclear C — D2 / B2.
- Water B — D2.

These are separate successor decisions for historical reconciliation only. They do not overwrite either source row and do not populate the current Claim worksheet. This report does not reopen them.

## 2. Historical rows preserved

The two remaining conflicts are:

| Exact Claim key | Batch 21 historical E | Batch 27 historical E | Status |
|---|---:|---:|---|
| `CLM-WATER_TREATMENT_BASICS-A@1` | E2 | E3 | UNRESOLVED |
| `CLM-WATER_TREATMENT_BASICS-C@1` | E2 | E3 | UNRESOLVED |

All 14 historical rows across the seven repeat groups remain preserved. No row is deleted, rewritten, or selected by date, score magnitude, or rationale length.

## 3. Final bounded recovery attempt

The following primary repository materials were inspected at the stated inspection HEAD:

1. `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md` — the original Batch 21 scored rows and rationales.
2. `RELEASE/M13-CLAIM-REVIEW-BATCH-27-WATER-TREATMENT-2026-10-10.md` — the original Batch 27 scored rows and rationales.
3. `reports/agent-work/m13-auditor/M13-SIX-CONFLICTS-HISTORICAL-EVIDENCE-EXTRACTION-2026-11-18.md` — historical worksheet artifacts, Git snapshots, source versions, report commits, and exact known gaps.
4. `RELEASE/M13-REPEATED-ASSESSMENT-COMPARISON-2026-11-18.md` — the row-level comparison and subsequent version-provenance reconstruction.

The extraction report establishes that the relevant Claim, WHO Evidence Use, EPA Evidence Use and Source records were version 1 in the inspected historical Git snapshots. It also records that the worksheets do not preserve the EU/Source record versions, the two scored reports do not give reproducible WHO/EPA passage locators, and the reviewer identities / actual pages read are not documented. The four repository snapshots establish the bytes present in those trees; they do not establish which external page revision a reviewer opened or read.

### 3.1 WHO

The historical canonical WHO Source points to the broad WHO Water, Sanitation and Health programme page:

`https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health`

The corresponding Evidence Use descriptions state that WHO provides public-health/water-quality context (A) and domain-level support for water-quality/use dependence (C). Neither identifies a reproducible section, paragraph, table, figure, or page from the historical review.

The original Batch 21 and Batch 27 reports do not preserve an exact WHO passage or historical page capture. The historical extraction report likewise identifies no such passage. A final attempt to locate an October 2026 archived copy through Wayback CDX / availability access did not yield a retrievable capture in the available research interface. This is an access/recovery limitation, not proof that no archive capture exists.

WHO's *Guidelines for drinking-water quality*, fourth edition incorporating the first, second and third addenda, was published on 17 June 2026. Its current materials contain much more specific treatment guidance, including catchment/source-water characteristics, contaminant hazards, treatment processes and performance conditions. Those are valid candidates for a **new current-version review**, but the canonical historical WHO Source is the broad programme page. The 2026 Guidelines cannot be retroactively attributed to the October reviewers without primary evidence that they used them.

### 3.2 EPA

The linked EPA Source is the official *Overview of Drinking Water Treatment Technologies*:

`https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies`

Its current content directly describes contaminant-specific technologies, performance/capacity, influent-water characteristics and operating limitations. This is strong direct support for the substance relevant to A and C. However, the historical reports do not preserve the exact EPA passages, the page revision actually consulted, or a reproducible locator. The present page cannot prove the exact historical page state or reviewer use.

### 3.3 Independence and E2/E3

The repository graph confirms two distinct institutional Source records (WHO and EPA). That proves structural source diversity, not material independent corroboration for the precise propositions.

- For A, EPA directly supports contaminant-specific treatment and limits. The historical WHO programme-page description establishes broad public-health context, but the surviving record does not show a distinct WHO passage that independently corroborated the proposition that treatment targets depend on intended use.
- For C, EPA's technology-specific limitations directly support the non-universality boundary. The surviving WHO description is domain-level context; no historical WHO passage is preserved that independently corroborates that same boundary.

Accordingly, E2 is the more conservative technical direction on the surviving substantive material, but it is **not** adopted as the historical winner. E3 is also not established merely by counting two institutions or by relying on the present-day WHO Guidelines. The historical conflict cannot be resolved to the required provenance standard.

## 4. Formal disposition

For both `CLM-WATER_TREATMENT_BASICS-A@1` and `CLM-WATER_TREATMENT_BASICS-C@1`:

- Preserve Batch 21 E2 and Batch 27 E3 unchanged.
- Record `UNRESOLVED — HISTORICAL EVIDENCE NOT RECOVERABLE`.
- Do not select E2 or E3 as the winning historical assessment.
- Do not count either historical row as a validated current-version assessment.
- Exclude these historical E2/E3 disputes from the current-version scoring calculation. The current assessment must independently evaluate the exact current Claim@version and its current canonical Evidence Use/Source chain under the active rubric.
- Keep the source-chain repair and high-consequence/Human View gates separate from this historical disposition.

The strict current locator rule remains in force: where the current canonical Evidence Use lacks a reproducible claim-specific page/section/paragraph/table/figure locator, a current E score above 1 is not available until the locator is corrected and verified. This current rule does not retroactively alter the preserved historical E2/E3 rows.

## 5. What this closes — and what it does not

**Closed:** the one final bounded attempt to recover the historical WHO passages and reviewer notes. The surviving primary materials do not contain them; no further repetitive search of the same report set is warranted unless new primary evidence appears.

**Not closed:** current-version source quality, current D/E/B scoring, evidence-chain remediation, independent human review, high-consequence review, Human View, Relations, rights/publication suitability, or M13 overall.

No canonical Claim, Evidence Use, Source, Assessment, Relation, or score record was changed. No new Batch or Package was created. PR #21 remains Draft/unmerged. `main` was not modified. This report is a historical-provenance disposition only; it is not Phase 1 authorization or release approval.

## 6. Next operation

Proceed to a reproducible current-version reconciliation of all 1,494 Claims using `Claim ID@version`. For every Claim, classify the available prior material as (a) reusable exact-version, claim-specific assessment with adequate evidence provenance; (b) partial assessment requiring targeted revalidation; (c) historical mention / score row only; or (d) no usable assessment. Separately flag current Evidence Use/Source locator repairs and source-independence questions.

Do not infer readiness from the 1,501-row historical ledger, a matching Claim ID, or a prior report mention. Do not start Batch 55. First publish the exact-HEAD reconciliation counts, exceptions and non-overlapping current-review needs; then continue the census in the already authorized M13 workflow.
