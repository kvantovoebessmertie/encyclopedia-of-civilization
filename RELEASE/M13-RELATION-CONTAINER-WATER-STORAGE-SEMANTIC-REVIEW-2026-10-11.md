# M13 Relation Semantic Review — Container and Stored Water States
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Source revision reviewed: `4453783e9dc2db55c4936a8acd85cbc666c46f86`
Status: **Record-level semantic/role mismatch confirmed for correction planning; no Relation JSON changed.**

## Relation under review

`REL-CONTAINER-WATER-STORAGE` currently has:
- `relation_type = storage_container_for`;
- `direction = directed`;
- roles `container_state` and `stored_water_state`;
- participants `ST-WATER-CONTAINER-SANITIZED` and `ST-WATER-CONTAINER-STORED`.

Both participant records are `state` records whose `content.subject_ref.record_id` is the same `OBJ-WATER-CONTAINER`.

- `ST-WATER-CONTAINER-SANITIZED` describes the condition “ёмкость очищена и подготовлена к хранению воды”.
- `ST-WATER-CONTAINER-STORED` describes the condition “в подготовленной ёмкости хранится вода”, but its subject is still the **container**, not a water object/state.

## Finding

The second role, `stored_water_state`, implies that the participant represents a state of the stored water, but the record represents a state of the container. The relation type `storage_container_for` also sounds like a container-to-contained-water relation, while the actual participants are two states of the same container. This is a semantic participant/role mismatch, not a missing-reference or schema-validation failure.

## Correction options for the authorized phase

1. If the intended relation is container-to-water, model or reference a water object/state with the correct subject, then assign roles consistent with those participant types.
2. If the intended relation is between two container states, replace the container-to-water relation type and role labels with a relation type/roles that accurately express the intended state relationship. Do not invent a transition or causal sequence unless the model and source support it.

The relation's source provenance is `SRC-CDC-WATER-STORAGE-2025`; its presence does not resolve the participant-role mismatch. Preserve all IDs and references until the authorized correction plan is approved.

No content JSON was changed. M13 remains open.
