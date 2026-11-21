# R9 — Library / Archival Preservation Relation Alignment

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Branch: `mvp-public-contribution-design-2026-10-11`

## Owner decision and authorization

The project owner explicitly approved a bounded correction on 2026-11-20. The authorization is recorded in `RELEASE/EDITORIAL-CORRECTION.json` under `r9_library_archival_relation_alignment_2026_11_20`.

The authorized change is limited to the exact Library/Archival Relation and its target-specific Context. No Claim, Source, Evidence Use, Scope, other Relation, or other Context is modified.

## Final canonical state

### Relation

`REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@6`

- Library participant: `CLM-LIBRARY_SCIENCE-C@2`
- Archival participant: `CLM-ARCHIVAL_SCIENCE-A@2`
- Type: `shared_information_preservation_context`
- Roles: `linked_record`, `linked_record`
- Direction: `undirected`
- Provenance: `SRC-LIBRARY_SCIENCE@2` and `SRC-ARCHIVAL_SCIENCE@2`
- Frame: `CTX-REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3`

Only the library Claim endpoint was substituted. The Relation type, participant order, archival endpoint, roles, direction, provenance sources and conceptual scope were preserved.

### Context

`CTX-REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@3`

- `target_ref` points to `REL-CROSS-LIBRARY-ARCHIVAL-PRESERVATION@6`.
- The Relation's `frame_ref` points back to this exact Context version.
- Context condition, epistemic status, provenance and method remain unchanged.

The final reciprocal version references are exact: Relation @6 → Context @3; Context @3 → Relation @6.

## Semantic basis and limits

The former Library Claim A concerned equal access to information, knowledge, collections and library services. The selected Claim C more directly addresses preservation and access to local and Indigenous knowledge and heritage, including oral traditions and digital materials.

Its Evidence Use points to IFLA-UNESCO Public Library Manifesto 2022, “Missions of the Public Library”, p. 2. The archival endpoint remains Claim A, whose Evidence Use points to the Society of American Archivists' introductory “Archives 101: Basic Principles” processing paragraph and the Appraisal, Arrangement, Description and Preservation subsections.

This is a bounded conceptual linkage, not a claim that public libraries and archives perform identical functions, share one operational preservation system, or that the two sources jointly establish a technical workflow. The sources support their respective endpoint Claims; the Relation records the explicit cross-domain linkage and does not replace either Evidence Use.

## Release and rights status

- Relation remains HOLD.
- Library Science remains HOLD.
- Archival Science remains HOLD.
- No first-edition allowlist or INCLUDE decision was changed.
- IFLA-UNESCO and SAA item-level rights, project-distribution compatibility, independent editorial review and Human View remain open.
- No publication, deployment, merge or change to `main` is authorized.

## Verification required

The final canonical pair was re-read from the PR branch and checked for exact reciprocal version references. The four required CI workflows must be evaluated on the final PR HEAD; results from earlier commits do not carry forward.

**Conclusion:** the semantic endpoint is now more specific and the Relation/Context version chain is internally aligned. This is a bounded remediation only; it does not clear either slice or the Relation for release.
