# MVP pilot candidate screen — acid-base basics (OpenStax rights gate)

Date: 2026-10-11
Branch: `mvp-public-contribution-design-2026-10-11`
Status: **HOLD — source fit is strong, but licensing and AI-use terms are a release blocker**

## 1. Candidate inspected

The existing slice `acid-base-basics` contains three introductory Claims and separate Evidence Use records linked to `SRC-ACID_BASE_BASICS@1`, which identifies OpenStax *Chemistry 2e*, Chapter 14 Summary:
https://openstax.org/books/chemistry-2e/pages/14-summary

The Claims are:
- A: Brønsted–Lowry acid donates a proton and base accepts a proton.
- B: pH is defined through hydrogen-ion activity; concentration is only an approximation under explicitly limited conditions.
- C: a buffer contains a conjugate acid-base pair and resists small pH changes when small amounts of acid/base are added.

## 2. Source fit and specific locators

OpenStax Chapter 14 Summary contains direct text for:
- Claim A — subsection heading **14.1 Brønsted-Lowry Acids and Bases**, opening paragraph: the acid donates a proton and the base accepts it.
- Claim B — subsection heading **14.2 pH and pOH**. The current summary emphasizes hydronium concentration and logarithmic pH; the canonical Claim is more nuanced because it refers to activity. This summary alone is not sufficient for the full activity-based formulation; the relevant full textbook section and exact thermodynamic definition would need review.
- Claim C — subsection heading **14.6 Buffers**, opening paragraph: buffer solutions contain a weak conjugate acid-base pair and show only slight pH changes after small additions of acid or base.

Source fit is therefore strong for A and C, partial for B. These are stable section-level locators for screening, not yet approved canonical Evidence Use pinpoints.

## 3. Rights gate — decisive blocker

The OpenStax page's own “Citation/Attribution” section states that:
- the textbook uses a Creative Commons Attribution-NonCommercial-ShareAlike license for reuse/redistribution;
- derivative works must be shared under the same license and attributed;
- commercial use requires permission; and
- the book may not be used in training large language models or otherwise ingested into LLM/generative-AI offerings without prior written permission.

These conditions mean that the encyclopedia must not assume the source is freely reusable for any public edition. The project's intended publication model, derivative status, commercial/noncommercial status, attribution obligations and AI-use permission must be decided and documented before this source can pass the release gate. Do not copy or redistribute textbook prose/figures in the preview while this remains unresolved. This note does not make a legal determination about whether a particular independent paraphrase is a derivative work.

## 4. Eligibility decision

**Decision: HOLD.** This candidate is not approved for the MVP pilot.

| Gate | Status | Reason |
|---|---|---|
| Claim/source fit | Partial | A and C direct; B requires a more precise source passage on activity. |
| Exact Evidence Use pinpoint | Partial | Section headings found; reproducible claim-specific locators still need recording. |
| Rights / attribution | FAIL / unresolved | NonCommercial-ShareAlike conditions and explicit AI-ingestion restriction need project-level resolution and, if required, permission. |
| Exact-version manifest | FAIL | No real-record allowlist approved. |
| Human View and editorial sign-off | UNKNOWN | No reviewed real-record artifact exists. |

## 5. Next action

Do not prioritize this slice as the first public pilot until the project's licensing model is settled. Prefer a candidate whose source rights and permitted uses clearly match the intended public edition, but still check exact source pinpoints, privacy, attribution and Human View before inclusion.

No canonical Claim, Evidence Use or Source record changed. No real-record preview allowlist was created.
