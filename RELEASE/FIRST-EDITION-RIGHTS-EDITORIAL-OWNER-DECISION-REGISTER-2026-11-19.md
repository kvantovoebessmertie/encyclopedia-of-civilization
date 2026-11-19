# First Edition — Rights, Editorial Accountability and Release-Owner Decision Register

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`

## Status

**OPEN — owner decisions required. No license, rights grant, editorial appointment, release approver, or public contact is approved by this register.**

This register records the decisions and evidence required for Work Package 2. It is not legal advice, a rights clearance, a contributor agreement, or an authorization to publish.

## Existing architecture constraints verified

- `STANDARD/017-PROVENANCE.md` explicitly distinguishes original author, contributor, rights holder, and owner; these roles may overlap but are not automatically equivalent. It also states that the Standard does not define a complete model of authorship, contribution, ownership, rights, or responsibility.
- `IMPLEMENTATION/018-AUTHORSHIP-CONTRIBUTION.md` supports `rights_ref` as a structural field, but distinguishes rights, credit, and responsibility. Its enforcement matrix marks rights/responsibility semantics as deferred.
- `IMPLEMENTATION/020-OPERATIONS-SECURITY.md` identifies license/compatibility metadata and release applicability as operational dependency metadata.
- `RELEASE/EDITORIAL-CORRECTION.json` is a bounded authorization for specified editorial corrections. It does not itself select a publication license or appoint a rights holder, editor, release approver, or public contact.
- Source records marked `availability=public` identify publicly accessible sources. That field alone is not a license or permission to reproduce source text, figures, images, tables, or datasets.

## Decision register

| ID | Required owner decision | Minimum evidence / recorded output | Current state |
|---|---|---|---|
| R-01 | Identify the rights holder(s) for the Encyclopedia-authored corpus and project-created editorial material | Named legal person/entity or explicitly documented collective ownership; basis for authority to license | OPEN |
| R-02 | Select the license for original text and structured data | Exact license name/version, canonical license text/URI, covered material, exclusions, attribution requirements, compatibility review | OPEN |
| R-03 | Decide whether software/code is licensed separately from content/data | Separate code license or explicit statement that the content license does not cover code | OPEN |
| R-04 | Define contributor terms for future submissions | Contributor grant/permission, attribution choice, warranties/representations, third-party material rules, withdrawal and dispute process | OPEN |
| R-05 | Define source reuse policy | Distinguish factual paraphrase and linking from quotations, images, diagrams, tables, datasets, and copied source material; require source-specific permission/license evidence where needed | OPEN |
| R-06 | Appoint editorially accountable role/entity | Named accountable role, scope of authority, review responsibility, conflict/escalation route | OPEN |
| R-07 | Appoint release approver | Explicit approver and approval record for each edition; separate technical CI from editorial/rights approval | OPEN |
| R-08 | Establish correction, dispute, and withdrawal process | Public contact channel, response target, triage, temporary restriction, version history, appeal/escalation, withdrawal criteria | OPEN |
| R-09 | Establish attribution and authorship policy | Rules for authors, editors, translators, reviewers, contributors, AI/tool assistance, collective/anonymous attribution, and rights-holder attribution | OPEN |
| R-10 | Define rights evidence storage and validation | Canonical rights/permission records or documented external evidence references; owner, version, scope, territory, term, restrictions, expiry/review date | OPEN |

## Mandatory distinctions

1. Public accessibility is not equivalent to a reuse license.
2. Attribution is not equivalent to permission.
3. Contributor credit is not proof of ownership or transfer of rights.
4. Editorial responsibility is not automatically legal liability.
5. A source link and a factual paraphrase do not authorize copying protected expression or media.
6. A repository license does not automatically cover third-party source content, images, datasets, or contributor submissions.
7. Technical CI PASS does not establish rights clearance or editorial approval.

## Release gate

Work Package 2 cannot be marked complete until the responsible owner records decisions for R-01 through R-10, the applicable rights evidence is attached or referenced, and a rights review is completed against the actual material selected for the first edition.

Any unresolved third-party material must be excluded, replaced, linked without reproduction where appropriate, or held pending permission. Do not infer permission from `availability=public`, source attribution, or the fact that content is already present in the repository.

## Boundaries

- No license was selected.
- No rights holder or editor was named.
- No approver or public contact was invented.
- No content was published, relicensed, or reattributed.
- All first-edition candidate records and Relations remain HOLD.


## Consolidated source-screen follow-up — 2026-11-19

See `RELEASE/FIRST-EDITION-WP2-RIGHTS-AND-ATTRIBUTION-CONSOLIDATED-STATUS-2026-11-19.md`.

Seven source-specific rights screens now have a consolidated index covering 55 table entries and 52 distinct slices: Engineering & Computing (8), History/Culture/Knowledge Traditions (6), Human Sciences (3), Legal/Trade/Institutional Systems (10), R9 evidence-depth follow-up (13 table entries, including three repeated slice rows), Society/Public Institutions (10), and Batch 2 History/Culture/Humanities (5). The screens preserve exact-source conditions and distinctions between factual paraphrase, expressive reuse, public-domain government material, third-party assets, institutional terms, and archive/community ethics. The Batch 2 screen also records source-specific licence/version caveats for OpenStax Anthropology, OpenStax-derived Philosophy, Essentials of Linguistics, Smithsonian/University of Chicago article identity, AAA, Britannica, SEP and UNESCO.

This consolidation does **not** close any owner decision. R-01 through R-10 remain OPEN. No project licence was selected, no rights holder/editor/approver/contact was appointed, no permission request was submitted, and no slice was promoted from HOLD. The recommended conservative operating baseline is recorded for owner consideration only.


## Source-rights delta — Batches 10–15 — 2026-11-19

The consolidated WP2 status has been extended with item-specific findings for OpenStax, the joint Settlement Geography manual, ASA, UN ECOSOC, USGS and NOAA. See `RELEASE/FIRST-EDITION-WP2-RIGHTS-AND-ATTRIBUTION-CONSOLIDATED-STATUS-2026-11-19.md`, §8.

Material owner-decision flags:
- OpenStax *Principles of Economics 3e*, *Principles of Microeconomics 3e* and *Organizational Behavior*: CC BY-NC-SA 4.0 plus explicit LLM-ingestion/generative-AI restriction without prior written permission. The earlier *Principles of Economics 3e* CC BY 4.0 statement is corrected and must not be used.
- Settlement Geography joint 2021 manual: CC BY-NC-SA 3.0 IGO; commercial reuse not cleared; six co-publishers must be identified; third-party cover photography/maps excluded.
- ASA Sociology brochure: copyrighted; no open licence identified in the reviewed page; factual paraphrase only, permission/terms review required.
- UN ECOSOC E/C.16/2006/4: publicly accessible official document; public access is not a blanket republication licence; use exact citations and factual paraphrase only.
- USGS/NOAA: proposed use is factual text and locators; third-party images/media and credited material remain item-level rights checks.

These flags do not close R-02, R-05, R-09 or R-10. R-01–R-10 remain OPEN. No rights clearance, licence, permission, owner or editor is approved by this addendum; all affected slices remain HOLD.


## Source-rights delta — Batch 15–16 and P4/P5 supplemental pinpoint review — 2026-11-19

The consolidated WP2 rights status now includes item-specific flags for Cornell LII Wex; UN Human Rights Council A/HRC/25/27; UN Fundamental Principles of Official Statistics; Statistics Canada; ASA Sociology brochure; BIPM/JCGM VIM and SI Brochure; NIST TN 1297; IOM World Migration Report Educators' Toolkit; UNHCR refugee guidance; UN Guiding Principles on Internal Displacement; FEMA IS-52, Distribution Management Plan Guide 2.0 and NDRF Third Edition; WFP Logistics Cluster; UNDRR recovery terminology; EPA water-quality criteria/standards; WHO drinking-water guidelines (2026 fourth edition with three addenda); EIA and DOE electric-grid pages.

Material owner-decision flags:
- Cornell Wex is a community-built U.S.-law reference, not legal advice or a universal law source; no expressive reuse is cleared.
- ASA brochure is copyrighted; factual paraphrase only pending item-specific permission/terms review.
- IOM Toolkit and WHO guidelines are copyrighted institutional publications; do not reproduce text, graphics, diagrams or tables without a documented reuse basis.
- BIPM/JCGM and UN institutional materials require exact edition/attribution and item-level reuse review; public accessibility is not blanket republication permission.
- FEMA, EPA, EIA, DOE and NIST government materials still require third-party asset/embedded-content checks; preserve jurisdiction and scope boundaries.
- WFP Logistics Cluster content is hosted institutional material; verify item-level terms before reproduction.
- Migration/refugee/IDP distinctions and U.S. water-quality legal claims require qualified subject-matter/legal review independent of rights clearance.

See RELEASE/FIRST-EDITION-WP2-RIGHTS-AND-ATTRIBUTION-CONSOLIDATED-STATUS-2026-11-19.md, §9, for the source-by-source references and boundaries. R-01–R-10 remain OPEN. No rights clearance, licence, permission, rights holder, editor, approver or public contact is approved by this addendum. All affected slices remain HOLD.


## R9 Settlement Geography source alternative — 2026-11-19

A Eurostat 2026 source alternative with CC BY 4.0 terms has been identified for the Settlement Geography locator remediation. Its front matter allows reuse of EU-owned content with attribution and indication of changes, while excluding third-party cover photography, most maps, other photos and administrative-boundary material. Proposed use is factual paraphrase and text locators only. The report states that it is a Eurostat Statistical Report and not representative of the European Commission's official position. The 2021 joint manual's CC BY-NC-SA 3.0 IGO commercial-use blocker can therefore be avoided for this bounded text-only use if the owner approves the Eurostat Source replacement.

See RELEASE/R9-SETTLEMENT-GEOGRAPHY-EUROSTAT-CC-BY-4-0-SOURCE-ALTERNATIVE-2026-11-19.md and the WP2 rights status §10. This does not clear the project licence or close R-02/R-05/R-10. No canonical record changed; all nine records remain HOLD pending explicit authorization.


## Owner decision required — R7 Labour Economics / OpenStax — 2026-11-19

**Issue:** the active bounded authorization `REMAINING-R7-SOURCE-REMEDIATION-001` still states CC BY 4.0 for *Principles of Economics 3e*. The official OpenStax Preface states CC BY-NC-SA 4.0 and requires prior written permission for LLM training/ingestion and generative-AI offerings. The current authorization text is materially inconsistent with the official source terms.

Decision packet: `RELEASE/R7-LABOUR-ECONOMICS-OPENSTAX-RIGHTS-DECISION-2026-11-19.md`.

Owner must select one path: obtain written permission covering the actual AI-assisted/LLM and any commercial use; replace OpenStax with an approved rights-compatible primary source and amend the bounded authorization; or approve a narrowly defined citation/metadata-only use after explicit review of the AI workflow and final distribution model. No option is selected by this register update.

**Current disposition:** decision pending; do not implement OpenStax-dependent canonical changes; Labour Economics remains HOLD. No canonical Source/Claim/Evidence Use record changed. R-01–R-10 remain OPEN.

## R7 Comparative Civilizations — bounded implementation completed; rights decision remains open — 2026-11-19

Under `REMAINING-R7-SOURCE-REMEDIATION-001`, the nine-record canonical graph is now v2. The Source identifies the AHA “Introduction to Doing World History” page; Claims A–C were versioned only for provenance alignment, with statements and `claim_type` preserved; all three Evidence Use records now have claim-specific locators. EU-C retains the single canonical AHA `content.source_ref` and carries the Singapore MOE chronology/causation reference only in schema-supported `provenance.external_sources`. Context, Scope and README now state the educational and methodological limits. No second canonical Source ID or schema change was added.

AHA page rights and MOE syllabus non-commercial educational reproduction terms remain item-level review flags. No source expression or visual assets are copied. Rights clearance and independent historical/editorial review remain open; slice HOLD.


## R7 source-specific owner decisions added — 2026-11-19

The following are concrete applications of the open R-01–R-05 decisions to the remaining R7 slices. They are recorded as requests for an accountable owner, not as decisions made by the remediation team.

### R7-CS-01 — Civil Society Basics

Required owner response:
- Confirm the intended project distribution/licence model (R-02/R-03) and whether independently authored factual paraphrase with attribution and source links is acceptable for this edition.
- Confirm that no UN Civil Society Unit page text, image, layout or other expressive material is to be reproduced; otherwise obtain the necessary permission.
- Confirm whether the OECD Legal Instrument's narrow no-charge, unaltered reproduction terms are compatible with the intended edition, if any instrument text is ever reproduced. Current remediation proposes factual paraphrase only.

Implementation state: **13/13 canonical records v2; all three Claims preserved; six primary/independent Evidence Use records have exact locators and support boundaries; README updated.** Rights/distribution decision remains **OPEN**; no source expression or visual assets are reproduced; slice remains **HOLD**.

### R7-CC-01 — Comparative Civilizations Basics

Required owner response:
- Confirm whether the project can include independently authored factual paraphrases citing the AHA “Introduction to Doing World History” resource where no open licence for that resource was identified.
- Confirm whether the MOE syllabus may be used only as a cited methodological reference, without reproducing or adapting its protected syllabus content. Its stated reproduction permission is limited to the publication in entirety for personal/non-commercial educational use.
- If the project's intended distribution is commercial, mixed-use or otherwise outside the stated permissions, choose permission, a rights-compatible replacement, or exclusion from the first edition.

Implementation state: **9/9 canonical records v2; all three Claims preserved; three Evidence Use records have exact locators; EU-C supplementary MOE reference is schema-supported; README updated.** AHA/MOE rights and distribution decision remains **OPEN**; no source expression or visual assets are reproduced; slice remains **HOLD**.

### R7-LE-01 — Labour Economics Basics

Required owner response:
- Resolve the active authorization's incorrect/unsettled statement that OpenStax *Principles of Economics 3e* is CC BY 4.0.
- OpenStax's current HTML Preface and licensing help pages state CC BY-NC-SA 4.0 and prohibit LLM training/ingestion without prior written permission. A separate OpenStax-hosted PDF asset displays CC BY 4.0, so the exact asset/version intended must be clarified with OpenStax.
- Choose one documented path: (a) written OpenStax clarification/permission for the exact asset and intended use; (b) replace OpenStax with a rights-compatible source and issue a corrected bounded authorization; or (c) leave the OpenStax branch unused and retain HOLD.
- Confirm item-level terms for the ILOSTAT independent source before any redistribution or adaptation.

Current state: **OPEN — no canonical changes; 13-record graph remains v1 and aligned; implementation blocked.**

### Decision discipline

No response is inferred from the existence of this register. Until an authorized owner records a choice and the applicable bounded authorization is corrected where necessary, the remediation team must not choose a licence, declare permission, alter canonical records, change candidate membership, or remove HOLD.
