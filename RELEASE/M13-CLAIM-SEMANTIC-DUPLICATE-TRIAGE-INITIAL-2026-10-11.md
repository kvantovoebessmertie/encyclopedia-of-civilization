# M13 Initial Claim Semantic-Duplicate Triage

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **machine-assisted candidate groups for human adjudication; no content changes**

## Basis and limits

A full-corpus Claim worksheet was generated from 4,831 record files and contains all 1,494 Claims. Its recorded source revision is CI merge checkout `f39f0dbc51bceb3726ee5945370cb878566e70b7`; the Claim content was not changed by the subsequent audit-report/tooling commits. Statement comparison used Unicode normalization, case-folding and whitespace normalization. This pass is a candidate finder, not proof that any repeated wording must be deleted: cross-cutting policy text may be intentionally repeated, but its type, source and placement still need to be justified.

## 1. Exact normalized duplicate statements

The worksheet found **two exact normalized statement groups covering 18 Claims**.

### Group A — source/context/applicability rule (9 Claims)

Exact statement: «Для интерпретации сведений по срезу необходимо учитывать источник, контекст и ограничения применимости.»

| Claim ID | Slice |
|---|---|
| `CLM-ARCHITECTURE_BASICS-B` | architecture-basics |
| `CLM-EPIDEMIOLOGY_BASICS-B` | epidemiology-basics |
| `CLM-ETHICS_BASICS-B` | ethics-basics |
| `CLM-FOOD_SCIENCE_BASICS-B` | food-science-basics |
| `CLM-IMMUNOLOGY_BASICS-B` | immunology-basics |
| `CLM-LINGUISTICS_BASICS-B` | linguistics-basics |
| `CLM-PHILOSOPHY_BASICS-B` | philosophy-basics |
| `CLM-RENEWABLE_ENERGY_BASICS-B` | renewable-energy-basics |
| `CLM-ROBOTICS_BASICS-B` | robotics-basics |

### Group B — specialist-checking rule (9 Claims)

Exact statement: «Обобщённые сведения среза не заменяют специализированную проверку там, где вывод зависит от условий, измерений или профессиональной оценки.»

| Claim ID | Slice |
|---|---|
| `CLM-ARCHITECTURE_BASICS-C` | architecture-basics |
| `CLM-EPIDEMIOLOGY_BASICS-C` | epidemiology-basics |
| `CLM-ETHICS_BASICS-C` | ethics-basics |
| `CLM-FOOD_SCIENCE_BASICS-C` | food-science-basics |
| `CLM-IMMUNOLOGY_BASICS-C` | immunology-basics |
| `CLM-LINGUISTICS_BASICS-C` | linguistics-basics |
| `CLM-PHILOSOPHY_BASICS-C` | philosophy-basics |
| `CLM-RENEWABLE_ENERGY_BASICS-C` | renewable-energy-basics |
| `CLM-ROBOTICS_BASICS-C` | robotics-basics |

All 18 are stored as `claim_type: documented_fact` and are linked to subject-matter Sources with generic or near-generic Evidence Use descriptions. The likely issue is not necessarily that the methodological advice is wrong; it is that a cross-cutting epistemic/governance rule is being represented repeatedly as a domain-specific fact and appears to be “supported” by sources that may not establish the rule.

## 2. Three 20-Claim template families (60 candidates)

The worksheet also found 20 Claims in each of these templated families, with the slice slug substituted into the sentence. These are not byte-for-byte duplicate statements after normalization, but are semantically near-duplicate across domains.

### Family A — slice coverage/learning-purpose statement (20 Claims)

`Срез {slice-slug} вводит базовые понятия и отношения, необходимые для ориентации в предметной области.`

`CLM-ANTHROPOLOGY_BASICS-A`; `CLM-BIOCHEMISTRY_BASICS-A`; `CLM-CELL_BIOLOGY_BASICS-A`; `CLM-CIVIL_ENGINEERING_BASICS-A`; `CLM-CLIMATE_SCIENCE_BASICS-A`; `CLM-COMPUTER_NETWORKS_BASICS-A`; `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-A`; `CLM-DATA_SCIENCE_BASICS-A`; `CLM-ECOLOGY_BASICS-A`; `CLM-ELECTROMAGNETISM_BASICS-A`; `CLM-FLUID_MECHANICS_BASICS-A`; `CLM-GENETICS_BASICS-A`; `CLM-GENOMICS_BASICS-A`; `CLM-GEOLOGY_BASICS-A`; `CLM-LOGIC_BASICS-A`; `CLM-OCEANOGRAPHY_BASICS-A`; `CLM-OPERATING_SYSTEMS_BASICS-A`; `CLM-ORGANIC_CHEMISTRY_BASICS-A`; `CLM-PSYCHOLOGY_BASICS-A`; `CLM-SOCIOLOGY_BASICS-A`.

### Family B — source/context/applicability principle (20 Claims)

`Интерпретация сведений по {slice-slug} зависит от источника, контекста и границ применимости утверждения.`

`CLM-ANTHROPOLOGY_BASICS-B`; `CLM-BIOCHEMISTRY_BASICS-B`; `CLM-CELL_BIOLOGY_BASICS-B`; `CLM-CIVIL_ENGINEERING_BASICS-B`; `CLM-CLIMATE_SCIENCE_BASICS-B`; `CLM-COMPUTER_NETWORKS_BASICS-B`; `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-B`; `CLM-DATA_SCIENCE_BASICS-B`; `CLM-ECOLOGY_BASICS-B`; `CLM-ELECTROMAGNETISM_BASICS-B`; `CLM-FLUID_MECHANICS_BASICS-B`; `CLM-GENETICS_BASICS-B`; `CLM-GENOMICS_BASICS-B`; `CLM-GEOLOGY_BASICS-B`; `CLM-LOGIC_BASICS-B`; `CLM-OCEANOGRAPHY_BASICS-B`; `CLM-OPERATING_SYSTEMS_BASICS-B`; `CLM-ORGANIC_CHEMISTRY_BASICS-B`; `CLM-PSYCHOLOGY_BASICS-B`; `CLM-SOCIOLOGY_BASICS-B`.

### Family C — specialist review/limits principle (20 Claims)

`Базовое знание по {slice-slug} не заменяет специализированную проверку, когда вывод зависит от условий, измерений или профессиональной оценки.`

`CLM-ANTHROPOLOGY_BASICS-C`; `CLM-BIOCHEMISTRY_BASICS-C`; `CLM-CELL_BIOLOGY_BASICS-C`; `CLM-CIVIL_ENGINEERING_BASICS-C`; `CLM-CLIMATE_SCIENCE_BASICS-C`; `CLM-COMPUTER_NETWORKS_BASICS-C`; `CLM-COMPUTER_SCIENCE_ALGORITHMS_BASICS-C`; `CLM-DATA_SCIENCE_BASICS-C`; `CLM-ECOLOGY_BASICS-C`; `CLM-ELECTROMAGNETISM_BASICS-C`; `CLM-FLUID_MECHANICS_BASICS-C`; `CLM-GENETICS_BASICS-C`; `CLM-GENOMICS_BASICS-C`; `CLM-GEOLOGY_BASICS-C`; `CLM-LOGIC_BASICS-C`; `CLM-OCEANOGRAPHY_BASICS-C`; `CLM-OPERATING_SYSTEMS_BASICS-C`; `CLM-ORGANIC_CHEMISTRY_BASICS-C`; `CLM-PSYCHOLOGY_BASICS-C`; `CLM-SOCIOLOGY_BASICS-C`.

## 3. Required adjudication

1. Do not silently deduplicate or delete these 78 candidates. Retain all IDs and historical audit traces until each group has an explicit disposition.
2. Decide whether Families A–C belong as shared editorial/learning-design metadata, a common methodology/policy record referenced by each slice, or truly need a distinct domain-specific formulation.
3. If a statement remains a Claim, verify that its `claim_type` is appropriate and that its Evidence Use points to material that supports that exact proposition; an external subject-matter overview cannot prove the adequacy of the local slice itself.
4. For the exact duplicate groups, distinguish repeated wording from legitimate shared policy; if one canonical shared rule is created, that requires a separate authorized change plan and graph/reference migration.
5. Run near-duplicate clustering beyond these templates; this pass only reports the exact duplicate groups and the three obvious templated families, not all possible semantic duplicates.

## Protected-state boundary

No Claim, Evidence Use, Source or Relation JSON was changed. No identifiers were merged, normalized in storage, renamed or deleted. These findings do not change the fixed 1,494-Claim denominator. M13 remains open; independent semantic adjudication and authorized corrections remain pending.
