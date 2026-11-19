# Chemistry foundations — record-level domain audit

Date: 2026-11-19  
Workstream: PR #22 / Work Package 1 — first-edition candidate screening  
Branch: `mvp-public-contribution-design-2026-10-11`  
Scope: seven chemistry slices; exact record versions read from the PR branch.

## Coverage

| Slice | Records inspected | Record versions | Outcome |
|---|---:|---|---|
| mixtures-and-solutions | 9/9 | Source, 3 Claims, 3 Evidence Use, Context, Scope — all v1 | HOLD |
| acid-base-basics | 9/9 | Same canonical pattern — all v1 | HOLD; reuse prior M2 work, close record-level gap |
| chemical-reactions-basics | 9/9 | Same canonical pattern — all v1 | HOLD |
| organic-chemistry-basics | 9/9 | Same canonical pattern — all v1 | HOLD |
| analytical-chemistry-basics | 9/9 | Same canonical pattern — all v1 | HOLD; reuse prior M2 work, reconcile source identity |
| biochemistry-basics | 9/9 | Same canonical pattern — all v1 | HOLD |
| physical-chemistry-basics | 9/9 | Same canonical pattern — all v1 | HOLD |
| **Total** | **63/63** | **7 Sources, 21 Claims, 21 Evidence Use, 7 Context, 7 Scope** | **0 INCLUDE / 7 HOLD / 0 EXCLUDE** |

All 63 expected files exist on the PR branch and are marked `published`; that status is not treated as substantive publication eligibility.

## Findings by slice

### mixtures-and-solutions — HOLD

- Claims A–C are substantive and match OpenStax Chemistry 2e §11.1: homogeneous solution, solvent/solute distinction, and molecular/ionic dispersion.
- The current source record identifies the exact §11.1 URL.
- All three Evidence Use records merely say that the source is used within its material; none supplies a pinpoint section, passage, table, or figure locator.
- Context and Scope exist and are structurally linked to Claim A. Context is useful but does not replace applicability detail for concentration, phase, and solution composition.
- Remediation: add exact §11.1 locators to all three Evidence Use records; retain the existing Claim wording unless the editorial pass finds a specific overgeneralization.

### chemical-reactions-basics — HOLD

- Claims A–C concern reaction/product transformation, balanced-equation quantitative relations, and stoichiometric coefficients.
- OpenStax Chemistry 2e §4.3 directly supports stoichiometric relationships and the use of balanced-equation coefficients; the chapter summary also distinguishes yields and quantitative analysis.
- The Source record uses the generic identity “Authoritative reference source” rather than naming OpenStax, despite the README naming OpenStax Chemistry 2e.
- All three Evidence Use records contain generic descriptions without section-level locators.
- Remediation: normalize Source identity to the actual named source and provide precise §4.3 (and, where needed, chapter 4 introductory/summary) locators. Keep this slice educational; no operational synthesis or hazardous procedure is implied.

### organic-chemistry-basics — HOLD

- All three Claims are editorial/meta statements about what the slice introduces, the dependence of interpretation on context, and the limits of general knowledge.
- They are not substantive, independently falsifiable organic-chemistry propositions. The OpenStax Organic Chemistry introduction cannot substantiate them as domain facts in the form currently written.
- Evidence Use entries are generic and do not identify a specific passage.
- Context and Scope repeat the same editorial boundary rather than adding scientific applicability conditions.
- Remediation: replace Claims A–C through an authorized, versioned editorial correction with substantive foundational propositions (for example, carbon bonding/structural representation/functional-group concepts only after source and scope selection); then map each proposition to exact source passages. Do not silently rewrite canonical v1 records.

### biochemistry-basics — HOLD

- All three Claims are editorial/meta statements about the purpose of the slice, source/context dependence, and the need for specialist review.
- They do not state biochemical facts and are not supported as scientific Claims by the cited OpenStax Biology 2e metabolism introduction.
- Evidence Use entries are generic; no exact subsection, figure, or passage is identified.
- Context and Scope are generic editorial boundaries, not biochemical context.
- Remediation: authorized, versioned replacement with substantive, bounded propositions (e.g. ATP coupling, enzyme catalysis, or metabolic pathway concepts only after selecting precise source passages); add exact locators and appropriate biological context.

### physical-chemistry-basics — HOLD

- Claims A–C are substantive introductory thermodynamics propositions: energy/work/process relations, distinction between thermodynamic feasibility/direction and rate, and condition dependence of equilibrium/spontaneity.
- The cited OpenStax Chemistry 2e URL is the chapter 16 introduction, but Evidence Use records provide no exact section or passage. A chapter landing/introductory locator is insufficient for the detailed Claims as written.
- Context and Scope correctly warn against transferring conclusions across conditions but remain broad.
- Remediation: map each Claim to the relevant chapter 16 sections and equations, add exact locators, and preserve the distinction between thermodynamics and kinetics.

### acid-base-basics — HOLD; prior M2 remediation partially present

- The current Claims contain the corrected Brønsted–Lowry definition, pH through hydrogen-ion activity with an explicitly bounded concentration approximation, and buffer behavior.
- The README records the prior IUPAC Gold Book pH corroboration and the semantic correction. The current canonical Source/Evidence Use records, however, point only to OpenStax Chemistry 2e Ch. 14; no separate IUPAC Source/Evidence Use record is present in this nine-record slice.
- Evidence Use records remain generic and lack exact OpenStax §14 and IUPAC term locators.
- Remediation: do not repeat the completed semantic correction. Reconcile the README's independent-IUPAC statement with the canonical record graph by adding a controlled, versioned IUPAC source/evidence record set or correcting the README claim; add exact locators for acid/base, pH, and buffer propositions.

### analytical-chemistry-basics — HOLD; prior M2 remediation requires reconciliation

- Claims A–C are substantive: analytical measurement/data interpretation, method/sample/data-processing dependence, and calibration-model/range applicability.
- The README says an independent IUPAC Gold Book track was added, while the canonical Source record currently identifies NIST Tutorials in Analytical Chemistry. No IUPAC source record is present in the nine-record slice. This is a provenance/representation mismatch that must be resolved, not assumed to be covered by the README.
- Evidence Use records contain generic descriptions and no exact NIST or IUPAC locators.
- Context and Scope correctly signal method- and condition-dependence but do not supply measurement uncertainty, traceability, calibration-model, or validation detail.
- Remediation: preserve prior substantive work; reconcile the source-of-record against the claimed IUPAC track, add exact NIST/IUPAC locators and any required separate source records, and bound calibration/measurement claims to method and intended use.

## Cross-slice systemic defects

1. **Evidence Use is structurally linked but evidentially thin.** Most records point to a Source and say “supports” without identifying the actual passage, section, equation, figure, or table.
2. **Editorial Claims masquerade as documented facts.** Organic chemistry and biochemistry have three meta-claims each. These require authorized substantive replacement, not cosmetic evidence edits.
3. **README-to-canonical provenance drift.** Analytical chemistry claims IUPAC corroboration in its README but the current canonical Source points to NIST; acid-base README claims IUPAC corroboration while the current record graph contains only OpenStax.
4. **Source identity quality is uneven.** Chemical reactions uses a generic Source identity even though the README identifies OpenStax.
5. **Context/Scope records exist but are generic.** Their presence does not close Claim-level applicability or safety boundaries.

## Decisions and controlled next work

- Decision: **0 INCLUDE / 7 HOLD / 0 EXCLUDE**.
- Do not change publication state or include any of these slices in a first-edition allowlist on this evidence.
- No canonical JSON was modified by this audit.
- Do not repeat the prior M2 semantic remediation for acid-base or analytical chemistry. Resolve only the remaining source-graph, locator, and README/canonical consistency gaps.
- Batch remediation should be performed as controlled, versioned corrections: (a) repair Source identity/provenance, (b) add pinpoint Evidence Use, (c) replace organic/biochemistry meta-Claims, (d) strengthen Context/Scope where the substantive propositions require it.
- Re-run the affected schema, semantic, reference, and release-conformance checks on the exact resulting PR head after approved corrections. This audit does not claim CI PASS or authorize release.

## Evidence references used for external spot-check

- OpenStax Chemistry 2e §11.1, “The Dissolution Process”: https://openstax.org/books/chemistry-2e/pages/11-1-the-dissolution-process
- OpenStax Chemistry 2e §4.3, “Reaction Stoichiometry”: https://openstax.org/books/chemistry-2e/pages/4-3-reaction-stoichiometry
- OpenStax Chemistry 2e Chapter 4 summary: https://openstax.org/books/chemistry-2e/pages/4-summary

These spot-checks confirm the stated solution and stoichiometry concepts; they do not replace pinpoint Evidence Use records or establish rights clearance for redistribution.
