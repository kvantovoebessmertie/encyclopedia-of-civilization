# P7 Food Security & Nutrition Resilience — Content Gap Map — 2026-10-06

## Objective

Select the next maturation cluster after P6 Public Health & Health Resilience by targeting a high-leverage dependency for population resilience: food availability, food-system continuity, distribution, food safety, and nutrition.

## Current baseline

- Corpus: 478 vertical slices / 4405 Records / 19 Record types.
- P1–P6 are treated as closed baselines.
- Current cross-slice linkage baseline: 30 dedicated Relations.
- Coverage declares remaining gaps in domain breadth, cross-domain linkage, content depth, and domain-specific editorial evidence.

## P7 target cluster

1. `food-security-basics`
2. `food-systems-basics`
3. `food-distribution-basics`
4. `food-safety-basics`
5. `nutrition-basics`

## Why this cluster

Food is a direct continuity layer between infrastructure/disaster resilience and population health. The cluster also exposes an important maturation pattern: several existing slices are introductory and single-source, while food safety already has a partially independent second evidence track. P7 therefore tests whether the corpus can mature an existing domain without merely duplicating source counts.

## Initial gap hypotheses to test

### P7-EVIDENCE
- Food security appears to rely on one FAO source.
- Food systems appears to rely on one FAO source.
- Food distribution appears to use the same FAO Food Systems locator as food systems, creating a likely non-independent evidence basis.
- Nutrition appears to rely on one NIH/NIEHS source.
- Food safety has two institutional sources, but the CDC source record identity/provenance should be checked for consistency with the actual source and claim references.

### P7-CONTENT
- Food security, food systems, distribution and nutrition may be too introductory for the resilience role assigned to P7.
- Distribution requires explicit treatment of continuity, bottlenecks, storage/transport interfaces and failure boundaries rather than only generic food-system description.
- Food security should distinguish availability, access, utilization and stability where supported by evidence.
- Nutrition should distinguish population nutrition concepts from individualized dietary/medical advice.

### P7-HUMAN / SAFETY
- Food-safety content must not become individualized medical or regulatory instruction.
- Nutrition content must not silently turn population-level evidence into personalized dietary prescriptions.
- Food-security/distribution information must distinguish educational concepts from live shortage, recall, logistics or authority instructions.

### P7-LINKAGE
Assess whether existing relations adequately connect food systems to P5/P6 domains: disaster response/recovery, logistics, water/sanitation, public health, environmental health and critical infrastructure. Add Relations only when semantically justified.

### P7-DOCUMENTATION / REGRESSION
Verify README registry, coverage manifest, identity/reference integrity, duplicate URLs/identities, dedicated regression contracts, cross-slice audit and full-corpus regression alignment.

## Gate

No P7 CLEAN is allowed from this Gap Map. The next artifact is the substantive/debt audit. Every confirmed finding becomes part of one P7 Unified Debt Map and must be closed and re-audited before technical 3/3.
