# First Edition — Water Storage State/Relation/Context Conformance Audit

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `95ca0f26cef8e63e07b26f373e07feb5d7d75310`

## Scope

Re-examined `REL-CONTAINER-WATER-STORAGE@1` and every directly referenced record to establish whether the relation type, participant roles, State subjects, and Context target form a coherent model.

## Exact records fetched

- `REL-CONTAINER-WATER-STORAGE@1` — exact `relation`.
- `ST-WATER-CONTAINER-SANITIZED@1` — exact `state`.
- `ST-WATER-CONTAINER-STORED@1` — exact `state`.
- `OBJ-WATER-CONTAINER@1` — exact generic `record` used as both State `subject_ref` targets.
- `CTX-WATER-STORAGE-EMERGENCY@1` — exact `context`.
- `CLM-WATER-STORAGE-CONTAINER@1` — exact `claim`.
- `SRC-CDC-WATER-STORAGE-2025@1` — exact `source`, referenced by the Relation, both States, Object record, Context, and Claim.

All fetched record IDs, versions, and types match the references inspected. No canonical record was changed.

## Findings

### 1. Relation type and participants are semantically misaligned

The Relation declares:

- `relation_type=storage_container_for`;
- participant 1: `ST-WATER-CONTAINER-SANITIZED@1`, role `container_state`;
- participant 2: `ST-WATER-CONTAINER-STORED@1`, role `stored_water_state`;
- `direction=directed`.

Both State records have the same `subject_ref`: `OBJ-WATER-CONTAINER@1`.

The first State describes the container after cleaning/preparation. The second State describes the condition of that same container when water is stored. Both have `subject_ref=OBJ-WATER-CONTAINER@1`; the second is not a State of the water. Consequently, the role `stored_water_state` is unsupported by the participant's actual subject identity.

The declared relation type ordinarily reads as a container-to-stored-water relationship, but the actual participants are two States of the same container subject. The current graph does not establish a container Object linked to a distinct water Object/subject, nor does it establish that the Relation is a state transition.

### 2. No transition semantics are represented

Both States use `status=snapshot`. The Relation is directed, but no temporal ordering, transition event, start/end time, or explicit state-transition relation type is represented. It must not be interpreted as proving that the sanitized state necessarily transitions into the stored state or that the stored-water state is a distinct entity.

### 3. Context target does not match the Relation/State frame usage

`CTX-WATER-STORAGE-EMERGENCY@1` has:

`target_ref = CLM-WATER-STORAGE-CONTAINER@1`

However:
- the Relation uses this Context in `frame_ref`;
- both State records use this Context in `frame_ref`;
- the Context itself is target-relative to the Claim.

The shared emergency-water-storage circumstances may be relevant to all these records, but the current representation does not explicitly authorize the Context to transfer from the Claim to the two States and the Relation. The same target-relative/Frame distinction found in the cross-slice Context audit applies here.

## Disposition

**HOLD — do not use `REL-CONTAINER-WATER-STORAGE@1` as a release navigation or instructional relation until the model is corrected or explicitly justified by an approved semantic contract.**

## Required owner/editorial resolution

Choose the intended semantic model before changing canonical records:

1. **Object-to-object relation (if container-for-water is intended):** represent a distinct water Object/Record (and a water State if needed), then link the container Object and water Object. This requires source support and authorization; do not infer a water participant from the current State records.
2. **State-representation relation (if both snapshots are intentionally compared):** define a Relation type that accurately describes two states of the same container. Do not use `storage_container_for` with a `stored_water_state` role. Do not infer a transition or temporal order; neither State has temporal data.
3. **Redundancy/removal option:** if the Relation adds no meaning beyond the two States' common `subject_ref`, remove it from release scope through an authorized allowlist decision rather than preserving a misleading edge.
4. **Context applicability:** the Context may contribute to the applicable frame, but its `target_ref` is the Claim. Give it a target-compatible basis for this Relation/State use or keep the Relation on HOLD; do not assume a single target is a wildcard.

Do not change only the relation label while leaving the State subjects and Context targets inconsistent.

## Boundaries

- No canonical Relation, State, Object, Claim, Context, or Source changed.
- No decision or allowlist status changed.
- No Claim or Relation promoted to INCLUDE.
- This remains an independent blocker in addition to the shared cross-slice Context/Frame conformance issue.
