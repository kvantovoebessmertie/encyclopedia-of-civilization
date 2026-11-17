# MVP SI-Units Candidate — Next-Gate Status — 2026-10-12

Status: **two conditional candidates remain HOLD; no real-record allowlist or release approval.**

## Exact candidate state

| Claim | Evidence Use | Source | Current disposition |
|---|---|---|---|
| `CLM-SI-SEVEN-BASE` v1 | `EU-SI-SEVEN-BASE` v2 | `SRC-NIST-SI-UNITS` v1 | Conditional candidate; exact NIST section pinpoints recorded; reader clarification and release gates remain. |
| `CLM-SI-DERIVED` v1 | `EU-SI-DERIVED` v2 | `SRC-NIST-SI-UNITS` v1 | Conditional candidate; preserve that 22 means derived units with special names and symbols, not all derived units. |
| `CLM-SI-ACCURACY-BOUNDARY` v1 | `EU-SI-ACCURACY-BOUNDARY` v1 | `SRC-BIPM-SI-BROCHURE-2026` v1 | HOLD / exclude from first pilot pending pinpoint, rights/attribution, and specialist review. |

The bounded correction authorization `MVP-SI-PINPOINT-001` and the existing SI candidate/Human View desk-review notes are the governing records for the two Evidence Use v2 corrections. Do not infer that an Evidence Use correction itself constitutes release approval.

## Gate matrix for the first two candidates

| Gate | State | Evidence / remaining work |
|---|---|---|
| Claim/source fit | PASS at desk-review level, conditional | NIST “Defining Constants” and “Base and Derived Units” sections are identified. Confirm the exact rendered text against the versioned Evidence Use records. |
| Claim wording | PASS WITH CLARIFICATION | Keep base units distinct from defining constants; preserve the 22-unit category boundary. Test the short reader-facing glosses in the actual reader. |
| Rights/attribution | CONDITIONAL | NIST's general public-information statement is a candidate basis; preserve NIST attribution and exclude separately credited/copyright-marked assets unless separately cleared. Record the final rights decision for the exact edition. |
| Technical/build checks | PASS on recorded exact heads only | The current PR heads must be checked again after any code or content changes; a green CI run is not editorial approval. |
| Rendered reader inspection | OPEN | Inspect actual HTML for unit symbols, superscripts, language, accessibility, source navigation, qualifications, and status labels. |
| Independent non-specialist reader test | OPEN | Desk review is not an independent reader test. Have a reader unfamiliar with the repository explain both Claims and the “22” qualification in their own words; record observed confusion and revisions. |
| Editorial owner approval | OPEN | A named owner must approve each exact Claim version and its complete linked record bundle. |
| Exact-version allowlist and artifact hashes | NOT CREATED | Add only the individually approved IDs/versions after all gates pass; record source revision and generated artifact hashes. |
| Public operations/policies | OPEN / launch blocker | License/terms, corrections/takedown, privacy, hosting, backup/monitoring, and operating ownership remain unresolved. |

## Next bounded actions

1. Build the private preview only with the existing synthetic fixture and inspect its layout/security behavior; do not represent synthetic data as real content.
2. Confirm that the current renderer can show Claim, exact Evidence Use pinpoint, source attribution, and limitations without losing the SI count qualification.
3. Conduct and document an independent non-specialist comprehension test for the two candidate Claims using RELEASE/MVP-SI-UNITS-NON-SPECIALIST-READABILITY-TEST-2026-10-14.md. The protocol is prepared but has not been run; do not mark this gate PASS until actual reader observations and the exact tested artifact revision are recorded.
4. Record rights and editorial decisions against exact record versions. If any wording or record changes, repeat the relevant checks on the resulting exact commit.
5. Only after all per-Claim gates pass, prepare a separate exact-version allowlist and inspect the generated artifact. Keep the third Claim excluded.

## Protected-state controls

- No canonical content or allowlist change is authorized by this status note.
- No deployment, public intake, or publication is authorized.
- The local contribution form remains an offline JSON-export prototype; it is not a hosted intake channel.
- Keep MVP implementation PRs Draft/unmerged and keep `main` unchanged until the established review and release gates pass.

## Continuation addendum — private real-record preview completed, release gate still open

Date: 2026-11-13

The project owner separately authorized a **private, non-release review preview** under `RELEASE/MVP-SI-UNITS-PRIVATE-REVIEW-PREVIEW-AUTHORIZATION-2026-11-13.md`. This does not supersede the release restrictions above.

### Exact private preview

- Builder branch: `mvp-reader-prototype-2026-10-11`.
- Exact merge revision embedded in the generated manifest: `2268166627a7d853622af12bbf55731c32590937`.
- Artifact: `mvp-si-private-review-preview-2268166627a7d853622af12bbf55731c32590937`, GitHub Actions run `43495829280`.
- Exact records: `CLM-SI-SEVEN-BASE` v1, `EU-SI-SEVEN-BASE` v2, `CLM-SI-DERIVED` v1, `EU-SI-DERIVED` v2, `SRC-NIST-SI-UNITS` v1, `CTX-SI` v1 and `SCP-SI` v1.
- Excluded: `CLM-SI-ACCURACY-BOUNDARY`, its Evidence Use, the BIPM Source and every other record.
- The manifest contains SHA-256 hashes for all seven full input records and for the rendered HTML and search script. It records `edition_state=preview`, `redistribution_allowed=false` and `network_required=false`.

### Actual browser inspection

**PASS** The private preview workflow completed successfully. Desktop 1280×900 and mobile 390×844 Chromium inspection passed:
- exact seven-record allowlist and exclusion of the third Claim;
- NIST attribution and Claim-specific section pinpoints;
- the “22 special-named derived units” boundary;
- search match/no-match/reset;
- visible keyboard focus and full keyboard order through links/disclosures;
- no mobile horizontal overflow;
- no external network requests, console errors or runtime errors.

The first browser pass found a keyboard-order test assumption and then a real mobile overflow caused by long identifiers. Both were corrected; the final exact workflow passed. The rendered page remains an internal preview and was not deployed.

### Remaining gates — unchanged

- Independent three-reader comprehension test: **NOT RUN**. Actual external readers must explain both Claims and the “22” qualification in their own words; a browser test is not a substitute.
- Final rights/attribution decision for the exact edition: **CONDITIONAL / OPEN**.
- Editorial owner approval for each exact Claim bundle: **OPEN**.
- Release/public allowlist: **NOT CREATED**.
- Public operations, correction/takedown, privacy and deployment approval: **OPEN / launch blockers**.

The private preview manifest is not the release allowlist. No publication approval, deployment or public distribution is implied.

## 9. Final exact private-preview verification

A follow-up exact-head run added explicit browser assertions for the NIST non-endorsement notice and for the rule that Claim A's Context/Scope must not be carried over to Claim B.

- Workflow run: `43496130959` — **SUCCESS**.
- Reader branch head: `82baeb22a8fb79f3ac140e898d4d90da92b7143a`.
- Exact combined review revision in manifest: `64ad1f73ac3c2bd324b46d6f6322b9131a875715`.
- Artifact: `mvp-si-private-review-preview-64ad1f73ac3c2bd324b46d6f6322b9131a875715`.
- Selected records: exactly 7; input record hashes: 7; output hashes: present.
- `redistribution_allowed=false`; `network_required=false`; no external requests or browser errors.
- Desktop/mobile, allowlist, exclusion, NIST attribution/non-endorsement, Claim-specific pinpoints, 22-unit boundary, search, keyboard navigation and mobile overflow checks: **PASS**.

This supersedes the earlier successful preview run as the latest verification baseline. It still does not close the independent three-reader comprehension gate, exact release allowlist, rights/editorial approval or public operations gates.
