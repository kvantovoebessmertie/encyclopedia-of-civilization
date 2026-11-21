# First Edition Chemical Sciences — Exact-Version Register Addendum

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `efdfcf3d723c88ddc4b85283fe343e4180e4d2ab`  
Source screening: `RELEASE/FIRST-EDITION-CHEMICAL-SCIENCES-REGISTER-ADDENDUM-2026-11-19.md`

## Purpose

This addendum expands the existing four-slice / 36-record screening summary into exact canonical `record_id@record_version` rows. It is inventory normalization only; no substantive adjudication is repeated and no decision is changed.

## Exact-version inventory

| Record/version | Type | Slice | Existing decision |
|---|---|---|---|
| `SRC-MIXTURES_AND_SOLUTIONS@1` | source | `mixtures-and-solutions` | HOLD |
| `CLM-MIXTURES_AND_SOLUTIONS-A@1` | claim | `mixtures-and-solutions` | HOLD |
| `CLM-MIXTURES_AND_SOLUTIONS-B@1` | claim | `mixtures-and-solutions` | HOLD |
| `CLM-MIXTURES_AND_SOLUTIONS-C@1` | claim | `mixtures-and-solutions` | HOLD |
| `EU-MIXTURES_AND_SOLUTIONS-A@2` | evidence_use | `mixtures-and-solutions` | HOLD |
| `EU-MIXTURES_AND_SOLUTIONS-B@2` | evidence_use | `mixtures-and-solutions` | HOLD |
| `EU-MIXTURES_AND_SOLUTIONS-C@2` | evidence_use | `mixtures-and-solutions` | HOLD |
| `CTX-MIXTURES_AND_SOLUTIONS@1` | context | `mixtures-and-solutions` | HOLD |
| `SCP-MIXTURES_AND_SOLUTIONS@1` | scope | `mixtures-and-solutions` | HOLD |
| `SRC-CHEMICAL_REACTIONS_BASICS@2` | source | `chemical-reactions-basics` | HOLD |
| `CLM-CHEMICAL_REACTIONS_BASICS-A@2` | claim | `chemical-reactions-basics` | HOLD |
| `CLM-CHEMICAL_REACTIONS_BASICS-B@2` | claim | `chemical-reactions-basics` | HOLD |
| `CLM-CHEMICAL_REACTIONS_BASICS-C@2` | claim | `chemical-reactions-basics` | HOLD |
| `EU-CHEMICAL_REACTIONS_BASICS-A@4` | evidence_use | `chemical-reactions-basics` | HOLD |
| `EU-CHEMICAL_REACTIONS_BASICS-B@4` | evidence_use | `chemical-reactions-basics` | HOLD |
| `EU-CHEMICAL_REACTIONS_BASICS-C@4` | evidence_use | `chemical-reactions-basics` | HOLD |
| `CTX-CHEMICAL_REACTIONS_BASICS@2` | context | `chemical-reactions-basics` | HOLD |
| `SCP-CHEMICAL_REACTIONS_BASICS@2` | scope | `chemical-reactions-basics` | HOLD |
| `SRC-ORGANIC_CHEMISTRY_BASICS@2` | source | `organic-chemistry-basics` | HOLD |
| `CLM-ORGANIC_CHEMISTRY_BASICS-A@2` | claim | `organic-chemistry-basics` | HOLD |
| `CLM-ORGANIC_CHEMISTRY_BASICS-B@2` | claim | `organic-chemistry-basics` | HOLD |
| `CLM-ORGANIC_CHEMISTRY_BASICS-C@2` | claim | `organic-chemistry-basics` | HOLD |
| `EU-ORGANIC_CHEMISTRY_BASICS-A@2` | evidence_use | `organic-chemistry-basics` | HOLD |
| `EU-ORGANIC_CHEMISTRY_BASICS-B@2` | evidence_use | `organic-chemistry-basics` | HOLD |
| `EU-ORGANIC_CHEMISTRY_BASICS-C@2` | evidence_use | `organic-chemistry-basics` | HOLD |
| `CTX-ORGANIC_CHEMISTRY_BASICS@2` | context | `organic-chemistry-basics` | HOLD |
| `SCP-ORGANIC_CHEMISTRY_BASICS@2` | scope | `organic-chemistry-basics` | HOLD |
| `SRC-BIOCHEMISTRY_BASICS@2` | source | `biochemistry-basics` | HOLD |
| `CLM-BIOCHEMISTRY_BASICS-A@2` | claim | `biochemistry-basics` | HOLD |
| `CLM-BIOCHEMISTRY_BASICS-B@3` | claim | `biochemistry-basics` | HOLD |
| `CLM-BIOCHEMISTRY_BASICS-C@2` | claim | `biochemistry-basics` | HOLD |
| `EU-BIOCHEMISTRY_BASICS-A@2` | evidence_use | `biochemistry-basics` | HOLD |
| `EU-BIOCHEMISTRY_BASICS-B@3` | evidence_use | `biochemistry-basics` | HOLD |
| `EU-BIOCHEMISTRY_BASICS-C@2` | evidence_use | `biochemistry-basics` | HOLD |
| `CTX-BIOCHEMISTRY_BASICS@2` | context | `biochemistry-basics` | HOLD |
| `SCP-BIOCHEMISTRY_BASICS@2` | scope | `biochemistry-basics` | HOLD |

## Reconciliation result

- Slices: 4/4 — `mixtures-and-solutions`, `chemical-reactions-basics`, `organic-chemistry-basics`, `biochemistry-basics`.
- Canonical records fetched and parsed at the inspection HEAD: 36/36.
- Existing decision preserved: 36 HOLD; 0 INCLUDE; 0 EXCLUDE.
- Current versions are not uniform: `EU-MIXTURES_AND_SOLUTIONS-A/B/C@2`; `chemical-reactions-basics` uses Source/Claims/Context/Scope @2 and Evidence Use @4; `organic-chemistry-basics` is @2; `biochemistry-basics` includes Claim B and Evidence Use B @3 while the other listed records are @2.
- No canonical content, provenance, Context, Scope, publication state, Relation or allowlist was changed by this inventory extraction.
- Dependency closure (Claim → Evidence Use → Source and Context/Scope target refs) remains a separate verification field in the master register; matching suffixes and slice counts do not prove referential integrity.

## Existing blockers retained

- `mixtures-and-solutions`: direct OpenStax §11.1 support is identified; EUs require exact pinpoint verification and rights/attribution remains open.
- `chemical-reactions-basics`: direct sections are identified for reactants/products and stoichiometry; current EU versions still require pinpoint and boundary verification.
- `organic-chemistry-basics`: the three Claims are editorial slice-purpose/evidence-boundary statements rather than falsifiable organic-chemistry propositions.
- `biochemistry-basics`: the three Claims are editorial slice-purpose/evidence-boundary statements rather than falsifiable biochemical propositions.

All four slices remain HOLD.

## Next

Continue exact-version extraction for the remaining summary-only addenda. Then normalize dependency references and deduplicate the resulting rows against the base register and detailed addenda.
