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
