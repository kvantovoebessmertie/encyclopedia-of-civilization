# Public Pilot and Release Gates — 2026-10-11

## Purpose

Turn the public MVP and professional contribution specifications into a controlled, testable release plan. This workstream is independent of M13 and must not change M13's scope, scoring, evidence, or closure criteria.

## Workstream separation

- M13 remains on its existing branch/PR and continues its full audit. Do not close M13 until the agreed complete audit, defect register, Relations/evidence/applicability review, independent re-check, and exact-head release checks are complete.
- Public MVP design is maintained on `mvp-public-contribution-design-2026-10-11`, branched from `main`.
- The MVP design PR must not merge into `main` until its documentation has been reviewed and any architectural conflicts with the existing standard/reference implementation are resolved.
- Do not copy unaudited M13 output into the public pilot by default.

## Work sequence

### P0 — Freeze requirements (current step)

Deliverables:
- Public MVP scope and acceptance criteria.
- Claim-level publication-state vocabulary and eligibility gate.
- Professional contribution schema and workflow.
- Release gates, non-goals, and unresolved decisions.

Exit criteria:
- The specifications are internally consistent.
- No design implies that CI alone proves substantive correctness.
- No intake path can write directly to canonical records.
- M13 remains untouched.

### P1 — Architecture fit and implementation decision

Inspect the current Reference Implementation, record schemas, release scripts, Offline Edition, and existing publication/export mechanisms. Produce a mapping table:

- existing capability and file/path;
- reuse/adaptation needed;
- missing capability;
- tests required;
- security/privacy implication;
- dependency on M13 or independent of it.

Choose a publication approach only after this inspection. Prefer the smallest implementation that preserves stable record IDs, deterministic builds, provenance, and offline/export requirements. Do not introduce a new database or framework without a demonstrated need.

Exit criteria:
- Data source and public manifest are explicit.
- Public/private boundaries are specified.
- Search, topic view, Claim detail, source links, relations, and correction intake have implementation owners and test cases.

### P2 — Build a non-public prototype

Deliverables:
- Read-only rendering for a small, explicitly reviewed sample.
- Claim/source/Relation navigation.
- Review-state and applicability presentation.
- Search over the sample.
- Versioned publication manifest.
- No public submission endpoint and no production domain yet.

Exit criteria:
- Sample is selected by documented criteria, not convenience alone.
- Every displayed Claim links to evidence/source metadata as applicable.
- Drafts and internal audit material are excluded.
- Human View usability check is recorded.
- Build is reproducible from a pinned corpus revision.

### P3 — Structured contribution pilot

Deliverables:
- Intake form matching the contribution schema.
- Unique submission ID and receipt acknowledgement.
- Restricted queue with statuses and decision history.
- Manual reviewer rubric and clarification/rejection templates.
- Rights, privacy, retention, and correction policies.

Exit criteria:
- Test submissions can be received, tracked, clarified, rejected, accepted, integrated, and linked to a release.
- No submitter or intake service can directly alter canonical records.
- Spam, malformed input, link failure, privacy, and attachment handling are tested.
- Public intake remains closed until an operational owner is assigned.

### P4 — Closed public pilot

Invite a small group of readers and selected professionals. Test:
- findability and comprehension;
- whether review states are understood correctly;
- source and relation navigation;
- reporting a correction;
- contribution completion rate and reviewer workload;
- safety and privacy issues;
- offline/export behavior if included in the release claim.

Record findings and fix blockers before opening wider access.

### P5 — Public MVP release

Required release packet:
- release manifest and exact corpus revision;
- public-topic and Claim eligibility list;
- passed technical workflows on the exact release candidate;
- substantive and Human View sign-off;
- unresolved limitations and exclusions;
- privacy, licensing, contributor, editorial, and correction policies;
- rollback and urgent correction procedure;
- operational owner and monitoring/contact route.

A release can be small. It must not claim full-corpus completeness or that every Claim has passed M13 unless the evidence explicitly supports those statements.

### P6 — Continuous improvement

- Triage contributions by safety, materiality, and user impact.
- Publish versioned updates with change notes.
- Re-run affected-Claim, Relation, source, and cross-domain regression checks.
- Track submission backlog, time to first response, acceptance/rejection reasons, duplicate rate, and escaped defects.
- Periodically sample public pages with Human View review.
- Expand topic coverage only when the publication gate can be met.

## Minimum release blockers

Do not launch a public pilot if any of these is true:
- a public Claim has unresolved critical contradiction or materially misleading wording;
- source/evidence links are broken or provenance cannot be traced for a material Claim;
- review state is ambiguous or implies a guarantee not supported by the process;
- high-consequence content lacks the required additional review or boundaries;
- private contact details, drafts, reviewer notes, or restricted records can leak;
- content license, contributor rights, or privacy/retention policy is undefined;
- a contribution can mutate canonical data without controlled review;
- the exact release candidate is not reproducible or required workflows fail;
- no one is responsible for urgent corrections and rollback.

## Metrics (measure quality, not vanity)

- Share of published Claims meeting all applicable eligibility criteria.
- Number and age of unresolved high-severity public issues.
- Source traceability and broken-link rate.
- Human View comprehension results.
- Contribution completeness and duplicate rate.
- Median time to first response and decision.
- Fraction of accepted contributions traceable to a specific release.
- Offline/export verification status.
- Number of corrections required after publication and their severity.

Do not optimize solely for page count, submission volume, or the percentage of Claims labelled reviewed.

## Current state

- Requirements documents are being prepared on a separate branch from `main`.
- The public site, live form, hosting, production endpoint, and launch date are **not** claimed to exist.
- M13 remains open and draft. Its audit is not waived by this plan.
