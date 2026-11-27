# First Edition Foundations — Exact-Version Register Addendum

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `a1392bc324982ee151ae58c57fe8d65ffad43f31`  
Source screening: `RELEASE/FIRST-EDITION-FOUNDATIONS-RECORD-LEVEL-REGISTER-ADDENDUM-2026-11-19.md`

## Purpose

This addendum expands the existing 3-slice / 27-record screening summary into exact canonical `record_id@record_version` rows. It is an inventory normalization only; it does not repeat substantive review or alter any decision.

## Exact-version inventory

| Record/version | Type | Slice | Existing decision |
|---|---|---|---|
| `SRC-UNITS_AND_MEASUREMENT@1` | source | `units-and-measurement` | HOLD |
| `CLM-UNITS_AND_MEASUREMENT-A@1` | claim | `units-and-measurement` | HOLD |
| `CLM-UNITS_AND_MEASUREMENT-B@1` | claim | `units-and-measurement` | HOLD |
| `CLM-UNITS_AND_MEASUREMENT-C@1` | claim | `units-and-measurement` | HOLD |
| `EU-UNITS_AND_MEASUREMENT-A@1` | evidence_use | `units-and-measurement` | HOLD |
| `EU-UNITS_AND_MEASUREMENT-B@1` | evidence_use | `units-and-measurement` | HOLD |
| `EU-UNITS_AND_MEASUREMENT-C@1` | evidence_use | `units-and-measurement` | HOLD |
| `CTX-UNITS_AND_MEASUREMENT@1` | context | `units-and-measurement` | HOLD |
| `SCP-UNITS_AND_MEASUREMENT@1` | scope | `units-and-measurement` | HOLD |
| `SRC-GEOMETRY_BASICS@1` | source | `geometry-basics` | HOLD |
| `CLM-GEOMETRY_BASICS-A@1` | claim | `geometry-basics` | HOLD |
| `CLM-GEOMETRY_BASICS-B@1` | claim | `geometry-basics` | HOLD |
| `CLM-GEOMETRY_BASICS-C@1` | claim | `geometry-basics` | HOLD |
| `EU-GEOMETRY_BASICS-A@1` | evidence_use | `geometry-basics` | HOLD |
| `EU-GEOMETRY_BASICS-B@1` | evidence_use | `geometry-basics` | HOLD |
| `EU-GEOMETRY_BASICS-C@1` | evidence_use | `geometry-basics` | HOLD |
| `CTX-GEOMETRY_BASICS@1` | context | `geometry-basics` | HOLD |
| `SCP-GEOMETRY_BASICS@1` | scope | `geometry-basics` | HOLD |
| `SRC-CALCULUS_BASICS@1` | source | `calculus-basics` | HOLD |
| `CLM-CALCULUS_BASICS-A@1` | claim | `calculus-basics` | HOLD |
| `CLM-CALCULUS_BASICS-B@1` | claim | `calculus-basics` | HOLD |
| `CLM-CALCULUS_BASICS-C@1` | claim | `calculus-basics` | HOLD |
| `EU-CALCULUS_BASICS-A@1` | evidence_use | `calculus-basics` | HOLD |
| `EU-CALCULUS_BASICS-B@1` | evidence_use | `calculus-basics` | HOLD |
| `EU-CALCULUS_BASICS-C@1` | evidence_use | `calculus-basics` | HOLD |
| `CTX-CALCULUS_BASICS@1` | context | `calculus-basics` | HOLD |
| `SCP-CALCULUS_BASICS@1` | scope | `calculus-basics` | HOLD |

## Reconciliation result

- Slices: 3/3 — `units-and-measurement`, `geometry-basics`, `calculus-basics`.
- Canonical records fetched and parsed at the inspection HEAD: 27/27.
- Record versions: all 27 current records are version 1.
- Existing decision preserved: 27 HOLD; 0 INCLUDE; 0 EXCLUDE.
- No canonical content, provenance, Context, Scope, publication state, Relation or allowlist was changed.
- Dependency closure (Claim → Evidence Use → Source and Context/Scope target refs) remains a separate verification field in the master register; this inventory does not infer closure from matching suffixes or record counts.

## Existing blockers retained

- `units-and-measurement`: measurement-definition and uncertainty claims need suitable additional sources and claim-specific locators; current NIST SI source alone is insufficient for A/C.
- `geometry-basics`: current source fit is inadequate for general geometry propositions; Claim C is too broad; EUs lack pinpoints.
- `calculus-basics`: direct OpenStax section support is identified, but EUs need exact section pinpoints and OpenStax CC BY-NC-SA / LLM-ingestion restrictions require explicit rights handling.

No new decision is made here. All three slices remain HOLD.

## Next

Continue exact-version extraction for the other five summary-only addenda. Then normalize dependency references and deduplicate the resulting rows against the base register and detailed addenda.
