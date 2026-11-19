# Human Sciences Domain Audit — 2026-11-19

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
Scope: three not-yet-screened Part II slices in the Human Sciences family. Previously reviewed learning, anatomy and physiology material is not repeated.

## Scope and method

Reviewed all 27 exact current canonical JSON records in:

- `psychology-basics`
- `neuroscience-basics`
- `developmental-biology-basics`

The review checked source identity and locator quality, Claim substance and scope, Evidence Use specificity, provenance/reference alignment, and Context/Scope usefulness. This is record-level screening, not a complete external-source or rights clearance.

### Reused prior work

- `learning-basics` is covered by the third domain-roadmap ten-slice expansion audit in `RELEASE/DOMAIN-EXPANSION-AUDIT-2026-09-30.md`; it is not re-audited here.
- Anatomy and physiology have already been reviewed in the earlier life-sciences / Part I screening work; no duplicate adjudication is performed in this package.

## Record inventory

| Slice | Records | Source | Claims | Evidence Use | Context | Scope | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| `psychology-basics` | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| `neuroscience-basics` | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| `developmental-biology-basics` | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| **Total** | **27** | **3** | **9** | **9** | **3** | **3** | **0 INCLUDE / 3 HOLD / 0 EXCLUDE** |

## Findings by slice

### psychology-basics — HOLD

- Claims A–C are editorial/meta placeholders describing the purpose of the slice, context dependence and the need for specialist review. They are not psychological propositions.
- The Source is the APA Dictionary entry “psychology”, updated 6 March 2026. It is a directly relevant definitional source and provides a suitable basis for a bounded definition of psychology, the study of mind and behavior, and the range of research approaches/branches.
- All three Evidence Use records are generic and contain no pinpoint locator or description of the specific definition or passage supporting a Claim.
- Context and Scope are generic and do not distinguish descriptive psychological science from clinical practice, diagnosis or individual treatment.

Required remediation: replace the three meta-Claims with bounded factual propositions derived from the APA definition; add a precise entry/definition locator to each Evidence Use; make Context/Scope distinguish research and general knowledge from individual clinical advice. APA copyright and reuse terms require separate review; no dictionary text should be copied into the corpus.

### neuroscience-basics — HOLD

- Claims A–C are substantive: scope of neuroscience, brain roles in sensory processing/movement/behavior, and the relationship between understanding the nervous system and neurological research/treatment development.
- The Source is an NINDS “Brain Basics” public-education landing page. It supports the general claims at a high level, but a more direct source record should identify the specific NINDS primer *Know Your Brain* (NIH Publication No. 23-NS-3440a, November 2023) or the relevant Brain Basics page.
- All three Evidence Use records lack exact section/page locators. This prevents the current graph from showing which parts support the three distinct propositions.
- Context and Scope are comparatively relevant but remain broad. The slice should distinguish basic human brain/neuron information from clinical interpretation or neurological diagnosis/treatment.

Required remediation: pin the specific NINDS primer and use exact page/section locators for brain functions, neuron structure/signaling and neurological research. Preserve the boundary between general neuroscience information and clinical advice.

### developmental-biology-basics — HOLD

- Claims A–C are substantive and concern developmental change, cell differentiation, and genetic/cellular-signal regulation.
- The Source is OpenStax Biology 2e, Chapter 43, “Animal Reproduction and Development”. It is relevant to animal reproduction and early embryonic development, but the current record does not identify the exact subsections. Its scope is narrower than the broad field label “developmental biology”.
- Evidence Use A–C are generic and contain no pinpoint locators. The cited chapter has direct relevant material in §43.6 “Fertilization and Early Embryonic Development” and §43.7 “Organogenesis and Vertebrate Axis Formation”: cleavage, blastula formation, gastrulation, germ layers, differentiation and cellular signaling.
- Context and Scope are boilerplate and do not state that the source-bounded material concerns animal embryonic development/organogenesis.

Required remediation: retain the current Source only if the slice is explicitly narrowed to animal early embryonic development and organogenesis; add locators to §§43.6 and 43.7 for each Claim; make Context/Scope reflect the limits of the cited chapter. Any use beyond factual paraphrase and attribution requires a separate OpenStax rights review.

## Cross-slice findings

1. **Record graph:** all three slices have the expected 9-record structure. Claim provenance points to the current Source; Evidence Use links the corresponding Claim and Source; Context and Scope target Claim A. No stale version reference was identified in this sample.
2. **Evidence Use:** all 9 Evidence Use records lack claim-specific pinpoint locators. This is a shared remediation requirement.
3. **Claim substance:** psychology has three editorial/meta Claims requiring replacement. Neuroscience and developmental biology have substantive Claims; their wording should be retained unless exact-source review identifies a material overstatement.
4. **Source fit:** APA Dictionary is a relevant definition source; NINDS is a relevant public-education source but should be pinned to the actual primer; OpenStax Chapter 43 is relevant but requires an explicit animal embryology/organogenesis boundary.
5. **Context/Scope:** psychology needs clinical-practice boundaries; neuroscience needs clinical-information boundaries; developmental biology needs a precise animal-development scope.
6. **Rights:** APA copyright, OpenStax CC BY-NC-SA and no-LLM-ingestion notice, and the rights status of NINDS text/visual components require source-specific review. Public accessibility does not automatically clear reuse.
7. **Publication:** existing `publication_status=published` values are not first-edition approval. All three slices remain HOLD.

## Aggregate decision

**0 INCLUDE / 3 HOLD / 0 EXCLUDE.**

No canonical JSON was modified. No publication state, first-edition allowlist, or release decision was changed. This report does not authorize Claim replacement, source substitution or versioned corrections.

## Next remediation order

1. Obtain bounded authorization for `psychology-basics`, `neuroscience-basics` and `developmental-biology-basics`.
2. Replace psychology's three editorial/meta Claims with source-bounded propositions.
3. Pin the NINDS primer and add precise Evidence Use locators for neuroscience.
4. Add exact OpenStax §§43.6–43.7 locators and narrow developmental biology's Context/Scope to the cited material.
5. Re-run exact-head preflight, Reference tests, Release Conformance Gate and Offline Edition.
6. Keep all three slices HOLD until rights and independent editorial/Human View gates are resolved.


## Remediation follow-up — 2026-11-19

The bounded remediation for all three slices was subsequently completed under `HUMAN-SCIENCES-REMEDIATION-001`. Source, Claims, Evidence Use, Context and Scope records were versioned; claim-specific locators and exact version references were added; and the three slice READMEs were aligned. See `RELEASE/HUMAN-SCIENCES-REMEDIATION-ADDENDUM-2026-11-19.md` for the full source map, record counts, rights boundaries and remaining release gates.

The original screening decisions remain unchanged: 0 INCLUDE / 3 HOLD / 0 EXCLUDE. The remediation does not grant publication approval.


## Rights-screen follow-up

The exact-source rights and attribution screen is recorded in `RELEASE/HUMAN-SCIENCES-RIGHTS-AND-ATTRIBUTION-SCREEN-2026-11-19.md`. It does not clear any slice for release; all three remain HOLD pending named human rights review and project-owner decisions.
