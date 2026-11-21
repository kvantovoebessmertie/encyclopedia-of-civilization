# First Edition — Relation Context Isolation Reconciliation and Exact-Head Gate

Date: 2026-11-20  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR: #22 — OPEN · DRAFT · NOT MERGED  
Branch: `mvp-public-contribution-design-2026-10-11`  
Verified HEAD before this report: `02285d67d3926d426b2d7d954e066068471c321e`

## 1. Exact-head CI result

All four required workflows completed successfully on the same verified HEAD `02285d67d3926d426b2d7d954e066068471c321e`:

| Workflow | Run ID | Result |
|---|---:|---|
| Reference implementation tests | 44692960238 | PASS |
| MVP Contribution Form Browser Tests | 44692960004 | PASS |
| Release Conformance Gate | 44692960140 | PASS |
| Offline Edition | 44692960145 | PASS |

These are exact-commit results, not a mixture of runs from different revisions. A subsequent documentation commit will require a fresh exact-head gate; the results above must not be carried forward as proof for that later commit.

## 2. Repository boundary verification

At verification time:
- PR #22 head branch resolves to `02285d67d3926d426b2d7d954e066068471c321e`.
- PR #22 base is `main`; state is OPEN, draft is true, merged is false.
- `main` resolves to `d58289f319993ede5294a46f4741a506fd2fd710`.
- The PR branch head and `main` are distinct; no merge or main update was performed.

## 3. Context architecture decision — implementation reconciliation

The owner-approved Option A is implemented as target-specific Context isolation:
- 61 new Context Records were created for the 61 cross-slice Relations that previously reused the shared Context.
- The original `CTX-CROSS-SLICE-LINKAGE@1` remains attached only to its own target Relation.
- Each of the 61 migrated Relations was versioned and now references its own Context; each new Context's `target_ref` identifies that exact Relation ID and new version.
- The separate water-storage Context and Relation were intentionally not changed.
- Relation participants, roles, direction, relation types and semantic propositions were preserved by the isolation migration.
- The corpus-wide regression test checks all 63 Relations, requires target-specific Context/frame alignment for every Relation except the separately held water-storage Relation, and checks the inventory count of 63.

This implements the lowest-risk target-specific Context strategy without introducing a new Core Frame entity or changing the Relation schema. It is consistent with `STANDARD/013-RELATION.md` §11, which permits Context as a component of an applicable frame, and preserves `STANDARD/015-CONTEXT.md`'s distinction that Context is not universally equivalent to Frame and does not select a frame automatically. Here the Context role is explicit in `frame_ref`, and target compatibility is checked against the exact Relation.

### Historical audit reconciliation

The 2026-11-19 reports identifying the shared-Context fan-out were accurate for their inspection HEADs. Their specific finding that one target-relative Context was silently reused across 62 Relations is superseded by the 2026-11-20 isolation implementation and the exact-target regression coverage. The older reports are retained as historical evidence; they are not silently rewritten.

The separate water-storage Context remains an exception and is not declared conformant by this reconciliation.

## 4. Earthquake Event — remains HOLD

At the verified HEAD:
- `EVT-EARTHQUAKE-SHAKING@1` still describes generic felt ground shaking, not a particular identified occurrence.
- Its provenance points only to the general FEMA earthquake-safety publication; no event-specific report or observation is identified.
- The earthquake Relation has been versioned to `REL-CROSS-EARTHQUAKE-AFTERSHOCK@2`; its new target-specific Context correctly targets that exact Relation version.
- The Event's own Context/Scope applicability still needs separate resolution: the existing Event points to Context/Scope Records whose target is a protective-action Claim, not this Event.

Decision: retain the Event and `REL-CROSS-EARTHQUAKE-AFTERSHOCK@2` on HOLD. Do not invent a date, place, magnitude, or occurrence. The aftershock warning Claim remains independently represented with its USGS provenance. Reconsider only if the project chooses a valid general-knowledge representation or supplies a genuine occurrence-specific source/observation and correct Event-target Context/Scope.

## 5. Water-storage State/Relation — remains HOLD

At the verified HEAD:
- `ST-WATER-CONTAINER-SANITIZED@1` and `ST-WATER-CONTAINER-STORED@1` both have `subject_ref=OBJ-WATER-CONTAINER@1`.
- The second State describes the condition of that same container when water is stored; it is not a State of water.
- `REL-CONTAINER-WATER-STORAGE@1` still declares `storage_container_for` with roles `container_state` and `stored_water_state`.
- `CTX-WATER-STORAGE-EMERGENCY@1` still targets `CLM-WATER-STORAGE-CONTAINER@1`, while the Relation and both States use it as a frame component.

Decision: retain the Relation on HOLD. Do not invent a water Object/State, infer a transition between snapshots, or relabel only the Relation while leaving its participants and Context misaligned. A future correction requires an explicit domain model and bounded authorization, or exclusion from release scope.

## 6. Semantic HOLD register and publication boundary

The existing 15 semantic HOLD Relations remain HOLD. The 48 contextual-navigation candidates are not publication approvals. No Relation or Claim is promoted to INCLUDE by this report. No release allowlist, rights clearance, editorial approval, Human View, or public-release decision is created here.

The library/archival preservation and infrastructure-resilience endpoint alternatives remain proposals subject to their existing authorization and evidence constraints. In particular, the Library Claim C alternative requires a new bounded authorization; the infrastructure-specific Claim D candidate still lacks a claim-specific pinpoint locator and a reconciled source-identity basis.

## 7. Next work sequence

1. Re-run the four exact-head workflows after this report commit; accept only runs attached to the resulting new HEAD.
2. Keep the two model-level blockers above on HOLD; resolve them only with supported models and bounded authorization.
3. Continue the 15-HOLD remediation in evidence-ready order, starting with library/archival preservation; obtain authorization before changing the endpoint pair.
4. Reconcile the infrastructure-resilience source identity and pinpoint locator before considering the proposed Claim D endpoint.
5. Preserve independent rights/licensing, editorial ownership, Human View, allowlist and final artifact gates.

**Conclusion:** the shared cross-slice Context fan-out issue is remediated under the owner-approved target-specific model. The exact-head CI at the pre-report HEAD was 4/4 PASS. Earthquake Event identity, water-storage State/Relation alignment, 15 semantic HOLDs, and independent publication governance remain open. PR #22 remains Draft and unmerged; `main` remains unchanged.
