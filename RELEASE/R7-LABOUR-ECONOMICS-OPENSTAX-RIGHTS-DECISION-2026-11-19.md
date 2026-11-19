# R7 Labour Economics — OpenStax Rights Conflict and Owner Decision

Date: 2026-11-19
Target branch: `mvp-public-contribution-design-2026-10-11`
Authorization under review: `REMAINING-R7-SOURCE-REMEDIATION-001`
Affected slice: `labor-economics-basics`
Status: **OWNER DECISION REQUIRED — IMPLEMENTATION HOLD; NO CANONICAL JSON CHANGED**

## 1. Executive finding

The active bounded authorization contains a materially incorrect rights statement for *Principles of Economics 3e*.

Authorization text currently states:

> “OpenStax Principles of Economics 3e is CC BY 4.0; attribution is required and third-party components are excluded.”

The current official OpenStax Preface states instead:
- the book is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0);
- reuse/modification/distribution is permitted only for noncommercial purposes, with attribution and ShareAlike obligations;
- the book may not be used in training large language models or otherwise ingested into large language models or generative-AI offerings without OpenStax's prior written permission;
- commercial use of the book's content and some components requires permission.

Official source:
`https://openstax.org/books/principles-economics-3e/pages/preface`

The authorization's CC BY 4.0 assertion is therefore not supportable and must not be relied upon.

## 2. Exact conflict location

File: `RELEASE/EDITORIAL-CORRECTION.json`

Object: `remaining_r7_remediation_2026_11_19`

Field: `basis.rights_boundary`

Incorrect clause: “OpenStax Principles of Economics 3e is CC BY 4.0…”

Correct official terms are CC BY-NC-SA 4.0 plus the separate prior-written-permission condition for LLM training/ingestion and generative-AI offerings.

The conflict affects the authorization's planned use of:
- *Principles of Economics 3e*, Chapter 14, “Introduction to Labor Markets and Income”;
- Chapter 14.1, “The Theory of Labor Markets”.

## 3. Why this is a release blocker

The Encyclopedia's final distribution/licensing model remains unresolved. A CC BY-NC-SA source cannot be treated as generally commercially reusable under CC BY 4.0. Separately, OpenStax expressly conditions LLM training/ingestion and generative-AI offering use on prior written permission.

This packet does not make a legal determination that every act of factual citation, independent paraphrase or metadata recording constitutes prohibited reuse. It does establish that the current blanket rights statement is wrong, and that the intended AI-assisted preparation and eventual distribution context requires an explicit rights decision before the source is used in the canonical remediation.

No OpenStax prose, figures, tables, exercises, images or other expressive content should be copied, translated, embedded, or used to create derivatives while this decision is pending.

## 4. Existing canonical state — confirmed unchanged

At inspection HEAD `820125dc1b470b79f2d49eb3bee2be9af2383ef0`:

| Record | Version | Blob SHA |
|---|---:|---|
| `SRC-LABOR_ECONOMICS_BASICS` | 1 | `7f0aca55f80cb830bd01d35dbee0f32b7ce60d7a` |
| `SRC-LABOR_ECONOMICS_BASICS-INDEPENDENT` | 1 | `a8df946369b79788cf88e5285b5b51ef0fd4b3e9` |
| `EU-LABOR_ECONOMICS_BASICS-A` | 1 | `f1d24559a8367fca4cd131cc7b71eeaca08ac216` |

The existing primary and independent Source records remain v1. The three records above are not modified by this decision packet.

## 5. Owner decision required

Choose and record one of the following paths in the authorization register.

### Path A — obtain explicit permission

Before using the OpenStax source in the remediation:
1. Obtain written permission from OpenStax covering the precise proposed AI-assisted processing/LLM ingestion use.
2. Obtain permission for any commercial redistribution or use that is outside CC BY-NC-SA 4.0, if the Encyclopedia's distribution model requires it.
3. Record the permission scope, grantor, date, exact permitted material/use, attribution conditions, derivative/share-alike requirements, exclusions and expiry/termination conditions.
4. Correct the authorization's rights_boundary to quote the actual CC BY-NC-SA 4.0 terms and separately reference the written permission.
5. Keep third-party images, graphs, tables, exercises and other separately credited components excluded unless their rights are independently cleared.

### Path B — replace OpenStax as the authorized primary source

1. Identify an alternative primary source for the exact Claim scope in Labour Economics Basics.
2. Verify direct support for each authorized Claim A–C, including labour-market supply/demand, wages/employment and productivity as applicable to the existing Claim statements.
3. Verify the alternative's item-level rights and AI-processing/distribution terms for the actual intended workflow.
4. Prepare exact Source/Evidence Use replacement diffs and a revised rights boundary.
5. Obtain owner approval of the replacement source and revised record-level authorization before canonical edits.

The existing authorization's ILOSTAT independent sources remain subject to item-level rights review. Their public accessibility alone is not a reuse licence.

### Path C — retain OpenStax only as a non-reproduced bibliographic reference

This path is not automatically approved. It requires an explicit owner/legal decision on whether the proposed AI-assisted research workflow and final citation-only/independent-paraphrase use fall within permitted use, and it does not remove the noncommercial/share-alike restriction if any OpenStax expression is reproduced or adapted.

## 6. Required correction to authorization text

Do not edit the authorization automatically. After the owner selects a path:

- If Path A: replace the inaccurate CC BY 4.0 clause with the exact CC BY-NC-SA 4.0 terms and a narrowly scoped written-permission record.
- If Path B: remove OpenStax from the authorized primary source list and specify the approved replacement and its rights boundary.
- If Path C: document the narrow permitted citation/metadata use and the approved AI workflow; do not imply CC BY 4.0 or blanket commercial rights.

## 7. Explicit non-actions

This document:
- does not change `EDITORIAL-CORRECTION.json`;
- does not revoke or expand any authorization;
- does not change any canonical Source, Claim, Evidence Use, Relation, Context or Scope;
- does not assign INCLUDE/EXCLUDE or change the allowlist;
- does not establish legal clearance;
- does not authorize use of OpenStax material by an LLM or generative-AI offering.

Labour Economics Basics remains HOLD.

## 8. Release and implementation gates

Implementation remains blocked until the owner decision is recorded, the authorization is corrected, exact item-level rights are documented, and the approved source chain is re-fetched and diffed against a frozen HEAD. Even after those steps, the slice remains HOLD pending independent editorial review, Human View and the full release gates.

**Decision status:** pending owner decision. No canonical JSON changed.
