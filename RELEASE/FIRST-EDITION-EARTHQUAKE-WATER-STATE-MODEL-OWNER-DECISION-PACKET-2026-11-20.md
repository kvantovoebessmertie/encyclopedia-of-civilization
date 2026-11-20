# First Edition — Earthquake Event and Emergency Water State Model Owner Decision Packet

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `653c4f6770ee757452d3ea5eeb8c9f61ea2d1a09`  
Status: **DECISION PACKET ONLY — OWNER DECISIONS OPEN; NO CANONICAL CHANGES**

## 1. Scope and constraints

This packet documents the two model-level blockers at the top of the First Edition priority sequence. It does not choose or implement an owner decision.

The current owner direction is that both decisions remain open and all Relations remain HOLD. Preserve that boundary:
- do not delete or rewrite the Event, State, Relation or Context records;
- do not invent an earthquake occurrence, date, location, time or sequence;
- do not infer a water Object/State or relation semantics without source and owner authorization;
- do not change allowlists, publication decisions or release scope.

## 2. Earthquake Event — `EVT-EARTHQUAKE-SHAKING@1`

### Exact current model

- Event: `EVT-EARTHQUAKE-SHAKING@1`
- Context: `CTX-EARTHQUAKE-SHAKING@1`
- Scope: `SCP-EARTHQUAKE-SHAKING@1`
- Cross-slice Relation: `REL-CROSS-EARTHQUAKE-AFTERSHOCK@2`
- Relation Context: `CTX-REL-CROSS-EARTHQUAKE-AFTERSHOCK@1`
- Event source: `SRC-FEMA-EARTHQUAKE-2025@1`
- Aftershock Claim: `CLM-AFTERSHOCK-EXPECT@1`

The Event content is the generic sentence “Ощущается сотрясение грунта при землетрясении.” Its status is `reported`, but it has no identified occurrence, time/boundary, location, observation report or other event-specific attribution.

The Event's Context and Scope both target `CLM-EARTHQUAKE-DROP-COVER-HOLD@1`, a protective-action Claim, rather than identifying a particular Event occurrence. The cross-slice Relation treats the generic Event as the `preceding_event` for the aftershock warning Claim.

### Normative finding

`STANDARD/009-EVENT.md` requires:
- E-01: an Event represents a defined occurrence with temporal occurrence/boundary semantics, represented as having occurred;
- E-02: defined event content;
- E-03: sufficient event attribution as a temporal occurrence/transition/boundary;
- E-05: simple state attribution alone does not automatically constitute an Event;
- E-07: an Event must remain distinguishable from a Claim, Action, Process, State, Observation and Result;
- E-08: the existence of an Event record does not itself establish epistemic certainty.

The current record supplies a generic description of ground shaking but no specific occurrence or adequate event attribution. The current source, FEMA/Ready.gov *How to Stay Safe When an Earthquake Threatens*, is a general preparedness and safety fact sheet. It gives protective guidance and warns readers to expect aftershocks; it is not a report of a particular earthquake occurrence.

Official source:
https://www.ready.gov/sites/default/files/2025-02/fema_full-suite-hazard-info-sheets.pdf

The source supports general earthquake safety guidance and the aftershock warning, not an identified historical Event instance.

### Recommendation

Do not invent an occurrence or retrofit a date/location. Keep `EVT-EARTHQUAKE-SHAKING@1` and `REL-CROSS-EARTHQUAKE-AFTERSHOCK@2` unchanged and HOLD. Preserve the general protective-action and aftershock Claims as knowledge records.

For first-edition release selection, the conservative option is to exclude the Event and the Event-dependent Relation from the release allowlist while preserving them in the canonical corpus as HOLD. If the owner intends an actual event instance, a separate source documenting a specific occurrence and its event attribution is required before any correction.

### Owner choice required

- **E-Q1 — Conservative disposition (recommended):** keep Event and Relation unchanged and HOLD; exclude both from first-edition release scope without deleting canonical records.
- **E-Q2 — Specific occurrence:** supply/approve an exact event source and occurrence attribution, then authorize a bounded Event/Context/Scope/Relation versioning plan.
- **E-Q3 — Generic knowledge only:** authorize removal of the Event's role from the release graph and retain the general guidance Claims; do not represent the generic phenomenon as an occurrence Event.

No option is selected by this packet.

## 3. Emergency Water Storage — `REL-CONTAINER-WATER-STORAGE@1`

### Exact current model

- Container Object: `OBJ-WATER-CONTAINER@1`
- State A: `ST-WATER-CONTAINER-SANITIZED@1`
  - subject: `OBJ-WATER-CONTAINER@1`
  - condition: the container has been cleaned and prepared for water storage.
- State B: `ST-WATER-CONTAINER-STORED@1`
  - subject: `OBJ-WATER-CONTAINER@1`
  - condition: water is stored in the prepared container.
- Relation: `REL-CONTAINER-WATER-STORAGE@1`
  - type: `storage_container_for`
  - participants: State A @1 and State B @1
  - roles: `container_state` and `stored_water_state`
  - direction: directed
- Context: `CTX-WATER-STORAGE-EMERGENCY@1`
  - target: `CLM-WATER-STORAGE-CONTAINER@1`, not the Relation.

Both State participants refer to the same container Object. State B describes the container being in a condition in which it holds water; it is not a State of a separately represented water Object. The Relation's role `stored_water_state` therefore does not match the actual participant's subject identity. The Context is a general emergency-water Context targeting the Claim, not a Relation-specific Context target.

### Evidence basis

The CDC source `SRC-CDC-WATER-STORAGE-2025@1` directly describes:
- choosing an approved food-grade water-storage container;
- washing and sanitizing the container before filling;
- letting the container air-dry;
- filling the sanitized container with clean water and closing it tightly;
- storing and labeling the filled container.

Official source:
https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html

The current claim and Evidence Use records are about approved food-grade containers and avoiding toxic transfer. The CDC page also supplies a defensible factual basis for distinguishing the container object, the prepared-container state, and the stored-water state. The EPA source provides general emergency drinking-water supply context.

### Model alternatives

**W-Q1 — Add an explicit water Object/State (recommended if the Relation is to mean “container for stored water”).**

- Preserve `OBJ-WATER-CONTAINER@1` and the two existing container-state records.
- Add a separately identified water Object and a State representing water stored in that Object/inside the container, with a precise CDC locator.
- Rebuild the Relation so the participants and roles genuinely represent a container and a water State; use `storage_container_for` only if the registered Relation semantics permit that participant-type pairing.
- Create/align a Relation-specific Context whose target is the new exact Relation version, and ensure the Relation frame points back to that exact Context version.
- Preserve all existing State history; do not repurpose a container State as a water State.

**W-Q2 — Recast the Relation as a container-state transition.**

- Keep the two current State records as snapshots of the same container.
- Only consider a registered transition Relation type and roles that mean “prepared container state” → “container filled/storing water state”.
- The source supports the procedural sequence (clean/sanitize, dry, fill), but the current snapshots do not themselves contain timestamps. Do not claim an exact time or observed transition unless separately sourced.
- Create/align a Relation-specific Context with exact target/frame references.

This option changes the Relation's meaning from “container for water” to “transition between container states”; it must not be done by merely relabeling the existing roles.

**W-Q3 — Preserve but exclude.**

- Keep both State records and the existing Relation unchanged in the canonical corpus.
- Leave the Relation HOLD and exclude it from the first-edition release allowlist until the model is corrected or independently accepted.

No option is selected by this packet. The earlier acceptance of preserving the Relation is respected: no deletion is proposed or performed.

## 4. Cross-item release boundaries

- Both items remain HOLD.
- No source, claim, event, object, state, relation, context or scope was changed.
- No new Event or water Object/State record was created.
- No Relation was promoted to INCLUDE.
- No first-edition allowlist or release package was changed.
- Public availability of FEMA/Ready.gov, CDC or EPA pages does not itself grant blanket reuse permission. Use factual paraphrase and exact attribution; rights review remains item-specific.
- Technical CI cannot decide the semantic model or substitute for owner approval.

## 5. Recommended owner decision sequence

1. Decide E-Q1/E-Q2/E-Q3 for the earthquake Event and dependent Relation.
2. Decide W-Q1/W-Q2/W-Q3 for the water-storage Relation.
3. Only after both decisions, record separate bounded authorizations with exact allowed files/fields, preserved versions and prohibited changes.
4. Implement one bounded change at a time, preserving exact historical records and HOLD status.
5. Re-run affected slice tests, graph/reference checks, exact-version Context/Relation validation and all release CI on one final HEAD.

Until those choices are made, the current canonical records remain unchanged and HOLD.
