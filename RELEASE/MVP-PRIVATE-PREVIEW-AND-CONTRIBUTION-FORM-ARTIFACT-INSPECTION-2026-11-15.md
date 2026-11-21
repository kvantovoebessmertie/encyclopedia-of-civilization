# MVP exact-head and artifact inspection — 2026-11-15

Status: **private SI review preview and local contribution form browser artifact inspected; public real-record release remains NO-GO.**

## 1. Exact pull-request heads and technical checks

Repository: `kvantovoebessmertie/encyclopedia-of-civilization`

| PR | Workstream | Exact head checked | Required checks |
|---:|---|---|---|
| #22 | MVP publication gates and professional contribution workflow | `6c842922b37da179f01f92904fa5ccef4585fef4` | Reference implementation tests, Offline Edition, Release Conformance Gate — all successful |
| #24 | Offline HTML escaping/security fix | `b0c0522098ef0d7f4613269d921c2f789e9a0a99` | Reference implementation tests, Offline Edition, Release Conformance Gate — all successful |
| #25 | Allowlisted read-only reader and private SI review preview | `4b7208adb6a0b957d070409dcfb656a8dfbcd17e` | Reference implementation tests, Offline Edition, Release Conformance Gate, SI private review preview — all successful |
| #26 | Professional contribution intake schema | `6c5c3d4c1788bed05d1ff6e559c0aeb800f42932` | Reference implementation tests, Offline Edition, Release Conformance Gate — all successful |
| #27 | Local-only contribution form / JSON export | `f923edde79e81391f2430ba6b494fc879b07c235` | Reference implementation tests, Offline Edition, Release Conformance Gate, contribution-form browser tests — all successful |

All five PRs remain open, Draft and unmerged. `main` remains at `203a7028e08da394fd44630fe38727be07bc8849`. CI conformance is limited to the exact heads above and is not a content, rights or publication decision.

## 2. Private SI preview artifact — inspected

- Workflow run: `43497005562`
- Artifact: `14072625768`
- Artifact name: `mvp-si-private-review-preview-6cd2aa4c500744a0cb44aa9e9c0133131c458fd4`
- Preview source revision: `6cd2aa4c500744a0cb44aa9e9c0133131c458fd4`
- Workflow job: `build-private-review-preview` — completed successfully.

The downloaded artifact was inspected, not merely inferred from the green check.

### Manifest integrity

- `edition_state=preview`
- Exactly 7 records selected, each with an input SHA-256:
  - `CLM-SI-SEVEN-BASE@1`
  - `EU-SI-SEVEN-BASE@2`
  - `CLM-SI-DERIVED@1`
  - `EU-SI-DERIVED@2`
  - `SRC-NIST-SI-UNITS@1`
  - `CTX-SI@1`
  - `SCP-SI@1`
- `CLM-SI-ACCURACY-BOUNDARY` is excluded.
- `redistribution_allowed=false`
- `network_required=false`
- Rendered index SHA-256: `5ec3c3b5eff8f9b18c01c1cfcc77b4650294cb7f329744f5cc58d142d6a11299`
- Search script SHA-256: `3cab55efca98e7998231e235761561d4efff56fd997d3fb0e2d6312cb1e21ad1`

### Rendered browser artifact

The desktop (1280×900) and mobile (390×844) screenshots were visually inspected. The browser report returned PASS and recorded:
- exact seven-record private allowlist;
- third SI Claim excluded;
- NIST attribution and claim-specific pinpoints visible;
- qualification that 22 refers to derived units with special names and symbols visible;
- search match/no-match/reset and keyboard focus checks;
- mobile no-horizontal-overflow;
- no external requests;
- no console/runtime errors.

The rendered view visibly labels the edition “Private prototype — not a public edition” and each selected record as `preview_only`. The canonical `publication_status` field is also shown separately; it must not be confused with preview approval or a truth rating.

## 3. Local contribution form artifact — inspected

- Workflow run: `43491454403`
- Artifact: `14069383959`
- Workflow job: `browser-form` — completed successfully.

The downloaded browser report returned PASS. Six JSON payload scenarios were validated:
1. new Claim;
2. gap / no source yet;
3. correction;
4. contradiction;
5. Source proposal;
6. Relation proposal.

Checks included JSON Schema validation, conditional Source and related-record requirements, duplicate-ID rejection, Relation add/remove, Source add/remove, reset, keyboard focus and mobile layout. The report records no external requests and no browser console/runtime errors.

This remains a local-only form and JSON export. It is not a hosted intake endpoint, editorial inbox, moderation system or data-collection service.

## 4. Remaining gates — no implied clearance

1. The prepared three-reader non-specialist protocol remains **NOT RUN**. No participant results or readability PASS are claimed.
2. Independent editorial review and record-level approval remain outstanding.
3. The rights basis is bounded to project-authored factual paraphrases and NIST attribution. No third-party graphics or separately copyrighted material may be copied.
4. Public terms/licensing, privacy and retention, abuse handling, editorial ownership, hosting/operations, correction/takedown and rollback remain open.
5. The seven-record artifact is an internal preview only. It is not a public allowlist, release manifest, deployment approval or permission to distribute.

## 5. Decision

**Technical prototype gates: PASS on the exact heads listed. Private SI preview: built and artifact-inspected successfully. Public real-record pilot: NO-GO.**

No canonical Claim, Evidence Use, Source, Context or Scope record was changed by this inspection. No D/E/B score, public allowlist, publication status, deployment or release decision was changed. No PR was merged and `main` remains unchanged.
