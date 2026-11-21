# MVP supporting PR integration-equivalence audit

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Integration target inspected: PR #22, branch `mvp-public-contribution-design-2026-10-11`  
Inspected PR #22 HEAD: `8de901ec54e18da0853e5359592ba3ec86ae335d`

## Purpose

Verify whether the implementation work represented by supporting MVP PRs #24–#27 is actually present in the current PR #22 branch, rather than assuming that references in the PR description imply integration.

## Exact blob-equivalence checks

The following files were fetched independently at the supporting PR head and PR #22 HEAD. Their Git blob SHAs were identical in every comparison:

| Supporting PR | File | Blob SHA | Result |
|---|---|---|---|
| #24 | `REFERENCE/src/encyclopedia_reference/offline_edition.py` | `5979a55f71d14b41fe98177c2ac9e6982c4b65fa` | IDENTICAL |
| #24 | `REFERENCE/tests/test_offline_edition.py` | `e92d7e8a28ac9f6d1be493e13db7483bee14e098` | IDENTICAL |
| #26 | `CONTRIBUTIONS/INTAKE-CONTRACT-V1.md` | `692f0984c981ec3c29ff8c4183f6f38cc3e77921` | IDENTICAL |
| #26 | `CONTRIBUTIONS/contribution-submission-v1.schema.json` | `83700b21047e1e1571f07a4582706cecf1a49d6f` | IDENTICAL |
| #26 | `REFERENCE/tests/test_contribution_submission_schema.py` | `1343ef8b782a1f57e0aa3d8fde77034c057b2d3d` | IDENTICAL |
| #27 | `CONTRIBUTIONS/intake-form-prototype.html` | `375e8b555b675c6d158b06f25069f2f7c5614371` | IDENTICAL |
| #27 | `CONTRIBUTIONS/intake-form.js` | `15dd35bf3fce30b975c34cfd7db6dfa95ca670ec` | IDENTICAL |
| #27 | `REFERENCE/tests/browser_inspect_contribution_form.cjs` | `6a8c3680ef6745f5ed3604ed7be7aadc3143e268` | IDENTICAL |

This establishes exact file-content equivalence for the checked implementation surfaces; it does not claim that every file or commit in each supporting PR is identical or that those PRs have been merged into `main`.

## PR topology at inspection

| PR | State | Base | Head | Interpretation |
|---|---|---|---|---|
| #22 | OPEN / DRAFT / NOT MERGED | `main` | `8de901e` | Current integration branch |
| #24 | OPEN / DRAFT / NOT MERGED | `main` | `b0c0522` | Supporting offline HTML-escaping PR; checked files already identical in #22 |
| #25 | CLOSED / MERGED | PR #22 branch | `4b7208a` | Reader prototype merged into the PR #22 branch, not into `main` |
| #26 | OPEN / DRAFT / NOT MERGED | `main` | `6c5c3d4` | Supporting intake-contract PR; checked files already identical in #22 |
| #27 | OPEN / DRAFT / NOT MERGED | PR #26 branch | `f923edd` | Supporting local-form PR; checked files already identical in #22 |

No supporting PR was closed, retargeted, marked ready, or merged during this audit.

## CI evidence

At the inspected supporting heads, the available GitHub Actions runs were completed successfully:

- PR #24 head `b0c0522`: Offline Edition, Release Conformance Gate, Reference implementation tests — all SUCCESS.
- PR #26 head `6c5c3d4`: Release Conformance Gate, Reference implementation tests, Offline Edition — all SUCCESS.
- PR #27 head `f923edd`: Reference implementation tests, Offline Edition, MVP Contribution Form Browser Tests, Release Conformance Gate — all SUCCESS.

These are historical head-specific runs, not substitutes for validation of the integrated branch.

At PR #22 HEAD `8de901ec54e18da0853e5359592ba3ec86ae335d`, all four required workflows completed successfully on that same immutable commit:

- Offline Edition — SUCCESS (run 44729737966)
- MVP Contribution Form Browser Tests — SUCCESS (run 44729738199)
- Reference implementation tests — SUCCESS (run 44729737970)
- Release Conformance Gate — SUCCESS (run 44729738088)

## Disposition and boundaries

1. The checked supporting implementation surfaces from #24, #26 and #27 are present byte-for-byte in PR #22.
2. PR #25's reader prototype was merged into the PR #22 branch; this does not mean #25 or #22 was merged into `main`.
3. PR #22's exact-head 4/4 PASS validates the integrated branch snapshot at the stated SHA.
4. Keep PR #22 Draft and keep `main` unchanged. Do not merge, close, retarget, or mark any supporting PR ready without an explicit owner decision.
5. Technical CI does not approve public intake, content inclusion, rights clearance, deployment, or release. The local form remains local-only; no hosted endpoint or public intake is authorized.
6. No canonical content, allowlist, publication state, or release disposition was changed by this audit.

## Next WP3 action

Maintain the PR #22 integration branch as the current technical integration candidate. Before any merge/release decision, perform a final integrated artifact inspection against the frozen, explicitly approved record allowlist and the unresolved WP2 rights/editorial decisions. Re-run all required checks on the final immutable candidate HEAD after any further changes.
