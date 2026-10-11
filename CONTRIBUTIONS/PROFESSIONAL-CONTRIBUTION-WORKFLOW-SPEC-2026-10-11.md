# Professional Contribution Workflow — Specification — 2026-10-11

## Status

**Design draft.** This is the proposed intake and review contract for the public MVP. It does not represent a live form or deployed service.

## Objective

Allow domain professionals, researchers, practitioners, and readers to propose additions or corrections in a structure that maps to the encyclopedia's existing knowledge architecture. The form guides contributors; it does not grant direct write access to canonical records.

## Submission types

Required single-choice field:

- `new_claim` — propose a new factual or practical Claim.
- `correction` — propose a correction to an existing Claim or topic.
- `contradiction` — report a conflict between Claims or between a Claim and its evidence.
- `source` — propose a source or additional evidence for an existing Claim.
- `relation` — propose a meaningful relation between existing knowledge items.
- `gap` — identify an important missing topic or capability.
- `other` — explain a contribution that does not fit the listed types.

## Intake fields

### Required for every submission

- Submission type.
- Subject area and narrower topic, where known.
- Short title.
- Main proposal in the contributor's own words.
- Rationale: why it matters and what problem it solves.
- At least one evidence/source description, or an explicit explanation of why a source cannot currently be provided.
- Scope, assumptions, limitations, and uncertainty, where applicable.
- Existing Claim/Record identifiers or URLs if the proposal concerns existing material.
- Contributor role: researcher, practitioner, educator, professional, reader, or other.
- Contact method for follow-up, collected only when needed.
- Confirmation that the contributor has read the submission terms and has permission to submit any attached material.

### Conditional fields

- Bibliographic metadata: title, author(s), publication/issuing body, date, edition/version, DOI/ISBN/standard number, URL, page/section/table/figure, and access date as relevant.
- Evidence characterization: what the source supports, whether it is primary/secondary, method and population/context where relevant, limitations, and possible dependence on another source.
- Applicability: geography, time period, environmental/operational conditions, population/material/system, prerequisites, and known exclusions.
- Contradiction report: exact Claim IDs, competing formulations, evidence on each side, and whether the disagreement may be explained by scope, date, definitions, or method.
- Relation proposal: source and target IDs, proposed relation type, direction, and why the relation materially helps reasoning or navigation.
- Safety/consequence flag and a short explanation.
- Attachments only where needed, with file type and rights confirmation.

### Professional profile

Do not require a CV or government identity document for ordinary submissions. Request professional affiliation, qualifications, publications, or verification only when relevant to the subject's risk and the weight assigned to the contribution. Verification of identity/credentials is distinct from verification of the Claim.

## Submission data contract (logical schema)

Every submission should have:

- `submission_id`: immutable unique identifier generated on receipt.
- `schema_version`: intake schema version.
- `submitted_at`: UTC timestamp.
- `submission_type`.
- `subject_area`, `topic`, `title`, `proposal_text`.
- `rationale`, `sources[]`, `evidence_notes`, `applicability`, `limitations`, `uncertainty`.
- `related_record_ids[]`, `proposed_relations[]`.
- `contributor_role`, optional `contributor_profile`, and a separate restricted `contact_record` where needed.
- `rights_and_terms_acknowledged`.
- `risk_flags[]`.
- `status`, `triage_results[]`, `review_events[]`, `decision`, and `release_reference`.

Do not put personal contact details into the public content record. Keep contact information access-controlled and separate from the submission payload used for editorial review wherever feasible. Avoid collecting sensitive personal data unless a specific, justified process requires it.

## Workflow states

1. `received` — accepted by the intake service; tracking ID issued.
2. `needs_clarification` — missing information; questions recorded for the contributor.
3. `triage` — classify domain, risk, duplicates, and target records.
4. `automated_checks` — validate structure, links, bibliographic completeness, likely duplicates, and possible conflicts.
5. `editorial_review` — reviewer evaluates claim wording, scope, evidence relevance, source independence, and architecture fit.
6. `domain_review` — additional subject expert review where required.
7. `decision_ready` — evidence and review comments assembled for decision.
8. `accepted_for_change` — proposal accepted in principle, not yet canonical.
9. `integrated` — controlled repository change has been made and validated.
10. `published` — accepted change is included in a named public release.
11. `rejected` — decision and reason recorded; contributor receives a useful explanation when possible.
12. `withdrawn` — contributor withdrew the proposal; retention follows the published policy.
13. `superseded` — submission replaced by a later linked submission.

A state transition must record actor/role, timestamp, reason, and relevant evidence. Only authorized editors may approve integration; only the release process can mark a contribution as published.

## Automated checks

Automation may:
- validate required fields and schema version;
- normalize identifiers and bibliographic metadata without changing source meaning;
- check link syntax and availability;
- identify probable duplicates and matching Claims;
- identify references to unknown IDs;
- suggest possible contradictions or missing applicability conditions;
- create a reviewer summary and a list of questions.

Automation must not:
- assert that a Claim is true merely because sources exist;
- treat repeated dependent sources as independent corroboration;
- resolve substantive disagreement silently;
- promote a high-consequence submission to publication without the required human review;
- rewrite a contributor's meaning without showing the change and retaining the original;
- write directly into canonical records or publish automatically.

## Review rubric

Reviewers record separate judgments for:

- Identity/architecture fit.
- Clarity and falsifiability of the Claim.
- Source relevance, quality, independence, and traceability.
- Evidence-to-Claim support.
- Applicability and limitations.
- Contradictions and uncertainty.
- Safety/consequence review.
- Human View readability.
- Rights, privacy, and policy compliance.

Use explicit outcomes such as pass, pass-with-limits, needs-work, conflict-unresolved, and fail. Do not collapse these into one opaque quality score.

## Integration contract

When accepted:
1. Map the proposal to existing Claim/Source/Evidence Use/Relation records.
2. Reuse existing identities when updating an existing item; create a new identity only when justified.
3. Preserve source provenance and distinguish quoted source content from contributor interpretation.
4. Record the editorial decision and rationale.
5. Implement the change in a dedicated branch/PR or equivalent controlled change set.
6. Run relevant schema/link checks and the applicable release workflows on the exact candidate.
7. Run substantive review and regression checks for affected relations and dependent Claims.
8. Merge only through the repository's approved process.
9. Publish in a versioned release manifest and link the submission ID to that release.
10. Notify the contributor of the outcome where contact was supplied and permitted.

## Abuse, rights, and operational controls

- Rate-limit intake and protect against spam and malicious attachments.
- Do not accept executable uploads as evidence.
- Define content license and contributor permission before launch.
- Define copyright handling, attribution, takedown/correction process, and dispute handling.
- Publish privacy, retention, deletion, and contact-access rules.
- Provide a high-priority path for credible reports of dangerous errors.
- Keep unpublished peer review, private contact details, and internal deliberations non-public.
- Establish an appeal or re-submission path for rejected contributions.

## MVP implementation stages

### Stage 1 — manual but structured pilot

A hosted or repository-backed form produces a validated structured submission, generates an ID, and routes it to a restricted review queue. Reviewers process it manually using the rubric. No direct canonical writes.

### Stage 2 — assisted triage

Add schema validation, link checks, duplicate/identifier checks, reviewer summaries, and queue status notifications.

### Stage 3 — contributor portal

Add contributor status view, clarification threads, controlled profile verification where needed, and release notifications. Only after privacy/security and operational ownership are established.

## Acceptance criteria

- Every submission gets a unique immutable ID and timestamp.
- Intake rejects or flags malformed submissions without losing the original payload.
- Contact information is separated from public content and limited to authorized access.
- The queue supports all listed workflow states and records transition history.
- Automated checks produce suggestions, not authoritative truth decisions.
- Canonical content cannot be changed by submitters or by automated intake.
- Acceptance requires a recorded editorial decision; high-consequence cases receive additional review.
- Integrated changes preserve provenance, identity, and regression coverage.
- A published contribution is traceable to the release that includes it.
- Rights, privacy, retention, and correction policies are approved before the form is opened publicly.

## Open decisions

- Intake provider and hosting.
- Canonical submission storage and backup/retention policy.
- License and contributor terms.
- Who can approve routine, specialist, and high-consequence changes.
- Expected response targets and urgent safety escalation ownership.
- Whether contributors may choose public attribution, pseudonym, or non-public attribution.
