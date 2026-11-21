# First Edition — Part II Claim Dependency Closure Batch 1

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `b975b2a2a4280c879c7a18d94ee397492f4c710c`  
Status: **19/19 CLAIM → EVIDENCE USE → SOURCE CHAINS ID/VERSION/TYPE MATCH; ALL HOLD; EVIDENCE LOCATOR AND SUBSTANTIVE REVIEW OPEN**

## 1. Scope

This bounded batch advances the exact dependency closure for the base-register records previously marked `canonical_json_verified_identity_only`. It checks 19 Claims across 15 slices and follows each Claim to its exact Evidence Use and Source versions.

No canonical JSON was changed. No decision was promoted. All records remain HOLD.

## 2. Canonical graph results

| Check | Result |
|---|---:|
| Claims fetched and parsed | 19/19 |
| Evidence Use records fetched and parsed | 19/19 |
| Source records fetched and parsed | 15/15 |
| Claim ID/version/type matches | 19/19 |
| Evidence Use `claim_ref` matches exact Claim | 19/19 |
| Evidence Use `source_ref` matches exact Source | 19/19 |
| Claim provenance source identity matches EU source target | 19/19 |
| Evidence Use records with claim-specific `material.locator` | 0/19 |
| Source records with an exact `content.locator` / external pinpoint | 0/15 |
| New Evidence Use dependency records absent from prior master | 10 |

The 10 previously omitted Evidence Use dependencies, now required in the master register, are:

- `EU-BIODIVERSITY_BASICS-B@1`
- `EU-BIODIVERSITY_BASICS-C@1`
- `EU-CONSERVATION_BIOLOGY_BASICS-A@1`
- `EU-CONSERVATION_BIOLOGY_BASICS-B@1`
- `EU-CONSERVATION_BIOLOGY_BASICS-C@1`
- `EU-ECOTOXICOLOGY_BASICS-A@1`
- `EU-ENTOMOLOGY_BASICS-A@1`
- `EU_MARINE_BIOLOGY_BASICS_A@1`
- `EU_PATHOLOGY_BASICS_A@1`
- `EU-PLANT_PATHOLOGY_BASICS-A@1`

All ten were fetched from their canonical slice paths at the inspection HEAD; each has the exact expected `record_id`, `record_version=1`, `record_type=evidence_use`, Claim reference and Source reference.

## 3. Exact chains

| Slice | Claim/version | Evidence Use/version | Source/version | Graph result |
|---|---|---|---|---|
| astronomy-basics | `CLM-ASTRONOMY_BASICS-A@1` | `EU-ASTRONOMY_BASICS-A@1` | `SRC-ASTRONOMY_BASICS@1` | MATCH |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-A@1` | `EU-BIODIVERSITY_BASICS-A@1` | `SRC-BIODIVERSITY_BASICS@1` | MATCH |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-B@1` | `EU-BIODIVERSITY_BASICS-B@1` | `SRC-BIODIVERSITY_BASICS@1` | MATCH |
| biodiversity-basics | `CLM-BIODIVERSITY_BASICS-C@1` | `EU-BIODIVERSITY_BASICS-C@1` | `SRC-BIODIVERSITY_BASICS@1` | MATCH |
| cell-basics | `CLM-CELL_BASICS-A@1` | `EU-CELL_BASICS-A@1` | `SRC-CELL_BASICS@1` | MATCH |
| cell-biology-basics | `CLM-CELL_BIOLOGY_BASICS-A@1` | `EU-CELL_BIOLOGY_BASICS-A@1` | `SRC-CELL_BIOLOGY_BASICS@1` | MATCH |
| conservation-biology-basics | `CLM-CONSERVATION_BIOLOGY_BASICS-A@1` | `EU-CONSERVATION_BIOLOGY_BASICS-A@1` | `SRC-CONSERVATION_BIOLOGY_BASICS@1` | MATCH |
| conservation-biology-basics | `CLM-CONSERVATION_BIOLOGY_BASICS-B@1` | `EU-CONSERVATION_BIOLOGY_BASICS-B@1` | `SRC-CONSERVATION_BIOLOGY_BASICS@1` | MATCH |
| conservation-biology-basics | `CLM-CONSERVATION_BIOLOGY_BASICS-C@1` | `EU-CONSERVATION_BIOLOGY_BASICS-C@1` | `SRC-CONSERVATION_BIOLOGY_BASICS@1` | MATCH |
| ecotoxicology-basics | `CLM-ECOTOXICOLOGY_BASICS-A@1` | `EU-ECOTOXICOLOGY_BASICS-A@1` | `SRC-ECOTOXICOLOGY_BASICS@1` | MATCH |
| entomology-basics | `CLM-ENTOMOLOGY_BASICS-A@1` | `EU-ENTOMOLOGY_BASICS-A@1` | `SRC-ENTOMOLOGY_BASICS@1` | MATCH |
| evolution-basics | `CLM-EVOLUTION_BASICS-A@1` | `EU-EVOLUTION_BASICS-A@1` | `SRC-EVOLUTION_BASICS@1` | MATCH |
| genetics-basics | `CLM-GENETICS_BASICS-A@1` | `EU-GENETICS_BASICS-A@1` | `SRC-GENETICS_BASICS@1` | MATCH |
| immunology-basics | `CLM-IMMUNOLOGY_BASICS-A@1` | `EU-IMMUNOLOGY_BASICS-A@1` | `SRC-IMMUNOLOGY_BASICS@1` | MATCH |
| marine-biology-basics | `CLM_MARINE_BIOLOGY_BASICS_A@1` | `EU_MARINE_BIOLOGY_BASICS_A@1` | `SRC_MARINE_BIOLOGY_BASICS@1` | MATCH |
| measurement-uncertainty-basics | `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@1` | `SRC-MEASUREMENT_UNCERTAINTY_BASICS@1` | MATCH |
| motion-basics | `CLM-MOTION_BASICS-A@1` | `EU-MOTION_BASICS-A@1` | `SRC-MOTION_BASICS@1` | MATCH |
| pathology-basics | `CLM_PATHOLOGY_BASICS_A@1` | `EU_PATHOLOGY_BASICS_A@1` | `SRC_PATHOLOGY_BASICS@1` | MATCH |
| plant-pathology-basics | `CLM-PLANT_PATHOLOGY_BASICS-A@1` | `EU-PLANT_PATHOLOGY_BASICS-A@1` | `SRC-PLANT_PATHOLOGY_BASICS@1` | MATCH |

## 4. Evidence and editorial blockers

**All 19 Evidence Use records lack a claim-specific locator.** Their `claim_ref` and `source_ref` fields are structurally correct, but a correct edge is not evidence sufficiency. All 15 Source records also lack a canonical pinpoint locator.

Additional content-level issues identified during this graph pass:

- `CLM-CELL_BIOLOGY_BASICS-A@1`, `CLM-GENETICS_BASICS-A@1` and `CLM-IMMUNOLOGY_BASICS-A@1` are editorial placeholders (“the slice introduces basic concepts…”), not falsifiable subject-matter Claims.
- `SRC-EVOLUTION_BASICS@1` uses a generic placeholder identity (“Authoritative reference source for evolution-basics”) rather than a properly identified publication/authoring body.
- `SRC-IMMUNOLOGY_BASICS@1` identifies OpenStax Microbiology “Innate and Adaptive Immunity” but the stored URL points to a “How Pathogens Cause Disease” page; this is a source/title/locator mismatch requiring correction.
- Biodiversity and conservation Claims share the broad OpenStax Biology 2e §47.4 source page; exact Claim-specific sections are not identified and may not support every proposition.
- Marine biology uses a broad NOAA marine-life portal; it needs a direct subject-matter page/section.
- Measurement uncertainty points to NIST Technical Note 1297 but has no pinpoint to the relevant section or formula.
- Astronomy, cell biology, cell basics, evolution, genetics, pathology, plant pathology, entomology and ecotoxicology also lack exact section/term locators in the canonical Source/Evidence Use records.

These findings are blockers, not automatic exclusions. Rights, attribution and reuse permissions have not been cleared by this graph pass.

## 5. Decision

- 19/19 Claim → Evidence Use → Source identity/version/type chains: **MATCH**.
- 10 previously omitted Evidence Use dependencies: add to master register once, keyed by exact `record_id@version`.
- All 19 Claims remain **HOLD** because evidence pinpoints are absent and substantive source-fit review remains open.
- No canonical JSON, Relation or source record was edited.
- No INCLUDE/EXCLUDE decision, public allowlist or release permission was created.

## 6. Next bounded action

Continue the remaining 21 identity-only Claims in the base-register pool using the same exact chain check. Do not repeat these 19 chains. After the 40-Claim base-register closure batch is complete, resolve all missing locators and source-fit blockers in a separate substantive pass.
