# M13 — residual 356 generic Evidence Use queue: nested-reference check tranche 03

Date: 2026-11-23  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Input queue: workflow run 43748097686, artifact 14174823129 (`m13-generic-eu-report-coverage.json`), reconciled against artifact 14174388824 (`M13-CLAIM-AUDIT-WORKSHEET.csv`) and the exact 20-Claim priority review.

## 1. Scope and deterministic queue reconstruction

The queue is the 496 generic-EU candidate set after removing:
- 120 exact candidate Claims carrying the worksheet's `high_consequence_screen` machine-triage flag;
- the disjoint 20 exact Claims in `M13-REMAINING-379-PRIORITY-20-CLAIM-SOURCE-PASSAGE-REVIEW-2026-11-12.md`.

Independent reconstruction:
- 496 candidates matched to worksheet: 496/496;
- high-consequence subset: 120;
- priority second-pass subset: 20;
- overlap: 0;
- residual queue: 356;
- unique Claim IDs / EU IDs / canonical paths: 356 / 356 / 356;
- distinct Source IDs: 135.

The queue file paths and IDs were taken from the exact coverage artifact, not generated from naming assumptions.

## 2. Completion of nested EU reference checks

Tranche 01 documented 100 fresh full structural EU checks and 14 earlier strict-locator checks. Tranche 02 documented identity/version checks for the remaining 256 EU records. This tranche closes the remaining nested-reference work for the 242 EU rows not already included in the earlier 114 full structural checks.

For each of the 242 exact residual EU records, this tranche fetched the canonical JSON at the M13 branch and checked:
- canonical record ID equals the queue's exact Evidence Use ID;
- record version is exactly `1`;
- `content.claim_ref` resolves to the exact queue Claim ID at version `1`;
- `content.source_ref` resolves to the exact queue Source ID at version `1`.

Result: **242/242 exact nested-reference matches; 0 mismatches; 0 missing canonical paths**.

Combined with the previously documented 114 full structural checks, the complete residual queue now has:
- **356/356** EU canonical identity/version checks;
- **356/356** EU Claim@1 and Source@1 nested-reference checks;
- **0** identity, version or nested-link mismatches.

The 242 checks are the remaining set after removing the 100 EU IDs enumerated in tranche 01 and the 14 strict-locator EU IDs listed in the 2026-11-15 residual integrity report. No row was counted twice.

## 3. Source identity/version coverage

The preceding tranches directly fetched and checked all 135 distinct Source records at their exact canonical paths:
- expected Source record ID: 135/135;
- version `1`: 135/135;
- mismatches: 0.

This confirms endpoint identity and version only. It does not establish passage-level support, source currency, rights, independent corroboration or expert acceptance.

## 4. Consolidated structural ledger

| Control | Result |
|---|---:|
| Exact residual Claim/EU mappings | 356 |
| EU canonical paths checked | 356/356 |
| EU record ID/version checked | 356/356 |
| EU Claim@1 nested references checked | 356/356 |
| EU Source@1 nested references checked | 356/356 |
| Distinct Source records checked | 135/135 |
| Missing canonical paths | 0 |
| Identity/version/nested-link mismatches | 0 |
| D/E/B scores assigned in these tranches | 0 |
| Canonical content records modified | 0 |
| Canonical writes authorized | 0 |

## 5. Verification limits and next work

This is a structural identity/version/reference audit. It is not:
- proof that the cited source passage supports the Claim;
- proof that the locator is reproducible or sufficiently specific;
- rights or licence clearance;
- source-independence/diversity certification;
- specialist or Human View approval;
- D/E/B evaluation;
- publication or release authorization.

The next M13 work is therefore no longer basic canonical-link reconciliation for this 356-row queue. It is exact source-review report-body reconciliation by Claim/EU/Source/version, followed by passage/locator reproducibility, source diversity, evidence quality, risk routing and separately authorized expert assessment.

All 356 Claims remain subject to their existing HOLD and human-confirmation requirements. No historical evaluation was transferred into current D/E/B fields. No Claim, EU, Source, Assessment, Relation, risk, allowlist or publication record was changed. PR #21 remains Draft/open/unmerged; `main` was not modified.
