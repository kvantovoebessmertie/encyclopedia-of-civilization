# Migration / Labour Economics — Focused Relation Evidence Adjudication

- **Agent:** chief-engineer
- **Task:** Focused WP1 evidence and endpoint-fit review of `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`
- **Date (UTC):** 2026-11-20
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** mvp-public-contribution-design-2026-10-11
- **Starting HEAD:** 858c2ee7f9bcc0c95334d495be1e6ad026081ce7
- **Status:** VERIFIED — exact graph, ILO Practical Guide and work-level rights notice inspected; report-only

## 1. Request and acceptance criteria

Continue WP1 by checking whether the existing Migration / Labour Economics Relation has a direct authoritative source bridge and whether the exact participant Claims fit its declared semantics. Preserve canonical records, current versions and HOLD unless a separate bounded owner authorization permits changes.

## 2. Scope

- **In scope:** Relation @4, Context @1, both participant Claims @2, their Evidence Use @2 and Source @2 records, and the ILO 2026 Practical Guide on international labour migration and temporary labour mobility statistics.
- **Out of scope:** adding the ILO Guide as a canonical Source, modifying Evidence Use or Relation/Context, changing Claims, rights clearance, candidate disposition, and release/merge actions.
- **Dependencies:** PR #22 branch HEAD and the existing WP1 checkpoint.

## 3. Work performed

Fetched the exact Relation, Context, Claims, Evidence Use and Source records at the starting HEAD. Inspected the ILO Practical Guide (June 2026) PDF, including its copyright page, concepts on labour attachment and international labour migration, and its core labour-market indicators for international migrants. Cross-checked the item-specific CC BY 4.0 notice against the rights delta already recorded in the WP2 consolidated status.

## 4. Files changed

| Path | Change | Reason |
|---|---|---|
| `reports/agent-work/chief-engineer/migration-labour-measurement-relation-evidence-adjudication-2026-11-20.md` | Added report-only adjudication | Record direct evidence, endpoint fit, limits and rights boundary |

## 5. Exact canonical graph

At starting HEAD `858c2ee7f9bcc0c95334d495be1e6ad026081ce7`:

- `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4`
  - `relation_type`: `migration_and_labor_measurement_link`
  - participants: `CLM-MIGRATION_AND_MOBILITY_BASICS-C@2` and `CLM-LABOR_ECONOMICS_BASICS-C@2`
  - frame: `CTX-REL-CROSS-MIGRATION-LABOR-ECONOMICS@1`, correctly targeting Relation @4.
- Migration Claim C@2: “Сравнение миграционных процессов требует уточнения определения, временного периода, территории и способа измерения потоков или запасов.”
  - `EU-MIGRATION_AND_MOBILITY_BASICS-C@2` cites UNSD *Recommendations on Statistics of International Migration and Temporary Mobility* (2025, rev. 2), Executive Summary recommendations 1–3 and Chapters 2–3, with locators and boundaries.
- Labour Economics Claim C@2: “Анализ рынка труда использует показатели занятости, заработков, рабочего времени, производительности и недоиспользования труда.”
  - `EU-LABOR_ECONOMICS_BASICS-C@2` cites ILOSTAT concepts and definitions, labour-force survey and wages/working-time databases, productivity and labour-underutilization resources. Its boundary warns that indicator definitions and periods differ and are not interchangeable without methodological checks.

The two participant Claims are conceptually compatible: migration statistics require explicit definitions, populations, time periods and stock/flow measures; labour economics measures labour-market characteristics and indicators. The question is whether a single authoritative source explicitly integrates these statistical domains.

## 6. Direct ILO evidence

**Source:** International Labour Organization, *Mapping and assessing sources for statistics of international labour migration and temporary labour mobility: ILO Practical Guide*, June 2026, ISBN 9789220434925, DOI 10.54394/00034270.

PDF: https://www.ilo.org/sites/default/files/2026-07/ILO_Guide_Mapping_ILMS_2026_FINAL.pdf

### 6.1 Direct conceptual integration

- Foreword, printed p. 8 (PDF p. 9): the Guide states that reliable statistics are needed to understand labour-mobility dynamics and assess migrants' labour-market outcomes; it recommends mapping sources, assessing data quality and comparability, and identifying gaps.
- Chapter 2, §2.2.4, printed pp. 34–37 (PDF pp. 35–38): introduces labour attachment and defines international labour migration statistics in terms of labour-market characteristics of groups of international migrants; distinguishes stocks and flows and describes changes in migrants' labour-force status.
- Box 11, printed pp. 35–36: defines working-age, employed and unemployed international migrant stocks.
- Printed p. 37: states that international labour migration statistics include labour statistics and indicators disaggregated by migration status, using country of birth and country of citizenship criteria.
- Chapter 3, Table 8, printed p. 57 (PDF p. 58): lists core labour-market indicators for international migrants, including labour-force participation, employment-to-population, unemployment and underutilization rates, status in employment, occupation and branch of economic activity.
- Chapter 4 / Chapter 5: the Guide maps data sources and recommends labour-force surveys, censuses, administrative records and other sources, while warning that no single data source captures international labour mobility in full.

This is a direct authoritative bridge between migration measurement and labour-market measurement, not merely a shared topic.

### 6.2 Exact endpoint fit

The ILO Guide directly supports the intended `migration_and_labor_measurement_link`:
- migration concepts, definitions, population groups, reference periods and stock/flow measures are explicit inputs;
- labour-force status, employment, unemployment, underemployment, earnings/working conditions and other labour-market indicators are measured for migrant groups;
- the two domains are integrated through migration-status disaggregation and labour attachment.

The current participant Claims are broad summaries, but both fall within the Guide's explicit framework. The source therefore supplies strong external semantic support for the existing Relation type and endpoints.

### 6.3 Limits that must remain visible

- The Guide focuses on international labour migration and temporary labour mobility, not every form of migration or all labour-market analysis.
- It describes statistical measurement and data-source assessment, not migration law, individual legal status, entitlement to work, or an individual migration procedure.
- It distinguishes migration stocks/flows from labour-mobility stocks/flows and explains that labour-related flows are more complex because labour-force status can change after migration.
- Labour-market statistics require disaggregation and comparability checks; definitions, reference periods, population coverage and source quality cannot be assumed interchangeable.
- The Guide notes that no single data source captures international labour mobility fully; censuses, labour-force surveys, administrative records and other sources have different coverage and limitations.

## 7. Rights and attribution screen

The exact Guide's copyright page, printed p. ii (PDF p. 2), expressly identifies **Creative Commons Attribution 4.0 International (CC BY 4.0)**. It permits reuse, sharing and adaptation subject to attribution and indicating changes. It excludes third-party materials from the licence; use of the ILO emblem/name/logo in connection with translations, adaptations or derivative works is prohibited. The page gives a specific attribution and translation/adaptation disclaimers.

This is a work-level licence for this exact 2026 Guide. It is not a licence for all ILOSTAT web pages or all ILO publications, and it does not establish compatibility with the Encyclopedia's still-undecided project licence or final distribution model. No third-party figures, photographs, tables or other assets are proposed for reuse in this review.

The source-level rights findings are already recorded in `RELEASE/FIRST-EDITION-WP2-RIGHTS-AND-ATTRIBUTION-CONSOLIDATED-STATUS-2026-11-19.md`, Cross-slice Relation source-rights follow-up — 2026-11-20. R-01–R-10 remain OPEN.

## 8. Adjudication

**Finding:** direct authoritative support is established for the existing `migration_and_labor_measurement_link`. The ILO Practical Guide integrates migration definitions and stock/flow measures with labour-force status and labour-market indicators for migrant populations. The current participant Claims are consistent with that bounded relation.

**Disposition:** the previous blocker “ILO source candidate identified, canonical linkage and independent review open” can be refined to **“direct ILO bridge verified; source-level CC BY 4.0 identified; canonical evidence linkage and independent semantic/editorial review remain open.”**

The Relation remains **HOLD**. Do not add the ILO Guide as a Source, add Evidence Use records, change Relation provenance, or alter Context without separate bounded owner authorization. The ILO 2026 Guide was not included in the prior Labour Economics Path B authorization for its 13-record graph; this is a separate cross-slice use.

## 9. Verification

| Check | Result | Notes |
|---|---|---|
| Exact Relation/Context | VERIFIED | Relation @4; Context @1 targets Relation @4 |
| Exact participant Claims | VERIFIED | Both Claim @2 statements inspected |
| Exact Evidence Use and Sources | VERIFIED | Current sources/locators and scope limits inspected |
| ILO Guide semantic bridge | VERIFIED | Foreword, Chapter 2, Box 11, Chapter 3/Table 8 and Chapter 4/5 inspected |
| ILO Guide rights notice | VERIFIED | Work-level CC BY 4.0, attribution and third-party exclusions inspected |
| Canonical changes | NONE | Report-only |
| CI | NOT RUN | No CI PASS claimed |

## 10. Unresolved issues and risks

- No independent migration-statistics / labour-statistics reviewer was engaged.
- No canonical Evidence Use links the ILO 2026 Guide to either participant Claim.
- No new Source or Relation provenance was added.
- The exact Guide licence does not close the Encyclopedia's project licence, distribution compatibility or third-party component checks.
- No owner decision R-01–R-10 is closed.
- No allowlist, candidate disposition, or publication state changed.

## 11. Recommendation and acceptance

- **Recommendation:** preserve the current Relation @4 and Context @1. If the owner authorizes canonical evidence integration, add the exact ILO 2026 Guide as a separately identified Source and link it through schema-compliant Evidence Use records to the precise participant Claims, with pinpoint locators and scope boundaries. Do not overwrite the existing UNSD and ILOSTAT source chains.
- **Acceptance status:** CONDITIONAL — direct semantic evidence and item-specific rights notice verified; canonical integration and independent review remain blocked.
- **Reason:** the ILO Guide is a direct bridge but its addition is outside the existing bounded authorization.

## 12. Handoff

- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22
- **Report path:** `reports/agent-work/chief-engineer/migration-labour-measurement-relation-evidence-adjudication-2026-11-20.md`
- **Next owner/action:** if desired, issue a separate bounded authorization for the exact ILO Source and Claim-specific Evidence Use additions; then request independent migration/labour-statistics review.

## 13. Integrity statement

- No canonical Claim, Evidence Use, Source, Relation, Context or Scope changed.
- No candidate disposition, INCLUDE/EXCLUDE, HOLD, allowlist, licence, permission, or publication state changed.
- PR #22 remains Draft and unmerged; `main` is untouched.
