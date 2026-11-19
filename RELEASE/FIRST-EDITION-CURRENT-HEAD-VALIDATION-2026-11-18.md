# First Edition — Current-Head Validation Evidence

Date: 2026-11-18  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Validated PR: #22 (open, Draft, not merged)  
Exact validated HEAD: `722f79a9940acdc0170077a2c63a4419759d8358`

## Result

All four PR-triggered GitHub Actions workflows observed for this exact HEAD completed successfully:

| Gate | Run ID | Result | Evidence |
|---|---:|---|---|
| Release Conformance Gate | 44364249473 | PASS | Job `release-gate`; report artifact uploaded |
| Reference implementation tests | 44364249432 | PASS | `1003 passed in 427.51s` |
| Offline Edition | 44364249526 | PASS | identity validation, offline tests, full build, manifest verification and artifact upload |
| MVP Contribution Form Browser Tests | 44364249542 | PASS | real-browser form, payload-schema and mobile checks; evidence artifact uploaded |

All four workflow run records identify the same exact HEAD above. All jobs and their listed steps completed with conclusion `success`.

## Content preflight

The Release Conformance Gate log reports:

- 4,674 records;
- 479 vertical slices;
- 4,674 unique record identities;
- 19 record types.

The release-gate log reports an empty `blocking_or_limiting_gates` list and successfully uploads `RELEASE/release-gate-report.json` as artifact `release-gate-report`.

## Retained build and test artifacts

| Artifact | Artifact ID | Size | Created (UTC) | Expiry (UTC) |
|---|---:|---:|---|---|
| `release-gate-report` | 14456935539 | 1,520 bytes | 2026-11-18 18:04:58 | 2027-02-16 17:56:47 |
| `encyclopedia-offline-edition` | 14456023347 | 1,135,433 bytes | 2026-11-18 17:57:22 | 2027-02-16 17:56:47 |
| `mvp-contribution-form-browser-e591bbd8118f69dc6b40153b4d24805f25f9f012` | 14456592831 | 237,297 bytes | 2026-11-18 17:57:27 | 2026-12-02 17:57:26 |

The offline edition artifact was produced by the workflow associated with the exact validated HEAD. Its SHA-256 recorded by the workflow artifact inspection is `32e56177b982bf5ac5d7f8f876c740012f21a4ac7f60844c3795e4b99dd5a2fb`.

## What this evidence establishes

1. The current PR #22 snapshot passes the repository's Reference tests, Release Conformance Gate, Offline Edition build/manifest checks and MVP contribution-form browser checks.
2. The repository-wide content preflight is green for the inventory counts above.
3. A reproducible offline-edition build and release-gate report are retained as GitHub Actions artifacts.

## What this evidence does not establish

1. CI success is not editorial approval and does not automatically assign `INCLUDE` to any Claim.
2. It does not close per-record source pinpoint, rights, attribution, qualified high-consequence review or reader-facing Human View requirements where those remain open.
3. It does not retroactively prove that historical P1/P2/M3 checkpoint commits passed their own exact-commit workflows. Those historical checkpoints remain accurately described by their own reports; this current-head run is new validation evidence for the current PR snapshot, not a rewrite of their history.
4. It does not authorize publication, licensing, hosting, merge, or changes to `main`.

## Release-register consequence

The first-edition candidate register may now cite this current-HEAD technical validation as evidence that the current repository snapshot passes the four named technical workflows. Do not remove any remaining HOLD solely on this basis. Record-level decisions still require the exact candidate's own evidence/dependency closure and all applicable editorial, rights and safety gates.

## Change control

No canonical Claim, Evidence Use, Source, Context, Scope, Assessment, Inference, Decision or Relation record was changed as part of this validation note. PR #22 remains Draft and unmerged; `main` was not changed.


## Subsequent exact-HEAD validation — 2026-11-18

A later commit on the same PR branch was checked independently after the validation snapshot above.

- Exact HEAD: `27708a6bb55d70894e22c9338e65cb8c69d899a8`
- PR #22 remains open, Draft and unmerged.
- All four PR-triggered workflows for this exact HEAD completed with `success`:
  - Release Conformance Gate — run `44372533549`
  - Reference implementation tests — run `44372533473`
  - Offline Edition — run `44372533725`
  - MVP Contribution Form Browser Tests — run `44372533516`

This later exact-head result supersedes the earlier HEAD as the latest technical validation point. It does not retroactively validate historical P1/P2/M3 checkpoint commits, does not assign any record INCLUDE, and does not close rights, source-pinpoint, editorial, Human View or qualified-review requirements.

No canonical content records were changed by this validation update. `main` remains untouched; no merge or publication is authorized.


## Subsequent exact-HEAD validation — 2026-11-19

Exact PR #22 HEAD: `d2195c6b1425f15997a033769b033372c66cb1d7`.

PR state at validation: open, Draft, unmerged; base `main` remained at `91ebdb1993e8c4ad38ac56ddc8be329ac7d77cc9`.

All four PR-triggered workflows for this exact HEAD completed successfully:

| Gate | Run ID | Result |
|---|---:|---|
| Reference implementation tests | 44502715208 | PASS |
| Offline Edition | 44502715187 | PASS |
| MVP Contribution Form Browser Tests | 44502715210 | PASS |
| Release Conformance Gate | 44502715387 | PASS |

The Release Conformance Gate report was downloaded and inspected, not inferred from the workflow conclusion alone.

- Release-gate job: `135490516118`; all steps completed successfully, including Content preflight, Run release gate and artifact upload.
- Report artifact: `release-gate-report`, artifact ID `14517549760`, ZIP size 1,519 bytes, SHA-256 `913beaa3bd2a467d462da3cf28e73dfc239531a0b2ac4d1db834932a301e8fb7`.
- Report generated: `2026-11-19T10:19:44.502937+00:00`.
- Gate registry: 18 gates, all PASS; final state `CONFORMING`; `blocking_or_limiting_gates=[]`.
- Semantic conformance: 1,191/1,191 declared Reference Implementation mappings.
- Corpus preflight: 4,674 records, 479 slices, 4,674 unique identities, 19 record types.
- Reference test suite: `1003 passed in 240.18s`.

The Offline Edition artifact was also downloaded and inspected:

- Artifact ID `14518046658`; ZIP size 1,135,433 bytes; ZIP SHA-256 `19fc44e496fd53b51f2f3efec97933b3ad234d962f594663d87d17b2ecdffff5`.
- Manifest: edition ID `encyclopedia-offline`, version `1.0`, 4,674 records, `network_required=false`.
- All five manifest file hashes independently matched the downloaded files: README, HTML, JSON, JSONL and SQLite.
- JSON, JSONL and SQLite each contain the full 4,674-record corpus; no duplicate ID/version identities were found.

### Critical interpretation boundary

This Offline Edition artifact is a **full-corpus technical package, not the curated first edition**. The first-edition Part I inventory records 94/94 slices and 980/980 JSON files screened, with every candidate still HOLD and zero public INCLUDE decisions. The corpus artifact must therefore remain an internal build/test artifact and must not be represented or distributed as the approved first edition. Canonical `publication_status` and a green release-conformance gate do not override the record-level HOLD decisions or create edition membership.

The first-edition release builder must continue to render only an exact, separately approved version-pinned allowlist. The current full-corpus Offline Edition workflow does not itself establish that allowlist.

No canonical content record, candidate decision, allowlist, owner decision, or `main` branch was changed by this validation. PR #22 remains Draft and unmerged.
