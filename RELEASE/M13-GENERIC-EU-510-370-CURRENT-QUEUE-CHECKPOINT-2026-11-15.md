# M13 — current generic-EU 510 → 370 residual queue checkpoint

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
State: **current routing checkpoint; proposal-only; no canonical writes**.

> This checkpoint supersedes the 516/376 intermediate routing and the historical 359-row ledger for current work. The 359-row ledger remains a valid historical subset, not the current denominator.

## 1. Exact current population

| Population | Count |
|---|---:|
| Current generic-EU Claim/Evidence Use pairs | 510 |
| High-consequence candidates within those 510 | 120 |
| Previously reviewed priority second-pass Claims | 20 |
| **Current residual remediation population** | **370** |

Arithmetic: `510 - 120 - 20 = 370`.

The 20 priority Claims are all present in the 510-candidate set and are disjoint from the 120 high-consequence subset. Every candidate maps to one Claim; the coverage artifact reports 0 unmapped and 0 ambiguous Evidence Use IDs. All 17 Claims identified in the OpenStax/tax false-positive correction are present in the current 370 residual population.

## 2. Exact artifacts and revisions

- Generic-EU coverage workflow run `43710332774`, artifact `14159847839`, generated on branch commit `bb73e1342192f7926af7e247fe0759a481b47a37`: 510 mapped candidates, 510/510 report mentions, 510/510 source-review filename mentions, 0 unmapped, 0 ambiguous.
- Claim worksheet workflow run `43710480136`, artifact `14160401976`, PR merge-tree source revision `4a1b48229669202ffa4eeb1b89e5d884d93f38fb`: 4,851 records scanned, 1,494 Claims, 131 `legal_financial` domain matches, 519 `high_consequence_screen` flags.
- Current branch HEAD when this checkpoint was prepared: `6290dface563bc152cd311f8a0d91af590348a6d`.

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

A 370-row CSV and README have been generated in the current ChatGPT conversation:

- `M13-residual-370-generic-EU-remediation-ledger-2026-11-15.csv`
- `M13-residual-370-generic-EU-remediation-ledger-README-2026-11-15.md`

The CSV is unique by EU ID and carries Claim/EU/Source references, slice, canonical EU path, machine risk flags, Claim statement, existing evidence material, source identities/URIs, source-review report mentions, human review state and D/E/B fields. Every row explicitly sets `human_confirmation_required=true` and `canonical_write_authorized=false`.

## 6. Authorization boundary

- No Claim, Evidence Use, Source, Context, Scope, Relation, risk metadata or D/E/B record was modified by this routing checkpoint.
- Do not interpret machine flags as semantic risk findings.
- Do not interpret filename mentions as proof of source-passage review.
- Re-read current canonical records before any proposal; import existing support, rights, jurisdiction, independence and HOLD findings.
- Any canonical correction requires a separate bounded authorization, versioned changes and regression tests.

M13 remains **OPEN / NOT RELEASE-READY**. PR #21 remains Draft/unmerged and `main` remains unchanged. A fresh exact-head Reference Tests, Release Conformance Gate and Offline Edition 3/3 pass is required after the final documentation/test commits.