# MVP — Real-record pilot readiness reconciliation — 2026-11-15

Status: **private SI preview and local contribution-form artifacts are verified on the current exact PR heads; three-reader comprehension test and publication/operations gates remain open. Public pilot: NO-GO.**

This checkpoint supersedes the operational status in the 2026-11-13 continuation checkpoint while preserving that file as history. It does not authorize publication or deployment.

## 1. Exact PR and CI state

Repository default branch `main`: `203a7028e08da394fd44630fe38727be07bc8849` (unchanged).

| PR | Purpose | Current exact HEAD | Required checks |
|---:|---|---|---|
| #22 | MVP publication gates and professional contribution workflow | `fead1e1b2a6759bb66cc8fe5c7d150272336e1f5` | Reference implementation tests, Offline Edition, Release Conformance Gate — all successful |
| #24 | Offline HTML escaping/security fix | `b0c0522098ef0d7f4613269d921c2f789e9a0a99` | Reference implementation tests, Offline Edition, Release Conformance Gate — all successful |
| #25 | Allowlisted read-only reader / private SI preview | `4b7208adb6a0b957d070409dcfb656a8dfbcd17e` | Reference implementation tests, Offline Edition, Release Conformance Gate, SI private review preview — all successful |
| #26 | Professional contribution intake schema | `6c5c3d4c1788bed05d1ff6e559c0aeb800f42932` | Reference implementation tests, Offline Edition, Release Conformance Gate — all successful |
| #27 | Local-only contribution form / JSON export | `f923edde79e81391f2430ba6b494fc879b07c235` | Reference implementation tests, Offline Edition, Release Conformance Gate, contribution-form browser tests — all successful |

All five PRs remain open, Draft and unmerged. PR #25 is stacked on PR #24; PR #27 is stacked on PR #26. These results establish technical conformance only for the exact heads listed. They do not establish content eligibility, usability, rights clearance, editorial approval or publication permission.

## 2. Private SI preview — exact-head artifact verified

- PR: #25, HEAD `4b7208adb6a0b957d070409dcfb656a8dfbcd17e`.
- Workflow run: `43497005562`, event `pull_request`, exact `head_sha` matches PR #25.
- Artifact: `14072625768`, `mvp-si-private-review-preview-6cd2aa4c500744a0cb44aa9e9c0133131c458fd4`.
- Artifact digest: `sha256:3e7e5381ee575e6462b5ba15a23cb25282d1155d9237e4e11055c9d2339405f1`.
- Pinned preview source revision in the manifest: `6cd2aa4c500744a0cb44aa9e9c0133131c458fd4`.

The downloaded artifact and browser report were inspected. It contains exactly seven allowlisted versioned records:
- `CLM-SI-SEVEN-BASE@1`
- `EU-SI-SEVEN-BASE@2`
- `CLM-SI-DERIVED@1`
- `EU-SI-DERIVED@2`
- `SRC-NIST-SI-UNITS@1`
- `CTX-SI@1`
- `SCP-SI@1`

The accuracy-boundary Claim is excluded. The manifest states `edition_state=preview`, `redistribution_allowed=false`, and `network_required=false`. Desktop and mobile screenshots were inspected; the browser report passed its navigation, search, keyboard-focus and mobile-layout checks and recorded no external requests or browser runtime errors. The exact rendered-index and search-script hashes are recorded in `MVP-PRIVATE-PREVIEW-AND-CONTRIBUTION-FORM-ARTIFACT-INSPECTION-2026-11-15.md`.

This is an internal preview artifact only. Its seven-record selection is not a public release allowlist or a distribution authorization.

## 3. Local contribution form — exact-head artifact verified

- PR: #27, HEAD `f923edde79e81391f2430ba6b494fc879b07c235`.
- Workflow run: `43491454403`, event `pull_request`, exact `head_sha` matches PR #27.
- Artifact: `14069383959`, `mvp-contribution-form-browser-4c1a4171481ca88ca004f9aa8fedbf6ee9a35348`.
- Artifact digest: `sha256:0b4e2600cf282254cb490a2d8796e9d5863f183d186dd50583da24ffe2c689d6`.

The downloaded browser report was inspected. All six JSON scenarios passed schema and browser checks: new Claim, gap/no source yet, correction, contradiction, Source proposal, and Relation proposal. Conditional requirements, duplicate-ID rejection, add/remove/reset behavior, keyboard focus and mobile layout were exercised. The report records no external requests or browser runtime errors.

This remains a local-only form and JSON export. It is not a hosted endpoint, editorial inbox, moderation system or production data-collection service.

## 4. Human and editorial gates

The three-reader non-specialist protocol in `MVP-SI-UNITS-NON-SPECIALIST-READABILITY-TEST-2026-10-14.md` remains **NOT RUN**. All R1–R3 rows are blank. No comprehension PASS is claimed.

The next reader test must use the exact private artifact above, with the protocol's two distinctions:
1. seven base units versus defining constants;
2. the number 22 refers to derived units with special names and symbols, not all derived units.

Recruit three independent non-specialists who have not worked on the repository and do not routinely work in metrology/standards. Use anonymous labels R1–R3; do not collect unnecessary personal data. Do not explain the intended answer before the task. Record unaided comprehension, source navigation and exact confusion. A blocker requires correction and a repeat of the affected task on a newly pinned artifact.

Separate decisions remain outstanding:
- explicit editorial-owner decision for each SI Claim and the exact preview bundle;
- documented rights/attribution decision for the exact bundle, including exclusion of third-party graphics or separately copyrighted assets;
- public terms/licensing and contributor-consent policy;
- privacy, contact-data separation, access and retention policy;
- abuse/spam handling, editorial ownership, reviewer workload and response process;
- correction, takedown, appeal and urgent rollback procedure;
- hosting/domain, operational owner, monitoring, backups and incident responsibility.

A passing reader test does not replace any of these decisions.

## 5. Next permitted sequence

1. Run and record the three-reader protocol on the exact seven-record private artifact. Do not add the excluded accuracy-boundary Claim.
2. Resolve any comprehension or navigation blockers and rebuild/retest only the affected parts, pinning the new source revision and hashes.
3. Obtain the editorial-owner decision and rights/attribution decision for the exact bundle.
4. Close the public operational policies listed above before opening a closed public pilot.
5. Re-run all required workflows on the exact final candidate and inspect the resulting artifact.

## 6. Integrity and release boundary

- No PR was merged or retargeted.
- `main` remains at `203a7028e08da394fd44630fe38727be07bc8849`.
- No canonical Claim, Evidence Use, Source, Context or Scope record was changed by this reconciliation.
- No D/E/B score, public allowlist, publication status, deployment or release decision was changed.
- M13 remains open and draft; the MVP workstream does not waive or close M13.
- **Private technical prototype: PASS. Public real-record pilot: NO-GO.**
