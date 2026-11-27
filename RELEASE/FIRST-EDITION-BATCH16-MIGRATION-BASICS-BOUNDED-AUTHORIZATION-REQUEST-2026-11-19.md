# Batch 16 — Migration Basics Exact Source-Graph Authorization Request

Date: 2026-11-19
Target branch: `mvp-public-contribution-design-2026-10-11`
Inspection HEAD: `3d1d1d9c83b16e1e60a78f95dae4dfad501defa8`
Status: **OWNER AUTHORIZATION REQUIRED — PROPOSAL ONLY; NO CANONICAL JSON CHANGED**

## 1. Purpose

Convert the completed Batch 16 research into an exact, bounded owner decision. The current seven-record slice has three Claims and three generic Evidence Use records, all v1, plus one generic IOM Source v1. The research found direct IOM Toolkit locators for all three Claims, but Claim C also requires separate UNHCR and UN Guiding Principles evidence chains to preserve the legal distinction between refugees and internally displaced persons.

This document requests approval for a narrowly scoped graph expansion. It does not create IDs, modify records, change publication states or approve release.

## 2. Exact current records and blob SHAs

All seven records were re-fetched at the inspection HEAD.

| Record | Current version | Blob SHA |
|---|---:|---|
| `SRC-MIGRATION_BASICS` | 1 | `2ffcbf2ad91efde76b7429b907c0a5f03084cd9f` |
| `CLM-MIGRATION_BASICS-A` | 1 | `b59085a17ba3568a187cb3b29612aed7f9560375` |
| `CLM-MIGRATION_BASICS-B` | 1 | `a4c21141934c816e7fd3cbbf9793eedff54ad7b6` |
| `CLM-MIGRATION_BASICS-C` | 1 | `54cb80278a2913bf3f1e98903d657821920e23b6` |
| `EU-MIGRATION_BASICS-A` | 1 | `6cb06f03418a426b098127fa4359619695952164` |
| `EU-MIGRATION_BASICS-B` | 1 | `0e7f0455b8e392106813cfb413abc16947bcf17e` |
| `EU-MIGRATION_BASICS-C` | 1 | `30794122dc7f83e4586572a44f202a11f620fd0c` |

If any current SHA/version differs when owner authorization is granted, regenerate the packet at a new frozen HEAD.

## 3. Existing Claim statements — preserve exactly

- A: “Миграция включает перемещение людей из одного места проживания в другое, в том числе через международные границы.”
- B: “Причины и формы миграции разнообразны и могут включать экономические, семейные, образовательные, конфликтные и другие обстоятельства.”
- C: “Статус мигранта, беженца или другого перемещённого лица определяется применимыми правовыми и фактическими обстоятельствами и не является взаимозаменяемым понятием.”

No change to any Claim statement or `claim_type` is requested.

## 4. Proposed source graph

### 4.1 Existing IOM Source — update identity to exact Toolkit source

Proposed Source version: `SRC-MIGRATION_BASICS@1 → @2`.

**Source identity:** International Organization for Migration (IOM), *World Migration Report Educators' Toolkit* (2022).

**URI:** `https://wmr-educatorstoolkit.iom.int/glossary`

**Source locator metadata:**
- Glossary: “Migration”, “Migrant”, “Refugee (1951 Convention)”, “Internally Displaced Persons (IDPs)”;
- Module 3, “Why do people migrate?” and “Drivers of migration”.

The existing general WMR landing-page identity is too broad for the material actually used. Replacing it with the exact Toolkit identity allows the existing three EU records to reference a specific, stable research resource.

### 4.2 Additional source for Claim C — UNHCR / 1951 Convention

A separate canonical Source record is required; do not merge the Convention with the IOM Toolkit.

**Source identity:** UNHCR, “The 1951 Refugee Convention”, section “What is the definition of a refugee?”

**URI:** `https://www.unhcr.org/about-unhcr/overview/1951-refugee-convention`

**Pinpoint locator:** Convention Article 1 definition and UNHCR's explanatory section on the definition of a refugee.

**Purpose:** support the legal criteria for refugee status, including being outside the country of nationality/former habitual residence and the well-founded-fear/persecution grounds in Article 1.

### 4.3 Additional source for Claim C — UN Guiding Principles on Internal Displacement

A separate canonical Source record is required; do not merge this instrument with the Convention or IOM Source.

**Source identity:** United Nations, *Guiding Principles on Internal Displacement*, E/CN.4/1998/53/Add.2.

**URI:** `https://digitallibrary.un.org/nanna/record/251017/files/E_CN-4_1998_53_Add-2-EN.pdf`

**Pinpoint locator:** Introduction, paragraph 2 — definition of internally displaced persons, including forced/obliged movement and remaining within internationally recognized State borders.

**Purpose:** support the internal-displacement boundary and distinguish IDPs from persons who crossed an international border.

### 4.4 Canonical ID allocation — owner action required

No new canonical IDs are assigned in this proposal. If approved, the owner/editor must allocate IDs under the repository's canonical ID policy for:
- one UNHCR Source record;
- one UN Guiding Principles Source record;
- one additional Evidence Use record for the UNHCR Source→Claim C chain;
- one additional Evidence Use record for the UN Guiding Principles Source→Claim C chain.

The three existing EU records remain the IOM Toolkit chains. Claim C therefore has three independent, source-specific Evidence Use records: IOM, UNHCR and UN Guiding Principles.

Do not use raw URLs in `content.source_ref`, do not place multiple canonical Sources in one Source record, and do not invent IDs.

## 5. Existing EU v2 proposal

If authorized, version each existing EU v1→v2:
- update `content.claim_ref` to the exact corresponding Claim v2;
- update `content.source_ref` to `SRC-MIGRATION_BASICS@2`;
- update `provenance.created_from` to the exact current Claim and Source references consistent with the chosen record-provenance convention;
- add claim-specific `content.material.locator` and a bounded description;
- preserve `evidence_role: supports`.

### EU A — migration definition

Locator: IOM Toolkit Glossary, “Migration”: movement away from a person's usual place of residence, either across an international border or within a State.

Boundary: distinguish international from internal migration; do not imply that all migration crosses borders or confers a particular legal status.

### EU B — migration drivers

Locator: IOM Toolkit Module 3, “Why do people migrate?” and “Drivers of migration”; work, family and study, plus conflict, persecution and disasters.

Boundary: drivers are illustrative, diverse and often interlinked. Do not classify all economic, family or educational movement as forced migration.

### EU C — broad category distinction

Locator: IOM Toolkit Glossary entries “Migrant”, “Refugee (1951 Convention)” and “Internally Displaced Persons (IDPs)”.

Boundary: IOM's broad movement-based “migrant” concept is not interchangeable with refugee status under the 1951 Convention or the UN Guiding Principles' IDP definition. The IOM glossary is not a substitute for the treaty text or UN Guiding Principles.

## 6. New Claim C Evidence Use dependencies

Subject to owner ID allocation, create two new Evidence Use records, each with:
- `record_type: evidence_use`;
- exact `claim_ref: CLM-MIGRATION_BASICS-C@2`;
- one exact `source_ref` to its own Source v1 (or the version explicitly approved by the owner);
- `evidence_role: supports`;
- pinpoint locator and support boundary;
- provenance references aligned to the source/claim used.

The UNHCR EU supports only the 1951 Convention refugee definition. The UN Guiding Principles EU supports only the IDP definition and non-crossing of an internationally recognized State border. Neither record alone establishes the entire broad Claim C.

## 7. Rights, legal and editorial boundaries

- IOM Toolkit materials are institutional publications; public access is not a blanket reproduction licence. Use bibliographic identity, exact locator metadata and independently worded factual paraphrase; do not copy toolkit pages, diagrams or photographs.
- The 1951 Convention and UN Guiding Principles are official legal instruments/documents. Retain exact article/paragraph locators; do not replace the legal instruments with explanatory summaries.
- UNHCR explanatory pages are guidance, not a substitute for the Convention or applicable national/regional law.
- The slice makes distinctions affecting legal protection and rights. Qualified migration/refugee-law review and independent Human View are mandatory before any release decision.
- The project's final distribution and content-licensing model remains unresolved. No blanket rights clearance is inferred.

## 8. Requested owner authorization

Approve or amend this exact bounded scope:

1. Version `SRC-MIGRATION_BASICS` from v1 to v2 to identify the IOM World Migration Report Educators' Toolkit.
2. Version Claims A–C from v1 to v2 only for provenance alignment to the approved Source v2; preserve statements and `claim_type`.
3. Version existing EU A–C from v1 to v2 with the IOM claim-specific locators and exact Claim/Source references.
4. Allocate two canonical Source IDs and two Evidence Use IDs for UNHCR and UN Guiding Principles Claim C dependencies.
5. Create those two source-specific Claim C Evidence Use records with exact locators and bounded support.
6. Update only this slice's README and bounded audit/rights register entries as needed.
7. Do not change publication/completion states, allowlist, INCLUDE/HOLD/EXCLUDE, unrelated records, Relations, validators, schema or release-gate semantics.

## 9. Explicit non-actions

This request does not authorize or perform:
- any canonical JSON change before owner approval;
- any Claim statement or `claim_type` change;
- any new ID allocation before owner approval;
- any legal conclusion beyond the cited definitions;
- any publication status, completion status, allowlist or release decision change;
- any deployment, merge or write to `main`.

Migration Basics remains HOLD.

## 10. Post-authorization validation contract

1. Freeze a new exact PR HEAD and re-fetch the seven existing records; verify all SHAs in §2.
2. Confirm canonical IDs for the two new Sources and two new EUs are allocated and unique.
3. Apply Source and Claim provenance alignment, then existing EU A–C changes, then new Claim C source/EU dependencies.
4. Re-fetch all changed records and validate exact versioned Claim→EU→Source references.
5. Verify Claim statements and types are unchanged.
6. Validate legal-category support boundaries separately for migrant, refugee and IDP.
7. Run affected-slice schema/graph/reference tests, then exact-head Reference Tests, Release Conformance Gate, Offline Edition and Browser Tests on one immutable final HEAD.
8. Preserve HOLD pending rights review, qualified legal/editorial review and Human View.

**Owner decision:** pending. No canonical JSON changed.
