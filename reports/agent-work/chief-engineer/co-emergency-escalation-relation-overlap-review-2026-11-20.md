# CO Heating / Generator Emergency Escalation — Focused Claim-Overlap Review

- **Agent:** chief-engineer
- **Task:** Focused WP1 endpoint-overlap and relation-semantics review
- **Date (UTC):** 2026-11-20
- **Repository:** kvantovoebessmertie/encyclopedia-of-civilization
- **Branch:** mvp-public-contribution-design-2026-10-11
- **Starting HEAD:** 2db806e7bc1e2c8158707d029c28d10d41afad30
- **Status:** VERIFIED — exact endpoints and official CPSC/CDC guidance inspected; report-only

## 1. Request and acceptance criteria

Continue WP1 by examining the known overlapping emergency Claims in `REL-CROSS-CO-EMERGENCY-ESCALATION@2`. Determine whether the relation represents an independent mechanism or only a repeated emergency action in two exposure contexts. Preserve all canonical records and existing publication/HOLD controls.

## 2. Scope

- **In scope:** Relation @2, Context @1, both participant Claims, both Evidence Use and Source records, and official CPSC/CDC emergency guidance.
- **Out of scope:** Claim consolidation, Claim rewriting, Source/Evidence Use changes, Relation/Context versioning, clinical advice changes, candidate disposition, rights clearance, and release/merge actions.

## 3. Work performed

Fetched exact participant and evidence records at the starting HEAD. Compared the two Claim statements and the supporting material. Cross-checked current official CPSC guidance for a sounding CO alarm and symptoms, and current CDC/NIOSH generator-related CO guidance.

## 4. Files changed

| Path | Change | Reason |
|---|---|---|
| `reports/agent-work/chief-engineer/co-emergency-escalation-relation-overlap-review-2026-11-20.md` | Added report-only overlap review | Record the semantic distinction between common emergency action and distinct exposure contexts |

## 5. Exact canonical graph

At starting HEAD `2db806e7bc1e2c8158707d029c28d10d41afad30`:

- `REL-CROSS-CO-EMERGENCY-ESCALATION@2`
  - `relation_type`: `shared_carbon_monoxide_emergency_escalation`
  - participants: `CLM-CO-HEATING-EMERGENCY@1` and `CLM-GENERATOR-CO-ALARM-EMERGENCY@1`
  - frame: `CTX-REL-CROSS-CO-EMERGENCY-ESCALATION@1`, correctly targeting Relation @2.
- Heating Claim: on a CO alarm or possible CO-poisoning symptoms, immediately go to fresh air, seek emergency medical help, and do not return until safety is checked.
  - Its Evidence Use references CPSC and describes the instruction to go outside, call emergency services, and not re-enter until authorized.
- Generator Claim: the same action when an alarm or symptoms occur during generator operation, with the same no-return-until-safe instruction.
  - Its Evidence Use references CDC and describes immediate evacuation and emergency assistance.

The Claim texts are nearly duplicative. The only substantive endpoint distinction is the explicit generator-operating context in the second Claim versus the general heating / residential CO context in the first.

## 6. Official-source cross-check

### 6.1 CPSC — CO alarm and suspected exposure

Official locator: https://www.cpsc.gov/safety-education/safety-guides/carbon-monoxide/carbon-monoxide-fact-sheet

CPSC says a sounding CO alarm should not be ignored: occupants should immediately move outside to fresh air, call emergency services/fire department/911, and not re-enter until responders permit it. For suspected symptoms even without an alarm, CPSC instructs people to get outside immediately and contact emergency/medical services.

### 6.2 CDC — generator-specific CO exposure

Official locator: https://www.cdc.gov/carbon-monoxide/about/index.html

CDC identifies portable generators as a CO source, says generators must never be used inside a home or garage (even with doors/windows open), and recommends operating them outdoors more than 20 feet from windows, doors and vents.

### 6.3 CDC / NIOSH — immediate response to CO symptoms at work

Official locator: https://www.cdc.gov/niosh/carbon-monoxide/about/index.html

CDC/NIOSH advises users who have CO symptoms to turn off equipment, go outdoors or to uncontaminated air, and call 911 or the local emergency number for medical attention. This source adds a work-equipment context and the step of turning off the equipment when safe to do so.

## 7. Adjudication

**Finding:** both sources support the shared core emergency response (fresh air, emergency assistance, no unsafe re-entry), but the Relation does not establish a distinct causal or technical mechanism between heating systems and generators. It connects two scenario-specific Claims that repeat the same response pattern.

The endpoints are not wholly interchangeable:
- The heating/residential endpoint is triggered by a household CO alarm or symptoms and addresses residential fuel-burning appliances generally.
- The generator endpoint is triggered in the context of generator operation and is supported by generator-specific CDC guidance.
- The generator context has prevention details that are not represented in the emergency Claim itself (outdoor placement, distance from openings, no indoor/garage use).
- The current Relation can at most serve as contextual navigation to a shared emergency response across two CO exposure scenarios. It should not imply that the two exposure sources, prevention controls, or underlying risk conditions are identical.

**Disposition:** do not promote this Relation as a substantive cross-domain mechanism. Retain existing publication and HOLD controls pending independent editorial comparison. If a navigation-only treatment is considered, the relation type/label and surrounding editorial text must explicitly describe shared emergency escalation across distinct CO exposure scenarios. No canonical change is authorized by this review.

## 8. Rights and reuse boundary

Only official source identities, links, and independently worded summaries are used. No CPSC/CDC text, images, charts, or other expressive content is reproduced. No rights decision is closed.

## 9. Verification

| Check | Result | Notes |
|---|---|---|
| Exact Relation/Context | VERIFIED | Relation @2 and Context @1 |
| Exact Claims | VERIFIED | Participant wording compared directly |
| Exact Evidence Use/Sources | VERIFIED | CPSC and CDC references confirmed |
| Official CPSC/CDC cross-check | VERIFIED | Current emergency guidance inspected |
| Canonical changes | NONE | Report-only |
| CI | NOT RUN | No CI PASS claimed |

## 10. Unresolved issues and risks

- No independent emergency-medicine / fire-safety reviewer was engaged.
- The two Claims overlap substantially; no editorial decision to consolidate or preserve both was made.
- No new prevention Claim was added to the generator endpoint.
- No Relation/Context version, candidate disposition, rights decision, allowlist or publication decision changed.

## 11. Recommendation and acceptance

- **Recommendation:** preserve the current records and HOLD; treat the link as a possible contextual-navigation aid only, not a substantive causal relation. Before any canonical change, obtain an independent editorial comparison and exact owner authorization.
- **Acceptance status:** CONDITIONAL — overlap review complete; editorial decision remains open.
- **Reason:** common emergency response is well supported, but the relation adds navigation rather than a new cross-domain mechanism.

## 12. Handoff

- **Draft PR:** https://github.com/kvantovoebessmertie/encyclopedia-of-civilization/pull/22
- **Report path:** `reports/agent-work/chief-engineer/co-emergency-escalation-relation-overlap-review-2026-11-20.md`
- **Next owner/action:** decide whether to retain the pair as separate scenario Claims with navigation-only linkage or pursue a bounded editorial consolidation review.

## 13. Integrity statement

- No canonical Claim, Evidence Use, Source, Relation, Context or Scope changed.
- No candidate disposition, INCLUDE/EXCLUDE, HOLD, allowlist, licence, permission, or publication state changed.
- PR #22 remains Draft and unmerged; `main` is untouched.
