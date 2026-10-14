# MVP Pilot Corpus Selection Worksheet

Date: 2026-10-11  
Status: **selection instrument; no corpus is approved by this document**  
Applies to: private/local preview, closed pilot, and any proposed public edition.

## Purpose

Turn “choose a small, reviewed pilot corpus” into a repeatable editorial decision. The worksheet does not infer release eligibility from `publication_status`, `completion_status`, a passing build, or the existence of a Source/Evidence Use record. Each selected Claim must be reviewed in context, and all linked records needed to interpret it must be included or explicitly handled.

## Selection principles

1. Start from real canonical records, not synthetic fixtures. Synthetic preview fixtures remain test-only.
2. Prefer a small set of self-contained, low-consequence Claims with clear public sources and understandable limits. Do not optimize for quantity.
3. Exclude high-consequence medical, emergency, legal, financial, engineering-safety, and similar guidance from the first pilot unless the relevant specialist review and escalation requirements are already satisfied.
4. Select whole, interpretable record bundles: Claim, Evidence Use, Source, relevant Context, and required Relations/related Claims. Do not publish an orphaned Claim that loses important qualifications.
5. A source is not verified merely because it is official, accessible, or topically relevant. The reviewer must locate the exact passage supporting the full Claim.
6. Rights, privacy, and attribution are hard gates, not soft scores. If status is unknown, exclude the record from the pilot.
7. Keep an auditable decision for every candidate: include, hold for remediation, or exclude, with a reason and reviewer/date.

## Per-Claim eligibility gates

Mark each as **PASS**, **FAIL**, or **UNKNOWN**. UNKNOWN is not a pass.

| Gate | PASS requires |
|---|---|
| Identity and integrity | Exact record IDs/versions resolve; no unresolved alias, mismatch, or broken reference. |
| Claim quality | The statement is clear, appropriately scoped, non-duplicative, and classified as a domain claim rather than generic editorial instructions. |
| Evidence fit | A named reviewer has checked a reproducible page/section/table/paragraph locator and confirmed it supports the whole proposition. |
| Source identity | Source title/creator/issuer and URI describe the same actual work; the destination is accessible enough for a reader to verify. |
| Applicability and uncertainty | Necessary dates, jurisdiction, context, exceptions, and uncertainty are visible. |
| Relations and context | The selected package retains the context and related records required to prevent misleading interpretation. |
| Rights and attribution | License/permission basis and required attribution are recorded and permit the intended distribution. |
| Risk review | Consequence level is identified; any specialist review, warning, or escalation requirement is satisfied. |
| Reader usability | A non-specialist can understand the Claim and navigate to its evidence in the built artifact. |
| Reproducible build | Exact allowlist, record versions, source revision, and output hashes are recorded; the artifact has been inspected. |

**Decision rule:** include only when all applicable gates pass and the named editorial owner approves the exact version. Any FAIL or UNKNOWN means HOLD/EXCLUDE until resolved. Do not “average out” a failed rights, evidence, identity, or safety gate.

## Candidate register

Duplicate this row for each real candidate. Do not populate with synthetic fixtures.

| Field | Entry |
|---|---|
| Candidate key | |
| Claim ID and version | |
| Slice / subject | |
| Claim statement (short) | |
| Related EU / Source / Context / Relation IDs | |
| Exact source locator checked | |
| Reviewer and review date | |
| Rights basis / attribution | |
| Risk class and specialist review | |
| Gate results (PASS/FAIL/UNKNOWN) | |
| Decision (INCLUDE / HOLD / EXCLUDE) | |
| Reason and remediation owner | |

## Batch decision log

| Decision date | Candidate IDs / exact versions | Included count | Held/excluded count | Editorial owner | Review record / rationale |
|---|---|---:|---:|---|---|
| Not yet approved | — | 0 | 0 | Not assigned | No real pilot allowlist approved yet. |

## Allowlist and build handoff

Once candidates pass review, create a separate machine-readable allowlist that records at least:

- exact Claim IDs and versions;
- exact related record IDs and versions needed to interpret them;
- explicit edition state (`preview` during internal work; never bypass the builder's preview-only guard);
- source repository revision;
- reviewer and approval reference for each Claim;
- rights/attribution decision reference;
- a stable hash of each selected record and the generated artifact.

The builder must reject any record not explicitly allowlisted. A green CI run validates code/contracts, not editorial suitability. Inspect the rendered reader and verify that no unapproved record or synthetic fixture is represented as real public content.

## Release decision

The pilot is **not ready** until:
- the candidate register is populated with real records and all required gates pass;
- a named editorial owner signs off on the exact allowlist;
- public license/terms, attribution, corrections/takedown and privacy policy are approved;
- a secure approved intake channel and abuse-handling procedure exist if submissions are accepted;
- hosting, backups, monitoring, rollback and operational ownership are defined;
- Reference tests, Release Conformance Gate, and Offline Edition all pass on the exact release commit;
- the final generated artifact is inspected and release approval is recorded.

Until then, keep the preview local/private and all related pull requests Draft.
