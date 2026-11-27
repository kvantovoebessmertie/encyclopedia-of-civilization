# First Edition — Consolidated Owner Decision Packet (R-01–R-10)

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
Status: **FOR OWNER DECISION — no option below is adopted by this document.**

## Purpose

This is the short decision surface for the ten owner-level blockers already documented in `FIRST-EDITION-RIGHTS-EDITORIAL-OWNER-DECISION-REGISTER-2026-11-19.md`. It avoids asking the owner to reread the full research register. It does not grant rights, appoint people, approve records, or authorize publication.

## Recommended conservative operating baseline

The defaults below are recommendations designed to let technical and editorial preparation continue without implying rights or authority that have not been established.

| ID | Decision required | Conservative proposal for Edition 1 | What the owner must supply |
|---|---|---|---|
| R-01 | Rights holder / authority | Do not infer ownership from repository control or authorship metadata. Record the actual person/entity with authority over project-authored material. | Exact legal name and basis of authority; identify any co-owners or excluded material. |
| R-02 | Project text/data licence | Until R-01 is resolved, publish no blanket licence. After authority is confirmed, consider CC BY 4.0 for only original project-authored text and structured data, excluding third-party material, personal data, trademarks and software. If the owner does not want reuse, choose an explicit proprietary/all-rights-reserved notice instead. | Choose CC BY 4.0 (scoped) or proprietary/no public reuse; confirm commercial reuse policy and covered assets. |
| R-03 | Software licence | Keep code legally separate from content. A permissive licence such as MIT may be considered only after code ownership and third-party dependency notices are checked. | Select exact code licence or explicitly keep code unlicensed/proprietary; confirm authority. |
| R-04 | Contributor terms | Do not accept hosted submissions or imply that local JSON export transfers rights. Keep contributions as proposals pending human review and a separate explicit grant/permission. | Approve a contributor agreement before accepting contributions for publication; otherwise keep intake disabled/manual and non-binding. |
| R-05 | Third-party source reuse | Factual paraphrase plus citation/link only as the default; no copied prose, images, diagrams, maps, tables or datasets absent item-specific permission/licence and attribution review. Public accessibility is not permission. | Approve this restrictive default or specify a narrower/stronger rule; exceptions require item-level evidence. |
| R-06 | Accountable editor | Name one accountable editorial owner; subject experts approve only the subject matter they actually review. | Full name or accountable legal entity, role, scope and escalation route. |
| R-07 | Release approver | Require a separate, recorded approval for each immutable edition bundle. CI and AI checks are never the approver. | Name the person/entity authorized to approve or halt a release. |
| R-08 | Corrections / disputes / withdrawal | No public contact should be invented. Until a monitored channel exists, do not claim a public correction service or SLA; use a controlled private channel for internal testing only. | Monitored email/form/issue channel, responsible monitor, response target, urgent takedown authority and appeal route. |
| R-09 | Attribution / authorship | Distinguish author, contributor, editor, translator, reviewer, rights holder and AI/tool assistance. Credit must not imply ownership or endorsement. | Approve a concise attribution policy and whether AI/tool assistance is disclosed at edition level. |
| R-10 | Rights evidence register | Maintain an item-level, version-pinned register with source/material, licence/permission, territory, term, restrictions, attribution, reviewer, evidence URI and review/expiry date. | Confirm system of record and accountable maintainer; require evidence before any item leaves HOLD. |

## Decision dependencies and safe sequencing

1. R-01 precedes R-02 and R-03: a licence cannot be granted by someone whose authority is unknown.
2. R-02 and R-05 determine whether candidate content can be distributed and under what restrictions.
3. R-04 must be settled before accepting rights-bearing contributor submissions.
4. R-06 and R-07 must be settled before any release-facing editorial sign-off.
5. R-08 must be operational before a public release claims a correction/withdrawal route.
6. R-09 and R-10 must be implemented for the exact selected material before final release review.

## What remains prohibited until decisions are recorded

- No licence, rights holder, editor, approver or public contact is assumed.
- No candidate Claim, Evidence Use, Source, Context, Scope or Relation is promoted from HOLD.
- No allowlist, public preview, deployment, publication or merge is authorized.
- No third-party text/media is copied on the strength of a public URL or attribution alone.
- No hosted contribution intake or collection of contributor personal data is enabled.

## Owner response template

Copy and complete only the fields being decided. Leaving a field blank means it remains OPEN; it does not mean consent.

```text
R-01 Rights holder / authority:
R-02 Project text/data licence and commercial reuse:
R-03 Software licence:
R-04 Contributor terms:
R-05 Third-party source reuse policy:
R-06 Accountable editor:
R-07 Release approver:
R-08 Correction / dispute / withdrawal channel and owner:
R-09 Attribution / authorship / AI-tool disclosure:
R-10 Rights evidence register and maintainer:

Additional limits / exclusions:
Effective date:
```

## Effect on the first edition

The owner decisions are a genuine release blocker, but they do not prevent continued private engineering, exact-version screening, rights research, reader implementation or offline-bundle preparation. The project can prepare a private release candidate; it must not be represented as publicly released until the applicable decisions and exact-item gates are closed.

This packet is a decision aid, not legal advice or a substitute for jurisdiction-specific legal review.


## First-edition-specific decision consequences — 2026-11-23

The following decisions are now tied to actual candidate sources, rather than abstract policy alone.

| Candidate source | Verified source-use condition | Consequence for Edition 1 |
|---|---|---|
| NIST SI Units | NIST pages are generally public information unless a specific item is marked copyrighted; attribution and item-level exceptions apply | Textual factual paraphrase/link can proceed through item-level review; do not reuse graphics/logos without checking credits |
| PostgreSQL 18.7 docs | PostgreSQL License permits use/copy/modify/distribute documentation with required copyright notice and disclaimers | Add the exact required notice/disclaimer to the relevant release attribution surface if any documentation content is redistributed; verify whether only independent paraphrase/link is used |
| CDC emergency hygiene | Most CDC material is public domain, with contractor/third-party exceptions; attribution, no-endorsement disclaimer, substantive integrity and free-source link required; CDC flags international differences | Candidate can advance only after item-level page/asset check, prominent disclaimer and jurisdiction review |
| NOAA weather explainer | Most NOAA information is public information, but page/item credits and third-party content exclusions apply; no implied endorsement or altered official presentation | Candidate can advance as independent factual explanation + attribution/link after item-level verification |
| American Red Cross alerts | No sufficient item-level reuse permission established in this audit | Keep text/media/logo out of release; factual paraphrase/link still requires project rights-policy decision and documented review |
| FAO food security handbook | General website/publication terms allow stated noncommercial uses with attribution; commercial use, resale and adaptation/translation require permission; third-party elements excluded | If Edition 1 is commercial/resale/adaptation or AI-processed in a way not covered, obtain written permission or replace source; otherwise document precise noncommercial use and attribution |
| OpenStax Chemistry 2e | CC BY-NC-SA 4.0; prior written permission required for LLM/generative-AI ingestion/use; commercial reuse requires permission | Mixtures candidate remains HOLD unless use path is compatible or a replacement source is selected |
| OpenStax Biology 2e | CC BY-NC-SA 4.0; prior written permission required for LLM/generative-AI ingestion/use; commercial reuse requires permission | Cell candidate remains HOLD unless use path is compatible or a replacement source is selected |
| OpenStax World History Volume 1 | CC BY-NC-SA 4.0; prior written permission required for LLM/generative-AI ingestion/use; commercial reuse requires permission | Ancient civilizations candidate remains HOLD unless use path is compatible or a replacement source is selected |
| OpenStax Physics | Physics title's separate license must be verified at its own preface; earlier audit identified CC BY 4.0 for the specific title examined | Do not transfer this license to other OpenStax books |

### Decisions that now have a concrete first-edition effect

- **R-02 (project content/data licence):** must specify whether the first edition is commercial, noncommercial, freely accessible but monetized indirectly, or otherwise distributed. “Free to read” alone does not determine whether source terms are compatible.
- **R-05 (third-party reuse):** decide whether the first edition uses only independently written factual paraphrases and outbound source links, or whether it will redistribute licensed excerpts/assets. Conservative default: no copied source prose, no images/figures/tables/maps, no logos, no embedded third-party media without item-level permission and a recorded licence.
- **R-10 (rights evidence register):** add source title/edition, exact URL/section, asset-level credit, applicable jurisdiction, distribution model, AI/LLM processing status, required attribution/disclaimer, permission evidence, reviewer and review date.
- **R-07 (release approver):** approval must attach to the frozen exact-version manifest and exact built artifact hash, not merely to a branch or PR.
- **R-08 (correction/takedown):** a public release must not claim a correction service until a monitored channel and responsible operator exist.

### Minimum owner decisions to unblock a private release candidate

For a private, non-public, non-redistributable review artifact, the project still needs a named accountable editor and an identified internal reviewer/approver for the private exercise. The existing SI private-preview authorization is limited to that exact preview and cannot be generalized to other content.

### Minimum owner decisions to unblock public Edition 1

At minimum: R-01, R-02, R-05, R-06, R-07, R-08, R-09 and R-10 must be decided and recorded. R-03 and R-04 must be decided before software licensing or contributor intake is enabled. All decisions must be consistent with the intended distribution model and each selected source's terms.

This addendum clarifies consequences; it does not select any option, appoint a person, grant permission, or close any R-01–R-10 item.


---

## Дополнительные bounded authorization requests — 2026-11-23

Помимо project-level решений R-01–R-10, подготовлены два независимых запроса на точные versioned source migrations. Они не заменяют и не закрывают R-01–R-10.

### A. Ancient Civilizations — Claim B provenance migration

Документ:
`RELEASE/OWNER-AUTHORIZATION-REQUEST-ANCIENT-CIVILIZATIONS-CLAIM-B-CC-BY-PROVENANCE-MIGRATION-2026-11-23.md`

Предлагается:
- CLM-ANCIENT_CIVILIZATIONS_BASICS-B@1 → @2, statement неизменен, provenance новой версии опирается на три уже approved CC BY 4.0 Sources;
- три соответствующих EU-B records @1 → @2, меняется только claim_ref на Claim B@2;
- старые версии остаются историческими;
- Claim A/C, Context/Scope и старый OpenStax Source не меняются;
- все новые версии остаются HOLD.

Причина: Claim B@1 provenance ссылается на OpenStax World History Volume 1 CC BY-NC-SA 4.0 Source и AI-ingestion restriction; builder требует включить provenance Source в exact dependency closure.

### B. Cell Basics — NCI Source migration

Документ:
`RELEASE/OWNER-AUTHORIZATION-REQUEST-CELL-BASICS-NCI-SOURCE-MIGRATION-2026-11-23.md`

Предлагается:
- новый NCI Dictionary Source@1 и EU-NCI@1;
- CLM-CELL_BASICS-A@1 → @2 с неизменным statement и новым NCI provenance;
- CTX/SCP@1 → @2 с target_ref на Claim A@2;
- targeted tests, README, master и exact coverage metadata updates;
- старые OpenStax @1 records сохраняются исторически;
- все новые версии остаются HOLD.

Причина: OpenStax Biology 2e имеет CC BY-NC-SA 4.0 и LLM ingestion restriction; NCI разрешает повторное использование текста с attribution/link, а graphics/third-party assets исключаются.

### Правило частичного решения

Каждый запрос самостоятельный. Владелец может:
- одобрить оба;
- одобрить только один;
- отложить оба.

Approval разрешает только перечисленные операции. Он не означает INCLUDE, rights clearance для всей темы, release approval, merge или publication.

### Отдельно остаются открытыми R-01–R-10

До публичного выпуска всё ещё требуются:
- правообладатель;
- лицензия оригинального корпуса/данных;
- отдельная лицензия программного кода;
- условия для будущих участников;
- политика использования сторонних источников;
- редакционно ответственный владелец;
- release approver;
- публичный correction/dispute/takedown process;
- политика авторства/атрибуции;
- rights evidence register и процедура проверки.

Ни один из этих пунктов не считается закрытым из-за подготовки двух source migration requests.
