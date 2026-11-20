# First Edition — Current Execution Checkpoint
Date: 2026-11-20
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`
Branch: `mvp-public-contribution-design-2026-10-11`
PR: #22
Inspection HEAD before this report: `d994f97d94bac85441aa5d8d22a6ecc9465d52b7`

Status: **WP1/WP2 remain open; WP3 implementation gates pass on the inspected HEAD; PR remains Draft and unmerged. This is a report-only checkpoint.**

## 1. Purpose and controlling order

This checkpoint reconciles the current execution state against the controlling first-edition scope and the existing three work packages. It does not change the release scope or authorize a new workstream.

Execution order remains:
1. WP1 — exact-version first-edition corpus selection, evidence/dependency closure and semantic review.
2. WP2 — rights, licensing, editorial accountability, correction/withdrawal and governance.
3. WP3 — selection-aware offline build, artifact inspection and release validation, only after WP1/WP2 approvals.

M13 remains an independent quality-improvement workstream, not a blanket first-edition gate. Only M13 findings materially affecting selected records, high-consequence boundaries or publication integrity block those items.

## 2. Current repository and CI state

PR #22 was re-fetched during this checkpoint:
- State: OPEN
- Draft: true
- Merged: false
- Mergeable: true
- Head: `d994f97d94bac85441aa5d8d22a6ecc9465d52b7`
- Base SHA reported by PR metadata: `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`

The current HEAD was compared with the last code/content HEAD `c8c7694808886657432ab56653225a9682b710c1`. The comparison is exactly one commit ahead and exactly one added file:
- `reports/agent-work/chief-engineer/relation-provenance-a-b-c1-owner-authorization-ratification-2026-11-20.md`
- 84 additions, 0 deletions.
No canonical Content, implementation, workflow, schema, test, allowlist or release-manifest path changed in that final commit.

Four required workflows were independently fetched for the exact current HEAD `d994f97d94bac85441aa5d8d22a6ecc9465d52b7`; all four completed successfully:

| Required workflow | Run ID | Exact-head result |
|---|---:|---|
| Offline Edition | 44773902856 | PASS |
| MVP Contribution Form Browser Tests | 44773902866 | PASS |
| Release Conformance Gate | 44773902945 | PASS |
| Reference implementation tests | 44773903049 | PASS |

The earlier code/content HEAD `c8c7694...` also had 4/4 PASS. The current report records the newer exact-head result and does not transfer the earlier test count or runtime to the new run without inspecting its logs.

The repository `main` branch was read separately and remains at `d58289f319993ede5294a46f4741a506fd2fd710`; this work did not update it. PR #22 remains Draft and unmerged.

## 3. WP1 — exact-version selection and Relation closure

### 3.1 Candidate register boundary

The Part II exact-version master register records 1,130 unique `record_id@version` rows: 1,058 candidate keys plus 72 dependency records. Its represented Part II coverage is 124/385 slices. The 261 other Part II slices are outside the bounded map scope and are not an automatic audit queue. The separate 30 known Claim records across 14 slices remain outside the candidate denominator pending scope triage. Relations are tracked separately from the vertical-slice denominator.

The Part I inventory is separately recorded as 94/94 slices and 980/980 records screened, all HOLD.

These are inventory/coverage facts, not eligibility findings. No INCLUDE or EXCLUDE is created by this checkpoint; no allowlist is created.

### 3.2 Relation status

- All 63/63 Relations have received semantic review; exact participant references were checked.
- 48 were classified as contextual-navigation candidates; this is not release approval.
- 15 remain semantic HOLD.
- The target-specific Context isolation implementation created 61 target-specific Context records and advanced 61 Relation frame references; the two intentional exceptions remain documented.
- Earthquake Event E-Q1 and container/water State W-Q3 retain their owner-directed HOLD / exclusion-from-first-edition-scope decisions; their canonical records remain unchanged.
- Library/Archival endpoint alignment, Research/Statistics endpoint review, Infrastructure Resilience evidence remediation, Labour Economics ILO Path B, Settlement Geography Eurostat remediation, and the A/B/C1 Relation provenance work have their own bounded records and must not be re-applied or widened.

### 3.3 A/B/C1 owner ratification

The owner confirmed A + B + C1 exactly within the existing authorization packet. The implementation predated that confirmation; the ratification report transparently records the chronology and exact scope.

The implementation changed only the six named Relation/Context records and added three source identity/locator records. The three Relations and affected slices remain HOLD. No Claim/Evidence Use changes, rights clearance, INCLUDE/EXCLUDE, allowlist, publication, deployment, merge or main-branch change was authorized.

### 3.4 Remaining semantic and evidence blockers

The semantic-HOLD remediation register and its 2026-11-20 superseding reviews remain controlling. Current known blockers include:
- Air Quality / Power Systems: current endpoints do not establish a demonstrated cross-domain mechanism.
- CO / Emergency Escalation: overlapping Claims; navigation-only at most pending editorial comparison.
- AMR / Plant Health: direct FAO bridge research exists, but canonical evidence linkage and endpoint-fit review remain open.
- Plant Pathology / Entomology and Quantum / Measurement: no canonical endpoint/evidence repair is authorized by the present scope; new Source/Evidence Use/Relation changes require separate bounded owner authorization.
- Research / Statistics: the current pair is a high-confidence navigation candidate, but independent scientific/editorial boundary review remains outstanding.
- M2 Statistics / Research: current endpoints still do not establish the declared research-design link.
- Migration / Labour Economics: ILO 2026 guide is a strong integrated source candidate, but canonical source/provenance linkage and independent semantic review remain open.
- Food Security / Public Health and Settlement / Public Health: WHO bridge evidence is strong; canonical provenance additions were implemented under A/B/C1, but rights, expert review and Human View remain open.

All these Relations and their affected slices remain HOLD. No relation-level research report is itself an owner authorization or independent expert review.

### 3.5 WP1 next actions

1. Do not repeat completed audits or re-apply implemented corrections.
2. Continue only report-only evidence/semantic review where it adds new information to an existing HOLD decision.
3. Before any further canonical endpoint, Source, Evidence Use or provenance mutation, obtain the exact bounded owner authorization for that named change.
4. Obtain independent subject-matter review and Human View for any Relation proposed for first-edition inclusion.
5. Keep the 261 map-external slices and the 30 out-of-master Claims outside the bounded denominator until explicit scope triage.

## 4. WP2 — rights and editorial governance

The current owner decision register still has R-01 through R-10 OPEN:
- R-01 rights holder;
- R-02 original content/data licence;
- R-03 separate software licence;
- R-04 contributor terms;
- R-05 third-party source reuse policy;
- R-06 accountable editor;
- R-07 release approver;
- R-08 correction/dispute/withdrawal process and public contact;
- R-09 attribution/authorship policy;
- R-10 versioned rights-evidence storage and validation.

Source-specific screens are evidence, not legal clearance. Public accessibility is not a reuse licence; attribution is not permission; repository licensing does not clear third-party text, media or datasets. WHO web-page terms are not interchangeable with the WHO publication CC BY-NC-SA policy. The ILO WESO 2023 report's CC BY 4.0 notice applies to that specific report, not all ILO pages. OpenStax-specific blockers were superseded only for the Labour Economics ILO Path B scope; this is not a general rights resolution.

### WP2 next actions

- Keep R-01–R-10 open until the authorized owner records actual decisions.
- Continue item-level rights evidence verification against exact sources proposed for the edition.
- Do not select a licence, name an editor/approver, create contributor terms or infer permission on the owner's behalf.
- Keep all affected records and slices HOLD until the actual distribution model and rights compatibility are reviewed.

## 5. WP3 — selection-aware offline builder

The selection-aware builder is implemented in PR #22 and covered by synthetic positive/fail-closed tests. It uses exact record ID/version, a full 40-character source commit SHA, explicit INCLUDE decisions, per-record approval attestations, exact dependency closure, duplicate/version conflict rejection, and mandatory Claim → Evidence Use → Source closure. Full-corpus diagnostic mode remains available.

The approval attestation is structural metadata; it does not cryptographically authenticate approver identity or authority. No real allowlist has been created and no real selected edition has been authorized or published.

### WP3 next actions

1. Keep the implementation in PR #22 Draft.
2. Do not create a real selection manifest or mark records INCLUDE without separate explicit owner/editorial approval.
3. After WP1 and WP2 approvals, build only the exact approved allowlist and inspect the actual generated artifact.
4. Complete focused reader, security, independent editorial and high-consequence review before any release decision.

Issue #43 (offline `edition_id` hardening and structural HTML regression tests) remains OPEN and is a separate task. It requires its own authorization and branch. It is not included in this checkpoint and must not be started by inference.

## 6. Non-negotiable controls

- PR #22 remains OPEN / DRAFT / NOT MERGED.
- `main` remains unchanged.
- No public or private-preview allowlist is created by this report.
- No INCLUDE/EXCLUDE, publication state, deployment or release approval is inferred.
- No canonical record is changed by this report.
- CI PASS means only the named technical workflows passed on the exact SHA.
- Rights clearance, scientific/editorial acceptance, Human View and owner release approval remain separate gates.

## 7. Next execution sequence

1. WP1: finish only the remaining bounded evidence/semantic work that can be done without changing canonical records; route new canonical changes through exact owner authorization.
2. WP2: continue item-level rights verification and prepare concise, evidence-backed owner decision packets for R-01–R-10; do not invent decisions.
3. WP3: preserve the passing selection-aware builder and its tests; defer real selection/build/release until WP1 and WP2 gates are satisfied.
4. Re-fetch PR state and rerun the four required workflows on one immutable exact HEAD after any subsequent code/content change; documentation-only commits must be checked rather than assumed green.

This checkpoint is report-only and does not supersede the controlling scope, individual authorization packets, canonical records, rights screens or independent review requirements. It supersedes only earlier execution summaries where they conflict with the exact PR/CI facts recorded above.
