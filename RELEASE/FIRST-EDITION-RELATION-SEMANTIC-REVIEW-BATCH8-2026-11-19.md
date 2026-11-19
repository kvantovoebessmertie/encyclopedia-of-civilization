# First Edition — Cross-Slice Relation Semantic Review — Batch 8

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `e7fd4e81e7e7f520e5ec5bab2dda074a6472627f`

## Scope and method

Eight previously unreviewed Relations were fetched and reviewed. All participant records and provenance Sources were fetched from their owning slices. This batch deliberately includes mixed participant types: Claim, Event, and State. The container-storage Relation's separate Context frame and object subject were also fetched to test whether its endpoints and frame describe the same modeled entity.

No canonical JSON, allowlist, or publication decision was changed. This is not a release approval; participant Claims remain HOLD.

## Exact verification

- 8/8 Relation records: exact ID, version, and `record_type=relation`.
- 16/16 participant references fetched and checked: 13 Claims, 1 Event, and 2 State records; all exact IDs, versions, and types match the Relation participants.
- 15 Relation/participant provenance Source edges fetched; 14 unique Source records (the risk-assessment Source is shared by two Relations).
- Source identities and versions match the participant provenance and Relation `created_from` references.
- Seven Relations reference `CTX-CROSS-SLICE-LINKAGE@1`.
- `REL-CONTAINER-WATER-STORAGE@1` instead references `CTX-WATER-STORAGE-EMERGENCY@1`; the Context and `OBJ-WATER-CONTAINER@1` were fetched and exact-verified.

## Relation-by-relation semantic findings

| Relation/version | Exact participant pair | Semantic assessment | Release-use disposition |
|---|---|---|---|
| `REL-CROSS-DISASTER-BUILDING-SERVICES@1` | Disaster Recovery Claim A; Building Services Engineering Claim A | Recovery requires coordinated restoration and development of affected communities; building-services engineering helps make buildings safe, healthy, and usable. The cross-reference is useful for recovery planning, but the selected Claims do not specify building services as a recovery activity or priority. | ACCEPT WITH RESTRICTION — contextual navigation only; do not imply that building services alone constitute recovery planning; retain HOLD for publication eligibility. |
| `REL-CROSS-EARTHQUAKE-AFTERSHOCK@1` | Earthquake Shaking Event; Aftershock Expectation Claim | The directed sequence from earthquake shaking to the subsequent possibility of aftershocks is semantically coherent and preserves the Event/Claim distinction. However, the Event record has only a generic description (“ground shaking during an earthquake”) and status `reported`; it contains no occurrence-specific attribution beyond a generic present-tense description and the status `reported`; its provenance is a general FEMA earthquake-safety source, not an identified report/observation of this particular shaking occurrence. Exact time and location are not universal requirements under `STANDARD/009-EVENT.md` §2, so their absence alone is not the defect. The issue is that the record does not establish a definite occurrence represented as having happened (E-01) or sufficient event attribution (E-03); it reads as a generic event class/template. | HOLD — do not publish as a concrete Event instance until the record identifies a definite reported/observed occurrence or the model explicitly represents this as an event type/class rather than an occurrence. The Relation does not establish that aftershocks will occur in every instance. |
| `REL-CROSS-ETHNOBOTANY-AGRIFOOD@1` | Ethnobotany Claim B; Agrifood Systems Claim A | Local crop systems may support crop diversity and cultural practices; agrifood systems include people, activities, investment, and decisions in food/agricultural production and delivery. The intersection is direct and useful, though the broad agrifood Claim does not itself explain ethnobotanical practice. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |
| `REL-CROSS-FOOD-PUBLIC-HEALTH@1` | Food Security Claim D; Public Health Claim A | This Relation was already reviewed in Batch 4 and is intentionally not re-reviewed here. Batch 4 retained it on HOLD because the selected public-health endpoint is too generic for the named food-security/population-health link. | Previously reviewed — HOLD remains unchanged. |
| `REL-P11-RISK-COMMUNICATION@1` | Risk Analysis Claim B; Public Risk Communication Claim A | Risk-assessment results support decisions about response to identified risks; risk communication helps establish shared understanding and support risk-reduction action. The decision/communication interface is direct. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; do not imply that communication itself constitutes risk assessment or guarantees risk reduction; retain HOLD for publication eligibility. |
| `REL-P11-RISK-SYSTEMS-THINKING@1` | Risk Analysis Claim A; Systems Thinking Claim A | Risk analysis requires defining objectives, scope, assumptions, limits, and information sources; systems thinking examines interactions among elements, dependencies, and processes. The link is a coherent methodological lens for defining the system and its risk boundaries. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; retain HOLD for publication eligibility. |
| `REL-CONTAINER-WATER-STORAGE@1` | Sanitized Container State; Stored Water State | Both State records refer to the same `OBJ-WATER-CONTAINER@1` and emergency-water-storage Context. The states describe a cleaned/prepared container and water stored in it. Both State records have `subject_ref=OBJ-WATER-CONTAINER@1`; the second State describes the condition of that same container when water is stored, not a State of the water itself. Thus `relation_type=storage_container_for` and the roles `container_state` / `stored_water_state` do not match the actual participant identities. The Context's `target_ref` points to `CLM-WATER-STORAGE-CONTAINER@1`, not either State or this Relation. No temporal ordering is recorded, so the pair must not be silently reinterpreted as a state transition. | HOLD — either model a distinct water Object/State if the intended meaning is container-for-water, or remove/replace the redundant Relation if both endpoints are snapshots of the same container; do not infer a transition without temporal evidence; resolve Context target applicability before release. |
| `REL_M3_FIRE_SAFETY_EMERGENCY_MANAGEMENT@1` | Fire Safety Claim B; Emergency Management Claim A | Fire-safety measures include prevention, detection, suppression, compartmentation, evacuation, and response; emergency management includes preparedness, response, resource coordination, and recovery. The domains overlap directly in planning and response, while remaining distinct disciplines. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; preserve the distinction between fire-specific controls and all-hazard emergency management; retain HOLD for publication eligibility. |
| `REL-CROSS-WATER-CHEMICAL@1` | Water Chemical Limit Claim; Chemical Water No-Boil Claim | Both Claims state that boiling does not make chemically contaminated/toxic water safe. The relationship is exact and safety-critical, but the Claims substantially overlap and are based on two CDC pages from the same institution. The Relation is a navigation/consistency link, not independent corroboration. | ACCEPT AS CONTEXTUAL NAVIGATION ONLY; flag near-duplicate content and shared institutional provenance for editorial review; retain HOLD for publication eligibility. |

## Cross-cutting frame limitation

The seven cross-slice Relations in this batch reference `CTX-CROSS-SLICE-LINKAGE@1`, whose `target_ref` names `REL-CROSS-WATER-CHEMICAL@1` specifically. The Water Chemical Relation itself is therefore the named target, but the Context's applicability to every other Relation is not established by the shared frame ID/version alone. Do not treat the target as a wildcard. The container-storage Relation uses a different Context whose target is a Claim, not the Relation or its State endpoints. Context applicability must be resolved separately for both patterns.

## Result

- Structurally exact: 8 Relations and 16 participant records (13 Claims, 1 Event, 2 States).
- Provenance: 15 Source edges, 14 unique exact-version Source records; participant provenance matches Relation provenance.
- Semantic dispositions: 6 contextual-navigation candidates (two with explicit restrictions); 2 HOLD (generic Event instance and misaligned State/Relation/Context modeling).
- The already reviewed food/public-health Relation is recorded as a cross-check only and is not counted as a ninth review.
- No canonical records changed; no Claim or Relation promoted to INCLUDE.

## Remaining work

Continue the final unreviewed Relations. Keep event-instance grounding, state/object modeling, Context applicability, and semantic relationship quality as separate gates. Contextual acceptance is not release approval.
