# M13 — consolidated Batch 42–43 checkpoint: report bodies and current graph

Date: 2026-11-21  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Checkpoint commit before this addendum: `d7b4b8766439167ae3ec5d6d94e1c853197cb1e7`.

## Completed

1. Individually inspected all Batch 42 and Batch 43 scored-row report bodies: **200/200**.
2. Reconciled current canonical primary Claim/Evidence Use/Source chains for Batch 42 rows 069–100: **32/32 exact ID/version matches**.
3. Reconciled current canonical primary Claim/Evidence Use/Source chains for Batch 43 rows 001–100: **100/100 exact ID/version matches**.
4. Combined graph comparison: **132/200 report-row occurrences verified**; **68 Batch 42 rows (001–068) remain for current canonical graph comparison**.
5. Preserved all secondary EU/source edges identified in the reviewed records; did not flatten multi-source cases.
6. No canonical records, current assessment scores, worksheet statuses, risk records or queue states were modified.

## Evidence boundary

Exact ID/version graph match does not prove passage support. The 132 matched rows remain historical-chain/canonical-graph reconciliation only. In this pass one current EU with an explicit reproducible section-and-paragraph locator was verified: Batch 43 row 098, hydrology Claim/EU/Source @2. Current accepted D/E/B remains zero for this graph-reconciliation work.

The Batch 43 historical D/E/B distribution remains D1=5/D2=29/D3=66; E1=26/E2=67/E3=7; B1=6/B2=61/B3=33. No historical scores were transferred.

## Remaining work

- Complete current graph reconciliation for Batch 42 rows 001–068.
- Rerun the master normalized-ID/version join across all 200 report files; distinguish report-row occurrences from unique normalized Claim IDs and adjudicate duplicate groups without automatic score selection.
- Investigate Batch 43 row 012 WHO Source URI/version-history concern and verify all secondary evidence links at passage level.
- Reconcile generic-EU 496/356 cohort only after the canonical join.
- Continue source-passage, evidence-diversity, risk, specialist, independent Human View, rights/editorial and release gates.

## CI and repository protection

At the checkpoint SHA `d7b4b8766439167ae3ec5d6d94e1c853197cb1e7`, six GitHub Actions runs were observed: Offline Edition (PR and push), Release Conformance Gate, Reference implementation tests, M13 Audit Queue Automation and M13 Generic Evidence Use Report Coverage. They were pending or in progress when checked; no PASS is claimed.

PR #21 was reverified Open / Draft / Unmerged with head `d7b4b8766439167ae3ec5d6d94e1c853197cb1e7`. The branch ref matched that SHA. `main` remained `d58289f319993ede5294a46f4741a506fd2fd710`.

No canonical Claim, Evidence Use, Source, Assessment, Relation or risk record changed. No historical score accepted. No queue exclusions or risk classifications changed. PR #21 remains Draft and unmerged; `main` remains untouched.
