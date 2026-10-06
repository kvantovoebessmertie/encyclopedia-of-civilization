# P7 Food Security & Nutrition Resilience — Unified Debt Map — 2026-10-06

## Baseline

- Gap Map: `f2bc3b76eaee74ff1c97881384350f663a52f30b`
- Corpus baseline: 478 vertical slices / 4405 Records / 19 Record types.
- Target cluster: 5 slices.

## Findings

### P7-EVIDENCE-001 — food-security-basics
**Status: OPEN**
The slice has one FAO source supporting three claims. Independent evidence depth is insufficient for the P7 resilience role.

**Required correction:** add an independent institutional source and evidence uses without duplicating the existing FAO locator.

### P7-EVIDENCE-002 — food-systems-basics
**Status: OPEN**
The slice has one FAO Agrifood Systems source supporting three claims. Independent evidence depth is insufficient for the maturation target.

**Required correction:** add an independent institutional source with claim-level provenance/evidence linkage.

### P7-EVIDENCE-003 — food-distribution-basics
**Status: OPEN**
The slice uses FAO Food Systems as its source, with the same canonical locator as food-systems-basics. This is not independent evidence for distribution.

**Required correction:** add a distribution/logistics-specific independent institutional source; retain FAO only for system context where justified.

### P7-EVIDENCE-004 — nutrition-basics
**Status: OPEN**
The slice has one NIH/NIEHS source for three claims.

**Required correction:** add an independent population-health/nutrition source and preserve the boundary against individualized medical/dietary advice.

### P7-EVIDENCE-005 — food-safety-basics
**Status: OPEN**
The slice has an FDA evidence track plus a CDC track, but the CDC source record identity is inconsistent in the repository: filename/record naming uses `SRC_FOOD_SAFETY_CDC` while the canonical project naming convention elsewhere uses hyphenated IDs. The claim/evidence references must be audited and normalized before closure.

**Required correction:** verify every CDC Claim → Evidence Use → Source reference and normalize identity only if required by the schema/contract; do not change identifiers blindly.

### P7-CONTENT-006 — cluster depth
**Status: OPEN**
Four of five target slices are explicitly introductory/single-source or otherwise thin. The P7 role requires mechanism, dependency, continuity and failure-boundary coverage rather than merely definitions.

**Required correction:** deepen claims only where independently supported; explicitly distinguish educational knowledge from live shortage, recall, logistics, regulatory or medical decisions.

### P7-LINKAGE-007 — cross-domain integration
**Status: OPEN**
The current cross-slice baseline is valid, but the P7 cluster needs a semantic audit against P4/P5/P6 dependencies: water/sanitation, public health, disaster response/recovery, logistics and infrastructure resilience. No artificial Relation should be added solely to increase counts.

**Required correction:** add only semantically justified relations, or document why the existing linkage is sufficient.

### P7-HUMAN-008 — adversarial boundaries
**Status: OPEN**
Food security, food distribution, food safety and nutrition can be misread as live operational instructions or individualized advice.

**Required correction:** make population/system scope, current-authority dependency, professional judgment and uncertainty boundaries explicit.

### P7-DOC-009 — documentation/regression
**Status: OPEN**
The target READMEs currently describe several slices as basic/introductory, and food-distribution-basics has an especially minimal README. Regression contracts and coverage must be synchronized after topology changes.

## Initial conclusion

P7 has substantive work to do. No finding is being carried forward as silently accepted.

## Closure rule

Every OPEN finding must be corrected, then the entire P7 cluster must undergo a fresh substantive re-audit. Only after that may the technical Reference + Release Gate + Offline 3/3 gate run, followed by a dedicated CLEAN checkpoint and independent 3/3 validation.
