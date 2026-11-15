# M13 — final audit checkpoint for the 359-Claim remediation cohort

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Validation head before this checkpoint: `00eb4ff97c0bb78806e22bd010c93c705f8364dc`

## 1. Audit result

The residual 359-row Generic Evidence Use cohort has completed:
- report-body coverage and exact Claim-ID joins;
- row-level consolidation of source-passage findings, support disposition, rights status, source-identity/source-chain notes and next actions;
- current-branch EU version and Claim/Source reference validation;
- protected-state checks confirming no canonical writes and no official D/E/B changes.

This is a **completed audit checkpoint for coverage and structural linkage**, not a completed remediation or release gate. All 359 Claims remain **HOLD**.

## 2. Coverage and current canonical linkage

| Control | Result |
|---|---:|
| Unique Claims in cohort | 359 |
| Claims with exact report-body coverage | 359/359 |
| Claims with one report reference | 356 |
| Claims with two distinct report references | 3 |
| Current EU record version v1 | 359/359 |
| Exact Claim v1 and Source v1 references | 359/359 |
| EU JSONs freshly fetched at current branch head | 44 |
| Earlier exact checks carried forward after docs-only branch diff | 315 |
| Canonical Claim/EU/Source/Context/Scope/Relation writes in this pass | 0 |

The 44 fresh checks parsed the current branch EU JSONs and compared `record_version`, `content.claim_ref.record_id/version` and `content.source_ref.record_id/version` to the master ledger. The other 315 had exact EU/Claim/Source checks in earlier imports. A compare from `967da40d66650b1d535744ac676be28519ebc57c` to `00eb4ff97c0bb78806e22bd010c93c705f8364dc` showed only added RELEASE Markdown artifacts; no canonical JSON changed after those checks.

## 3. Support disposition

| Disposition | Claims |
|---|---:|
| DIRECT_WITH_PINPOINT_GAP | 159 |
| PARTIAL | 84 |
| NOT_ESTABLISHED_BY_CURRENT_SOURCE | 66 |
| DIRECT | 26 |
| DIRECT_WITH_SCOPE_LIMIT | 15 |
| DIRECT_WITH_RIGHTS_HOLD | 3 |
| DIRECT_WITH_SOURCE_IDENTITY_AND_RIGHTS_HOLD | 2 |
| PARTIAL_WITH_RIGHTS_HOLD | 2 |
| PARTIAL_WITH_SOURCE_IDENTITY_AND_RIGHTS_HOLD | 1 |
| DIRECT_WITH_SCOPE_GAP | 1 |
| **Total** | **359** |

A direct-fit finding is not acceptance. Locator gaps, rights restrictions, scope limits and specialist review remain independent gates.

## 4. Defect-screening profile

The row-level register records:
- 332 Claims with a pinpoint/locator issue mentioned;
- 103 with a new/distinct Source or EU registration action mentioned;
- 68 with scope, jurisdiction or Claim-boundary issues mentioned;
- 67 with specialist, independent or Human View review mentioned;
- 35 with explicit rights/attribution/permission notes;
- 30 with explicit source-identity, URI, source-chain or source-scope caveats.

These are non-exclusive report-text screening flags. They are routing counts, not separate expert adjudications.

Rights control:
- 324 rows have no rights issue reported in the imported report bodies. That does **not** mean rights are cleared.
- 35 rows have explicit rights or attribution review notes. OpenStax AI-ingestion restrictions, ISO restrictions, DACS rights uncertainty and source-specific attribution/media-use conditions must be resolved before relevant reuse.

Source identity control:
- 30 rows have a recorded source identity/source-chain caveat.
- 329 rows have no specific identity defect recorded in the reports. Independence is not assessed merely because no identity defect was reported.

## 5. Protected state

- All 359 Claims remain **HOLD**.
- `canonical_write_permitted = NO` for all 359.
- No canonical Claim/EU/Source/Context/Scope/Relation JSON changed.
- No official D/E/B score was overwritten.
- Rights status, source identity, support disposition and next actions are kept separate.
- PR #21 remains open, Draft and unmerged. PR #22 remains open, Draft and unmerged.
- No merge was performed.

## 6. CI state and release gate

At the last status poll for validation head `00eb4ff97c0bb78806e22bd010c93c705f8364dc`:
- Offline Edition: **in progress**.
- Reference implementation tests: **pending**.
- Release Conformance Gate: **in progress**.
- Combined commit status: no status entries returned.

On the preceding head `098ee29b5db089e818dfc002547b917fa07e2833`, Offline Edition succeeded, Reference Tests were still in progress, and Release Conformance Gate was cancelled. This is not a full CI pass. The latest three required workflows must each report explicit `success` before the M13 branch is treated as CI-verified.

## 7. Next gate — bounded remediation proposals

The next work is not a broad canonical rewrite. It is to prepare bounded, reviewable proposals in separate queues:
1. exact EU locator additions for direct-fit Claims;
2. Source identity/URI corrections with version-history preservation;
3. new Source/EU records for supplementary authorities;
4. partial-support Claim narrowing or additional-source proposals;
5. rights and permissions decisions;
6. no-support/source-replacement and expert-decision cases;
7. specialist and Human View routing.

Do not write canonical JSON until a specific bounded change is explicitly authorized. After each authorized batch, run the local reference/schema/regression checks; run consolidated full CI after the authorized remediation set. Do not merge PR #21 until all required workflows succeed and the remaining release gates are satisfied.

## 8. Artifacts

- Import 21 — final 26 residual Claims: `RELEASE/M13-MASTER-REMEDIATION-REPORT-BODY-IMPORT-21-FINAL-26-RESIDUAL-CLAIMS-2026-11-15.md`
- Consolidated defect register: `RELEASE/M13-MASTER-REMEDIATION-CONSOLIDATED-DEFECT-REGISTER-359-2026-11-15.md`
- Downloadable row-level ledger: `m13-master-remediation-ledger-consolidated-v25.csv`

**Final audit checkpoint:** report-body coverage and EU link integrity are complete for the 359-Claim cohort. Remediation, rights clearance, specialist review, CI verification, M13 closure and publication approval remain open.
