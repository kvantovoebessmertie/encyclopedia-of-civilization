# First Edition Economic Systems — Exact-Version Register Addendum

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `90400abb626400a8762e77ffd6e507a2c0e2aa3e`  
Source screening: `RELEASE/FIRST-EDITION-ECONOMIC-SYSTEMS-REGISTER-ADDENDUM-2026-11-19.md`

## Purpose

This addendum expands the existing five-slice / 45-record screening summary into exact canonical `record_id@record_version` rows. It is inventory normalization only; no substantive adjudication is repeated and no decision is changed.

## Exact-version inventory

| Record/version | Type | Slice | Existing decision |
|---|---|---|---|
| `SRC-ACCOUNTING_BASICS@1` | source | `accounting-basics` | HOLD |
| `CLM-ACCOUNTING_BASICS-A@1` | claim | `accounting-basics` | HOLD |
| `CLM-ACCOUNTING_BASICS-B@1` | claim | `accounting-basics` | HOLD |
| `CLM-ACCOUNTING_BASICS-C@1` | claim | `accounting-basics` | HOLD |
| `EU-ACCOUNTING_BASICS-A@1` | evidence_use | `accounting-basics` | HOLD |
| `EU-ACCOUNTING_BASICS-B@1` | evidence_use | `accounting-basics` | HOLD |
| `EU-ACCOUNTING_BASICS-C@1` | evidence_use | `accounting-basics` | HOLD |
| `CTX-ACCOUNTING_BASICS@1` | context | `accounting-basics` | HOLD |
| `SCP-ACCOUNTING_BASICS@1` | scope | `accounting-basics` | HOLD |
| `SRC-MACROECONOMICS_BASICS@1` | source | `macroeconomics-basics` | HOLD |
| `CLM-MACROECONOMICS_BASICS-A@1` | claim | `macroeconomics-basics` | HOLD |
| `CLM-MACROECONOMICS_BASICS-B@1` | claim | `macroeconomics-basics` | HOLD |
| `CLM-MACROECONOMICS_BASICS-C@1` | claim | `macroeconomics-basics` | HOLD |
| `EU-MACROECONOMICS_BASICS-A@1` | evidence_use | `macroeconomics-basics` | HOLD |
| `EU-MACROECONOMICS_BASICS-B@1` | evidence_use | `macroeconomics-basics` | HOLD |
| `EU-MACROECONOMICS_BASICS-C@1` | evidence_use | `macroeconomics-basics` | HOLD |
| `CTX-MACROECONOMICS_BASICS@1` | context | `macroeconomics-basics` | HOLD |
| `SCP-MACROECONOMICS_BASICS@1` | scope | `macroeconomics-basics` | HOLD |
| `SRC-MICROECONOMICS_BASICS@1` | source | `microeconomics-basics` | HOLD |
| `CLM-MICROECONOMICS_BASICS-A@1` | claim | `microeconomics-basics` | HOLD |
| `CLM-MICROECONOMICS_BASICS-B@1` | claim | `microeconomics-basics` | HOLD |
| `CLM-MICROECONOMICS_BASICS-C@1` | claim | `microeconomics-basics` | HOLD |
| `EU-MICROECONOMICS_BASICS-A@1` | evidence_use | `microeconomics-basics` | HOLD |
| `EU-MICROECONOMICS_BASICS-B@1` | evidence_use | `microeconomics-basics` | HOLD |
| `EU-MICROECONOMICS_BASICS-C@1` | evidence_use | `microeconomics-basics` | HOLD |
| `CTX-MICROECONOMICS_BASICS@1` | context | `microeconomics-basics` | HOLD |
| `SCP-MICROECONOMICS_BASICS@1` | scope | `microeconomics-basics` | HOLD |
| `SRC-MONEY_AND_BANKING_BASICS@1` | source | `money-and-banking-basics` | HOLD |
| `CLM-MONEY_AND_BANKING_BASICS-A@1` | claim | `money-and-banking-basics` | HOLD |
| `CLM-MONEY_AND_BANKING_BASICS-B@1` | claim | `money-and-banking-basics` | HOLD |
| `CLM-MONEY_AND_BANKING_BASICS-C@1` | claim | `money-and-banking-basics` | HOLD |
| `EU-MONEY_AND_BANKING_BASICS-A@1` | evidence_use | `money-and-banking-basics` | HOLD |
| `EU-MONEY_AND_BANKING_BASICS-B@1` | evidence_use | `money-and-banking-basics` | HOLD |
| `EU-MONEY_AND_BANKING_BASICS-C@1` | evidence_use | `money-and-banking-basics` | HOLD |
| `CTX-MONEY_AND_BANKING_BASICS@1` | context | `money-and-banking-basics` | HOLD |
| `SCP-MONEY_AND_BANKING_BASICS@1` | scope | `money-and-banking-basics` | HOLD |
| `SRC-ORGANIZATIONAL_BEHAVIOR_BASICS@1` | source | `organizational-behavior-basics` | HOLD |
| `CLM-ORGANIZATIONAL_BEHAVIOR_BASICS-A@1` | claim | `organizational-behavior-basics` | HOLD |
| `CLM-ORGANIZATIONAL_BEHAVIOR_BASICS-B@1` | claim | `organizational-behavior-basics` | HOLD |
| `CLM-ORGANIZATIONAL_BEHAVIOR_BASICS-C@1` | claim | `organizational-behavior-basics` | HOLD |
| `EU-ORGANIZATIONAL_BEHAVIOR_BASICS-A@1` | evidence_use | `organizational-behavior-basics` | HOLD |
| `EU-ORGANIZATIONAL_BEHAVIOR_BASICS-B@1` | evidence_use | `organizational-behavior-basics` | HOLD |
| `EU-ORGANIZATIONAL_BEHAVIOR_BASICS-C@1` | evidence_use | `organizational-behavior-basics` | HOLD |
| `CTX-ORGANIZATIONAL_BEHAVIOR_BASICS@1` | context | `organizational-behavior-basics` | HOLD |
| `SCP-ORGANIZATIONAL_BEHAVIOR_BASICS@1` | scope | `organizational-behavior-basics` | HOLD |

## Reconciliation result

- Slices: 5/5 — accounting, macroeconomics, microeconomics, money/banking and organizational behavior.
- Canonical records fetched and parsed at the inspection HEAD: 45/45.
- All 45 current canonical records are version 1.
- Existing decision preserved: 45 HOLD; 0 INCLUDE; 0 EXCLUDE.
- No canonical content, provenance, Context, Scope, publication state, Relation or allowlist was changed by this inventory extraction.
- Dependency closure (Claim → Evidence Use → Source and Context/Scope target refs) remains a separate verification field in the master register; matching suffixes and slice counts do not prove referential integrity.

## Existing blockers retained

- `accounting-basics`: IFRS Conceptual Framework is relevant, but paragraph-level locators and rights review remain open.
- `macroeconomics-basics`: IMF support for GDP is direct; aggregate macroeconomics and inflation need precise source pinpoints.
- `microeconomics-basics`: OpenStax supports core supply/demand/equilibrium concepts; exact section locators and assumptions remain required.
- `money-and-banking-basics`: Federal Reserve source is U.S.- and date-bounded; retain those boundaries and precise locators.
- `organizational-behavior-basics`: APA support is partial; communication and generalizability require additional direct evidence.

All five slices remain HOLD.

## Next

Continue exact-version extraction for the remaining summary-only addenda. Then normalize dependency references and deduplicate the resulting rows against the base register and detailed addenda.
