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


## 9. Follow-up — official asset-level discrepancy (2026-11-19)

A fresh comparison found an additional conflict within OpenStax-hosted materials for the same book:

- The current official HTML Preface states CC BY-NC-SA 4.0 and the prior-written-permission restriction for LLM training/ingestion: https://openstax.org/books/principles-economics-3e/pages/preface
- OpenStax's official licensing help page states that OpenStax textbooks use CC BY-NC-SA: https://help.openstax.org/s/article/Licensing-information-of-OpenStax-textbooks
- A separately indexed OpenStax-hosted PDF asset for *Principles of Economics 3e* displays a CC BY 4.0 notice: https://assets.openstax.org/oscms-prodcms/media/documents/principles-economics-3e_-_WEB.pdf

This is an asset/edition-level inconsistency in official OpenStax materials. It does not justify selecting the more permissive notice by default. The authorization must identify the exact file/edition and obtain written clarification from OpenStax about the applicable licence and the separate AI-processing restriction. Until then, treat the rights status as unresolved and do not use the CC BY 4.0 clause.

The current branch recheck confirms the complete Labour Economics graph is still 13/13 records at v1, with both Source branches and all dependent references aligned at v1. No canonical record was changed. This follow-up does not select Path A, B or C above.


## 10. Follow-up — authorization rights-boundary correction and replacement-source research — 2026-11-19

The known inaccurate CC BY 4.0 statement in `RELEASE/EDITORIAL-CORRECTION.json` has now been corrected conservatively. The authorization's `basis.rights_boundary` records the unresolved HTML-Preface/PDF-asset conflict and the separate prior-written-permission condition for LLM training/ingestion and generative-AI offerings. A new explicit prohibition prevents Labour Economics canonical changes dependent on OpenStax until the owner records Path A, B or C. This is a documentation/scope-safety correction only; it does not select a rights path or grant permission.

A separate check found that *Principles of Economics 2e* is not an automatic workaround: its official HTML Preface begins with CC BY 4.0 but its “Citation/Attribution” section states noncommercial/ShareAlike conditions and prior written permission for LLM training/ingestion.

A BLS-based alternative has been researched:
- BLS official copyright page says its publications are public domain except previously copyrighted photographs and illustrations; cite BLS and do not use its emblem.
- BLS Monthly Labor Review (2024) provides a U.S.-specific labour-market definition (geography × industry/occupation).
- BLS ECEC help page distinguishes employer costs for wages/salaries and benefits.
- BLS Information Guide covers productivity, hours, employment and labour costs.
- BLS CPS definitions cover U-1–U-6 labour-underutilization measures.

The BLS alternative is promising for text-only factual paraphrase but remains U.S.-specific and does not alone support every general/global Claim. The independent international source must be separately rights-screened. ILO Open Access CC BY 4.0 applies automatically only to ILO knowledge products published or made available on/after 3 May 2023 unless otherwise indicated; exact page dates and third-party components require verification.

Full research and proposed source-to-Claim mapping: `reports/agent-work/chief-engineer/r7-labour-economics-rights-compatible-source-options-2026-11-19.md`.

No canonical Labour record was changed. The 13-record graph remains v1, aligned and HOLD. Path A/B/C remains an owner decision.


## 11. Superseding owner decision — ILO Path B selected and implemented (2026-11-20)

This section supersedes the prior “OWNER DECISION REQUIRED — IMPLEMENTATION HOLD” and the pending Path A/B/C status above for the bounded `labor-economics-basics` remediation only.

The project owner explicitly selected **Path B — ILO-led replacement source chain** on 2026-11-20. The bounded authorization is recorded as `R7-LABOUR-ECONOMICS-ILO-PATH-B-OWNER-DECISION-2026-11-20` in `RELEASE/EDITORIAL-CORRECTION.json`.

Current implementation has been re-fetched at PR HEAD `c177cbf0def595b4d478d0eddb512db5b33c18d4`:
- 13/13 authorized canonical records are current version @2: two Source, three Claim, six Evidence Use, one Context and one Scope.
- The primary Source @2 is an ILOSTAT reference hub. It explicitly does **not** assert CC BY 4.0 for the referenced ILOSTAT web pages because their item-level publication dates/licences are not established; use factual paraphrase and citations only.
- The independent Source @2 is ILO *World Employment and Social Outlook 2023: The value of essential work*, DOI 10.54394/OQVF7543, with an explicit CC BY 4.0 notice in the report PDF. Third-party cover photography/assets are excluded; ILO attribution is required; the ILO emblem is not used.
- All six Evidence Use records @2 resolve to the exact current Claim @2 and the corresponding primary/independent Source @2. The Context and Scope @2 target Claim A@2.
- The two explicitly named dependent Relations are now @4 and resolve to Labour Claim C@2; their relation-specific Context @1 records target the exact Relation @4. The direct Claim provenance pattern was expressly included in the owner-approved bounded Path B authorization for those two Relations.
- No OpenStax Source or Evidence Use remains in the current Labour Economics graph.

Read-only verification report:
`reports/agent-work/chief-engineer/r7-labour-economics-ilo-path-b-exact-record-and-rights-verification-2026-11-20.md`.

### Important separation

The separate ILO 2026 *Mapping and assessing sources for statistics of international labour migration and temporary labour mobility* guide has now been identified as a promising direct source for the Migration/Labour cross-slice Relation and its own PDF states CC BY 4.0. It is **not** one of the 13 records in the Path B authorization and has not been added to the Labour Economics graph. Adding it as a Source/Evidence Use or Relation provenance reference requires a separate bounded authorization.

### Current disposition

The OpenStax-specific blocker for the Labour Economics source chain is superseded by the owner-selected ILO Path B. This does **not** close the item-level rights question for ILOSTAT pages, adopt the Encyclopedia's own content licence, or establish distribution compatibility.

Labour Economics Basics and both dependent Relations remain **HOLD** pending independent labour-economics/statistical editorial review, project-level rights/distribution review, Human View and the remaining first-edition release gates. No INCLUDE, EXCLUDE, allowlist, publication, deployment, merge or main-branch change was made.
