# M13 energy-basics OpenStax source-fit correction checkpoint

Date: 2026-11-15  
Authorization: `M13-ENERGY-BASICS-OPENSTAX-001`  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Finding and correction

The former Source v1 paired the identity “OpenStax Physics — work, energy and energy resources” with a URI under `/books/physics/pages/9-...`. The official OpenStax result matching the chapter title is **College Physics, Chapter 7, “Work, Energy, and Energy Resources”**. The former identity/URI pair did not match the official book/chapter record.

The bounded correction is registered in `RELEASE/EDITORIAL-CORRECTION.json` and authorized by `RELEASE/M13-CORRECTION-AUTHORIZATION-ENERGY-BASICS-OPENSTAX-2026-11-15.md`.

## Exact version cascade

- `SRC-ENERGY_BASICS@2`: corrected identity to OpenStax, College Physics, Chapter 7 and corrected URI to the official chapter page.
- `CLM-ENERGY_BASICS-A/B/C@2`: provenance reference only, now points to Source @2. Claim statements and claim types are unchanged.
- `EU-ENERGY_BASICS-A/B/C@3`: each points to its corresponding Claim @2 and Source @2, with claim-specific locators:
  - A: §7.2, kinetic energy and the work-energy theorem; introductory translational case.
  - B: §§7.3–7.4, gravitational potential energy and conservative forces/potential energy; not an exhaustive theory of all potential-energy models.
  - C: §7.1, scientific definition of work; energy transfer by a force acting through displacement.
- `CTX-ENERGY_BASICS@2` and `SCP-ENERGY_BASICS@2`: target reference version only, now points to Claim A @2.
- Updated only the energy-basics README and its dedicated regression.

The resolver retains only the current version of a Record. Therefore, the Source correction required the version-reference cascade above; it is not a semantic Claim rewrite. The slice remains exactly nine records. No Context/Scope wording, Relation, risk metadata or D/E/B score changed. No new or deleted Record was added.

## Source review

Official OpenStax chapter:
https://openstax.org/books/college-physics/pages/7-introduction-to-work-energy-and-energy-resources

Claim-specific section pages:
- §7.1: https://openstax.org/books/college-physics/pages/7-1-work-the-scientific-definition
- §7.2: https://openstax.org/books/college-physics/pages/7-2-kinetic-energy-and-the-work-energy-theorem
- §7.3: https://openstax.org/books/college-physics/pages/7-3-gravitational-potential-energy
- §7.4: https://openstax.org/books/college-physics/pages/7-4-conservative-forces-and-potential-energy

The official chapter outline and section summaries identify these sections and learning objectives. Evidence descriptions paraphrase the sections and do not reproduce textbook passages. Public-edition rights and attribution review remains a separate gate.

## Status and remaining gates

This is a source-identity, pinpoint and reference-integrity correction, not final semantic certification. No D/E/B score is assigned. Human View, independent review, rights/attribution review and the wider M13 audit remain open. Keep PR #21 Draft/unmerged and `main` unchanged.

Acceptance requires the dedicated regression, content preflight, Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD, followed by independent changed-path/tree/base/main verification.
