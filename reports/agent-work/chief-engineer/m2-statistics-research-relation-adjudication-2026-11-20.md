# M2 Statistics / Research Relation — Focused Endpoint and Evidence Adjudication

- **Agent:** chief-engineer
- **Task:** Focused WP1 adjudication of the M2 Statistics / Research Relation
- **Date (UTC):** 2026-11-20
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** mvp-public-contribution-design-2026-10-11
- **Starting HEAD:** faa03c994704f36e05997b81a20bca359f9027eb
- **Pre-final report HEAD:** 5d43e2ccd41d377f9f22825e0e103761a70de333
- **Status:** VERIFIED — exact records and official source pages inspected; CI not run for documentation-only change

## 1. Request and acceptance criteria

Continue WP1 without repeating completed audits. Adjudicate one existing semantic HOLD using exact current records and authoritative sources. Preserve canonical data and HOLD unless exact owner authorization exists.

## 2. Scope

- **In scope:** one Relation, its two participant Claims, their Evidence Use and Source records, its target-specific Context, and direct primary-source cross-checks.
- **Out of scope:** canonical mutation, endpoint replacement, new Source/Evidence Use, candidate disposition, rights clearance, WP2 owner decisions, and release/merge actions.
- **Dependencies:** exact PR branch HEAD and the current WP1 semantic-HOLD checkpoint.

## 3. Work performed

Fetched the exact Relation, both Claims, both Evidence Use records, both Source records, and target Context at the starting HEAD. Cross-checked NIST and National Academies official source pages and relevant chapters. Recorded the endpoint mismatch and the narrower supportable conceptual connections. Committed this report-only finding to the existing PR #22 branch and linked it from the Draft PR description.

## 4. Files changed

| Path | Change | Reason |
|---|---|---|
| `reports/agent-work/chief-engineer/m2-statistics-research-relation-adjudication-2026-11-20.md` | Added/expanded report-only adjudication | Durable record of exact endpoint/evidence findings |

## 5. Findings and evidence

### 5.1 Exact current canonical graph

At inspection HEAD `faa03c994704f36e05997b81a20bca359f9027eb`:

- `REL-CROSS-M2-STATISTICS-RESEARCH@3`
  - `relation_type`: `statistics_and_research_design_link`
  - participant 1: `CLM-STATISTICS_BASICS-C@1`
  - participant 2: `CLM-RESEARCH_METHODS_BASICS-B@2`
  - roles: `m2_foundation_claim`, `linked_domain_claim`
  - frame: `CTX-REL-CROSS-M2-STATISTICS-RESEARCH@2`, whose `target_ref` correctly points to Relation @3.
- `CLM-STATISTICS_BASICS-C@1` states: “Экспериментальный дизайн и анализ данных связаны: качество вывода зависит не только от вычислений, но и от постановки исследования.”
  - `EU-STATISTICS_BASICS-C@1` references `SRC-STATISTICS_BASICS@1` (NIST/SEMATECH Engineering Statistics Handbook), but has no pinpoint locator and only a generic material description.
- `CLM-RESEARCH_METHODS_BASICS-B@2` states: “Воспроизводимость и реплицируемость являются важными аспектами оценки надёжности научных результатов.”
  - `EU-RESEARCH_METHODS_BASICS-B@3` references `SRC-RESEARCH_METHODS_BASICS@1` (National Academies, *Reproducibility and Replicability in Science*), with a locator to Chapter 3, pp. 42–46 and Box 3-1, p. 48. Its stated boundary concerns definitions of reproducibility/replicability and the distinction from metrological repeatability.

The participant pair combines an experimental-design/data-analysis proposition with a reproducibility/replicability proposition. The declared Relation type says “research design”, but the Research Methods B endpoint does not make a research-design proposition.

### 5.2 NIST: statistical methods and experimental design

NIST's official description of the NIST/SEMATECH e-Handbook says it is intended to help scientists and engineers design experiments and carry out appropriate statistical analyses, and to help users understand the assumptions underlying statistical procedures.

Locator: https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook

This supports the general subject matter of the Statistics endpoint. It does not, by itself, turn the current Research Methods B reproducibility Claim into a research-design Claim.

### 5.3 National Academies: statistical inference within scientific inquiry

Chapter 2 of the National Academies work already cited by the Research Methods source states that statistical inference is part of the broader process by which scientific knowledge is gained, questioned and modified. The chapter describes estimation and hypothesis testing as frameworks for answering scientific questions.

Locator: https://www.nationalacademies.org/read/25303/chapter/5

This is a direct conceptual bridge between statistical inference and scientific inquiry. However, the current canonical Evidence Use B points to Chapter 3, not Chapter 2; the Chapter 2 locator is not currently recorded in that Evidence Use.

### 5.4 National Academies: statistical analysis and reproducibility practice

Chapter 6, Recommendation 6-1, says research reporting should describe methods and data-analysis decisions, and, where results depend on statistical inference, should describe analytic decisions and whether a study is exploratory or confirmatory. Recommendation 6-2 addresses proper training in statistical analysis and inference.

Locator: https://www.nationalacademies.org/read/25303/chapter/14

This supplies a real methodological connection between statistical inference and transparent/reproducible research practice. It is not equivalent to saying that the current pair establishes a research-design relation. The connection is more accurately framed as statistics/inference ↔ research reporting, rigor and reproducibility.

## 6. Adjudication

**Finding:** the existing HOLD rationale is confirmed and can be made more precise.

- The current endpoints do not establish the declared `statistics_and_research_design_link`.
- Authoritative external material confirms meaningful connections between statistical inference, scientific inquiry, and transparent/reproducible research practice.
- Those connections do not cure the endpoint mismatch: the current Research Methods B Claim is specifically about reproducibility and replicability, not research design.
- The current Evidence Use records do not contain the newly identified pinpoint locators for the NIST handbook overview or National Academies Chapters 2 and 6.
- A different Relation type and/or a different Research Methods participant might be more defensible, but either would change canonical semantics and requires a separate bounded owner authorization plus independent editorial review.

**Disposition:** retain `REL-CROSS-M2-STATISTICS-RESEARCH@3` and affected slices on **HOLD**. Do not promote it to a contextual-navigation candidate on this evidence alone. Do not substitute endpoints, broaden Claims, or silently add locators/provenance.

## 7. Rights and reuse boundary

This research uses source identities and links only. No National Academies chapter text, PDF, tables, figures, or other expressive material is proposed for reproduction. The National Academies rights restrictions already recorded in the project remain applicable; source access and citation do not clear expressive reuse. NIST material must likewise be screened at item level before any reproduction; public accessibility is not treated as a blanket licence.

No project-level rights decision (R-01–R-10) is closed by this review.

## 8. Commands and verification

| Check | Result | Exact SHA / URL | Notes |
|---|---|---|---|
| Exact canonical record inspection | VERIFIED | `faa03c994704f36e05997b81a20bca359f9027eb` | Relation, Claims, EU, Sources, Context fetched from PR branch |
| Primary-source cross-check | VERIFIED | NIST handbook; National Academies Chapters 2 and 6 (links above) | Official source pages inspected |
| GitHub Actions workflow runs | NOT RUN | `5d43e2ccd41d377f9f22825e0e103761a70de333` | No PR workflow runs returned for this documentation-only change |
| Commit combined status | NOT RUN | `5d43e2ccd41d377f9f22825e0e103761a70de333` | No commit statuses returned; no CI PASS claimed |
| PR state | VERIFIED | https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22 | OPEN, Draft, unmerged; latest fetched state reported mergeable=true before this final report-only update |

No test command was run locally. No CI PASS is claimed for this report-only change.

## 9. Unresolved issues, risks, and not done

- No independent subject-matter reviewer was engaged; this is not an independent expert sign-off.
- No canonical evidence locator was added.
- No rights permission or project licence was established.
- No workflow CI PASS is claimed for this documentation-only change.
- No PR rebase/update, merge, main change, allowlist, or release action was performed.

## 10. Recommendation and acceptance

- **Recommendation:** retain Relation @3 and Context @2 on HOLD; require an owner choice of intended semantics before any canonical adjustment.
- **Acceptance status:** CONDITIONAL — research adjudication complete; canonical resolution and independent review remain blocked.
- **Reason:** exact endpoint mismatch is verified, but the evidence supports narrower alternate concepts, not the current declared relation type.

## 11. Handoff

- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22
- **Report path:** `reports/agent-work/chief-engineer/m2-statistics-research-relation-adjudication-2026-11-20.md`
- **Next owner/action:** choose the intended semantic relation only if this link is to be repaired; then issue exact bounded authorization and obtain independent editorial review.
- **Final report revision:** committed on the PR branch; the exact resulting commit SHA is the final HEAD recorded in the PR.

## 12. Integrity statement

- No canonical Claim, Evidence Use, Source, Relation, Context or Scope changed.
- No candidate disposition, INCLUDE/EXCLUDE, HOLD, allowlist, licence, permission, or publication state changed.
- PR #22 remains Draft and unmerged; `main` is untouched.
