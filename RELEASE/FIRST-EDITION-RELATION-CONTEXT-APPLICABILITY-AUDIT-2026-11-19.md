# First Edition — Relation Context Applicability and Frame Semantics Audit

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `b03508c84bd689281814479180956a4b0aabbe05`

## Purpose

After the 63/63 Relation semantic review, the shared Context issue was checked against the normative Standard, implementation contract, JSON Schema, validator, reference resolver, and existing corpus test. This is a cross-cutting architecture finding, not a re-review of the Relations.

No canonical Relation, Context, or endpoint JSON was changed. No test or validator code was changed. No release decision was made.

## Canonical record facts

`CONTENT/vertical-slices/cross-slice-linkage/records/CTX-CROSS-SLICE-LINKAGE.json` is:

- `record_type=context`, version 1;
- its `content.target_ref` is exactly `REL-CROSS-WATER-CHEMICAL@1`;
- its `context_content.condition` describes a shared semantic frame for relations among already-published records from different vertical slices;
- its `provenance.created_from` includes water, chemical-water, hygiene, flood, and CO-related Sources.

The 63-Relation inventory shows that the other cross-slice Relation records reference this same Context record in `content.frame_ref`; `REL-CONTAINER-WATER-STORAGE@1` is the separate exception and uses `CTX-WATER-STORAGE-EMERGENCY@1`.

## Normative and implementation requirements

1. `STANDARD/015-CONTEXT.md` §§4–5: Context is target-relative; a target may be a whole representation or one Relation, and target granularity must be preserved when material.
2. `STANDARD/015-CONTEXT.md` §§12–13 and `IMPLEMENTATION/015-CONTEXT.md` §11: Context is not automatically a semantic/reference frame; frame selection is a separate role.
3. `IMPLEMENTATION/015-CONTEXT.md` §§4, 7, and 29: `target_ref` identifies what is contextualized; Context applicability is target-relative; L3 is responsible for resolving target identity/version and historical compatibility.
4. `IMPLEMENTATION/005-RECORD-SCHEMA.json`: the Record envelope has a `context` reference; the Relation Content Profile has `frame_ref`; the Context Content Profile requires `context_content` and `target_ref`. These are separate schema locations and roles.

## Verified implementation/test gap

- `REFERENCE/tests/test_content_cross_slice_linkage_vertical_slice.py::test_cross_slice_relations_resolve_to_explicit_context` checks that the Context's single `target_ref` exists somewhere in the Relation set, then checks that every Relation in that slice references the same Context via `frame_ref`. It does not verify that the Context target is the Relation being contextualized, nor does it represent an explicit group target.
- `REFERENCE/src/encyclopedia_reference/references.py` resolves versioned references, but its typed-path map does not assign an expected type to `content.frame_ref`; the resolver therefore checks existence/version without evaluating whether the referenced Context is actually applicable to the Relation using it. A universal `record_type=frame` requirement would be incorrect because the Relation Standard permits Context as one component of an applicable frame.
- The resolver also resolves a Context's `content.target_ref` as a generic reference. It does not compare that target with each Relation that reuses the Context through `frame_ref`, nor does it require an explicit transferability/applicability justification when the target differs.
- `REFERENCE/src/encyclopedia_reference/semantic_rules.py` checks Context inheritance, precedence, transferability, fidelity, dimension dependencies, and overlapping-target conflicts. It does not enforce that a Relation's frame reference points to a frame object or that a Context target matches the Relation that attaches it.

This means the current checks can pass while target-relative Context semantics and Context/Frame role separation remain unresolved.

## Finding

<escape>CTX-CROSS-SLICE-LINKAGE@1</escape> is used as though it were a reusable shared Relation frame, but it is a Context record whose declared target is one specific Relation. The Relation field using it is named `frame_ref`, although the referenced record is typed `context`. The current test confirms reference presence, not semantic applicability.

This is a **release-blocking semantic/modeling issue**, not merely a missing reference or a cosmetic naming concern. It can cause one Relation's Context to be read as applicable to other Relations without a target-specific basis, and it conflates Context with Frame.

## Required architecture decision — do not implement by assumption

The owner must select and approve one coherent model before canonical changes:

### Option A — target-specific Context

- Keep Context target-relative.
- Create a distinct Context Record for each Relation that needs contextualization, or create a single explicit group/collection Record if the intended target is the Relation set as a whole.
- Ensure each Context `target_ref` points to that exact target.
- Attach Context using the schema's Context reference role, not by silently treating a Context Record as a Frame.

### Option B — actual shared Frame

- If the intention is one reusable cross-slice semantic/reference frame, represent it as an explicit Frame/reference-system object under an approved model.
- Keep Context records separate and target-relative.
- Make Relation `frame_ref` resolve to the actual Frame type, not to a Context Record.

### Required regression coverage

Before release use, add tests that prove:

1. a Context targeting Relation A cannot be attached to Relation B as though it were automatically applicable;
2. a group-level Context must target an explicit group/collection Record, not an arbitrary member Relation;
3. `frame_ref` must resolve to a semantically valid applicable-frame component; do not impose a nonexistent universal `record_type=frame`;
4. Where the component is a Context Record, validate target compatibility and preserve the distinction between contextual conditions and the wider applicable frame;
5. the existing cross-slice Relation set has no silent Context fan-out or Context/Frame type substitution.

## Decision boundary

No option is selected or approved in this report. No canonical data was changed. The current shared Context usage must remain a release blocker until the project owner approves the target model and the schema, resolver, validator, and tests enforce it.
