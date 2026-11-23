# M13 — unassessed-risk screen coverage reconciliation

Date: 2026-11-14  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Queue denominator: 711 Claims (source revision `f26820e59b08b4036ad78302dad8118c51dac540`)

## Finding

The four earlier 14 November screening reports state cumulative coverage of 61/711. That figure is a **reported screen-observation count**, not yet a reconciled count of unique Claim IDs.

A deterministic extraction of explicit Claim IDs from the four reports gives:

| Report | Reported inspected count | Explicit Claim-ID occurrences | Explicit unique IDs |
|---|---:|---:|---:|
| Preliminary content-level screen | 17 | 3 | 3 |
| Second screen | 15 | 15 | 15 |
| Package 03 | 18 | 18 | 18 |
| Package 04 | 11 | 11 | 11 |
| Total | 61 | 47 | 45 |

Two Claim IDs are repeated across reports: `CLM-AFTERSHOCK-DAMAGE` and `CLM-FLOOD-FOOD-FDA-CONTACT`. The preliminary screen explicitly names only those three high-priority Claims, then says that 14 further Claims were inspected but does not enumerate their IDs. Package 03 also repeats the two high-priority Claims in its 18-row list while describing the package as additional. The four reports therefore do not currently support a claim that 61 distinct queue entries have been screened.

## Consequence for Packages 05 and 06

Packages 05 and 06 each contain explicit Claim IDs not present in the 45-ID set extracted from the four prior reports. Together they add 35 distinct, explicitly identified Claims relative to that explicit-ID set. However, because the earlier preliminary report does not enumerate its other 14 inspected IDs, full historical deduplication against all 61 reported observations is not yet proven.

Do not calculate or publish a cumulative unique coverage percentage by simply adding 61 + 20 + 15. The defensible current statement is:
- 711 queue entries in the source denominator;
- 45 unique Claim IDs explicitly enumerated in the four earlier reports;
- 35 further explicit Claim IDs in Packages 05 and 06;
- 14 previously reported inspected Claims remain unidentified in the preliminary report;
- 2 repeated explicit Claim IDs appear in more than one earlier report.

## Required reconciliation

The historical identity-recovery step is closed as unrecoverable on 2026-11-18. The available preliminary report, reconciliation, subsequent screen packages, PR #21 changed-file inventory, and repository code search do not identify the 14 omitted IDs. No further search loop is authorized or useful unless genuinely new primary evidence is found.

For future queue accounting only:
1. Normalize every explicitly recorded Claim ID to exact `record_id@version` identity.
2. Build and maintain one deduplicated ledger with queue source revision, Claim ID/version, first review package, repeat review packages, review scope, source/EU inspection level, disposition and reviewer.
3. Verify every reviewed ID belongs to the applicable queue revision and that no ID/version was silently substituted.
4. Recompute unique coverage and remaining queue only from that ledger. Keep the 14 historical observations outside the count of ID-verified Claims.

## Disposition — 2026-11-18

- Status: `UNRESOLVED — historical identity not recoverable` (14 observations; Claim IDs and versions absent from the primary report).
- This is a provenance/accounting limitation, not 14 newly identified Claims, not 14 additional queue entries, and not evidence that 14 particular Claims were assessed.
- The 14 observations are excluded from verified unique-ID coverage and from any claim-level D/E/B, source-fit, risk, or completion totals.
- Do not infer or assign IDs from topic descriptions. Do not repeatedly search the same reports, packages, PR file inventory, or repository index.
- Reopen only if new primary evidence appears (for example, original reviewer notes or an artifact explicitly listing the selected IDs).
- All other screening and M13 audit work proceeds using explicit, versioned Claim IDs and traceable evidence.

## Integrity boundaries

This reconciliation does not change any Claim, Evidence Use, Source, risk metadata or D/E/B score. It does not reclassify any of the 14 unidentified observations as complete or incomplete. Until the IDs are recovered, cumulative unique coverage remains **unreconciled**.
