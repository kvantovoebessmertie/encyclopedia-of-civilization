# M13 Next-Stage Reconciliation Checkpoint — 2026-10-11

Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **major reconciliation work in progress; M13 remains OPEN**.
Protected state: PR #21 must remain open as Draft and unmerged; `main` must not change.

## Work completed in this stage

### 1. Consolidated Claim scoring ledger
- Combined scored rows from Batch 12, general review batches 17–40, and Batch 41 scored blocks 1–6.
- **259 report rows** are represented with Claim ID, candidate inventory path, internal `record_id`, duplicate/alias status, D/E/B scores, and rationale/disposition.
- **252 normalized report-ID groups** remain after removing seven confirmed repeat rows.
- Frozen Claim inventory denominator: **1,494 Claim-prefixed JSON files**.
- Provisional arithmetic: **252 unique normalized scored IDs**, leaving **1,242 not represented by a unique scored row** before full inventory reconciliation and semantic duplicate analysis.
- The ledger is a review ledger, not a final acceptance register.

Ledger: [M13 consolidated Claim audit ledger](M13-CONSOLIDATED-CLAIM-AUDIT-LEDGER-WORKING-2026-10-11.md)

### 2. Duplicate and score-conflict reconciliation
Seven repeated-ID groups were confirmed:
- Three nuclear-physics Claims appear in Batch 12 and Batch 17.
- Four water-treatment/emergency-disinfection Claims appear in Batch 21 and Batch 27.

The three nuclear Claims have different D/E/B values between Batch 12 and Batch 17. Both sets remain visible; no score was silently overwritten. A canonical score decision and rationale are still required. Batch 41 has no exact or separator-insensitive ID overlap in the inspected prior reports, but semantic duplicates remain an open gate.

### 3. Batch 41 Claim → Evidence Use → Source structural linkage
- **100/100 primary Batch 41 links** were opened and checked.
- Claim record type, Claim `record_id`, EU `claim_ref`, EU `source_ref` versus Claim provenance, `supports` role, and Source record existence passed the structural check under exact/comparison-only separator matching.
- An additional **15 Evidence Use records** were found in the 33 candidate slices and individually inspected. They point to Batch 41 Claims, use `supports`, and resolve their Source records.
- Across primary and additional evidence links, **44 unique Source records** were inspected for metadata identity/URI consistency.
- A separate post-score reconciliation classifies **49/100 primary EU descriptions as generic** and **52/100 rows as having locator-specificity gaps**; these categories overlap. The linkage table preserves the actual description text, but a description—generic or otherwise—is not proof of pinpoint evidence support. See [Batch 41 post-score reconciliation](M13-BATCH-41-POST-SCORE-RECONCILIATION-2026-10-11.md).
- One confirmed Source identity/URI mismatch remains: `SRC-ASSET_MANAGEMENT_BASICS` labels ISO 55000:2024 while its URI points to ISO 55001:2024. No content record was changed.
- Fifteen additional EU records refer to 11 distinct Source IDs beyond the primary sources. URI-host comparison indicates 14/15 are on a different publisher domain than the primary source; the agricultural-engineering corroboration and primary source both use FAO, so that pair is not publisher-independent. Different domains still do not prove claim-specific fit or independence of the underlying evidence.

Linkage report: [Batch 41 linkage reconciliation](M13-BATCH-41-LINKAGE-RECONCILIATION-2026-10-11.md)

### 4. Relation graph structural audit
- All **64 Relation JSON records** were inspected.
- **0 structural errors** were found in this pass: participant references, frame/context references, provenance Source references and role/participant cardinality resolve.
- This does not establish that the relations are semantically justified, that direction/roles are correct, or that linked Claims are independently evidenced.

Relation report: [M13 Relation graph audit](M13-RELATION-GRAPH-AUDIT-2026-10-11.md)

## Findings that must not be hidden by a green structural result
1. Structurally valid pointers do not demonstrate source passage fit.
2. Generic Evidence Use descriptions remain a substantial traceability weakness.
3. ISO 55000/55001 Source identity mismatch needs an authorized, separately reviewed correction plan; no Source JSON was edited.
4. The Batch 12/17 nuclear score conflicts require explicit adjudication.
5. Report-ID uniqueness does not rule out semantic duplicates.
6. Relation endpoint existence does not prove relation meaning or source independence.

## Remaining M13 gates

1. Finish the inventory-to-ledger join for all 1,494 Claims and document exclusions/aliases/semantic duplicates.
2. Adjudicate duplicate report score conflicts; keep every historical score and disposition auditable.
3. Complete claim-specific locator/source-fit review for Batch 41 and the earlier scored rows; distinguish generic metadata from evidence that directly supports the exact proposition.
4. Check source independence, jurisdiction/date boundaries, and whether corroborating Sources actually provide independent evidence rather than repeating one underlying authority.
5. Review all 64 Relations semantically and audit cross-domain coverage/consistency.
6. Run Human View and adversarial review, including misclassification of editorial/methodological rules as `documented_fact`.
7. Obtain an explicit correction plan before editing substantive Claim/Evidence Use/Source/Relation JSON; then run regression checks for every authorized correction.
8. Perform an independent recheck and run all three required CI checks on one exact final HEAD; verify branch tree, PR #21 state/head/base and unchanged `main`.

## No changes to protected content
This stage changed audit reports only. No Claim, Evidence Use, Source or Relation JSON was modified. PR #21 remains intended to stay open as Draft; `main` remains protected and must not be changed.

**Conclusion:** this stage has materially advanced the ledger, identity reconciliation, Batch 41 structural linkage, and Relation graph structural checks. It has **not** completed the M13 audit and does not authorize merging PR #21.
