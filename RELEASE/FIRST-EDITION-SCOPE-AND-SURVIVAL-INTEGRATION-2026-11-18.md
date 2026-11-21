# First Edition Scope and Civilization Knowledge Architecture — 2026-11-18

## Controlling purpose

> Чтобы знания пережили нас.

The Encyclopedia of Civilization is an open library of verifiable, durable knowledge intended to preserve, transmit, and enable the practical use of human experience regardless of time, place, or access to modern technology.

Its purpose is broader than an emergency manual and broader than a collection of academic summaries. It must help people preserve life and health, understand the world, meet essential needs, create tools and systems, sustain communities, recover capabilities, and pass knowledge to future generations.

This document controls the first-edition workstream unless the project owner explicitly changes it.

## Content architecture: survival is a foundational opening section

**Survival and preservation of life is a full, standalone opening section of the Encyclopedia.** It is not merely a cross-cutting tag, an optional pathway, or a secondary application of other disciplines. It belongs at the beginning because preserving life and essential human capabilities is an immediate prerequisite for every further activity.

The opening section should organize practical knowledge in a coherent progression, including:

1. Immediate safety, situation assessment, priorities, and emergency response.
2. Water: finding, collecting, assessing, treating, storing, and distributing water.
3. Food: safe sourcing, preparation, preservation, storage, food security, and nutrition.
4. Shelter and settlement: protection from weather, safe temporary shelter, housing principles, and basic construction knowledge.
5. Health: hygiene, sanitation, disease prevention, first aid, basic human physiology, and clear medical boundaries.
6. Heat, fire, energy, and lighting: safe use, basic energy systems, and hazard prevention.
7. Tools, materials, repair, and basic production.
8. Agriculture, soil, seeds, plants, animals, and ecological resource stewardship.
9. Environmental and natural hazards: weather, flood, wildfire, extreme heat/cold, earthquakes, smoke, and other locally relevant risks.
10. Communication, navigation, signaling, coordination, and community-level logistics.

This is a content and navigation structure, not permission to publish unreviewed procedures. High-consequence practical guidance requires stronger evidence, explicit scope, limitations, and qualified review.

## The wider Encyclopedia

The survival section is the beginning, not the boundary, of the work. The Encyclopedia must then provide a broad and coherent body of knowledge, including:

- Fundamental sciences: mathematics, physics, chemistry, biology, earth and environmental sciences, astronomy, and scientific methods.
- Human body and health sciences: anatomy, physiology, nutrition, microbiology, epidemiology, public health, and medicine-related knowledge with appropriate boundaries.
- Engineering and technology: materials, construction, mechanics, electricity, energy, manufacturing, computing, telecommunications, transport, and infrastructure.
- Living systems and resources: ecology, agriculture, zoology, botany, soil, water systems, and biodiversity.
- Human and social knowledge: history, archaeology, language, culture, philosophy, ethics, education, law, economics, governance, and organization of communities.
- Civilization and recovery: settlements, logistics, public systems, knowledge preservation, production, infrastructure, and intergenerational transmission.

These are connected domains, not isolated silos. The reader should be able to move from a practical need to the underlying explanations, methods, sciences, technologies, social systems, and historical experience—and back again.

Cross-domain Relations and reader-facing pathways must express real, supported connections. Do not force every theoretical or historical Claim into a survival instruction, and do not distort canonical records to create artificial links.

## First-edition product boundary

The first edition is a curated, version-pinned and coherent publication drawn from the existing canonical corpus. It is not a claim that all repository records or all knowledge have been fully audited.

The first edition should begin with the survival section and then offer a meaningful breadth of foundational and wider civilizational knowledge. It must be useful as a real first volume, not merely a narrow technical demo. The exact included records are frozen through an explicit allowlist; gaps and exclusions are visible.

Selection principles:
1. Give the opening survival section meaningful, coherent coverage across essential human needs.
2. Include foundational knowledge and wider domains so the work remains an Encyclopedia of Civilization, not only a survival handbook.
3. Prefer Claims with clear wording, stable source identity, resolvable Claim → Evidence Use → Source chains, and reproducible source locators.
4. Communicate scope, uncertainty, currentness, and limitations honestly.
5. Exclude unresolved material contradictions, broken provenance, unclear rights, privacy issues, and high-consequence content lacking required review.
6. Do not infer eligibility from publication_status, CI success, historical D/E/B scores, slice names, or source counts.
7. Do not require every Claim in the repository to be accepted before release.

## Required first-edition deliverables

1. Exact allowlist: record IDs and versions for every included Claim, Evidence Use, Source, Context, Scope, and relevant Relation.
2. Opening survival section: a coherent table of contents and pathways through the essential life-preservation topics listed above, grounded in existing records.
3. Wider encyclopedia navigation: fundamental sciences, technology, living systems, human/social knowledge, and civilization/recovery domains.
4. Reader experience: home/overview, topic navigation, search, Claim detail, source/evidence navigation, related knowledge, review-state explanations, and offline access.
5. Editorial and safety boundary: visible review state, applicability, uncertainty, version information, and clear exclusions for unreviewed or high-risk content.
6. Rights and attribution register for the exact release bundle and displayed third-party material.
7. Operations and correction process: accountable editorial owner, correction/takedown route, release rollback, and a controlled manual contribution path.
8. Reproducible release packet: pinned source revision, builder/version, manifest, hashes, exact-head required CI, offline verification, and final human sign-off.

## Three work packages — release-critical

### Work package 1 — Select and freeze the first-edition corpus and structure
- Inventory existing candidate records and prior candidate reviews; do not recreate completed work.
- Build the opening survival section from existing domain slices first.
- Map the wider foundational and civilizational domains into the same reader-facing architecture.
- Identify genuine cross-domain Relations and learning paths.
- Screen proposed records for identity/version, chain integrity, passage fit, scope, currentness, consequence, rights, and reader comprehension.
- Record INCLUDE, HOLD, or EXCLUDE with a short reason and exact version.
- Produce the allowlist, opening table of contents, and explicit exclusions/gaps register.

Do not launch new M13 batches for this work. Use existing evidence and perform only targeted checks necessary for proposed public records. Do not modify canonical Claims or Evidence Use merely to make a candidate fit the release.

### Work package 2 — Close minimum publication governance
- Decide publication license/terms and source attribution policy.
- Name the accountable editorial owner and define review/approval responsibilities.
- Define correction, urgent takedown, appeal, and rollback handling.
- Define privacy and retention rules for any contact information.
- Use a controlled manual contribution route initially if a hosted intake service is not yet justified.

### Work package 3 — Assemble, test, and release
- Reuse the existing reader, publication builder, and offline edition implementation.
- Render only the exact allowlist; never expose internal drafts, review notes, or the full unaudited corpus by accident.
- Run exact-head reference, security, release-conformance, and offline checks; inspect the actual built artifact.
- Complete a focused non-specialist reader test and independent release review.
- Publish the first edition with a clear version, date, scope, known limitations, and update path.

## Relationship to M13

M13 continues as a separate quality-improvement and audit workstream. It is not a blanket release gate for every record in the repository.

M13 work is release-critical only where a specific unresolved issue affects a proposed first-edition record, a material cross-record relation, a high-consequence safety boundary, or publication integrity. All other M13 gaps remain visible in the internal limitations register and can be addressed after the first edition.

Historical scores and reports remain preserved. They are not automatically accepted as current assessments, but recovering every historical version or adjudicating every historical row is not a first-edition prerequisite. Do not repeat already completed adjudications.

## Release completion definition

The first edition is ready when:
- its opening survival section is coherent, useful, and grounded in reviewed records;
- the wider Encyclopedia domains are represented in a comprehensible structure;
- the exact, bounded allowlist has passed applicable record-level gates;
- no known critical safety, provenance, rights, privacy, or security blocker remains in included material;
- minimum editorial/operational responsibilities and correction routes are in place;
- the actual reader and offline artifact work as intended;
- exact-candidate CI, artifact inspection, independent review, and explicit release approval are recorded.

The first edition may openly contain gaps. It must not disguise them as completeness. The project continues through versioned additions, corrections, deeper evidence, and expanded domain coverage.
