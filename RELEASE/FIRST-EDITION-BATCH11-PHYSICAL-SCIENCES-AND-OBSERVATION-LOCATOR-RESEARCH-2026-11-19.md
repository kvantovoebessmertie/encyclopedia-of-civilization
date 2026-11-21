# First Edition — Batch 11 Physical Sciences and Observation Evidence Locator Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `257ce340e097993850dddd98b8e4fff46de4b6ef`  
Status: **15 CANDIDATE CLAIMS / 15 EUS RESEARCHED ACROSS FIVE SLICES; DIRECT LOCATOR CANDIDATES FOUND; OPTICS SOURCE MISMATCH AND ASTRONOMY SOURCE-GRAPH EXPANSION IDENTIFIED; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and selection controls

Batch 11 selects 15 Claims from five candidate slices present in the exact-version master and not covered by Batches 1–10 or active bounded authorizations:

- astronomy-observation-basics — Claims A–C;
- matter-basics — Claims A–C;
- optics-basics — Claims A–C;
- temperature-basics — Claims A–C;
- waves-and-sound-basics — Claims A–C.

All 15 Claim records, 15 Evidence Use records and five Source records were re-fetched from the current PR branch and confirmed present in the exact-version master. All 15 EUs currently have generic descriptions rather than claim-specific `material.locator` values.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation was edited. No record version, publication/completion status, allowlist or INCLUDE/HOLD/EXCLUDE decision changed. All five slices remain HOLD.

## 2. Aggregate result

| Slice | Claims / EUs | Source-fit result |
|---|---:|---|
| astronomy-observation-basics | 3 / 3 | NASA Universe Overview supports a narrowed Claim A; Claims B/C need direct NASA spectrum/telescope sources |
| matter-basics | 3 / 3 | OpenStax Chemistry 2e §§1.2, 1.3 and 2.3 directly support A–C |
| optics-basics | 3 / 3 | Current OpenStax Physics Chapter 16 URI is a waves source, not an optics source; replace with University Physics Volume 3 Chapters 1–2 |
| temperature-basics | 3 / 3 | NIST Kelvin page directly supports SI unit, Celsius interval equivalence and absolute zero |
| waves-and-sound-basics | 3 / 3 | OpenStax University Physics Volume 1 §§16.1 and 17.1 provide direct wave/sound locators; correct Source identity/URI |

**Total:** 15 Claims / 15 EUs / 5 existing Sources. No new canonical dependencies were created or discovered in this pass.

## 3. Astronomy Observation Basics — Claims A–C

Current records:
- `CLM-ASTRONOMY_OBSERVATION_BASICS-A/B/C@1`
- `EU-ASTRONOMY_OBSERVATION_BASICS-A/B/C@1`
- `SRC-ASTRONOMY_OBSERVATION_BASICS@1`

Current Source: NASA Science, “Universe Overview”. It is a relevant background page but does not directly support every detail in the current three Claims.

| Claim / EU | Current proposition | Direct locator candidate | Fit assessment |
|---|---|---|---|
| A | The Universe includes space, time, matter and energy and can be studied by astronomy | NASA “Universe Overview”, opening cosmology discussion and passages on origin/evolution/nature of the Universe | Partial. The page supports cosmology as study of the Universe's origin, evolution and nature; it does not provide a formal four-component definition exactly as the current Claim states |
| B | Astronomical observations use different electromagnetic-spectrum ranges | NASA “Sensing the Universe” and “Observatories Across the Electromagnetic Spectrum”; radio, infrared, visible, ultraviolet, X-ray and gamma-ray observatories |
| C | Telescopes/observatories collect and analyze signals from distant celestial objects | NASA Universe Glossary, “Telescope”; NASA “Telescopes” overview, light collection, mirrors/instruments and detection of faint distant objects |

Sources:
- NASA “Universe Overview”: https://science.nasa.gov/universe/overview/
- NASA “Sensing the Universe”: https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/sensing-the-universe/
- NASA “Observatories Across the Electromagnetic Spectrum”: https://science.nasa.gov/mission/hubble/science/explore-the-night-sky/observatories-across-the-electromagnetic-spectrum/
- NASA Universe Glossary, “Telescope”: https://science.nasa.gov/universe/glossary/
- NASA “Telescopes”: https://science.nasa.gov/mission/hubble/science/telescopes/

Recommended Claim A narrowing, if approved:

> Космология изучает происхождение, эволюцию и природу Вселенной.

This aligns the proposition to the NASA Universe Overview page without treating a programme description as a formal physical definition of the Universe. For Claim B, use the electromagnetic-spectrum and observatory pages rather than the Universe Overview alone. For Claim C, pin the telescope definition and the telescope overview's explanation of collecting light/signals from distant objects.

Recommended source graph:
- Keep the existing NASA Universe Overview Source for Claim A, with a claim-specific locator.
- Add separate NASA Sources/Evidence Uses for electromagnetic-spectrum observations (Claim B) and telescope function (Claim C), under the canonical ID allocation process. Do not invent IDs.
- The NASA pages are public informational pages; do not assume that every embedded image, diagram or third-party visual has the same reuse status as the text.

## 4. Matter Basics — Claims A–C

Current records:
- `CLM-MATTER_BASICS-A/B/C@1`
- `EU-MATTER_BASICS-A/B/C@1`
- `SRC-MATTER_BASICS@1`

The current Source identity is OpenStax *Chemistry 2e*, Chapter 1. The Source is appropriate; the EUs need exact section locators.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Matter is described by composition and properties and can be classified as elements, compounds or mixtures | §1.2 “Phases and Classification of Matter” and §1.3 “Physical and Chemical Properties” |
| B | An element is identified by its atomic number, which equals the number of protons in its atoms | §2.3 “Atomic Structure and Symbolism”, atomic number and element identity |
| C | Mixtures contain more than one substance and can have variable composition | §1.2 “Phases and Classification of Matter”, pure substances versus mixtures and homogeneous/heterogeneous mixtures |

Sources:
- §1.2: https://openstax.org/books/chemistry-2e/pages/1-2-phases-and-classification-of-matter
- §1.3: https://openstax.org/books/chemistry-2e/pages/1-3-physical-and-chemical-properties
- §2.3: https://openstax.org/books/chemistry-2e/pages/2-3-atomic-structure-and-symbolism

Claim B should state the atomic-number/proton relationship explicitly; it is not merely that an element has a unique chemical name. Claim C should preserve the distinction between pure substances and mixtures and between homogeneous and heterogeneous mixtures.

**Rights:** verify the exact OpenStax Chemistry 2e preface and licence terms. Attribution and ShareAlike may apply; public access does not grant commercial reuse or AI-ingestion permission. No textbook text, diagrams or tables are proposed for reproduction.

## 5. Optics Basics — Claims A–C; Source mismatch

Current records:
- `CLM-OPTICS_BASICS-A/B/C@1`
- `EU-OPTICS_BASICS-A/B/C@1`
- `SRC-OPTICS_BASICS@1`

The current Source identity says “OpenStax — Optics”, but the stored URI points to OpenStax Physics Chapter 16 introduction, a waves chapter. This is a material Source mismatch. The best direct source is OpenStax *University Physics Volume 3*, Chapters 1–2.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Optics studies light and its behavior/interactions with matter | Chapter 1 “The Nature of Light”; §1.1 “The Propagation of Light” |
| B | Geometric optics models light propagation using rays when wave effects can be neglected | §2.1 “The Ray Model of Light”; ray approximation and geometric-optics boundary |
| C | Mirrors and lenses form images whose properties depend on geometry and object position | §2.2 “The Law of Reflection” for mirrors; §2.4 “Thin Lenses” for lens image formation |

Sources:
- Chapter 1: https://openstax.org/books/university-physics-volume-3/pages/1-introduction
- §1.1: https://openstax.org/books/university-physics-volume-3/pages/1-1-the-propagation-of-light
- §2.1: https://openstax.org/books/university-physics-volume-3/pages/2-1-the-ray-model-of-light
- §2.2: https://openstax.org/books/university-physics-volume-3/pages/2-2-the-law-of-reflection
- §2.4: https://openstax.org/books/university-physics-volume-3/pages/2-4-thin-lenses

Recommended action:
1. Version the Source to the exact title *University Physics Volume 3* and correct the URI to the book/Chapter 1 identity.
2. Version each EU to the relevant section locator.
3. Version Claims only if the current statements need a wording adjustment or provenance must align to Source @2.
4. Preserve the model boundary: the ray model is an approximation appropriate when wave effects such as diffraction are negligible; it is not a universal description of all light behavior.

**Rights:** verify the current OpenStax Volume 3 preface/licence and AI-use restrictions before reuse. Do not infer commercial permission.

## 6. Temperature Basics — Claims A–C

Current records:
- `CLM-TEMPERATURE_BASICS-A/B/C@1`
- `EU-TEMPERATURE_BASICS-A/B/C@1`
- `SRC-TEMPERATURE_BASICS@1`

The existing NIST Source, “Kelvin: Introduction”, is appropriate. Pin each EU to the direct statement/paragraph.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Kelvin is the SI unit of thermodynamic temperature | NIST “Kelvin: Introduction”, opening paragraph and SI unit statement |
| B | A temperature interval of one kelvin equals an interval of one degree Celsius | Same page, paragraph defining Celsius temperature and stating equal interval size |
| C | Absolute zero corresponds to zero kelvin | Same page, paragraph on the zero point/absolute zero and the thermodynamic temperature scale |

Official source: https://www.nist.gov/si-redefinition/kelvin-introduction

The NIST page directly states that kelvin is the SI unit of thermodynamic temperature, the Celsius and kelvin scales have equal interval size, and zero kelvin is absolute zero. Preserve the distinction between a temperature value and a temperature interval: (0,^circmathrm C) is not (0,mathrm K), but a change of (1,^circmathrm C) equals a change of (1,mathrm K).

No Claim wording change is necessary if the current statements preserve these boundaries. NIST source reuse/attribution terms and any embedded graphics remain subject to source-specific review.

## 7. Waves and Sound Basics — Claims A–C

Current records:
- `CLM-WAVES_AND_SOUND_BASICS-A/B/C@1`
- `EU-WAVES_AND_SOUND_BASICS-A/B/C@1`
- `SRC-WAVES_AND_SOUND_BASICS@1`

The current Source points to OpenStax Physics Chapter 16 introduction, which is relevant to waves but does not directly cover the sound Claim. Correct the Source identity to the exact book-level publication and pin Claims A/B to Chapter 16 and Claim C to Chapter 17.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | A wave is a disturbance that propagates and can be described by amplitude, wavelength and frequency | *University Physics Volume 1* §16.1 “Traveling Waves”, wave definition and sinusoidal-wave parameters |
| B | For a periodic wave, propagation speed equals frequency multiplied by wavelength: (v=flambda) | §16.1 “Traveling Waves”, wave-speed equation |
| C | Sound is a mechanical wave and requires a material medium for propagation | *University Physics Volume 1* §17.1 “Sound Waves”, sound as a disturbance propagating through a medium |

Sources:
- §16.1: https://openstax.org/books/university-physics-volume-1/pages/16-1-traveling-waves
- §17.1: https://openstax.org/books/university-physics-volume-1/pages/17-1-sound-waves
- Book: https://openstax.org/books/university-physics-volume-1

Recommended Source correction: version the current Source identity to OpenStax *University Physics Volume 1* and use a book-level or §16.1 URI. The §17.1 locator for Claim C must identify the same exact edition/book. Do not claim that sound propagates through vacuum; the mechanical-wave boundary requires a material medium.

**Rights:** verify the exact current Volume 1 preface/licence and AI-use restrictions. Attribution/ShareAlike and non-commercial boundaries may apply.

## 8. Rights, source and editorial gates

- NASA Universe, spectrum and telescope pages: use claim-specific text locators; do not reuse images/diagrams without item-level rights review.
- OpenStax Chemistry 2e, University Physics Volume 1 and Volume 3: verify the exact edition's licence, attribution/ShareAlike conditions, commercial-use limits and AI-ingestion terms.
- NIST Kelvin page: preserve the exact SI definition and temperature-interval boundary; no reuse of embedded media is proposed.
- No source is treated as cleared solely because it is hosted by a government or educational institution.
- All five slices remain HOLD pending canonical locator implementation, source rights, independent subject/editorial review and Human View.

## 9. Recommended execution order after authorization

1. Locator-only: Matter A–C and Temperature A–C.
2. Source identity/URI correction: Optics and Waves/Sound; version their EUs to the exact OpenStax book/section locators.
3. Astronomy: keep the NASA Universe Overview chain for narrowed Claim A; authorize distinct source/EU chains for electromagnetic-spectrum observation and telescope function.
4. Claim wording decision: approve or amend Astronomy A if the formal space/time/matter/energy wording is not retained; preserve the exact ray-model and sound-medium boundaries.
5. Re-fetch all authorized records at one frozen HEAD, apply only approved versioned changes, validate Claim→EU→Source edges, run affected-slice tests, then full release gates on the final immutable HEAD.

## 10. Explicit non-actions

This report does not:
- authorize or perform any canonical JSON change;
- change Claim statements or versions;
- create new canonical Source/Evidence Use IDs;
- change publication/completion status or INCLUDE/HOLD/EXCLUDE decisions;
- modify Relations, validators, storage, recovery, allowlists or release-gate semantics;
- merge PR #22, deploy or approve publication.

**Owner decision required:** approve or amend the 15 locator/source changes; separately decide whether to narrow Astronomy A and whether to authorize the additional NASA Source/Evidence Use chains for Claims B/C.
