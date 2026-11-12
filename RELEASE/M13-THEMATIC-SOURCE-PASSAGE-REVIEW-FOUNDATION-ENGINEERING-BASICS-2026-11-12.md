# M13 thematic source-passage review — foundation engineering basics — 2026-11-12

Status: **3 CLAIMS REVIEWED; SOURCE PASSAGES LOCATED; CANONICAL CORRECTION NOT AUTHORIZED; ALL THREE REMAIN HOLD**

## Scope

Reviewed the three Claims, their three Evidence Use records, the linked FHWA Source record and slice README in `foundation-engineering-basics`. This review was triggered by the M13 evidence-linkage audit's generic Evidence Use descriptions.

No canonical JSON, Claim wording, D/E/B scores, manifest or publication status was changed. This is not a structural/geotechnical design review, independent specialist approval, or release authorization.

## Record-level findings

| Claim | Statement scope | Evidence finding | Disposition |
|---|---|---|---|
| `CLM-FOUNDATION_ENGINEERING_BASICS-A@1` | Foundations transfer structural loads to soil and must be coordinated with geotechnical/structural conditions | Directly supported at introductory level by FHWA NHI manual, Ch. 8 §8.0 and §8.1; it explains loads, soil response, settlement and structural criteria | HOLD pending versioned pinpoint |
| `CLM-FOUNDATION_ENGINEERING_BASICS-B@1` | Foundation type depends on loads, soil, water and site conditions | Directly supported by FHWA NHI manual, Ch. 8 §8.1 and Ch. 9 design sequence; site investigations, subsurface conditions, groundwater, loading and project constraints influence selection | HOLD pending versioned pinpoint |
| `CLM-FOUNDATION_ENGINEERING_BASICS-C@1` | Specific dimensions and structural solutions require calculation and design verification | Directly supported by FHWA NHI manual, Ch. 8 §8.1, §8.1.2 and design flow chart; loads, bearing capacity, settlement, limit states and specialist design are explicit | HOLD pending versioned pinpoint |

## Claim A — load transfer and coordination

The stored Evidence Use `EU-FOUNDATION_ENGINEERING_BASICS-A@1` points to `SRC-FOUNDATION_ENGINEERING_BASICS@1`, FHWA “Structural Foundations”, but contains only a generic sentence and no exact locator.

Direct passages located:

- FHWA NHI-06-089, *Soils and Foundations — Reference Manual, Volume II*, §8.0 (PDF pp. 8-1 onward), states that foundation design ensures imposed loads do not cause shear failure or damaging settlement (PDF lines 1136–1137).
- §8.1 identifies the foundation specialist's task as selecting a design that safely meets structural criteria and the intended function; it requires considering loads and tolerable deformation (lines 1145–1153).
- §8.1.2 explains ultimate and serviceability limit states, including soil bearing capacity, settlement and lateral displacement (lines 1184–1198).

**Finding:** Direct support for the core statement. The source is transportation-foundation guidance and should not be represented as a universal building code. The Claim is general and descriptive; retain the current boundary that actual design is project-specific.

## Claim B — selection depends on loads, ground, water and site conditions

The stored Evidence Use `EU-FOUNDATION_ENGINEERING_BASICS-B@1` has the same generic material description and no pinpoint.

Direct passages located:

- FHWA NHI-06-089, §8.1, requires determining load direction/type/magnitude, tolerable deformations and special constraints (lines 1147–1153).
- §8.1 also requires evaluating subsurface investigation and laboratory testing data and matching design methods to the quality/quantity of geotechnical data (lines 1162–1165).
- Chapter 9, foundation selection discussion, says the shallow/deep foundation decision depends primarily on site soil strength/compressibility, proposed loading, scour depth, performance criteria and cost (lines 3633–3637).
- The manual's geotechnical report guidance stresses that groundwater conditions are important to design and construction and must be assessed/described (lines 9484–9486).
- FHWA PDDM Chapter 6.4.3, §“Structure Foundations”, provides a current practice example: foundation selection considers subsurface investigation, material tests, surface/groundwater, loads, bearing materials, liquefaction, scour, frost depth and construction cost: https://highways.fhwa.dot.gov/sites/fhwa.dot.gov/files/Chapter_06.pdf

**Finding:** Direct support for the four stated factors. “Site conditions” is broad but is consistent with the source. The claim does not say these are the only factors, which is appropriate.

## Claim C — dimensions and design require calculation and project verification

The stored Evidence Use `EU-FOUNDATION_ENGINEERING_BASICS-C@1` has no exact locator.

Direct passages located:

- FHWA NHI-06-089, §8.1.2, describes ultimate and serviceability limit states and requires considering bearing capacity, settlement, lateral displacement and structural deterioration (lines 1184–1198).
- The §8.1 shallow-foundation design flow chart includes subsurface exploration, calculation of allowable bearing capacity, sliding/passive resistance, global stability checks and sizing the footing using service loads (lines 1392–1417).
- Chapter 9 emphasizes that an unambiguous set of foundation loads and performance requirements is necessary to proceed with design (lines 3622–3625).
- FHWA GEC 009 (2018), *Design, Analysis, and Testing of Laterally Loaded Deep Foundations*, explicitly describes design, analysis and testing guidance for deep foundations used in transportation facilities (PDF lines 14–16 and 51–54).

**Finding:** Direct support. The Claim is a sound safety boundary, but should not imply that this generic statement replaces applicable codes, site investigation, qualified geotechnical/structural engineering, or independent design review.

## Source identity and scope

The current Source record identifies the FHWA “Structural Foundations” overview page, which is a directory of methods, procedural guidance and technical publications for transportation foundations. It is not itself the detailed calculation source.

The reviewed NHI-06-089 manual is a distinct source (FHWA NHI-06-089, December 2006). FHWA GEC 009 is another distinct source (FHWA-HIF-18-031, April 2018). The FHWA PDDM Chapter 6 is a separate guidance document. These must be represented as separate Source identities if used in canonical Evidence Use records. Do not silently replace the current FHWA landing-page Source identity with a manual or PDF.

The NHI manual explicitly warns against indiscriminate application and says local conditions and geotechnical specialist judgment are necessary (PDF lines 71–75). It also states it is not a standard, specification or regulation (lines 19–20). This limitation is important and should accompany any use of the 2006 manual.

## Required bounded correction

1. Add distinct Source record(s) for FHWA NHI-06-089 and, if selected, FHWA GEC 009 / current PDDM Chapter 6. Preserve the existing FHWA overview Source identity.
2. Version the three Evidence Use records with Claim-specific pinpoints:
   - A: NHI-06-089 §§8.0, 8.1 and 8.1.2.
   - B: NHI-06-089 §8.1, Ch. 9 design sequence and geotechnical report groundwater section; corroborate with current PDDM §6.4.3.
   - C: NHI-06-089 §8.1.2 and design flow chart; GEC 009 foreword/abstract for deep-foundation design, analysis and testing.
3. Preserve transportation-specific scope and the source's warning that its guidance is not a standard or regulation.
4. Add regression tests for exact Claim/Source versions, locator presence and scope limitations.
5. Update coverage metadata only if the actual number of canonical records changes.
6. Run Reference Tests, Release Conformance Gate and Offline Edition on the exact resulting commit; retain Draft/unmerged status pending qualified geotechnical review and Human View.

## Evidence references

- FHWA, Structural Foundations overview (updated 2026-09-23): https://www.fhwa.dot.gov/engineering/geotech/foundations/
- FHWA NHI-06-089, *Soils and Foundations — Reference Manual, Volume II* (December 2006): https://www.fhwa.dot.gov/engineering/geotech/pubs/nhi06089.pdf
- FHWA GEC 009, *Design, Analysis, and Testing of Laterally Loaded Deep Foundations* (April 2018): https://www.fhwa.dot.gov/engineering/geotech/pubs/hif18031.pdf
- FHWA PDDM, Chapter 6 — Geotechnical, §6.4.3 Structure Foundations: https://highways.fhwa.dot.gov/sites/fhwa.dot.gov/files/Chapter_06.pdf

## Evidence boundary

Source-passage review only. No canonical records or scores changed. No Claim accepted or release-cleared. The three Claims remain HOLD pending bounded correction, independent geotechnical review, Human View and release gates.
