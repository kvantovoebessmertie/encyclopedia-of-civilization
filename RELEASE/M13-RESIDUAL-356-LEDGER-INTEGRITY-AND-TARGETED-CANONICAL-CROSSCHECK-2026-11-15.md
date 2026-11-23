# M13 — residual 356 ledger integrity and targeted canonical cross-check

Date: 2026-11-15  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed HEAD: `2f7df2f3a966bed1bebe3eda662e356435ac7627`  
State: **proposal-only audit; no canonical writes; no D/E/B changes.**

## 1. Ledger structural validation

The local companion ledger `M13-residual-356-generic-EU-remediation-ledger-current-2026-11-15.csv` was parsed independently.

| Control | Result |
|---|---:|
| Rows | 356 |
| Unique Claim IDs | 356 |
| Unique Evidence Use IDs | 356 |
| Unique canonical paths | 356 |
| Duplicate Claim/EU/path rows | 0 |
| Missing Claim IDs, EU IDs, paths, Source IDs | 0 |
| Rows with multiple Source IDs | 0 |
| Source version snapshot | v1 for 356/356 |
| Human confirmation required | 356/356 |
| Canonical write authorized | 0/356 |
| D/E/B score fields populated | 0/356 |
| Slices represented | 135 |
| Rows with source-review report filename mentions | 356/356 |

Report filename mentions are routing hints only. They do not establish exact report-body coverage, passage support, rights clearance, or acceptance.

## 2. Reuse of strict locator work

The ledger identifies 14 rows already handled in strict locator Packages 03, 05 and 06:
- Package 03: 7 rows
- Package 05: 1 row
- Package 06: 6 rows

These 14 were fetched directly from the reviewed branch HEAD and parsed. All 14 match the ledger's exact path, EU record ID, record version, Claim ID/version, and Source ID/version. Their blob SHAs are:

| Evidence Use | Blob SHA |
|---|---|
| EU-ALGEBRA_BASICS-A | 9c653cb07e12014c6d687e21c16c657b72637e59 |
| EU-ALGEBRA_BASICS-B | 4bc5a56d47fd95321546feff6f9593b2446d597e |
| EU-ALGEBRA_BASICS-C | a3c2c53f651a2ec5d889b7d02d06074c78460ae7 |
| EU-ANATOMY_BASICS-B | 74f46a719dd025fb91d29b36e381eb70b4df8fc9 |
| EU-ARCHIVAL_SCIENCE-A | 0bfcd9965255f401cbea81d2b9c61b059a720bcf |
| EU-ARCHIVAL_SCIENCE-B | 49ced0957b41f42162c698a8ba290fdc1ca1864d |
| EU-ARCHIVAL_SCIENCE-C | cc88de88fb3458f979b0650a77337d721d4e084b |
| EU-BEHAVIORAL_ECONOMICS_BASICS-B | 6989b2ed6eb1cbfe81ee4717631ba9c693fac5a8 |
| EU-BEHAVIORAL_ECONOMICS_BASICS-C | acfea35abfe1bf5412cffde010294ba8979e39ef |
| EU-BIODIVERSITY_BASICS-A | fe463a973c3a22f0d595379d61d3b519c0e4ba05 |
| EU-BIODIVERSITY_BASICS-B | ac111c28d2f44975fae8a3e87952c53f826beec9 |
| EU-CALIBRATION_BASICS-B | 1d99009f5a68191937872aa90359ad7665f4737c |
| EU-CALIBRATION_BASICS-C | 227ae9bca933eee884cd340e82f503dc2dc4ec66 |
| EU-CELL_BASICS-C | ef2e4cd3f1655932998059fa59b2bcd943868c19 |

The remaining 342 rows have not yet received this fresh per-file cross-check in this pass. No 356/356 current canonical integrity claim is made.

## 3. Additional routing observations

- 14 rows reuse strict locator packages; do not repeat their source-passage searches unless a relevant version/source/report conflict is found.
- 330 rows have no machine triage flag; 15 carry a very-short-Claim review flag; 11 carry an actionable/prescriptive-Claim review flag. These are routing signals, not D/E/B assessments.
- All 356 D/E/B fields remain blank in this ledger. No automatic score assignment is permitted.
- Source-review report mentions range from one to three filenames per row; each report body still needs exact Claim/EU/Source and version matching before its findings are imported.

## 4. Next bounded work

1. Fresh-fetch the remaining 342 canonical EU JSON files and compare record ID/version, Claim ref ID/version, and Source ref ID/version to the ledger.
2. For rows with prior review mentions, resolve exact report-body evidence and import support/rights/scope/identity findings without repeating searches.
3. Prepare separate proposal queues for locator gaps, source identity/URI corrections, new Sources/EUs, partial support/Claim narrowing, rights restrictions, and specialist/Human View review.
4. Preserve HOLD and `canonical_write_permitted = NO` until a specific bounded authorization is recorded.

## 5. Protected state

No Claim/EU/Source/Context/Scope/Relation JSON was modified. No D/E/B values were assigned. No rights, specialist, Human View, release, or publication gate was cleared. PR #21 remains Draft/unmerged; `main` remains unchanged.

**Disposition:** ledger structure passes; targeted strict-cohort canonical cross-check passes 14/14; full current canonical cross-check remains OPEN (342 rows).
