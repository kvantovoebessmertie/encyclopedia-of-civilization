# M2 Statistics / Research Relation — Focused Endpoint and Evidence Adjudication

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Inspection HEAD before this report: `faa03c994704f36e05997b81a20bca359f9027eb`  
Scope: `REL-CROSS-M2-STATISTICS-RESEARCH` only  
Status: **ENDPOINT MISMATCH CONFIRMED; SUPPORTING CROSS-DOMAIN MATERIAL EXISTS FOR A DIFFERENT, NARROWER LINK; CURRENT RELATION REMAINS HOLD; REPORT-ONLY**

## 1. Request and acceptance criteria\n\nContinue WP1 without repeating closed audits; adjudicate one existing semantic HOLD using exact current records and authoritative sources. Preserve canonical data and HOLD unless an exact owner authorization exists.\n\n## 2. Scope\n- In scope: one Relation, its two participant Claims, their Evidence Use and Source records, its target-specific Context, and direct primary-source cross-checks.\n- Out of scope: canonical mutation, endpoint replacement, new Source/Evidence Use, candidate disposition, rights clearance, WP2 owner decisions, and release/merge actions.\n- Dependencies: exact branch HEAD and current WP1 semantic-HOLD checkpoint.\n\n## 3. Work performed\n\nFetched the exact Relation, both Claims, both Evidence Use records, both Source records, and target Context at the starting HEAD. Cross-checked NIST and National Academies primary-source descriptions and relevant chapters. Recorded the endpoint mismatch and the narrower supportable conceptual connections.\n\n## 4. Files changed\n| Path | Change | Reason |\n|---|---|---|\n| `reports/agent-work/chief-engineer/m2-statistics-research-relation-adjudication-2026-11-20.md` | Added and expanded report-only adjudication | Durable record of exact endpoint/evidence findings |\n\n## 5. Findings and evidence\n\n

This is a report-only WP1 adjudication. It does not modify canonical Claim, Evidence Use, Source, Relation, Context, Scope, rights, candidate disposition, allowlist, or publication state. It does not authorize endpoint substitution, a new Source/Evidence Use, a Relation version, or an INCLUDE/EXCLUDE decision. The Relation and affected slices remain HOLD.

## 2. Exact current canonical graph

At inspection HEAD `faa03c994704f36e05997b81a20bca359f9027eb`:

- `REL-CROSS-M2-STATISTICS-RESEARCH@3`
  - `relation_type`: `statistics_and_research_design_link`
  - participant 1: `CLM-STATISTICS_BASICS-C@1`
  - participant 2: `CLM-RESEARCH_METHODS_BASICS-B@2`
  - roles: `m2_foundation_claim`, `linked_domain_claim`
  - frame: `CTX-REL-CROSS-M2-STATISTICS-RESEARCH@2`, whose `target_ref` correctly points to Relation @3.
- `CLM-STATISTICS_BASICS-C@1` states: “Экспериментальный дизайн и анализ данных связаны: качество вывода зависит не только от вычислений, но и от постановки исследования.”
  - Its `EU-STATISTICS_BASICS-C@1` references `SRC-STATISTICS_BASICS@1` (NIST/SEMATECH Engineering Statistics Handbook) but has no pinpoint locator and only a generic material description.
- `CLM-RESEARCH_METHODS_BASICS-B@2` states: “Воспроизводимость и реплицируемость являются важными аспектами оценки надёжности научных результатов.”
  - Its `EU-RESEARCH_METHODS_BASICS-B@3` references `SRC-RESEARCH_METHODS_BASICS@1` (National Academies, *Reproducibility and Replicability in Science*), with a locator to Chapter 3, pp. 42–46 and Box 3-1, p. 48. Its stated boundary concerns definitions of reproducibility/replicability and the distinction from metrological repeatability.

The participant pair therefore combines an experimental-design/data-analysis proposition with a reproducibility/replicability proposition. The declared Relation type says “research design”, but the Research Methods endpoint does not make a research-design proposition.

## 3. External primary-source cross-check

### 3.1 NIST: statistical methods and experimental design

NIST's official description of the NIST/SEMATECH e-Handbook says it is intended to help scientists and engineers design experiments and carry out appropriate statistical analyses, and to help users understand the assumptions underlying statistical procedures.

Locator: https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook

This supports the general subject matter of the Statistics endpoint. It does not, by itself, turn the current Research Methods B reproducibility Claim into a research-design Claim.

### 3.2 National Academies: statistical inference within scientific inquiry

Chapter 2 of the same National Academies work already cited by the Research Methods source states that statistical inference is part of the broader process by which scientific knowledge is gained, questioned and modified. The chapter describes estimation and hypothesis testing as frameworks for answering scientific questions.

Locator: https://www.nationalacademies.org/read/25303/chapter/5

This is a direct conceptual bridge between statistical inference and scientific inquiry. However, the current canonical Evidence Use B points to Chapter 3, not Chapter 2; the Chapter 2 locator is not currently recorded in that Evidence Use.

### 3.3 National Academies: statistical analysis and reproducibility practice

Chapter 6, Recommendation 6-1, says research reporting should describe methods and data-analysis decisions, and, where results depend on statistical inference, should describe analytic decisions and whether a study is exploratory or confirmatory. Recommendation 6-2 addresses proper training in statistical analysis and inference.

Locator: https://www.nationalacademies.org/read/25303/chapter/14

This supplies a real methodological connection between statistical inference and transparent/reproducible research practice. It is not equivalent to saying that the current pair establishes a research-design relation. The connection is more accurately framed as statistics / inference ↔ research reporting, rigor and reproducibility.

## 6. Adjudication

**Finding:** the existing HOLD rationale is confirmed and can be made more precise.

- The current endpoints do not establish the declared `statistics_and_research_design_link`.
- Authoritative external material confirms meaningful connections between statistical inference, scientific inquiry, and transparent/reproducible research practice.
- Those connections do not cure the endpoint mismatch: the current Research Methods B Claim is specifically about reproducibility and replicability, not research design.
- The current Evidence Use records do not contain the newly identified pinpoint locators for the NIST handbook overview or National Academies Chapters 2 and 6.
- A different Relation type and/or a different Research Methods participant might be more defensible, but either would change canonical semantics and requires a separate bounded owner authorization plus independent editorial review.

**Disposition:** retain `REL-CROSS-M2-STATISTICS-RESEARCH@3` and affected slices on **HOLD**. Do not promote it to a contextual-navigation candidate on this evidence alone. Do not substitute endpoints, broaden Claims, or silently add locators/provenance.

## 7. Rights and reuse boundary

This research uses source identities and links only. No National Academies chapter text, PDF, tables, figures, or other expressive material is proposed for reproduction. The National Academies rights restrictions already recorded in the project remain applicable; source access and citation do not clear expressive reuse. NIST material must likewise be screened at item level before any reproduction, and the fact that the NIST page is publicly accessible is not treated here as a blanket licence.

No project-level rights decision (R-01–R-10) is closed by this review.

## 8. Exact next actions

1. Preserve the current canonical graph and HOLD state.
2. If the owner wants this conceptual connection represented, first choose the intended relation semantics: research design, statistical inference within scientific inquiry, or statistics and reproducible research practice. These are not interchangeable.
3. Only after that choice, obtain a bounded authorization naming exact record IDs, versions, permitted fields, and whether a new Source/Evidence Use or participant alignment is allowed.
4. Require independent scientific/editorial review of the selected endpoint pair and its limits.
5. Screen the exact proposed source material under WP2 before any edition inclusion decision.

## 9. Commands and verification\n\n| Check | Result | Exact SHA / URL | Notes |\n|---|---|---|\n| Exact canonical record inspection | VERIFIED | `faa03c994704f36e05997b81a20bca359f9027eb` | Relation, Claims, EU, Sources, Context fetched from PR branch |\n| Primary-source cross-check | VERIFIED | NIST handbook; National Academies Chapters 2 and 6 (links above) | External primary sources inspected via official pages |\n| GitHub Actions workflow runs | NOT RUN / no runs returned | `96d67e46a6b50b7a84d6ec3c9594901a37db920f` | Documentation-only path did not produce PR workflow runs in the queried endpoint |\n| Commit combined status | NOT RUN / no statuses returned | `96d67e46a6b50b7a84d6ec3c9594901a37db920f` | Empty status collection; do not describe as CI PASS |\n| PR integration state | BLOCKED for mergeability | https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22 | PR remains Draft; mergeable=false; current main is 8 commits ahead of merge base; no update/rebase performed |\n\n## 10. Unresolved issues, risks, and not done\n\n- No independent subject-matter reviewer was engaged; the report is not an independent expert sign-off.\n- No canonical evidence locator was added.\n- No rights permission or project licence was established.\n- No workflow CI PASS is claimed for this documentation-only commit.\n- No PR rebase/update, merge, main change, allowlist, or release action was performed.\n\n## 11. Recommendation and acceptance\n- **Recommendation:** retain Relation @3 and Context @2 on HOLD; require an owner choice of intended semantics before any canonical adjustment.\n- **Acceptance status:** CONDITIONAL — research adjudication complete; canonical resolution and independent review remain blocked.\n- **Reason:** exact endpoint mismatch is verified, but the evidence supports narrower alternate concepts, not the current declared relation type.\n\n## 12. Handoff\n- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22\n- **Report path:** `reports/agent-work/chief-engineer/m2-statistics-research-relation-adjudication-2026-11-20.md`\n- **Next owner/action:** choose the intended semantic relation only if this link is to be repaired; then issue exact bounded authorization and obtain independent editorial review.\n\n## 13. Integrity statement

- No canonical records changed.
- No Claim wording, Evidence Use, Source, Relation or Context changed.
- No candidate disposition, INCLUDE/EXCLUDE, HOLD, allowlist, licence, permission, or publication state changed.
- PR #22 remains Draft and unmerged; `main` is untouched.
