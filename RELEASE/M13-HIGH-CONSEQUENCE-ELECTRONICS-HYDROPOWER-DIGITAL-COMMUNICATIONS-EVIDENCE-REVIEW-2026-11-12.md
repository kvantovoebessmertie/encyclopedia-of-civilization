# M13 high-consequence evidence-use review — electronics, hydropower and digital communications (7 Claims)

Date: 2026-11-12
Scope: 7 high-consequence Claims with generic/template-like Evidence Use descriptions. This is a source-passage review and locator proposal, not engineering certification, standards compliance review or release clearance.

## 1. Electronics — 3 Claims

Canonical Source: `SRC-ELECTRONICS_BASICS`, NIST, “Electronics”, https://www.nist.gov/electronics

### Claim A — `CLM-ELECTRONICS_BASICS-A`

Claim: electronics covers systems/components using electrical, electromagnetic or optical properties to process, transmit or measure signals.

Exact support:
- NIST “Electronics” page, “Electronics Topics”, lists electromagnetics, flexible electronics, magnetoelectronics, optoelectronics, organic electronics, semiconductors, sensors and superconducting electronics.
- Its overview says NIST provides standards, instruments and calibrations for electronic components and systems, from small components to power grids.
- The NIST page does not itself provide a complete definition of electronics or directly describe all signal-processing/transmission/measurement functions.

Proposed locator: NIST “Electronics”, “Electronics Topics” and opening overview paragraph. Add a standard electronics textbook or IEEE technical glossary for the complete field definition.

Assessment: partial support; the source establishes the domain and principal subfields but not the full definition as worded.

### Claim B — `CLM-ELECTRONICS_BASICS-B`

Claim: semiconductors are basic materials for many modern electronic components and integrated circuits.

Exact support:
- NIST “Semiconductors”, “What are semiconductors?”, says materials such as silicon with tunable electrical conductivity are the base for most electronics and enable complex integrated circuits/chips.
- The page also discusses the transistor, semiconductor devices and their use in healthcare, communications, computing and transportation.

Proposed locator: NIST “Semiconductors”, “What are semiconductors?”, paragraph 1.

Assessment: direct support.

### Claim C — `CLM-ELECTRONICS_BASICS-C`

Claim: electronic component characteristics depend on design, materials, operating conditions and measurement methods.

Exact support:
- NIST “Semiconductors”, “What is NIST's Role?”, says semiconductor research improves measurement methods, data, reference artifacts, models and theory for device yield, reliability, fabrication and performance.
- “The State of the Industry” identifies technical limits of materials and the need for advances in measurement science, standards, materials, instrumentation, testing and manufacturing capabilities.
- This source is semiconductor-specific; it does not cover all electronic components or fully establish the effect of operating conditions for every component class.

Proposed locator: NIST “Semiconductors”, “What is NIST's Role?” and “The State of the Industry”, paragraphs 1–2. Add component-specific data sheets, reliability standards and test methods for operational specifications.

Assessment: partial support. Preserve the Claim's broad scope only if additional sources cover non-semiconductor components and operating conditions.

## 2. Hydropower — 1 Claim

Canonical Source: `SRC-HYDROPOWER_BASICS`, U.S. Department of Energy, “Hydropower Basics”, https://www.energy.gov/cmei/water/hydropower-basics

### Claim A — `CLM-HYDROPOWER_BASICS-A`

Claim: hydropower generates electricity by using the natural flow of moving water.

Exact support:
- DOE “Hydropower Basics”, “What is Hydropower?”, states: hydropower uses the natural flow of moving water to generate electricity.
- “How Does Hydropower Work?” explains that elevation differences created by dams or diversion structures move water through turbines and generators.

Proposed locator: DOE “Hydropower Basics”, “What is Hydropower?” and “How Does Hydropower Work?”.

Assessment: direct support, nearly verbatim. Keep the distinction between conventional hydropower and pumped-storage hydropower; pumped storage consumes electricity to pump water uphill and is an energy-storage system, not a net primary energy source.

Disposition: HOLD until the locator is entered and the pumped-storage boundary is preserved in adjacent material.

## 3. Digital communications — 3 Claims

Canonical Source: `SRC-DIGITAL_COMMUNICATIONS_BASICS`, ITU-T Recommendations, https://www.itu.int/rec/T-REC/en/

### Claim A — `CLM-DIGITAL_COMMUNICATIONS_BASICS-A`

Claim: digital communications systems use standardized methods to transmit and process information over telecommunications networks.

Exact support:
- ITU-T “Recommendations and other publications” says ITU-T Recommendations are standards defining how telecommunication networks operate and interwork, and that they enable interconnectivity and services worldwide.
- The catalogue identifies standards families for transmission systems/media, digital systems and networks (G), audiovisual and multimedia systems (H), data networks/open-system communications/security (X), and global information infrastructure/Internet protocol/next-generation networks (Y).

Proposed locator: ITU-T “Recommendations and other publications”, opening paragraph; ITU-T Recommendations catalogue, G/H/X/Y series.

Assessment: direct support for standardized transmission and interworking. The Claim's “processing information” is broader than the catalogue's high-level taxonomy; link a specific coding, protocol or signal-processing Recommendation if this component is intended to be precise.

### Claim B — `CLM-DIGITAL_COMMUNICATIONS_BASICS-B`

Claim: ITU-T Recommendations cover transmission systems, digital systems, multimedia systems and data networks.

Exact support:
- ITU-T Recommendations catalogue explicitly lists G (Transmission systems and media, digital systems and networks), H (Audiovisual and multimedia systems), X (Data networks, open system communications and security) and Y (Global information infrastructure, Internet protocol aspects and next-generation networks).

Proposed locator: ITU-T Recommendations catalogue, G/H/X/Y series.

Assessment: direct support.

### Claim C — `CLM-DIGITAL_COMMUNICATIONS_BASICS-C`

Claim: compatibility depends on standards, network architecture, interfaces and transmission conditions.

Exact support:
- ITU-T states that Recommendations define how networks operate and interwork and enable network interconnectivity.
- The catalogue includes recommendations on transmission media, digital systems/networks, data networks, Internet protocols, network management and measurement.
- The broad catalogue does not by itself establish every specific interface, physical-layer condition or architecture dependency; those require the particular Recommendations governing the network technology and interface in question.

Proposed locator: ITU-T “Recommendations and other publications”, opening paragraph; the relevant G/X/Y-series Recommendation for each claimed interface/protocol. Do not use the whole catalogue as a substitute for an individual technical standard.

Assessment: partial support. The general standards/interworking dependency is supported; specific interface and transmission-condition statements need exact Recommendations.

Scope boundary: ITU-T Recommendations are generally non-mandatory until adopted in national laws or regulations. They are international technical standards, not automatically binding legal requirements in every jurisdiction.

Disposition: all three HOLD until the EU records contain exact Recommendation series/IDs and the non-binding/adoption boundary is preserved.

## 4. Summary and disposition

- Claims reviewed: 7/7.
- Generic Evidence Use records reviewed: 7.
- Direct support: 4 Claims (electronics B, hydropower A, digital communications A/B).
- Partial/source-scope qualification: 3 Claims (electronics A/C and digital communications C).
- Canonical Evidence Use locators added: 0.
- Canonical Claim/Evidence Use/Source JSON changed: 0.
- D/E/B scores changed: 0.
- Electrical/electronics, hydropower or telecommunications specialist review completed: 0.
- Claims accepted or release-cleared: 0.
- All 7 remain HOLD pending controlled locator/source additions and specialist/Human View review.

## 5. Proposed remediation

1. Add NIST “Semiconductors” as a separate Source/Evidence Use for electronics B/C; add an authoritative general electronics definition for A.
2. Add the exact DOE Hydropower Basics headings to the hydropower EU and preserve the pumped-storage distinction.
3. Replace the generic ITU catalogue description with exact G/H/X/Y series and individual Recommendation identifiers relevant to the Claim.
4. Preserve the distinction between international technical recommendations and national legal adoption.
5. Do not edit canonical records until bounded authorization and regression tests cover Claim→EU→Source references, versioning and offline output.

## 6. Sources checked

- NIST, Electronics: https://www.nist.gov/electronics
- NIST, Semiconductors: https://www.nist.gov/semiconductors
- U.S. Department of Energy, Hydropower Basics: https://www.energy.gov/cmei/water/hydropower-basics
- U.S. Department of Energy, How Hydropower Works: https://www.energy.gov/cmei/water/how-hydropower-works
- ITU-T, Recommendations and other publications: https://www.itu.int/en/ITU-T/publications/pages/default.aspx
- ITU-T, Recommendations catalogue: https://www.itu.int/rec/T-REC/en/
