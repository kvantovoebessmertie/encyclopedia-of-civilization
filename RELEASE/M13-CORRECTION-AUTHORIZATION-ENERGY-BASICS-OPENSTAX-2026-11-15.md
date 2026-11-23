# M13 Controlled Correction Authorization — Energy Basics OpenStax Source Identity and Pinpoints

Date: 2026-11-15  
Authorization ID: `M13-ENERGY-BASICS-OPENSTAX-001`  
Branch: `m13-system-wide-depth-audit-2026-10-09`

## Finding

The energy-basics slice identifies its source as “OpenStax Physics” and points to `https://openstax.org/books/physics/pages/9-introduction-to-work-energy-and-energy-resources`. The official OpenStax chapter matching the represented title is **College Physics, Chapter 7, “Work, Energy, and Energy Resources”**, at `https://openstax.org/books/college-physics/pages/7-introduction-to-work-energy-and-energy-resources`. Its official section structure identifies 7.1 Work: The Scientific Definition, 7.2 Kinetic Energy and the Work-Energy Theorem, 7.3 Gravitational Potential Energy, and 7.4 Conservative Forces and Potential Energy.

The current Source identity/URI pair is inconsistent with the official OpenStax title and chapter structure. The correction uses the official College Physics chapter and precise section locators. It does not imply that one chapter independently establishes all broader energy topics.

## Authorized exact scope

On branch `m13-system-wide-depth-audit-2026-10-09` only:

1. Version `SRC-ENERGY_BASICS` from v1 to v2, correcting only the source identity, URI, representation and preservation/rights note to the official OpenStax College Physics Chapter 7 page.
2. Version `CLM-ENERGY_BASICS-A/B/C` from v1 to v2, changing only `provenance.created_from[0].version` from Source v1 to Source v2. Preserve Claim statement, type, ID and all substantive content byte-for-byte.
3. Version `EU-ENERGY_BASICS-A/B/C` from the already-created v2 to v3, updating only Claim references to the corresponding Claim v2, Source-version reference/lineage to Source v2, and `content.material.description` with these claim-specific locators and limits:
   - A: §7.2, “Kinetic Energy and the Work-Energy Theorem”; supports kinetic energy as energy of motion and its dependence on mass and speed.
   - B: §§7.3–7.4, “Gravitational Potential Energy” and “Conservative Forces and Potential Energy”; supports position-related gravitational potential energy and potential energy for conservative-force configurations, without claiming this introductory treatment exhausts all potential-energy models.
   - C: §7.1, “Work: The Scientific Definition”; supports work as energy transfer by a force acting through displacement.
4. Version `CTX-ENERGY_BASICS` and `SCP-ENERGY_BASICS` from v1 to v2, changing only `content.target_ref.version` to Claim A v2. Preserve all context/scope wording.
5. Update only `CONTENT/vertical-slices/energy-basics/README.md` to the corrected book title, chapter and URL.
6. Strengthen only `REFERENCE/tests/test_content_energy_basics_vertical_slice.py` to assert exact Source identity/URI, Claim/Evidence Use/Source versions and links, Context/Scope targets, section locators and scope boundaries while preserving all three Claim statements.
7. Register this authorization and update only the M13 source-fit checkpoint documentation.

The version cascade is required because the repository storage resolver retains only the current version of a Record; after a version is replaced, references to the former version fail preflight. This cascade changes references only and does not change Claim meaning.

## Explicit exclusions

No Claim wording/type/content, new/deleted Records, Relations, other slices, risk metadata, D/E/B scores, publication allowlist, schema, coverage count, release gate, `main`, or PR merge change is authorized. Do not infer that these three Claims have final scores or publication eligibility. Do not reproduce OpenStax text beyond short section titles and paraphrased evidence descriptions; page-level rights/attribution review for a public edition remains separate.

## Acceptance

Run the dedicated regression, content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact changed paths, unchanged Claim statements, unchanged record count (9), and unchanged `main`. Keep PR #21 Draft/unmerged. This correction does not close M13 or approve publication.
