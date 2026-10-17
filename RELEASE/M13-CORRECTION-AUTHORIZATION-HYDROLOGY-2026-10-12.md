# M13 Controlled Correction Authorization — Hydrology Source and Evidence Pinpoints

Date: 2026-10-12  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Finding: `M13-HYDROLOGY-SOURCE-001`

## Status

**Authorized for one bounded, versioned source/evidence correction and required reference-version cascade only.** This authorization does not assign final D/E/B scores, approve publication, or close M13.

## Basis

The M13 Batch 14 metadata-level triage found that `SRC-HYDROLOGY_BASICS@1` uses a Claim-like sentence as its `source_identity`, while the URI points to the official U.S. Geological Survey Water Science School page, “What is Hydrology?”. The official page contains the exact general definition of hydrology, an explanation of the hydrologic cycle, and a paragraph describing different water pathways.

Official locator: https://www.usgs.gov/water-science-school/science/what-hydrology

The correction records the actual page identity and adds section/paragraph-level descriptions for the three existing Claims. Because the current storage contains only the latest version of a Record, all direct references to the revised Source/Claim versions must remain resolvable. The three Claim statements remain byte-for-byte semantically unchanged; Context, Scope and one cross-slice Relation are versioned only to preserve reference integrity. The Relation's meaning, participants' identities, roles and direction do not change.

The descriptions use paraphrase and short section labels; no graphics or third-party media are copied. Rights and attribution review for any public edition remains a separate gate.

## Exact authorized changes

1. Version `SRC-HYDROLOGY_BASICS` from @1 to @2, correcting only its source identity/representation/preservation metadata and retaining the same official URI.
2. Version `CLM-HYDROLOGY_BASICS-A/B/C` from @1 to @2, changing only their `provenance.created_from` reference to `SRC-HYDROLOGY_BASICS@2`; preserve statement, Claim type and all other semantics.
3. Version `EU-HYDROLOGY_BASICS-A/B/C` from @1 to @2, pointing to the corresponding Claim @2 and Source @2, and adding claim-specific section/paragraph pinpoints with scope limits.
4. Version `CTX-HYDROLOGY_BASICS` and `SCP-HYDROLOGY_BASICS` to @2, changing only `target_ref` to `CLM-HYDROLOGY_BASICS-A@2`.
5. Version `REL_M3_WATER_RESOURCES_HYDROLOGY` to @2, updating only the hydrology Source provenance reference and the participant reference to Claim A @2. Preserve relation type, participant identities, roles, direction and frame.
6. Strengthen only `REFERENCE/tests/test_content_hydrology_basics_vertical_slice.py` to assert the versioned Source identity, exact Claim/Evidence Use/Source links and pinpoint markers, Context/Scope targets, and the cross-slice Relation references.
7. Update `CONTENT/vertical-slices/hydrology-basics/README.md`, this authorization registry, the M13 next-stage reconciliation checkpoint, and the Batch 14 triage note.

## Explicit exclusions

- No Claim wording, Claim IDs, Claim types or relation semantics change.
- No new or deleted Records; hydrology remains at nine records and no new Relation is added.
- No other slices, Sources, Evidence Uses, Context/Scope records, Relations, schemas, coverage counts or release gates may be changed.
- No preview allowlist, public release approval, or implication that the hydrology Claims have final D/E/B scores.
- No changes to `main` or protected historical checkpoints.

## Acceptance

Run content preflight, the dedicated hydrology regression, Reference Tests, Release Conformance Gate and Offline Edition on one exact final PR head. Keep PR #21 Draft/unmerged and `main` unchanged.
