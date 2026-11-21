# M13 — calculus basics: OpenStax passage and rights reassessment

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Review class: follow-up source-passage and rights reassessment; **not new first-pass Claim coverage**. The three Claims appear in Batch 41, scored block 06, but the exact passage locators and the OpenStax AI-ingestion restriction were not resolved there.

## 1. Exact records and prior-review reconciliation

| Claim | Evidence Use | Source | Version |
|---|---|---|---|
| `CLM-CALCULUS_BASICS-A` | `EU-CALCULUS_BASICS-A` | `SRC-CALCULUS_BASICS` | v1 / v1 / v1 |
| `CLM-CALCULUS_BASICS-B` | `EU-CALCULUS_BASICS-B` | `SRC-CALCULUS_BASICS` | v1 / v1 / v1 |
| `CLM-CALCULUS_BASICS-C` | `EU-CALCULUS_BASICS-C` | `SRC-CALCULUS_BASICS` | v1 / v1 / v1 |

The three Claim → EU → Source links are internally consistent. The Source identity is only a generic sentence (“Математический анализ описывает изменение и накопление величин.”); the URI points to the OpenStax book landing page, not to claim-specific sections. All three EUs use the same generic description and contain no section/page pinpoint.

Prior coverage is a Batch 41 scoring-block mention, not a separate first-pass source-passage report. This reassessment adds precise passage mapping but does not create new D/E/B scoring rows or count the Claims as new first-pass coverage.

## 2. Passage-level support

OpenStax, *Calculus Volume 1*, Gilbert Strang and Edwin “Jed” Herman, published 30 March 2016. Official book page:
https://openstax.org/books/calculus-volume-1/pages/preface

### Claim A — limit and approach

Claim: “Предел описывает поведение функции при приближении аргумента к заданному значению.”

**Assessment: DIRECT.**
- §2.2, “The Limit of a Function”: introduces the intuitive definition of a limit in terms of function values approaching a value as the argument approaches a point.
- §2.5, “The Precise Definition of a Limit”: formalizes the same idea with the epsilon-delta definition, including the condition that the argument is close to but not equal to the target value.

**Proposed locator:** OpenStax Calculus Volume 1, Chapter 2, §§2.2 and 2.5.

### Claim B — derivative and instantaneous rate of change

Claim: “Производная характеризует мгновенную скорость изменения функции при выполнении условий существования.”

**Assessment: DIRECT.**
- §3.1, “Defining the Derivative”: defines the instantaneous rate of change of a function at a value as its derivative.
- §3.2, “The Derivative as a Function”: defines the derivative through the limit of the difference quotient and specifies that the derivative exists where the relevant limit exists.
- Chapter 3 key concepts connect instantaneous velocity to the derivative of the position function.

The Claim's explicit existence condition is appropriate and avoids implying differentiability at every point.

**Proposed locator:** OpenStax Calculus Volume 1, Chapter 3, §§3.1–3.2.

### Claim C — definite integral and accumulation

Claim: “Определённый интеграл используется для описания накопления величины при соответствующих условиях.”

**Assessment: DIRECT at the stated level, with the condition preserved.**
- §5.2, “The Definite Integral”: defines the definite integral through the limit of Riemann sums, provided that limit exists; explains the relationship to area/net signed accumulation.
- §5.4, “Integration Formulas and the Net Change Theorem”: states that when a quantity changes, its final value equals its initial value plus the integral of its rate of change.
- §5.3, “The Fundamental Theorem of Calculus”: connects differentiation and integration.

“При соответствующих условиях” is essential: the definite integral is not a universal accumulation operator for arbitrary functions without integrability and model assumptions.

**Proposed locator:** OpenStax Calculus Volume 1, Chapter 5, §§5.2–5.4, especially §5.4, “The Net Change Theorem.”

## 3. Rights and ingestion gate — decisive blocker

The book's own Preface states:
- the book is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0);
- redistribution/adaptation requires attribution, noncommercial use and ShareAlike compliance;
- the book may not be used to train large language models or otherwise be ingested into large language models or generative-AI offerings without OpenStax's prior written permission.

Official rights statement: https://openstax.org/books/calculus-volume-1/pages/preface

The public CC BY-NC-SA licence does **not** override the book's explicit additional AI-ingestion restriction. Open access and permission to link to a chapter do not establish permission to ingest or reproduce the content in this project or any generative-AI workflow.

**Disposition: HOLD.** Do not copy, adapt, ingest or add the OpenStax passages to the Encyclopedia's knowledge corpus or an AI ingestion/training pipeline without prior written permission from OpenStax. A citation/link-only reference may be considered separately, subject to attribution and legal review; it does not cure the ingestion restriction. The safe path is to obtain written permission or replace the source with a rights-compatible source whose licence and intended uses are verified.

## 4. Proposed remediation — not applied

Subject to a bounded authorization:
1. Replace the generic Source identity with the full bibliographic identity and stable book URL only if the project is authorized to retain a citation-only reference.
2. Add the section locators above to the three EUs only after the rights path is resolved.
3. If permission is not obtained, replace the OpenStax Source/EUs with independently verified, rights-compatible sources for limits, derivatives and definite integrals; do not merely change the URL while retaining OpenStax-derived text.
4. Preserve the Claim wording only if the replacement sources support the same definitions and existence/integrability conditions.
5. Preserve historical D/E/B scores and Batch 41 reports append-only.

## 5. Disposition and integrity

| Measure | Result |
|---|---:|
| Claims re-assessed | 3 |
| Previously scored in Batch 41 | 3 |
| New first-pass Claim coverage | 0 |
| Direct passage support at stated scope | 3 |
| Generic EU descriptions replaced | 0 |
| Canonical Source/EU/Claim JSON changed | 0 |
| Canonical pinpoint locators added | 0 |
| Historical D/E/B scores changed | 0 |
| Written OpenStax permission obtained | 0 |
| Rights-cleared for AI ingestion | 0 |
| Claims accepted or release-cleared | 0 |

All three Claims remain HOLD until the explicit OpenStax AI-ingestion restriction is resolved through written permission or a rights-compatible replacement source. This report documents mathematical source fit; it does not authorize ingestion, canonical edits or publication.
