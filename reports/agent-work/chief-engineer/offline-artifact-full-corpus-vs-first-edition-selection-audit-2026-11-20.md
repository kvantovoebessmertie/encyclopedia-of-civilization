# Offline Artifact — Full-Corpus Build vs First-Edition Selection Audit

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Artifact-producing PR #22 HEAD: `6c33b415ffa1877e62fda83af20136a5a31046c0`  
Artifact workflow: Offline Edition, run `44731511140`  
Artifact: `encyclopedia-offline-edition`, artifact ID `14625628883`  
Downloaded archive SHA-256: `f46929d38f97d86233ea949879e39b466b782ad03bd007c06cbe506c61a673b7`  
Disposition: **CI ARTIFACT VERIFIED AS FULL-CORPUS DIAGNOSTIC; NOT A FIRST-EDITION RELEASE CANDIDATE**

## 1. Why this audit was performed

The Offline Edition workflow passed at exact HEAD `6c33b415ffa1877e62fda83af20136a5a31046c0`. The first-edition plan, however, requires a frozen, exact-version, owner-approved selection and must not publish the full canonical corpus by default. The successful workflow artifact was therefore downloaded and inspected rather than treating CI PASS as sufficient evidence of publication readiness.

## 2. Artifact integrity and contents

The downloaded ZIP contains exactly six files:

- `README.md`
- `edition-manifest.json`
- `index.html`
- `records.json`
- `records.jsonl`
- `records.sqlite3`

Manifest values:
- `edition_id`: `encyclopedia-offline`
- `edition_version`: `1.0`
- `record_count`: 4,742
- `network_required`: false
- canonical source: `records.json`
- durable formats: JSON, JSONL, SQLite

The manifest's SHA-256 hashes were independently recomputed for all five listed output files and matched exactly. The ZIP archive SHA-256 is recorded above.

Cross-format inspection:
- `records.json`: 4,742 records;
- `records.jsonl`: 4,742 records;
- SQLite: 4,742 rows;
- 4,742 unique (record_id, record_version) keys;
- JSON, JSONL and SQLite payloads were equal after parsing and keying by exact record identity/version;
- no duplicate identity/version keys were found.

HTML structure was parsed with Python's standard-library `html.parser`:
- 4,742 article elements;
- zero script, img, svg, iframe, object or embed elements;
- zero event-handler attributes;
- static style/title/meta and expected record text elements only.

The artifact README explicitly identifies `records.json` as canonical and derived views as non-normative. The artifact is self-contained and declares no network requirement.

## 3. Critical finding — the artifact contains the full canonical corpus

The workflow file `.github/workflows/offline-edition.yml` explicitly runs:

```sh
python REFERENCE/build_offline_edition.py --output offline-edition
```

The builder's `load_records()` function reads every `*/records/*.json` file under `CONTENT/vertical-slices`. The workflow then asserts that the generated record count equals `RELEASE/CONTENT-COVERAGE.json.total_records` and the number of canonical record JSON files. The artifact is therefore deliberately a full-corpus CI build, not a selection-based first-edition build.

At the inspected artifact snapshot, all 4,742 records have canonical `publication_status=published` and `completion_status=complete`. Those fields are not the first-edition owner disposition. The record objects do not carry a release-disposition field, and the offline builder does not consume an approved first-edition allowlist, exact-version selection manifest, HOLD/EXCLUDE decisions or dependency-closure manifest.

This distinction matters: the project's reviewed candidate inventories and exact-version registers still mark their records HOLD. The nine-slice Survival Opening Candidate Manifest explicitly says it is not a publication allowlist and all 112 records remain HOLD. It cannot authorize the full 4,742-record corpus.

## 4. Governing implementation requirement

`IMPLEMENTATION/012-PUBLICATION-BUILDER.md` defines the architecture as:

`Canonical Records → selection → composition → validation → Publication Builder → derived publication`

It requires reproducible selection criteria to be stored with the build, exact source-record versions to be pinned, and the build to carry build ID, date, tool versions, input record set and digest. The current simple Offline Edition builder provides deterministic full-corpus packaging, but does not implement that first-edition selection contract.

## 5. Disposition

1. The artifact is valid evidence that the current full-corpus offline packager can produce internally consistent JSON, JSONL, SQLite and static HTML outputs.
2. It is **not** evidence that the first edition has been selected, rights-cleared, editorially approved or safely scoped.
3. It must remain a CI/diagnostic artifact only. Do not distribute, deploy, publish, link as a first-edition release, or use it as a public pilot bundle.
4. The full-corpus build is not itself a CI failure: it is the current workflow's declared diagnostic behavior. The blocker is that a separate selection-aware release build has not yet been implemented and validated.
5. No canonical content, allowlist, release state or publication decision was changed by this audit.

## 6. Required next WP3 implementation — separate bounded work item

Before any first-edition bundle can be called release-ready, create a separate selection-aware build path. It should:

- accept a version-pinned, owner-approved record selection manifest (not a broad folder glob);
- validate each exact `record_id@record_version` and `type_version`;
- validate transitive dependency closure for required Evidence Use, Source, Context, Scope and Relation records;
- reject unresolved HOLD and EXCLUDE records, duplicate identities, missing records, stale versions and dependencies outside the approved selection;
- never infer INCLUDE from `publication_status=published`, `completion_status=complete` or CI PASS;
- preserve canonical record payloads byte-for-byte/semantically unchanged in JSON, JSONL and SQLite;
- write the exact selection manifest, selection digest, source commit, builder version, build ID, timestamp, input record identities and output hashes into the publication manifest;
- remain deterministic for identical exact inputs and settings;
- produce a CI fixture using a small synthetic approved selection until the actual first-edition allowlist exists and is explicitly approved;
- keep the current full-corpus workflow clearly labelled diagnostic, or separate it from the release-selection workflow so that the two artifacts cannot be confused.

The implementation must not invent the first-edition allowlist. The owner-approved record selection is a prerequisite, not something the builder should generate automatically.

## 7. Related security boundary

The HTML output passed the structural parser check on the downloaded artifact and is built by the renderer whose implementation blob is identical to the independently accepted PR #41 SEC-1 fix. This does not close separate low-priority Issue #43 concerning the operator-supplied `edition_id` written to README.md and stronger structural regression tests. Issue #43 remains separate and needs its own bounded scope.

## 8. Non-actions

- No canonical JSON, Source, Claim, Evidence Use, Relation, Context or Scope was changed.
- No allowlist was created or inferred.
- No HOLD was removed and no INCLUDE/EXCLUDE decision was made.
- No publication, deployment or public distribution occurred.
- PR #22 remains Draft and unmerged; `main` remains unchanged.
