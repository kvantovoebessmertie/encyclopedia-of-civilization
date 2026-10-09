# M11 Initial Candidate Gap Audit — 2026-10-09

## Baseline and method

Read-only review performed against the M11 stacked branch baseline `313b5dc663e032da0e7499829fd55aaf2a1ee157` (M10 Human View follow-up), before any M11 content edits. Candidate: `accessibility-basics`, which contains 9 records: 1 Source, 3 Claims, 3 Evidence Use, 1 Context and 1 Scope. The slice was previously introduced in the R18 controlled-slice expansion; it is not new work and must not be recreated.

Reviewed the README, all three Claims, all three linked Evidence Use records, Source, Context, Scope, and the dedicated regression. Reviewed the current coverage registry and editorial-correction authorization registry. This is a desk audit, not a live novice usability study or external peer review.

## Source-fit review

Canonical Source: United Nations, Convention on the Rights of Persons with Disabilities:
https://www.un.org/development/desa/disabilities/convention-on-the-rights-of-persons-with-disabilities.html

Article 9 describes equal access to the physical environment, transport, information and communications, and public facilities/services; it calls for identifying and removing barriers and for States Parties to develop, promulgate and monitor minimum standards and guidelines. The recorded source is relevant to the three introductory claims. It does not certify any particular local building, service, interface or design, and it does not replace checking applicable jurisdiction-specific requirements.

### Claim A — equality and participation

The claim says accessibility is part of enabling persons with disabilities to participate in society on an equal basis. This is supported at introductory level by the Convention's purpose and Article 9. No claim wording change is currently justified by this review.

### Claim B — barriers and independent/equal use

The claim says a barrier-filled environment can limit independent and equal use of objects and services. This is supported at introductory level by Article 9's focus on identifying and eliminating barriers across physical environments, transport, information/communications and public facilities/services. Keep it general; do not treat it as a complete assessment method.

### Claim C — local requirements and applicability

The claim says concrete accessibility requirements depend on the object's purpose, users and applicable jurisdiction. This is a reasonable applicability boundary, but the relationship to the recorded Source should be made explicit: the Convention supplies an international framework and calls for minimum standards/guidelines; it does not itself establish every technical requirement for every local object. This is a confirmed explanatory/boundary debt, not evidence that the Claim is false.

## Confirmed Human View and regression gaps

### M11-ACC-001 — README is not a reader-facing introduction

The README consists of the internal profile pattern, a source label/URL and a generic boundary statement. It does not explain accessibility in Russian for an ordinary reader, provide a bounded example, or help a reader distinguish an international rights framework from local technical criteria.

**Result:** CONFIRMED. Proposed correction: add a concise Russian-language orientation, one clearly illustrative example (not a legal/design test), and a visible boundary against treating the slice as certification of a specific object.

### M11-ACC-002 — Evidence Use descriptions are generic

All three Evidence Use records use the same description: the UN Convention is used to represent the claim without going beyond the material. The descriptions do not identify the distinct source contribution for Claims A, B and C, nor the limits of that support.

**Result:** CONFIRMED. Proposed correction: rewrite the three existing descriptions claim-by-claim. Preserve record IDs, claim/source refs, `supports` roles, provenance, Source identity and canonical URL.

### M11-ACC-003 — Claim C needs a visible international/local boundary

The Claim itself is already bounded by object, users and jurisdiction. The current Evidence Use does not explain that the Convention establishes an international framework and calls for standards/guidelines, while specific technical/legal criteria must be verified in the applicable context.

**Result:** CONFIRMED explanatory debt. Proposed correction: clarify the existing Evidence Use description first; change the Claim only if a separate post-correction review shows that the current wording still implies direct specification of local technical criteria. No automatic Claim rewrite is authorized by this audit.

### M11-ACC-004 — dedicated regression protects shape, not meaning

The existing test protects the 9-record shape, record types, source count, provenance and claim/evidence linkage. It does not protect claim-specific evidence explanations, the international/local boundary, Russian-facing orientation, or the non-certification limit.

**Result:** CONFIRMED. Proposed correction: preserve all current assertions and add targeted content assertions after the correction scope is explicitly authorized.

## Relation and structure checks

- The known cross-slice Relation `REL-CROSS-MANUFACTURING-HUMAN-FACTORS` concerns manufacturing and human factors; it does not justify adding an accessibility Relation by topical proximity.
- No new Relation is justified by this candidate audit. The permitted Relation delta remains zero.
- No record, source, context, scope, Relation, record type or slice addition/deletion is proposed.
- The candidate's 9-record shape and the corpus coverage baseline are unchanged at this audit stage.
- The current `RELEASE/EDITORIAL-CORRECTION.json` does not authorize M11 corrections to `accessibility-basics`; do not edit the slice before a separate exact-file authorization is recorded.

## Prior-work / duplicate check

The prior M11 audit records identify `accessibility-basics` as an R18 slice and previously flagged generic Evidence Use, an English-only README and structure-only regression. Those findings are consistent with this read-only recheck; this file revalidates them against the newer M10 Human View baseline rather than treating the old branch's CI or acceptance state as current. No evidence was found that the accessibility-specific explanatory debt has already been resolved in M1–M10.

## Candidate decision and proposed next step

**INCLUDE `accessibility-basics` for a bounded M11 correction, subject to a separate authorization.**

Proposed exact content/test surface:
1. `CONTENT/vertical-slices/accessibility-basics/README.md`
2. `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-A.json`
3. `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-B.json`
4. `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-C.json`
5. `REFERENCE/tests/test_content_accessibility_basics_vertical_slice.py`
6. `RELEASE/EDITORIAL-CORRECTION.json` — only the required M11 authorization entry.
7. M11 audit/debt documents required to record the authorization and post-correction result.

The Claim C file is **not** in the initial proposed correction list; keep its current wording unless the authorized post-correction review establishes a concrete reason to change it. Do not edit `ergonomics-basics` or `human-factors-basics` in this candidate pass. No new Source is required by source-count quota; no new Relation or record is justified.

**Acceptance status: OPEN.** No content correction has been implemented or accepted. Next step is to record the exact correction authorization and update the unified debt map before editing the authorized files.
