# First Edition — Minimum Editorial, Rights and Operations Policy

Date: 2026-11-18  
Status: **POLICY DRAFT FOR PROJECT-OWNER ADOPTION — not a declaration that unresolved legal/ownership decisions are complete**

## 1. Scope

This policy applies only to the exact version-pinned first-edition release bundle. It does not authorize publication of the full canonical corpus, internal audit material, private preview artifacts, contributor contact data, or records marked HOLD/EXCLUDE.

## 2. Editorial responsibility

Before release, the project owner must explicitly name:
- accountable editor/release owner;
- subject-matter reviewers for high-consequence domains;
- person authorized to approve a release;
- backup contact/maintainer for urgent correction or rollback.

A technical CI pass, automated validator, source author, or AI-generated assessment is not an editorial approval.

Recommended operating rule: one accountable release owner signs the allowlist and release manifest; domain reviewers sign only the subject areas they actually reviewed. If no qualified reviewer is available for a high-consequence item, that item remains HOLD.

## 3. Publication and third-party rights

No blanket licence is assumed for the corpus. Rights are assessed per exact release item and its displayed third-party material.

Before publication, the rights register must record:
- source and exact material used;
- source copyright/licence/terms as applicable;
- attribution text and link;
- whether adaptation, translation, excerpting, redistribution and commercial use are permitted;
- any share-alike, non-commercial, no-derivatives, or other conditions;
- whether permission is required and whether it has been obtained;
- decision, reviewer and date.

Recommended conservative default: publish original project-authored summaries and factual descriptions only where their source use and rights basis are documented; do not reproduce third-party figures, tables, long text, images, or other expressive material unless the specific licence/permission clearly allows it. A source being public or authoritative does not mean its content is public domain.

**Project-owner decision still required:** choose the first-edition licence/terms for project-authored material and confirm the intended distribution model (including whether commercial reuse is allowed). Do not silently infer this choice.

## 4. Attribution

Every included Claim must provide a clear route to the Evidence Use and Source. Reader-facing source details must not imply that a source endorses the Encyclopedia. Attribution must follow the source's actual terms and preserve author/title/organisation/link/licence information where required.

## 5. Safety and editorial states

Use distinct reader-facing states:
- reviewed for this edition;
- limited / context-dependent;
- under review (not part of public instructional content);
- excluded from this edition.

Do not show HOLD or EXCLUDE records as usable public knowledge. Do not use green styling or a generic “verified” label to imply certainty beyond the recorded evidence.

High-consequence content requires a named domain reviewer, explicit applicability and limitations, escalation boundaries, and a review date. Medical, water-treatment, electrical, structural, chemical, fire, and emergency instructions remain excluded if these conditions are not met.

## 6. Corrections and urgent takedown

Provide one visible contact route controlled by the release owner. A report should capture:
- affected edition and record ID/version;
- description of the suspected error or harm;
- supporting source or context, if available;
- whether immediate safety action may be needed.

Operational sequence:
1. Acknowledge and log the report.
2. Triage severity: critical safety/legal/privacy/security; material factual error; ordinary correction; suggestion.
3. For credible critical risk, temporarily unpublish or disable the affected item/pathway promptly while investigating.
4. Preserve the prior release, record versions, evidence and decision trail; do not erase history.
5. Review the report, consult a qualified reviewer when needed, and decide correct / annotate / retain / withdraw.
6. Publish a versioned correction with a concise change note.
7. Rebuild and validate the affected release bundle; roll back to the last known-good release if integrity or safety cannot be restored.
8. Close the report with a public explanation that does not disclose private reporter information.

No public endpoint or guaranteed response-time SLA is claimed until a staffed operating process exists.

## 7. Privacy and contribution intake

For the first edition, use the existing local-only JSON contribution form or a controlled manual contact route. Do not launch hosted intake, accounts, public uploads, or a database until ownership, privacy notice, retention, abuse controls, access controls, deletion process and operational staffing are defined.

Collect the minimum information needed to assess a contribution. Do not put personal contact details into canonical content records or public contribution JSON. Restrict access to any correspondence and define a retention/deletion schedule before collection.

## 8. Release and rollback controls

Each release must preserve:
- edition identifier and publication date;
- exact source commit and allowlist;
- builder/tool versions;
- manifest and cryptographic hashes;
- test and artifact-inspection evidence;
- rights/attribution register;
- editorial approval and limitations statement;
- prior release identifier and rollback instructions.

The release owner may halt publication or roll back a release. No automated workflow may publish merely because CI is green.

## 9. Project-owner decisions that cannot be made by automation

The following are genuine adoption decisions, not technical checks:
1. Project-authored content licence and intended commercial-reuse policy.
2. Named accountable editor/release owner and backup.
3. Public correction contact route and who will monitor it.
4. Whether any contributor contact information will be collected; default for edition one is no hosted collection.
5. Distribution/hosting choice and publication language(s).

Until decisions 1–3 are explicitly made, the first edition must not be represented as publicly released. The rest of the implementation can proceed in a private, reproducible release candidate.

## 10. Adoption checklist

- [ ] Project licence/terms approved and recorded.
- [ ] Rights register complete for every included item.
- [ ] Accountable editor and release approver named.
- [ ] Qualified review recorded for every high-consequence included item.
- [ ] Correction/takedown and rollback owner/contact established.
- [ ] Privacy/retention policy adopted for any collected data.
- [ ] Manual/local contribution boundary visible to users.
- [ ] Release manifest, hashes, exact-head tests and artifact inspection retained.
