# PR #22 — Exact-Head CI and Historical Checkpoint Reconciliation

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR: https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22

## Current branch snapshot

The PR head was re-fetched before this report was written.

- PR #22: OPEN / DRAFT / NOT MERGED.
- Base: `main`.
- Exact PR head: `940dc2fbe84ad43ab1602591caee1dc8e1d2ba1f`.
- Main head observed: `d58289f319993ede5294a46f4741a506fd2fd710`.
- Main was not modified, rebased, or merged.

## Exact-head checks

GitHub's commit check-runs endpoint was queried for the exact SHA above. All six returned check runs are completed successfully:

| Check | Run | Result |
|---|---:|---|
| Reference implementation tests | 45162967962 | PASS |
| Reference implementation tests | 45162978788 | PASS |
| Release Conformance Gate | 45162978781 | PASS |
| Offline Edition / build-and-test | 45162978697 | PASS |
| Browser form tests | 45162978797 | PASS |
| Offline Edition / build-and-test | 45162967903 | PASS |

The two Reference and two build runs are separate GitHub check-run instances. Every returned check run on this exact commit has `status=completed` and `conclusion=success`.

**Interpretation:** the current PR head is technically green for the checks returned by GitHub. This is not an editorial approval, rights clearance, production deployment, public-release approval, or authorization to merge. The selection-aware builder still has no production INCLUDE manifest.

## Historical checkpoint evidence recovered

The following historical checkpoint commits were checked directly; each has three successful required jobs (Reference, Release Gate, Offline/build), 12 successful jobs total:

| Work package | Exact checkpoint | Result | Qualification |
|---|---|---:|---|
| P1 correction baseline | `b83a37df4d44c151cda8e4d74e370390902dcc44` | 3/3 PASS | Original P1 clean SHA `2974a8e9d4c69c6f8bf922ba7b405d6afe55de4b` is unavailable; this is the verified correction baseline, not the original clean checkpoint. |
| P2 clean checkpoint | `3e2971a87119d746c277c6607875a56673dfe764` | 3/3 PASS | Exact historical SHA. |
| P3 clean checkpoint | `d8600b53c225fefb7c1beae924a85556ceb1d4d6` | 3/3 PASS | Exact historical SHA. |
| P5 clean checkpoint | `b0da033bc3e566c5a2259598e660c4abcfef63fc` | 3/3 PASS | Exact historical SHA. |

Unavailable historical SHAs (not counted as passes):
- P1 original clean checkpoint: `2974a8e9d4c69c6f8bf922ba7b405d6afe55de4b`.
- P2 correction checkpoint: `b7ccf467a3a1452c020be9b5dc414b2d4f702a79`.
- M3 clean checkpoint: `bb3a348afc4ff3470ae16c5f90421a0796bc5403`.

## Release state unchanged

- Part I record screening remains complete at 980/980, but the 112-record early manifest remains 0 INCLUDE / 112 HOLD; the other 868 screened records are not thereby approved.
- Part II master remains 1,146 exact-version rows (1,058 candidate keys + 88 dependencies), with all entries HOLD; represented-slice coverage remains 124/385.
- No exact-version production allowlist exists.
- Rights/editorial owner decisions R-01–R-10 remain OPEN.
- The production reader/release artifact, item-level rights clearance, qualified review for any high-consequence material, independent Human View, artifact inspection and explicit owner release approval remain outstanding.

## Next execution order

1. Keep the current PR #22 branch technically green; any subsequent commit requires exact-head revalidation.
2. Use the consolidated owner decision packet in `FIRST-EDITION-OWNER-DECISION-PACKET-R01-R10-2026-11-23.md` to close the non-delegable R-01–R-10 decisions.
3. In parallel, continue private release-candidate engineering and bounded exact-version screening; do not create an INCLUDE manifest by converting HOLD rows.
4. Once owner decisions and item-level gates exist, select the smallest coherent, low-risk cross-domain set and build the real production reader/offline artifact from the exact allowlist.
5. Do not merge PR #22 or change `main` without explicit owner authorization.

## Scope of this report

This report records check evidence and release-state reconciliation only. It does not change canonical records, candidate membership, record dispositions, rights, publication status, allowlist, release state, PR state or `main`.
