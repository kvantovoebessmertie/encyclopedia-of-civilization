# M13 Controlled Correction Authorization — Hydrology Source and Evidence Pinpoints

Date: 2026-10-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Finding: `M13-HYDROLOGY-SOURCE-001`

## Status

**Authorized for one bounded, versioned source-metadata and Evidence Use correction only.** This authorization does not assign final D/E/B scores, approve publication, or close M13.

## Basis

The M13 Batch 14 metadata-level triage found that `SRC-HYDROLOGY_BASICS@1` uses a Claim-like sentence as its `source_identity`, while the URI points to the official U.S. Geological Survey Water Science School page, “What is Hydrology?”. The official page contains the exact general definition of hydrology, an explanation of the hydrologic cycle, and a paragraph describing different water pathways.

Official locator: https://www.usgs.gov/water-science-school/science/what-hydrology

The bounded correction records the actual page identity and adds section/paragraph-level descriptions for the three existing Claims. It uses paraphrase and short section labels; no graphics or third-party media are copied. Rights and attribution review for any public edition remains a separate gate.

## Exact authorized changes

1. Version `SRC-HYDROLOGY_BASICS` from @1 to @2, correcting only its source identity/representation/preservation metadata and retaining the same official URI.
2. Version `EU-HYDROLOGY_BASICS-A/B/C` from @1 to @2, each pointing to Source @2 and identifying the specific USGS section or paragraph supporting the complete Claim, with explicit scope limits.
3. Strengthen only `REFERENCE/tests/test_content_hydrology_basics_vertical_slice.py` to assert the versioned Source identity, URI, exact Claim/Evidence Use/Source references, and Claim-specific pinpoint markers.
4. Update `CONTENT/vertical-slices/hydrology-basics/README.md`, this authorization registry, the M13 next-stage reconciliation checkpoint, and the Batch 14 triage note to record the bounded correction.

## Explicit exclusions

- No Claim wording, Claim IDs or Claim versions change.
- No new or deleted Records; the slice remains at nine records.
- No changes to other slices, Sources, Evidence Uses, Context/Scope records, Relations, schemas, coverage counts or release gates.
- No preview allowlist, public release approval, or implication that the hydrology Claims have final D/E/B scores.
- No changes to `main` or protected historical checkpoints.

## Acceptance

Run content preflight, the dedicated hydrology regression, Reference Tests, Release Conformance Gate and Offline Edition on one exact final PR head. Keep PR #21 Draft/unmerged and `main` unchanged.
