# Continuation Checkpoint — M13 and MVP — 2026-10-12

## Verified exact-head technical state

Repository: `kvantovoebessmertie/encyclopedia-of-civilization`

- M13 PR #21 head: `a8f8fbd1e676e7d2af5ec0592a6648e3ccef1112`. The three required workflows returned completed/successful for this exact SHA: Reference implementation tests, Offline Edition, and Release Conformance Gate.
- MVP PR #22 head: `aa14bea8448cbf96b8162cc2bf8e2fa7974d8755`. All three required workflows returned completed/successful for this exact SHA.
- PR #24 head: `b0c0522098ef0d7f4613269d921c2f789e9a0a99`; PR #25 head: `91fc6e4d5872735edc460f58b8a4d4518924b07d`; PR #26 head: `40fe3de52dd044b1445f9429eac0c6846a6c6771`; PR #27 head: `0b56e81b301843e83c3ac6e1944c5dab7c0b7c8b`. Each of these exact SHAs also returned completed/successful results for Reference implementation tests, Offline Edition, and Release Conformance Gate.
- These results establish technical conformance for those exact commits only. They do not establish substantive content correctness, independent review, legal/rights clearance, usability, or publication readiness.
- PRs #21, #22, and #24–#27 are open Drafts and unmerged at this checkpoint. No canonical content records or `main` were changed by this checkpoint.

## M13 substantive status

- The denominator remains 1,494 Claim records.
- Batch 14 reviews inventory rows 651–750 (100 Claims) at Claim / Evidence Use / Source metadata level. It assigned no D/E/B scores and changed no canonical JSON.
- Batch 14 reports 82/100 Claims with at least one generic or near-generic Evidence Use description, 75/100 whose descriptions are all generic/near-generic, and 37/100 with one or more automated flags. These are overlapping triage signals, not verdicts about truth or support.
- The Batch 14 remediation checkpoint confirms the hydrology Source identity and three Evidence Use v2 links are already corrected in the reviewed tree; targeted verification should be recorded before marking that stale finding resolved.
- Human-computer interaction remains HOLD: the current Source identity is sentence-like and the URI is a broad/redirecting NIST locator. A topical NIST candidate is not sufficient without versioned Source/Evidence Use changes and claim-specific pinpoints.
- Immunology remains HOLD: the current three Claims are editorial/methodological rather than substantive immunology claims. Do not patch the URL alone; first decide whether to replace the Claims with sourced domain claims or relocate the editorial material.
- A source-count reconciliation remains open. `RELEASE/CONTENT-COVERAGE.json` currently reports 619 Source records. The source-identity triage dated 2026-10-11 reports 617 distinct Source IDs referenced by an older Claim worksheet reviewed at revision `4453783e9dc2db55c4936a8acd85cbc666c46f86`. These are not a like-for-like current snapshot; the difference must be reconciled from the current tree and current references before interpreting it as orphaned or missing Sources.

## Next controlled actions

1. Rebuild a current-head inventory-to-ledger join for all 1,494 Claims; distinguish final D/E/B scores, provisional reviews, metadata-only triage, duplicate/alias candidates, and untouched Claims.
2. Reconcile current Source record count against the distinct Source IDs referenced by current Claim/Evidence Use records; enumerate the exact unmatched records and confirm scope/version semantics.
3. Run targeted regression/linkage verification for the hydrology v2 correction; record the result before closing its stale Batch 14 finding.
4. Prepare a bounded HCI remediation only after inspecting each Claim and its Evidence Use; keep unsupported Claims on HOLD.
5. Resolve immunology Claim-type disposition before considering any source/URL correction.
6. Continue with the next non-overlapping 100-Claim batch only after excluding previously scored, duplicated, and already triaged IDs. For each candidate, verify the exact source passage, claim scope/limitations, and evidence independence before final D/E/B scoring.
7. For MVP, review PR #24 and PR #25 together as the renderer/security boundary; keep the legacy full-corpus renderer distinct from the curated allowlisted preview. Review PR #26 and #27 together as a local-only JSON contract/form flow. Do not enable real-record allowlisting, hosted intake, or public deployment until rights, attribution, editorial ownership, Human View, privacy/retention, abuse controls, and security gates are explicitly satisfied.

## Release boundary

Green CI is not a content-audit closure. Keep every Draft PR open/unmerged, keep `main` unchanged, do not add canonical records as part of metadata triage, and do not enable publication or real submission intake from this checkpoint.


## Acceleration checkpoint — 2026-10-12, verified continuation

This addendum supersedes earlier stale status lines above where they name an older M13 head or imply that the next step is to begin another metadata-triage batch.

### Exact-head technical state before this checkpoint commit

- M13 PR #21 head: `849888c585b1403789ccaf3f8dc72bfbcab53bcf`; Reference implementation tests, Offline Edition, and Release Conformance Gate all completed successfully on this exact SHA.
- MVP PR #22 head `aa14bea8448cbf96b8162cc2bf8e2fa7974d8755`, PR #25 head `91fc6e4d5872735edc460f58b8a4d4518924b07d`, and PR #27 head `0b56e81b301843e83c3ac6e1944c5dab7c0b7c8b` each have all three required workflows completed successfully on their exact recorded heads.
- All PRs remain Draft/unmerged. No merge, deployment, or change to `main` is authorized by these results.

### Newly reconciled first-pass work

The branch contains Batch 15 through Batch 21 reports, in addition to Batch 14:

| Batch | Selected unique Claims | Scope |
|---|---:|---|
| 14 | 100 | Inventory rows 651–750 |
| 15 | 100 | Rows 751–859, excluding 9 already-scored IDs |
| 16 | 100 | Rows 860–962, excluding 3 already-scored IDs |
| 17 | 100 | Rows 963–1062 |
| 18 | 100 | Rows 1063–1166, excluding 4 already-scored IDs |
| 19 | 100 | Rows 1167–1276, excluding 10 already-scored IDs |
| 20 | 100 | Rows 1277–1383, excluding 7 already-scored IDs |
| 21 | 96 | Rows 1384–1494, excluding 15 already-scored IDs |

- Batches 15–21 account for 696 unique Claims at metadata/source-fit triage level; combined with Batch 14, 796 selected Claims have triage reports across inventory rows 651–1494.
- This is **not** 796 finalized D/E/B assessments. These reports explicitly do not score or clear Claims. Report-specific worksheet source revisions differ and must be reconciled to the current corpus before substantive scoring or remediation.
- The final inventory span has been covered; do not create another 100-Claim metadata-triage batch merely to repeat the same first pass.

### Faster next sequence

1. Regenerate the current-head machine inventory, scored-report ledger, linkage findings, and triage-report coverage; reconcile them by literal ID and exact path, using separator normalization only to flag possible aliases.
2. Produce one deduplicated action queue that distinguishes: final score absent; provisional-only; metadata-triaged but not passage-verified; source/linkage defect; high-consequence review; semantic-duplicate/alias review; and already cleared.
3. Prioritize high-consequence and broken-linkage cases first. For the remaining unscored queue, perform claim-specific passage verification and D/E/B review in batches of 100 without repeating inventory discovery.
4. Close a finding only after checking the current record versions and exact source passages. Do not use metadata heuristics or plausible source identity as a substitute for evidence.
5. Keep MVP moving separately: prepare a small real-record candidate list for rights/source/editorial review; keep the public allowlist empty of unapproved records; review renderer/security and local JSON intake as separate flows. No hosted intake or public deployment until the required gates are satisfied.

### Recorded score baseline — interpret narrowly

The latest committed inventory-to-ledger join reports 1,494 Claim records, 259 historical score rows, 252 normalized Claim IDs represented, 7 repeated report-ID groups, and 1,242 Claims with no score row in that snapshot. These are ledger accounting values, not proof that 252 Claims have passed the full M13 evidence, duplicate, high-consequence, Human View, and independent-review gates. Rebuild the join from the current head before using these counts as a new baseline.

### Safety and governance

No canonical record edit, score, publication approval, or change to `main` is implied by this checkpoint. Because this commit changes the M13 branch, all required workflows must again pass on its new exact head before further branch commits.
