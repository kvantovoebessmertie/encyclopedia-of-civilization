# M5 Candidate Verification and Scope Lock — 2026-10-09

## Verification baseline
- Protected M4 accepted content HEAD: `83b2e3185cd92c55d53a5ce661be384508870e1a`
- Working branch: `m5-content-maturation-2026-10-09`
- Baseline: 479 vertical slices / 4698 Records / 19 Record types.
- M4 remains CLOSED CLEAN and is not reopened. M5 changes are isolated to this working branch.

## Method
Each candidate was checked against its three existing Claims, claim-specific Evidence Use records, registered source identity, Context and Scope, and existing cross-slice Relations. Record count is a screening signal, not an acceptance target. Selection considers claim substance, source-to-claim fit, evidence independence, consequence and Human View risk, existing integration, and the risk of duplicating already mature content.

## Candidate findings at the initial M5 baseline (pre-correction)

### A. Energy systems — `energy-systems-basics` — INCLUDE
- Claims describe the components and interactions of energy systems and list factors affecting choices; useful orientation, but broad and not sufficiently operationally differentiated.
- One source: IEA Energy System. All three Evidence Use records point to this same source and use generic support descriptions.
- Context and Scope are generic educational boundaries.
- Existing Relation: `REL-CROSS-SETTLEMENT-ENERGY` links the settlement-system claim to energy-systems Claim A. Preserve it; do not add a duplicate.
- Main gaps: independent evidence, grid/storage/infrastructure dependencies, resilience and safety boundaries, clearer conditions and limitations.

### B. Water treatment — `water-treatment-basics` — INCLUDE
- Claims establish treatment purpose, dependency on raw-water quality and contaminants, and the non-universality of methods.
- WHO is the primary source. An EPA emergency-disinfection source provides an additional evidence track only for Claim B; it must not be treated as independent support for all three claims or as a general treatment-design authority.
- Context/Scope correctly limit automatic application but do not yet sufficiently distinguish routine treatment, emergency disinfection, testing, and water-quality-specific selection.
- Existing Relation: `REL-CROSS-WATER-QUALITY-TREATMENT` links water-quality Claim A to treatment Claim B. Preserve it.

### C. Sanitation — `sanitation-basics` — INCLUDE
- Claims cover the sanitation service chain, exposure/pathogen reduction, and dependence on local systems, operation, maintenance and safe disposal.
- WHO is the primary source. CDC independently supports Claim B only; Claims A and C currently have one evidence track each.
- Context/Scope are generic and do not clearly expose service-chain failure, wastewater, environmental contamination, and health-risk boundaries.
- Existing Relations: `REL-CROSS-SANITATION-WASTEWATER` and `REL-CROSS-SANITATION-HYGIENE` exist. Preserve them; assess only claim-level justification for any future change.

### D. Materials science — `materials-science-basics` — INCLUDE / HIGHEST SUBSTANTIVE GAP
- The three Claims are largely meta-statements about the slice, interpretation, and need for specialized assessment. They do not yet teach substantive materials-science concepts.
- One source: NIST Materials Science and Engineering. Evidence Use descriptions are generic and all three Claims use the same source.
- Context/Scope are generic.
- Main gaps: material classes/structure-property relationships, processing and performance conditions, degradation/failure, testing/measurement, and lifecycle boundaries. Any new claim must be directly supported by its source.

### E. Manufacturing — `manufacturing-basics` — INCLUDE
- Claims cover operations, adjacent functions and systems thinking, but remain broad.
- One source: NIST CSRC glossary entry on manufacturing operations. The locator appears narrower than several claims, especially maintenance, supply/distribution, safety and IT.
- Context warns that specific parameters and safety procedures need verification; Scope remains generic.
- Existing nearby Relation concerns `manufacturing-processes-basics` and human factors, not this slice. Do not treat it as a direct relation to these Claims without a claim-level justification.
- Main gaps: source-to-claim alignment, process/quality/maintenance/lifecycle substance and independent evidence.

### F. Transportation — `transportation-basics` — INCLUDE
- Claims identify movement of people/goods, system components and dependence of safety/efficiency on operating conditions; currently introductory and generic.
- One source: U.S. DOT “About DOT,” which may not substantiate all claims at the required level of specificity. All three Evidence Use records point to it.
- Context/Scope distinguish system variation and local/professional requirements, but do not yet explain infrastructure dependencies or resilience.
- Existing Relation: `REL-CROSS-SETTLEMENT-TRANSPORTATION` links the settlement system to Transportation Claim A. Preserve it.

### G. Supply chains — `supply-chain-basics` — INCLUDE
- Claims have stronger substantive content than several other candidates: multi-tier dependencies, NIST risk management, and limited visibility/provenance.
- One source: NIST SP 800-161 Rev. 1 Update 1, specifically cybersecurity supply-chain risk management. The title/domain is broader than the current cyber-risk focus, so the slice must either clearly scope itself to that subdomain or add well-matched evidence for broader supply-chain concepts.
- Context/Scope are comparatively stronger and already caution against generalization.
- Main gaps: independent evidence, explicit domain boundary, continuity/logistics/resilience links where justified.

### H. Environmental engineering — `environmental-engineering-basics` — INCLUDE
- Claims describe the field, list water/wastewater/air/waste topics, and note dependence on environmental-system characteristics; they remain broad.
- One source: U.S. EPA Environmental Topics landing page. This locator is too broad to be assumed to substantiate all discipline-level claims without claim-specific source alignment.
- Evidence Use descriptions are generic. Context/Scope are generic educational boundaries.
- Main gaps: domain-specific independent sources and better-supported substance around pollution prevention/control, water/wastewater, waste, environmental measurement, and public-health boundaries.

### I. Telecommunications — `telecommunications-basics` — INCLUDE
- Claims cover information transmission, infrastructure components and standards/interoperability; foundational but broad.
- One source: ITU delegate guide / networks-and-services reference. All three Evidence Use records point to this source with limited claim-specific explanation.
- Context lists technology, infrastructure, standards, capacity and operating conditions; Scope excludes project/exploitation documentation.
- Main gaps: independent evidence, network layers/components, reliability/continuity, dependencies and interoperability conditions.

## Comparative priority
1. **Materials science** — most severe substantive gap: Claims currently describe the knowledge slice rather than materials-science facts.
2. **Energy systems** — high cross-domain importance; one broad source; grid, storage and resilience are not differentiated.
3. **Water treatment and sanitation** — high-consequence domains; independent sources currently support only a subset of Claims, so triangulation must be claim-specific.
4. **Environmental engineering** — high public-health/environmental consequence; broad locator and broad Claims.
5. **Manufacturing** — source-to-claim fit and lifecycle/process substance need improvement.
6. **Transportation and supply chains** — infrastructure and continuity importance; transportation evidence fit is weak, while supply-chain claims are currently focused on cybersecurity.
7. **Telecommunications** — critical infrastructure relevance; needs better claim-specific support and continuity boundaries.

## M5 locked scope
M5 is authorized to mature these nine existing slices only:
1. `energy-systems-basics`
2. `water-treatment-basics`
3. `sanitation-basics`
4. `materials-science-basics`
5. `manufacturing-basics`
6. `transportation-basics`
7. `supply-chain-basics`
8. `environmental-engineering-basics`
9. `telecommunications-basics`

No new vertical slice is authorized by this scope lock. No new Record type is authorized. Additions or rewrites must follow substantive findings, direct source-to-claim alignment, claim-specific Evidence Use, explicit Context/Scope boundaries, Relation review, dedicated regression updates, unified debt tracking, post-correction audits and exact-head Reference + Release Gate + Offline CI.

## Relation guardrails
- Preserve existing direct relations for settlement ↔ energy, settlement ↔ transportation, water quality ↔ treatment, and sanitation ↔ wastewater/hygiene.
- Do not add relations solely because two slices are topically adjacent.
- Evaluate a new Relation only if a specific Claim-level dependency materially improves navigation or reasoning and both endpoints are correct.

## Current decision
**M5 scope is locked and the controlled authoring pass is implemented on the working branch. M5 is not CLEAN.** The following post-authoring snapshot supersedes the baseline-only source and record counts above. Formal audits, full regression execution, exact-head CI and a CLEAN decision remain pending.


## Post-authoring snapshot — 2026-10-09

The following counts are from the current M5 working tree, not from the pre-correction baseline above.

| Slice | Records | Current evidence shape |
|---|---:|---|
| materials-science-basics | 15 | 2 Source, 4 Claim, 7 Evidence Use; Claims A–C triangulated NIST/NSF, Claim D NSF |
| energy-systems-basics | 15 | 2 Source, 4 Claim, 7 Evidence Use; Claims A–C triangulated IEA/DOE, Claim D DOE |
| water-treatment-basics | 17 | 3 Source, 4 Claim, 8 Evidence Use; WHO and EPA technology source across A–C, emergency EPA source supports B and D |
| sanitation-basics | 16 | 3 Source, 4 Claim, 7 Evidence Use; WHO/UNEP tracks for A/C, WHO/CDC for B, Claim D UNEP |
| manufacturing-basics | 15 | 2 Source, 4 Claim, 7 Evidence Use; Claims A–C triangulated NIST/UNIDO, Claim D UNIDO |
| transportation-basics | 15 | 2 Source, 4 Claim, 7 Evidence Use; Claims A–C triangulated DOT/World Bank, Claim D World Bank |
| supply-chain-basics | 16 | 3 Source, 4 Claim, 7 Evidence Use; Claims A–C triangulated NIST/CISA, Claim D OECD |
| environmental-engineering-basics | 16 | 3 Source, 4 Claim, 7 Evidence Use; Claims A–C triangulated EPA/AAEES, Claim D UNEP |
| telecommunications-basics | 15 | 3 Source, 4 Claim, 6 Evidence Use; Claims A/B ITU/CISA, Claim C ITU, Claim D FCC |

Current corpus snapshot: **479 vertical slices / 4754 Records / 19 Record types / 601 Sources / 1634 Evidence Use / 64 Relations**. The one additional Relation is `REL-CROSS-TELECOM-ENERGY-RESILIENCE`, justified by the direct telecommunications-continuity ↔ energy-grid-resilience dependency and covered by the cross-slice regression. The M5 additions do not create a new vertical slice or a new Record type.

The post-authoring shape includes claim-specific evidence links and dedicated regression assertions. This is not proof of correctness or a release pass: source-content fit, claim quality, safety boundaries, relation correctness, full corpus consistency and exact-head CI must still be checked. In particular, no claim is considered independently triangulated merely because its slice has more than one Source record.

M4 remains CLOSED CLEAN at accepted content HEAD `83b2e3185cd92c55d53a5ce661be384508870e1a`. Its checkpoint and synchronized debt map are carried forward unchanged in the M5 working branch. M5 changes remain isolated to `m5-content-maturation-2026-10-09`.
