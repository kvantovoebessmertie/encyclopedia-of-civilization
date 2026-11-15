# M13 energy-basics OpenStax source-fit correction checkpoint

Date: 2026-11-15  
Authorization: `M13-ENERGY-BASICS-OPENSTAX-001`  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Finding and correction

The former Source v1 paired the identity “OpenStax Physics — work, energy and energy resources” with a URI under `/books/physics/pages/9-...`. The official OpenStax result matching the chapter title is **College Physics, Chapter 7, “Work, Energy, and Energy Resources”**. The former identity/URI pair was not an exact book/chapter match.

The bounded correction is registered in `RELEASE/EDITORIAL-CORRECTION.json` and authorized by `RELEASE/M13-CORRECTION-AUTHORIZATION-ENERGY-BASICS-OPENSTAX-2026-11-15.md`.

## Exact changes

- `SRC-ENERGY_BASICS@2`: corrected identity to OpenStax, College Physics, Chapter 7 and corrected URI to the official chapter page.
- `EU-ENERGY_BASICS-A@2`: §7.2, kinetic energy and the work-energy theorem; support is limited to translational kinetic energy of an object of mass and speed.
- `EU-ENERGY_BASICS-B@2`: §§7.3–7.4, gravitational potential energy and conservative forces/potential energy; introductory support for position/configuration framing, not an exhaustive theory of all potential-energy models.
- `EU-ENERGY_BASICS-C@2`: §7.1, scientific definition of work; support is limited to energy transfer by a force acting through displacement.
- Updated only the energy-basics README and its dedicated regression.

All three Claim records remain v1 and their statement strings are preserved byte-for-byte. No Context, Scope, Relation, Record count, risk metadata or D/E/B score was changed. The slice remains nine records. No new Source or Evidence Use was added; existing records were versioned.

## Source review

Official OpenStax chapter:
https://openstax.org/books/college-physics/pages/7-introduction-to-work-energy-and-energy-resources

Claim-specific section pages:
- §7.1: https://openstax.org/books/college-physics/pages/7-1-work-the-scientific-definition
- §7.2: https://openstax.org/books/college-physics/pages/7-2-kinetic-energy-and-the-work-energy-theorem
- §7.3: https://openstax.org/books/college-physics/pages/7-3-gravitational-potential-energy
- §7.4: https://openstax.org/books/college-physics/pages/7-4-conservative-forces-and-potential-energy

The chapter outline and section summaries identify the above section titles and learning objectives. The evidence descriptions paraphrase those sections; they do not reproduce textbook passages. Public-edition rights and attribution review remains a separate gate.

## Status and remaining gates

This is a source-identity and pinpoint correction, not final semantic certification. No D/E/B score is assigned. Human View, independent review, rights/attribution review and the wider M13 audit remain open. Keep PR #21 Draft/unmerged and `main` unchanged.

Acceptance still requires the dedicated regression, content preflight, Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD, followed by independent changed-path/tree/base/main verification.
