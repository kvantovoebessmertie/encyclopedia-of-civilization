# R7 Civil Society Basics — Bounded Canonical Diff Packet

Date: 2026-11-19
Target branch: `mvp-public-contribution-design-2026-10-11`
Inspection HEAD: `838c039851eddb281664fce779cfd6be4ef72747`
Authorization: `REMAINING-R7-SOURCE-REMEDIATION-001` in `RELEASE/EDITORIAL-CORRECTION.json`
Status: **IMPLEMENTED UNDER EXISTING BOUNDED AUTHORIZATION — 13/13 RECORDS v1→v2; RIGHTS AND RELEASE HOLD REMAIN**

## 1. Authorization and scope

This packet is limited to `civil-society-basics`, one of the four slices expressly covered by `REMAINING-R7-SOURCE-REMEDIATION-001`. That authorization supersedes the earlier prohibition for this slice only.

The exact 13-record graph was re-fetched at the inspection HEAD. All 13 current records are v1:
- one primary Source;
- Claims A–C;
- primary Evidence Use A–C;
- one independent Source;
- independent Evidence Use A–C;
- one Context and one Scope.

The existing Claims are retained verbatim. Their v1→v2 increments are provenance-only, aligning `provenance.created_from` with the new primary Source v2. No new IDs are required or proposed.

## 2. Exact record inventory and proposed versions

| Record | Current version | Proposed version | Current blob SHA |
|---|---:|---:|---|
| `SRC-CIVIL_SOCIETY_BASICS` | 1 | 2 | `cbd3d57977a502f10805e4f7a0786ee4647c02c2` |
| `CLM-CIVIL_SOCIETY_BASICS-A` | 1 | 2 | `3fac8ba3ef4d7ab2e4689a942144e2ad5e8d6868` |
| `CLM-CIVIL_SOCIETY_BASICS-B` | 1 | 2 | `63c5855fc3e102249643a332a0aa47e91ac11c3f` |
| `CLM-CIVIL_SOCIETY_BASICS-C` | 1 | 2 | `a2391c698ab75f6eaae87580190546f80824ce15` |
| `EU-CIVIL_SOCIETY_BASICS-A` | 1 | 2 | `680f006d01e605b4c9b3b0a0f3227cbeabbb66fe` |
| `EU-CIVIL_SOCIETY_BASICS-B` | 1 | 2 | `b99c2cbe446836b4539dce3aace6b3917d1eded1` |
| `EU-CIVIL_SOCIETY_BASICS-C` | 1 | 2 | `6b43e2e3b186e23cb63b4638fa65eafbc80794cf` |
| `SRC-CIVIL_SOCIETY_BASICS-INDEPENDENT` | 1 | 2 | `7b4a6af5881905f4ca5d42a9e9844d7cc51a5b8e` |
| `EU-CIVIL_SOCIETY_BASICS-INDEPENDENT-A` | 1 | 2 | `6ef334b0e13843337d8027a0a5473f3c492dd274` |
| `EU-CIVIL_SOCIETY_BASICS-INDEPENDENT-B` | 1 | 2 | `37b7ce2f47d5875cd51cc9390394193bf936a974` |
| `EU-CIVIL_SOCIETY_BASICS-INDEPENDENT-C` | 1 | 2 | `6900c9d1c8e83a1aa31a3efe181a31b010190d3b` |
| `CTX-CIVIL_SOCIETY_BASICS` | 1 | 2 | `eb1be062271efcc0defe6e6dcc9646ea8517a9d1` |
| `SCP-CIVIL_SOCIETY_BASICS` | 1 | 2 | `1e9b82c7e6965105ee715e6797e56f757f0d7d37` |

If any blob SHA or version differs at implementation time, stop and regenerate this packet from the new frozen HEAD.

## 3. Proposed Source v2 records

### Primary Source

**ID/version:** `SRC-CIVIL_SOCIETY_BASICS@2`

**Source identity:**

> OECD Development Assistance Committee, *DAC Recommendation on Enabling Civil Society in Development Co-operation and Humanitarian Assistance*, OECD/LEGAL/5021, adopted 6 July 2021.

**URI:**

`https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-5021`

**Locator:**
- Section I: definitions of “civil society”, “civil society organisations (CSOs)” and “civic space”.
- Section II, especially recommendations 1–10: respect, protect and promote civic space; public awareness, monitoring and civil-society participation.
- Section III, especially recommendations 1–2: engagement with civil society and participation in policy/programme priority-setting, design, implementation, monitoring and evaluation.
- Section IV: effectiveness, transparency and accountability of CSOs.

**Identity boundary:** this is an OECD DAC Recommendation directed to development co-operation and humanitarian-assistance providers. It is not a universal national legal definition or a comprehensive law of civil-society organisations.

### Independent Source

**ID/version:** `SRC-CIVIL_SOCIETY_BASICS-INDEPENDENT@2`

**Source identity:**

> United Nations Department of Global Communications, Civil Society Unit, “About us”.

**URI:**

`https://www.un.org/en/civil-society/page/about-us`

**Locator:**
- “Who We Are”: Civil Society Unit mandate within the Outreach Division / Department of Global Communications.
- Definition paragraph beginning “A civil society organization (CSO) or non-governmental organization (NGO)…”.
- The same paragraph's description of services and humanitarian functions, bringing citizens' concerns to governments, policy monitoring, political participation, analysis/expertise, early-warning functions and monitoring/implementation of international agreements.

**Identity boundary:** this page describes the UN DGC Civil Society Unit and the CSOs relevant to its mandate. It is an institutional example, not an exhaustive global taxonomy of civil-society organisations.

## 4. Claim-by-claim evidence mapping

All three Claim statements and `claim_type` values remain unchanged. Each Claim advances v1→v2 only to align `provenance.created_from` with `SRC-CIVIL_SOCIETY_BASICS@2`.

### Claim A — civil society as a voluntary sphere distinct from state and commercial sector

Current statement retained:

> Гражданское общество обычно описывает пространство добровольных объединений, отличное от государства и коммерческого сектора.

Primary EU v2 locator:
- OECD/LEGAL/5021, Section I, definition of “civil society”: voluntary human association/interaction for shared needs, ideas, interests, values, faith and beliefs; distinct from states, private for-profit enterprises and the family.
- Section I, definition of “CSOs”: organisational representation of civil society.

Independent EU v2 locator:
- UN Civil Society Unit, “Who We Are”: definition of a CSO/NGO as a non-profit, voluntary citizens' group organised at local, national or international level.

Support boundary: OECD's definition is the primary conceptual basis. The UN page supplies an institutional illustration; it does not define every possible civil-society form.

### Claim B — possible organisational forms

Current statement retained:

> К организациям гражданского общества могут относиться общественные группы, фонды, профессиональные объединения, НКО и сети граждан.

Primary EU v2 locator:
- OECD/LEGAL/5021, Section I, definition of “CSOs”: not-for-profit, non-state, non-partisan, non-violent and self-governing organisations; formal registered organisations and informal associations without legal status; people joining around shared needs, ideas, interests, values, faith and beliefs.

Independent EU v2 locator:
- UN Civil Society Unit, “Who We Are”: voluntary citizens' groups organised locally, nationally or internationally; task-oriented groups driven by common interests; examples of functions and issue areas.

Support boundary: the list in the Claim is illustrative, not exhaustive. The sources do not establish that every listed form has the same legal personality, registration status, rights or powers in every jurisdiction.

### Claim C — participation, representation and public services

Current statement retained:

> Организации гражданского общества могут участвовать в общественных обсуждениях, представительстве интересов и предоставлении общественно значимых услуг.

Primary EU v2 locator:
- OECD/LEGAL/5021, Section II, recommendation 9: greater and more inclusive civil-society participation in public policy.
- Section III, recommendation 2: participation in policy/programme priority-setting, design, implementation, monitoring and evaluation.
- Section IV, provisions on CSO effectiveness, transparency and accountability.

Independent EU v2 locator:
- UN Civil Society Unit, “Who We Are”: functions paragraph describing services and humanitarian functions, bringing citizens' concerns to governments, monitoring policies, encouraging political participation, providing analysis and expertise, early-warning functions and helping monitor/implement international agreements.

Support boundary: these are possible roles and examples, not duties or powers held by every organisation. The OECD Recommendation addresses providers' enabling actions in development co-operation/humanitarian assistance; the UN page describes functions in the context of UN engagement.

## 5. Exact per-record field changes

| Record group | Permitted field changes | Fields to preserve |
|---|---|---|
| Primary Source v1→v2 | Correct `source_identity` to the OECD Recommendation title/number/date; set `external_ref.uri` to the OECD legal-instrument page | ID, type, publication/completion states; no copied source prose |
| Independent Source v1→v2 | Correct `source_identity` to UN DGC Civil Society Unit “About us”; set `external_ref.uri` to the official UN page | ID, type, publication/completion states; no copied page prose or image |
| Claims A–C v1→v2 | Update only `provenance.created_from` to `SRC-CIVIL_SOCIETY_BASICS@2` | Statement, claim_type and all other semantic content unchanged |
| Primary EUs A–C v1→v2 | Update `provenance.created_from` and `content.source_ref` to primary Source v2; update `content.claim_ref` to corresponding Claim v2; add claim-specific `content.material.locator`; replace generic description with support-bounded description | `evidence_role: supports`; no other graph or publication field changes |
| Independent EUs A–C v1→v2 | Update `provenance.created_from` and `content.source_ref` to independent Source v2; update `content.claim_ref` to corresponding Claim v2; add claim-specific `content.material.locator`; replace generic description with support-bounded description | `evidence_role: supports`; no other graph or publication field changes |
| Context v1→v2 | Update `target_ref` to Claim A v2; refine context to identify the OECD/UN source roles and jurisdictional/organisational boundary | No new Claim, Source or Relation; preserve the context's educational character |
| Scope v1→v2 | Update `target_ref` to Claim A v2; state that the slice is conceptual, not a universal legal classification or a determination of an organisation's local legal status/powers | No change to candidate membership, publication state or allowlist |

### Proposed Context v2 text

> Срез описывает гражданское общество как разнообразные формы добровольного общественного объединения и совместной деятельности, отличные от государства и коммерческих предприятий. Рекомендация OECD DAC используется для понятийной рамки гражданского общества, организаций гражданского общества и их возможного участия в общественной политике в контексте развития и гуманитарной помощи. Страница Civil Society Unit ООН показывает отдельные формы взаимодействия организаций гражданского общества с ООН и возможные общественные функции. Состав, правовой статус, регистрация, права и полномочия конкретной организации зависят от страны, законодательства и институционального контекста.

### Proposed Scope v2 text

> Срез ограничен базовым понятийным описанием гражданского общества, возможных организационных форм и общественных функций. Он не является универсальной юридической классификацией, исчерпывающим перечнем организаций или заключением о правовом статусе, регистрации, правах либо полномочиях конкретной организации. Рекомендация OECD DAC относится к действиям участников международного сотрудничества в сфере развития и гуманитарной помощи; страница ООН описывает мандат Civil Society Unit Департамента глобальных коммуникаций и связанные с ним примеры. Для правовых выводов требуется проверка законодательства и институционального контекста соответствующей юрисдикции.

## 6. Rights and attribution boundary

- OECD/LEGAL/5021 is an official OECD DAC legal instrument. Public availability does not grant blanket permission to reproduce the instrument's text, tables or related material. Proposed use is bibliographic identification, exact locator metadata and independently worded factual paraphrase.
- The UN Civil Society Unit page is an official UN institutional page. Public accessibility is not treated as a blanket republication licence. Proposed use is factual paraphrase and attribution only.
- Do not copy, translate or reproduce source wording, page layouts, photographs, diagrams or other expressive material.
- These changes do not close R-01–R-10 or establish the Encyclopedia's own content/data licence.
- Keep the slice HOLD pending item-level rights review, independent editorial review and Human View.

## 7. Explicit non-actions

This packet does not authorize or perform:
- any change to Claim statements or `claim_type`;
- any publication/completion status change;
- any INCLUDE/EXCLUDE decision or allowlist change;
- any new canonical ID;
- any Relation, validator, storage, recovery, package or release-gate change;
- any source-text reproduction, translation, figure/table/image reuse or deployment;
- any merge of PR #22 or write to `main`.

## 8. Validation contract after implementation

1. Freeze a new exact PR HEAD and re-fetch all 13 records by exact ID/version/type.
2. Verify all current blob SHAs against §2; abort and regenerate if any drift is found.
3. Apply Source v2 records first; then Claims A–C provenance-only increments; then primary and independent EUs; then Context/Scope target alignment.
4. Re-fetch all 13 changed records and validate all six Claim→EU→Source chains resolve to exact versions.
5. Verify every EU has a non-empty claim-specific locator, accurate support boundary and `evidence_role: supports`.
6. Verify Context and Scope target `CLM-CIVIL_SOCIETY_BASICS-A@2`.
7. Run affected-slice schema/graph/reference tests, then exact-head Reference Tests, Release Conformance Gate, Offline Edition and Browser Tests on one immutable final HEAD.
8. Preserve HOLD. Technical conformance does not establish factual truth, legal status, rights clearance or publication eligibility.

**Status:** the bounded scope is authorized by `REMAINING-R7-SOURCE-REMEDIATION-001`; this packet is a prepared implementation specification. No canonical record has been edited in this step.


## 10. Implementation result — 2026-11-19

The packet was implemented on the current PR #22 branch after all 13 canonical records were re-fetched and verified at v1. All 13 are now v2; all six primary/independent Evidence Use records have non-empty claim-specific locators and support-boundary descriptions. Claims A–C retain their statements and `claim_type`; Context and Scope target Claim A@2; publication/completion states remain published/complete. The README and source-specific rights screen were updated.

The current exact-head validation found 13/13 expected records at v2 with no missing EU locators/descriptions. The slice remains HOLD. Project licence/distribution compatibility, item-level rights, independent editorial review and Human View remain open. No source expression or visual assets were reproduced.
