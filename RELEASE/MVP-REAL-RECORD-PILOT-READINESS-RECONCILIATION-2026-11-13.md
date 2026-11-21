# MVP continuation checkpoint — real-record pilot readiness

Date: 2026-11-13
Workstream: public MVP, separate from M13
Status: technical prototypes are green on their recorded heads; real-record reader pilot remains blocked by explicit publication gates.

## 1. Exact branch and CI reconciliation

Repository default branch `main` remains at `203a7028e08da394fd44630fe38727be07bc8849`.

| PR | Purpose | Exact head | Required technical checks |
|---|---|---|---|
| #22 | MVP requirements / pilot design | `64f083c2d613b7352500f31fb59524bba94f64db` | Reference Tests, Release Gate, Offline Edition: successful |
| #24 | Offline HTML escaping/security fix | `b0c0522098ef0d7f4613269d921c2f789e9a0a99` | Reference Tests, Release Gate, Offline Edition: successful |
| #25 | Allowlisted read-only reader prototype | `a79ebb84d03482aaf412e9c8ea8bba215588d643` | Reference Tests, Release Gate, Offline Edition and synthetic-preview build: successful |
| #26 | Professional contribution intake schema | `6c5c3d4c1788bed05d1ff6e559c0aeb800f42932` | Reference Tests, Release Gate, Offline Edition: successful |
| #27 | Local-only professional form / JSON export | `b9e750f0c6bf885b2839416e614359cb9dc50325` | Reference Tests, Release Gate, Offline Edition: successful |

All five PRs remain open, Draft and unmerged. PR #25 is stacked on PR #24; PR #27 is stacked on PR #26. These checks establish technical conformance only for the exact heads listed. They do not establish content eligibility, usability, rights clearance or publication approval.

## 2. Current real-record candidate

The best documented low-consequence candidate remains the SI-units slice, limited to two Claims:

- `CLM-SI-SEVEN-BASE@1` + `EU-SI-SEVEN-BASE@2` + `SRC-NIST-SI-UNITS@1`.
- `CLM-SI-DERIVED@1` + `EU-SI-DERIVED@2` + `SRC-NIST-SI-UNITS@1`.

The bounded authorization `MVP-SI-PINPOINT-001` covers only the two Evidence Use v2 locator/attribution corrections and their regression/documentation. The current regression verifies the exact versions, preserved references, NIST section names, attribution and the critical boundary that 22 means derived units with special names and symbols, not all derived units.

The third Claim `CLM-SI-ACCURACY-BOUNDARY@1` remains excluded from the first pilot.

NIST's public-information/copyright statement is a conditional rights basis for factual paraphrase with attribution. It does not extend to third-party graphics, images or separately copyrighted assets. The final edition rights decision remains unrecorded.

## 3. Actual reader test and real-record preview

The current reader PR #25 still builds only the two-record synthetic fixture. Its exact-head `build-synthetic-preview` check succeeded, but this is not a real-record reader test.

The independent non-specialist protocol is prepared in `RELEASE/MVP-SI-UNITS-NON-SPECIALIST-READABILITY-TEST-2026-10-14.md`. It requires three readers, tests the distinction between base units and defining constants, and tests the meaning of the number 22. All three participant rows remain NOT RUN. No participant observations or readability PASS are claimed.

No real-record preview allowlist or exact-version release manifest exists. The bounded SI correction authorization explicitly excludes creation of a real-record allowlist, release manifest, deployment or hosted intake. Therefore do not silently use the corrected Evidence Uses as permission to build or publish a real-record preview.

## 4. Next permitted sequence

1. Preserve the synthetic-only workflow and security guards; do not weaken preview-state or allowlist checks.
2. Obtain a separately bounded editorial authorization for a **private, non-release real-record preview** containing only the two SI Claims and their exact Claim/Evidence Use/Source/Context/Scope versions. Keep the accuracy-boundary Claim excluded.
3. Under that authorization, add a preview-only manifest with exact IDs/versions, pinned source revision, and record/output hashes. No deployment or public release.
4. Inspect the rendered artifact for Russian text, unit symbols, superscripts, source navigation, section pinpoints, the base-unit/constant distinction, and the “22” qualification.
5. Run the prepared three-reader protocol on that exact rendered artifact; record observations without collecting unnecessary personal data. Fix any comprehension or navigation blockers and repeat affected tasks.
6. Obtain an explicit editorial-owner decision for each Claim and a documented rights/attribution decision for the exact preview bundle.
7. Re-run all required technical/security workflows on the exact final preview commit and inspect the artifact before considering a closed pilot.

## 5. Intake and public operations boundary

- PR #27 remains a local-only form that exports JSON; it does not submit to an editorial inbox.
- PR #26 supplies a schema/validation contract; schema validity is not evidence of truth or permission to publish.
- There is no hosted submission endpoint, intake storage, or public deployment.
- Public terms/licensing, privacy and retention, abuse handling, editorial ownership, hosting/operations, correction/takedown and rollback remain launch blockers.

## 6. Integrity

- No canonical records changed in this checkpoint.
- No real-record allowlist was created.
- No publication or deployment approval is claimed.
- No PR was merged or retargeted.
- `main` remains unchanged.

---
This checkpoint records the current state and the next safe gate. It is not an authorization to create the real-record allowlist or publish the SI slice.
