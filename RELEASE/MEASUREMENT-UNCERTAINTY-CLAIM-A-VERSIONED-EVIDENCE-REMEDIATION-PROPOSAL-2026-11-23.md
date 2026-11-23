# Measurement Uncertainty — Claim A Versioned Evidence Remediation Proposal

Date: 2026-11-23  
Target branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: OPEN / DRAFT / NOT MERGED  
Inspection HEAD: `00d503154bdd8ec33fdf5b1442c1f4b02921fb15`  
Status: PROPOSAL ONLY — NOT AUTHORIZED FOR CANONICAL WRITES

## 1. Purpose and strict boundary

This proposal addresses only the evidence trail for the existing Claim A:

> Результат измерения должен интерпретироваться вместе с оценкой его неопределённости.

It prepares a bounded, versioned evidence correction. It does not authorize edits to canonical records, does not rewrite the Claim, does not resolve the full Measurement Uncertainty slice, and does not approve publication.

**Disposition remains HOLD.** Existing `publication_status: published` fields are not first-edition admission decisions.

## 2. Exact canonical baseline re-fetched

| Record | Version | Type | Blob SHA |
|---|---:|---|---|
| `CLM-MEASUREMENT_UNCERTAINTY_BASICS-A` | 1 | Claim | `c352d4f41e4a64cfc8747926c5a74bc3cfa8e93f` |
| `EU-MEASUREMENT_UNCERTAINTY_BASICS-A` | 1 | Evidence Use | `34d962fe7a0f96163cc81e9f3e8a30fed273e0c5` |
| `SRC-MEASUREMENT_UNCERTAINTY_BASICS` | 1 | Source | `f167d0df955e8ec99a26f64fca9a5a4df49164fd` |
| `CTX-MEASUREMENT_UNCERTAINTY_BASICS` | 1 | Context | `fdfefe7f5632413306291f947e4ff72049fa1bcd` |
| `SCP-MEASUREMENT_UNCERTAINTY_BASICS` | 1 | Scope | `9a38ab3081c7b124a488be68f3d8750b38166806` |

Baseline findings:

- Claim A v1 states that a measurement result should be interpreted together with an assessment of its uncertainty.
- EU v1 is `supports`, but its description is generic and contains no pinpoint.
- Source v1 points to NIST Technical Note 1297 and describes uncertainty as quantitatively describing doubt in a measurement result.
- Context v1 limits the slice to basic understanding and says claims apply only within the definitions, conditions and source; it targets Claim A v1.
- Scope v1 describes a basic educational slice, not an exhaustive reference; it targets Claim A v1.

The Context and Scope target references are consistent and must remain Claim-A-only.

## 3. NIST primary-source inspection

The following official NIST material was inspected on 2026-11-23.

### A. NIST TN 1297, §2.1 — direct support

https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty

Section 2.1 states that a measurement result is an approximation or estimate of the measurand and is complete only when accompanied by a quantitative statement of its uncertainty. This is a close, direct match for Claim A.

Section 2.2 explains that uncertainty generally has several components and describes two categories by evaluation method. Section 2.3 warns that Type A/Type B do not map simply onto random/systematic classifications. These details are useful boundaries but exceed the Claim’s single basic proposition.

### B. NIST Measurement Uncertainty topic page — current explanatory definition

https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty

The page presents GUM and VIM definitions. It describes uncertainty as a parameter associated with a measurement result that characterizes dispersion of values reasonably attributable to the measurand, based on available information. It also explains that uncertainty expresses incomplete knowledge and may be represented using a suitable parameter such as a standard deviation or interval half-width with stated coverage probability.

This is a strong maintained explanatory locator for the meaning of measurement uncertainty. It is not a substitute for the exact NIST policy or for the full GUM/VIM documents.

### C. NIST TN 1900 — supplementary methodological source

https://www.nist.gov/publications/simple-guide-evaluating-and-expressing-uncertainty-nist-measurement-results

NIST identifies TN 1900 as a Simple Guide that supplements, but does not replace, TN 1297. Its abstract describes probabilistic characterization, measurement models, input quantities, bottom-up and top-down approaches, and examples. It is a useful currentness/methodology cross-check, but it is not necessary to support the narrow Claim A if TN 1297 §2.1 and the NIST topic page are properly cited.

### D. TN 1297 §7 — reporting guidance, not the best sole basis for Claim A

https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty

Section 7 addresses how uncertainty should be reported, including the coverage factor and supporting information. It is relevant to downstream reporting practices, but the direct Claim A proposition is better pinned to §2.1. Do not use §7 as the sole support for the general interpretation of a measurement result.

## 4. Essential conceptual boundary: uncertainty is not error

NIST TN 1297 Appendix D1 distinguishes measurement error from measurement uncertainty:

https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d1-terminology

The appendix defines measurement error as the result minus the value of the measurand and notes that the error is generally unknown, while uncertainty of the measurement result may be evaluated.

The NIST glossary also gives the GUM/VIM-style definition of uncertainty as a parameter characterizing dispersion of values reasonably attributable to the measurand:

https://pml.nist.gov/cuu/Uncertainty/glossary.html

The repaired EU must not imply any of the following:

- uncertainty is the same as measurement error;
- uncertainty is necessarily a known correction or a known bias;
- every uncertainty interval has a universal confidence level;
- a coverage factor such as (k=2) guarantees a particular probability without justified distributional assumptions;
- one calculation method applies to every measurand or measurement model.

These are important boundaries for a later reader explanation, even though the Claim itself does not need to enumerate them.

## 5. Source currency and authority assessment

TN 1297 remains an official NIST technical note with directly relevant sections. NIST TN 1900 is explicitly described by NIST as supplementing, not replacing, TN 1297. Therefore, it would be inaccurate to label TN 1297 simply obsolete or superseded on the evidence reviewed here.

At the same time, a single legacy technical note should not be presented as the only current explanation of the field. The maintained NIST Measurement Uncertainty topic page provides a current explanatory definition, while TN 1900 supplies a later methodological supplement.

Recommended treatment:

1. Keep TN 1297 §2.1 as the direct, concise support for the proposition that a measurement result is complete with a quantitative uncertainty statement.
2. Use the maintained NIST topic page as the current explanatory definition of the term.
3. Mention TN 1900 only if the final EU needs a methodological/currentness qualification; it is not required merely to support Claim A.
4. Do not imply that the topic page or TN 1900 replaces GUM, VIM, or the full technical framework.

## 6. Proposed remediation design

The current EU v1 structure contains one `source_ref`. Do not invent a multi-source field or assume the validator supports it.

### Preferred bounded approach

If the record model supports a single EU with one Source:

- Create a versioned Source record (or a new Source identity, according to the governing versioning standard) for the maintained NIST Measurement Uncertainty topic page.
- Preserve the existing TN 1297 Source v1 as historical canonical content; do not overwrite it.
- Create `EU-MEASUREMENT_UNCERTAINTY_BASICS-A@2` pointing to the exact Claim A v1 and to the most appropriate single Source selected by the schema.
- If the EU must point to only one Source, select TN 1297 §2.1 for the most direct proposition match and keep the maintained NIST topic page as a separately linked corroborating record only if the schema supports it without undocumented fields.

### If both primary sources must be directly attached

Inspect whether the standards permit multiple Evidence Use records for one Claim or another explicit provenance pattern. If so, propose a second EU record or other schema-compliant linkage. Do not silently change `source_ref` into an array, add unsupported keys, or introduce a Relation merely to work around the current schema.

### Draft EU description

> NIST TN 1297 §2.1 states that a measurement result is an estimate of the measurand and is complete only when accompanied by a quantitative statement of its uncertainty. NIST’s Measurement Uncertainty topic page defines uncertainty as a parameter associated with the result that characterizes the dispersion of values reasonably attributable to the measurand, based on the information used. This supports the Claim’s general requirement to interpret a measurement result together with an uncertainty assessment. Uncertainty is not identical to measurement error; the result’s error is generally unknown, while uncertainty can be evaluated.

This is draft prose only. It must be adapted to the actual Source/EU fields, exact versioning rules and pinpoint model before any write.

## 7. Full-slice dependency warning

This review covers only the five-record Claim-A subgraph. The existing candidate register indicates that the wider Measurement Uncertainty slice contains additional Claims and a BIPM VIM Evidence Use/Source track.

Consequently:

- This proposal does not certify the complete slice.
- Do not omit the BIPM/VIM dependency track from a future exact-version selection without a complete slice dependency audit.
- Do not infer that the five-record Claim-A subgraph is the complete closure for the slice.
- Do not retarget the current Context or Scope beyond Claim A.
- A later selection must include every exact dependency required by the selected Claims and reader rendering.

## 8. Required pre-write checks

Before canonical implementation:

1. Re-fetch the governing Evidence Use, Source, versioning, provenance and citation-locator standards.
2. Inspect the complete slice inventory and exact BIPM VIM records, not only Claim A.
3. Confirm whether one Claim may have multiple Evidence Use records and whether each EU may reference only one Source.
4. Confirm the exact pinpoint syntax supported by the schema and validators.
5. Verify the exact current NASA/NIST page availability and section headings at implementation time.
6. Preserve the distinction between uncertainty, error, random effects, systematic effects, correction, standard uncertainty and expanded uncertainty.
7. Preserve Context and Scope as Claim-A-only dependencies.
8. Run schema, reference, coverage and release-conformance tests after any authorized canonical change.
9. Keep all affected records HOLD regardless of technical test outcome.

## 9. Authorization request

No canonical writes are authorized by this proposal. A separate owner decision must identify:

- whether to version the existing NIST Source or create a new Source ID;
- whether to retain TN 1297 §2.1 as the primary pinpoint and add the maintained NIST topic page as corroboration;
- whether multiple EU records per Claim are permitted and desired;
- the exact permitted record IDs and fields;
- explicit exclusions: no Claim wording change, no Context/Scope change, no BIPM track deletion, no Decision/status change, no candidate-register/manifest/allowlist change.

## 10. Explicitly not included

- No canonical JSON changed and no record version was created.
- No Claim, Context, Scope, Relation, Assessment, Inference or Decision changed.
- No BIPM VIM record was changed, removed or declared unnecessary.
- No candidate denominator, coverage manifest or allowlist changed.
- No INCLUDE decision; HOLD remains.
- No licence, publication, merge, deployment or main-branch update was authorized.

## 11. Review conclusion

Claim A is a sound, low-consequence metrology proposition, and NIST TN 1297 §2.1 provides a direct statement supporting it. The maintained NIST Measurement Uncertainty page provides a useful current explanatory definition. TN 1900 supplements TN 1297 rather than replacing it. A release-quality evidence trail should use exact locators and explicitly preserve the uncertainty/error distinction.

**Disposition: HOLD — bounded remediation proposal prepared; canonical implementation not authorized.**
