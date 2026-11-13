# Public MVP Specification — 2026-10-11

## Status

**Design draft.** This document defines the smallest responsible public edition of the Encyclopedia of Civilization. It does not authorize publication of the full corpus, changes to the M13 audit, or a production deployment.

## Product objective

Give the public a useful, readable entry point into the encyclopedia while keeping every published knowledge item traceable to its sources, scope, uncertainty, and review history. Enable continuous growth through a separate, structured contribution pipeline.

The public edition and the internal knowledge system must use the same canonical record identities and provenance. The public interface is a presentation layer, not a second independent encyclopedia.

## Product principles

1. Correctness, provenance, and safety outrank speed and item count.
2. Schema/CI conformance is necessary but does not by itself establish substantive reliability.
3. Claims carry their own review state; an article-level label must not imply every Claim is equally supported.
4. Unknowns, applicability conditions, source limitations, and material disagreements are visible.
5. Historical descriptions are distinguished from current practical instructions.
6. High-consequence guidance receives stricter review and clear boundaries.
7. Public reading should be simple; technical detail is available progressively.
8. The system is versioned, auditable, exportable, and designed for offline use.
9. External contributions enter a quarantine/review queue and never alter canonical content directly.
10. User-submitted content is not published merely because it passes automated checks.

## MVP audience and primary jobs

- General reader: find a topic, understand the core explanation, and follow related concepts.
- Careful reader: inspect sources, evidence, applicability, uncertainty, and revision history.
- Professional contributor: submit a structured new Claim, correction, source, contradiction, or Relation.
- Editor/reviewer: triage submissions, inspect evidence and conflicts, record a decision, and preserve provenance.

## MVP surface

### Public pages

- Home page with search and a short explanation of the project's method and limitations.
- Topic index and topic pages for an explicitly selected, reviewed publication set.
- Claim detail view: stable ID where appropriate, plain-language statement, scope/applicability, evidence and sources, known limitations, uncertainty, relevant Relations, review state, and last-reviewed/version metadata.
- Source detail view with bibliographic metadata and links, subject to lawful access and privacy limits.
- Related-knowledge navigation.
- Correction/contribution entry point.
- Editorial policy, review-state definitions, safety notice, privacy notice, terms/licensing, and contact/reporting route.
- Change log for public releases and substantive changes.

### Minimum search

Search published topics and Claims by text and identifier. Results must not expose quarantined drafts, private contributor data, unpublished review notes, or internal audit artifacts.

### Claim-level public states

Use plain labels with explanatory text. Initial vocabulary:

- **Reviewed for publication** — passed the declared editorial checks for this release; not a guarantee of absolute truth.
- **Limited / context-dependent** — valid only under stated conditions or with material limitations.
- **Contested** — credible sources or interpretations materially disagree; disagreement is represented rather than silently flattened.
- **Under review** — only for a public item whose status genuinely changed after publication; explain what is being rechecked.
- **Not included in this edition** — internal state only; do not expose as a public Claim page by default.

Do not display a green check as a universal truth guarantee. Distinguish technical conformance, evidence quality, editorial review, and safety review.

## Publication eligibility gate

A Claim is eligible for the public MVP only if all applicable checks pass:

1. Stable identity and valid links to required records.
2. Required source and evidence-use relationships are present and resolvable.
3. Wording is understandable and does not overstate the evidence.
4. Scope, context, applicability, and important limitations are recorded where relevant.
5. Material contradictions are resolved, explicitly represented, or the Claim is withheld.
6. Safety-sensitive/high-consequence material has the required additional review.
7. Human View review confirms that a non-specialist can understand the meaning and boundaries.
8. The exact release candidate passes the applicable Reference Tests, Release Conformance Gate, and Offline Edition checks.
9. The publication manifest identifies exactly which version and records are exposed.

A passing CI run is not sufficient by itself. A Claim not yet audited under M13 must not be presented as if it passed M13. The publication policy must specify a separate documented basis for any earlier reviewed material admitted to the initial pilot.

## MVP exclusions

- No public editing of canonical records.
- No automatic publication from a form or AI-generated review.
- No public account/reputation/leaderboard system in the first release.
- No promise of exhaustive coverage or professional advice.
- No unrestricted publication of high-consequence procedural instructions.
- No exposing internal notes, private identities, contact details, or confidential review materials.
- No full-corpus release until corpus-level eligibility and release gates are demonstrated.

## Architecture boundary

Public renderer -> versioned publication manifest -> approved canonical records.

Contribution intake -> isolated submission store -> automated triage -> human review -> accepted change proposal -> validated repository change -> versioned release.

The intake store and canonical corpus are separate. Every accepted change retains submitter attribution/permission basis, source provenance, reviewer decision, timestamps, and the release that incorporated it. Rejected or withdrawn submissions do not silently disappear from the internal audit trail, subject to retention/privacy policy.

## MVP acceptance criteria

- A reader can find a published topic and navigate to its Claims, sources, limitations, and related concepts.
- Every public Claim has a resolvable identity and displays its actual review state and applicability boundaries.
- Search and navigation never leak drafts or internal-only metadata.
- A visible route exists to propose a correction or contribution.
- Contributions are stored separately and receive a tracking ID.
- No submission can directly write to the canonical corpus.
- Editorial decisions and accepted changes are auditable and versioned.
- The release manifest is reproducible and identifies the exact corpus revision.
- Applicable automated checks pass on the exact release candidate.
- A human review records usability, accessibility, safety, and misleading-confidence checks.
- Offline/export behavior is documented and tested before claiming it is available.
- Legal, licensing, privacy, and content policy are approved before open intake.

## Open decisions to resolve before implementation

1. The exact pilot topic set and its evidence of publication eligibility.
2. Public display language(s) for the pilot.
3. Repository-driven static publication versus a database-backed service; decide after inspecting existing implementation and deployment constraints.
4. Hosting/domain and operational ownership.
5. License for canonical content and contributor submissions.
6. Minimum personal data needed for professional contributors and retention/deletion rules.
7. Review service levels and escalation path for urgent safety corrections.
8. Whether the first pilot is invitation-only or publicly readable with a limited contribution intake.

## Non-goals

This specification does not claim that a public site, contribution service, deployment, domain, or form endpoint already exists. It defines the acceptance target for design and implementation.
