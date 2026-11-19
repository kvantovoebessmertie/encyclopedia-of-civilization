# Chemistry evidence remediation — controlled addendum

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
Parent audit: `RELEASE/DOMAIN-AUDIT-CHEMISTRY-FOUNDATIONS-2026-11-19.md`

## Applied corrections

All changes below are versioned record updates. No Claim text or publication state was changed. Mixtures, acid-base and physical-chemistry Evidence Use records advanced v1→v2; reaction Evidence Use records advanced v1→v2→v3 to keep their source references aligned with the normalized Source v2.

| Slice | Record | Change |
|---|---|---|
| mixtures-and-solutions | EU A | Added OpenStax Chemistry 2e §11.1 definition locator for homogeneous solutions |
| mixtures-and-solutions | EU B | Added §11.1 solvent/solute definition locator |
| mixtures-and-solutions | EU C | Added §11.1 sucrose and ionic-dissolution examples for molecular/ionic dispersion |
| chemical-reactions-basics | SRC | Replaced generic source identity with OpenStax Chemistry 2e §4.3 Reaction Stoichiometry |
| chemical-reactions-basics | EU A | Added §4.3 locator for reactant/product identity in chemical change |
| chemical-reactions-basics | EU B | Added §4.3 locator for balanced-equation quantitative relationships |
| chemical-reactions-basics | EU C | Added §4.3 worked Examples 4.8–4.10 locator for stoichiometric factors |
| acid-base-basics | EU A | Added §14.1 Brønsted–Lowry proton-transfer definition locator |
| acid-base-basics | EU B | Added §14.2 pH/hydronium concentration locator, explicitly limited to the introductory concentration treatment |
| acid-base-basics | EU C | Added §14.6 buffer composition and function locator |
| physical-chemistry-basics | EU B | Added §16.1 and §16.4 spontaneity/free-energy locator; explicitly notes that kinetics/rate distinction remains unsupported by this source |
| physical-chemistry-basics | EU C | Added §16.4 equilibrium, spontaneity, and nonstandard-condition locator |

## Remaining blockers — intentionally not papered over

1. **Organic chemistry and biochemistry:** six v1 Claims remain editorial/meta statements rather than falsifiable domain propositions. No replacement text was invented or silently substituted. They require an approved content decision, source passage selection, and versioned Claim/EU corrections.
2. **Acid-base pH:** the v2 EU locator for Claim B supports the OpenStax introductory aqueous concentration treatment only. It does not establish the README's activity-based pH definition. The README's claimed independent IUPAC corroboration still has no corresponding IUPAC Source/Evidence Use record in the canonical nine-record graph.
3. **Analytical chemistry:** the README's claim of independent IUPAC corroboration remains inconsistent with the canonical NIST Source record. No locator or source was fabricated; reconcile the evidence graph before treating the prior M2 remediation as closed.
4. **Physical chemistry:** Claim A's energy/work scope still needs a directly matching source section. Claim B's thermodynamics-versus-kinetics distinction still needs a kinetics source. Claims remain HOLD.
5. **Rights:** OpenStax source locators do not settle redistribution, adaptation, or other rights questions for the intended edition.

## Integrity and release boundary

- 11 Evidence Use records were corrected: 8 advanced v1→v2 and the 3 reaction Evidence Use records advanced v1→v2→v3 to reference the normalized Source v2.
- 1 Source record identity was normalized and advanced from v1 to v2.
- No Claims, Context, Scope, allowlist, or publication states were changed.
- No main-branch change, merge, deploy, or release action was performed.
- The seven chemistry slices remain **HOLD**. This addendum records remediation progress, not publication approval.
- Exact-head workflows were still in progress when this addendum was prepared; no CI PASS is claimed.

## External section references checked

- OpenStax Chemistry 2e §11.1: https://openstax.org/books/chemistry-2e/pages/11-1-the-dissolution-process
- OpenStax Chemistry 2e §4.3: https://openstax.org/books/chemistry-2e/pages/4-3-reaction-stoichiometry
- OpenStax Chemistry 2e §14.1: https://openstax.org/books/chemistry-2e/pages/14-1-bronsted-lowry-acids-and-bases
- OpenStax Chemistry 2e §14.2: https://openstax.org/books/chemistry-2e/pages/14-2-ph-and-poh
- OpenStax Chemistry 2e §14.6: https://openstax.org/books/chemistry-2e/pages/14-6-buffers
- OpenStax Chemistry 2e §16.1: https://openstax.org/books/chemistry-2e/pages/16-1-spontaneity
- OpenStax Chemistry 2e §16.4: https://openstax.org/books/chemistry-2e/pages/16-4-free-energy


## Second remediation pass — substantive Claims and source alignment

A second bounded authorization was added to `RELEASE/EDITORIAL-CORRECTION.json` for `organic-chemistry-basics` and `biochemistry-basics`. The six former meta-Claims were replaced by substantive, falsifiable propositions, with corresponding source, evidence, context and scope versioning.

### organic-chemistry-basics

- Source v1→v2 now identifies OpenStax Organic Chemistry §3.1, “Functional Groups”.
- Claims A–C v1→v2 now cover: the definition of a functional group; the role of functional groups in determining characteristic chemical behavior; and common structural classes (C–C multiple bonds, carbon–electronegative-atom bonds, and carbonyl groups).
- Evidence Use A–C v1→v2 now identify the exact §3.1 passages/subsections.
- Context and Scope v1→v2 now describe the scientific context and limit the slice to introductory functional-group concepts.
- README records the controlled correction.

### biochemistry-basics

- Source v1→v2 now identifies OpenStax Biology 2e, Chapter 6, “Energy and Metabolism”.
- Claims A–C were replaced with propositions about metabolic pathways (§6.1), ATP as a cellular energy carrier (§6.4), and enzyme catalysis/activation energy/ΔG (§6.5).
- Claim B advanced v1→v2→v3 to correct a Russian wording typo; its Evidence Use record was correspondingly advanced v1→v2→v3. Claims A and C are v2.
- Evidence Use A–C identify §§6.1, 6.4 and 6.5 respectively.
- Context and Scope v1→v2 now provide biochemical context and exclude clinical or individualized protocols.
- README records the controlled correction.

### Updated remediation totals

- 17 Evidence Use records corrected across the six slices with locator changes: 14 are at v2 and 3 reaction-slice EUs are at v3 to align with Source v2. Biochemistry EU-B is also v3 after the Claim-B wording correction.
- 3 Source records advanced v1→v2: chemical reactions, organic chemistry, and biochemistry.
- 6 substantive Claims replaced: organic A–C and biochemistry A–C; biochemistry Claim B is v3 after the wording correction.
- 4 Context/Scope records advanced to v2.
- No publication state, allowlist, release decision, or main-branch state changed.

### Remaining HOLD conditions

The organic and biochemistry substantive-Claim defects are corrected, but both slices remain HOLD pending rights/licensing review and independent editorial/Human View approval. Other remaining blockers across the seven-slice batch are unchanged: acid-base activity-based pH needs a canonical IUPAC source/evidence link; analytical chemistry still has README-to-canonical IUPAC/NIST provenance drift; physical chemistry still needs a direct energy/work source for Claim A and a kinetics source for Claim B; rights clearance remains unresolved for the intended redistribution model.

This is a correction record, not a publication approval. Exact-head CI remains the release prerequisite.
