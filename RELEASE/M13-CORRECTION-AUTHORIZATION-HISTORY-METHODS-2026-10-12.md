# M13 Controlled Correction Authorization — History Methods Claim B

Date: 2026-10-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Finding: `M13-HISTORY-METHODS-EVIDENCE-001`

## Status

**Authorized for one bounded, versioned evidence correction only.** This authorization is limited to the history-methods provenance/context Claim and its evidence link described below. It does not approve the Claim for public release or close M13.

## Evidence basis

The existing broad AHA Teaching & Learning landing page is a weak locator for the Claim that a source's provenance and context affect its use as evidence. The U.S. National Archives and Records Administration's *Analyze a Written Document* (Intermediate) worksheet directly asks readers to identify who wrote/read a document, when/where it is from, why it was created, what was happening at the time, and what other evidence should be consulted. The page states that materials created by NARA are in the public domain.

Source URL: https://www.archives.gov/education/lessons/worksheets/analyze-a-written-document-intermediate

The evidence link is deliberately limited: it supports considering provenance and context when interpreting a document as historical evidence. It does not claim that context alone determines reliability or that one worksheet supports every source type. The recorded rights basis applies only to NARA-created worksheet material; third-party content and credited assets are excluded.

## Exact authorized changes

1. Add `SRC-HISTORY-METHODS-NARA-DOCUMENT-ANALYSIS@1` with the exact official NARA locator and bounded rights note.
2. Version `EU-HISTORY_METHODS_BASICS-B` from version 1 to version 2, pointing to the new Source and recording the pinpoint sections “Observe its parts,” “Try to make sense of it,” and “Use it as historical evidence,” plus explicit scope limits.
3. Strengthen only `REFERENCE/tests/test_content_history_methods_basics_vertical_slice.py` to cover the exact Claim/Source/version links, pinpoint text, schema validation, and updated record/source inventory.
4. Update this authorization registry and the M13 remediation checkpoint to document the bounded correction and remaining HOLD.

## Explicit exclusions

- No Claim wording, ID, or version changes.
- No changes to `CLM-HISTORY_METHODS_BASICS-A`, its Evidence Use, or the existing AHA Source.
- No other slices, Sources, Claims, Evidence Uses, Context/Scope records, Relations, schemas, coverage counts, or release gates may be changed under this authorization.
- No deduplication, deletion, preview allowlist, or public release approval.
- Claim B remains publication HOLD until exact-head preflight/CI, Human View, and editorial review are complete.

## Acceptance

Run content preflight, schema/semantic validation, the dedicated regression, Reference Tests, Release Conformance Gate, and Offline Edition on the exact final PR head. Keep PR #21 Draft/unmerged and leave `main` unchanged.
