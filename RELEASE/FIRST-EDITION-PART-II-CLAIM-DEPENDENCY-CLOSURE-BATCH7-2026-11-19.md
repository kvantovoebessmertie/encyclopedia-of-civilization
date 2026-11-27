# First Edition — Part II Claim Dependency Closure Batch 7

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Canonical inspection HEAD: `51a1b5b00df0c135fb8eccc49be3a427c06c8d3c`  
Status: **15/15 CLAIM → EVIDENCE USE → SOURCE CHAINS ID/VERSION/TYPE MATCH; 9/15 EUS HAVE PINPOINTS; ALL HOLD**

## 1. Scope and result

This batch closes dependency chains for cultural anthropology, cultural heritage, databases, distributed systems and education systems.

| Check | Result |
|---|---:|
| Claims fetched and parsed | 15/15 |
| Evidence Use records fetched and parsed | 15/15 |
| Source records fetched and parsed | 6/6 |
| Claim ID/version/type matches | 15/15 |
| Evidence Use `claim_ref` matches exact Claim | 15/15 |
| Evidence Use `source_ref` matches exact Source | 15/15 |
| Claim provenance source identity matches EU source target | 15/15 |
| Evidence Use records with claim-specific locators | 9/15 |
| Source records with explicit locator metadata | 4/6 |
| New exact-version dependencies absent from master | 0 |

All exact-version records were already present in the master. This batch advances dependency verification only; it adds no new master keys.

## 2. Exact chains

| Slice | Claim/version | Evidence Use/version | Source/version | Locator / note |
|---|---|---|---|---|
| cultural-anthropology-basics | `CLM-CULTURAL_ANTHROPOLOGY-A@1` | `EU-CULTURAL_ANTHROPOLOGY-A@1` | `SRC-CULTURAL_ANTHROPOLOGY@1` | No locator |
| cultural-anthropology-basics | `CLM-CULTURAL_ANTHROPOLOGY-B@1` | `EU-CULTURAL_ANTHROPOLOGY-B@1` | `SRC-CULTURAL_ANTHROPOLOGY@1` | No locator |
| cultural-anthropology-basics | `CLM-CULTURAL_ANTHROPOLOGY-C@1` | `EU-CULTURAL_ANTHROPOLOGY-C@1` | `SRC-CULTURAL_ANTHROPOLOGY@1` | No locator |
| cultural-heritage-basics | `CLM-CULTURAL_HERITAGE-A@2` | `EU-CULTURAL_HERITAGE-A@2` | `SRC-CULTURAL_HERITAGE@2` | UNESCO 1972 Convention, Article 1 |
| cultural-heritage-basics | `CLM-CULTURAL_HERITAGE-B@2` | `EU-CULTURAL_HERITAGE-B@2` | `SRC-CULTURAL_HERITAGE@2` | UNESCO 1972 Convention, Article 3 |
| cultural-heritage-basics | `CLM-CULTURAL_HERITAGE-C@2` | `EU-CULTURAL_HERITAGE-C@2` | `SRC-CULTURAL_HERITAGE-ICH@1` | UNESCO 2003 Convention, Article 2(1) |
| databases-basics | `CLM-DATABASES_BASICS-A@3` | `EU-DATABASES_BASICS-A@3` | `SRC-DATABASES_BASICS@3` | PostgreSQL 18.7 Tutorial §2.2 |
| databases-basics | `CLM-DATABASES_BASICS-B@3` | `EU-DATABASES_BASICS-B@3` | `SRC-DATABASES_BASICS@3` | PostgreSQL 18.7 Tutorial §2.2 |
| databases-basics | `CLM-DATABASES_BASICS-C@3` | `EU-DATABASES_BASICS-C@3` | `SRC-DATABASES_BASICS@3` | PostgreSQL 18.7 Tutorial §§2.5–2.6 |
| distributed-systems-basics | `CLM-DISTRIBUTED_SYSTEMS_BASICS-A@2` | `EU-DISTRIBUTED_SYSTEMS_BASICS-A@2` | `SRC-DISTRIBUTED_SYSTEMS_BASICS@2` | van Steen & Tanenbaum §2, p. 969 |
| distributed-systems-basics | `CLM-DISTRIBUTED_SYSTEMS_BASICS-B@2` | `EU-DISTRIBUTED_SYSTEMS_BASICS-B@2` | `SRC-DISTRIBUTED_SYSTEMS_BASICS@2` | van Steen & Tanenbaum §2, p. 969 |
| distributed-systems-basics | `CLM-DISTRIBUTED_SYSTEMS_BASICS-C@2` | `EU-DISTRIBUTED_SYSTEMS_BASICS-C@2` | `SRC-DISTRIBUTED_SYSTEMS_BASICS@2` | van Steen & Tanenbaum §1, pp. 968–969 |
| education-systems | `CLM-EDUCATION_SYSTEMS-A@1` | `EU-EDUCATION_SYSTEMS-A@1` | `SRC-EDUCATION_SYSTEMS@1` | No locator |
| education-systems | `CLM-EDUCATION_SYSTEMS-B@1` | `EU-EDUCATION_SYSTEMS-B@1` | `SRC-EDUCATION_SYSTEMS@1` | No locator |
| education-systems | `CLM-EDUCATION_SYSTEMS-C@1` | `EU-EDUCATION_SYSTEMS-C@1` | `SRC-EDUCATION_SYSTEMS@1` | No locator |

## 3. Source-fit and editorial findings

- **Cultural anthropology:** the American Anthropological Association's “What is Anthropology?” page is relevant to the discipline, but all three EUs lack pinpoints. Claim B's broad list of social, linguistic, biological and historical aspects and Claim C's participant-observation/methodological limitation need direct text support.
- **Cultural heritage:** the 1972 and 2003 UNESCO Conventions provide primary legal texts and direct article locators for all three Claims. Rights/translation and jurisdictional wording still need editorial review.
- **Databases:** PostgreSQL 18.7 official documentation directly supports relation/table terminology, row/column/data types, SELECT and JOIN. This is a strong technical chain. Confirm documentation version and software licence/attribution policy before republication.
- **Distributed systems:** van Steen and Tanenbaum's 2016 paper provides direct locators for the definition, node independence and network interconnection. The source is a scholarly paper; rights and reuse terms still need review.
- **Education systems:** UNESCO's right-to-education page is relevant, but all three EUs lack locators. Claim B's 4A framework needs an exact UNESCO/Committee on Economic, Social and Cultural Rights source. Claim C's cross-country differences in law, finance, governance, curriculum and delivery need a separate comparative source; the right-to-education landing page alone is insufficient.

## 4. Decision

- All 15 Claim → Evidence Use → Source chains match exact canonical ID/version/type.
- Nine EUs have direct locators; six do not.
- All 15 Claims remain **HOLD** pending the outstanding locator, source-fit, rights and editorial checks.
- No canonical JSON changed and no INCLUDE/EXCLUDE or allowlist decision was created.


## Locator and source-fit research closure — 2026-11-19 (research only)

The six previously unpinned Batch 7 EUs have been researched in `FIRST-EDITION-BATCH7-UNPINNED-EVIDENCE-AND-SOURCE-FIT-RESEARCH-2026-11-19.md`.

- Cultural Anthropology A/B/C: direct locators found in AAA's *Perspectives: An Open Introduction to Cultural Anthropology*, 2nd ed. (Introduction pp. 4–6; Fieldwork pp. 48–49, 60–63 and 66). Claim B may be narrowed to match the book's four-field model. The textbook is CC BY-NC 4.0; commercial use is not granted.
- Education Systems A: direct locator in UNESCO's “The right to education” opening statement.
- Education Systems B: direct locator in UNESCO's “State obligations and responsibilities” page, the four essential features (availability, accessibility, acceptability, adaptability). Pin the exact subpage, not just the root landing page.
- Education Systems C: the current single UNESCO rights page does not support the broad comparative proposition. Recommended minimum path is to narrow it to UNESCO's country-tailored education-system review methodology; retaining the broad comparative claim requires additional UNESCO/OECD source chains for law, financing, governance, curriculum and delivery.

This closes locator discovery for the six unpinned EUs with one explicit source/scope decision still open. No canonical JSON changed; all 15 Claims remain HOLD. Rights and qualified editorial review remain open.
