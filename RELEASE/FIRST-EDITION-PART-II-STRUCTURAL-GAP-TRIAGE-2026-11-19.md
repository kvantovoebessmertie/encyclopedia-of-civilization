# First Edition — Part II Structural Gap Triage

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `724a547ba5c9f5fe58b38b61b9095acfccc797ec`  
Status: **SCOPE TRIAGE ONLY — NO NEW RECORD ADJUDICATION**

## 1. Purpose

Identify the unrepresented slices that are explicitly named by the controlling first-edition domain map, without launching a blanket audit of the remaining corpus. This is a bounded scope triage artifact, not an approval, substantive audit, or change to any canonical record.

## 2. Reconciliation method

Compared:
- `RELEASE/FIRST-EDITION-OPENING-SURVIVAL-AND-DOMAIN-MAP-2026-11-18.md` — Part II structural examples;
- `RELEASE/FIRST-EDITION-PART-I-SURVIVAL-FULL-SLICE-INVENTORY-2026-11-18.md` — completed Part I inventory;
- `RELEASE/FIRST-EDITION-PART-II-EXACT-VERSION-MASTER-REGISTER-2026-11-19.md` — current Part II candidate set;
- canonical repository tree at the inspection HEAD — JSON record-file counts.

The domain map explicitly says its examples are non-exhaustive. Therefore this comparison identifies obvious map gaps; it does not establish that every unlisted slice belongs in the first edition.

## 3. Structural-map coverage

| Measure | Count |
|---|---:|
| Part II structural examples in controlling map | 69 |
| Already represented in Part II candidate register | 37 |
| Also present in completed Part I inventory (reuse; do not repeat) | 7 |
| Not represented in either first-edition candidate register | 25 |
| Canonical JSON records in those 25 slices | 235 |
| Wider Part II slices still unregistered overall | 286 |
| Of those 286, not explicitly named in current map examples | 261 |

The 7 Part I overlaps are:
`energy-basics`, `electricity-basics`, `microbiology-basics`, `geology-basics`, `civil-engineering-basics`, `anatomy-basics`, and `physiology-basics`.

These are not new Part II audit tasks. Their Part I screening evidence remains the controlling prior work; cross-reference them in navigation rather than repeat their audits or duplicate their records.

## 4. Initial structural-map gaps and prior-audit reuse

The 25 rows below were initially absent from the Part I and Part II candidate registers. Eighteen already had substantive prior screens and are now reused rather than repeated; two received a new bounded first-edition screen; five remain unreviewed. The count is the number of canonical JSON files currently in each slice's `records/` directory; it is not a count of Claims or a readiness score.

| Domain family | Slice | Canonical JSON records | Status |
|---|---|---:|---|
| Mathematics and measurement | `ratios-and-percentages` | 10 | Prior M1/M2 HOLD — reused |
| Mathematics and measurement | `probability-basics` | 10 | Prior M1/M2 HOLD — reused |
| Mathematics and measurement | `algebra-basics` | 11 | Prior M1/M2 HOLD — reused |
| Physical sciences | `matter-basics` | 9 | New first-edition screen HOLD |
| Chemical sciences | `acid-base-basics` | 11 | Prior M2 HOLD — current EU v2 reconciled |
| Chemical sciences | `analytical-chemistry-basics` | 11 | Prior M2 HOLD — reused |
| Earth, climate and space | `earth-system-basics` | 9 | New first-edition screen HOLD |
| Earth, climate and space | `oceanography-basics` | 9 | Prior domain HOLD — reused |
| Earth, climate and space | `astronomy-observation-basics` | 9 | Prior domain HOLD — reused |
| Engineering and computing | `cybersecurity-basics` | 9 | Prior engineering audit HOLD — reused |
| Human sciences | `psychology-basics` | 9 | Prior human-sciences audit HOLD — reused |
| Human sciences | `neuroscience-basics` | 9 | Prior human-sciences audit HOLD — reused |
| Human sciences | `learning-basics` | 9 | Prior domain-expansion audit — reused |
| Human sciences | `developmental-biology-basics` | 9 | Prior human-sciences audit HOLD — reused |
| Society and institutions | `economics-basics` | 9 | Prior M1 audit — reused |
| History and culture | `chronology-methods` | 9 | Prior domain-expansion audit — reused |
| History and culture | `archaeology-basics` | 9 | Prior domain-expansion audit — reused |
| History and culture | `ancient-civilizations-basics` | 11 | UNSCREENED — scope triage only |
| History and culture | `writing-systems` | 9 | Prior domain-expansion audit — reused |
| History and culture | `trade-networks` | 9 | Prior domain-expansion audit — reused |
| History and culture | `state-formation` | 9 | Prior domain-expansion audit — reused |
| History and culture | `anthropology-basics` | 9 | UNSCREENED — scope triage only |
| History and culture | `linguistics-basics` | 9 | UNSCREENED — scope triage only |
| History and culture | `philosophy-basics` | 9 | UNSCREENED — scope triage only |
| History and culture | `ethics-basics` | 9 | UNSCREENED — scope triage only |

| **Total** | **25 slices** | **235** | **No decision assigned** |

## 5. Bounded screening sequence — recommendation, not approval

To preserve meaningful encyclopedia breadth without auditing all 286 unregistered slices, screen only the 25 explicit structural-map gaps, in three coherent batches:

1. **Foundations and natural sciences — 9 slices / 89 records:** ratios-and-percentages, probability-basics, algebra-basics, matter-basics, acid-base-basics, analytical-chemistry-basics, earth-system-basics, oceanography-basics, astronomy-observation-basics.
2. **Human, social, engineering and computing foundations — 6 slices / 54 records:** cybersecurity-basics, psychology-basics, neuroscience-basics, learning-basics, developmental-biology-basics, economics-basics.
3. **History and culture — 10 slices / 92 records:** chronology-methods, archaeology-basics, ancient-civilizations-basics, writing-systems, trade-networks, state-formation, anthropology-basics, linguistics-basics, philosophy-basics, ethics-basics.

The order is a proposed work sequence based on the controlling map's domain architecture. It does not create INCLUDE/HOLD/EXCLUDE decisions and does not override owner/editorial scope approval.

## 6. Cross-slice relation observation

The separate 63-record Relation inventory contains no participant endpoint in these 25 unrepresented slices. This means the current Relation set does not yet supply an explicit bridge for these map gaps. Do not create Relations merely to fill the gap; only add a relation when canonical records support a genuine connection.

## 7. Controls preserved

- No M13 batch started and no closed Part I audit repeated.
- No canonical Claim, Evidence Use, Source, Context, Scope or Relation changed.
- No record in the 25 slices promoted to INCLUDE, HOLD or EXCLUDE; they remain unadjudicated scope candidates.
- No rights clearance, editorial approval, Human View, allowlist, preview or publication action was inferred.
- `main` remains untouched.

## 8. Next bounded action

Begin batch 1 only after checking the current canonical record graph and any existing domain-level work for those nine slices. Reuse prior source and rights findings wherever they exist; do not infer readiness from record counts, publication status, or CI.

## 9. Post-Batch 1 and prior-audit reconciliation

Current reconciliation HEAD: `82a511547a92da9196c30b6231054511f2623420`.

- The initial 25 unrepresented structural-map examples / 235 records have been split into completed and remaining work.
- Batch 1 reconciled 9 slices / 89 records: 7 slices / 71 records reuse prior M1/M2/domain screens; only matter-basics and earth-system-basics (2 slices / 18 records) were newly screened. All nine retain HOLD; no canonical JSON was modified.
- Eleven additional prior-screen slices / 99 records were then reconciled at current canonical versions and added to the master without repeating their substantive audits.
- Across the 25 initial structural-map gaps: 18 prior-screened slices / 170 records are reused, 2 new slices / 18 records are screened, and 5 slices / 47 records remain unreviewed.
- The 7 Part I overlaps remain covered by the completed Part I inventory and must be reused, not re-audited.
- The other 261 unregistered slices are not explicitly named in the controlling map examples and remain outside the bounded screen.
- Total Part II coverage is now 119/385 slices, with 266 still unregistered; the master contains 1009 candidate keys plus 12 additional dependency records (1021 exact-version rows).
- Next bounded screen: ancient-civilizations-basics, anthropology-basics, linguistics-basics, philosophy-basics and ethics-basics (5 slices / 47 records). This is a screening queue, not an approval or allowlist.

All Batch 1 decisions remain HOLD. No INCLUDE/EXCLUDE decision, rights clearance, Human View approval or publication permission is inferred.
