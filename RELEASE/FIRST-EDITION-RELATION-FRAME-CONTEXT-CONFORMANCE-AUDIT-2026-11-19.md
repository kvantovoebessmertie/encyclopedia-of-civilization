# First Edition — Relation Frame / Context Conformance Audit

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `38fff5786f7dd2d3400b27f298c022a342479668`

## Purpose

Determine whether the shared Context used by the cross-slice Relation corpus is correctly scoped to the Relations that reference it, and whether the implementation contract, schema, validator, and tests enforce that applicability.

## Canonical structure checked

- `CTX-CROSS-SLICE-LINKAGE@1` is an exact `context` Record.
- Its `content.target_ref` is exactly `REL-CROSS-WATER-CHEMICAL@1`.
- The Relation inventory contains 63 records. Exactly 62 Relation rows reference `CTX-CROSS-SLICE-LINKAGE@1`; the remaining `REL-CONTAINER-WATER-STORAGE@1` references its separate `CTX-WATER-STORAGE-EMERGENCY@1`.
- The cross-slice linkage test checks that the Context target ID belongs to the Relation set and that each Relation in that directory has the exact shared `frame_ref`. It does not test whether the Context's target-relative semantics are applicable to every Relation using it.

## Normative and implementation requirements

The Context standard and implementation contract establish three relevant rules:

1. Context is always interpreted relative to its explicit `target_ref`.
2. Context of Record A is not automatically the Context of every component or neighboring Record; the Validator must not spread Context merely because references are nearby.
3. Context and an applicable semantic/reference Frame are not automatically the same thing. A factual Context does not select a Frame by itself; the Frame must have its own resolvable mechanism.

The Relation content profile defines `frame_ref` as a generic `record_ref`, without proving the referenced Record's semantic role or applicability to the Relation. This is not necessarily a schema defect: `STANDARD/013-RELATION.md` §11 explicitly allows Context to be one component of an applicable frame. Conversely, `STANDARD/015-CONTEXT.md` §§12–13 prohibits treating Context as a Frame automatically. The current L4 Relation validator checks that a frame reference is present; that check does not establish target compatibility or justify use of this particular Context as a component of each Relation's applicable frame.

## Finding

**BLOCKING ARCHITECTURE CONFORMANCE GAP**

The repository currently uses one target-relative Context Record as the `frame_ref` for 62 Relations, while that Context's own target is one specific Relation. Context may legitimately participate in an applicable frame, but its reuse for other Relations needs an explicit target-compatible transfer/applicability basis. The tests establish reference presence and that the target is a Relation, but do not establish that basis for all 62 Relations.

This is not proof that the Context content is factually wrong. It is a mismatch between:
- target-relative Context semantics;
- the distinct semantic role of a Frame;
- the corpus pattern of one Context reused as a frame by many Relations; and
- the limited assertions in the current test/validator.

The test currently passes a structure that does not prove the semantic applicability it appears to assume.

## Required resolution — decision, not an automatic edit

Choose and specify one of the following architectural paths through the project's normal review process:

**Path A — explicit shared applicable-frame composition.** If a shared semantic/reference system is needed, define how it is represented and resolved using an approved existing model/Profile or other mechanism. Keep target-relative Context distinct; it may contribute to the applicable frame only where its role and applicability are explicit. Do not introduce a new Core Frame entity or require a `record_type=frame` without a separate Standard decision.

**Path B — formally reusable Context.** If a Context is intended to apply to multiple Relations, amend the normative/implementation contract to define explicit multi-target or inheritance/applicability semantics, including transferability and validation. A single `target_ref` must not be silently treated as a wildcard.

**Path C — per-Relation Context.** Give each Relation its own Context Record with an exact `target_ref` to that Relation, while keeping genuinely shared frame semantics separate.

No path is selected here. This requires architecture-owner approval; do not change canonical Records or standards speculatively.

## Required validator and test changes after the decision

- Validate that every Relation `frame_ref` resolves to a semantically valid applicable-frame component. Do not require a separate `record_type=frame` universally; where the component is a Context Record, enforce target compatibility and any explicit transferability justification.
- Validate target compatibility for every Context reference; reject implicit Context propagation.
- Add negative tests where a Context targets Relation A but is attached to Relation B without an explicit reuse/transfer rule.
- Add positive tests for the chosen approved reuse or per-Relation model.
- Ensure offline/reference builds enforce the same semantic contract.

## Scope and impact

- Affects the shared frame references of 62/63 Relations.
- `REL-CONTAINER-WATER-STORAGE@1` has a separate previously recorded Context/State/Relation target-alignment issue and is not resolved by this audit.
- Does not change any participant Claim, Source, Evidence Use, Relation, Context, Scope, allowlist, or publication decision.
- All candidate decisions remain HOLD; no Relation is approved for release.

## Conclusion

The 63/63 Relation semantic audit is complete, but Relation frame/Context conformance is not. This issue must be resolved before any of the affected Relations can be treated as release-eligible.


## Normative precision correction

`STANDARD/013-RELATION.md` §11 states that an applicable frame may include Context. `STANDARD/015-CONTEXT.md` §§12–13 states that Context is not universally a Frame and does not determine frame selection automatically. These provisions are compatible: a Context may contribute to an applicable frame when explicitly selected, while its own target-relative applicability remains independently validated. This audit does not require a new Frame Record type. The unresolved defect is the unvalidated reuse of one target-relative Context across 62 Relation targets.
