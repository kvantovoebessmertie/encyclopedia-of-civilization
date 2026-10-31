# MVP — gate for selecting the first real-record pilot corpus

Date: 2026-10-17  
Branch: `mvp-reader-prototype-2026-10-11`  
State: **PREPARATION ONLY — no real records approved, no publication authorized**

## 1. Purpose

Turn the current synthetic reader into a bounded, reviewable real-record pilot without treating the entire encyclopedia as release-ready. This document defines the decision procedure and evidence required before any real record enters a pilot build. It does not itself select or approve records.

## 2. Current verified boundary

- The browser reader is a technical prototype and currently renders exactly two synthetic fixture records.
- The exact-head browser workflow has passed its configured desktop/mobile checks, including search, keyboard focus order, mobile viewport behavior, and an empty browser error list.
- The reader and its manifest explicitly identify the build as a private synthetic preview; synthetic fixture data is not evidence of the truth of any Claim.
- Technical success does not establish content accuracy, source rights, editorial approval, privacy readiness, or authorization to publish.
- The existing contribution workflow is local JSON export only; it is not a server submission or moderation system.
- No real-record pilot allowlist is approved in this gate.

## 3. Pilot scope principle

The first pilot must be a small, coherent, low-complexity corpus that demonstrates the Claim → Evidence Use → Source chain and useful reader navigation. Do not begin by publishing high-consequence prescriptive guidance merely because it already exists in the repository.

Prefer a small candidate set with:
- clear, stable public sources and verifiable exact passages;
- explicit scope and context;
- understandable claims that do not require specialist interpretation to avoid harm;
- no unresolved source-linkage, identity, version, rights, translation, or safety issue;
- sufficient variety to test record navigation without implying broad domain coverage.

The initial candidate selection is **not yet made**. Candidate records must be reviewed individually; slice names and machine flags are not approval.

## 4. Mandatory record-level acceptance gates

A candidate record may be proposed only when every applicable gate below has an evidence pointer.

| Gate | Required evidence | Fail-closed rule |
|---|---|---|
| Identity and version | Exact `record_id`, `record_version`, `type_version`, schema and current branch/commit | Missing or ambiguous version → exclude |
| Chain integrity | Resolvable Claim → Evidence Use → Source links; no dangling or silently substituted reference | Broken link or version mismatch → exclude |
| Passage fit | Exact source passage/section and context support the whole Claim, not merely the topic | Generic or partial support → exclude or hold |
| Scope and limits | Applicable population, place, conditions, uncertainty and limitations are visible where material | Material scope omitted → exclude or hold |
| Currentness | Source date/current status checked; date-sensitive claims marked for recheck | Stale/unclear currentness → hold |
| Independence | Source lineage assessed; duplicate republications not counted as independent corroboration | Independence unknown when material → hold |
| Consequence review | D/E/B assessment and written rationale; high-consequence content gets qualified Human View | Unresolved high-consequence concern → exclude from first pilot |
| Rights and attribution | Source licence/terms and attribution requirements checked; project’s right to display derived text and metadata recorded | Unclear rights → exclude |
| Human-readable view | Reader summary preserves meaning, uncertainty, scope and source links; technical/raw view remains available as designed | Meaning changes or citations disappear → exclude |
| Privacy/security | No unnecessary personal/sensitive data; rendered text escaped; no unsafe external resource loading | Privacy/security issue → exclude |
| Correction and withdrawal | Responsible contact, correction path, review history, and a withdrawal/takedown procedure are defined for the pilot | No accountable correction path → do not release |
| Reproducible build | Explicit ID/version allowlist, pinned builder, generated manifest/digest, offline and release-gate checks pass on one exact commit | Failed/missing gate → no release |
| Independent review | Reviewer who did not author the record confirms the above evidence | No independent review → preview only |

## 5. Pilot selection register

For each proposed record, create a row in a separate review register containing:
- exact record ID and version;
- proposed reader-visible summary;
- Claim, Evidence Use and Source references;
- exact source locator and a short passage-level rationale;
- D/E/B values and their definitions/rationale;
- source date, rights/attribution result and reviewer;
- risk classification and any required specialist review;
- decision: `PROPOSED`, `HOLD`, `REJECTED`, or `APPROVED FOR PILOT`;
- review date, evidence links, and commit SHA.

The register must distinguish an approved record from an approved slice. Approval is not inherited by adjacent records, duplicate-looking IDs, or a whole topic area.

## 6. Required project-level gates before the pilot is called public

1. **Corpus gate:** every included record is explicitly allowlisted by ID and version; no accidental full-corpus inclusion.
2. **Editorial gate:** a named accountable editor and independent reviewers are recorded; disputed content and correction handling are defined.
3. **Rights gate:** source and derived-content reuse terms have been checked and recorded; attribution is rendered correctly.
4. **Privacy gate:** data minimization, retention, contact/intake handling, and any applicable jurisdictional obligations have been reviewed.
5. **Operations gate:** hosting, backups, update cadence, monitoring, security contact, and withdrawal procedure are assigned to an accountable owner.
6. **Technical gate:** release build is reproducible and offline-capable as promised; security, reader, schema, preflight, release-conformance and regression tests pass on the exact release commit.
7. **Independent sign-off:** reviewer records decision and date against the exact release candidate.
8. **Explicit authorization:** public release is a separate decision. Passing CI or this document does not publish anything.

## 7. Current decision

**NO-GO for a real-record public pilot at this checkpoint.**

Reason: the reader prototype has demonstrated technical behavior with synthetic data, but no real-record allowlist has been approved in this gate, independent reviewer sign-off is outstanding, and the editorial/rights/privacy/operations decisions required for a public pilot are not recorded here.

This is a scoped, actionable block—not a claim that the whole encyclopedia must be complete first. The next content action is to propose a very small candidate set and evaluate each record against Section 4, then obtain independent review. Do not alter canonical JSON records as part of this selection step; corrections require separately authorized, versioned changes and regression tests.

## 8. Change control

- Keep this gate in the MVP prototype branch until review.
- Do not merge the draft PR, publish a public URL, or label the pilot released on the strength of this document.
- Re-evaluate the decision only after the record register, rights/editorial/privacy/operations evidence, independent sign-off, and exact-commit CI results are present.
