# M13 execution reconciliation — evidence debt, duplicate scores and identifier integrity

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Base revision reviewed: `1fcaeb300fba77c349d764c852de360ae495a342`
Status: **execution checkpoint; desk review only; no canonical data or score changes; not a release decision.**

## 1. Reconcile the work queue before creating more batches

The successful M13 automation artifact for the base revision reports:
- 4,834 record files scanned; 1,494 Claims inventoried; 1,501 scored-report rows.
- 0 Claims without a historical scored-report match.
- 0 new Claims selected into the five automated scoring lanes.
- 1,143 structural finding rows: 1,137 medium and 6 high.

The empty scoring queue is expected: the pipeline excludes Claims that already have historical score-ledger matches. It does **not** certify those matches, the underlying evidence, or the current validity of D/E/B assessments. The automation explicitly assigned no scores and changed no canonical records. It is therefore incorrect to interpret the empty queue as M13 completion or as a reason to manufacture another scoring batch.

The evidence-linkage register identifies 519 generic Evidence Use candidates. Of these, the 140-Claim high-consequence subset has source-passage review coverage 140/140. The residual 379 are the arithmetic remainder (519 - 140), not 379 unscored Claims. Within the previously screened 49 residual cases, 39 were reported as directly supported at stated scope, 7 partial, and 3 not directly supported; that content screening did not itself add canonical locators. Accordingly:
- 519 is the original generic-EU structural candidate count;
- 140 is the high-consequence subset with source-passage report coverage;
- 379 is the residual generic-EU queue after that subset;
- locator remediation remains 0 in canonical records at the reviewed checkpoint;
- every candidate remains subject to record-level verification and authorization before canonical correction.

Do not collapse these populations into a single “remaining Claims” number.

## 2. Seven duplicate scored-report groups

The 2026-11-13 nuclear/water desk-review report covers all seven groups: three nuclear Claims, three water-treatment Claims, and one emergency-water-disinfection Claim. Its proposed dispositions are provisional only.

Key findings:
- Nuclear A/B/C remain HOLD because their current generic EU descriptions point to a broad IAEA topic page without Claim-specific pinpoints. Proposed D/B reconciliations must not be written into the ledger until an independent reviewer records a decision.
- Water-treatment A/B/C have separate WHO and EPA Evidence Use records linked to distinct Source IDs. This is a genuine structural two-institution chain, but neither chain currently contains exact passage locators. E3 is therefore not established by the existing canonical records; provisional E2 is the maximum desk-review recommendation pending passage-level confirmation.
- Emergency-water-disinfection D has identical D3/E3/B3 rows in two historical batches. The second row is a repeated historical review, not independent corroboration. Preserve both rows and record any later adjudication separately.
- No historical report row should be deleted or overwritten.

Required next step: independent adjudication against the current rubric, with reviewer, date, rubric version, evidence chain, rationale and decision recorded. Until then, all seven remain HOLD.

## 3. Identifier/path reconciliation

The static register reports six genuine filename/internal-ID mismatches in `web-systems-basics`:
- `CLM-A.json`, `CLM-B.json`, `CLM-C.json` contain IDs `CLM-WEB_SYSTEMS_BASICS-A/B/C`;
- `EU-A.json`, `EU-B.json`, `EU-C.json` contain IDs `EU-WEB_SYSTEMS_BASICS-A/B/C`.

Direct inspection confirms that all six JSON records have valid internal IDs and version 1 Claims / version 2 Evidence Uses; each EU points to its corresponding Claim and the shared Source. This is a filename-to-ID mismatch, not evidence of a broken Claim/EU reference chain. No canonical record IDs should be rewritten to match abbreviated filenames.

The 493 separator-only aliases are a separate normalization class and must remain comparison-only. The Batch 44 alias `CLM-POWER_ELECTRONICS_BASICS_B@1` still requires manual confirmation after separator normalization and version handling. Do not treat normalization as identity proof or silently rewrite stored IDs.

Safe remediation options, requiring a separately reviewed implementation, are:
1. add explicit path-to-record-ID alias coverage to inventory/reference tooling; or
2. rename the six files to full internal IDs only after checking every path-based consumer and adding regression tests.

No path or record is changed by this checkpoint.

## 4. Current-rubric score register

The current M13 locator rule requires a reproducible Claim-specific locator in the canonical Evidence Use record. The register reports 140 high-consequence generic-EU Claims, including 38 historical E=2/3 rows. Those historical scores remain historical; under the current locator rule, the current evidence state is provisional E1/HOLD until the locator and passage are verified.

Do not rewrite old batch reports or historical scores. A future adjudication ledger must distinguish:
- historical batch score;
- current-rubric desk-review recommendation;
- independently adjudicated current score;
- canonical evidence-chain state;
- publication/Human View decision.

## 5. Targeted remediation packages

Prioritize bounded packages in this order:
1. safety-critical source passages and locator repairs (water, emergency disinfection, electrical safety, wastewater, infrastructure, process safety, health);
2. the seven duplicate scored-report adjudications;
3. six filename/internal-ID mismatches and the single Batch 44 alias;
4. 48 sentence-like Source identity candidates, verifying actual title, issuer, edition/date and URI rather than auto-replacing metadata;
5. remaining generic-EU locator work by thematic slice, preserving the 379 residual count and recording partial/unsupported results distinctly.

Each package must identify exact Claim/EU/Source IDs and versions, source edition, passage locator, scope, support/contradiction, rights boundary, proposed patch, regression tests and reviewer state.

## 6. Parallel MVP boundary confirmed

The MVP checkpoint dated 2026-11-13 remains accurate at the reviewed PR heads:
- PRs #22, #24, #25, #26 and #27 are Draft and unmerged;
- the reader's successful build is synthetic-fixture-only;
- the two SI-unit Claims are the leading real-record candidate, but no exact-version real-record allowlist exists;
- the existing bounded SI authorization does not authorize an allowlist, deployment or publication;
- the three-reader non-specialist test remains NOT RUN;
- PR #27 is local-only JSON export, not a hosted editorial intake.

Continue MVP work on isolated Draft branches. Do not use the SI candidate in a preview until a separate bounded authorization exists, then build a private preview with exact IDs/versions and hashes, inspect the artifact, run the prepared reader protocol, and record rights/editorial decisions.

## 7. Acceptance and integrity

At this checkpoint:
- canonical Claim/Evidence Use/Source records changed: 0;
- canonical Evidence Use locators added: 0;
- historical D/E/B rows overwritten: 0;
- independent adjudications completed by this desk review: 0;
- real-record preview allowlists created: 0;
- PRs merged: 0.

This checkpoint is a controlled execution map. It does not close M13, certify any source, authorize canonical edits, or approve an MVP pilot.

## 8. Continuation addendum — source-review mention gap queue

A dedicated report was added at `RELEASE/M13-GENERIC-EU-SOURCE-REVIEW-MENTION-GAP-QUEUE-2026-11-13.md`.

The report-coverage artifact at source revision `3fefb3fcba27da3f722d2e60d0f373ccb49811ca9` identified 519 mapped generic-EU candidates; all 519 had some Claim-ID text mention, but only 479 had a source-review filename-hint mention. The remaining 40 were enumerated as a separate report-discovery queue with exact Claim/EU/Source IDs and slice names. This is not a finding that 40 received no substantive review: filename matching can produce both false positives and false negatives.

The coverage tool was extended to emit the exact list and count of candidates without source-review filename-hint mentions. It also quarantines conflicting EU-to-Claim worksheet mappings instead of silently selecting the last row. Regression tests cover both conditions. The report itself preserves the earlier artifact revision and its limitations; the updated workflow must be used for the next current-head count.

No new 100-Claim scoring batch was created. The existing scoring automation still selects zero Claims because all 1,494 have historical score-ledger matches; those matches are not certifications. The next substantive work remains record-level passage verification and controlled locator remediation, not another inventory sweep.

## 9. MVP reader integrity enhancement

The private-preview builder now records a SHA-256 hash for every selected input record in `selected_record_hashes`, in addition to the existing rendered HTML and search-script hashes. The hash is computed from canonical JSON serialization of the complete selected record. Regression coverage checks deterministic hashes and confirms that a changed selected record changes its hash.

This improves exact-input traceability for a future private preview. It does not create a real-record allowlist, authorize SI-unit records, establish rights clearance, or approve deployment. The reader remains synthetic-fixture-only until the separate bounded real-record preview authorization and remaining human/editorial gates are completed.

## 10. Corrected passage-report classifier and explicit risk-screening queue

The initial 40-item gap report is superseded. Its filename classifier treated `GENERIC-EU` remediation registers and `SOURCE-IDENTITY` reviews as passage-review evidence. That was too broad and produced false positives.

The corrected classifier uses only `SOURCE-PASSAGE`, `SOURCE-PINPOINT`, `EVIDENCE-LOCATOR` and `SOURCE-FIT` filename signals. Its successful artifact at `e5a0790b918bb895ed6cc2c03e901b1356ee9b34` reports:
- 519 generic-EU candidates, all mapped to Claims;
- 519 with some report text mention;
- 469 with a passage/pinpoint/locator/source-fit filename signal;
- 50 without such a filename signal.

The 50 are listed in `RELEASE/M13-STRICT-PASSAGE-LOCATOR-REPORT-MENTION-GAP-QUEUE-2026-11-13.md`. The list is a manual routing queue only. Neither the 469 filename signals nor the 50 missing signals establish substantive review status.

The audit-queue automation now also emits all **711 Claims without recorded risk metadata** as explicit `UNASSESSED` records, including exact Claim path, version, linked Evidence Use IDs and Source IDs. The successful artifact at source revision `43e799d329cfdce41221b92855fafb6b90cfb5db` confirms:
- 1,494 Claims inventoried;
- 1,501 historical scored-report rows;
- 0 Claims without a historical scored-report match;
- 1,143 structural finding rows (1,137 medium; 6 high);
- 783 Claims with at least one risk signal;
- 591 with a high-consequence screen;
- 711 with no recorded risk signal and therefore UNASSESSED;
- 0 new scoring-queue selections, because historical score matches exclude every Claim.

The 711-record list is a separate screening queue, not 711 low-risk Claims and not 711 unscored Claims. A CSV export is being added to the workflow artifact so the queue can be reviewed operationally. No automated D/E/B scores or canonical edits are made.
