# M13 — Phase 0 Closure Addendum and Phase 1 Scope Lock

Date: 2026-11-17

Branch: `m13-system-wide-depth-audit-2026-10-09`

PR: #21, open and Draft; no merge authorized

Disposition: **OPEN / NOT RELEASE-READY**. This addendum corrects the
operational reading of the 2026-11-17 revalidation checkpoint; it does not
declare the M13 audit complete or authorize Phase 1.

## 1. Baseline and evidence

The source HEAD before this addendum is
`dde6610971e43922d68daf36fe0a8da370b017cd`; PR #21 targets
`m12-human-factors-source-and-human-view-2026-10-09` at
`e87e5bba60c9ed1101ecd4d53493c968c4760dac`. The observed `main` HEAD is
`d58289f319993ede5294a46f4741a506fd2fd710`. This replaces the earlier
checkpoint's `main` reference for current coordination, not its historical
record. Recheck all refs before any later integration.

The historical reconciliation below is **cited**, not regenerated on
`dde66109`. PR #35, report
`reports/agent-work/m13-auditor/phase-0-independent-review.md` at
`d2861284d3acebb32a4713ba3dab953cc9581b17`, §5.5, cross-joined the queue
artifact 14321250860 and scored-ledger artifact 14319589240 from source
revision `92d76761bdc6e6d1bdbcfd74608652ae555b4fd3`. PR #34's plan and PR #40's
remediation report describe that baseline; they do not establish its counts
for a later revision.

| Historical population / observation | Reconciliation at `92d76761` |
|---|---|
| Claims marked UNASSESSED by the risk queue | **751/751** have at least one prior scored-report row |
| Claims selected by that queue | **100/100** have at least one prior scored-report row |
| Repeated assessment groups | **7 groups, 14 rows**; no established supersession rule |

The comparison stripped `@version` and separators for matching; it is not
proof that each prior row assesses the exact current Claim version. UNASSESSED
means no risk-domain or machine-triage metadata, not absence of earlier D/E/B
rows or low risk. The selected 100 are routing candidates with prior scored
rows, not a proven first-time review population.

A report mention is a retrieval lead; a queue entry is machine routing; a
scored row is historical assessment metadata. None by itself proves a
complete, current-version, claim-specific substantive review. Scores and
review depth are heterogeneous; do not infer acceptance, source fit, completed
D/E/B, Human View, independent review, or publication clearance from a row.
The 1,501 historical scored rows have not been individually validated here.

## 2. Unresolved provenance

- **14 Claim IDs: UNRESOLVED.** The preliminary screen reports 17 inspections
  and names only three; the remaining 14 identities cannot be reconstructed
  from counts, topics, queue selections, or the separate 17 holdouts. Do not
  include unknown IDs in unique coverage. PR #39, report
  `reports/agent-work/evidence-researcher/14-id-and-prior-audit-provenance.md`
  at `8e9217bacecf2924993216deae2d8082b804c3a8`, §5.1, records the
  search and its limits, including input artifact 14071268296. Release
  requires original notes or another primary record identifying each exact
  `Claim ID@version` and its provenance; otherwise the discrepancy remains
  open. A separately authorized new screen is not a reconstruction.
- **Prior independent REJECT D1–D4: provenance UNVERIFIED.** The earlier
  checkpoint and protocol assert it, but PR #39 §5.2 found no confirmed
  primary report, reviewer, audited SHA, or supporting artifact. Do not
  present the REJECT or its remediation as an independently proven result.
  PR #35 is a distinct, conditional review, not the missing primary report.

## 3. PR #21 / PR #28 and governance decision

PR #21 remains the M13 integration branch and Draft PR. PR #28 remains open,
Draft, and untouched: **do not merge, close, retarget, or use it to overwrite
governance files**. At the observed heads, its six `.github` governance blobs
are identical to M13's; it contributes no distinct current governance
content. Those six blobs differ from `main@d58289f3`; the main reporting
template is absent on both M13 and #28. PR #38, report
`reports/agent-work/ci-engineer/phase-0-exact-revision-and-governance-report.md`
at `f5f8245e025963ff7caf3759eb21bb3bac6cad32`, §§5.6–5.8, documents the
overlap and integration risk. Blob identities were rechecked against current
M13, #28 head `3127aa64313ae1c76075d3c53e44d38e836df325`, and that main
revision for this addendum.

Governance synchronization is **not performed**. If separately authorized,
compare the then-current three heads, explicitly reconcile the six files and
`reports/agent-work/REPORT-TEMPLATE.md` against main, preserve both applicable
rules, verify the resulting blobs and integration diff, and run exact-head CI.
Do not blindly take either side or merge main. The owner must decide the
eventual disposition of #28; other integration conflicts require separate
review. This is a coordination decision, not a claim that governance drift
has been resolved.

## 4. CI and Phase 0 conditions

PR #34 head `fb2b11af62554caf2fb5bee261494cff1d145b94`, Offline Edition
push run `44077774361`: **completed / action_required, not PASS**. PR #38
§5.2 records zero jobs and no approval; the reason for the gate was not
verified. Approval and a successful run, or an explicitly recorded alternative
decision by the owner, remain necessary; do not count it as a passing check.

The source HEAD `dde6610971e43922d68daf36fe0a8da370b017cd` had successful
PR runs Reference `44145701081`, Release Gate `44145701078`, Offline Edition
`44145701128`, and push runs Audit Queue `44145681202` and Offline Edition
`44145680824`. These results apply **only to that SHA**. They do not prove CI
for the commit adding this document. Exact-head runs and artifacts must be
checked after that commit is pushed; missing, pending, action_required, and
failed checks are not PASS. A document cannot contain its own commit SHA.

| Phase 0 condition | Decision / remaining condition |
|---|---|
| Correct 751/751 and 100/100 accounting and current main reference | Addressed in §§1–2, with revision and matching limitations. |
| 14 IDs and prior REJECT provenance | Explicitly unresolved; obtain primary evidence or retain the unknowns without inferred coverage. |
| Seven repeated-score groups | Preserve all rows; no automatic supersession. Owner approval of an adjudication rule and per-group decisions remain open (§5). |
| PR #21 / #28 governance | Safe no-merge coordination decision recorded (§3); governance synchronization and owner's #28 disposition remain open. |
| PR #34 CI | `action_required` recorded, not PASS; approval/success or explicit owner decision remains open. |
| Addendum exact HEAD | Verify required checks and relevant artifacts against the new SHA; previous-head success is not transferable. Recompute the PR changed-path inventory/hash if used. |
| Independent review | PR #35 is conditional at `92d76761`, not an independent review of this addendum or its final HEAD. A second review remains required; no new agent was invoked for this task. |
| Workflow provenance | PR #38 §5.4 identifies missing explicit revision assertions in the Audit Queue and Generic EU Coverage workflows; a separately authorized fix and verification remain open. |
| Phase 1 authorization | Scope below is a lock proposal; explicit separate owner authorization is required before execution. |

## 5. Phase 1 Scope Lock — proposed, not started

**Input freeze:** capture the exact approved M13 HEAD, PR base and main SHA;
generate reproducible, revision-bound inventory and artifacts. The historical
denominator is 1,494 Claims, not a substitute for revalidation at the approved
HEAD. If the count or tree differs, report the discrepancy and obtain a new
scope decision rather than silently changing the denominator.

**Inventory and identity:** reconcile all 1,494 Claims to canonical record
path, internal ID, exact version, slice, Evidence Use and Source references.
Use `Claim ID@version` as the working key; preserve original IDs, versions,
paths and historical spellings. Separator normalization and documented aliases
are matching aids only, with an explicit crosswalk and collision/ambiguity
exceptions; never rewrite or merge canonical identities. Reconcile version
differences and the historically reported 16 version-2 Claims without
assuming a prior row applies to a different version.

**One prior-assessment register:** one auditable history per Claim key, linked
to all candidate rows and exceptions. For each occurrence retain report path,
line/table row, source revision/artifact, exact or inferred match type,
version, review scope, reviewer and date if documented, source and exact
pinpoint, D/E/B and rationale if stated, disposition, limitations and
provenance. Unknown fields remain unknown. Distinguish incidental mention,
machine routing, scored row, provisional review, substantiated assessment and
independent review. Preserve all prior rows; do not award scores from metadata.

**Repeated assessments and final status:** for all seven known groups and any
new repeats, retain each row and its provenance. A later date or higher score
does not supersede an earlier row automatically. Until an owner-approved rule
and claim-specific adjudication identify the applicable version, evidence,
reason and explicit predecessor/successor links, mark the conflict unresolved;
do not manufacture a final score. Proposed rule for approval: supersession
requires an explicit, traceable adjudication for the same exact Claim version,
with source pinpoints and rationale, preserving the earlier row; cross-version
applicability needs separate evidence. Conflicts or missing identity/provenance
remain unresolved.

**Separate outcomes:** `REVIEWED` requires documented claim-specific scope,
source pinpoint and reasoning for the exact version; it is not a release
clearance. `HOLD` records a known blocker and release criteria. `REJECT`
requires an explicit evidence-backed rejection, reviewer and reason;
historical unverified assertions do not qualify. `UNRESOLVED` covers unknown
identity, version, provenance or conflicting assessments. Keep review,
evidence, risk, Human View, high-consequence and independent-review gates as
separate dimensions; the four outcomes do not erase those gates or equate a
historical scored row with review. For the single summary status use this
precedence: `UNRESOLVED` when identity, version, provenance or assessment
conflict prevents a defensible decision; otherwise `REJECT` for an explicit
evidence-backed rejection; otherwise `HOLD` while any required gate is blocked
or review is incomplete; otherwise `REVIEWED` only when its stated
claim-specific evidence is present. Retain every underlying gate and reason
even when another outcome takes precedence. Unresolved conflicts must not be
promoted to REVIEWED.

**Packages:** after reconciliation and separate authorization, produce
deterministic, frozen, non-overlapping packages of 20–30 distinct Claim keys;
record input SHA, manifest, owner, scope, dependencies and outputs. Balance the
last packages rather than creating a smaller remainder. For a confirmed
1,494-key denominator, one valid partition is 49 packages of 30 and one of 24;
this is arithmetic, not an already created or assigned package. Verify union
equals the frozen inventory and pairwise intersections are empty. If ambiguous
identities prevent stable unique keys or a complete union, retain the
exceptions and stop package creation until a documented identity decision;
do not silently assign or merge them.

**Exit criteria:** reproducible full-inventory reconciliation, explicit
exceptions, a provenance-backed register, approved supersession and
disposition rules, unique package manifests and independent review. Carry the
14 unknown IDs, source-fit, Human View, high-consequence and other unresolved
gates forward; no count of processed worklists establishes audit completion.
No canonical Claim, Source, Evidence Use, Assessment or other record change,
new score, batch execution, or Phase 1 work is authorized by this lock.
