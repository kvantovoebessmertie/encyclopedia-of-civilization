# First Edition Scope and Survival Integration — 2026-11-18

## Decision and purpose

The Encyclopedia of Civilization will be released in useful, bounded editions. Completion of the entire M13 audit, exhaustive recovery of historical assessments, or complete coverage of all knowledge is not a prerequisite for the first edition.

The first edition must be a coherent, safe, traceable publication that can be extended through later versioned releases. Unreviewed material remains outside the public edition; it is not silently treated as verified. Known gaps and limitations are recorded and may remain open after release.

This plan is the controlling product direction for the first-edition workstream unless the project owner explicitly changes it.

## Core mission: preserve knowledge for life, survival, recovery, and civilization

Survival is a central purpose of the Encyclopedia, not an isolated subject silo. The publication should make practical survival and resilience knowledge discoverable across the corpus and connect it to the scientific, technical, social, and historical foundations that explain it.

The first edition should represent both:
- Direct survival and resilience knowledge: water, food, shelter, sanitation, health, first aid, fire, energy, tools, communications, navigation, agriculture, environmental hazards, emergency coordination, and practical safety.
- Foundational knowledge that enables survival and recovery: biology, chemistry, physics, materials, engineering, medicine, ecology, mathematics, measurement, logistics, governance, education, and other relevant fields.

Do not force every theoretical or historical Claim into an artificial survival instruction. Instead, create explicit, evidence-grounded Relations and reader-facing context where a real connection exists. Preserve the distinction between explanation, historical description, general practical knowledge, and prescriptive or emergency guidance.

High-consequence instructions (medical, water-treatment, electrical, structural, chemical, fire, and similar guidance) require stronger review and clear scope. They must not enter the first public edition merely to make the survival theme look comprehensive.

## First-edition product boundary

The first edition is a curated, version-pinned subset of the canonical corpus, not a claim that all 483 slices or all 1,494 Claims have been fully audited.

Selection principles:
1. Include a balanced cross-section of useful foundational knowledge, with meaningful survival/resilience coverage.
2. Prefer Claims with clear wording, stable source identity, resolvable Claim → Evidence Use → Source chains, and reproducible source locators.
3. Include only records whose scope, uncertainty, currentness, and limitations can be communicated honestly.
4. Exclude unresolved material contradictions, broken provenance, unclear rights, privacy issues, and high-consequence content lacking the required qualified review.
5. Do not infer eligibility from publication_status, CI success, a historical D/E/B score, a slice name, or the presence of many sources.
6. Do not require every Claim in the repository to be accepted before release.
7. Publish a visible scope statement and limitations register; expand coverage in later releases.

## Required first-edition deliverables

1. Exact allowlist: record IDs and versions for every included Claim, Evidence Use, Source, Context, Scope, and relevant Relation.
2. Reader experience: home/overview, topic navigation, search, Claim detail, source/evidence navigation, related knowledge, review-state explanations, and offline access.
3. Survival/resilience navigation: a cross-cutting index or curated pathways that connect practical topics to their foundational knowledge without distorting the source records.
4. Editorial and safety boundary: visible review state, applicability, uncertainty, last-reviewed/version information, and clear exclusions for unreviewed or high-risk content.
5. Rights and attribution register: documented reuse basis for the exact release bundle and all displayed third-party material.
6. Operations and correction process: accountable editorial owner, correction/takedown route, release rollback, and a controlled manual contribution path.
7. Reproducible release packet: pinned source revision, builder/version, manifest, hashes, exact-head required CI, offline verification, and final human sign-off.

## Three work packages — and only these are release-critical

### Work package 1 — Select and freeze the first-edition corpus
- Inventory existing candidate records and prior candidate reviews.
- Build a cross-domain shortlist that includes direct survival/resilience topics and foundational topics that support them.
- Screen candidates against identity/version, chain integrity, passage fit, scope, currentness, independence where material, consequence, rights, and reader comprehension.
- Record INCLUDE, HOLD, or EXCLUDE with a short reason and exact version.
- Produce a minimal coherent first-edition allowlist and explicit exclusions/gaps register.

Do not launch new M13 batches for this work. Use existing evidence and perform only targeted checks necessary for proposed public records.

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

M13 work is release-critical only where a specific unresolved issue affects a proposed first-edition record, a material cross-record relation, a high-consequence safety boundary, or the integrity of the publication process. All other M13 gaps remain visible in the internal limitations register and can be addressed after the first edition.

Historical scores and reports remain preserved. They are not automatically accepted as current assessments, but recovering every historical version or adjudicating every historical row is not a first-edition prerequisite.

## Release completion definition

The first edition is ready when:
- the exact, bounded allowlist has passed the applicable record-level gates;
- survival/resilience knowledge is represented as a coherent cross-cutting purpose alongside other knowledge domains;
- no known critical safety, provenance, rights, privacy, or security blocker remains in the included material;
- minimum editorial/operational responsibilities and correction routes are in place;
- the actual reader and offline artifact work as intended;
- exact-candidate CI, artifact inspection, independent review, and explicit release approval are recorded.

The first edition may openly contain gaps. It must not disguise them as completeness. The project then continues through versioned additions, corrections, and expanded domain coverage.