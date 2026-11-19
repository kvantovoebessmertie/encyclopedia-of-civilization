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

Six existing source-specific rights screens now have a consolidated index covering 47 distinct slice entries across Engineering & Computing (8), History/Culture/Knowledge Traditions (6), Human Sciences (3), Legal/Trade/Institutional Systems (10), R9 evidence-depth follow-up (10), and Society/Public Institutions (10). The screens preserve exact-source conditions and distinctions between factual paraphrase, expressive reuse, public-domain government material, third-party assets, institutional terms, and archive/community ethics.

This consolidation does **not** close any owner decision. R-01 through R-10 remain OPEN. No project licence was selected, no rights holder/editor/approver/contact was appointed, no permission request was submitted, and no slice was promoted from HOLD. The recommended conservative operating baseline is recorded for owner consideration only.
