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


## Revalidated candidate: ergonomics-basics

This slice has 9 records: one CDC/NIOSH Source, three Claims, three Evidence Use, Context and Scope. The recorded source is reachable and directly states that ergonomics fits work tasks and demands to worker capabilities, describes risk factors including force, repetition, awkward postures and vibration, and defines an ergonomics program as a systematic process for identifying, analyzing and controlling workplace risk factors. Source: https://www.cdc.gov/niosh/ergonomics/about/index.html

- Claim A is bounded and consistent with the source's definition of ergonomics.
- Claim B is consistent with the source's listed risk factors, though the current Evidence Use does not explain that connection.
- Claim C says programs include identifying risk factors, choosing controls and evaluating their effectiveness. The recorded overview directly supports identifying, analyzing and controlling risk factors, but does not itself describe effectiveness evaluation in that definition. This is a confirmed source-scope mismatch at the current wording. Narrow Claim C to the directly described identify/analyze/control process; do not infer a full evaluation protocol from this locator.
- All three Evidence Use descriptions are identical generic statements and do not explain the distinct claim/source connection.
- The README is mostly English and centers a “Definition of Done” schema rather than a Russian-facing reader introduction. It does not provide a simple explanation or clear educational/workplace-assessment boundary.
- The dedicated regression checks structure and linkage only; it does not protect the source-specific content or the Claim C boundary.

**Confirmed findings:** M11-ERG-001 (Human View/readability), M11-ERG-002 (generic Evidence Use), M11-ERG-003 (Claim C overstates the recorded overview), M11-ERG-004 (regression does not protect the confirmed content requirements).

## Revalidated candidate: human-factors-basics

This slice has 9 records: one NASA Source, three Claims, three Evidence Use, Context and Scope. The Claims cover human-system interaction, effects of human perception/attention/decision limitations, and whole-system design. These are plausible introductory themes, but source-specific boundaries need to be visible.

- All three Evidence Use descriptions repeat the same generic statement and do not explain the distinct contribution or limitations for each Claim.
- The README is partly Russian but gives no plain-language explanation of the concept; its main body is a source label, URL and internal “Definition of Done” schema.
- The dedicated regression checks shape and linkage, not the claim-specific explanation, domain boundary or user-facing introduction.
- The exact canonical locator recorded in the Source, https://www.nasa.gov/reference/human-factors/, could not be independently retrieved in this review. A related official NASA page on Human Factors & Performance is available at https://www.nasa.gov/reference/jsc-human-factors-performance/ and discusses human capabilities/limitations and human-system integration, but it is not substituted for the recorded Source. This remains a retrieval/source-verification limitation, not proof that the recorded URL is broken. No Claim should be expanded and no Source identity/URL should be changed in this pass. If post-correction source fit cannot be established against the recorded source or its authoritative redirect, stop and request a separate scope amendment.
- Preserve the existing cross-slice Relation `REL-CROSS-MANUFACTURING-HUMAN-FACTORS` exactly. Topical proximity does not justify a new Relation.

**Confirmed findings:** M11-HF-001 (Human View/readability), M11-HF-002 (generic Evidence Use), M11-HF-003 (regression does not protect confirmed content boundaries). **Limitation:** source locator needs a careful post-correction verification; this is not a confirmed source failure.

## Cluster-level Relation and structure decision

The current review does not justify adding, deleting or editing any Relation. Preserve the known `REL-CROSS-MANUFACTURING-HUMAN-FACTORS` record, participants, direction, frame and provenance exactly; permitted Relation delta is zero. No Source, Context, Scope, record type or slice addition/deletion is proposed. The corpus coverage baseline is unchanged.

## Revised candidate decision and proposed correction scope

**INCLUDE all three existing slices for controlled M11 maturation, subject to explicit correction authorization:**
1. `accessibility-basics`
2. `ergonomics-basics`
3. `human-factors-basics`

Proposed exact content/test surface:
- `CONTENT/vertical-slices/accessibility-basics/README.md`
- `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-A.json`
- `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-B.json`
- `CONTENT/vertical-slices/accessibility-basics/records/EU-ACCESSIBILITY_BASICS-C.json`
- `REFERENCE/tests/test_content_accessibility_basics_vertical_slice.py`
- `CONTENT/vertical-slices/ergonomics-basics/README.md`
- `CONTENT/vertical-slices/ergonomics-basics/records/CLM-ERGONOMICS_BASICS-C.json`
- `CONTENT/vertical-slices/ergonomics-basics/records/EU-ERGONOMICS_BASICS-A.json`
- `CONTENT/vertical-slices/ergonomics-basics/records/EU-ERGONOMICS_BASICS-B.json`
- `CONTENT/vertical-slices/ergonomics-basics/records/EU-ERGONOMICS_BASICS-C.json`
- `REFERENCE/tests/test_content_ergonomics_basics_vertical_slice.py`
- `CONTENT/vertical-slices/human-factors-basics/README.md`
- `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-A.json`
- `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-B.json`
- `CONTENT/vertical-slices/human-factors-basics/records/EU-HUMAN_FACTORS_BASICS-C.json`
- `REFERENCE/tests/test_content_human_factors_basics_vertical_slice.py`
- `RELEASE/EDITORIAL-CORRECTION.json` — only the explicit M11 authorization entry.
- M11 audit/authorization/debt documents required to record findings and post-correction verification.

Do not add Sources or Relations by quota. Preserve all record IDs, provenance, canonical source identities/URLs, Claim/Evidence Use references, evidence roles, Context/Scope records and target refs, and corpus coverage. The NASA locator limitation remains explicit. No content correction has yet been implemented or accepted.

**Acceptance status: OPEN.** Next: record the exact correction authorization and unified debt map before editing any authorized content.
