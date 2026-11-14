# M13 high-consequence evidence-use review — metrology, industrial safety, water security and basic mechanics (6 Claims)

Date: 2026-11-12
Scope: 6 high-consequence Claims with generic/template-like Evidence Use descriptions. This is a source-passage review and locator proposal; it does not certify a measuring instrument, approve industrial process safety or clear Claims for release.

## 1. Calibration — 1 Claim

Canonical Source: `SRC-CALIBRATION_BASICS`, NIST Calibration Services, https://www.nist.gov/calibrations

### Claim A — `CLM-CALIBRATION_BASICS-A`

Claim: calibration establishes a relation between indications from a measuring instrument and corresponding values of the measured quantity.

Exact support:
- JCGM 200:2012, International Vocabulary of Metrology (VIM), term 2.39 “calibration”, defines calibration as an operation which, under specified conditions, first establishes a relation between quantity values with measurement uncertainties provided by measurement standards and corresponding indications with associated uncertainties, and then uses that information to obtain a measurement result from an indication.
- VIM Note 2 distinguishes calibration from adjustment and verification.

Proposed locator: JCGM 200:2012 (VIM), 2.39 “calibration”, definition and Notes 1–3.

Assessment: direct, normative metrology definition. The currently linked NIST Calibration Services page is a service overview, not the definition itself. Add JCGM VIM 2.39 as a distinct Source/Evidence Use and preserve the distinction between calibration, adjustment and verification.

Disposition: HOLD pending exact JCGM locator.

## 2. Industrial safety — 1 Claim

Canonical Source: `SRC-INDUSTRIAL_SAFETY_BASICS`, OSHA, Process Safety Management (PSM), https://www.osha.gov/process-safety-management

### Claim C — `CLM-INDUSTRIAL_SAFETY_BASICS-C`

Claim: safety requirements depend on jurisdiction, industry, process and applicable standards.

Exact support:
- OSHA standard 29 CFR 1910.119 is a U.S. federal workplace regulation for process safety management of highly hazardous chemicals.
- §1910.119(a) specifies which processes and threshold quantities are covered and lists exclusions, including retail facilities, oil/gas well drilling or servicing, and normally unoccupied remote facilities.
- §1910.119(d)–(f) specifies process-specific information, hazard analysis, operating procedures and safety/health considerations; §1910.119(e)(4) requires process hazard analysis by a team with engineering and process-operation expertise.

Proposed locator: 29 CFR 1910.119(a) “Application”; (d) “Process safety information”; (e) “Process hazard analysis”; (f) “Operating procedures”.

Assessment: partial support. OSHA demonstrates that requirements can depend on jurisdiction, covered process, chemical thresholds and exclusions, but it is a specific U.S. PSM standard—not a universal industrial-safety rule. The Claim is a reasonable boundary statement, but a general assertion across industries needs a broader source such as ILO OSH standards plus jurisdiction-specific legislation for operational use.

Disposition: HOLD; narrow the linked OSHA EU to U.S. PSM scope and add a general OSH source if the Claim remains global.

## 3. Water security — 1 Claim

Canonical Sources:
- `SRC-EPA-WATER-SECURITY`, U.S. EPA, Water Security.
- `SRC-WATER_SECURITY`, UN-Water, Water Security and the Global Water Agenda.

### Claim B — `CLM-WATER_SECURITY-B`

Claim: water security includes protection against contamination and water-related disasters, and preservation of ecosystems.

Exact support:
- UN-Water, “Water Security and the Global Water Agenda”, proposed working definition states that water security includes sustainable access to adequate quantities and acceptable quality water, protection against water-borne pollution and water-related disasters, and preservation of ecosystems.
- EPA, “Water Security”, lines 5–11, says EPA works to prevent, prepare for and respond to contamination threatening public health; natural or human-made disasters can disrupt water/wastewater utilities; and drinking-water systems are vulnerable to terrorist attacks, industrial accidents, extreme weather and aging infrastructure.

Proposed locators: UN-Water analytical brief, “Proposed definition of water security”, paragraph 1; EPA “Water Security”, opening paragraphs and “Research Topics”.

Assessment: direct support for the Claim's three components. Preserve the fact that the UN-Water definition is a proposed working definition intended as a starting point for dialogue, not a binding legal definition in every jurisdiction.

Disposition: HOLD until both EU records carry their own exact locators.

## 4. Energy fundamentals — 3 Claims

Canonical Source: `SRC-ENERGY_BASICS`, OpenStax Physics, “Work, Energy, and Energy Resources”.

### Claim A — `CLM-ENERGY_BASICS-A`

Claim: kinetic energy is associated with an object's motion and depends on mass and speed.

Exact support:
- OpenStax, §9.1 “Work, Power, and the Work–Energy Theorem”, states that kinetic energy is energy of motion and gives (KE = \frac{1}{2}mv^2), explicitly showing dependence on mass and velocity.

Proposed locator: OpenStax Physics, §9.1, “The Work–Energy Theorem”, paragraph defining kinetic energy and equation (KE=\frac{1}{2}mv^2).

Assessment: direct support.

### Claim B — `CLM-ENERGY_BASICS-B`

Claim: potential energy is energy associated with the position or configuration of a system.

Exact support:
- OpenStax, §9.1, describes gravitational potential energy as stored energy due to an object's position.
- OpenStax College Physics 2e, §7.4 “Conservative Forces and Potential Energy”, defines potential energy as energy a system has due to position, shape or configuration and gives gravitational and spring examples.
- The OpenStax glossary entry “potential energy” uses the same definition.

Proposed locator: OpenStax College Physics 2e, §7.4, “Potential Energy and Conservative Forces”; Ch. 7 Glossary, “potential energy”.

Assessment: direct support. The source record's URL points to a general chapter landing page; add exact section/edition locators.

### Claim C — `CLM-ENERGY_BASICS-C`

Claim: work is a means of transferring energy through a force acting over displacement.

Exact support:
- OpenStax, §9.1, defines work as applying force to move an object over a distance in the direction of the force, (W=Fd).
- The section explicitly relates work to changes in energy and describes energy transfer into a system.
- OpenStax glossary defines work as transfer of energy by a force that causes an object to be displaced.

Proposed locator: OpenStax Physics, §9.1, “The Work–Energy Theorem”; Ch. 7 Glossary, “work”.

Assessment: direct support.

Disposition: all three HOLD until exact section/edition locators are entered. These are foundational physics claims, not operational engineering instructions.

## 5. Summary and disposition

- Claims reviewed: 6/6.
- Generic Evidence Use records reviewed: 6.
- Direct support: 5 Claims (calibration A, water security B, energy A/B/C).
- Partial/source-scope qualification: 1 Claim (industrial safety C).
- Canonical Evidence Use locators added: 0.
- Canonical Claim/Evidence Use/Source JSON changed: 0.
- D/E/B scores changed: 0.
- Metrology, industrial process-safety or water-security specialist review completed: 0.
- Claims accepted or release-cleared: 0.
- All 6 remain HOLD pending controlled locator/source-role remediation and Human View.

## 6. Proposed remediation

1. Add JCGM 200:2012 VIM 2.39 as a distinct Source/Evidence Use for calibration A; preserve the distinction between calibration, adjustment and verification.
2. Narrow OSHA industrial safety C to U.S. PSM scope; add ILO and other jurisdictional sources if a general cross-industry proposition is intended.
3. Add separate UN-Water and EPA locators to water-security B.
4. Add exact OpenStax section/edition locators for energy A/B/C; avoid mixing Physics and College Physics editions without explicit source identity.
5. Do not edit canonical records until bounded authorization and regression tests cover Claim→EU→Source links, source versioning and offline output.

## 7. Sources checked

- JCGM 200:2012, International Vocabulary of Metrology, VIM 2.39 “calibration”: https://jcgm.bipm.org/vim/en/2.39.html
- NIST Calibration Services: https://www.nist.gov/calibrations
- OSHA, 29 CFR 1910.119 Process Safety Management of Highly Hazardous Chemicals: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.119
- EPA, Water Security: https://www.epa.gov/emergency-response-research/water-security
- UN-Water, Water Security and the Global Water Agenda: https://www.unwater.org/publications/water-security-and-global-water-agenda
- OpenStax Physics, §9.1 Work, Power, and the Work–Energy Theorem: https://openstax.org/books/physics/pages/9-1-work-power-and-the-work-energy-theorem
- OpenStax College Physics 2e, §7.4 Conservative Forces and Potential Energy: https://openstax.org/books/college-physics-2e/pages/7-4-conservative-forces-and-potential-energy
- OpenStax College Physics 2e, Chapter 7 Glossary: https://openstax.org/books/college-physics-2e/pages/7-glossary


## 8. Second-pass canonical Claim → Evidence Use → Source inspection

The six Claim records and their primary Evidence Use/Source records were fetched from the current branch at version 1. The expected primary Claim/EU/Source pointers resolve. Water-security Claim B also has a separate EPA Evidence Use and Source link. No canonical record was modified.

### Findings by Claim

- **Calibration A:** the primary Evidence Use identifies NIST Calibration Services but gives no pinpoint and the linked page is a service overview, not the normative definition. JCGM VIM 2.39 is the direct definitional authority and should be a separate Source/Evidence Use. Preserve VIM Note 2's distinction between calibration, adjustment and verification. Current E=1 pending a canonical pinpoint/source link.
- **Industrial safety C:** the primary Evidence Use is generic. OSHA 29 CFR 1910.119 directly supports a narrow U.S. process-safety example with scope thresholds and exclusions. It does not establish a universal rule across industries and jurisdictions. Keep the Claim HOLD until its wording/source chain is either narrowed to the U.S. PSM example or broadened with an appropriate international OSH source (e.g. ILO standards) plus jurisdiction-specific context.
- **Water security B:** the UN-Water EU is generic and lacks its proposed-definition locator. The additional EPA EU is more descriptive but also lacks an exact paragraph locator. Both sources support relevant parts of the Claim, but preserve the UN-Water document's status as a proposed working definition rather than binding universal law. Current E=1 pending pinpoint locators in both Evidence Use records.
- **Energy A:** the canonical EU is generic and the Source points to the chapter introduction rather than §9.1. OpenStax §9.1 directly supports kinetic energy as energy of motion and the dependence on mass and velocity. Exact locator needed.
- **Energy B:** the canonical Source points to OpenStax Physics, while the report's broader “position or configuration” support relies partly on a different textbook, College Physics 2e §7.4. The current linked source alone supports gravitational potential energy due to position, but not the full generalization to configuration. Either narrow the Claim to the linked source's scope or add the College Physics 2e source as a distinct versioned Source/Evidence Use. Do not silently mix editions.
- **Energy C:** the canonical EU is generic and the Source points to the chapter introduction rather than §9.1. The source defines work as force applied over displacement in the direction of the force. The Claim should preserve this directional condition; a force perpendicular to displacement does not do mechanical work.

### Cross-record result

- Primary Claim/EU/Source links checked: 6/6, resolved.
- Supplementary water-security EPA EU/source: 1 additional link, resolved.
- Primary Evidence Use records with exact locators: 0/6.
- Supplementary water-security EPA Evidence Use with exact locator: 0/1.
- Current M13 E disposition: E=1 for all six until reproducible pinpoint locators are stored and verified.
- D/E/B reassessment in this second pass: 0.
- Canonical Claim/Evidence Use/Source changes: 0.
- All six remain HOLD. This second pass identifies two source-scope issues (calibration and industrial safety) and two content/source-precision issues (potential energy scope and work direction).
