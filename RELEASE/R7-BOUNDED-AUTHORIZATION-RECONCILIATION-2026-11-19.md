# R7 Bounded Authorization Reconciliation — 2026-11-19

Inspection HEAD: `76ceab9c3e426962a65873dfa29ec6264bc5bc10`
Authorization manifest: `RELEASE/EDITORIAL-CORRECTION.json`
Status: **SPOT-CHECK RECONCILIATION; NOT A COMPLETE 94-SCOPE CERTIFICATION**

## 1. Purpose

Reconcile selected active bounded authorizations against the current canonical tree so completed work is not repeated and genuinely pending work is isolated. This is a spot-check of exact records and versions, not a claim that all 94 record-level scopes have been reconciled.

## 2. Verified as already applied — do not repeat

### R9 evidence-depth/source authorizations

Current canonical Source versions re-fetched at the inspection HEAD:

| Slice | Record | Current version | Current blob SHA |
|---|---|---:|---|
| History of Medicine | `SRC-HISTORY_OF_MEDICINE` | 2 | `6dd5e07c52caa94cc6c27e6c2fe60b5544df12b0` |
| History of Engineering | `SRC-HISTORY_OF_ENGINEERING` | 2 | `7785646b231a0ef0a8a0020f6ddbdd39fee92e95` |
| Library Science | `SRC-LIBRARY_SCIENCE` | 2 | `d0d133f2ab61ea7c67b7c7ab42a6ee037e97139f` |
| Cultural Heritage | `SRC-CULTURAL_HERITAGE` | 2 | `ba8ac3f2409712ef714b2c6570c2634162b8b96a` |
| History of Mathematics | `SRC-HISTORY_OF_MATHEMATICS` | 2 | `388c020f207ff4fcf25840e290b1368d3ac8d4a1` |
| Cartography | `SRC-CARTOGRAPHY` | 2 | `6973eb28c9ea8ff9105c29185bf48fb1a44695ee` |
| Food Systems | `SRC-FOOD_SYSTEMS` | 2 | `30da768f715b18da016085cc8a3a5145c3ed5cfe` |
| Hydraulic Engineering | `SRC-HYDRAULIC_ENGINEERING` | 2 | `33f8b6cd620835c427d658e97f700f9204d24b63` |

Additional spot-check: `CLM-ARCHIVAL_SCIENCE-B@3` is already present (blob SHA `217615940b297f153a0e4347e6eb77b5019da439`). These sampled authorized changes are already reflected in the current tree. Do not reapply them; verify remaining dependent records only if an exact authorization-specific closure check is still outstanding.

### Legal/Trade/Institutional remediation

Six primary Sources are already v2 at the current tree:
- Administrative Law — `SRC-ADMINISTRATIVE_LAW_BASICS@2`
- Comparative Law — `SRC-COMPARATIVE_LAW_BASICS@2`
- Migration and Mobility — `SRC-MIGRATION_AND_MOBILITY_BASICS@2`
- Political Economy — `SRC-POLITICAL_ECONOMY_BASICS@2`
- Social Policy — `SRC-SOCIAL_POLICY_BASICS@2`
- Taxation — `SRC-TAXATION_BASICS@2`

The Legal/Trade/Institutional remediation addendum records the six-slice 13-record-per-slice implementation as complete. Do not repeat this six-slice implementation.

### International Law reference alignment

The seven records expressly covered by `INTERNATIONAL-LAW-REFERENCE-ALIGNMENT-001` are already v2 and point to the current Claim/Source v2 references:
- `EU-INTERNATIONAL_LAW_BASICS-B@2`
- `EU-INTERNATIONAL_LAW_BASICS-C@2`
- `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-A@2`
- `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-B@2`
- `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-C@2`
- `CTX-INTERNATIONAL_LAW_BASICS@2`
- `SCP-INTERNATIONAL_LAW_BASICS@2`

Do not reapply this alignment.

## 3. Confirmed pending or blocked — prepare, do not repeat

### Civil Society Basics

All 13 exact records remain v1 at the inspection HEAD. The primary Source is still the generic World Bank-hosted PDF identity and the independent Source still points to Britannica. The new R7 authorization expressly permits replacing these with OECD/LEGAL/5021 and the UN Civil Society Unit “About us” page.

A record-by-record 13-record packet has been prepared:
`RELEASE/R7-CIVIL-SOCIETY-BOUNDED-DIFF-PACKET-2026-11-19.md`

This packet stays within the active bounded authorization. It preserves all Claim statements, versions Claims only for provenance alignment, and specifies primary/independent EU locators and support boundaries. No canonical change has been applied.

### Labour Economics Basics — rights conflict blocks implementation

Current Source state remains v1:
- `SRC-LABOR_ECONOMICS_BASICS@1` (primary; blob SHA `7f0aca55f80cb830bd01d35dbee0f32b7ce60d7a`)
- `SRC-LABOR_ECONOMICS_BASICS-INDEPENDENT@1` (independent; blob SHA `a8df946369b79788cf88e5285b5b51ef0fd4b3e9`)
- `EU-LABOR_ECONOMICS_BASICS-A@1` remains v1 (blob SHA `f1d24559a8367fca4cd131cc7b71eeaca08ac216`).

**Material authorization inconsistency:** the `remaining_r7_remediation_2026_11_19` rights_boundary currently says *Principles of Economics 3e* is CC BY 4.0. The current official OpenStax preface instead states CC BY-NC-SA 4.0 and expressly says the book may not be ingested into LLMs or generative-AI offerings without prior written permission. This agrees with the consolidated WP2 rights status and conflicts with the authorization JSON.

Until the owner corrects this inconsistency and records written permission or approves a rights-compatible replacement, do not implement the OpenStax-dependent Labour Economics source/EU chain. The ILOSTAT independent source branch also requires item-level rights review. No canonical record was changed.

### Comparative Civilizations Basics — supplementary source mapping requires clarification

All nine current records remain v1; the primary Source still identifies a Central Asia-specific UNESCO archive item. The active R7 authorization permits replacement with the AHA “Introduction to Doing World History” (1998) and specifies a supplementary historical-method source reference in EU-C provenance for Claim C (chronology versus causation).

Research confirmation:
- AHA directly supports cross-cultural comparison, interaction between societies, different development patterns, diffusion and syncretism. Its current page is marked © American Historical Association; no open licence was identified.
- The Singapore MOE 2021 Lower Secondary History syllabus directly distinguishes chronology (sequence/order) from causation (reasons/how events happened), pp. 4–5. Its front matter grants reproduction only for personal or non-commercial educational use; other rights are reserved.

**Implementation blocker:** the authorization describes a supplementary source reference in EU-C provenance but does not allocate a canonical Source ID or specify a schema-valid graph representation for that second source. Do not invent an ID or place a raw external URL into a record-reference field. Resolve the intended reference model and rights boundary before preparing an apply-ready EU-C diff. Claims A/B and the AHA Source/EU path can be specified separately, but the full nine-record authorization packet is not yet safe to apply.

## 4. Work completed in this reconciliation

- Distinguished already-applied R9 and Legal/Trade/Institutional samples from pending R7 slices.
- Verified International Law's seven dependent alignment records are already v2.
- Identified and documented the OpenStax licensing contradiction in the active R7 authorization.
- Identified the unresolved canonical-reference model and non-commercial terms for the Comparative Civilizations supplementary source.
- Confirmed Civil Society as a fully v1, bounded-authorized pending slice and prepared its exact 13-record packet.

## 5. Required next order

1. Obtain an owner correction/decision for the OpenStax rights inconsistency before any Labour Economics implementation.
2. Resolve the schema-valid supplementary-source representation and rights status for Comparative Civilizations Claim C.
3. Continue exact record/version reconciliation of the remaining bounded authorizations; do not infer completion from a Source version alone.
4. Only then prepare or apply the next exact packet, re-fetching every record at one frozen HEAD.
5. Preserve HOLD; all technical and editorial gates remain independent.

No canonical JSON, Relation, allowlist, coverage field, publication state or release decision changed during this reconciliation.


## Correction — Comparative Civilizations supplementary reference resolved — 2026-11-19

The §3 statement that the Comparative Civilizations supplementary-source representation remained unresolved is superseded by the schema inspection and packet prepared after that spot-check.

The existing `IMPLEMENTATION/005-RECORD-SCHEMA.json` already defines `provenance.external_sources` as an array of `external_ref` objects containing `uri` and optional/non-empty locator metadata. The bounded authorization's instruction to add only a supplementary historical-method source reference in EU-C provenance can therefore be implemented without creating a second canonical Source ID, changing `content.source_ref`, or modifying schema/validator code.

Exact packet: `RELEASE/R7-COMPARATIVE-CIVILIZATIONS-BOUNDED-DIFF-PACKET-2026-11-19.md`. It specifies all nine records, exact inspection SHAs, AHA source/claim-specific locators, and the MOE 2021 chronology/causation reference in EU-C `provenance.external_sources`. No canonical JSON changed. Slice remains HOLD pending rights review, independent historical/editorial review and Human View.


## Exact-head follow-up — remaining R7 slices (2026-11-19)

Inspection head before this documentation update: `531d4f57c8aed106e1f2b42bd5295752740e3545`.

### Comparative Civilizations Basics — packet preconditions still exact

- Re-fetched all nine canonical records at the inspection head.
- All nine remain v1; every current blob SHA exactly matches `R7-COMPARATIVE-CIVILIZATIONS-BOUNDED-DIFF-PACKET-2026-11-19.md`.
- The packet's schema design remains valid: the AHA source stays the single canonical `content.source_ref`; the MOE chronology/causation source is a supplementary `provenance.external_sources` entry on EU-C, using the existing schema.
- Source substance and locators were independently rechecked against the official AHA resource and MOE syllabus. The AHA resource supports world-history comparison, cross-cultural interaction, diffusion and syncretism; the MOE syllabus at printed p. 5 distinguishes chronology from causation and cautions that historical events commonly have multiple causes and consequences.
- Rights remain unresolved: AHA's site displays © 2026 and all rights reserved, with no open licence found for the resource; MOE permits reproduction only in entirety for personal/non-commercial educational use and reserves other rights. Project distribution/licensing model remains open.
- **Disposition:** packet remains technically ready but not rights-cleared. No canonical changes. HOLD.

### Labour Economics Basics — exact graph and licence conflict

- Re-fetched the complete 13-record graph. All records remain v1.
- Both Source records remain v1: primary `SRC-LABOR_ECONOMICS_BASICS@1` (ILO Wages topic page) and independent `SRC-LABOR_ECONOMICS_BASICS-INDEPENDENT@1` (World Bank Jobs and Development page).
- Claims A–C point to primary Source v1; primary and independent Evidence Use A–C point to the corresponding Claim v1 and respective Source v1; Context/Scope target Claim A v1.
- The active authorization's statement that OpenStax *Principles of Economics 3e* is CC BY 4.0 conflicts with the current official OpenStax HTML Preface and licensing help pages, which state CC BY-NC-SA 4.0 and a prior-written-permission restriction for LLM training/ingestion. An official OpenStax-hosted PDF asset separately surfaced with CC BY 4.0, creating an asset-level inconsistency that must be clarified with OpenStax rather than resolved by assumption.
- **Disposition:** do not implement OpenStax-dependent changes until the owner corrects the authorization after exact-asset clarification, records permission, or approves a rights-compatible source replacement. No canonical changes. HOLD.

### Civil Society Basics — packet remains exact, rights remain open

- All 13 records remain v1 and all 13 current SHAs match the prepared bounded diff packet.
- OECD Recommendation and UN Civil Society Unit source identity/locator mapping is ready at the record level. The OECD Legal Instrument's narrow reproduction permission does not apply as a blanket licence to the UN page or to the Encyclopedia project. UN site terms do not grant broad redistribution/derivative rights.
- **Disposition:** no canonical changes pending owner decision on project licence/distribution compatibility and rights treatment. HOLD.

### Reconciliation outcome

The three remaining R7 slices have now been freshly reconciled at the exact current record level:
- Civil Society: 13/13 exact packet SHA matches; rights decision pending.
- Comparative Civilizations: 9/9 exact packet SHA matches; rights decision pending.
- Labour Economics: 13/13 records re-fetched and graph-aligned at v1; authorization rights inconsistency blocks implementation.

No canonical JSON, Relation, allowlist, coverage field, publication state or release decision changed. The three slices remain HOLD. This follow-up supersedes no owner decision and does not expand any bounded authorization.
