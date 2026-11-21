# M13 master remediation — exact report-body import 17

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Source report: `RELEASE/M13-BATCH-47-LANE-02-SOURCE-PASSAGE-REVIEW-2026-11-12.md`
Source report blob: `b05db4e7366ccc4da2870cd1f7c8dd4df7560a1b`

## Scope and exact join

The full source report reviews 20 Claims. Exact Claim-ID matching against the 359-row residual Generic Evidence Use cohort yields **8** rows. Twelve report entries are outside the residual cohort and excluded. No fuzzy or normalized-ID matching was used.

All 8 canonical Evidence Use JSON records were fetched from the exact paths recorded in the master ledger at this branch. Each is record version 1, and its `content.claim_ref` and `content.source_ref` exactly match the expected Claim v1 and Source v1 IDs. Exact EU blob SHAs are recorded in the CSV ledger. This verifies the current EU edges only; it does not certify the full Claim/Source contents or source passage validity.

## Imported findings

| Claim ID | Desk D/E/B | Import disposition | Finding / next action |
|---|---:|---|---|
| CLM-UNITS_AND_MEASUREMENT-C | 2/1/2 | PARTIAL | NIST SI Units is relevant to units, but the Claim's method and measurement-uncertainty elements require the GUM/VIM rather than an SI-units page alone. Add VIM/GUM pinpoint and preserve the distinction between unit, method, and uncertainty. |
| CLM-ZOOLOGY_BASICS-A | 2/1/2 | NOT_ESTABLISHED_BY_CURRENT_SOURCE | OpenStax Biology 2e Chapter 28 concerns animal diversity, but the Claim is a general definition of zoology and the source identity sentence is not the chapter's exact definition. Add an authoritative zoology definition and scope. |
| CLM-CLIMATE_ADAPTATION-A | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | IPCC AR6 WGII directly uses hazard, exposure, and vulnerability in climate-risk framing; the registered report landing page lacks the exact figure/section locator and the role of capacity should be preserved. Add SPM/Chapter locator. |
| CLM-CLIMATE_ADAPTATION-B | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | IPCC WGII supports context-specific adaptation across systems and climate impacts, but the Claim's exact boundary needs a specific chapter/section locator. |
| CLM-CLIMATE_ADAPTATION-C | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | IPCC WGII discusses adaptation limits and residual risks, supporting the proposition. Add the exact section/figure locator and distinguish limits, barriers, and residual risk. |
| CLM-CLIMATE_BASICS-A | 3/1/2 | DIRECT_WITH_PINPOINT_GAP | NASA Climate Change is relevant to long-term patterns and changes in weather conditions, but the broad page does not identify the exact climate definition. Add NASA climate-vs-weather definition locator. |
| CLM-CLIMATE_BASICS-B | 3/1/2 | DIRECT_WITH_PINPOINT_GAP | NASA climate material is relevant to observations, measurements, and models across long time scales, but the registered page does not pinpoint the methods statement. Add exact section and scope. |
| CLM-CLIMATE_BASICS-C | 3/1/3 | DIRECT_WITH_PINPOINT_GAP | NASA explicitly distinguishes climate as long-term patterns from individual weather events. Add the exact section locator. |

## Control results

- Exact residual-cohort imports: **8/8**.
- Out-of-cohort report entries excluded: **12**.
- Canonical Evidence Use records modified: **0**.
- Claim, Source, Context, Scope and Relation records modified: **0**.
- Official D/E/B values overwritten: **0**; desk scores remain separate provisional fields.
- All 8 Claims remain **HOLD**.
- Specialist, independent, Human View, rights, editorial and publication gates remain uncleared.
- No canonical-write authorization is created or implied.

Disposition labels are conservative ledger classifications derived from the report narrative, not new specialist adjudications. Append-only remediation documentation; not release or publication approval.
