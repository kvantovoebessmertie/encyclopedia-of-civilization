# First Edition — Release Blocker Reconciliation

Date: 2026-11-23  
PR: #22 — `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `d8fbbe0a06f3ac137fb332000fda25a64962395a`  
Status: **RELEASE NOT YET APPROVABLE — NO PRODUCTION INCLUDE MANIFEST**

This report is the current execution snapshot for the controlling plan:
`RELEASE/PROJECT-EXECUTION-PLAN-FIRST-EDITION-AND-FULL-COMPLETION-2026-11-23.md`.

It consolidates existing evidence and distinguishes genuine release blockers from work that belongs after edition one. It does not grant rights, make owner decisions, alter canonical records, or promote any record.

---

## 1. Executive conclusion

The first-edition work is **not blocked by the need to finish all M13 Claims or all 385 Part II slices**. It is blocked because the current curated candidate sets have not yet produced any approved exact-version `INCLUDE` records, the project-level rights/editorial decisions remain open, and the reader/release path is still preview-oriented rather than a signed production edition.

The current record-level candidate register explicitly says:
- public `INCLUDE`: **0**;
- all exact candidates in that register remain `HOLD`;
- no production allowlist should be generated from HOLD records.

The selection-aware offline builder is implemented and fail-closed, but the implementation documentation explicitly states that **no production INCLUDE manifest is supplied**. The public reader implementation currently supports `edition_state: preview` only. These are honest safety controls, not defects to bypass.

**Therefore: do not publish the full corpus, do not relabel preview records as INCLUDE, and do not wait for full M13.**

## 2. What is already substantially done and must not be repeated

### Part I — survival opening

The controlling Part I inventory records:
- 94/94 mapped slices structurally inventoried and screened;
- 980/980 record files enumerated and record-screened;
- nine early manifest slices contain 112 exact-version records / 33 Claims;
- 85 additional slices / 868 records have exact-record screening;
- zero public INCLUDE decisions; all candidates remain HOLD.

The 112-record survival candidate manifest covers nine slices: emergency alerts, hand-tool safety, home fire/smoke, emergency lighting, septic-system emergency, food safety, food preservation, flood food safety, and power-outage food. Its current disposition is 0 INCLUDE / 112 HOLD. Do not repeat the structural inventory or the completed P1/P2/M3 substantive audits.

Existing P1/P2/M3 work is reusable within its exact scope. Some historical checkpoint validation evidence was not independently retrievable when the candidate register was compiled. P5 disaster-recovery checkpoint validation has since been retrieved as exact-commit 3/3 PASS. Do not treat this as validation of the other checkpoints.

### Part II — wider foundational and civilizational knowledge

The current Part II exact-version master register records:
- 1,058 candidate keys;
- 88 dependency records;
- 1,146 unique exact-version rows total;
- 124/385 Part II slices represented;
- 261 Part II slices not yet registered in this bounded first-edition map.

All entries in the master are HOLD. The 261 unregistered slices are explicitly outside the current bounded candidate map; they are **not** a reason to start a blanket audit before edition one. Preserve the existing broad Part II architecture, but include only records that actually pass release gates.

### Cross-slice Relations

The relation work is substantially inventoried:
- 63/63 Relations inventoried and semantically reviewed;
- 126/126 participant references identity/version/type checked;
- 48 contextual-navigation candidates and 15 semantic HOLD cases;
- shared Context isolation implemented under owner approval, with exact-head validation required.

The 15 semantic HOLD Relations and any unapproved evidence additions remain HOLD. The owner-directed earthquake Event and container/water State decisions remain HOLD/EXCLUDE for edition one. Do not spend release-critical time trying to repair all Relations. Include only Relations required by the exact candidate edition and already supported.

### Rights screening

Seven source-specific rights screens cover 55 table entries / 52 distinct slices. They are preliminary screens, not final clearance. The project-level decisions R-01–R-10 are all still OPEN.

---

## 3. Actual release blockers

### BLOCKER A — no approved exact-version content set

**Severity: STOP — release cannot be assembled.**

- The candidate register has zero public INCLUDE decisions.
- The 112-record survival manifest is inventory plus HOLD decisions, not a release manifest.
- Part II's 1,146 exact-version rows are HOLD; exact identity/dependency verification is not a publication decision.
- The first-edition machine-readable production manifest does not exist.

**Work required:** build a small, coherent first-edition release candidate by reusing completed reviews and closing only the remaining exact record-level requirements for selected records. Assign INCLUDE only after each selected record and its dependency closure pass evidence, applicability, consequence, rights and reader checks. Keep all other records HOLD or EXCLUDE with reasons.

**Do not:** promote whole slices automatically, use the 112/1,146 candidate registers as a manifest, or require all 1,494 M13 Claims / all 385 Part II slices to pass.

### BLOCKER B — project-owner rights and accountability decisions

**Severity: STOP — public release cannot be signed.**

The ten unresolved owner decisions are:

| ID | Decision still required |
|---|---|
| R-01 | Identify the rights holder and evidence of authority |
| R-02 | Select licence / rights model for project-authored text and structured data |
| R-03 | Decide separate software/code licence |
| R-04 | Adopt contributor submission terms |
| R-05 | Adopt source reuse policy |
| R-06 | Name accountable editor |
| R-07 | Name release approver |
| R-08 | Establish monitored correction/dispute/withdrawal contact and process |
| R-09 | Adopt authorship and attribution policy |
| R-10 | Define rights evidence register and validation |

These cannot be inferred from Git history or decided by automation. The current owner decision record recommends conservative defaults but marks them as proposed, not adopted. No licence, rights holder, editor, approver or public contact is invented in this report.

**Work required:** prepare/approve the compact owner decision record; complete item-level rights review for the actual selected release records and displayed assets. Unclear third-party material must be excluded or linked without reproduction until permission/compatibility is established.

### BLOCKER C — first-edition reader/release is preview, not production

**Severity: STOP for public release; private preview work can continue.**

Verified implementation boundaries:
- `REFERENCE/SELECTION-MANIFEST.md` requires schema 1.1, exact IDs/versions/types/schemas, `decision: INCLUDE`, explicit APPROVED attestation and complete explicit dependency closure.
- The selection-aware builder rejects HOLD/EXCLUDE, missing approval, stale versions, undeclared/unselected dependencies, and incomplete Claim → Evidence Use → Source closure.
- The documentation states no production INCLUDE manifest is supplied.
- `REFERENCE/src/encyclopedia_reference/public_reader.py` is a read-only preview builder and accepts `edition_state: preview` only.
- The existing full-corpus offline builder is not a curated first-edition release. A selected release must be built from the exact approved manifest.

**Work required after BLOCKER A:** complete a production reader/edition path that consumes the approved selection manifest, visibly distinguishes reviewed/limited/excluded states, exposes evidence and source links, excludes HOLD/private/internal material, and produces a reproducible offline bundle with manifest and hashes. Do not weaken fail-closed rules.

### BLOCKER D — current candidate-level evidence and high-consequence closure

**Severity: STOP only for affected records; not a reason to re-audit the whole corpus.**

Known examples in the current candidate register:
- SI Units is the strongest low-risk private-preview candidate: exact seven-record closure and NIST section locators were checked. It remains HOLD because Context/Scope target Claim A only, release-facing Human View/editorial sign-off is absent, and project/item-level rights remain open.
- P1 emergency cluster: substantive/Human View work is reusable, but historical checkpoint validation evidence was not independently retrievable in the register review. Validate the relevant current reviewed commit or retrieve exact historical evidence; do not repeat the content audit.
- P2 food cluster: substantive/Human View work is reusable, but exact historical checkpoint validation evidence was not independently retrievable; validate the reviewed checkpoint/current exact records, then close rights and record-level dependencies.
- P3 disaster response: exact sources and direct passages were inspected, but current canonical EUs lack reproducible pinpoint locators and Context/Scope target Claim A only; all remain HOLD.
- Other inspected survival slices have specific locator, target-applicability, source identity, rights or qualified-review gaps recorded in the candidate register.

**Work required:** use the existing record-level candidate register as the queue; prioritize low-risk explanatory records with reusable prior audits. For each chosen Claim, close only its actual pinpoint, target-specific Context/Scope, exact dependencies and reader presentation. High-consequence operational procedures remain out until qualified review is documented.

### BLOCKER E — final artifact and exact-head release sign-off

**Severity: STOP at final publication stage.**

Once A–D are closed for the selected bundle:
- freeze one immutable release SHA and exact-version allowlist;
- build the selected offline edition from a clean checkout;
- inspect the actual artifact and its hashes;
- pass Reference Tests, Release Conformance Gate, browser/security tests and Offline Edition on that exact SHA;
- perform independent editorial/Human View and non-specialist reader review;
- record rights/attribution, known limitations, correction/takedown route and rollback;
- obtain explicit owner release approval.

---

## 4. Current exact-head technical state

PR #22 is OPEN / Draft / NOT MERGED. Base is `main`; no merge or publication has occurred.

The new plan commit / current inspection HEAD is:
`d8fbbe0a06f3ac137fb332000fda25a64962395a`.

Latest observed workflow runs for this exact HEAD:
- Offline Edition — **PASS** (run 45162362941).
- Reference implementation tests — **IN PROGRESS** (run 45162362775).
- Release Conformance Gate — **IN PROGRESS** (run 45162362933).
- MVP Contribution Form Browser Tests — **IN PROGRESS** (run 45162362779).

Do not report 4/4 PASS until the three in-progress runs complete successfully. The earlier 4/4 result on HEAD `a56bce1...` is historical evidence for that exact older HEAD, not a substitute for this run.

PR #21 M13 remains a separate Draft workstream. Full M13 is not a first-edition prerequisite; only a concrete M13 issue affecting a selected record, safety boundary, material Relation or release integrity becomes a release blocker.

---

## 5. What can be done by the implementation team without new owner decisions

1. Poll the three in-progress exact-head workflows and inspect failed jobs/steps if any.
2. Produce a compact exact-version queue from the existing candidate register; do not redo closed audits.
3. Recover or replace missing historical checkpoint validation evidence with a current exact-head validation where appropriate.
4. Perform noncanonical direct-source and exact-dependency checks for the next small, low-risk survival-first candidate set.
5. Prepare a proposed rights/owner decision packet with conservative options and precise consequences; do not adopt it on the owner's behalf.
6. Complete the selected-manifest and production-reader implementation only after the first approved record set exists.
7. Keep internal reports, HOLD records, private previews, contributor contact data and M13 working material out of the public bundle.

## 6. What requires the project owner's explicit action

Only the owner can:
- establish the legal rights holder / authority;
- select or defer the project content/data licence and software licence;
- appoint the accountable editor and release approver;
- authorize a monitored correction/takedown contact route;
- approve contributor terms and authorship policy;
- approve the exact first-edition allowlist and the final release.

If the owner does not want to decide every long-term policy before a private preview, the project may continue with a non-public preview. It may not be represented as a public first edition or redistributed as an approved release.

---

## 7. Execution order from this report

1. **Now:** finish exact-head CI on `d8fbbe0...`; record true results.
2. **Next:** create the smallest coherent survival-first release candidate from already-audited records; begin with low-risk explanatory content and reuse P1/P2/P3/M3 work without repeating it.
3. **In parallel:** prepare one owner-decision packet for R-01–R-10 with conservative proposed defaults and a clear sign-off section.
4. Close the selected candidates' exact evidence locators, dependency and applicability checks, item-level rights, Human View and any qualified review.
5. Freeze the first production allowlist only after actual INCLUDE decisions exist.
6. Complete production reader/offline packaging, exact-head CI, artifact inspection and final sign-off.
7. After first release, resume full M13 and wider corpus completion under the main project plan.

## 8. Change-control statement

This is a noncanonical release-planning/reconciliation report. No Claim, Evidence Use, Source, Context, Scope, Relation, Assessment, Inference, Decision, candidate disposition, allowlist, licence, rights grant, publication state, `main` branch or PR merge was changed by this report.


---

## 9. Historical checkpoint validation recovery — 2026-11-23 addendum

A fresh GitHub Checks lookup was performed against the exact historical commit SHAs named in the candidate register. Where the commit exists, the workflow jobs were also inspected.

### Exact historical commits with recoverable 3/3 PASS

| Audit checkpoint | Exact commit inspected | Reference tests | Release Gate | Offline/build workflow | Result |
|---|---|---|---|---|---|
| P1 correction baseline | `b83a37df4d44c151cda8e4d74e370390902dcc44` | PASS | PASS | PASS | 3/3 |
| P2 clean checkpoint | `3e2971a87119d746c277c6607875a56673dfe764` | PASS | PASS | PASS | 3/3 |
| P3 clean checkpoint | `d8600b53c225fefb7c1beae924a85556ceb1d4d6` | PASS | PASS | PASS | 3/3 |
| P5 clean checkpoint | `b0da033bc3e566c5a2259598e660c4abcfef63fc` | PASS | PASS | PASS | 3/3 |

For all twelve workflow jobs above, the job conclusion was `success` and no failed steps were present.

### Exact commit references still unavailable

- P1 clean checkpoint commit `2974a8e9d4c69c6f8bf922ba7b405d6afe55de4b`: GitHub reports no commit found for this SHA.
- P2 correction commit `b7ccf467a3a1452c020be9b5dc414b2d4f702a79`: GitHub reports no commit found for this SHA.
- M3 clean candidate commit `bb3a348afc4ff3470ae16c5f90421a0796bc5403`: GitHub reports no commit found for this SHA.

P1's later correction baseline is now verifiably 3/3 PASS, but this does not prove the unavailable P1 clean-checkpoint SHA itself. P2, P3 and P5 exact checkpoint technical validation is now recoverable. M3's old candidate checkpoint remains unavailable.

### Consequence for first-edition work

This recovery closes several historical technical-evidence gaps and reduces duplicate work. It does **not**:
- assign INCLUDE to any record;
- supply missing current canonical Evidence Use locators;
- resolve target-specific Context/Scope applicability;
- close item-level or project-level rights;
- provide qualified high-consequence review;
- create a production allowlist or approve publication.

Do not repeat P2/P3/P5 technical checkpoint validation unless a new canonical change makes it necessary. Reuse these exact results for their stated commits only.

### Current PR #22 state after this report update

- PR #22 remains OPEN / Draft / NOT MERGED; `main` is unchanged.
- Newest report commit at time of this addendum: `75232c33165bf45a0a91c6b2a236e8b63bbf05bc`.
- On that exact HEAD, three PR workflows were queued/pending: Reference implementation tests, MVP Contribution Form Browser Tests, Release Conformance Gate. No final PASS is claimed until they complete. The Offline Edition PASS previously observed at the immediately preceding HEAD is not represented as a PASS on this newer SHA.

This addendum is evidence reconciliation only; no canonical record, disposition, allowlist, rights decision or publication state was changed.
