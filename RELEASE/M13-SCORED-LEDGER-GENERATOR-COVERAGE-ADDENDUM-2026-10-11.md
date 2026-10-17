# M13 Scored-Ledger Generator Coverage Addendum

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **coverage defect corrected in the generator; latest exact-head unit/CI validation still required**

## Defect found

The automated generator `REFERENCE/m13_claim_scored_report_ledger.py` originally read only table rows from `M13-CLAIM-REVIEW-BATCH-*.md`. That omitted:
- Batch 12's three D/E/B results, which are encoded in Claim-level headings rather than a score table;
- the six Batch 41 scored-block reports, which use a six-column table with an ordinal and Claim ID;
- six Batch 41 rows whose Claim ID cells contain explanatory filename/internal-ID alias annotations in parentheses.

The generated artifact therefore contained 156 rows, 152 normalized IDs, and four duplicate groups, while the authoritative working ledger represented 259 rows and 252 normalized IDs. This was a real **audit tooling coverage defect**: the generated artifact understated the set of historical scores and could not serve as the full score ledger.

## Correction

The generator now:
1. parses Batch 12's three heading-form scores and captures their Assessment rationale;
2. parses all six Batch 41 scored blocks;
3. accepts the parenthetical filename/internal-ID alias notes without changing the actual scored Claim ID;
4. keeps comparison-only ID normalization and never rewrites stored identifiers;
5. declares the actual input scope in its machine summary.

A regression guard now pins the current expected coverage:
- 1,494 Claim records in the inventory;
- 259 scored report rows;
- 252 normalized Claim IDs;
- seven repeated-ID groups, 14 rows within those groups;
- zero scored rows unmatched to the Claim inventory;
- exactly three Batch 12 rows and 100 Batch 41 rows.

## Verification evidence and limitation

On CI checkout revision `f39f0dbc51bceb3726ee5945370cb878566e70b7` (the pull-request merge checkout corresponding to branch HEAD `df081dc295e9d6e41bb52627896163da1cbef8fd`), the corrected generator executed successfully and produced:
- 259 CSV rows;
- 100 Batch 41 rows, distributed 6 + 14 + 20 + 20 + 20 + 20 across Blocks 01–06;
- 252 normalized IDs and seven duplicate groups;
- zero unmatched scored rows.

Content preflight and artifact generation passed in that run. The full Reference test step was still in progress when this report was written; because the branch has since received this addendum and the scope-description update, the three required workflows must be checked again on one exact final HEAD. This report does **not** claim those final checks have passed.

## Protected-state boundary

No Claim, Evidence Use, Source or Relation JSON changed. `main` remains protected. PR #21 must remain open as Draft and unmerged. This correction repairs accounting coverage only; it does not establish that any historical score is substantively correct, that all Claims are unique, or that M13 is complete.
