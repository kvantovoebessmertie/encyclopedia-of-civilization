# Bounded authorization — private SI-units reader review preview

Date: 2026-11-13  
Base branch: `mvp-public-contribution-design-2026-10-11`  
Reader branch: `mvp-reader-prototype-2026-10-11`  
Finding: `MVP-SI-PRIVATE-REVIEW-PREVIEW-001`  
Status: **AUTHORIZED FOR PRIVATE, NON-RELEASE REVIEW BUILD ONLY**

## Authorization basis

The project owner explicitly approved proceeding with the accumulated MVP work in the current project conversation. This file narrows that approval to a temporary, private reader preview so the existing SI-unit candidates can be inspected in the actual renderer.

## Exact preview allowlist

The preview may include only these seven exact records:
- `CLM-SI-SEVEN-BASE` v1
- `EU-SI-SEVEN-BASE` v2
- `CLM-SI-DERIVED` v1
- `EU-SI-DERIVED` v2
- `SRC-NIST-SI-UNITS` v1
- `CTX-SI` v1
- `SCP-SI` v1

The preview must exclude:
- `CLM-SI-ACCURACY-BOUNDARY` and `EU-SI-ACCURACY-BOUNDARY`;
- the BIPM Source and any other SI-slice record not listed above;
- all records from other slices.

The context and scope records target Claim A; the preview must not imply that they independently scope Claim B.

## Permitted work

- Add a manifest marked `edition_state: preview` with each selection marked `review_state: preview_only` and a visible internal-review notice.
- Add a builder that loads the exact canonical record files from the combined pull-request merge revision, verifies the exact ID/version set and Claim→EU→Source references, then invokes the existing read-only preview builder.
- Add a pull-request-only workflow that checks out the exact merge commit, builds the private preview, runs browser inspection and uploads a short-retention artifact.
- Record exact input-record SHA-256 values, output HTML/search-script hashes and the merge commit SHA.
- Add tests proving the third Claim is excluded and the preview contains exactly the seven authorized records.

## Rights and attribution boundary

The two Claims use NIST's official SI Units page and Evidence Use v2 records with factual paraphrases, exact section pinpoints and NIST attribution. The private preview may display only these project-authored paraphrases and bibliographic metadata. Do not copy NIST graphics, images, tables or separately copyrighted/third-party material. Preserve a clear NIST attribution and non-endorsement notice.

## Explicit exclusions

This authorization does **not** permit:
- changing any canonical Claim, Evidence Use, Source, Context or Scope record;
- adding any record to a public/release allowlist;
- changing `publication_status`, D/E/B scores or historical assessments;
- public hosting, deployment, distribution, indexing, public URLs or redistribution of the artifact;
- hosted contribution intake, collection of personal data, or external network requests;
- inclusion of the third SI Claim or any other slice;
- merging PR #22 or PR #25, or changing `main`.

The output must retain `edition_state=preview`, `redistribution_allowed=false`, `network_required=false`, and an explicit epistemic boundary. It must be uploaded only as a private GitHub Actions artifact with 14-day retention.

## Acceptance and remaining gates

1. The PR merge commit includes both the authorized SI canonical records and the reader builder.
2. The builder verifies the exact seven ID/version pairs and exact Claim/EU/Source references.
3. The generated manifest records SHA-256 for every full input record and for rendered outputs.
4. Desktop/mobile browser inspection passes; no console/runtime/network errors or horizontal overflow.
5. The rendered preview is inspected for Claim wording, source attribution, section pinpoints, the “22 special-named derived units” qualification and the non-approval notice.
6. Independent non-specialist testing remains NOT RUN until actual external readers complete the existing three-reader protocol.
7. Rights, editorial ownership, correction/takedown, privacy, operations, independent review and public release gates remain open.

This authorization is solely for internal review. It does not approve either Claim for publication or first-pilot release.
