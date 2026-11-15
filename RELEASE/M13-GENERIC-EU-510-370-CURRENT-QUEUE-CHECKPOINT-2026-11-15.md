# M13 — current generic-EU 507 → 367 residual queue checkpoint

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
State: **current routing checkpoint; proposal-only; no canonical writes**.

> This checkpoint supersedes the 516/376 intermediate routing and the historical 359-row ledger for current work. The 359-row ledger remains a valid historical subset, not the current denominator.

## 1. Exact current population

| Population | Count |
|---|---:|
| Current generic-EU Claim/Evidence Use pairs | 507 |
| High-consequence candidates within those 510 | 120 |
| Previously reviewed priority second-pass Claims | 20 |
| **Current residual remediation population** | **367** |

Arithmetic: `507 - 120 - 20 = 367`.

The 20 priority Claims are all present in the 507-candidate set and are disjoint from the 120 high-consequence subset. Every candidate maps to one Claim; the coverage artifact reports 0 unmapped and 0 ambiguous Evidence Use IDs. The 17 Claims identified in the OpenStax/tax false-positive correction were previously imported into the residual. Three `CLM-ENERGY_BASICS-A/B/C` records subsequently left the generic-EU set after their Evidence Use descriptions were corrected with claim-specific OpenStax College Physics Chapter 7 pinpoints. The remaining 14 of those 17 are still in the current 367 residual population.

## 1A. Separate unassessed-risk queue overlap

The M13 Audit Queue Automation workflow on exact branch revision `e0b5f8989738c94d9b16dacd4fa9671190e14086` selected 42 unassessed-risk Claims from 42 candidates in a requested 100-slot batch; 58 slots were unfilled. The workflow excluded 708 previously screened Claims and 17 unreconciled holdouts, with 15 reviewed-holdout overlaps and 710 unique exclusions.

**14 of the 42 selected Claims also occur in this 367-row residual ledger.** All 14 have existing source-review report filename mentions and are marked in the reconciled CSV with `unassessed_risk_queue_overlap=true`, lane 1. This is a cross-queue overlap, not 14 additional Claims. Reuse the existing passage-review work; do not repeat source searches solely because the claims appear in both queues. The other 28 selected unassessed-risk Claims are outside the 370 generic-EU residual population and remain in the separate risk workflow.

## 2. Exact artifacts and revisions

- Generic-EU coverage workflow run `43710332774`, artifact `14159847839`, generated on branch commit `bb73e1342192f7926af7e247fe0759a481b47a37`: 507 mapped candidates, 507/507 report mentions, 507/507 source-review filename mentions, 0 unmapped, 0 ambiguous.
- Claim worksheet refreshed on the current HEAD by Reference Tests workflow run `43741578315`: 4,851 records scanned, 1,494 Claims, 131 `legal_financial` domain matches, 519 `high_consequence_screen` flags. The workflow's final worksheet artifact is recorded in the exact-head CI checkpoint.
- Current branch HEAD when this checkpoint was refreshed: `42b2bb87f1fae9c0ba2ac99fdfe62ba9668b41b3`.

Coverage is exact-ID and filename/text mention coverage only. It is not proof of semantic review, exact passage support, rights clearance, specialist approval or publication readiness.

## 3. Six records removed from the former 516-candidate set

The exact 516 → 510 set difference contains these six Evidence Use records:

- `EU-ASSET_MANAGEMENT_BASICS-A`
- `EU-ASSET_MANAGEMENT_BASICS-B`
- `EU-ASSET_MANAGEMENT_BASICS-C`
- `EU-BEHAVIORAL_BIOLOGY_BASICS-A`
- `EU-BEHAVIORAL_BIOLOGY_BASICS-B`
- `EU-BEHAVIORAL_BIOLOGY_BASICS-C`

All six are now EU v3 with claim-specific source descriptions and no longer match the generic-description markers. Their removal from this routing queue is not a substantive approval. Asset Management B still has an unsupported opportunities element; Behavioural Biology C remains only partially supported and the OpenStax rights boundary remains unresolved. Existing HOLD/PARTIAL/RIGHTS HOLD dispositions remain in force.

## 4. Seventeen reclassified Claims imported into residual work

The 17 exact Claim/EU/Source triples in `M13-RISK-SCREEN-OPENSTAX-TAX-SUBSTRING-FALSE-POSITIVE-2026-11-15.md` are all present in the current 510 coverage set and all 17 are in the 370 residual population. Reuse their existing passage reviews; do not repeat the source search. Preserve the specific findings there, including OpenStax rights holds, missing locators, scope boundaries and the motion speed/velocity issue.

## 5. Current companion ledger

A refreshed 367-row CSV and README have been generated in the current ChatGPT conversation:

- `M13-residual-367-generic-EU-remediation-ledger-cross-queue-reconciled-2026-11-15.csv`
- `M13-residual-367-generic-EU-remediation-ledger-cross-queue-reconciled-README-2026-11-15.md`

The CSV is unique by EU ID and carries Claim/EU/Source references, slice, canonical EU path, machine risk flags, Claim statement, existing evidence material, source identities/URIs, source-review report mentions, human review state and D/E/B fields. Every row explicitly sets `human_confirmation_required=true` and `canonical_write_authorized=false`.

## 6. Authorization boundary

- No Claim, Evidence Use, Source, Context, Scope, Relation, risk metadata or D/E/B record was modified by this routing checkpoint.
- Do not interpret machine flags as semantic risk findings.
- Do not interpret filename mentions as proof of source-passage review.
- Re-read current canonical records before any proposal; import existing support, rights, jurisdiction, independence and HOLD findings.
- Any canonical correction requires a separate bounded authorization, versioned changes and regression tests.
- The separate 42-Claim unassessed-risk automation queue overlaps this residual ledger in 11 Claims; these are explicitly tagged in the reconciled CSV and must not be counted as an additional population.

M13 remains **OPEN / NOT RELEASE-READY**. PR #21 remains Draft/unmerged and `main` remains unchanged. A fresh exact-head Reference Tests, Release Conformance Gate and Offline Edition 3/3 pass is required after the final documentation/test commits.
## 7. 507 → 367 refresh after energy-basics correction

The exact-head coverage artifact from run `43741572801` now reports 507 generic-EU candidates, all mapped, with zero unmapped or ambiguous IDs and 507/507 report/source-review filename mentions. The energy-basics A/B/C EU v3 corrections removed three formerly generic descriptions. The 20 priority Claims remain present and disjoint from the 120 high-consequence candidates. The resulting residual is 367. The refreshed selected-risk queue from run `43741572645` still contains 42 Claims; 11 overlap this 367 set and 31 are separate. The prior 370-row CSV is superseded for current routing.
