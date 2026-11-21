# Domain audit — temperature, waves, optics, magnetism and mechanics (Part II physical sciences)

Date: 2026-11-19  
Branch: mvp-public-contribution-design-2026-10-11  
PR workstream: #22, Work Package 1  
Audited revision: 911bcc2ba24a3f5dbb925ed95af8f7c3abd39df8  
Disposition: **HOLD — seven slices / 63 records screened; no canonical records changed**

## Plan and duplicate-control

This is a large targeted Part II physical-sciences batch. The prior ten-slice substantive audit of motion-basics, energy-basics and matter-basics was not repeated. The prior first-edition screens for thermodynamics-basics and electricity-basics were also not repeated. The seven slices below were not found in the current candidate register's completed screen headings and were read at exact version 1.

## Scope

- temperature-basics — 9 records
- waves-and-sound-basics — 9 records
- optics-basics — 9 records
- magnetism-basics — 9 records
- mechanics-basics — 9 records
- fluid-mechanics-basics — 9 records
- electromagnetism-basics — 9 records

Total: **63 records** (21 Claims, 21 Evidence Use, 7 Sources, 7 Context, 7 Scope).

## 1. temperature-basics — 9 records

Claims:
- A: kelvin (K) is the SI unit of thermodynamic temperature.
- B: a temperature interval of 1 K is equal in size to an interval of 1 °C.
- C: zero on the Kelvin scale is 0 K, called absolute zero.

Source: NIST, “Kelvin: Introduction”  
https://www.nist.gov/si-redefinition/kelvin-introduction

Findings:
- NIST explicitly identifies kelvin as the SI unit of temperature.
- NIST states that a change of one kelvin is the same amount of temperature change as one degree Celsius.
- NIST explicitly identifies 0 K as absolute zero.
- The current Source directly supports all three Claims.
- All three EUs still use generic descriptions without exact locators; Context and Scope target Claim A only.

Decision: **HOLD — strongest complete source fit in this batch.** Claims A/B/C are directly supported by the current NIST source. Add exact NIST passage locators to each EU through an authorized correction, and close Claim-specific Context/Scope boundaries before inclusion.

## 2. waves-and-sound-basics — 9 records

Claims:
- A: a wave is a propagating disturbance characterized by amplitude, frequency and wavelength.
- B: for a periodic wave, speed is related to frequency and wavelength by v=fλ.
- C: sound is a wave and propagates through a material medium.

Current Source: OpenStax Physics §13.2, “Wave Properties: Speed, Amplitude, Frequency, and Period”  
https://openstax.org/books/physics/pages/13-2-wave-properties-speed-amplitude-frequency-and-period

Additional direct OpenStax sections checked:
- §13.1, “Types of Waves”: https://openstax.org/books/physics/pages/13-1-types-of-waves
- §14.1, “Speed of Sound, Frequency, and Wavelength”: https://openstax.org/books/physics/pages/14-1-speed-of-sound-frequency-and-wavelength

Findings:
- Claim A is directly supported by §13.2, which describes wave velocity as the speed at which the disturbance moves and defines amplitude, frequency and wavelength.
- Claim B is directly supported by §13.2 equation 13.4: v_w=fλ.
- Claim C is directly supported by §13.1 and §14.1: sound is a disturbance/wave in matter; sound and water waves are mechanical waves and require a medium.
- The current Source points only to §13.2. It is a good source for A/B, but does not itself provide the strongest direct locator for C.
- All three EUs are generic and do not name the exact sections or equations.
- Context and Scope target Claim A only.

Decision: **HOLD — strong substantive fit, incomplete source mapping.** Claims A/B can use §13.2; Claim C needs a direct §13.1 or §14.1 Source/Evidence Use link. Add exact section/equation locators and retain the distinction between mechanical and electromagnetic waves.

## 3. optics-basics — 9 records

Claims:
- A: optics studies the behaviour of light and other electromagnetic waves and their interaction with matter.
- B: geometric optics models light propagation using rays when wave effects are not dominant.
- C: lenses and mirrors can form images whose properties depend on system geometry and object position.

Source: OpenStax Physics, Chapter 16 introduction  
https://openstax.org/books/physics/pages/16-introduction

Findings:
- The Chapter 16 introduction explicitly defines optics as the branch of physics dealing with visible light and other electromagnetic waves, their propagation and interaction with matter. This directly supports Claim A.
- The same introduction distinguishes geometric optics from regimes in which light's wave characteristics are prominent and describes the ray approximation. This directly supports Claim B.
- It states that mirrors and lenses form images; the full dependency on system geometry and object position needs exact support from §§16.1–16.3 rather than the chapter introduction alone.
- All three EUs are generic and lack pinpoint references.
- Context and Scope target Claim A only.
- OpenStax Physics is CC BY-NC-SA 4.0; attribution, noncommercial, ShareAlike and the stated restriction on LLM ingestion/training require explicit rights treatment for the intended distribution model.

Decision: **HOLD — strong conceptual fit.** A/B are directly supported; C needs a precise §16.1–16.3 locator. All EUs need pinpoints, and rights/reader review remain open.

## 4. magnetism-basics — 9 records

Claims:
- A: a magnetic field describes magnetic influence in space.
- B: permanent magnets and current-carrying conductors can create magnetic fields.
- C: magnetic force depends on the magnetic field and properties of the interacting objects.

Source: OpenStax Physics §20.1, “Magnetic Fields, Field Lines, and Force”  
https://openstax.org/books/physics/pages/20-1-magnetic-fields-field-lines-and-force

Findings:
- §20.1 directly explains that a magnet creates a magnetic field around it and that the field describes forces exerted on other magnets.
- The same section explicitly states that electric currents cause magnetic effects and that current-carrying wires create magnetic fields.
- It gives the magnetic-force relations for a moving charge and a current-carrying wire, supporting the dependence in Claim C, though the Claim wording should not be read as a complete force law.
- All three EUs are generic and need section/equation locators.
- Context and Scope target Claim A only.
- OpenStax Physics is CC BY-NC-SA 4.0; attribution, noncommercial, ShareAlike and LLM-ingestion restrictions must be handled.

Decision: **HOLD — direct source fit for all three Claims.** Exact §20.1 passage/equation pinpoints and Claim-specific Context/Scope closure remain.

## 5. mechanics-basics — 9 records

Claims:
- A: “the mechanics-basics slice introduces basic concepts and relations needed for orientation in the subject area.”
- B: “interpretation of information about mechanics-basics depends on source, context and claim applicability boundaries.”
- C: “basic knowledge of mechanics-basics does not replace specialized checking when a conclusion depends on conditions, measurements or professional assessment.”

Source: OpenStax University Physics Volume 1, Chapter 5 introduction (Newton's laws)  
https://openstax.org/books/university-physics-volume-1/pages/5-introduction

Findings:
- All three current Claims describe the editorial purpose, evidence limitations or scope of the slice. None is a falsifiable mechanics proposition.
- The source is an introduction to Newton's laws and forces; it cannot turn these editorial statements into documented scientific facts.
- The three EUs point to the same Source but have no meaningful proposition-specific passage.
- Context and Scope also target Claim A; they do not cure the Claim-type defect.
- The OpenStax source is CC BY-NC-SA 4.0 and includes attribution/noncommercial/ShareAlike and LLM-ingestion restrictions.

Decision: **HOLD — Claim-type/content defect across all three Claims.** Requires owner/editor-authorized replacement with substantive mechanics propositions (for example, Newton's laws or force/equilibrium relations) and claim-specific EUs. Do not cosmetically replace the source while retaining the editorial Claims.

## 6. fluid-mechanics-basics — 9 records

Claims:
- A: the slice introduces basic concepts and relations needed for orientation in fluid mechanics.
- B: interpretation depends on source, context and applicability boundaries.
- C: basic knowledge does not replace specialized checking when conclusions depend on conditions, measurements or professional assessment.

Source: OpenStax University Physics Volume 1 §14.5, “Fluid Dynamics”  
https://openstax.org/books/university-physics-volume-1/pages/14-5-fluid-dynamics

Findings:
- All three Claims are editorial descriptions, not falsifiable fluid-mechanics propositions.
- §14.5 contains real fluid-dynamics content (flow, flow rate, velocity, continuity and assumptions such as incompressibility/ideal fluids), but that content does not substantiate the current generic editorial statements as documented facts.
- All three EUs are generic and do not cite the actual scientific content in §14.5.
- Context and Scope target Claim A only.
- OpenStax University Physics Volume 1 is CC BY-NC-SA 4.0; attribution, noncommercial, ShareAlike and LLM-ingestion restrictions remain relevant.

Decision: **HOLD — Claim-type/content defect across all three Claims.** Requires authorized substantive Claims (for example, flow rate Q=Av or continuity under stated assumptions) with exact §14.5 locators and appropriate conditions. No canonical rewrite is made.

## 7. electromagnetism-basics — 9 records

Claims:
- A: the slice introduces basic concepts and relations needed for orientation in electromagnetism.
- B: interpretation depends on source, context and applicability boundaries.
- C: basic knowledge does not replace specialized checking when conclusions depend on conditions, measurements or professional assessment.

Source: OpenStax University Physics Volume 2, Chapter 13 introduction (electromagnetic induction)  
https://openstax.org/books/university-physics-volume-2/pages/13-introduction

Findings:
- All three current Claims are editorial descriptions, not falsifiable electromagnetism propositions.
- The current Source introduces time-varying fields and electromagnetic induction; it is not a direct source for the broad subject-level statements as documented facts.
- All three EUs are generic and lack a proposition-specific locator.
- Context and Scope target Claim A only.
- OpenStax University Physics Volume 2 is CC BY-NC-SA 4.0; attribution, noncommercial, ShareAlike and LLM-ingestion restrictions require rights review.

Decision: **HOLD — Claim-type/content defect across all three Claims.** Requires owner/editor-authorized substantive electromagnetic propositions and corresponding source/section-specific EUs. Do not include the current editorial statements as scientific facts.

## Cross-slice and integrity checks

- All 63 inventory-listed files were read at version 1; each local Claim/EU/Source reference resolves to the corresponding listed record.
- No new Relation was created; subject proximity is not sufficient justification.
- No previously closed M1 ten-slice audit was repeated (motion, energy, matter).
- Existing first-edition screens for thermodynamics and electricity were not repeated.
- No canonical Claim, Evidence Use, Source, Context, Scope or Relation JSON was edited.
- No INCLUDE decision, allowlist, preview or publication status was changed.
- main was not changed; PR #22 remains Draft.

## Group result

| Slice | Records | Main finding | Decision |
|---|---:|---|---|
| temperature-basics | 9 | NIST directly supports all three Claims; EUs need pinpoints | HOLD |
| waves-and-sound-basics | 9 | A/B supported by §13.2; C by §13.1/§14.1 not currently linked | HOLD |
| optics-basics | 9 | A/B directly supported; C needs lens/mirror section pinpoints | HOLD |
| magnetism-basics | 9 | All three substantively supported by §20.1; EUs generic | HOLD |
| mechanics-basics | 9 | All three Claims are editorial metadata, not mechanics facts | HOLD |
| fluid-mechanics-basics | 9 | All three Claims are editorial metadata, not fluid-mechanics facts | HOLD |
| electromagnetism-basics | 9 | All three Claims are editorial metadata, not electromagnetism facts | HOLD |
| **Total** | **63** | **No public INCLUDE decisions** | **HOLD** |

Next physical-sciences work must skip these completed screens and the previously audited motion/energy/matter/thermodynamics/electricity candidates. Continue with the next unreviewed domain family in Part II; do not launch new M13 batches or make unauthorized canonical changes.
