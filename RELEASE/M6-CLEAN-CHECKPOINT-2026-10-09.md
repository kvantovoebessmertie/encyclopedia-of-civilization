# M6 CLEAN Checkpoint Candidate — 2026-10-09

## Status at authoring
**CANDIDATE — awaiting exact-checkpoint-HEAD CI and independent verification. Do not mark CLEAN yet.**

This file is deliberately a checkpoint candidate. Its commit must pass all three required workflows on its exact HEAD. If any check fails, M6 remains OPEN and only a confirmed defect may be corrected; then all three checks must run again on the resulting exact HEAD.

## Protected baseline and scope
- Working branch: `m6-gap-map-2026-10-09`.
- PR: [#11 — M6 validation-only: controlled correction pass](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/11). Keep open, draft, and unmerged during this validation process.
- Base branch: `m6-validation-base-2026-10-09`, protected M5 checkpoint `c911c6b4ad791cb933293608e298e318a608a02f`.
- Protected `main` HEAD observed during independent verification: `203a7028e08da394fd44630fe38727be07bc8849`. Do not alter `main`, M4, or M5.
- M6 is restricted to six existing slices: `sleep-basics`, `learning-basics`, `law-basics`, `demography-basics`, `governance-basics`, and `education-systems`. No new slice, Record type, or speculative Relation was introduced.

## Content and audit disposition
- Substantive findings M6-SUB-01..04: corrections re-read; claims narrowed to reviewed source support.
- Evidence findings M6-EV-01..07: descriptions made claim-specific; independent CDC, World Bank WGI, OECD Education at a Glance, and UN WPP methodology evidence added where warranted.
- Human View findings M6-HV-01..03: mixed-language sentence corrected, established bilingual convention preserved, all six Scope records made domain-specific and regressions updated.
- Relation audit: all 64 Relation records checked for M6 targets, broken endpoints, and duplicate unordered participant pairs; none confirmed.
- Process finding M6-PROC-01: initial preflight failure and subsequent authorization-manifest correction remain preserved in the audit trail; validation guard was not weakened. Close this finding only after checkpoint-head preflight and exact-head CI are confirmed.
- Unified Debt Map and Post-Correction Audit are synchronized with the verified documentation-finalized HEAD. The coverage manifest reflects the current corpus and keeps this checkpoint-head revalidation as the sole M6-specific remaining gate.

## Independently checked corpus snapshot
On documentation-finalized HEAD `aebef62de87407dbdcdbf988461242cd09ee3098`, the untruncated recursive Git tree contained 7,076 entries, 4,763 record JSON files, and 479 slices. The coverage manifest matched 4,763 records, 479 slices, 19 Record types, 605 Sources, 1,639 Evidence Use, and 64 Relations. The six locked M6 slices and README registry were previously cross-checked against the tree.

## Prior exact-head evidence (not evidence for this checkpoint commit)
Documentation-finalized HEAD `aebef62de87407dbdcdbf988461242cd09ee3098` passed:
- Reference implementation tests: [run 37899900359](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37899900359) — PASS.
- Release Conformance Gate: [run 37899900362](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37899900362) — PASS.
- Offline Edition: [run 37899895530](https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/actions/runs/37899895530) — PASS.

Those runs do not validate this checkpoint candidate commit.

## Acceptance rule
Run and independently verify all three workflows on the exact commit containing this checkpoint file:
1. Reference implementation tests.
2. Release Conformance Gate.
3. Offline Edition.

Every workflow must complete successfully on the same HEAD, and each Content preflight must pass. Independently recheck the final branch/PR head, protected base, unchanged `main`, corpus counts, manifest agreement, and audit sign-offs.

- If all gates pass: accept M6 as **CLEAN** and record the final result in the PR conversation/user status without adding a documentation-only commit.
- If any gate fails: M6 remains OPEN; inspect the failed job, fix only the confirmed defect without weakening validation, reconcile the audit records, and rerun all three workflows on the resulting exact HEAD.
- This checkpoint does not authorize merging PR #11 or promoting content to `main`.
