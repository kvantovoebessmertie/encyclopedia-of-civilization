# MVP exact-head continuation and implementation review

Date: 2026-11-13
Branch: `mvp-public-contribution-design-2026-10-11`
Status: **technical desk review; no publication approval, no real-record allowlist, no deployment.**

## 1. Live PR and exact-head reconciliation

The live PR heads checked on 2026-11-13 are:

| PR | Scope | Exact head | Required technical workflows |
|---|---|---|---|
| #22 | MVP architecture, publication gates and contribution workflow | `3068f801197387c2b2e0c923afccdeb9b182afcc` | Reference Tests, Release Conformance Gate, Offline Edition: PASS |
| #24 | Offline HTML escaping/security fix | `b0c0522098ef0d7f4613269d921c2f789e9a0a99` | Reference Tests, Release Conformance Gate, Offline Edition: PASS |
| #25 | Allowlisted read-only preview prototype | `a79ebb84d03482aaf412e9c8ea8bba215588d643` | Reference Tests, Release Conformance Gate, Offline Edition: PASS |
| #26 | Professional contribution schema/contract | `6c5c3d4c1788bed05d1ff6e559c0aeb800f42932` | Reference Tests, Release Conformance Gate, Offline Edition: PASS |
| #27 | Local-only contribution form and JSON export | `b9e750f0c6bf885b2839416e614359cb9dc50325` | Reference Tests, Release Conformance Gate, Offline Edition: PASS |

All five PRs were confirmed open, Draft and unmerged at the time of review. PR #25 is stacked on #24; PR #27 is stacked on #26. These results apply only to the exact SHAs above. Earlier checkpoint text listing PR #22 at `64f083c2d613b7352500f31fb59524bba94f64db` is superseded.

## 2. Reader implementation review

The reader implementation:
- requires an explicit non-empty record allowlist and exact record ID/version matches;
- rejects duplicate identities and duplicate selections;
- requires `edition_state=preview` and a visible `preview_only` note per selection;
- escapes displayed text and attribute values;
- renders internal record links only when the referenced exact identity is also in the selected preview;
- renders a Source link only for HTTP(S) URIs;
- keeps the renderer read-only and explicitly non-release.

This is a sound technical boundary for a preview prototype, not an eligibility adjudicator. It does not make a real record safe to publish. The successful #25 build remains synthetic-fixture-only. No real-record manifest/allowlist or rendered real-record artifact was found in the checkpoint.

## 3. Contribution form and schema review

The local form:
- constructs a JSON payload in the browser and downloads it locally;
- does not send the submission to a server or editorial inbox;
- uses textContent for status/error messages rather than injecting contributor text as HTML;
- enforces the 100-item caps for related IDs, Sources and Relations, plus creator/ID length limits;
- applies conditional source/relation requirements and rejects duplicate related IDs;
- explicitly tells the contributor that downloading JSON is not editorial receipt or acceptance.

The schema/contract correctly separates the contributor payload from a future server-side intake envelope. Unknown properties are rejected; private contact fields are excluded from the public content payload; schema validity is explicitly not treated as truth, evidence quality or publication approval.

Remaining implementation questions for the next code pass:
1. verify all browser interaction paths, including reset, dynamic add/remove, invalid form state and keyboard-only operation, in the automated browser test;
2. verify schema parity for every client-side conditional/length/count rule, so the browser cannot accept a payload that the contract rejects or vice versa;
3. verify the downloaded payload against the schema in a test using representative boundary cases;
4. preserve local-only behavior and ensure no hidden network submission or analytics is introduced;
5. keep hosted intake blocked until privacy/retention, abuse controls, access control, editorial ownership and operational recovery are specified.

## 4. Real-record candidate boundary

The two SI-units Claims remain the leading bounded candidate:
- `CLM-SI-SEVEN-BASE@1` + `EU-SI-SEVEN-BASE@2` + `SRC-NIST-SI-UNITS@1`;
- `CLM-SI-DERIVED@1` + `EU-SI-DERIVED@2` + `SRC-NIST-SI-UNITS@1`.

The existing `MVP-SI-PINPOINT-001` authorization covers only the two Evidence Use v2 locator/attribution corrections and their regressions/documentation. It does not authorize a real-record allowlist, preview manifest, deployment or publication. The third Claim `CLM-SI-ACCURACY-BOUNDARY@1` remains excluded.

The measurement-uncertainty candidate screened in `MVP-REAL-RECORD-PILOT-RIGHTS-SCREEN-005` remains HOLD: its source fit is promising, but the canonical EU lacks exact locators, Source identity needs bibliographic correction, and no separate bounded authorization exists.

## 5. Next safe MVP sequence

1. Complete the browser interaction and schema-parity tests listed above on the existing prototype branches.
2. Keep the SI pilot out of the reader until a separate authorization explicitly permits a private, non-release real-record preview.
3. Under that authorization only, create an exact-version allowlist and manifest pinned to a source revision, with input/output hashes.
4. Build privately; inspect Russian text, unit symbols, superscripts, internal navigation, source links, exact section pinpoints and the “22” qualification.
5. Run the prepared three-reader non-specialist protocol on that exact artifact. It remains NOT RUN; do not mark it PASS without participant observations.
6. Obtain editorial-owner and exact-bundle rights/attribution decisions; then rerun all required technical/security workflows on the final preview commit.
7. Keep public deployment and hosted intake blocked until legal, privacy, operations, correction/takedown and rollback gates are closed.

## 6. Integrity

- Canonical content records changed by this review: 0.
- Real-record preview allowlist created: 0.
- Real-record preview built or deployed: no.
- Human readability participants tested: 0.
- PRs merged or promoted from Draft: 0.

Technical CI is green on the five exact heads above. The MVP is not yet a public pilot and no publication approval is implied.

## 7. Follow-up implementation — exact preview input hashes

On the separate reader branch `mvp-reader-prototype-2026-10-11`, the preview manifest now includes `selected_record_hashes`: one SHA-256 per selected full record, computed from canonical JSON serialization. The existing HTML and search-script output hashes remain. Tests verify stable hashes for identical inputs and a changed hash when selected record content changes.

Implementation revision: `2ce1d2bb7f2a189c84642bad9324d33ff392dd57`. Exact-head Reference Tests, Release Conformance Gate, Offline Edition and synthetic-preview workflow are running for this revision at the time this addendum was written; no PASS is claimed until all complete successfully.

The enhancement improves traceability for a later exact-version private preview. It does not itself authorize a real-record allowlist or resolve the SI-unit rights/editorial gates. The reader remains synthetic-only.
