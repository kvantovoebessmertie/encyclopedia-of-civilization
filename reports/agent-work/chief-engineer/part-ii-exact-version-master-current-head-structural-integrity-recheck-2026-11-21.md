# Part II Exact-Version Master — Current-Head Structural Integrity Recheck

Date: 2026-11-21  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Inspection branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `c7f0c45babd5ac58bbffa17f0a263bde7826cda5`  
Register: `RELEASE/FIRST-EDITION-PART-II-EXACT-VERSION-MASTER-REGISTER-2026-11-19.md`  
Status: **1,134/1,134 UNIQUE EXACT-VERSION ROWS; ALL 1,134 HOLD; STRUCTURAL CHECK ONLY**

## 1. Scope and method

Parsed every data row in the current Part II exact-version master table using the compound key `record_id@record_version`. Reconciled candidate/dependency counts, type distribution, decision values, slice labels and verification labels. Re-fetched the recent Groundwater and ILO dependency records and the directly affected Relation/Context/Claim records at the same immutable PR branch HEAD.

This is a structural register and targeted dependency identity/reference check. It is not a full re-fetch of all 1,134 records, a complete dependency-closure audit, substantive review of every Claim, rights clearance, or release approval.

## 2. Master table results

| Measure | Current result |
|---|---:|
| Exact-version data rows | 1,134 |
| Unique compound `record_id@version` keys | 1,134 |
| Duplicate compound keys | 0 |
| Candidate keys | 1,058 |
| Dependency records | 76 |
| Decisions marked HOLD | 1,134 |
| Decisions marked INCLUDE | 0 |
| Decisions marked EXCLUDE | 0 |
| Part II slices represented | 124 / 385 |
| Additional dependency-only slice label | `cross-slice-linkage` |

The table therefore contains 125 distinct slice labels when the cross-slice Relation dependency slice is included. That dependency-only label is not part of the 385-slice Part II denominator; Part II coverage remains 124/385.

Record-type distribution:

| Type | Rows |
|---|---:|
| Claim | 352 |
| Evidence Use | 402 |
| Source | 165 |
| Context | 107 |
| Scope | 108 |
| **Total** | **1,134** |

The candidate/dependency arithmetic reconciles: 1,058 + 76 = 1,134. Type totals also reconcile exactly to 1,134.

## 3. Recent dependency rows and exact canonical checks

The following four dependency rows are present in the current master and their canonical JSON records were re-fetched at inspection HEAD `c7f0c45babd5ac58bbffa17f0a263bde7826cda5`:

- `SRC-GROUNDWATER-SOIL-MICROBIAL-TRANSPORT-2024@1` — Source, `cross-slice-linkage`.
- `SRC-MIGRATION-LABOUR-STATISTICS-ILO-GUIDE@1` — Source, `migration-and-mobility-basics`.
- `EU-MIGRATION_AND_MOBILITY_BASICS-C-ILO-GUIDE@1` — Evidence Use, exact Claim C @2 → ILO Source @1.
- `EU-LABOR_ECONOMICS_BASICS-C-ILO-GUIDE@1` — Evidence Use, exact Claim C @2 → ILO Source @1.

The two ILO endpoint Claims were re-fetched and verified at @2. Their statements were not changed by this check. The migration Evidence Use locator covers the ILO Guide's printed pp. 22–27 and 34–38; the labour Evidence Use covers pp. 30–33, 57–58 and 63–66 and expressly does not claim that the Guide supports labour-productivity comparability.

The Groundwater Relation @4 and Context @3 were re-fetched. Their reciprocal references resolve exactly (Relation @4 → Context @3; Context @3 → Relation @4), both retain the same two participant Claims @1, and both provenance arrays contain the authorized Groundwater Source @1. The relation type, undirected direction and participant order remain unchanged.

## 4. Verification-label interpretation

The master retains its historical/current verification distinctions, including snapshot rows, current-head identity checks, dependency-verified rows, prior-screen reuse, superseded historical versions and stale historical audit rows. In particular, the current parse contains 13 rows labelled `audit_table_stale` and 10 labelled `historical_version_superseded`.

These labels are not automatically defects and must not be flattened into one verification state. They indicate where a historical row is retained for lineage or where a prior audit version is no longer current. This structural pass does not upgrade any row's verification label or claim that every canonical JSON dependency has been re-fetched.

## 5. Disposition and controls

- All 1,134 master rows remain HOLD; no INCLUDE or EXCLUDE was added.
- The candidate denominator remains 1,058.
- Part II coverage remains 124/385; the 261 map-external slices remain outside the bounded map scope.
- The 30 known out-of-master Claims across 14 slices remain outside the candidate denominator pending explicit scope triage.
- Relations remain outside the Part II candidate denominator and are tracked in their separate dependency inventory.
- No canonical record, register row, candidate membership, rights decision, allowlist, publication state or release decision was changed by this report.
- PR #22 remains OPEN / DRAFT / NOT MERGED; `main` is unchanged.

## 6. Next controlled action

Continue WP1 only within the already bounded candidate map. Prioritize targeted exact Claim → Evidence Use → Source and Context/Scope dependency closure where it can materially change an existing HOLD reason. Do not repeat completed substantive screens, add the 261 map-external slices, or treat structural register integrity as eligibility. Any canonical mutation still requires its own exact bounded owner authorization. WP2 rights/owner decisions and WP3 selection-aware publication remain separate gates.
