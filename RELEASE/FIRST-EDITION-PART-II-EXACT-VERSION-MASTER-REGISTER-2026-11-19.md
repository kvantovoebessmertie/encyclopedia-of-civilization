# First Edition — Part II Exact-Version Master Register

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `846cefd71ae320f0aa8d39b93507ac78f2d591bf`  
Status: **CONSOLIDATED CANDIDATE REGISTER — ALL DECISIONS HOLD; CANONICAL DEPENDENCY AUDIT STILL OPEN**

## 1. Purpose and key rules

This register consolidates the ten Part II addenda and the Part II candidate references in the base record-level register. The deduplication key is the compound `record_id@record_version`.

- Same `record_id` at different versions is version lineage, not a duplicate.
- Relations are excluded from vertical-slice record counts and must be tracked in a separate relation-dependency ledger.
- No record is promoted to INCLUDE or EXCLUDE by this consolidation.
- `canonical_json_snapshot`: the six newly expanded addenda were fetched and parsed from canonical JSON at their pinned inspection HEADs.
- `canonical_json_verified_snapshot`: detailed audit-table rows were re-read and matched to canonical JSON at their pinned verification HEADs.
- `canonical_json_verified_current_head_hold`: exact record ID, version and type were re-read from canonical JSON at the master inspection HEAD; this is an identity/version check, not a substantive decision.
- `audit_table_stale`: historical v1 audit rows whose current canonical record is v2; retain as history, not as the current reviewed version.
- `canonical_json_substantively_rereviewed_hold`: current canonical v2 records have been re-fetched and received a bounded substantive dependency review; remaining remediation/rights/editorial gates are explicitly recorded and the disposition remains HOLD.
- `base_register_reference`: the exact ID/version appears in the base candidate register; current canonical version and complete dependency closure still require revalidation.
- The malformed R9 history-of-mathematics Cambridge source ID was normalized to the exact canonical underscore-form ID and deduplicated.

## 2. Reconciliation totals

| Measure | Count |
|---|---:|
| Part II exact-version rows from ten addenda after malformed-ID normalization | 621 |
| Base-register Part II raw exact-version references mapped to 37 slices | 197 |
| Distinct base-register canonical keys after water-quality alias normalization | 196 |
| Exact `record_id@version` matches deduplicated across both sources | 9 |
| Current-version additions discovered by legal drift check | 13
| Additional exact dependency records discovered during chain closure and current-head follow-up | 71 |
| Unique consolidated Part II candidate keys before Batch 1 | 821 |
| Batch 1 screened structural-gap exact-version rows | 89 |
| Unique consolidated Part II candidate keys, including Batch 1 | 910 |
| Prior-screen slices reconciled and added after Batch 1 | 11 |
| Exact-version rows reused from prior audits | 99 |
| Unique consolidated Part II candidate keys after prior-audit reuse | 1009 |
| Previously omitted relation-candidate Claims restored to the candidate master | 2 |
| Unique Part II candidate keys after relation-endpoint reconciliation | 1011 |
| Batch 2 newly screened exact-version candidate rows | 47 |
| Unique Part II candidate keys after Batch 2 | 1058 |
| Total exact-version rows after current-head dependency reconciliation (1058 candidate keys + 71 dependency records) | 1129 |

**Post-Batch 9 exact-dependency reconciliation:** the exact-version table contained 1,113 rows at PR HEAD `c209b90fbe542eeff08f46e6598ac1666b8dbaaa`. Six additional canonical dependency rows were subsequently reconciled and added: `EU-ANTIMICROBIAL_RESISTANCE_BASICS-C@1`, `EU-STATISTICS_BASICS-C@1`, `CTX-ANTIMICROBIAL_RESISTANCE_BASICS@1`, `SCP-ANTIMICROBIAL_RESISTANCE_BASICS@1`, `CTX-STATISTICS_BASICS@1`, and `SCP-STATISTICS_BASICS@1`. All six were fetched from canonical JSON at HEAD `4283b65031fe5d578aa4f92242b98b14fc392c94` and exact ID/version/type matched. The two EU rows close the dependencies discovered in Batch 9; the four Context/Scope rows are identity/dependency inventory additions only and each targets Claim A v1 in its own slice. No applicability to Claim C is inferred. This reconciles the exact table from 1,113 to **1,119 unique exact-version rows** (1,058 candidate keys + 61 dependency records).
| Part II slice denominator | 385 |
| Unique Part II slices represented before Batch 1 | 99 |
| Additional Part II slices screened in Batch 1 | 9 |
| Unique Part II slices represented after Batch 1 | 108 |
| Additional slices reconciled from prior audits | 11 |
| Unique Part II slices represented after prior-audit reuse | 119 |
| Additional slices newly screened in Batch 2 | 5 |
| Unique Part II slices represented after Batch 2 | 124 |
| Part II slices not yet represented after Batch 2 | 261 |

Slice-level coverage before Batch 1 was 99/385: 37 base-register slices + 64 addendum slices − 2 overlaps (`units-and-measurement`, `food-systems-basics`). Batch 1 adds 9 screened structural-map slices / 89 exact-version records, bringing coverage to 108/385. Reusing 11 already-screened slices / 99 records adds no new audit and brings coverage to 119/385; 266 slices remain unregistered and require scope triage, not automatic audit.

## 3. Exact-version duplicate resolution

- `SRC_WATER_QUALITY_BASICS@1` — the base register contains a duplicated/corrected alias row for the same canonical record; retain one canonical key and preserve the correction note. The canonical JSON record itself was not renamed.
- `SRC-UNITS_AND_MEASUREMENT@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md
- `CLM-UNITS_AND_MEASUREMENT-A@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md
- `CLM-UNITS_AND_MEASUREMENT-B@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md
- `CLM-UNITS_AND_MEASUREMENT-C@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md
- `EU-UNITS_AND_MEASUREMENT-A@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md
- `EU-UNITS_AND_MEASUREMENT-B@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md
- `EU-UNITS_AND_MEASUREMENT-C@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md
- `CTX-UNITS_AND_MEASUREMENT@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md
- `SCP-UNITS_AND_MEASUREMENT@1` — merged source references: FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md

The base register and addenda may refer to the same logical record at different versions. In particular, `food-systems-basics` base-register records are v1 while R9 records are v2; both versions are retained as lineage, not deduplicated. The nine `units-and-measurement` exact keys above are true duplicates and are represented once.

Other logical IDs with multiple versions in the consolidated register:
- `CLM-FOOD_SYSTEMS-A`: versions 1, 2
- `CLM-FOOD_SYSTEMS-B`: versions 1, 2
- `CLM-FOOD_SYSTEMS-C`: versions 1, 2
- `CLM-FOOD_SYSTEMS-D`: versions 1, 2
- `CTX-FOOD_SYSTEMS`: versions 1, 2
- `EU-FOOD_SYSTEMS-A`: versions 1, 2
- `EU-FOOD_SYSTEMS-D`: versions 1, 2
- `SCP-FOOD_SYSTEMS`: versions 1, 2
- `SRC-FOOD_SYSTEMS_WB`: versions 1, 2
- `SRC-FOOD_SYSTEMS`: versions 1, 2
- `CLM-INTERNATIONAL_LAW_BASICS-A`: versions 1, 2
- `CLM-INTERNATIONAL_LAW_BASICS-B`: versions 1, 2
- `CLM-INTERNATIONAL_LAW_BASICS-C`: versions 1, 2
- `CTX-INTERNATIONAL_LAW_BASICS`: versions 1, 2
- `EU-INTERNATIONAL_LAW_BASICS-A`: versions 1, 2
- `EU-INTERNATIONAL_LAW_BASICS-B`: versions 1, 2
- `EU-INTERNATIONAL_LAW_BASICS-C`: versions 1, 2
- `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-A`: versions 1, 2
- `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-B`: versions 1, 2
- `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-C`: versions 1, 2
- `SCP-INTERNATIONAL_LAW_BASICS`: versions 1, 2
- `SRC-INTERNATIONAL_LAW_BASICS-INDEPENDENT`: versions 1, 2
- `SRC-INTERNATIONAL_LAW_BASICS`: versions 1, 2

## 4. Consolidated exact-version rows

| Record/version | Type | Slice | Decision | Version verification | Source register(s) |
|---|---|---|---|---|---|
| `CLM-ACCOUNTING_BASICS-A@1` | claim | `accounting-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ACCOUNTING_BASICS-B@1` | claim | `accounting-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ACCOUNTING_BASICS-C@1` | claim | `accounting-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-ACCOUNTING_BASICS@1` | context | `accounting-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-ANTIMICROBIAL_RESISTANCE_BASICS@1` | context | `antimicrobial-resistance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-STATISTICS_BASICS@1` | context | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-ACCOUNTING_BASICS-A@1` | evidence_use | `accounting-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ACCOUNTING_BASICS-B@1` | evidence_use | `accounting-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ACCOUNTING_BASICS-C@1` | evidence_use | `accounting-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` | evidence_use | `antimicrobial-resistance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CROSS-SLICE-RELATION-DEPENDENCY-INVENTORY-2026-11-19.md |
| `EU-STATISTICS_BASICS-C@1` | evidence_use | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CROSS-SLICE-RELATION-DEPENDENCY-INVENTORY-2026-11-19.md |
| `SCP-ACCOUNTING_BASICS@1` | scope | `accounting-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-ANTIMICROBIAL_RESISTANCE_BASICS@1` | scope | `antimicrobial-resistance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-STATISTICS_BASICS@1` | scope | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-ACCOUNTING_BASICS@1` | source | `accounting-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ADMINISTRATIVE_LAW_BASICS-A@2` | claim | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ADMINISTRATIVE_LAW_BASICS-B@2` | claim | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ADMINISTRATIVE_LAW_BASICS-C@2` | claim | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-ADMINISTRATIVE_LAW_BASICS@2` | context | `administrative-law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ADMINISTRATIVE_LAW_BASICS-A@2` | evidence_use | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ADMINISTRATIVE_LAW_BASICS-B@2` | evidence_use | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ADMINISTRATIVE_LAW_BASICS-C@2` | evidence_use | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT-A@2` | evidence_use | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT-B@2` | evidence_use | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT-C@2` | evidence_use | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-ADMINISTRATIVE_LAW_BASICS@2` | scope | `administrative-law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-ADMINISTRATIVE_LAW_BASICS-INDEPENDENT@2` | source | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-ADMINISTRATIVE_LAW_BASICS@2` | source | `administrative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM_AGRICULTURAL_ENGINEERING_BASICS_A@1` | claim | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_AGRICULTURAL_ENGINEERING_BASICS_B@1` | claim | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_AGRICULTURAL_ENGINEERING_BASICS_C@1` | claim | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_AGRICULTURAL_ENGINEERING_BASICS@1` | source | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_AGRICULTURAL_ENGINEERING_BASICS_A@1` | evidence_use | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM_AGRICULTURAL_ENGINEERING_BASICS_A@1; canonical file EU-AGRICULTURAL_ENGINEERING_BASICS-A.json |
| `EU_AGRICULTURAL_ENGINEERING_BASICS_B@1` | evidence_use | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM_AGRICULTURAL_ENGINEERING_BASICS_B@1; canonical file EU-AGRICULTURAL_ENGINEERING_BASICS-B.json |
| `EU_AGRICULTURAL_ENGINEERING_BASICS_C@1` | evidence_use | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM_AGRICULTURAL_ENGINEERING_BASICS_C@1; canonical file EU-AGRICULTURAL_ENGINEERING_BASICS-C.json |
| `CTX_AGRICULTURAL_ENGINEERING_BASICS@1` | context | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | canonical context target CLM_AGRICULTURAL_ENGINEERING_BASICS_A@1; canonical file CTX-AGRICULTURAL_ENGINEERING_BASICS.json |
| `SCP_AGRICULTURAL_ENGINEERING_BASICS@1` | scope | `agricultural-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | canonical scope target CLM_AGRICULTURAL_ENGINEERING_BASICS_A@1; canonical file SCP-AGRICULTURAL_ENGINEERING_BASICS.json |
| `CLM-AGRIFOOD_SYSTEMS_BASICS-A@1` | claim | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-AGRIFOOD_SYSTEMS_BASICS-B@1` | claim | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-AGRIFOOD_SYSTEMS_BASICS-C@1` | claim | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-AGRIFOOD_SYSTEMS_BASICS@1` | source | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-AGRIFOOD_SYSTEMS_BASICS-A@1` | evidence_use | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-AGRIFOOD_SYSTEMS_BASICS-A@1; canonical file EU-AGRIFOOD_SYSTEMS_BASICS-A.json |
| `EU-AGRIFOOD_SYSTEMS_BASICS-B@1` | evidence_use | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-AGRIFOOD_SYSTEMS_BASICS-B@1; canonical file EU-AGRIFOOD_SYSTEMS_BASICS-B.json |
| `EU-AGRIFOOD_SYSTEMS_BASICS-C@1` | evidence_use | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-AGRIFOOD_SYSTEMS_BASICS-C@1; canonical file EU-AGRIFOOD_SYSTEMS_BASICS-C.json |
| `CTX-AGRIFOOD_SYSTEMS_BASICS@1` | context | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | canonical context target CLM-AGRIFOOD_SYSTEMS_BASICS-A@1; canonical file CTX-AGRIFOOD_SYSTEMS_BASICS.json |
| `SCP-AGRIFOOD_SYSTEMS_BASICS@1` | scope | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | canonical scope target CLM-AGRIFOOD_SYSTEMS_BASICS-A@1; canonical file SCP-AGRIFOOD_SYSTEMS_BASICS.json |
| `SRC-WORLDBANK-FOODSYSTEMS-2030@1` | source | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via EU-AGRIFOOD-WORLDBANK-CORROBORATION@1; canonical file SRC-WORLDBANK-FOODSYSTEMS-2030.json |
| `EU-AGRIFOOD-WORLDBANK-CORROBORATION@1` | evidence_use | `agrifood-systems-basics` | HOLD | canonical_json_dependency_verified_hold | canonical independent corroboration for CLM-AGRIFOOD_SYSTEMS_BASICS-C@1; canonical file EU-AGRIFOOD-WORLDBANK-CORROBORATION.json |
| `SRC-ANTIMICROBIAL_RESISTANCE_BASICS@1` | source | `antimicrobial-resistance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-ARCHIVAL_SCIENCE-A@2` | claim | `archival-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ARCHIVAL_SCIENCE-B@3` | claim | `archival-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ARCHIVAL_SCIENCE-C@2` | claim | `archival-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-ARCHIVAL_SCIENCE@2` | context | `archival-science-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ARCHIVAL_SCIENCE-A@2` | evidence_use | `archival-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ARCHIVAL_SCIENCE-B@3` | evidence_use | `archival-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ARCHIVAL_SCIENCE-C@2` | evidence_use | `archival-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-ARCHIVAL_SCIENCE@2` | scope | `archival-science-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-ARCHIVAL_SCIENCE-ICA@1` | source | `archival-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-ARCHIVAL_SCIENCE@2` | source | `archival-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-A@2` | claim | `artificial-intelligence-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-B@2` | claim | `artificial-intelligence-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ARTIFICIAL_INTELLIGENCE_BASICS-C@2` | claim | `artificial-intelligence-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-ARTIFICIAL_INTELLIGENCE_BASICS@2` | context | `artificial-intelligence-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ARTIFICIAL_INTELLIGENCE_BASICS-A@2` | evidence_use | `artificial-intelligence-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ARTIFICIAL_INTELLIGENCE_BASICS-B@2` | evidence_use | `artificial-intelligence-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ARTIFICIAL_INTELLIGENCE_BASICS-C@2` | evidence_use | `artificial-intelligence-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-ARTIFICIAL_INTELLIGENCE_BASICS@2` | scope | `artificial-intelligence-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-ARTIFICIAL_INTELLIGENCE_BASICS@2` | source | `artificial-intelligence-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ASTRONOMY_BASICS-A@1` | claim | `astronomy-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-ASTRONOMY_BASICS-A@1` | evidence_use | `astronomy-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-ASTRONOMY_BASICS@1` | source | `astronomy-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-BIOCHEMISTRY_BASICS-A@2` | claim | `biochemistry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-BIOCHEMISTRY_BASICS-B@3` | claim | `biochemistry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-BIOCHEMISTRY_BASICS-C@2` | claim | `biochemistry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-BIOCHEMISTRY_BASICS@2` | context | `biochemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-BIOCHEMISTRY_BASICS-A@2` | evidence_use | `biochemistry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-BIOCHEMISTRY_BASICS-B@3` | evidence_use | `biochemistry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-BIOCHEMISTRY_BASICS-C@2` | evidence_use | `biochemistry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-BIOCHEMISTRY_BASICS@2` | scope | `biochemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-BIOCHEMISTRY_BASICS@2` | source | `biochemistry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-BIODIVERSITY_BASICS-A@1` | claim | `biodiversity-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-BIODIVERSITY_BASICS-B@1` | claim | `biodiversity-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-BIODIVERSITY_BASICS-C@1` | claim | `biodiversity-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-BIODIVERSITY_BASICS-A@1` | evidence_use | `biodiversity-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-BIODIVERSITY_BASICS@1` | source | `biodiversity-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-CALCULUS_BASICS-A@1` | claim | `calculus-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CALCULUS_BASICS-B@1` | claim | `calculus-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CALCULUS_BASICS-C@1` | claim | `calculus-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-CALCULUS_BASICS@1` | context | `calculus-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CALCULUS_BASICS-A@1` | evidence_use | `calculus-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CALCULUS_BASICS-B@1` | evidence_use | `calculus-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CALCULUS_BASICS-C@1` | evidence_use | `calculus-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-CALCULUS_BASICS@1` | scope | `calculus-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CALCULUS_BASICS@1` | source | `calculus-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CARTOGRAPHY-A@2` | claim | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CARTOGRAPHY-B@2` | claim | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CARTOGRAPHY-C@2` | claim | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-CARTOGRAPHY@2` | context | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CARTOGRAPHY-A@2` | evidence_use | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CARTOGRAPHY-B@2` | evidence_use | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CARTOGRAPHY-C@2` | evidence_use | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-CARTOGRAPHY@2` | scope | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CARTOGRAPHY-TOPO@1` | source | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CARTOGRAPHY@2` | source | `cartography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CELL_BASICS-A@1` | claim | `cell-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-CELL_BASICS-A@1` | evidence_use | `cell-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-CELL_BASICS@1` | source | `cell-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-CELL_BIOLOGY_BASICS-A@1` | claim | `cell-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-CELL_BIOLOGY_BASICS-A@1` | evidence_use | `cell-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-CELL_BIOLOGY_BASICS@1` | source | `cell-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-CHEMICAL_REACTIONS_BASICS-A@2` | claim | `chemical-reactions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CHEMICAL_REACTIONS_BASICS-B@2` | claim | `chemical-reactions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CHEMICAL_REACTIONS_BASICS-C@2` | claim | `chemical-reactions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-CHEMICAL_REACTIONS_BASICS@2` | context | `chemical-reactions-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CHEMICAL_REACTIONS_BASICS-A@4` | evidence_use | `chemical-reactions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CHEMICAL_REACTIONS_BASICS-B@4` | evidence_use | `chemical-reactions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CHEMICAL_REACTIONS_BASICS-C@4` | evidence_use | `chemical-reactions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-CHEMICAL_REACTIONS_BASICS@2` | scope | `chemical-reactions-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CHEMICAL_REACTIONS_BASICS@2` | source | `chemical-reactions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CIVIL_SOCIETY_BASICS-A@1` | claim | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CIVIL_SOCIETY_BASICS-B@1` | claim | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CIVIL_SOCIETY_BASICS-C@1` | claim | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-CIVIL_SOCIETY_BASICS@1` | context | `civil-society-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CIVIL_SOCIETY_BASICS-A@1` | evidence_use | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CIVIL_SOCIETY_BASICS-B@1` | evidence_use | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CIVIL_SOCIETY_BASICS-C@1` | evidence_use | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CIVIL_SOCIETY_BASICS-INDEPENDENT-A@1` | evidence_use | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CIVIL_SOCIETY_BASICS-INDEPENDENT-B@1` | evidence_use | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CIVIL_SOCIETY_BASICS-INDEPENDENT-C@1` | evidence_use | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-CIVIL_SOCIETY_BASICS@1` | scope | `civil-society-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CIVIL_SOCIETY_BASICS-INDEPENDENT@1` | source | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CIVIL_SOCIETY_BASICS@1` | source | `civil-society-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CLIMATE_SCIENCE_BASICS-A@1` | claim | `climate-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CLIMATE_SCIENCE_BASICS-B@1` | claim | `climate-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CLIMATE_SCIENCE_BASICS-C@1` | claim | `climate-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-CLIMATE_SCIENCE_BASICS@1` | context | `climate-science-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CLIMATE_SCIENCE_BASICS-A@1` | evidence_use | `climate-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CLIMATE_SCIENCE_BASICS-B@1` | evidence_use | `climate-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CLIMATE_SCIENCE_BASICS-C@1` | evidence_use | `climate-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-CLIMATE_SCIENCE_BASICS@1` | scope | `climate-science-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CLIMATE_SCIENCE_BASICS@1` | source | `climate-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-A@1` | claim | `comparative-civilizations-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-B@1` | claim | `comparative-civilizations-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-C@1` | claim | `comparative-civilizations-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-COMPARATIVE_CIVILIZATIONS_BASICS@1` | context | `comparative-civilizations-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_CIVILIZATIONS_BASICS-A@1` | evidence_use | `comparative-civilizations-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_CIVILIZATIONS_BASICS-B@1` | evidence_use | `comparative-civilizations-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_CIVILIZATIONS_BASICS-C@1` | evidence_use | `comparative-civilizations-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-COMPARATIVE_CIVILIZATIONS_BASICS@1` | scope | `comparative-civilizations-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-COMPARATIVE_CIVILIZATIONS_BASICS@1` | source | `comparative-civilizations-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPARATIVE_LAW_BASICS-A@2` | claim | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPARATIVE_LAW_BASICS-B@2` | claim | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPARATIVE_LAW_BASICS-C@2` | claim | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-COMPARATIVE_LAW_BASICS@2` | context | `comparative-law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_LAW_BASICS-A@2` | evidence_use | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_LAW_BASICS-B@2` | evidence_use | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_LAW_BASICS-C@2` | evidence_use | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_LAW_BASICS-INDEPENDENT-A@2` | evidence_use | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_LAW_BASICS-INDEPENDENT-B@2` | evidence_use | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPARATIVE_LAW_BASICS-INDEPENDENT-C@2` | evidence_use | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-COMPARATIVE_LAW_BASICS@2` | scope | `comparative-law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-COMPARATIVE_LAW_BASICS-INDEPENDENT@2` | source | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-COMPARATIVE_LAW_BASICS@2` | source | `comparative-law-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPUTER_NETWORKS_BASICS-A@1` | claim | `computer-networks-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPUTER_NETWORKS_BASICS-B@1` | claim | `computer-networks-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPUTER_NETWORKS_BASICS-C@1` | claim | `computer-networks-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-COMPUTER_NETWORKS_BASICS@1` | context | `computer-networks-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPUTER_NETWORKS_BASICS-A@1` | evidence_use | `computer-networks-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPUTER_NETWORKS_BASICS-B@1` | evidence_use | `computer-networks-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPUTER_NETWORKS_BASICS-C@1` | evidence_use | `computer-networks-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-COMPUTER_NETWORKS_BASICS@1` | scope | `computer-networks-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-COMPUTER_NETWORKS_BASICS@1` | source | `computer-networks-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-A@2` | claim | `computer-science-algorithms-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-B@2` | claim | `computer-science-algorithms-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-C@2` | claim | `computer-science-algorithms-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-COMPUTER_SCIENCE_ALGORITHMS_BASICS@2` | context | `computer-science-algorithms-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPUTER_SCIENCE_ALGORITHMS_BASICS-A@2` | evidence_use | `computer-science-algorithms-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPUTER_SCIENCE_ALGORITHMS_BASICS-B@2` | evidence_use | `computer-science-algorithms-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-COMPUTER_SCIENCE_ALGORITHMS_BASICS-C@2` | evidence_use | `computer-science-algorithms-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-COMPUTER_SCIENCE_ALGORITHMS_BASICS@2` | scope | `computer-science-algorithms-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-COMPUTER_SCIENCE_ALGORITHMS_BASICS@2` | source | `computer-science-algorithms-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CONSERVATION_BIOLOGY_BASICS-A@1` | claim | `conservation-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-CONSERVATION_BIOLOGY_BASICS-B@1` | claim | `conservation-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-CONSERVATION_BIOLOGY_BASICS-C@1` | claim | `conservation-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-CONSERVATION_BIOLOGY_BASICS@1` | source | `conservation-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-CULTURAL_ANTHROPOLOGY-A@1` | claim | `cultural-anthropology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CULTURAL_ANTHROPOLOGY-B@1` | claim | `cultural-anthropology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CULTURAL_ANTHROPOLOGY-C@1` | claim | `cultural-anthropology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-CULTURAL_ANTHROPOLOGY@1` | context | `cultural-anthropology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CULTURAL_ANTHROPOLOGY-A@1` | evidence_use | `cultural-anthropology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CULTURAL_ANTHROPOLOGY-B@1` | evidence_use | `cultural-anthropology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CULTURAL_ANTHROPOLOGY-C@1` | evidence_use | `cultural-anthropology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-CULTURAL_ANTHROPOLOGY@1` | scope | `cultural-anthropology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CULTURAL_ANTHROPOLOGY@1` | source | `cultural-anthropology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CULTURAL_HERITAGE-A@2` | claim | `cultural-heritage-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CULTURAL_HERITAGE-B@2` | claim | `cultural-heritage-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-CULTURAL_HERITAGE-C@2` | claim | `cultural-heritage-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-CULTURAL_HERITAGE@2` | context | `cultural-heritage-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CULTURAL_HERITAGE-A@2` | evidence_use | `cultural-heritage-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CULTURAL_HERITAGE-B@2` | evidence_use | `cultural-heritage-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-CULTURAL_HERITAGE-C@2` | evidence_use | `cultural-heritage-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-CULTURAL_HERITAGE@2` | scope | `cultural-heritage-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CULTURAL_HERITAGE-ICH@1` | source | `cultural-heritage-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-CULTURAL_HERITAGE@2` | source | `cultural-heritage-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DATABASES_BASICS-A@3` | claim | `databases-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DATABASES_BASICS-B@3` | claim | `databases-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DATABASES_BASICS-C@3` | claim | `databases-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-DATABASES_BASICS@3` | context | `databases-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DATABASES_BASICS-A@3` | evidence_use | `databases-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DATABASES_BASICS-B@3` | evidence_use | `databases-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DATABASES_BASICS-C@3` | evidence_use | `databases-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-DATABASES_BASICS@3` | scope | `databases-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-DATABASES_BASICS@3` | source | `databases-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DEMOCRATIC_INSTITUTIONS_BASICS-A@1` | claim | `democratic-institutions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DEMOCRATIC_INSTITUTIONS_BASICS-B@1` | claim | `democratic-institutions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DEMOCRATIC_INSTITUTIONS_BASICS-C@1` | claim | `democratic-institutions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-DEMOCRATIC_INSTITUTIONS_BASICS@1` | context | `democratic-institutions-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DEMOCRATIC_INSTITUTIONS_BASICS-A@1` | evidence_use | `democratic-institutions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DEMOCRATIC_INSTITUTIONS_BASICS-B@1` | evidence_use | `democratic-institutions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DEMOCRATIC_INSTITUTIONS_BASICS-C@1` | evidence_use | `democratic-institutions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-DEMOCRATIC_INSTITUTIONS_BASICS@1` | scope | `democratic-institutions-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-DEMOCRATIC_INSTITUTIONS_BASICS@1` | source | `democratic-institutions-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DEMOGRAPHY_BASICS-A@1` | claim | `demography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DEMOGRAPHY_BASICS-B@1` | claim | `demography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DEMOGRAPHY_BASICS-C@1` | claim | `demography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-DEMOGRAPHY_BASICS@1` | context | `demography-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DEMOGRAPHY_BASICS-A@1` | evidence_use | `demography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DEMOGRAPHY_BASICS-B@1` | evidence_use | `demography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DEMOGRAPHY_BASICS-C@1` | evidence_use | `demography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-DEMOGRAPHY_BASICS@1` | scope | `demography-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-DEMOGRAPHY_BASICS@1` | source | `demography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DISASTER_RECOVERY_BASICS-A@1` | claim | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-DISASTER_RECOVERY_BASICS-B@1` | claim | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-DISASTER_RECOVERY_BASICS-C@1` | claim | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-DISASTER_RECOVERY_BASICS-D@1` | claim | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-DISASTER_RECOVERY_BASICS@1` | context | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-DISASTER_RECOVERY_BASICS-A@1` | evidence_use | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-DISASTER_RECOVERY_BASICS-B@1` | evidence_use | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-DISASTER_RECOVERY_BASICS-C@1` | evidence_use | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-DISASTER_RECOVERY_BASICS-D@1` | evidence_use | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-DISASTER_RECOVERY_BASICS@1` | scope | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-DISASTER_RECOVERY_BASICS@1` | source | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-UNDRR-RECOVERY-2026@1` | source | `disaster-recovery-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via EU-DISASTER_RECOVERY_BASICS-D@1; canonical file SRC-UNDRR-RECOVERY-2026.json |
| `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_A@1` | claim | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_B@1` | claim | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_DISASTER_RESPONSE_LOGISTICS_BASICS_C@1` | claim | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX_DISASTER_RESPONSE_LOGISTICS_BASICS@1` | context | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A_FEMA@1` | evidence_use | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_A@1` | evidence_use | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-DISASTER_RESPONSE_LOGISTICS_BASICS-B-FEMA@1` | evidence_use | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold (canonical ID corrected from base register token) | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_B@1` | evidence_use | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-DISASTER_RESPONSE_LOGISTICS_BASICS-C-FEMA@1` | evidence_use | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold (canonical ID corrected from base register token) | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_DISASTER_RESPONSE_LOGISTICS_BASICS_C@1` | evidence_use | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP_DISASTER_RESPONSE_LOGISTICS_BASICS@1` | scope | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_DISASTER_RESPONSE_LOGISTICS_BASICS@1` | source | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-FEMA-DISASTER-LOGISTICS-2026@1` | source | `disaster-response-logistics-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via FEMA Evidence Use A/B/C; canonical file SRC-FEMA-DISASTER-LOGISTICS-2026.json |
| `CLM-DISTRIBUTED_SYSTEMS_BASICS-A@2` | claim | `distributed-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DISTRIBUTED_SYSTEMS_BASICS-B@2` | claim | `distributed-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-DISTRIBUTED_SYSTEMS_BASICS-C@2` | claim | `distributed-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-DISTRIBUTED_SYSTEMS_BASICS@2` | context | `distributed-systems-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DISTRIBUTED_SYSTEMS_BASICS-A@2` | evidence_use | `distributed-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DISTRIBUTED_SYSTEMS_BASICS-B@2` | evidence_use | `distributed-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-DISTRIBUTED_SYSTEMS_BASICS-C@2` | evidence_use | `distributed-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-DISTRIBUTED_SYSTEMS_BASICS@2` | scope | `distributed-systems-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-DISTRIBUTED_SYSTEMS_BASICS@2` | source | `distributed-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ECOPHYSIOLOGY_BASICS-A@1` | claim | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-ECOPHYSIOLOGY_BASICS-B@1` | claim | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-ECOPHYSIOLOGY_BASICS-C@1` | claim | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-ECOPHYSIOLOGY_BASICS@1` | context | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-ECOPHYSIOLOGY_BASICS@1` | scope | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-ECOPHYSIOLOGY_BASICS@1` | source | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-ECOPHYSIOLOGY_BASICS-A@1` | evidence_use | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-ECOPHYSIOLOGY_BASICS-A@1; canonical file EU-ECOPHYSIOLOGY_BASICS-A.json |
| `EU-ECOPHYSIOLOGY_BASICS-B@1` | evidence_use | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-ECOPHYSIOLOGY_BASICS-B@1; canonical file EU-ECOPHYSIOLOGY_BASICS-B.json |
| `EU-ECOPHYSIOLOGY_BASICS-C@1` | evidence_use | `ecophysiology-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-ECOPHYSIOLOGY_BASICS-C@1; canonical file EU-ECOPHYSIOLOGY_BASICS-C.json |
| `CLM-ECOTOXICOLOGY_BASICS-A@1` | claim | `ecotoxicology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-ECOTOXICOLOGY_BASICS-B@1` | claim | `ecotoxicology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-ECOTOXICOLOGY_BASICS-C@1` | claim | `ecotoxicology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-ECOTOXICOLOGY_BASICS@1` | source | `ecotoxicology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-EDUCATION_SYSTEMS-A@1` | claim | `education-systems` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-EDUCATION_SYSTEMS-B@1` | claim | `education-systems` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-EDUCATION_SYSTEMS-C@1` | claim | `education-systems` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-EDUCATION_SYSTEMS@1` | context | `education-systems` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-EDUCATION_SYSTEMS-A@1` | evidence_use | `education-systems` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-EDUCATION_SYSTEMS-B@1` | evidence_use | `education-systems` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-EDUCATION_SYSTEMS-C@1` | evidence_use | `education-systems` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-EDUCATION_SYSTEMS@1` | scope | `education-systems` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-EDUCATION_SYSTEMS@1` | source | `education-systems` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM_ELECTRICAL_GRID_BASICS_A@1` | claim | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_ELECTRICAL_GRID_BASICS_B@1` | claim | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_ELECTRICAL_GRID_BASICS_C@1` | claim | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-ELECTRICAL_GRID_BASICS-D@1` | claim | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold (canonical ID corrected from base register token) | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX_ELECTRICAL_GRID_BASICS@1` | context | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_ELECTRICAL_GRID_BASICS_A@1` | evidence_use | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_ELECTRICAL_GRID_BASICS_B@1` | evidence_use | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_ELECTRICAL_GRID_BASICS_C@1` | evidence_use | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-ELECTRICAL_GRID_BASICS-D@1` | evidence_use | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold (canonical ID corrected from base register token) | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP_ELECTRICAL_GRID_BASICS@1` | scope | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_ELECTRICAL_GRID_BASICS@1` | source | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-DOE-ELECTRIC-GRIDS-2026@1` | source | `electrical-grid-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via EU-ELECTRICAL_GRID_BASICS-D@1; canonical file SRC-DOE-ELECTRIC-GRIDS-2026.json |
| `CLM-ELECTROMAGNETISM_BASICS-A@1` | claim | `electromagnetism-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ELECTROMAGNETISM_BASICS-B@1` | claim | `electromagnetism-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ELECTROMAGNETISM_BASICS-C@1` | claim | `electromagnetism-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-ELECTROMAGNETISM_BASICS@1` | context | `electromagnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ELECTROMAGNETISM_BASICS-A@1` | evidence_use | `electromagnetism-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ELECTROMAGNETISM_BASICS-B@1` | evidence_use | `electromagnetism-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ELECTROMAGNETISM_BASICS-C@1` | evidence_use | `electromagnetism-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-ELECTROMAGNETISM_BASICS@1` | scope | `electromagnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-ELECTROMAGNETISM_BASICS@1` | source | `electromagnetism-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ENTOMOLOGY_BASICS-A@1` | claim | `entomology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-ENTOMOLOGY_BASICS-B@1` | claim | `entomology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-ENTOMOLOGY_BASICS-C@1` | claim | `entomology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-ENTOMOLOGY_BASICS@1` | source | `entomology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-EVOLUTION_BASICS-A@1` | claim | `evolution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-EVOLUTION_BASICS-A@1` | evidence_use | `evolution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-EVOLUTION_BASICS@1` | source | `evolution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FLUID_MECHANICS_BASICS-A@1` | claim | `fluid-mechanics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-FLUID_MECHANICS_BASICS-B@1` | claim | `fluid-mechanics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-FLUID_MECHANICS_BASICS-C@1` | claim | `fluid-mechanics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-FLUID_MECHANICS_BASICS@1` | context | `fluid-mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-FLUID_MECHANICS_BASICS-A@1` | evidence_use | `fluid-mechanics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-FLUID_MECHANICS_BASICS-B@1` | evidence_use | `fluid-mechanics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-FLUID_MECHANICS_BASICS-C@1` | evidence_use | `fluid-mechanics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-FLUID_MECHANICS_BASICS@1` | scope | `fluid-mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-FLUID_MECHANICS_BASICS@1` | source | `fluid-mechanics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-FOOD_DISTRIBUTION_BASICS-A@1` | claim | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FOOD_DISTRIBUTION_BASICS-B@1` | claim | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FOOD_DISTRIBUTION_BASICS-C@1` | claim | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FOOD_DISTRIBUTION_BASICS-D@1` | claim | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-FOOD_DISTRIBUTION_BASICS@1` | context | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-FOOD_DISTRIBUTION_BASICS-A@1` | evidence_use | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-FOOD_DISTRIBUTION_BASICS-D@1` | evidence_use | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-FOOD_DISTRIBUTION_BASICS-B@1` | evidence_use | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-FOOD_DISTRIBUTION_BASICS-B@1; canonical file EU-FOOD_DISTRIBUTION_BASICS-B.json |
| `EU-FOOD_DISTRIBUTION_BASICS-C@1` | evidence_use | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-FOOD_DISTRIBUTION_BASICS-C@1; canonical file EU-FOOD_DISTRIBUTION_BASICS-C.json
| `SCP-FOOD_DISTRIBUTION_BASICS@1` | scope | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-FOOD_DISTRIBUTION_BASICS@1` | source | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-FOOD_DISTRIBUTION_WFP@1` | source | `food-distribution-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FOOD_SYSTEMS-A@1` | claim | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FOOD_SYSTEMS-A@2` | claim | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-FOOD_SYSTEMS-B@1` | claim | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FOOD_SYSTEMS-B@2` | claim | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-FOOD_SYSTEMS-C@1` | claim | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FOOD_SYSTEMS-C@2` | claim | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-FOOD_SYSTEMS-D@1` | claim | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-FOOD_SYSTEMS-D@2` | claim | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-FOOD_SYSTEMS@1` | context | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-FOOD_SYSTEMS@2` | context | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-FOOD_SYSTEMS-A@1` | evidence_use | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-FOOD_SYSTEMS-A@2` | evidence_use | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-FOOD_SYSTEMS-B@2` | evidence_use | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-FOOD_SYSTEMS-C@2` | evidence_use | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-FOOD_SYSTEMS-D@1` | evidence_use | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-FOOD_SYSTEMS-D@2` | evidence_use | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-FOOD_SYSTEMS@1` | scope | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-FOOD_SYSTEMS@2` | scope | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-FOOD_SYSTEMS_WB@1` | source | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-FOOD_SYSTEMS_WB@2` | source | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-FOOD_SYSTEMS@1` | source | `food-systems-basics` | HOLD | historical_version_superseded | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-FOOD_SYSTEMS@2` | source | `food-systems-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-GENETICS_BASICS-A@1` | claim | `genetics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-GENETICS_BASICS-A@1` | evidence_use | `genetics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-GENETICS_BASICS@1` | source | `genetics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-GEOMETRY_BASICS-A@1` | claim | `geometry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-GEOMETRY_BASICS-B@1` | claim | `geometry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-GEOMETRY_BASICS-C@1` | claim | `geometry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-GEOMETRY_BASICS@1` | context | `geometry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-GEOMETRY_BASICS-A@1` | evidence_use | `geometry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-GEOMETRY_BASICS-B@1` | evidence_use | `geometry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-GEOMETRY_BASICS-C@1` | evidence_use | `geometry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-GEOMETRY_BASICS@1` | scope | `geometry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-GEOMETRY_BASICS@1` | source | `geometry-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-GOVERNANCE_BASICS-A@1` | claim | `governance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-GOVERNANCE_BASICS-B@1` | claim | `governance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-GOVERNANCE_BASICS-C@1` | claim | `governance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-GOVERNANCE_BASICS@1` | context | `governance-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-GOVERNANCE_BASICS-A@1` | evidence_use | `governance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-GOVERNANCE_BASICS-B@1` | evidence_use | `governance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-GOVERNANCE_BASICS-C@1` | evidence_use | `governance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-GOVERNANCE_BASICS@1` | scope | `governance-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-GOVERNANCE_BASICS@1` | source | `governance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORICAL_GEOGRAPHY-A@1` | claim | `historical-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORICAL_GEOGRAPHY-B@1` | claim | `historical-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORICAL_GEOGRAPHY-C@1` | claim | `historical-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-HISTORICAL_GEOGRAPHY@1` | context | `historical-geography-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORICAL_GEOGRAPHY-A@1` | evidence_use | `historical-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORICAL_GEOGRAPHY-B@1` | evidence_use | `historical-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORICAL_GEOGRAPHY-C@1` | evidence_use | `historical-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-HISTORICAL_GEOGRAPHY@1` | scope | `historical-geography-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HISTORICAL_GEOGRAPHY@1` | source | `historical-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_ENGINEERING-A@2` | claim | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_ENGINEERING-B@2` | claim | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_ENGINEERING-C@2` | claim | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-HISTORY_OF_ENGINEERING@2` | context | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_ENGINEERING-A@2` | evidence_use | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_ENGINEERING-B@2` | evidence_use | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_ENGINEERING-C@2` | evidence_use | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-HISTORY_OF_ENGINEERING@2` | scope | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HISTORY_OF_ENGINEERING@2` | source | `history-of-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_MATHEMATICS-A@2` | claim | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_MATHEMATICS-B@2` | claim | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_MATHEMATICS-C@2` | claim | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-HISTORY_OF_MATHEMATICS@2` | context | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_MATHEMATICS-A@2` | evidence_use | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_MATHEMATICS-B@2` | evidence_use | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_MATHEMATICS-C@2` | evidence_use | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-HISTORY_OF_MATHEMATICS@2` | scope | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HISTORY_OF_MATHEMATICS-CAMBRIDGE@1` | source | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HISTORY_OF_MATHEMATICS-OXFORD@1` | source | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HISTORY_OF_MATHEMATICS@2` | source | `history-of-mathematics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_MEDICINE-A@2` | claim | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_MEDICINE-B@2` | claim | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_MEDICINE-C@2` | claim | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-HISTORY_OF_MEDICINE@2` | context | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_MEDICINE-A@2` | evidence_use | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_MEDICINE-B@2` | evidence_use | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_MEDICINE-C@2` | evidence_use | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-HISTORY_OF_MEDICINE@2` | scope | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HISTORY_OF_MEDICINE@2` | source | `history-of-medicine-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_SCIENCE-A@1` | claim | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_SCIENCE-B@1` | claim | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_SCIENCE-C@1` | claim | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-HISTORY_OF_SCIENCE@1` | context | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_SCIENCE-A@1` | evidence_use | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_SCIENCE-B@1` | evidence_use | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_SCIENCE-C@1` | evidence_use | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-HISTORY_OF_SCIENCE@1` | scope | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HISTORY_OF_SCIENCE@1` | source | `history-of-science-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_TECHNOLOGY-A@1` | claim | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_TECHNOLOGY-B@1` | claim | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HISTORY_OF_TECHNOLOGY-C@1` | claim | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-HISTORY_OF_TECHNOLOGY@1` | context | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_TECHNOLOGY-A@1` | evidence_use | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_TECHNOLOGY-B@1` | evidence_use | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HISTORY_OF_TECHNOLOGY-C@1` | evidence_use | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-HISTORY_OF_TECHNOLOGY@1` | scope | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HISTORY_OF_TECHNOLOGY@1` | source | `history-of-technology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HYDRAULIC_ENGINEERING-A@2` | claim | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HYDRAULIC_ENGINEERING-B@2` | claim | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-HYDRAULIC_ENGINEERING-C@2` | claim | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-HYDRAULIC_ENGINEERING@2` | context | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HYDRAULIC_ENGINEERING-A@2` | evidence_use | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HYDRAULIC_ENGINEERING-B@2` | evidence_use | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-HYDRAULIC_ENGINEERING-C@2` | evidence_use | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-HYDRAULIC_ENGINEERING@2` | scope | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HYDRAULIC_ENGINEERING-HMS@1` | source | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-HYDRAULIC_ENGINEERING@2` | source | `hydraulic-engineering-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-IMMUNOLOGY_BASICS-A@1` | claim | `immunology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-IMMUNOLOGY_BASICS-A@1` | evidence_use | `immunology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-IMMUNOLOGY_BASICS@1` | source | `immunology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-INFRASTRUCTURE_RESILIENCE-A@1` | claim | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-INFRASTRUCTURE_RESILIENCE-B@1` | claim | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-INFRASTRUCTURE_RESILIENCE-C@1` | claim | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-INFRASTRUCTURE_RESILIENCE-D@1` | claim | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-INFRASTRUCTURE_RESILIENCE@1` | context | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-INFRASTRUCTURE_RESILIENCE-A-2@1` | evidence_use | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-INFRASTRUCTURE_RESILIENCE-A@1` | evidence_use | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-INFRASTRUCTURE_RESILIENCE-B-2@1` | evidence_use | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-INFRASTRUCTURE_RESILIENCE-B@1` | evidence_use | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-INFRASTRUCTURE_RESILIENCE-C-2@1` | evidence_use | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-INFRASTRUCTURE_RESILIENCE-C@1` | evidence_use | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-INFRASTRUCTURE_RESILIENCE-D@1` | evidence_use | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-INFRASTRUCTURE_RESILIENCE@1` | scope | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-INFRASTRUCTURE_RESILIENCE@1` | source | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025@1` | source | `infrastructure-resilience-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via EU-INFRASTRUCTURE_RESILIENCE-A-2@1 / B-2@1 / C-2@1 / D@1; canonical file SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025.json |
| `CLM-INTERNATIONAL_LAW_BASICS-A@1` | claim | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-INTERNATIONAL_LAW_BASICS-A@2` | claim | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `CLM-INTERNATIONAL_LAW_BASICS-B@1` | claim | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-INTERNATIONAL_LAW_BASICS-B@2` | claim | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `CLM-INTERNATIONAL_LAW_BASICS-C@1` | claim | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-INTERNATIONAL_LAW_BASICS-C@2` | claim | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `CTX-INTERNATIONAL_LAW_BASICS@1` | context | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-INTERNATIONAL_LAW_BASICS@2` | context | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-A@1` | evidence_use | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-A@2` | evidence_use | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-B@1` | evidence_use | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-B@2` | evidence_use | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-C@1` | evidence_use | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-C@2` | evidence_use | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-A@1` | evidence_use | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-A@2` | evidence_use | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-B@1` | evidence_use | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-B@2` | evidence_use | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-C@1` | evidence_use | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-C@2` | evidence_use | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `SCP-INTERNATIONAL_LAW_BASICS@1` | scope | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-INTERNATIONAL_LAW_BASICS@2` | scope | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `SRC-INTERNATIONAL_LAW_BASICS-INDEPENDENT@1` | source | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-INTERNATIONAL_LAW_BASICS-INDEPENDENT@2` | source | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `SRC-INTERNATIONAL_LAW_BASICS@1` | source | `international-law-basics` | HOLD | audit_table_stale | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-INTERNATIONAL_LAW_BASICS@2` | source | `international-law-basics` | HOLD | canonical_json_substantively_rereviewed_hold | FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md |
| `CLM-LABOR_ECONOMICS_BASICS-A@1` | claim | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LABOR_ECONOMICS_BASICS-B@1` | claim | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LABOR_ECONOMICS_BASICS-C@1` | claim | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-LABOR_ECONOMICS_BASICS@1` | context | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LABOR_ECONOMICS_BASICS-A@1` | evidence_use | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LABOR_ECONOMICS_BASICS-B@1` | evidence_use | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LABOR_ECONOMICS_BASICS-C@1` | evidence_use | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LABOR_ECONOMICS_BASICS-INDEPENDENT-A@1` | evidence_use | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LABOR_ECONOMICS_BASICS-INDEPENDENT-B@1` | evidence_use | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LABOR_ECONOMICS_BASICS-INDEPENDENT-C@1` | evidence_use | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-LABOR_ECONOMICS_BASICS@1` | scope | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-LABOR_ECONOMICS_BASICS-INDEPENDENT@1` | source | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-LABOR_ECONOMICS_BASICS@1` | source | `labor-economics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LAW_BASICS-A@1` | claim | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LAW_BASICS-B@1` | claim | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LAW_BASICS-C@1` | claim | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-LAW_BASICS@1` | context | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LAW_BASICS-A@1` | evidence_use | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LAW_BASICS-B@1` | evidence_use | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LAW_BASICS-C@1` | evidence_use | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-LAW_BASICS@1` | scope | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-LAW_BASICS@1` | source | `law-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LIBRARY_SCIENCE-A@2` | claim | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LIBRARY_SCIENCE-B@2` | claim | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LIBRARY_SCIENCE-C@2` | claim | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-LIBRARY_SCIENCE@2` | context | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LIBRARY_SCIENCE-A@2` | evidence_use | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LIBRARY_SCIENCE-B@2` | evidence_use | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LIBRARY_SCIENCE-C@2` | evidence_use | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-LIBRARY_SCIENCE@2` | scope | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-LIBRARY_SCIENCE@2` | source | `library-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LITERATURE-A@1` | claim | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LITERATURE-B@1` | claim | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-LITERATURE-C@1` | claim | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-LITERATURE@1` | context | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LITERATURE-A@1` | evidence_use | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LITERATURE-B@1` | evidence_use | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-LITERATURE-C@1` | evidence_use | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-LITERATURE@1` | scope | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-LITERATURE@1` | source | `literature-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MACROECONOMICS_BASICS-A@1` | claim | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MACROECONOMICS_BASICS-B@1` | claim | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MACROECONOMICS_BASICS-C@1` | claim | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-MACROECONOMICS_BASICS@1` | context | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MACROECONOMICS_BASICS-A@1` | evidence_use | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MACROECONOMICS_BASICS-B@1` | evidence_use | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MACROECONOMICS_BASICS-C@1` | evidence_use | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-MACROECONOMICS_BASICS@1` | scope | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MACROECONOMICS_BASICS@1` | source | `macroeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MAGNETISM_BASICS-A@1` | claim | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MAGNETISM_BASICS-B@1` | claim | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MAGNETISM_BASICS-C@1` | claim | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-MAGNETISM_BASICS@1` | context | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MAGNETISM_BASICS-A@1` | evidence_use | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MAGNETISM_BASICS-B@1` | evidence_use | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MAGNETISM_BASICS-C@1` | evidence_use | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-MAGNETISM_BASICS@1` | scope | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MAGNETISM_BASICS@1` | source | `magnetism-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM_MARINE_BIOLOGY_BASICS_A@1` | claim | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_MARINE_BIOLOGY_BASICS_B@1` | claim | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_MARINE_BIOLOGY_BASICS_C@1` | claim | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_MARINE_BIOLOGY_BASICS@1` | source | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | claim | `measurement-uncertainty-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | evidence_use | `measurement-uncertainty-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1` | source | `measurement-uncertainty-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-MECHANICS_BASICS-A@2` | claim | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MECHANICS_BASICS-B@2` | claim | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MECHANICS_BASICS-C@2` | claim | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-MECHANICS_BASICS@2` | context | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MECHANICS_BASICS-A@2` | evidence_use | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MECHANICS_BASICS-B@2` | evidence_use | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MECHANICS_BASICS-C@2` | evidence_use | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-MECHANICS_BASICS@2` | scope | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MECHANICS_BASICS@2` | source | `mechanics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MICROECONOMICS_BASICS-A@1` | claim | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MICROECONOMICS_BASICS-B@1` | claim | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MICROECONOMICS_BASICS-C@1` | claim | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-MICROECONOMICS_BASICS@1` | context | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MICROECONOMICS_BASICS-A@1` | evidence_use | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MICROECONOMICS_BASICS-B@1` | evidence_use | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MICROECONOMICS_BASICS-C@1` | evidence_use | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-MICROECONOMICS_BASICS@1` | scope | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MICROECONOMICS_BASICS@1` | source | `microeconomics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIGRATION_AND_MOBILITY_BASICS-A@2` | claim | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIGRATION_AND_MOBILITY_BASICS-B@2` | claim | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIGRATION_AND_MOBILITY_BASICS-C@2` | claim | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-MIGRATION_AND_MOBILITY_BASICS@2` | context | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_AND_MOBILITY_BASICS-A@2` | evidence_use | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_AND_MOBILITY_BASICS-B@2` | evidence_use | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_AND_MOBILITY_BASICS-C@2` | evidence_use | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_AND_MOBILITY_BASICS-INDEPENDENT-A@2` | evidence_use | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_AND_MOBILITY_BASICS-INDEPENDENT-B@2` | evidence_use | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_AND_MOBILITY_BASICS-INDEPENDENT-C@2` | evidence_use | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-MIGRATION_AND_MOBILITY_BASICS@2` | scope | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MIGRATION_AND_MOBILITY_BASICS-INDEPENDENT@2` | source | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MIGRATION_AND_MOBILITY_BASICS@2` | source | `migration-and-mobility-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIGRATION_BASICS-A@1` | claim | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIGRATION_BASICS-B@1` | claim | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIGRATION_BASICS-C@1` | claim | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-MIGRATION_BASICS@1` | context | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_BASICS-A@1` | evidence_use | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_BASICS-B@1` | evidence_use | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIGRATION_BASICS-C@1` | evidence_use | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-MIGRATION_BASICS@1` | scope | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MIGRATION_BASICS@1` | source | `migration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIXTURES_AND_SOLUTIONS-A@1` | claim | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIXTURES_AND_SOLUTIONS-B@1` | claim | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MIXTURES_AND_SOLUTIONS-C@1` | claim | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-MIXTURES_AND_SOLUTIONS@1` | context | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIXTURES_AND_SOLUTIONS-A@2` | evidence_use | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIXTURES_AND_SOLUTIONS-B@2` | evidence_use | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MIXTURES_AND_SOLUTIONS-C@2` | evidence_use | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-MIXTURES_AND_SOLUTIONS@1` | scope | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MIXTURES_AND_SOLUTIONS@1` | source | `mixtures-and-solutions` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MONEY_AND_BANKING_BASICS-A@1` | claim | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MONEY_AND_BANKING_BASICS-B@1` | claim | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MONEY_AND_BANKING_BASICS-C@1` | claim | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-MONEY_AND_BANKING_BASICS@1` | context | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MONEY_AND_BANKING_BASICS-A@1` | evidence_use | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MONEY_AND_BANKING_BASICS-B@1` | evidence_use | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-MONEY_AND_BANKING_BASICS-C@1` | evidence_use | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-MONEY_AND_BANKING_BASICS@1` | scope | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-MONEY_AND_BANKING_BASICS@1` | source | `money-and-banking-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-MOTION_BASICS-A@1` | claim | `motion-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-MOTION_BASICS-A@1` | evidence_use | `motion-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-MOTION_BASICS@1` | scope | `motion-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-MOTION_BASICS@1` | source | `motion-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-OPTICS_BASICS-A@1` | claim | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-OPTICS_BASICS-B@1` | claim | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-OPTICS_BASICS-C@1` | claim | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-OPTICS_BASICS@1` | context | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-OPTICS_BASICS-A@1` | evidence_use | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-OPTICS_BASICS-B@1` | evidence_use | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-OPTICS_BASICS-C@1` | evidence_use | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-OPTICS_BASICS@1` | scope | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-OPTICS_BASICS@1` | source | `optics-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ORGANIC_CHEMISTRY_BASICS-A@2` | claim | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ORGANIC_CHEMISTRY_BASICS-B@2` | claim | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ORGANIC_CHEMISTRY_BASICS-C@2` | claim | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-ORGANIC_CHEMISTRY_BASICS@2` | context | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ORGANIC_CHEMISTRY_BASICS-A@2` | evidence_use | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ORGANIC_CHEMISTRY_BASICS-B@2` | evidence_use | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ORGANIC_CHEMISTRY_BASICS-C@2` | evidence_use | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-ORGANIC_CHEMISTRY_BASICS@2` | scope | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-ORGANIC_CHEMISTRY_BASICS@2` | source | `organic-chemistry-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ORGANIZATIONAL_BEHAVIOR_BASICS-A@1` | claim | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ORGANIZATIONAL_BEHAVIOR_BASICS-B@1` | claim | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ORGANIZATIONAL_BEHAVIOR_BASICS-C@1` | claim | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-ORGANIZATIONAL_BEHAVIOR_BASICS@1` | context | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ORGANIZATIONAL_BEHAVIOR_BASICS-A@1` | evidence_use | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ORGANIZATIONAL_BEHAVIOR_BASICS-B@1` | evidence_use | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-ORGANIZATIONAL_BEHAVIOR_BASICS-C@1` | evidence_use | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-ORGANIZATIONAL_BEHAVIOR_BASICS@1` | scope | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-ORGANIZATIONAL_BEHAVIOR_BASICS@1` | source | `organizational-behavior-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-PARASITOLOGY_BASICS@1` | source | `parasitology-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_PATHOLOGY_BASICS_A@1` | claim | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_PATHOLOGY_BASICS_B@1` | claim | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_PATHOLOGY_BASICS_C@1` | claim | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX_PATHOLOGY_BASICS@1` | context | `pathology-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP_PATHOLOGY_BASICS@1` | scope | `pathology-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_PATHOLOGY_BASICS@1` | source | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-PLANT_PATHOLOGY_BASICS-A@1` | claim | `plant-pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-PLANT_PATHOLOGY_BASICS-B@1` | claim | `plant-pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-PLANT_PATHOLOGY_BASICS-C@1` | claim | `plant-pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-PLANT_PATHOLOGY_BASICS@1` | context | `plant-pathology-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-PLANT_PATHOLOGY_BASICS@1` | scope | `plant-pathology-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-PLANT_PATHOLOGY_BASICS@1` | source | `plant-pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-POLITICAL_ECONOMY_BASICS-A@2` | claim | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-POLITICAL_ECONOMY_BASICS-B@2` | claim | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-POLITICAL_ECONOMY_BASICS-C@2` | claim | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-POLITICAL_ECONOMY_BASICS@2` | context | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-POLITICAL_ECONOMY_BASICS-A@2` | evidence_use | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-POLITICAL_ECONOMY_BASICS-B@2` | evidence_use | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-POLITICAL_ECONOMY_BASICS-C@2` | evidence_use | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-POLITICAL_ECONOMY_BASICS-INDEPENDENT-A@2` | evidence_use | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-POLITICAL_ECONOMY_BASICS-INDEPENDENT-B@2` | evidence_use | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-POLITICAL_ECONOMY_BASICS-INDEPENDENT-C@2` | evidence_use | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-POLITICAL_ECONOMY_BASICS@2` | scope | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-POLITICAL_ECONOMY_BASICS-INDEPENDENT@2` | source | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-POLITICAL_ECONOMY_BASICS@2` | source | `political-economy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-PUBLIC_ADMINISTRATION_BASICS-A@1` | claim | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-PUBLIC_ADMINISTRATION_BASICS-B@1` | claim | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-PUBLIC_ADMINISTRATION_BASICS-C@1` | claim | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-PUBLIC_ADMINISTRATION_BASICS@1` | context | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-PUBLIC_ADMINISTRATION_BASICS-A@1` | evidence_use | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-PUBLIC_ADMINISTRATION_BASICS-B@1` | evidence_use | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-PUBLIC_ADMINISTRATION_BASICS-C@1` | evidence_use | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-PUBLIC_ADMINISTRATION_BASICS@1` | scope | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-PUBLIC_ADMINISTRATION_BASICS@1` | source | `public-administration-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-PUBLIC_BUDGETING_BASICS-A@1` | claim | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-PUBLIC_BUDGETING_BASICS-B@1` | claim | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-PUBLIC_BUDGETING_BASICS-C@1` | claim | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-PUBLIC_BUDGETING_BASICS@1` | context | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-PUBLIC_BUDGETING_BASICS-A@1` | evidence_use | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-PUBLIC_BUDGETING_BASICS-B@1` | evidence_use | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-PUBLIC_BUDGETING_BASICS-C@1` | evidence_use | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-PUBLIC_BUDGETING_BASICS@1` | scope | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-PUBLIC_BUDGETING_BASICS@1` | source | `public-budgeting-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-RELIGIOUS_STUDIES-A@1` | claim | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-RELIGIOUS_STUDIES-B@1` | claim | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-RELIGIOUS_STUDIES-C@1` | claim | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-RELIGIOUS_STUDIES@1` | context | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-RELIGIOUS_STUDIES-A@1` | evidence_use | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-RELIGIOUS_STUDIES-B@1` | evidence_use | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-RELIGIOUS_STUDIES-C@1` | evidence_use | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-RELIGIOUS_STUDIES@1` | scope | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-RELIGIOUS_STUDIES@1` | source | `religious-studies-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-REMOTE_SENSING_BASICS-A@1` | claim | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-REMOTE_SENSING_BASICS-B@1` | claim | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-REMOTE_SENSING_BASICS-C@1` | claim | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-REMOTE_SENSING_BASICS@1` | context | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-REMOTE_SENSING_BASICS-A@1` | evidence_use | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-REMOTE_SENSING_BASICS-B@1` | evidence_use | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-REMOTE_SENSING_BASICS-C@1` | evidence_use | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-REMOTE_SENSING_BASICS@1` | scope | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-REMOTE_SENSING_BASICS@1` | source | `remote-sensing-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SETTLEMENT_GEOGRAPHY-A@1` | claim | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SETTLEMENT_GEOGRAPHY-B@1` | claim | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SETTLEMENT_GEOGRAPHY-C@1` | claim | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-SETTLEMENT_GEOGRAPHY@1` | context | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SETTLEMENT_GEOGRAPHY-A@1` | evidence_use | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SETTLEMENT_GEOGRAPHY-B@1` | evidence_use | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SETTLEMENT_GEOGRAPHY-C@1` | evidence_use | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-SETTLEMENT_GEOGRAPHY@1` | scope | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-SETTLEMENT_GEOGRAPHY@1` | source | `settlement-geography-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SI-DERIVED@1` | claim | `si-units-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-SI-SEVEN-BASE@1` | claim | `si-units-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-SI@1` | context | `si-units-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-SI-DERIVED@2` | evidence_use | `si-units-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-SI-SEVEN-BASE@2` | evidence_use | `si-units-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-SI@1` | scope | `si-units-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-SOCIAL_POLICY_BASICS-A@2` | claim | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOCIAL_POLICY_BASICS-B@2` | claim | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOCIAL_POLICY_BASICS-C@2` | claim | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-SOCIAL_POLICY_BASICS@2` | context | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_POLICY_BASICS-A@2` | evidence_use | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_POLICY_BASICS-B@2` | evidence_use | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_POLICY_BASICS-C@2` | evidence_use | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_POLICY_BASICS-INDEPENDENT-A@2` | evidence_use | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_POLICY_BASICS-INDEPENDENT-B@2` | evidence_use | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_POLICY_BASICS-INDEPENDENT-C@2` | evidence_use | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-SOCIAL_POLICY_BASICS@2` | scope | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-SOCIAL_POLICY_BASICS-INDEPENDENT@2` | source | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-SOCIAL_POLICY_BASICS@2` | source | `social-policy-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOCIAL_STATISTICS_BASICS-A@1` | claim | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOCIAL_STATISTICS_BASICS-B@1` | claim | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOCIAL_STATISTICS_BASICS-C@1` | claim | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-SOCIAL_STATISTICS_BASICS@1` | context | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_STATISTICS_BASICS-A@1` | evidence_use | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_STATISTICS_BASICS-B@1` | evidence_use | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIAL_STATISTICS_BASICS-C@1` | evidence_use | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-SOCIAL_STATISTICS_BASICS@1` | scope | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-SOCIAL_STATISTICS_BASICS@1` | source | `social-statistics-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOCIOLOGY_BASICS-A@1` | claim | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOCIOLOGY_BASICS-B@1` | claim | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOCIOLOGY_BASICS-C@1` | claim | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-SOCIOLOGY_BASICS@1` | context | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIOLOGY_BASICS-A@1` | evidence_use | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIOLOGY_BASICS-B@1` | evidence_use | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOCIOLOGY_BASICS-C@1` | evidence_use | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-SOCIOLOGY_BASICS@1` | scope | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-SOCIOLOGY_BASICS@1` | source | `sociology-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOFTWARE_ENGINEERING_BASICS-A@2` | claim | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOFTWARE_ENGINEERING_BASICS-B@2` | claim | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOFTWARE_ENGINEERING_BASICS-C@2` | claim | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-SOFTWARE_ENGINEERING_BASICS@2` | context | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOFTWARE_ENGINEERING_BASICS-A@2` | evidence_use | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOFTWARE_ENGINEERING_BASICS-B@2` | evidence_use | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOFTWARE_ENGINEERING_BASICS-C@2` | evidence_use | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-SOFTWARE_ENGINEERING_BASICS@2` | scope | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-SOFTWARE_ENGINEERING_BASICS@2` | source | `software-engineering-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOIL_MICROBIOLOGY_BASICS-A@1` | claim | `soil-microbiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-SOIL_MICROBIOLOGY_BASICS-B@1` | claim | `soil-microbiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-SOIL_MICROBIOLOGY_BASICS-C@1` | claim | `soil-microbiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-SOIL_MICROBIOLOGY_BASICS@1` | source | `soil-microbiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_SOIL_SCIENCE_BASICS_A@1` | claim | `soil-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_SOIL_SCIENCE_BASICS_B@1` | claim | `soil-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_SOIL_SCIENCE_BASICS_C@1` | claim | `soil-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_SOIL_SCIENCE_BASICS@1` | source | `soil-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-SOLAR_SYSTEM_BASICS-A@1` | claim | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOLAR_SYSTEM_BASICS-B@1` | claim | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-SOLAR_SYSTEM_BASICS-C@1` | claim | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-SOLAR_SYSTEM_BASICS@1` | context | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOLAR_SYSTEM_BASICS-A@1` | evidence_use | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOLAR_SYSTEM_BASICS-B@1` | evidence_use | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-SOLAR_SYSTEM_BASICS-C@1` | evidence_use | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-SOLAR_SYSTEM_BASICS@1` | scope | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-SOLAR_SYSTEM_BASICS@1` | source | `solar-system-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-STATISTICS_BASICS-A@1` | claim | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-STATISTICS_BASICS-A@1` | evidence_use | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-STATISTICS_BASICS-OPENSTAX@1` | evidence_use | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-STATISTICS_BASICS@1` | source | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-TAXATION_BASICS-A@2` | claim | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-TAXATION_BASICS-B@2` | claim | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-TAXATION_BASICS-C@2` | claim | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-TAXATION_BASICS@2` | context | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TAXATION_BASICS-A@2` | evidence_use | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TAXATION_BASICS-B@2` | evidence_use | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TAXATION_BASICS-C@2` | evidence_use | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TAXATION_BASICS-INDEPENDENT-A@2` | evidence_use | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TAXATION_BASICS-INDEPENDENT-B@2` | evidence_use | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TAXATION_BASICS-INDEPENDENT-C@2` | evidence_use | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-TAXATION_BASICS@2` | scope | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-TAXATION_BASICS-INDEPENDENT@2` | source | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-TAXATION_BASICS@2` | source | `taxation-basics` | HOLD | canonical_json_verified_snapshot | FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-TEMPERATURE_BASICS-A@1` | claim | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-TEMPERATURE_BASICS-B@1` | claim | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-TEMPERATURE_BASICS-C@1` | claim | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-TEMPERATURE_BASICS@1` | context | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TEMPERATURE_BASICS-A@1` | evidence_use | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TEMPERATURE_BASICS-B@1` | evidence_use | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-TEMPERATURE_BASICS-C@1` | evidence_use | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-TEMPERATURE_BASICS@1` | scope | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-TEMPERATURE_BASICS@1` | source | `temperature-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-THERMODYNAMICS_BASICS-A@1` | claim | `thermodynamics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-THERMODYNAMICS_BASICS-A@1` | evidence_use | `thermodynamics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-THERMODYNAMICS_BASICS@1` | source | `thermodynamics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-UNITS_AND_MEASUREMENT-A@1` | claim | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-UNITS_AND_MEASUREMENT-B@1` | claim | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-UNITS_AND_MEASUREMENT-C@1` | claim | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-UNITS_AND_MEASUREMENT@1` | context | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-UNITS_AND_MEASUREMENT-A@1` | evidence_use | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-UNITS_AND_MEASUREMENT-B@1` | evidence_use | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-UNITS_AND_MEASUREMENT-C@1` | evidence_use | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-UNITS_AND_MEASUREMENT@1` | scope | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-UNITS_AND_MEASUREMENT@1` | source | `units-and-measurement` | HOLD | base_register_reference+canonical_json_snapshot | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md; FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-VACCINATION_INFORMATION_BASICS@1` | source | `vaccination-information-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-VIROLOGY_BASICS@1` | source | `virology-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_WATER_QUALITY_BASICS_A@1` | claim | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_WATER_QUALITY_BASICS_B@1` | claim | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_WATER_QUALITY_BASICS_C@1` | claim | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_WATER_QUALITY_WHO_A@1` | claim | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX_WATER_QUALITY_BASICS@1` | context | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_WATER_QUALITY_BASICS_A@1` | evidence_use | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_WATER_QUALITY_WHO_A@1` | evidence_use | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_WATER_QUALITY_BASICS-B@1` | evidence_use | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM_WATER_QUALITY_BASICS_B@1; canonical file EU-WATER_QUALITY_BASICS-B.json |
| `EU_WATER_QUALITY_BASICS-C@1` | evidence_use | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM_WATER_QUALITY_BASICS_C@1; canonical file EU-WATER_QUALITY_BASICS-C.json |
| `SCP_WATER_QUALITY_BASICS@1` | scope | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_WATER_QUALITY_WHO@1` | source | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_WATER_QUALITY_BASICS@1` | source | `water-quality-basics` | HOLD | canonical_json_dependency_verified_hold (canonical ID corrected from base register token) | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM_WATER_RESOURCE_MANAGEMENT_BASICS_A@1` | claim | `water-resource-management-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX_WATER_RESOURCE_MANAGEMENT_BASICS@1` | context | `water-resource-management-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU_WATER_RESOURCE_MANAGEMENT_BASICS_A@1` | evidence_use | `water-resource-management-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP_WATER_RESOURCE_MANAGEMENT_BASICS@1` | scope | `water-resource-management-basics` | HOLD | canonical_json_verified_current_head_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC_WATER_RESOURCE_MANAGEMENT_BASICS@1` | source | `water-resource-management-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-WATER_SECURITY-A@1` | claim | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-WATER_SECURITY-B@1` | claim | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CLM-WATER_SECURITY-C@1` | claim | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `CTX-WATER_SECURITY@1` | context | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-WATER_SECURITY-A@1` | evidence_use | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SCP-WATER_SECURITY@1` | scope | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `SRC-WATER_SECURITY@1` | source | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md |
| `EU-EPA-WATER-SECURITY-B@1` | evidence_use | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-WATER_SECURITY-B@1; canonical file EU-EPA-WATER-SECURITY-B.json |
| `EU-WATER_SECURITY-B@1` | evidence_use | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-WATER_SECURITY-B@1; canonical file EU-WATER_SECURITY-B.json |
| `EU-WATER_SECURITY-C@1` | evidence_use | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via CLM-WATER_SECURITY-C@1; canonical file EU-WATER_SECURITY-C.json |
| `SRC-EPA-WATER-SECURITY@1` | source | `water-security-basics` | HOLD | canonical_json_dependency_verified_hold | canonical dependency discovered via EU-EPA-WATER-SECURITY-B@1; canonical file SRC-EPA-WATER-SECURITY.json |
| `CLM-WAVES_AND_SOUND_BASICS-A@1` | claim | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-WAVES_AND_SOUND_BASICS-B@1` | claim | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-WAVES_AND_SOUND_BASICS-C@1` | claim | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CTX-WAVES_AND_SOUND_BASICS@1` | context | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-WAVES_AND_SOUND_BASICS-A@1` | evidence_use | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-WAVES_AND_SOUND_BASICS-B@1` | evidence_use | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `EU-WAVES_AND_SOUND_BASICS-C@1` | evidence_use | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SCP-WAVES_AND_SOUND_BASICS@1` | scope | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `SRC-WAVES_AND_SOUND_BASICS@1` | source | `waves-and-sound-basics` | HOLD | canonical_json_snapshot | FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md |
| `CLM-ACID_BASE_BASICS-A@1` | claim | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `CLM-ACID_BASE_BASICS-B@1` | claim | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `CLM-ACID_BASE_BASICS-C@1` | claim | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `CTX-ACID_BASE_BASICS@1` | context | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `EU-ACID-BASE-IUPAC-CORROBORATION@1` | evidence_use | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `EU-ACID_BASE_BASICS-A@2` | evidence_use | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `EU-ACID_BASE_BASICS-B@2` | evidence_use | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `EU-ACID_BASE_BASICS-C@2` | evidence_use | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `SCP-ACID_BASE_BASICS@1` | scope | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `SRC-ACID_BASE_BASICS@1` | source | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `SRC-IUPAC-PH-2025@1` | source | `acid-base-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `CLM-ALGEBRA_BASICS-A@1` | claim | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CLM-ALGEBRA_BASICS-B@1` | claim | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CLM-ALGEBRA_BASICS-C@1` | claim | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CTX-ALGEBRA_BASICS@1` | context | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-ALGEBRA-UMN-CORROBORATION@1` | evidence_use | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-ALGEBRA_BASICS-A@1` | evidence_use | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-ALGEBRA_BASICS-B@1` | evidence_use | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-ALGEBRA_BASICS-C@1` | evidence_use | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SCP-ALGEBRA_BASICS@1` | scope | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SRC-ALGEBRA_BASICS@1` | source | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SRC-UMN-OPEN-ALGEBRA@1` | source | `algebra-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CLM-ANALYTICAL_CHEMISTRY_BASICS-A@1` | claim | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `CLM-ANALYTICAL_CHEMISTRY_BASICS-B@1` | claim | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `CLM-ANALYTICAL_CHEMISTRY_BASICS-C@1` | claim | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `CTX-ANALYTICAL_CHEMISTRY_BASICS@1` | context | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `EU-ANALYTICAL-CHEMISTRY-IUPAC-CORROBORATION@1` | evidence_use | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `EU-ANALYTICAL_CHEMISTRY_BASICS-A@1` | evidence_use | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `EU-ANALYTICAL_CHEMISTRY_BASICS-B@1` | evidence_use | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `EU-ANALYTICAL_CHEMISTRY_BASICS-C@1` | evidence_use | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `SCP-ANALYTICAL_CHEMISTRY_BASICS@1` | scope | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `SRC-ANALYTICAL_CHEMISTRY_BASICS@1` | source | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `SRC-IUPAC-ANALYTICAL-CHEMISTRY-2025@1` | source | `analytical-chemistry-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md |
| `CLM-ASTRONOMY_OBSERVATION_BASICS-A@1` | claim | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `CLM-ASTRONOMY_OBSERVATION_BASICS-B@1` | claim | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `CLM-ASTRONOMY_OBSERVATION_BASICS-C@1` | claim | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `CTX-ASTRONOMY_OBSERVATION_BASICS@1` | context | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `EU-ASTRONOMY_OBSERVATION_BASICS-A@1` | evidence_use | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `EU-ASTRONOMY_OBSERVATION_BASICS-B@1` | evidence_use | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `EU-ASTRONOMY_OBSERVATION_BASICS-C@1` | evidence_use | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `SCP-ASTRONOMY_OBSERVATION_BASICS@1` | scope | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `SRC-ASTRONOMY_OBSERVATION_BASICS@1` | source | `astronomy-observation-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md |
| `CLM-EARTH_SYSTEM_BASICS-A@1` | claim | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `CLM-EARTH_SYSTEM_BASICS-B@1` | claim | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `CLM-EARTH_SYSTEM_BASICS-C@1` | claim | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `CTX-EARTH_SYSTEM_BASICS@1` | context | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `EU-EARTH_SYSTEM_BASICS-A@1` | evidence_use | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `EU-EARTH_SYSTEM_BASICS-B@1` | evidence_use | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `EU-EARTH_SYSTEM_BASICS-C@1` | evidence_use | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `SCP-EARTH_SYSTEM_BASICS@1` | scope | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `SRC-EARTH_SYSTEM_BASICS@1` | source | `earth-system-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `CLM-MATTER_BASICS-A@1` | claim | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `CLM-MATTER_BASICS-B@1` | claim | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `CLM-MATTER_BASICS-C@1` | claim | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `CTX-MATTER_BASICS@1` | context | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `EU-MATTER_BASICS-A@1` | evidence_use | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `EU-MATTER_BASICS-B@1` | evidence_use | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `EU-MATTER_BASICS-C@1` | evidence_use | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `SCP-MATTER_BASICS@1` | scope | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `SRC-MATTER_BASICS@1` | source | `matter-basics` | HOLD | canonical_json_screened_batch1 | FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md |
| `CLM-OCEANOGRAPHY_BASICS-A@1` | claim | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `CLM-OCEANOGRAPHY_BASICS-B@1` | claim | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `CLM-OCEANOGRAPHY_BASICS-C@1` | claim | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `CTX-OCEANOGRAPHY_BASICS@1` | context | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `EU-OCEANOGRAPHY_BASICS-A@1` | evidence_use | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `EU-OCEANOGRAPHY_BASICS-B@1` | evidence_use | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `EU-OCEANOGRAPHY_BASICS-C@1` | evidence_use | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `SCP-OCEANOGRAPHY_BASICS@1` | scope | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `SRC-OCEANOGRAPHY_BASICS@1` | source | `oceanography-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md |
| `CLM-PROBABILITY_BASICS-A@1` | claim | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CLM-PROBABILITY_BASICS-B@1` | claim | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CLM-PROBABILITY_BASICS-MODEL@1` | claim | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CTX-PROBABILITY_BASICS@1` | context | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-PROBABILITY_BASICS-A@1` | evidence_use | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-PROBABILITY_BASICS-B@1` | evidence_use | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-PROBABILITY_BASICS-MODEL@1` | evidence_use | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SCP-PROBABILITY_BASICS@1` | scope | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SRC-OPENSTAX-PROBABILITY@1` | source | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SRC-PROBABILITY_BASICS@1` | source | `probability-basics` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CLM-RATIOS_AND_PERCENTAGES-A@1` | claim | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CLM-RATIOS_AND_PERCENTAGES-B@1` | claim | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CLM-RATIOS_AND_PERCENTAGES-CONTEXT@1` | claim | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `CTX-RATIOS_AND_PERCENTAGES@1` | context | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-RATIOS_AND_PERCENTAGES-A@1` | evidence_use | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-RATIOS_AND_PERCENTAGES-B@1` | evidence_use | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `EU-RATIOS_AND_PERCENTAGES-CONTEXT@1` | evidence_use | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SCP-RATIOS_AND_PERCENTAGES@1` | scope | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SRC-OPENSTAX-RATIOS-PERCENT@1` | source | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |
| `SRC-RATIOS_AND_PERCENTAGES@1` | source | `ratios-and-percentages` | HOLD | prior_screen_reused_current_json_reconciled | DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md |

## Current-head verification update

The R9 99-row register has now been re-read against canonical JSON at this exact master inspection HEAD; all 99 record IDs, versions and types match. All remain HOLD pending substantive and release review.
| `SRC-CYBERSECURITY_BASICS@2` | source | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `CLM-CYBERSECURITY_BASICS-A@2` | claim | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `CLM-CYBERSECURITY_BASICS-B@2` | claim | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `CLM-CYBERSECURITY_BASICS-C@2` | claim | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `EU-CYBERSECURITY_BASICS-A@2` | evidence_use | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `EU-CYBERSECURITY_BASICS-B@2` | evidence_use | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `EU-CYBERSECURITY_BASICS-C@2` | evidence_use | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `CTX-CYBERSECURITY_BASICS@2` | context | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `SCP-CYBERSECURITY_BASICS@2` | scope | `cybersecurity-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md |
| `SRC-PSYCHOLOGY_BASICS@2` | source | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-PSYCHOLOGY_BASICS-A@2` | claim | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-PSYCHOLOGY_BASICS-B@2` | claim | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-PSYCHOLOGY_BASICS-C@2` | claim | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-PSYCHOLOGY_BASICS-A@2` | evidence_use | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-PSYCHOLOGY_BASICS-B@2` | evidence_use | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-PSYCHOLOGY_BASICS-C@2` | evidence_use | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CTX-PSYCHOLOGY_BASICS@2` | context | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `SCP-PSYCHOLOGY_BASICS@2` | scope | `psychology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `SRC-NEUROSCIENCE_BASICS@2` | source | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-NEUROSCIENCE_BASICS-A@2` | claim | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-NEUROSCIENCE_BASICS-B@2` | claim | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-NEUROSCIENCE_BASICS-C@2` | claim | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-NEUROSCIENCE_BASICS-A@2` | evidence_use | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-NEUROSCIENCE_BASICS-B@2` | evidence_use | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-NEUROSCIENCE_BASICS-C@2` | evidence_use | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CTX-NEUROSCIENCE_BASICS@2` | context | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `SCP-NEUROSCIENCE_BASICS@2` | scope | `neuroscience-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `SRC-DEVELOPMENTAL_BIOLOGY_BASICS@2` | source | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-A@2` | claim | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-B@2` | claim | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CLM-DEVELOPMENTAL_BIOLOGY_BASICS-C@2` | claim | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-DEVELOPMENTAL_BIOLOGY_BASICS-A@2` | evidence_use | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-DEVELOPMENTAL_BIOLOGY_BASICS-B@2` | evidence_use | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `EU-DEVELOPMENTAL_BIOLOGY_BASICS-C@2` | evidence_use | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `CTX-DEVELOPMENTAL_BIOLOGY_BASICS@2` | context | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `SCP-DEVELOPMENTAL_BIOLOGY_BASICS@2` | scope | `developmental-biology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md |
| `SRC-LEARNING_BASICS@1` | source | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-LEARNING_BASICS-A@1` | claim | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-LEARNING_BASICS-B@1` | claim | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-LEARNING_BASICS-C@1` | claim | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-LEARNING_BASICS-A@1` | evidence_use | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-LEARNING_BASICS-B@1` | evidence_use | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-LEARNING_BASICS-C@1` | evidence_use | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CTX-LEARNING_BASICS@1` | context | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SCP-LEARNING_BASICS@1` | scope | `learning-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SRC-ECONOMICS_BASICS@1` | source | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `CLM-ECONOMICS_BASICS-A@1` | claim | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `CLM-ECONOMICS_BASICS-B@1` | claim | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `CLM-ECONOMICS_BASICS-C@1` | claim | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `EU-ECONOMICS_BASICS-A@1` | evidence_use | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `EU-ECONOMICS_BASICS-B@1` | evidence_use | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `EU-ECONOMICS_BASICS-C@1` | evidence_use | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `CTX-ECONOMICS_BASICS@1` | context | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `SCP-ECONOMICS_BASICS@1` | scope | `economics-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md |
| `SRC-CHRONOLOGY_METHODS@1` | source | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-CHRONOLOGY_METHODS-A@1` | claim | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-CHRONOLOGY_METHODS-B@1` | claim | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-CHRONOLOGY_METHODS-C@1` | claim | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-CHRONOLOGY_METHODS-A@1` | evidence_use | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-CHRONOLOGY_METHODS-B@1` | evidence_use | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-CHRONOLOGY_METHODS-C@1` | evidence_use | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CTX-CHRONOLOGY_METHODS@1` | context | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SCP-CHRONOLOGY_METHODS@1` | scope | `chronology-methods` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SRC-ARCHAEOLOGY_BASICS@1` | source | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-ARCHAEOLOGY_BASICS-A@1` | claim | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-ARCHAEOLOGY_BASICS-B@1` | claim | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-ARCHAEOLOGY_BASICS-C@1` | claim | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-ARCHAEOLOGY_BASICS-A@1` | evidence_use | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-ARCHAEOLOGY_BASICS-B@1` | evidence_use | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-ARCHAEOLOGY_BASICS-C@1` | evidence_use | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CTX-ARCHAEOLOGY_BASICS@1` | context | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SCP-ARCHAEOLOGY_BASICS@1` | scope | `archaeology-basics` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SRC-WRITING_SYSTEMS@1` | source | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-WRITING_SYSTEMS-A@1` | claim | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-WRITING_SYSTEMS-B@1` | claim | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-WRITING_SYSTEMS-C@1` | claim | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-WRITING_SYSTEMS-A@1` | evidence_use | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-WRITING_SYSTEMS-B@1` | evidence_use | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-WRITING_SYSTEMS-C@1` | evidence_use | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CTX-WRITING_SYSTEMS@1` | context | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SCP-WRITING_SYSTEMS@1` | scope | `writing-systems` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SRC-TRADE_NETWORKS@1` | source | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-TRADE_NETWORKS-A@1` | claim | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-TRADE_NETWORKS-B@1` | claim | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-TRADE_NETWORKS-C@1` | claim | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-TRADE_NETWORKS-A@1` | evidence_use | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-TRADE_NETWORKS-B@1` | evidence_use | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-TRADE_NETWORKS-C@1` | evidence_use | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CTX-TRADE_NETWORKS@1` | context | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SCP-TRADE_NETWORKS@1` | scope | `trade-networks` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SRC-STATE_FORMATION@1` | source | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-STATE_FORMATION-A@1` | claim | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-STATE_FORMATION-B@1` | claim | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CLM-STATE_FORMATION-C@1` | claim | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-STATE_FORMATION-A@1` | evidence_use | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-STATE_FORMATION-B@1` | evidence_use | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `EU-STATE_FORMATION-C@1` | evidence_use | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `CTX-STATE_FORMATION@1` | context | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |
| `SCP-STATE_FORMATION@1` | scope | `state-formation` | HOLD | prior_screen_reused_current_json_verified | DOMAIN-EXPANSION-AUDIT-2026-09-30.md |

| `CLM-ANTIMICROBIAL_RESISTANCE_BASICS-C@1` | claim | `antimicrobial-resistance-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CROSS-SLICE-RELATION-DEPENDENCY-INVENTORY-2026-11-19.md |
| `CLM-STATISTICS_BASICS-C@1` | claim | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-CROSS-SLICE-RELATION-DEPENDENCY-INVENTORY-2026-11-19.md |

## Current-head relation closure

At the master inspection HEAD, all 126 Relation participant references have exact canonical ID/version/type matches. This comprises 29 candidate-set references (25 unique Claims) and 97 other-slice references (82 unique records: 79 Claims, one Event, two States). The two candidate Claims missing from the earlier master were added as HOLD. The shared frame Context is valid. No Relation or participant canonical JSON changed during this reconciliation. Relation semantics, role compatibility, directionality, rights, editorial ownership and Human View remain open; no Relation is approved.
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-A@1` | claim | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-B@1` | claim | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-ANCIENT_CIVILIZATIONS_BASICS-C@1` | claim | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CTX-ANCIENT_CIVILIZATIONS_BASICS@1` | context | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ANCIENT-CIVILIZATIONS-SMITHSONIAN@1` | evidence_use | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ANCIENT_CIVILIZATIONS_BASICS-A@1` | evidence_use | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ANCIENT_CIVILIZATIONS_BASICS-B@1` | evidence_use | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ANCIENT_CIVILIZATIONS_BASICS-C@1` | evidence_use | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SCP-ANCIENT_CIVILIZATIONS_BASICS@1` | scope | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SRC-ANCIENT_CIVILIZATIONS_BASICS@1` | source | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SRC-SMITHSONIAN-ANCIENT-AGRICULTURE@1` | source | `ancient-civilizations-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-ANTHROPOLOGY_BASICS-A@1` | claim | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-ANTHROPOLOGY_BASICS-B@1` | claim | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-ANTHROPOLOGY_BASICS-C@1` | claim | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CTX-ANTHROPOLOGY_BASICS@1` | context | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ANTHROPOLOGY_BASICS-A@1` | evidence_use | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ANTHROPOLOGY_BASICS-B@1` | evidence_use | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ANTHROPOLOGY_BASICS-C@1` | evidence_use | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SCP-ANTHROPOLOGY_BASICS@1` | scope | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SRC-ANTHROPOLOGY_BASICS@1` | source | `anthropology-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-ETHICS_BASICS-A@1` | claim | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-ETHICS_BASICS-B@1` | claim | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-ETHICS_BASICS-C@1` | claim | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CTX-ETHICS_BASICS@1` | context | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ETHICS_BASICS-A@1` | evidence_use | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ETHICS_BASICS-B@1` | evidence_use | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-ETHICS_BASICS-C@1` | evidence_use | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SCP-ETHICS_BASICS@1` | scope | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SRC-ETHICS_BASICS@1` | source | `ethics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-LINGUISTICS_BASICS-A@1` | claim | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-LINGUISTICS_BASICS-B@1` | claim | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-LINGUISTICS_BASICS-C@1` | claim | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CTX-LINGUISTICS_BASICS@1` | context | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-LINGUISTICS_BASICS-A@1` | evidence_use | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-LINGUISTICS_BASICS-B@1` | evidence_use | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-LINGUISTICS_BASICS-C@1` | evidence_use | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SCP-LINGUISTICS_BASICS@1` | scope | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SRC-LINGUISTICS_BASICS@1` | source | `linguistics-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-PHILOSOPHY_BASICS-A@1` | claim | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-PHILOSOPHY_BASICS-B@1` | claim | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CLM-PHILOSOPHY_BASICS-C@1` | claim | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `CTX-PHILOSOPHY_BASICS@1` | context | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-PHILOSOPHY_BASICS-A@1` | evidence_use | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-PHILOSOPHY_BASICS-B@1` | evidence_use | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `EU-PHILOSOPHY_BASICS-C@1` | evidence_use | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SCP-PHILOSOPHY_BASICS@1` | scope | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |
| `SRC-PHILOSOPHY_BASICS@1` | source | `philosophy-basics` | HOLD | canonical_json_screened_batch2 | FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md |

| `EU-BIODIVERSITY_BASICS-B@1` | evidence_use | `biodiversity-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU-BIODIVERSITY_BASICS-C@1` | evidence_use | `biodiversity-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU-CONSERVATION_BIOLOGY_BASICS-A@1` | evidence_use | `conservation-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU-CONSERVATION_BIOLOGY_BASICS-B@1` | evidence_use | `conservation-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU-CONSERVATION_BIOLOGY_BASICS-C@1` | evidence_use | `conservation-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU-ECOTOXICOLOGY_BASICS-A@1` | evidence_use | `ecotoxicology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU-ENTOMOLOGY_BASICS-A@1` | evidence_use | `entomology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU_MARINE_BIOLOGY_BASICS_A@1` | evidence_use | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU_PATHOLOGY_BASICS_A@1` | evidence_use | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |
| `EU-PLANT_PATHOLOGY_BASICS-A@1` | evidence_use | `plant-pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md |

## Claim dependency closure — batch 1

At the inspection HEAD, 19 Claim → Evidence Use → Source chains were re-fetched. All Claim IDs/versions/types, EU Claim/Source references, and Source IDs/versions/types match. Ten Evidence Use dependency records absent from the prior master were added; 43 existing records had their verification status advanced from identity-only to dependency-verified. All 19 Claims remain HOLD because no Evidence Use has a claim-specific locator and substantive source-fit/rights review remains open. See `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH1-2026-11-19.md`.

| `EU-ECOTOXICOLOGY_BASICS-B@1` | evidence_use | `ecotoxicology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU-ECOTOXICOLOGY_BASICS-C@1` | evidence_use | `ecotoxicology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU-ENTOMOLOGY_BASICS-B@1` | evidence_use | `entomology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU-ENTOMOLOGY_BASICS-C@1` | evidence_use | `entomology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU_MARINE_BIOLOGY_BASICS_B@1` | evidence_use | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU_MARINE_BIOLOGY_BASICS_C@1` | evidence_use | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU_PATHOLOGY_BASICS_B@1` | evidence_use | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU_PATHOLOGY_BASICS_C@1` | evidence_use | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU-PLANT_PATHOLOGY_BASICS-B@1` | evidence_use | `plant-pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |
| `EU-PLANT_PATHOLOGY_BASICS-C@1` | evidence_use | `plant-pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md |

## Claim dependency closure — batch 2

Batch 2 adds 10 exact Claim → Evidence Use edges across ecotoxicology, entomology, marine biology, pathology and plant pathology. All Claim and EU IDs, versions, types and Source references match. Ten previously absent Evidence Use dependencies were added to the master. All ten Claims remain HOLD because claim-specific evidence locators are absent and substantive source-fit review is open. See `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH2-2026-11-19.md`. Cumulative closure: 29/40 identity-only Claims; 11 remain.

| `SRC-NIST-SI-UNITS@1` | source | `si-units-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH3-2026-11-19.md |
| `EU-SOIL_MICROBIOLOGY_BASICS-A@1` | evidence_use | `soil-microbiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH3-2026-11-19.md |
| `EU-SOIL_MICROBIOLOGY_BASICS-B@1` | evidence_use | `soil-microbiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH3-2026-11-19.md |
| `EU-SOIL_MICROBIOLOGY_BASICS-C@1` | evidence_use | `soil-microbiology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH3-2026-11-19.md |
| `EU_SOIL_SCIENCE_BASICS_A@1` | evidence_use | `soil-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH3-2026-11-19.md |
| `EU_SOIL_SCIENCE_BASICS_B@1` | evidence_use | `soil-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH3-2026-11-19.md |
| `EU_SOIL_SCIENCE_BASICS_C@1` | evidence_use | `soil-science-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH3-2026-11-19.md |

## Claim dependency closure — batch 3

Batch 3 closes the final 11/40 Claims previously marked identity-only. Their Claim IDs/versions/types, EU references and Source references match. Seven previously absent dependencies were added to the master; the two SI Evidence Use targets are correctly version 2 and were not downgraded. All 11 Claims remain HOLD because claim-specific locators are absent. See `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH3-2026-11-19.md`.

Cumulative result across Batches 1–3: 40/40 identity-only Claims have exact Claim → Evidence Use → Source identity/version/type closure. This is not evidence sufficiency or full Part II dependency closure.

| `SRC-OPENSTAX-STATISTICS-BASICS@1` | source | `statistics-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-PART-II-BASE-REGISTER-IDENTITY-TAIL-RECONCILIATION-2026-11-19.md |

## Base-register identity tail — closed

All 24 remaining identity-only rows were re-fetched at the inspection HEAD: 11 dependency-chain nodes were advanced to dependency-verified HOLD and 13 Context/Scope/Source records to current-head identity-verified HOLD. One additional dependency Source, `SRC-OPENSTAX-STATISTICS-BASICS@1`, was discovered through `EU-STATISTICS_BASICS-OPENSTAX@1` and added. No identity-only rows remain in the base-register tail. See `FIRST-EDITION-PART-II-BASE-REGISTER-IDENTITY-TAIL-RECONCILIATION-2026-11-19.md`.

## Claim dependency closure — batch 4

Batch 4 closes 15 Claims across accounting, administrative law, archival science, artificial intelligence and biochemistry. All 15 Claim IDs/versions/types and 18 Evidence Use edges match their exact canonical Claim/Source versions; seven Source records were re-fetched. Fifteen of 18 EUs contain pinpoints; the three accounting EUs do not. Administrative law is U.S.-jurisdiction-specific; archival SAA guidance is preliminary; IFRS rights and OpenStax attribution still require review. All 15 Claims remain HOLD. See `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH4-2026-11-19.md`.

## Claim dependency closure — batch 5

Batch 5 closes 15 Claims across calculus, chemical reactions, climate science, computer networks and algorithms. All 15 Claim/EU/Source chains match exact canonical IDs, versions and types. Six of 15 EUs have direct locators; climate science and computer networks contain generic placeholder Claims that require substantive rewrite, and calculus needs precise locators. All 15 Claims remain HOLD. See `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH5-2026-11-19.md`.

## Claim dependency closure — batch 6

Batch 6 closes 15 Claims and 21 Evidence Use edges across civil society, comparative civilizations, comparative law, democratic institutions and demography. All exact ID/version/type references match. Six EUs have locators (the comparative-law group); the remaining 15 lack pinpoints. Civil-society and comparative-civilizations source identity/fit remain weak; demographic and democratic-institution sources need precise tables/sections. All Claims remain HOLD. See `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH6-2026-11-19.md`.

## Claim dependency closure — batch 7

Batch 7 closes 15 Claims and 15 Evidence Use edges across cultural anthropology, cultural heritage, databases, distributed systems and education systems. All exact ID/version/type references match. Nine EUs have direct locators; education and cultural anthropology still lack pinpoints. UNESCO treaty text, PostgreSQL documentation and the distributed-systems paper provide the strongest chains in this batch. All Claims remain HOLD. See `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH7-2026-11-19.md`.

## Claim dependency closure — batch 8

Batch 8 closes 15 Claims and 15 Evidence Use edges across electromagnetism, fluid mechanics, geometry, governance and historical geography. All exact ID/version/type references match. No EU has a pinpoint. Six electromagnetism/fluid-mechanics Claims are generic placeholders; geometry has a source-fit mismatch; governance and historical geography need direct locators. All Claims remain HOLD. See `FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH8-2026-11-19.md`.

## 5. Current remaining integrity work — reconciled at PR head 49944b5dfeb3af912091440b10243321ad558824

The earlier numbered checklist below this heading was superseded by the completed Batch 1/2 screens, the base-register identity-tail reconciliation, the Relation endpoint closure, and Claim dependency batches 8–9. The current work state is:

1. **Base-register identity tail — CLOSED.** The final 24 identity-only rows were re-fetched at the pinned inspection HEAD; 24/24 exact ID/version/type matches. Eleven rows were advanced to dependency-verified HOLD, thirteen Context/Scope/Source rows to current-head identity-verified HOLD, and one previously omitted dependency Source was added. Zero identity-only rows remain. See `FIRST-EDITION-PART-II-BASE-REGISTER-IDENTITY-TAIL-RECONCILIATION-2026-11-19.md`. The original 197 raw references remain represented in the consolidated lineage; do not restart the old 197-row task as a fresh batch.
2. **International Law v2 — SUBSTANTIVE RE-REVIEW COMPLETE; REMEDIATION OPEN.** All 13 current v2 records were re-fetched and reviewed at `50d37a3`; 13/13 identity/version/type and 9/9 Claim→EU→Source edges match. Three primary locators were checked. The audit found Claim B/C scope wording to narrow, independent EU B only partially relevant and independent EU C mismatched to Claim C, while Context/Scope target Claim A only. All 13 remain HOLD; see `FIRST-EDITION-INTERNATIONAL-LAW-V2-SUBSTANTIVE-DEPENDENCY-REREVIEW-2026-11-19.md`. No canonical edits authorized.\n2. **Claim dependency closure — PARTIAL / CONTINUE BY GAP.** Batches 1–9 are recorded. Batch 7's six missing EU locators now have research routes (AAA Cultural Anthropology 3/3; UNESCO Education Systems A/B; Education C requires a source/scope choice). Batch 8 has locator and Claim-remediation research for 15/15 EUs/Claims (including six placeholder Claim proposals); Batch 9's five missing locator gaps also have direct candidates. Canonical EU/Source/Claim implementation and authorization remain open. See `FIRST-EDITION-BATCH7-UNPINNED-EVIDENCE-AND-SOURCE-FIT-RESEARCH-2026-11-19.md`, `FIRST-EDITION-BATCH8-EVIDENCE-AND-CLAIM-REMEDIATION-RESEARCH-2026-11-19.md` and `FIRST-EDITION-BATCH9-UNPINNED-EVIDENCE-LOCATOR-RESEARCH-2026-11-19.md`. These are research closures, not evidence sufficiency or publication approvals. Continue only against rows with unresolved EU locator, Source identity/fit, Context/Scope applicability, version drift, or substantive Claim defect. Do not repeat closed batches.
3. **Version lineage and identifier controls — PRESERVE.** Keep historical `food-systems-basics@1` separate from R9 `@2`; keep the 13 stale international-law v1 rows as history and the current v2 set on HOLD pending substantive re-review. Water-quality alias normalization and the malformed Cambridge source-ID normalization are recorded; never rename canonical IDs to match a malformed register token.
4. **Cross-slice Relations — IDENTITY/PAIR REVIEW CLOSED; RELEASE BLOCKERS OPEN.** The separate ledger contains 63 Relations and 126 participant references; 126/126 exact ID/version/type checks and 63/63 semantic pair reviews are complete. The 97 non-candidate references (82 unique endpoint records) are also identity-verified and considered in pair review. This does not approve any Relation. Remaining blockers include target-specific Context applicability for 62 Relations, the earthquake Event/Context/Scope model, the container/water State participant model, and 15 semantic-HOLD Relations. Keep Relations outside the vertical-slice record denominator.
5. **Bounded structural-map screening — CLOSED.** All 69 examples in the controlling Part II map are now accounted for: 37 already represented in Part II candidates, seven reused from Part I, and 25 initially absent examples screened/reconciled through prior-screen reuse, Batch 1 and Batch 2. Part II candidate coverage is 124/385 slices; 261 other slices are not named by the current map examples and remain outside the approved bounded scope. Do not treat them as an automatic audit queue.
6. **Batch 1 — CLOSED, ALL HOLD.** Nine slices / 89 records screened or prior-screen-reused; no automatic promotion.
7. **Prior-screen reuse — CLOSED, ALL HOLD.** Eleven slices / 99 records re-read at current versions and added using existing substantive HOLD decisions; audits were reused, not repeated.
8. **Batch 2 — CLOSED, ALL HOLD.** Five slices / 47 records screened; the 47 canonical record blobs were unchanged between the Batch 2 inspection and the last fully green content HEAD. The source-and-locator remediation dossier is research-only and does not authorize canonical edits.
9. **Rights, editorial accountability and Human View — OPEN.** Seven source-specific rights screens cover 55 entries / 52 distinct slices; they are screening evidence, not clearance. Owner decisions R-01–R-10 remain open. Human View and high-consequence review remain required for any proposed INCLUDE.
10. **Disposition — NO INCLUDE / NO EXCLUDE.** All current candidate and dependency rows remain HOLD. No allowlist, preview allowlist, publication state, deployment or release approval is created by this register.
11. **Exact-head CI.** The four required workflows passed on `48c78389fb5345223627a687b22d51ee260b9d7d`. Current PR HEAD is `24bbd561ea1829048d25ad9ab1500df11466b2bc`, 27 commits ahead of that green content HEAD. The complete comparison lists 13 changed paths, all under `RELEASE/`; no `CONTENT/` or `REFERENCE/` path changed in those 27 commits. No workflow runs were returned for the current documentation-only HEAD, so do not label it an exact-head 4/4 PASS. The confirmed 4/4 result remains tied to `48c78389`; rerun all gates on the final immutable release HEAD after canonical changes.
12. **Change control.** PR #22 remains Draft/unmerged; `main` is untouched. No canonical record, Relation, allowlist or release manifest is changed without the exact bounded authorization and owner/editorial approval required for that change.

## 6. Source registers

- `RELEASE/FIRST-EDITION-FOUNDATIONS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-CHEMICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-PHYSICAL-SCIENCES-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-ECONOMIC-SYSTEMS-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-ENGINEERING-COMPUTING-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-EARTH-SPACE-EXACT-VERSION-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-HISTORY-CULTURE-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-SOCIETY-AND-PUBLIC-INSTITUTIONS-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-LEGAL-TRADE-INSTITUTIONAL-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-R9-EVIDENCE-DEPTH-REGISTER-ADDENDUM-2026-11-19.md`
- `RELEASE/FIRST-EDITION-RECORD-LEVEL-CANDIDATE-REGISTER-2026-11-18.md`
- `RELEASE/FIRST-EDITION-PART-II-INVENTORY-RECONCILIATION-2026-11-19.md`
- `RELEASE/FIRST-EDITION-CROSS-SLICE-RELATION-DEPENDENCY-INVENTORY-2026-11-19.md`
- `RELEASE/FIRST-EDITION-PART-II-STRUCTURAL-GAP-TRIAGE-2026-11-19.md`
- `RELEASE/FIRST-EDITION-PART-II-BATCH1-FOUNDATIONS-SCREEN-2026-11-19.md`
- `RELEASE/FIRST-EDITION-PART-II-BATCH2-HISTORY-HUMANITIES-SCREEN-2026-11-19.md`
- `RELEASE/FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH8-2026-11-19.md`
- `RELEASE/FIRST-EDITION-PART-II-CLAIM-DEPENDENCY-CLOSURE-BATCH9-2026-11-19.md`
- `RELEASE/FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md`
- `RELEASE/FIRST-EDITION-INTERNATIONAL-LAW-V2-SUBSTANTIVE-DEPENDENCY-REREVIEW-2026-11-19.md`
- `RELEASE/FIRST-EDITION-BATCH7-UNPINNED-EVIDENCE-AND-SOURCE-FIT-RESEARCH-2026-11-19.md`
- `RELEASE/FIRST-EDITION-BATCH8-EVIDENCE-AND-CLAIM-REMEDIATION-RESEARCH-2026-11-19.md`
- `RELEASE/FIRST-EDITION-BATCH9-UNPINNED-EVIDENCE-LOCATOR-RESEARCH-2026-11-19.md`

- `RELEASE/DOMAIN-AUDIT-MEASUREMENT-GEOMETRY-CALCULUS-2026-11-19.md`
- `RELEASE/DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md`
- `RELEASE/DOMAIN-AUDIT-CLIMATE-SOLAR-SYSTEM-REMOTE-SENSING-2026-11-19.md`
- `RELEASE/DOMAIN-AUDIT-HYDROLOGY-METEOROLOGY-OCEANOGRAPHY-2026-11-19.md`
- `RELEASE/DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md`
- `RELEASE/DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md`
- `RELEASE/DOMAIN-AUDIT-ECONOMIC-SYSTEMS-2026-11-19.md`
- `RELEASE/DOMAIN-EXPANSION-AUDIT-2026-09-30.md`

## 7. Current-head dependency supplement — 2026-11-19

The following ten exact-version dependency records were re-fetched from canonical JSON at PR pre-supplement HEAD `cbb620b1b2fc714414b57dc53ac7b8faba8980e1`. Exact record IDs, version 1 and types were verified. All remain HOLD. They were absent from the previous 1,119-row table and are now added to the dependency inventory. This is a dependency-only reconciliation; candidate keys and slice coverage are unchanged.

| Record/version | Type | Slice | Decision | Version verification | Source register(s) |
|---|---|---|---|---|---|
| `EU_P9_MARINE_BIOLOGY_BASICS_A@1` | evidence_use | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `EU_P9_MARINE_BIOLOGY_BASICS_B@1` | evidence_use | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `EU_P9_MARINE_BIOLOGY_BASICS_C@1` | evidence_use | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `SRC_NOAA_ECOSYSTEM_SCIENCE_2026@1` | source | `marine-biology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `EU_P9_PATHOLOGY_BASICS_A@1` | evidence_use | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `EU_P9_PATHOLOGY_BASICS_B@1` | evidence_use | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `EU_P9_PATHOLOGY_BASICS_C@1` | evidence_use | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `SRC_NCBI_HISTOLOGY_PATHOLOGY@1` | source | `pathology-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `EU-MEASUREMENT_UNCERTAINTY_BIPM@1` | evidence_use | `measurement-uncertainty-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |
| `SRC-BIPM-VIM-MEASUREMENT-UNCERTAINTY@1` | source | `measurement-uncertainty-basics` | HOLD | canonical_json_dependency_verified_hold | FIRST-EDITION-BATCH1-3-CURRENT-HEAD-EVIDENCE-AND-SOURCE-FIT-FOLLOWUP-2026-11-19.md |

**Reconciled total:** 1,129 exact-version rows = 1,058 candidate keys + 71 dependency records. Part II slice coverage remains 124/385; no candidate Claim or slice has been added by this supplement.

**Separate scope finding:** 21 known current v1 Claim records across 11 slices were found outside the 1,058 candidate-key master. They are listed in the Batch 1/3 follow-up report and remain outside the candidate denominator pending explicit scope triage. Agricultural Engineering A–C, its three EUs and Source are present in the candidate master and were included in Batch 10. This is the known set from reviewed slices, not a claim of exhaustive repository-wide enumeration.



### Batch 10 inventory note — 2026-11-19

- Batch 10 screened 20 candidate Claims, 24 Evidence Use records and nine Sources across agricultural-engineering, agrifood-systems, ecophysiology, food-distribution, infrastructure-resilience and magnetism. All 53 exact keys are already present in this master; no row additions were needed.
- Agricultural Engineering A–C, its three EUs and Source are present in this master; source-fit corrections and possible additional sources remain subject to bounded authorization.
- See `FIRST-EDITION-BATCH10-EVIDENCE-LOCATOR-AND-SOURCE-FIT-RESEARCH-2026-11-19.md` for the detailed locator/source-fit dossier.
