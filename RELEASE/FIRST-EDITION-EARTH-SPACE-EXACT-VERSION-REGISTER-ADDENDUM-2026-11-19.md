# First Edition Earth, Climate and Space — Exact-Version Register Addendum

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `50b303e6df8ecf2022290baa1183746fe4011113`  
Source screening: `RELEASE/FIRST-EDITION-EARTH-SPACE-REGISTER-ADDENDUM-2026-11-19.md`

## Purpose

This addendum expands the existing three-slice / 27-record screening summary into exact canonical `record_id@record_version` rows. It is inventory normalization only; no substantive adjudication is repeated and no decision is changed.

## Exact-version inventory

| Record/version | Type | Slice | Existing decision |
|---|---|---|---|
| `SRC-CLIMATE_SCIENCE_BASICS@1` | source | `climate-science-basics` | HOLD |
| `CLM-CLIMATE_SCIENCE_BASICS-A@1` | claim | `climate-science-basics` | HOLD |
| `CLM-CLIMATE_SCIENCE_BASICS-B@1` | claim | `climate-science-basics` | HOLD |
| `CLM-CLIMATE_SCIENCE_BASICS-C@1` | claim | `climate-science-basics` | HOLD |
| `EU-CLIMATE_SCIENCE_BASICS-A@1` | evidence_use | `climate-science-basics` | HOLD |
| `EU-CLIMATE_SCIENCE_BASICS-B@1` | evidence_use | `climate-science-basics` | HOLD |
| `EU-CLIMATE_SCIENCE_BASICS-C@1` | evidence_use | `climate-science-basics` | HOLD |
| `CTX-CLIMATE_SCIENCE_BASICS@1` | context | `climate-science-basics` | HOLD |
| `SCP-CLIMATE_SCIENCE_BASICS@1` | scope | `climate-science-basics` | HOLD |
| `SRC-SOLAR_SYSTEM_BASICS@1` | source | `solar-system-basics` | HOLD |
| `CLM-SOLAR_SYSTEM_BASICS-A@1` | claim | `solar-system-basics` | HOLD |
| `CLM-SOLAR_SYSTEM_BASICS-B@1` | claim | `solar-system-basics` | HOLD |
| `CLM-SOLAR_SYSTEM_BASICS-C@1` | claim | `solar-system-basics` | HOLD |
| `EU-SOLAR_SYSTEM_BASICS-A@1` | evidence_use | `solar-system-basics` | HOLD |
| `EU-SOLAR_SYSTEM_BASICS-B@1` | evidence_use | `solar-system-basics` | HOLD |
| `EU-SOLAR_SYSTEM_BASICS-C@1` | evidence_use | `solar-system-basics` | HOLD |
| `CTX-SOLAR_SYSTEM_BASICS@1` | context | `solar-system-basics` | HOLD |
| `SCP-SOLAR_SYSTEM_BASICS@1` | scope | `solar-system-basics` | HOLD |
| `SRC-REMOTE_SENSING_BASICS@1` | source | `remote-sensing-basics` | HOLD |
| `CLM-REMOTE_SENSING_BASICS-A@1` | claim | `remote-sensing-basics` | HOLD |
| `CLM-REMOTE_SENSING_BASICS-B@1` | claim | `remote-sensing-basics` | HOLD |
| `CLM-REMOTE_SENSING_BASICS-C@1` | claim | `remote-sensing-basics` | HOLD |
| `EU-REMOTE_SENSING_BASICS-A@1` | evidence_use | `remote-sensing-basics` | HOLD |
| `EU-REMOTE_SENSING_BASICS-B@1` | evidence_use | `remote-sensing-basics` | HOLD |
| `EU-REMOTE_SENSING_BASICS-C@1` | evidence_use | `remote-sensing-basics` | HOLD |
| `CTX-REMOTE_SENSING_BASICS@1` | context | `remote-sensing-basics` | HOLD |
| `SCP-REMOTE_SENSING_BASICS@1` | scope | `remote-sensing-basics` | HOLD |

## Reconciliation result

- Slices: 3/3 — climate science, solar system and remote sensing.
- Canonical records fetched and parsed at the inspection HEAD: 27/27.
- All 27 current canonical records are version 1.
- Existing decision preserved: 27 HOLD; 0 INCLUDE; 0 EXCLUDE.
- No canonical content, provenance, Context, Scope, publication state, Relation or allowlist was changed by this inventory extraction.
- Dependency closure (Claim → Evidence Use → Source and Context/Scope target refs) remains a separate verification field in the master register; matching suffixes and slice counts do not prove referential integrity.

## Existing blockers retained

- `climate-science-basics`: the three current Claims are editorial descriptions, not climate-science propositions.
- `solar-system-basics`: NASA directly supports the substantive Claims, but EUs need exact locators and the catalogue-currentness boundary must remain explicit.
- `remote-sensing-basics`: the current USGS Landsat page is too broad for the Claims; Claim B/C require direct evidence for spectral, sensor, resolution and observation-condition limits.

All three slices remain HOLD.

## Next

The slice-level Part II inventory now has exact-version rows for all six summary-only addenda. Proceed to dependency normalization and exact-version deduplication across the full candidate register, then triage the remaining unregistered Part II slice pool without launching a blanket audit.
