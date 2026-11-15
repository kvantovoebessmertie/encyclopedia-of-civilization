# M13 — Post Package 31 Coverage Reconciliation and Canonical Remediation Gate

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Source revision: `814a441c9e3ab35e2ef2adf2fbdc0c810b9b4f2e`

## 1. Risk-priority queue: exhausted, not M13-closed

The post-Package-31 queue workflow completed successfully:
- Workflow run: `43681726478`
- Artifact: `14147794801`
- Artifact digest: `sha256:b2e6818dbac4b09a78bc5bfc05e9ebef551225873d01020b2117466bcc09f14f`
- 4,834 records scanned; 1,494 Claims inventoried.
- `candidate_unassessed_risk_claims=0`; `selected_claims=0`; all 100 slots unfilled.
- 709 previously screened Claim IDs, 17 unreconciled holdouts, 15 reviewed-holdout overlap; 711 unique exclusions.
- The queue explicitly warns that absence of risk metadata is not a low-risk determination.

This closes the current 711-Claim risk-priority screening queue. It does not close M13, establish D/E/B ratings, or certify the underlying claims as publishable.

## 2. Generic Evidence Use coverage: current exact artifact

The Generic Evidence Use Report Coverage workflow completed on the same source revision:
- Workflow run: `43682137052`
- Artifact: `14149375133`
- Artifact digest: `sha256:135d22bf0fc59254ecd04f1624fbd239c3a8665134ab6417b9bad19a64f8abc6`

Artifact counts:
- 516 generic-EU candidates.
- 516 mapped to Claim IDs.
- 0 unmapped Evidence Use IDs.
- 0 ambiguous mappings.
- 516 candidates with any M13 report mention.
- 516 candidates with a source-review filename mention.
- 0 candidates without any report mention.

**Critical limitation:** the artifact's method is an exact Claim-ID text-mention scan, not semantic review verification. Its own limitations state:
1. A text mention does not prove the report reviewed the exact Claim version or full Claim→EU→Source chain.
2. A report may mention a Claim in a handoff, duplicate check or exclusion note rather than substantive passage review.
3. No report mention does not prove no review occurred outside scanned M13 Markdown files.
4. The tool does not fetch sources, assess passage support, assign D/E/B, modify canonical records or authorize remediation.
5. Every candidate requires human confirmation before it is counted as reviewed.

Therefore, `516/516 report mentions` is filename/text coverage only. It is **not** 516 semantic confirmations.

## 3. Reconcile the 516 vs 519 denominator

Earlier remediation records describe 519 generic Evidence Use records split into a 140 high-consequence subset and a 379 residual queue. The current coverage artifact maps 516 candidate Claim IDs/Evidence Use candidates. The three-record difference is not yet reconciled at exact Evidence Use ID level.

Do not silently treat 516 and 519 as interchangeable. Before any canonical bulk update, generate an exact EU-ID ledger showing:
- all 519 inventory EU IDs;
- the 516 mapped candidate rows;
- any additional/multiple EU records attached to the same Claim;
- which 140 EU/Claim entries belong to the high-consequence subset;
- which 379 belong to the residual queue;
- the exact disposition of the three-record difference.

The 140 + 379 arithmetic is internally consistent at the older register's denominator, but the current 516-candidate artifact is the latest machine-mapped coverage source. The discrepancy needs an explicit reconciliation.

## 4. Existing source-passage review coverage and no-duplicate rule

- The 140 high-consequence generic-EU subset has report-level source-passage coverage recorded as 140/140. Within that subset, the 49 residual cases were separately screened (23 moderate and 26 low); these 49 are not a new 49-Claim queue outside the 140.
- The 47 strict passage-locator Claims were desk-reviewed in Packages 01–06. The erratum establishes that a later Package 07 risk-screen report is not part of the strict-locator series. All 47 strict-locator cases remain `HOLD`; no canonical EU locator was added.
- The 47 strict-locator set overlaps the generic-EU candidate set; it is not an additional disjoint population.
- The residual generic-EU register contains 379 entries. A 20-Claim priority deep-review report exists; 359 remain in that register. All 20 priority Claims also appear in earlier Batch 44–50 source-passage report mentions. Treat the priority-20 report as a deeper second-pass review, not as a new disjoint population; do not repeat its source search.
- 16 of the 17 candidates that lacked the strict `SOURCE-PASSAGE-REVIEW` filename pattern already had topic-specific source-passage reassessment/adjudication reports (Archival Description, AI, Atmospheric Science, Biodiversity, Calculus, Cartography). They were not unreviewed merely because the filename pattern differed.
- The remaining `CLM-ANATOMY_BASICS-C` has now received a first dedicated source-passage reassessment in `M13-ANATOMY-BASICS-C-SOURCE-PASSAGE-REASSESSMENT-2026-11-15.md`. A rights-compatible Open RN CC BY 4.0 passage was identified; the Claim remains on HOLD pending authorized Source/EU versioning.
- This reconciliation is designed to prevent duplicate source searches. Existing reports must be reused as evidence inputs; only missing locators, source rights, provenance or unresolved support should be worked again.

## 5. Current state and next work

### Completed desk work
- Risk-priority queue: 711 unique Claims accounted for; no new candidate remains.
- Generic-EU filename coverage: 516/516 report mentions, but no semantic confirmation implied.
- Strict locator queue: 47/47 desk-reviewed; all 47 still HOLD.
- Residual generic-EU queue: 20 priority Claims received a deeper second-pass report; 359 remain in the register.
- Topic-specific reassessment files are reused rather than repeated.
- Anatomy C received its missing dedicated source-passage reassessment.

### Still open
1. Reconcile the 516-vs-519 generic-EU denominator at exact EU-ID level.
2. Convert the 47 strict-locator HOLD findings and the 20 priority deep-review findings into versioned Evidence Use/Source change proposals.
3. Build an exact, deduplicated canonical remediation ledger for the 359 residual generic-EU records, importing all prior passage findings and rights holds. Do not re-review source passages already covered unless the earlier report is incomplete or the source has changed.
4. Apply only rights-compatible sources and precise locators; ISO material remains on RIGHTS HOLD unless a qualifying permission/Open Data basis exists.
5. After authorized canonical changes, run Reference Tests, Offline Edition, Release Conformance Gate, and the relevant evidence-linkage/locator regressions.
6. Obtain independent specialist confirmation and complete Human View; reports and CI are not substitutes.

### Authorization boundary

No canonical Claim, Evidence Use, Source, Context, Scope, Relation or D/E/B value was modified by this reconciliation. The next phase requires versioned canonical Evidence Use/Source changes. Prepare proposals first; do not apply them without explicit authorization for that canonical-data phase.

## 6. Overall disposition

M13 remains **OPEN / NOT RELEASE-READY**. The risk-priority queue is exhausted, but generic Evidence Use remediation, denominator reconciliation, canonical locators, rights checks, semantic human confirmation and Human View remain incomplete. No PR is merged and `main` remains unchanged.
