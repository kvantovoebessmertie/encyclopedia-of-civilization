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
