# M13 Reconciliation Addendum — Water Treatment Evidence-Use Cross-Link
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Related report: `RELEASE/M13-DUPLICATE-SCORE-ADJUDICATION-WATER-A-D-2026-10-11.md`
Status: audit-report correction; no content JSON changed.

## Why this addendum exists
A follow-up inspection of the water-treatment record graph found three additional Evidence Use records that were not included in the first adjudication's direct-link check:
- `EU-M5-EPA-DRINKING-WATER-A` → `CLM-WATER_TREATMENT_BASICS-A` and `SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES`
- `EU-M5-EPA-DRINKING-WATER-B` → `CLM-WATER_TREATMENT_BASICS-B` and `SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES`
- `EU-M5-EPA-DRINKING-WATER-C` → `CLM-WATER_TREATMENT_BASICS-C` and `SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES`

Therefore the prior report's statement that Claim B has no explicit EPA Evidence Use link was too broad when applied to the entire record graph. The narrower observation remains true: `EU-WATER_TREATMENT_BASICS-B` itself points to WHO while its description mentions EPA. But a separate, correctly linked EPA Evidence Use exists for the same Claim. Treat this as a **local description/source-ref mismatch in one EU record**, not a missing graph-level EPA link.

## Corrected interpretation
1. Do not open a graph-level missing-EPA-link defect for Claim B; the explicit EPA link already exists.
2. Keep a lower-severity metadata/description consistency flag on `EU-WATER_TREATMENT_BASICS-B`: its own `source_ref` is WHO while its description mentions EPA. In an authorized correction phase, either make that description WHO-specific or ensure descriptions clearly distinguish the separately linked EPA record. No correction is performed here.
3. Reconsider the provisional E=2 for Claim B on the evidence graph as a whole. The additional EPA Evidence Use describes treatment options in relation to target contaminants and water-quality characteristics, which is directly relevant to the Claim. This strengthens the case for E=3, but the final value should remain provisional until the duplicate-score ledger is recomputed against all evidence-use records and the actual source passages. Do not treat an institutional domain landing page alone as proof of passage-level traceability.
4. Claims A and C also have separate EPA Evidence Use records. Their earlier E=2 dispositions should be read as traceability cautions, not as evidence that they lack EPA linkage. The EPA record descriptions are claim-relevant but still broad and do not preserve precise section/paragraph locators.
5. The emergency-disinfection Claim D remains 3/3/3 in both reports, with its distinct EPA emergency-disinfection source.

## Graph check
For A, B, and C, the WHO-linked and EPA-linked Evidence Use records each point to the intended Claim and to a Source record with role `supports`. The existence of multiple Evidence Use records must be counted as multiple evidence links, not multiple Claims. This addendum makes no assertion that the sources are fully independent or that their evidence is sufficient in every intended use.

## Ledger handling
- Retain the original report and this addendum as audit history.
- Before the consolidated ledger is finalized, resolve the adjudicated E score for Claim B using all linked Evidence Use records and source-level support, not a single-EU-only view.
- Do not alter Claim/Evidence Use/Source JSON in this pass.
- M13 remains open; inventory-wide reconciliation, semantic duplicate adjudication, Relations, Human View, independent review, authorized corrections, regressions and same-HEAD CI remain outstanding.
