# Domain audit — measurement, geometry and calculus (Part II foundations)

Date: 2026-11-19  
Branch: mvp-public-contribution-design-2026-10-11  
PR workstream: #22, Work Package 1  
Audited revision: d055f24e6a1ed89c4cb9804a4060d09a8f6868e0  
Disposition: **HOLD — three slices / 27 records screened; no canonical records changed**

## Plan and duplicate-control

This is the next targeted first-edition screen after completion of the 94-slice Part I structural/record-file coverage. It follows Part II Foundations in the controlling first-edition map. Existing M1/M2 substantive and Human View work for ratios-and-percentages, probability-basics and algebra-basics was identified and deliberately not repeated. Existing candidate reviews for statistics-basics and measurement-uncertainty-basics were also left untouched.

## Scope

Exact version-1 records inspected:
- units-and-measurement — 9 records
- geometry-basics — 9 records
- calculus-basics — 9 records

Total: **27 records** (9 Claims, 9 Evidence Use, 3 Sources, 3 Context, 3 Scope).

## 1. units-and-measurement — 9 records

Claims:
- A: measurement expresses a quantity numerically relative to an adopted unit and measurement procedure.
- B: SI defines a coherent set of units for expressing physical quantities.
- C: a measurement result should not be treated as exact knowledge without considering the unit, method and measurement uncertainty.

Current Source: NIST — SI Units  
https://www.nist.gov/pml/owm/metric-si/si-units

Additional authoritative material checked:
- BIPM/JCGM VIM 2.1 (measurement): https://www.iso.org/sites/JCGM/VIM/JCGM_200e_FILES/MAIN_JCGM_200e/02_e.html
- BIPM/JCGM VIM 2.9 (measurement result): https://jcgm.bipm.org/vim/en/2.9.html
- NIST measurement uncertainty: https://www.nist.gov/itl/sed/topic-areas/measurement-uncertainty

Findings:
- Claim A is substantively supported by VIM 2.1: measurement is an experimental process of obtaining quantity values and presupposes a measurement procedure and calibrated measuring system operating under specified conditions. The current NIST SI Units page provides unit/quantity context, but does not fully establish the procedure element by itself.
- Claim B is directly supported by NIST: SI is the international system for measurement; it defines seven base units and derived units, and values are expressed as a number paired with a unit.
- Claim C is directly supported by VIM 2.9: a measurement result generally comprises a quantity value together with relevant information and is generally expressed with measurement uncertainty. NIST's measurement-uncertainty page likewise describes measurement as an experimental process and explains uncertainty as incomplete knowledge of the measurand.
- All three existing EUs point only to the NIST SI Units Source and use generic descriptions. They do not provide claim-specific pinpoint locators, and the existing Source is insufficient by itself for all three propositions.
- Context and Scope target Claim A only.

Decision: **HOLD — strong foundational candidate, but evidence structure is incomplete.** Claim B has direct current-source support. Claims A/C need explicit additional source records and claim-specific EUs (VIM/NIST uncertainty) through an authorized versioned correction. Do not silently attach external material to the existing NIST Source.

## 2. geometry-basics — 9 records

Claims:
- A: geometric objects are described through points, lines, angles and figures.
- B: perimeter characterizes the length of a plane figure's boundary, while area characterizes the size of its region.
- C: measurement properties of a figure depend on selected definitions and units.

Current Source: OpenStax, Precalculus 2e, Chapter 10 introduction  
Stored URL: https://openstax.org/books/precalculus-2e/pages/10-introduction

Current official Chapter 10 page found:
https://openstax.org/books/precalculus-2e/pages/10-introduction-to-analytic-geometry

Findings:
- The current source is an introduction to analytic geometry and conic sections (ellipse, hyperbola, parabola, rotation of axes and polar coordinates). It is not a direct general-geometry source for the primitive objects in Claim A or the perimeter/area definitions in Claim B.
- Claim C is overly broad and weakly discriminating as written; it needs a more precise proposition or an explicit mathematical context.
- All three EUs use a generic description and provide no section/passage locators.
- Context and Scope target Claim A only.
- The stored source URL is not the canonical current chapter URL surfaced by OpenStax; the currently discoverable page has the longer 10-introduction-to-analytic-geometry path.
- OpenStax Precalculus 2e is CC BY-NC-SA 4.0; its preface also states restrictions on commercial use and LLM ingestion/training without prior written permission. Rights/attribution must be checked for the actual planned distribution model; no textbook text or images are proposed for reuse.

Decision: **HOLD — source/content mismatch.** The current source cannot substantiate the three general-geometry Claims as written. A more suitable general geometry source and precise locators are required; Claim C may need authorized narrowing or replacement. Do not cosmetically repair only the URL.

## 3. calculus-basics — 9 records

Claims:
- A: a limit describes function behaviour as its argument approaches a specified value.
- B: a derivative characterizes the instantaneous rate of change of a function when the relevant conditions for existence are met.
- C: a definite integral is used to describe accumulation under appropriate conditions.

Current Source: OpenStax, Calculus Volume 1  
https://openstax.org/details/books/calculus-volume-1

Direct sections checked:
- §2.2, “The Limit of a Function”: https://openstax.org/books/calculus-volume-1/pages/2-2-the-limit-of-a-function
- §3.1, “Defining the Derivative”: https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative
- §5.2, “The Definite Integral”: https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral

Findings:
- Claim A is directly supported by §2.2, which defines a function limit in terms of the values approached as the argument approaches a.
- Claim B is directly supported by §3.1, which defines the derivative through a limit of a difference quotient, provided the limit exists, and relates it to instantaneous rate of change.
- Claim C is directly supported by §5.2, which defines the definite integral and its net signed area/accumulation interpretation for integrable functions.
- The three EUs point to the correct book-level Source but have generic descriptions with no section pinpoints. They should cite the relevant section individually.
- Context and Scope target Claim A only; do not imply they automatically bound B/C.
- OpenStax Calculus Volume 1 is CC BY-NC-SA 4.0. The preface requires attribution, noncommercial use and ShareAlike for reused/adapted content, and states that LLM training/ingestion requires prior written permission. The project must decide whether its factual paraphrases and planned distribution model satisfy the applicable rights conditions; do not reproduce textbook prose, figures or exercises.

Decision: **HOLD — strong substantive candidate.** All three Claims have direct section-level support; remaining gates are precise EU locator corrections, rights/attribution review, Claim-specific Context/Scope closure and non-specialist reader review. No canonical edit is authorized by this audit.

## Cross-slice and integrity checks

- All 27 listed files resolve at version 1; each Claim/EU/Source link resolves to the listed local record identity.
- No cross-slice Relation was created: mathematical topic proximity alone is not sufficient evidence of a semantic relation.
- Prior M1/M2 reviews of ratios, probability and algebra were not repeated.
- Prior candidate reviews of statistics and measurement uncertainty were not repeated.
- No canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON was changed.
- No INCLUDE decision, allowlist, preview or publication status was changed.
- main was not changed; PR #22 remains Draft.

## Group result

| Slice | Records | Source/content finding | Decision |
|---|---:|---|---|
| units-and-measurement | 9 | SI Claim directly supported; measurement procedure and uncertainty need VIM/NIST sources | HOLD |
| geometry-basics | 9 | Existing analytic-geometry source does not fit general-geometry Claims | HOLD |
| calculus-basics | 9 | All three Claims directly supported by OpenStax §§2.2, 3.1, 5.2; EUs lack pinpoints; rights open | HOLD |
| **Total** | **27** | **No public INCLUDE decisions** | **HOLD** |

Next Part II sequence: continue mathematics/measurement only with candidates not already covered by M1/M2 or prior candidate screens; then proceed to physical sciences. Do not repeat closed adjudications or start new M13 batches.
