# R7 Labour Economics — ILO-led Path B Implementation

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Owner decision: `R7-LABOUR-ECONOMICS-ILO-PATH-B-OWNER-DECISION-2026-11-20`

## 1. Owner decision and scope

The project owner explicitly approved Path B on 2026-11-20: replace the OpenStax-dependent Labour Economics chain with an ILO-led source chain. The bounded authorization is recorded in `RELEASE/EDITORIAL-CORRECTION.json`.

The existing 13-record graph was re-fetched at v1 before changes. Claims A–C retain their exact statements and `documented_fact` types. Only their provenance was aligned to the new primary Source. Publication/completion states remain unchanged.

## 2. New source chain

### Primary statistical reference — ILOSTAT

Source v2 identifies the ILOSTAT Concepts and Definitions hub and its exact dependent resources:
- Labour Force Statistics (LFS and RURBAN), Description — Overview, labour-force participation, employment and unemployment.
- Wages and Working Time Statistics (COND), Description — Wages — Introduction.
- ILOSTAT Data — Labour productivity and Hours of work.
- ILO labour-underutilization resource — the three main measures: time-related underemployment, unemployment and potential labour force.
- ILO Thesaurus concept 13.01.1, “Labour economics”, Scope Notes: the aspects of economics concerned with labour supply and demand.

Claim-specific locators and support boundaries are recorded in Evidence Use A–C v2.

**Rights boundary:** the item-level publication date and licence of the ILOSTAT pages were not established in this review. No CC BY 4.0 licence is asserted for those pages. They are cited as factual/statistical references only; canonical content uses independently worded paraphrase and exact locators. No page text, datasets, graphics or third-party assets are copied or adapted.

### Independent institutional reference — WESO 2023

ILO, *World Employment and Social Outlook 2023: The value of essential work*, published 2023-03-08, DOI 10.54394/OQVF7543. The official report PDF expressly states CC BY 4.0, notwithstanding its pre-3-May-2023 publication date. The exact PDF notice, rather than the general post-2023 policy, is the rights basis.

- Chapter 1, “Who are the key workers?”
- Chapter 3, “Working conditions of key workers”, including wages and working hours.

Attribution to ILO is required; indicate changes where applicable; do not use the ILO emblem. Third-party cover photography and separately credited assets are excluded. No report prose, tables, figures or images are reproduced.

The WESO evidence is contextual and does not pretend to provide the complete indicator taxonomy, particularly productivity and labour underutilization. Those parts are supported by ILOSTAT locators.

## 3. Canonical changes

All 13 slice records advanced from v1 to v2:
- 2 Source records;
- 3 Claims (provenance-only; statements and claim types preserved);
- 6 Evidence Use records (claim-specific locators, exact @2 references and support boundaries);
- 1 Context and 1 Scope (target_ref aligned to Claim A@2).

Two dependent cross-slice Relations advanced from v2 to v3:
- `REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY`
- `REL-CROSS-MIGRATION-LABOR-ECONOMICS`

Only the Labour Claim C references in `provenance.created_from` and `content.participants` were changed from @1 to @2. Relation type, participant order, roles, direction, frame and semantics were preserved.

## 4. OpenStax exclusion

OpenStax Principles of Economics 2e and 3e are excluded from this remediation. The previously documented conflicting licence notices and separate LLM-processing permission condition are not relied upon or resolved by this Path B decision.

## 5. Validation and release boundary

- 13/13 slice records are now v2.
- 2/2 dependent Relations are now v3.
- Claim statements and types are unchanged.
- No records were added or removed.
- No INCLUDE/EXCLUDE, allowlist, publication, deployment or release decision was changed.
- Labour Economics remains HOLD pending independent labour-economics/statistical editorial review, source-rights and project-distribution compatibility review, Human View and all applicable first-edition gates.
- Exact-head Content Preflight, Reference Tests, Release Conformance Gate, Offline Edition and browser checks must be rerun on the final branch HEAD; earlier PASS results do not transfer.

## 6. Official references

- ILO Thesaurus, Labour economics: https://metadata.ilo.org/PoolParty/wiki/thesaurus?URI=https%3A%2F%2Fmetadata.ilo.org%2Fthesaurus%2F703448397&lang=en
- ILOSTAT Concepts and Definitions: https://ilostat.ilo.org/methods/concepts-and-definitions/
- ILOSTAT LFS description: https://ilostat.ilo.org/databases/lfs/description/
- ILOSTAT COND description: https://ilostat.ilo.org/methods/concepts-and-definitions/description-wages-and-working-time-statistics/
- ILO labour underutilization: https://www.ilo.org/resource/labour-underutilization
- ILOSTAT data: https://ilostat.ilo.org/Data/
- WESO 2023 publication page: https://www.ilo.org/publications/flagship-reports/world-employment-and-social-outlook-2023-value-essential-work
- WESO 2023 report PDF / explicit CC BY 4.0 notice: https://digitallibrary.un.org/nanna/record/4036391/files/1396732_EN.pdf

**Disposition: bounded source remediation implemented; slice remains HOLD.**
