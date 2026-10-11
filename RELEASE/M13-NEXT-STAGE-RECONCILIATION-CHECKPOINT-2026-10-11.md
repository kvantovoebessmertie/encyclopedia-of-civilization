# M13 Next-Stage Reconciliation Checkpoint — 2026-10-11

Branch: `m13-system-wide-depth-audit-2026-10-09`
Status: **major reconciliation work in progress; M13 remains OPEN**.
Protected state: PR #21 must remain open as Draft and unmerged; `main` must not change.

## Work completed in this stage

### 1. Consolidated Claim scoring ledger
- Combined scored rows from Batch 12, general review batches 17–40, and Batch 41 scored blocks 1–6.
- **259 report rows** are represented with Claim ID, inventory path, internal `record_id`, duplicate/alias status, D/E/B scores, and rationale/disposition.
- The full inventory join now lists **all 1,494 Claim-prefixed JSON paths** and joins every scored path: 252 unique normalized scored IDs, zero unmatched scored paths, and **1,242 inventory Claims not yet represented by a scored row**.
- Seven repeated-ID paths remain explicit (three nuclear rows repeated in batches 12/17 and four water-treatment/emergency-disinfection rows repeated in batches 21/27); score conflicts are not silently overwritten.
- The join is a review index, not a final acceptance register. Semantic duplicates and eligibility still require review.

Inventory join: [Full Claim inventory-to-ledger join](M13-CLAIM-INVENTORY-TO-LEDGER-JOIN-2026-10-11.md).

Ledger: [M13 consolidated Claim audit ledger](M13-CONSOLIDATED-CLAIM-AUDIT-LEDGER-WORKING-2026-10-11.md)

### 2. Duplicate and score-conflict reconciliation
Seven repeated-ID groups were confirmed:
- Three nuclear-physics Claims appear in Batch 12 and Batch 17.
- Four water-treatment/emergency-disinfection Claims appear in Batch 21 and Batch 27.

The three nuclear Claims and three water-treatment Claims had conflicting scores across historical reports. Canonical audit scores are now explicitly adjudicated in [Duplicate score adjudication](M13-DUPLICATE-SCORE-ADJUDICATION-2026-10-11.md); every historical score/rationale remains visible in the detailed ledger. The water emergency-disinfection duplicate has identical scores in both reports. Independent review and semantic-duplicate review remain open. Batch 41 has no exact or separator-insensitive ID overlap in the inspected prior reports, but semantic duplicates remain an open gate.

### 3. Batch 41 Claim → Evidence Use → Source structural linkage
- **100/100 primary Batch 41 links** were opened and checked.
- Claim record type, Claim `record_id`, EU `claim_ref`, EU `source_ref` versus Claim provenance, `supports` role, and Source record existence passed the structural check under exact/comparison-only separator matching.
- An additional **15 Evidence Use records** were found in the 33 candidate slices and individually inspected. They point to Batch 41 Claims, use `supports`, and resolve their Source records.
- Across primary and additional evidence links, **44 unique Source records** were inspected for metadata identity/URI consistency.
- A separate post-score reconciliation classifies **49/100 primary EU descriptions as generic** and **52/100 rows as having locator-specificity gaps**; these categories overlap. The linkage table preserves the actual description text, but a description—generic or otherwise—is not proof of pinpoint evidence support. See [Batch 41 post-score reconciliation](M13-BATCH-41-POST-SCORE-RECONCILIATION-2026-10-11.md).
- One confirmed Source identity/URI mismatch remains: `SRC-ASSET_MANAGEMENT_BASICS` labels ISO 55000:2024 while its URI points to ISO 55001:2024. No content record was changed.
- Fifteen additional EU records refer to 11 distinct Source IDs beyond the primary sources. URI-host comparison indicates 14/15 are on a different publisher domain than the primary source; the agricultural-engineering corroboration and primary source both use FAO, so that pair is not publisher-independent. Different domains still do not prove claim-specific fit or independence of the underlying evidence.

Linkage report: [Batch 41 linkage reconciliation](M13-BATCH-41-LINKAGE-RECONCILIATION-2026-10-11.md)

### 4. Relation graph structural and initial semantic audit
- All **64 Relation JSON records** passed structural checks: 0 missing participant/frame/provenance Source pointers and 0 role-cardinality errors.
- Initial participant-statement review is complete for all 64: **32 strong/direct fits, 14 moderate/broad fits, 11 good thematic fits, and 7 weak/weak-to-moderate links**.
- Weak links requiring bridging Claims, narrower rationale or removal review are listed in the Relation report; near-duplicate Claim content and one state-relation type/direction issue are also flagged.
- Independent review, source independence, and authorized relation edits remain open.

Relation report: [M13 Relation graph audit](M13-RELATION-GRAPH-AUDIT-2026-10-11.md).

Relation report: [M13 Relation graph audit](M13-RELATION-GRAPH-AUDIT-2026-10-11.md)

### 5. Score-ledger generator coverage repaired

- The automated score-ledger generator was found to omit Batch 12 heading-form scores and six Batch 41 scored-block reports/alias-annotated rows. The generator now reads those formats and a regression guard pins the expected coverage.
- Corrected generated artifact: **259 rows / 252 normalized Claim IDs / 7 repeated-ID groups / 0 unmatched scored rows**, including **100 Batch 41 rows** and the three Batch 12 scores.
- The full-corpus Evidence Use triage scanned 4,831 records, including 1,669 Evidence Use records. It reported **529 generic material descriptions**, **493 separator-only filename/internal-ID aliases**, and **6 other filename/internal-ID mismatches**. It found no unresolved Claim/Source IDs, wrong target record types, invalid evidence roles, or explicit Claim/Source reference-version mismatches in that run. Generic descriptions remain a source-fit/traceability queue, not automatic proof of false claims.
- This is an audit-tooling correction and structural triage, not substantive acceptance of the scores. The final unit-test result and all three workflows still must pass on one exact final HEAD.

Score-ledger coverage addendum: [M13 score-ledger generator correction](M13-SCORED-LEDGER-GENERATOR-COVERAGE-ADDENDUM-2026-10-11.md).

### 6. Initial semantic-duplicate triage

- Normalized comparison of the 1,494-Claim worksheet found **2 exact duplicate statement groups covering 18 Claims** and **3 templated families covering 60 additional cross-slice Claims** (slice-purpose, source/context, specialist-checking statements).
- The candidates are stored as `documented_fact` and linked to subject-matter sources; this suggests type/placement and evidence-fit issues, but no Claim should be silently deleted or deduplicated. Each group needs an explicit disposition.
- These are initial candidate groups only; the full semantic duplicate/exclusion gate remains open.

Duplicate triage: [M13 initial Claim semantic-duplicate triage](M13-CLAIM-SEMANTIC-DUPLICATE-TRIAGE-INITIAL-2026-10-11.md).

### 7. First 30 unscored Claims — source-fit pass

- Thirty Claims selected from the unscored inventory were inspected at Claim/Evidence Use/Source level without assigning D/E/B.
- The pass found three climate-science Claims that are editorial/methodological rather than domain facts, a confirmed UNESCO Source identity/scope mismatch for comparative-civilizations Claims, and a Source identity quality defect in the combinatorics Source. Many otherwise plausible claims still have generic EUs.
- These 30 remain unscored and inside the fixed 1,494-Claim denominator; the pass does not reduce the 1,242 Claims without scored rows.

Unscored triage: [M13 unscored Claim source-fit batch 01](M13-UNSCORED-CLAIM-SOURCE-FIT-TRIAGE-BATCH-01-2026-10-11.md).

### 8. Low evidence-fit remediation planning
- A separate queue covers the **19 Batch 41 Claims with E=0 or E=1**: 10 E=0 type/placement mismatches and 9 E=1 source-fit gaps.
- It specifies source/narrowing/type decisions for each row, but does not edit content JSON. A correction plan still requires explicit authorization and exact diffs.

Remediation queue: [Batch 41 low evidence-fit remediation queue](M13-BATCH-41-LOW-EVIDENCE-FIT-REMEDIATION-QUEUE-2026-10-11.md).

## Findings that must not be hidden by a green structural result
1. Structurally valid pointers do not demonstrate source passage fit.
2. Generic Evidence Use descriptions remain a substantial traceability weakness.
3. ISO 55000/55001 Source identity mismatch needs an authorized, separately reviewed correction plan; no Source JSON was edited.
4. The Batch 12/17 nuclear score conflicts require explicit adjudication.
5. Report-ID uniqueness does not rule out semantic duplicates.
6. Relation endpoint existence does not prove relation meaning or source independence.

## Remaining M13 gates

1. Complete semantic duplicate/exclusion adjudication over all 1,494 Claims. The structural inventory-to-ledger join is complete; 1,242 Claims remain unscored.
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
