# M11 Relation Audit — 2026-10-09

## Baseline and method

The audit scanned all 58 JSON records in `CONTENT/vertical-slices/cross-slice-linkage/records/` at the M10 CLEAN baseline for references to the three M11 candidate slices.

## Findings

- Exactly one existing cross-slice Relation references an M11 target: `REL-CROSS-MANUFACTURING-HUMAN-FACTORS`.
- Its participants are `CLM-MANUFACTURING_PROCESSES_BASICS-B` and `CLM-HUMAN_FACTORS_BASICS-A`; direction is undirected and the frame is `CTX-CROSS-SLICE-LINKAGE`.
- No dedicated cross-slice Relation references `accessibility-basics` or `ergonomics-basics`.
- No new Relation is required by the locked content corrections. Topical proximity between accessibility, ergonomics and human factors is not by itself sufficient to create a Relation.

## Invariant

The permitted M11 Relation delta is **zero**. Preserve the existing Relation record, participants, roles, direction, frame and provenance exactly. Any unexpected Relation change blocks M11 acceptance and must be investigated.
