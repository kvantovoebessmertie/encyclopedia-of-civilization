# P2–P9 MATURITY GAP SCAN — 2026-10-07

## Purpose

Retroactive maturity scan of P2–P9 against the stricter maturation standard established and exercised in P10.

**Important:** this is a gap scan only. No content, source, Evidence Use, Relation or regression contract is modified by this artifact.

## Baseline

- Current HEAD: `afdda7cfe133cfc0a9e24292429baaf8d217bd34`
- Corpus: 478 vertical slices / 4500 records / 19 record types.
- P10 is CLOSED with D01–D12 closed and final Reference + Release Gate + Offline 3/3 GREEN.
- P2–P9 each have their own closure/re-audit artifacts and were not reopened automatically.

## Audit rule

A historical wave is considered **retroactively clean** only if its current repository state satisfies the P10 maturity dimensions below. Historical closure is evidence of prior conformance, not a substitute for this scan.

### Maturity dimensions

1. Claim depth: definition, mechanism/dependency, conditions and limitations where materially relevant.
2. Claim-specific Evidence Use: each Evidence Use describes what the source supports for the linked Claim and where the evidentiary boundary ends.
3. Evidence independence: distinct provenance where corroboration materially matters; no artificial source-count inflation.
4. Applicability/uncertainty: jurisdiction, date, population, method, context and causal limits where relevant.
5. Cross-slice linkage: relations are semantically justified, bounded and not manufactured for count.
6. Human View/adversarial: knowledge does not silently become individualized, current or operational instruction.
7. Documentation/coverage/regression synchronization.
8. Identity/duplicate integrity and reverse traceability.

## Wave-by-wave status

| Wave | Historical closure evidence | P10-standard retroactive status | Finding |
|---|---|---|---|
| P2 | Substantive re-audit PASS; prior evidence/Human View findings closed | **GAP-SCAN REQUIRED** | Prior closure is strong, but no explicit P10-style claim-by-claim Evidence Use specificity pass is recorded for the full P2 target cluster. |
| P3 | Correction + re-audit recorded zero open substantive findings | **GAP-SCAN REQUIRED** | Source independence and documentation were corrected, but full P10-style claim-level material-boundary verification is not explicitly recorded. |
| P4 | Full substantive re-audit recorded zero remaining findings | **GAP-SCAN REQUIRED** | Strong safety/topology audit; nevertheless the P10 claim-level Evidence Use specificity criterion was not separately applied to the full cluster. |
| P5 | Full substantive re-audit recorded zero remaining findings | **GAP-SCAN REQUIRED** | Strong provenance and Human View coverage; no explicit retroactive P10-style claim-by-claim Evidence Use specificity result. |
| P6 | Substantive re-audit PASS; all listed debts closed | **GAP-SCAN REQUIRED** | Evidence independence and Human View were checked, but P10-style claim/material specificity was not separately recorded. |
| P7 | Substantive re-audit CLEAN; linkage and Human View passed | **GAP-SCAN REQUIRED** | Strong claim/source integrity and linkage; P10-style Evidence Use semantic-boundary audit remains unrecorded. |
| P8 | Substantive re-audit + Human View PASS | **GAP-SCAN REQUIRED** | Broad maturity dimensions passed, but the exact P10 claim-level Evidence Use material-boundary screen is not explicitly evidenced. |
| P9 | Final re-audit + Human View + final 3/3; P9 CLOSED | **PARTIAL GAP** | P9 already performed substantially similar evidence-depth/applicability/Human View work; only a targeted P10-style Evidence Use specificity consistency check is needed. |

## Confirmed residual debt vs audit debt

At this stage the scan identifies **no confirmed content defect** in P2–P9.

It does identify a class of **audit debt**:

**MG-01 — Retroactive claim-specific Evidence Use verification**

The repository has historical evidence of source independence, claim→Evidence Use→source linkage, applicability and Human View checks across P2–P9, but the stricter P10 requirement that Evidence Use material be explicitly bounded to the exact Claim is not uniformly recorded as having been checked across all historical target clusters.

This is not a claim that the old Evidence Use records are wrong. It is a verification gap.

**MG-02 — Retroactive Human View consistency verification**

P2–P9 each contain Human View/adversarial evidence, but the P10 adversarial question set is now more explicit. A targeted scan should verify that old high-consequence clusters still preserve the same boundaries against individualized/current/operational interpretation.

**MG-03 — Retroactive cross-slice reconciliation**

Historical waves contain different Relation baselines (31 → 35+). Their closure artifacts generally reconcile dedicated cross-slice counts, but a single current-tree reconciliation should confirm that no valid non-cross-slice Relation is being confused with the dedicated Cross-Slice baseline.

## What is explicitly NOT a finding

- Different slice topologies are not defects by themselves.
- Single-source foundational slices are not defects by themselves when their claim scope is intentionally narrow.
- Lack of a technical locator is not a defect when Evidence Use material is semantically bounded under STANDARD/004 §4.
- No new Relation is not a defect when no material dependency exists.
- Historical closure artifacts are not reopened merely because the P10 standard is stricter.
- No mass rewrite is authorized.

## Required next stage

1. Run a targeted P2–P9 claim/Evidence Use material-boundary audit, prioritizing high-consequence and previously corrected slices.
2. Run the P2–P9 Human View/adversarial consistency screen using the P10 scenario set.
3. Reconcile current global Relation count vs dedicated Cross-Slice Relation count.
4. Produce a **P2–P9 Unified Retroactive Debt Map** containing only confirmed defects.
5. Fix confirmed debts only.
6. Re-audit the corrected state.
7. Run full technical CI and verify the resulting tree.
8. Only after the retroactive scan is clean, begin P11.

## Decision

**P2–P9 are NOT reopened.**

They are placed into a controlled **retroactive maturity verification** stage. The current result is an audit-gap inventory, not a defect inventory.

No content changes were made by this scan.
