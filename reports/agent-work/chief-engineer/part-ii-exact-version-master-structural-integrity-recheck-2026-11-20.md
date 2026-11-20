# Part II Exact-Version Master Register — Structural Integrity Recheck

Date: 2026-11-20  
Inspection PR HEAD: `9a933f272f2124a7748ab0d184de465e84bddee4`  
Register: `RELEASE/FIRST-EDITION-PART-II-EXACT-VERSION-MASTER-REGISTER-2026-11-19.md`  
Status: **1,130/1,130 TABLE KEYS UNIQUE; 1,130/1,130 HOLD; STRUCTURAL REGISTER CHECK ONLY**

## 1. Method and scope

Parsed every record row in the consolidated Part II exact-version master table using the compound identity `record_id@record_version`. Counted row identities, duplicates, record types, slice labels, and decision values.

This is a Markdown-register integrity check. It does not re-fetch and certify all 1,130 canonical JSON files, complete Claim → Evidence Use → Source dependency closure, or establish substantive eligibility. The master itself retains mixed historical verification labels and pinned inspection snapshots; those labels are not silently upgraded by this count.

## 2. Reconciled table counts

| Measure | Rechecked result |
|---|---:|
| Exact-version rows | 1,130 |
| Unique compound `record_id@version` keys | 1,130 |
| Duplicate compound keys | 0 |
| Distinct Part II slices represented | 124 |
| Candidate keys | 1,058 |
| Dependency records | 72 |
| Decisions marked HOLD | 1,130 |
| Decisions marked INCLUDE | 0 |
| Decisions marked EXCLUDE | 0 |

Record-type distribution:

| Record type | Rows |
|---|---:|
| Claim | 352 |
| Evidence Use | 400 |
| Source | 163 |
| Context | 107 |
| Scope | 108 |
| **Total** | **1,130** |

The type totals reconcile exactly to the table row count. The 1,058 candidate keys and 72 dependency records reconcile to the documented total of 1,130.

## 3. Scope boundaries retained

- Part II coverage remains 124/385 slices.
- The other 261 Part II slices are not automatically candidates; they remain outside the bounded map scope unless explicitly authorized.
- The separately identified 30 current Claim records across 14 slices remain outside the 1,058-key candidate denominator pending scope triage. This is the known set from previously reviewed slices, not an exhaustive repository-wide count.
- Relations remain tracked outside the vertical-slice candidate denominator.
- Part I remains a separate inventory: 94/94 slices and 980/980 records screened, all HOLD.

## 4. Verification-label distribution

The table retains distinct historical and current verification labels, including snapshot, current-head identity verification, stale historical version, substantive re-review, prior-screen reuse and dependency verification. The recheck does not flatten those categories into one claim of canonical verification.

In particular:
- a unique table key is not proof that the canonical file exists or that all references resolve;
- `canonical_json_verified_current_head_hold` is an identity/version check, not substantive review;
- historical v1 rows remain historical when a later version exists;
- dependency rows do not expand the candidate denominator;
- all records remain HOLD irrespective of the verification label.

## 5. Next exact closure work

1. Continue targeted canonical dependency verification for proposed first-edition records, beginning with exact Claim → Evidence Use → Source links and Context/Scope applicability.
2. Reconcile historical/stale verification labels only when the relevant canonical record and dependency chain are actually re-fetched at a frozen HEAD.
3. Keep candidate membership fixed; do not add the 30 known out-of-master Claims or 261 map-external slices without scope authorization.
4. Build no public allowlist until all exact record-level, rights, editorial, safety and release gates close.

## 6. Change-control statement

- No canonical JSON or repository source code was changed.
- No register row, candidate denominator, slice denominator or dependency count was changed.
- No HOLD was promoted or reclassified.
- No allowlist, publication, deployment, merge or main-branch change was made.

**Acceptance:** accept as a structural integrity recheck of the Part II Markdown master table only. It is not canonical corpus certification or release approval.
