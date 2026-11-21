# First Edition — Relation Architecture Remediation Decision Package

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
Purpose: provide the smallest standards-conformant resolution path for the remaining Relation/Context blockers.  
Status: **RECOMMENDATION FOR OWNER REVIEW — no architecture choice or canonical edit is authorized by this document.**

## 1. Correct normative interpretation

This package consolidates the findings in:

- `STANDARD/013-RELATION.md` §§10–12;
- `STANDARD/015-CONTEXT.md` §§4–5, 12–13, 103–106, and CTX-01 onward;
- `IMPLEMENTATION/015-CONTEXT.md` §§4, 7, 22–27, and 29;
- `IMPLEMENTATION/005-RECORD-SCHEMA.json`;
- `REFERENCE/src/encyclopedia_reference/references.py`;
- `REFERENCE/src/encyclopedia_reference/semantic_rules.py`;
- `REFERENCE/tests/test_content_cross_slice_linkage_vertical_slice.py`.

Important correction: the standards do **not** require a universal `record_type=frame`. `STANDARD/013-RELATION.md` §11 explicitly allows Context to be one component of a Relation's applicable frame. `STANDARD/015-CONTEXT.md` §§12–13 says Context is not universally equivalent to Frame and does not select a frame automatically. The implementation must preserve that role distinction; it must not reject every Context-valued `frame_ref` by type alone.

The established defect is narrower and stronger: a Context Record is target-relative, but its single `target_ref` identifies only one Relation. Reuse by other Relations is not justified or validated. A shared reference alone does not establish Context transferability or applicability.

## 2. Recommended resolution: target-specific Context Records

**Recommendation: use one Context Record per Relation wherever the Context is materially specific to that Relation.**

Why this is the lowest-risk path:

1. It follows the existing target-relative Context Standard without inventing a new Core Entity.
2. It preserves the current Relation schema and its `frame_ref` field.
3. It does not require defining a new universal Frame Record type; the applicable frame can include the target-specific Context component.
4. It avoids introducing an unmodeled group/collection target or an undocumented Context inheritance/transfer rule.
5. It is testable by exact target identity and version.

### Exact corpus impact

The inventory contains 63 Relations:

- 62 Relations reference `CTX-CROSS-SLICE-LINKAGE@1`.
- That Context's exact target is `REL-CROSS-WATER-CHEMICAL@1`.
- Therefore the existing Context can remain attached to that one target Relation.
- Under the recommended per-Relation path, **61 additional Context Records** would be needed for the other 61 Relations currently reusing it.
- `REL-CONTAINER-WATER-STORAGE@1` is a separate case and is not included in this 61-record migration.

The 61 Context records must each have:
- a unique exact `record_id` and version;
- `record_type=context`;
- `content.target_ref` equal to the exact owning Relation ID and version;
- independently reviewed `context_content` appropriate to that Relation;
- explicit epistemic status where material;
- provenance that identifies the basis for the Context content;
- no implied evidence, causality, Claim support, or publication eligibility.

Do not mechanically copy one Context record 61 times without checking whether its factual/contextual content and provenance apply to each target. The text may be structurally similar, but its target, applicability rationale and provenance must be target-specific.

### Alternative requiring an explicit architecture rule

A shared Context may be retained only if the project formally specifies and validates an explicit multi-target/transferability mechanism consistent with Standard 015. That mechanism must identify the full target set or justified target mapping, preserve uncertainty and partial applicability, and prevent automatic transfer to all same-domain Relations. The current single `target_ref` does not provide that mechanism.

A group-level Context is another possible design only if the target is an explicit, resolvable group/collection Record with defined membership and versioning. No such group target has been identified in the current implementation; do not treat one Relation as a group proxy.

## 3. Required validator and test contract

After owner approval, add or extend tests with these assertions:

1. **Exact target match:** when a Relation's `frame_ref` resolves to a Context Record, its `target_ref` must identify that Relation unless an explicit approved transfer/multi-target rule applies.
2. **No implicit fan-out:** a Context targeting Relation A cannot silently contextualize Relation B merely because both Relations reference the same Context ID/version.
3. **Positive per-target case:** a Context targeting Relation A and referenced by Relation A passes.
4. **Explicit transfer case:** a Context targeting another target passes only when the approved transfer/applicability record is resolvable and covers the exact Relation/version.
5. **Epistemic fidelity:** unknown, partial, reported, inferred, or disputed Context status is not silently upgraded during reuse.
6. **Applicable-frame semantics:** `frame_ref` must resolve and contribute to a coherent applicable frame under Relation Standard §11. Do not require a separate `record_type=frame` unless a future approved Standard introduces one.
7. **Scope separation:** Context target compatibility must not be confused with Scope membership or Evidence Use.
8. **Offline parity:** Reference Tests, Release Conformance Gate, and Offline Edition must enforce the same rules.

## 4. Separate blocker A — earthquake Event attribution

Canonical records:

- `EVT-EARTHQUAKE-SHAKING@1`;
- `REL-CROSS-EARTHQUAKE-AFTERSHOCK@1`;
- `CLM-AFTERSHOCK-EXPECT@1`.

The Event says only “ground shaking is felt during an earthquake”, assigns `event_class=hazardous_natural_event`, and sets `event_status=reported`. Its only provenance is a general FEMA earthquake-safety source. No particular reported/observed shaking occurrence is identified. A second target-linkage issue is present: the Event's `context_ref` and `scope_ref` point to `CTX-EARTHQUAKE-SHAKING@1` and `SCP-EARTHQUAKE-SHAKING@1`, but both of those Records target `CLM-EARTHQUAKE-DROP-COVER-HOLD@1`, not the Event. Their reuse on the Event therefore also needs an explicit target-applicability basis; it cannot be inferred from shared subject matter.

Normative boundary: `STANDARD/009-EVENT.md` §§1–2 and E-01/E-03 require a definite occurrence represented as having happened, with defined event content and sufficient event attribution. Exact time and location are **not** universal required fields; their absence alone is not the defect. The problem is the lack of a particular occurrence/report/observation basis.

Recommended resolution options:

- **Preferred if the record is intended as general guidance:** do not represent the generic shaking description as a concrete Event instance. Recast the general point in an appropriate Claim/knowledge representation, or remove this Relation from release scope. Keep the aftershock warning Claim independently governed by its own Evidence Use.
- **If an actual occurrence is intended:** add occurrence-specific attribution supported by an actual event report/observation, preserving unknown time/location where they are genuinely unknown. Do not invent date, place, magnitude, or source observation.
- **If the project intends a reusable event class/type:** obtain an approved model for class-level event representation; do not use an occurrence-level Event record as a class definition by implication.

Until one route is approved and supported, retain the Event and Relation on HOLD. Resolve the Event's Context/Scope target applicability at the same time; do not silently transfer Claim-targeted Context or Scope to the Event.

## 5. Separate blocker B — container/water State relation

Canonical records:

- `OBJ-WATER-CONTAINER@1`;
- `ST-WATER-CONTAINER-SANITIZED@1`;
- `ST-WATER-CONTAINER-STORED@1`;
- `CTX-WATER-STORAGE-EMERGENCY@1`;
- `CLM-WATER-STORAGE-CONTAINER@1`;
- `REL-CONTAINER-WATER-STORAGE@1`.

Both State records point to the same subject, `OBJ-WATER-CONTAINER@1`. The second State describes the condition of that same container when water is stored; it is not a State of the water. Yet the Relation type is `storage_container_for` and its roles are `container_state` and `stored_water_state`. Its Context targets the Claim, not either State or the Relation.

Recommended resolution options:

- **Preferred if the intention is container-for-water:** create or identify a distinct water Object/Record and, if necessary, a State of that water, then link the container Object and water Object with the correctly typed Relation. This requires source support and bounded authorization; do not infer a water entity from the current two State records.
- **If the intention is to compare two snapshots of the same container:** use a Relation whose semantics explicitly describe the relationship between those State representations, and provide the temporal/identity basis required by Standard 011/013. Do not call it `storage_container_for` and do not infer a transition from two snapshots alone.
- **If the extra Relation adds no information:** remove it from the release candidate/allowlist through an authorized decision; the State `subject_ref` links already identify the common container.

Until resolved, retain the Relation on HOLD.

## 6. Work sequence after owner decision

1. Approve the Context strategy (recommended: 61 target-specific Context Records).
2. Issue bounded authorization for the exact Relation/Context files and test/validator files.
3. Implement the Context records and exact target references; preserve all participant IDs, Relation semantics, Claim decisions and rights states.
4. Add regression tests and validator enforcement; run full Reference Tests.
5. Resolve the Event model and the State/Relation model separately under bounded authorizations.
6. Run Release Conformance Gate and Offline Edition at the final exact PR head.
7. Keep all related Claims/Relations HOLD until their independent evidence, rights, editorial and Human View gates are satisfied.

## 7. Decision table

| Decision | Recommendation | Can be decided by automation? |
|---|---|---|
| Shared Context strategy | Target-specific Context per Relation | No — architecture owner approval |
| Add new Frame Record type | Do not add unless a future Standard requires it | No — architecture owner approval |
| Earthquake Event | Recast generic guidance or provide a real occurrence basis | No — domain owner/source evidence |
| Container/water Relation | Add distinct water participant, correct State semantics, or remove redundant Relation | No — domain owner and bounded authorization |
| Publication status | Keep HOLD | No automatic promotion |

## 8. Change boundary

This decision package changes documentation only. It does not modify canonical JSON, standards, schema, resolver, validator, tests, allowlists, publication states, or release gates. It does not select an owner, approve a licence, or authorize release.

**Current disposition:** semantic audit 63/63 complete; these three modeling/applicability issues remain explicitly open; PR #22 remains Draft and unmerged.
