# M13 Claim Type Triage — Repeated Editorial and Cross-Cutting Templates
Date: 2026-10-11
Branch: `m13-system-wide-depth-audit-2026-10-09`
Source revision for machine worksheet: `16deebea913d67dee524d5aafaae87011a9f720e`
Status: **High-confidence pattern flags for human review; not an automatic finding that any Claim is false. No content JSON changed.**

## Why this pass exists

The complete 1,494-Claim worksheet labels every row `NOT_YET_REVIEWED`; its machine flags are discovery aids, not D/E/B scores. A narrow exact-template screen found two recurring classes that may be misrepresented as domain `documented_fact` Claims:

1. **20 slice-purpose statements** say that the named local slice introduces basic concepts and relations for orientation. An external domain overview cannot establish that this particular local slice has adequate coverage. This is an editorial acceptance/coverage assertion and needs either an internal learning-design specification or a different record placement/type.
2. **30 cross-cutting methodology statements** use the same template: interpretation of a domain slice depends on source, context, and applicability limits (or equivalent boilerplate). These are epistemic/editorial principles rather than straightforward facts about the named domain. They need a type/placement review and an appropriate policy/methodology source if retained as Claims.

All 50 currently have `content.claim_type = documented_fact`. This is a classification concern, not a conclusion that the statements are substantively wrong. Exact template matching was deliberately narrow; other similar claims may exist outside these two lists.

## 1. Slice-purpose candidates (20)

- `CLM-ANTHROPOLOGY_BASICS-A`
- `CLM-BIOCHEMISTRY_BASICS-A`
- `CLM-CELL_BIOLOGY_BASICS-A`
- `CLM-CIVIL_ENGINEERING_BASICS-A`
- `CLM-CLIMATE_SCIENCE_BASICS-A`
- `CLM-COMPUTER_NETWORKS_BASICS-A`
- `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-A`
- `CLM-DATA_SCIENCE_BASICS-A`
- `CLM-ECOLOGY_BASICS-A`
- `CLM-ELECTROMAGNETISM_BASICS-A`
- `CLM-FLUID_MECHANICS_BASICS-A`
- `CLM-GENETICS_BASICS-A`
- `CLM-GENOMICS_BASICS-A`
- `CLM-GEOLOGY_BASICS-A`
- `CLM-LOGIC_BASICS-A`
- `CLM-OCEANOGRAPHY_BASICS-A`
- `CLM-OPERATING_SYSTEMS_BASICS-A`
- `CLM-ORGANIC_CHEMISTRY_BASICS-A`
- `CLM-PSYCHOLOGY_BASICS-A`
- `CLM-SOCIOLOGY_BASICS-A`

Common statement pattern: “Срез [slice] вводит базовые понятия и отношения, необходимые для ориентации в предметной области.”

## 2. Cross-cutting methodology candidates (30)

- `CLM-ANTHROPOLOGY_BASICS-B`
- `CLM-ARCHITECTURE_BASICS-B`
- `CLM-BIOCHEMISTRY_BASICS-B`
- `CLM-CELL_BIOLOGY_BASICS-B`
- `CLM-CIVIL_ENGINEERING_BASICS-B`
- `CLM-CLIMATE_SCIENCE_BASICS-B`
- `CLM-COMPUTER_NETWORKS_BASICS-B`
- `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-B`
- `CLM-DATA_SCIENCE_BASICS-B`
- `CLM-ECOLOGY_BASICS-B`
- `CLM-ELECTROMAGNETISM_BASICS-B`
- `CLM-EPIDEMIOLOGY_BASICS-B`
- `CLM-ETHICS_BASICS-B`
- `CLM-FLUID_MECHANICS_BASICS-B`
- `CLM-FOOD_SCIENCE_BASICS-B`
- `CLM-GENETICS_BASICS-B`
- `CLM-GENOMICS_BASICS-B`
- `CLM-GEOLOGY_BASICS-B`
- `CLM-HISTORY_METHODS_BASICS-B`
- `CLM-IMMUNOLOGY_BASICS-B`
- `CLM-LINGUISTICS_BASICS-B`
- `CLM-LOGIC_BASICS-B`
- `CLM-OCEANOGRAPHY_BASICS-B`
- `CLM-OPERATING_SYSTEMS_BASICS-B`
- `CLM-ORGANIC_CHEMISTRY_BASICS-B`
- `CLM-PHILOSOPHY_BASICS-B`
- `CLM-PSYCHOLOGY_BASICS-B`
- `CLM-RENEWABLE_ENERGY_BASICS-B`
- `CLM-ROBOTICS_BASICS-B`
- `CLM-SOCIOLOGY_BASICS-B`

The exact matched patterns include:
- “Интерпретация сведений по [slice] зависит от источника, контекста и границ применимости утверждения.”
- “Для интерпретации сведений по срезу необходимо учитывать источник, контекст и ограничения применимости.”
- “Источник имеет происхождение и контекст, которые влияют на его использование как свидетельства.”

## Recommended review disposition

1. Check whether these Claims belong in a project-wide methodology/editorial policy layer rather than repeated inside domain slices.
2. For slice-purpose statements, compare the assertion with a defined internal acceptance specification; do not use an external subject-matter overview as evidence of the local slice's completeness.
3. For cross-cutting methodology statements, either move them to a shared policy/methodology location or retain them only where they have a genuine domain-specific role and a suitable source.
4. Preserve current IDs and JSON until a correction plan explicitly authorizes exact changes.
5. Extend the same review beyond exact template matches only after this high-confidence queue is adjudicated.

## Reproducibility and limitations

The flags were generated from the current full-corpus worksheet by exact statement patterns. The worksheet covered **1,494 Claims** and the same revision recorded 586 Claims under the broad high-consequence keyword screen. These numbers are triage counts and can overlap. The pattern counts are **20 + 30 = 50 distinct Claim IDs** in this pass; they do not measure the total number of all editorial/methodological Claims in the corpus.

No Claim, Evidence Use, Source, or Relation JSON was edited. M13 remains open; these candidates require human review, and no final content correction is authorized by this report.
