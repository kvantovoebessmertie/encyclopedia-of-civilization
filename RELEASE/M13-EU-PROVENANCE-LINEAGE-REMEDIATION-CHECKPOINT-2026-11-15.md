# M13 — Evidence Use provenance-lineage correction checkpoint

Date: 2026-11-15
Branch: m13-system-wide-depth-audit-2026-10-09
Authorization: M13-EU-PROVENANCE-LINEAGE-001
Authorization document: RELEASE/M13-CORRECTION-AUTHORIZATION-EU-PROVENANCE-LINEAGE-PACKAGES-30-31-2026-11-15.md
Registry entry: RELEASE/EDITORIAL-CORRECTION.json

## 1. Result

Four exact Evidence Use provenance defects identified in Packages 30 and 31 were corrected under a dedicated bounded authorization.

| Evidence Use | Old created_from | New created_from | Version |
|---|---|---|---|
| EU-INTERNATIONAL_TRADE_BASICS-B | CLM-INTERNATIONAL_TRADE_BASICS-B@1 | SRC-INTERNATIONAL_TRADE_BASICS@1 | 1 → 2 |
| EU-LABOR_LAW_BASICS-B | CLM-LABOR_LAW_BASICS-B@1 | SRC-LABOR_LAW_BASICS@1 | 1 → 2 |
| EU-RISK_MANAGEMENT_BASICS-B | CLM-RISK_MANAGEMENT_BASICS-B@1 | SRC-RISK_MANAGEMENT_BASICS@1 | 1 → 2 |
| EU-RISK_MANAGEMENT_BASICS-C | CLM-RISK_MANAGEMENT_BASICS-C@1 | SRC-RISK_MANAGEMENT_BASICS@1 | 1 → 2 |

The correction changed only record_version and provenance.created_from[0].record_id in each of the four records. created_from version remains 1.

## 2. Explicit exclusions and preservation

- Claim records remain version 1 and unchanged.
- Source records remain version 1 and unchanged.
- content.claim_ref, content.source_ref, evidence_role and material.description are preserved.
- provenance.method is preserved.
- EU-RISK_MANAGEMENT_COSO remains version 1 and unchanged, with created_from pointing to SRC-COSO-ERM-RISK-MANAGEMENT@1.
- No D/E/B value changed.
- No rights status changed. ISO 31000 remains RIGHTS HOLD and was not used as evidence; this was metadata-lineage correction only.
- No Claim was promoted, no publication status changed, and no Human View or release approval was granted.

## 3. Regression

Added test: test_m13_authorized_evidence_use_provenance_lineage_corrections in REFERENCE/tests/test_m13_evidence_linkage_audit.py.

The regression asserts all four version-2 EU records, exact Source@1 provenance lineage, unchanged Claim@1 and Source@1 content references, and unchanged separate COSO Evidence Use.

## 4. Commit history

- 8fac92a2d951a29f721e0e02d394f1e199c4246d — Package 28 bounded remediation proposal.
- 9634beba16a80d5d7cc43044a8bf07ea029c5c68 — Packages 29–31 remediation routing.
- 4f4372d1eb50f5945d1c84db2462b116a9dc722b — Package 31 arithmetic erratum.
- d91db0bb2cc1cd62cff24d6ac0f7f926eec98888 — exact four-record provenance authorization.
- ad9555dd8eb0d4207931b0dbbb3506b787956b56 — editorial-correction registry authorization entry.
- 4105e8142a0e3ca94fc0c1169a20fa1ce9394400 — International Trade EU correction.
- 7a684cb3a84e56f5371a6df5c98a8f866660da2f — Labor Law EU correction.
- beac251a5f879686c07197a0a1ae6d5e03e3d49c — Risk Management B EU correction.
- d1b6feec58a820b72786fea7ff91bc3df5d22305 — Risk Management C EU correction.
- 252ec94c526542fbc0ae88fd8ecb8992ddfe8c12 — dedicated regression.

## 5. Validation status at checkpoint creation

The latest branch HEAD is 252ec94c526542fbc0ae88fd8ecb8992ddfe8c12. Its automatically triggered build-and-test check was queued at the last poll; it is not yet a pass. Exact-head Reference Tests, Release Conformance Gate and Offline Edition success are still required after the authorized correction.

## 6. Disposition

Four authorized metadata corrections and one dedicated regression have been committed. The changes do not resolve the substantive partial-support findings in Packages 29–31 and do not close the 359-row remediation cohort, rights review, specialist review, Human View, M13 or release readiness.

M13 remains OPEN / NOT RELEASE-READY. PR #21 remains Draft and unmerged. main remains unchanged.
