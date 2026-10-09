# CONTENT — содержательный корпус

Каталог предназначен для реальных записей знаний проекта.

Это **не новый нормативный слой**. Семантика записей определяется FOUNDATION, STANDARD и IMPLEMENTATION 000–021.

## Принцип

Содержательный корпус строится как набор канонических Record, а не как коллекция свободно написанных статей.

Минимальная цепочка первого вертикального среза:

1. Source
2. Claim
3. Evidence Use
4. Scope / Context при необходимости
5. Provenance
6. версия и completion status
7. validation
8. conformance
9. publication
10. recovery

## Структура

Будущая структура корпуса должна позволять отделять:

- канонические Record;
- источники;
- манифесты пакетов;
- производные публикации;
- тестовые fixtures.

Нормативные документы не должны дублироваться в CONTENT.

## Содержательные вертикальные срезы

Каждый срез создаётся только после прохождения Authoring Contract и должен использовать существующие типы без искусственного введения новых Record types.

Текущие срезы:
- `vertical-slices/water` — 1 Source + 3 Claim + 3 Evidence Use;
- `vertical-slices/power-outage-food` — 1 Source + 3 Claim + 3 Evidence Use + 3 Context + 3 Scope;
- `vertical-slices/emergency-hand-hygiene` — 1 Source + 1 Claim + 1 Evidence Use + 1 Context + 1 Scope + 1 Process + 2 Action + 1 Result;
- `vertical-slices/water-filter-assessment` — 8 Record: Source + Claim + Evidence Use + Context + Scope + Assessment + Inference;
- `vertical-slices/earthquake-protective-action` — 10 Record: Source + Claim + Evidence Use + Context + Scope + Event + Decision + Action + Result;
- `vertical-slices/emergency-water-storage-state` — 10 Record: record + Source + Claim + Evidence Use + Context + Scope + 2 State + Relation + Identity;
- `vertical-slices/source-provenance-authorship-trust` — 7 Record: Source + record + Claim + Evidence Use + Provenance + Authorship Contribution + Trust/Reputation.
- `vertical-slices/septic-system-emergency` — 5 Record: Source + Claim + Evidence Use + Context + Scope.
- `vertical-slices/cold-weather-hypothermia` — 14 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope + independent emergency evidence.
- `vertical-slices/generator-carbon-monoxide-safety` — 12 Record: 2 Source + 3 Claim + 4 Evidence Use + Context + Scope + independent emergency escalation evidence.
- `vertical-slices/wildfire-smoke-safety` — 12 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope + emergency escalation.
- `vertical-slices/extreme-heat-safety` — 10 Record: 2 Source + 3 Claim + 3 Evidence Use + Context + Scope + emergency escalation.
- `vertical-slices/home-fire-smoke-safety` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/flood-food-safety` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.

Все практические утверждения в срезах должны иметь явный источник и Evidence Use; для опасных доменов границы применимости фиксируются отдельно.

- `vertical-slices/carbon-monoxide-heating-safety` — 13 Record: 3 Source + 4 Claim + 4 Evidence Use + Context + Scope + direct CPSC emergency evidence.
- flood-cleanup-safety — 12 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope + re-entry hazard escalation.
- burn-first-aid — 12 Record: 3 Source + 3 Claim + 4 Evidence Use + Context + Scope + independent ABA emergency evidence.

- chemical-water-advisory — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.

- seed-storage-basics — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- hand-tool-safety — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.

- `vertical-slices/si-units-basics` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/time-standard-basics` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.

## Machine-checked slice registry

- `vertical-slices/burn-first-aid`
- `vertical-slices/carbon-monoxide-heating-safety`
- `vertical-slices/chemical-water-advisory`
- `vertical-slices/cold-weather-hypothermia`
- `vertical-slices/earthquake-aftershock-safety`
- `vertical-slices/earthquake-protective-action`
- `vertical-slices/emergency-hand-hygiene`
- `vertical-slices/emergency-lighting-safety`
- `vertical-slices/emergency-waste-sanitation` — 12 Record: 2 Source + 3 Claim + 4 Evidence Use + Context + Scope + hazardous-waste boundary escalation.
- `vertical-slices/emergency-water-storage-state`
- `vertical-slices/extreme-heat-safety`
- `vertical-slices/flood-cleanup-safety`
- `vertical-slices/flood-food-safety`
- `vertical-slices/generator-carbon-monoxide-safety`
- `vertical-slices/hand-tool-safety`
- `vertical-slices/home-fire-smoke-safety`
- `vertical-slices/power-outage-food`
- `vertical-slices/seed-storage-basics`
- `vertical-slices/septic-system-emergency`
- `vertical-slices/source-provenance-authorship-trust`
- `vertical-slices/water-filter-assessment`
- `vertical-slices/water`
- `vertical-slices/wildfire-smoke-safety`
- `vertical-slices/si-units-basics`
- `vertical-slices/time-standard-basics`

- `vertical-slices/cross-slice-linkage` — 7 Record: 1 Context + 6 Relation records связывают существующие доменные срезы без объединения их Claims.

- `vertical-slices/emergency-alert-warning` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.

- `vertical-slices/ratios-and-percentages` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/probability-basics` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/motion-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/energy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/matter-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/cell-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/earth-system-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/anatomy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/economics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/computing-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

- `vertical-slices/temperature-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/mixtures-and-solutions` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/acid-base-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/genetics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/ecosystems-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/solar-system-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/seasons-and-orbits` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/physiology-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/nutrition-basics` — 12 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope.
- `vertical-slices/sleep-basics` — 11 Record: 2 Source + 3 Claim + 4 Evidence Use + Context + Scope; independent CDC sleep-health evidence.

- `vertical-slices/learning-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/mental-health-information-boundaries` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/law-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/demography-basics` — 12 Record: 2 Source + 3 Claim + 5 Evidence Use + Context + Scope; WPP 2024 methodology links for projection assumptions.
- `vertical-slices/governance-basics` — 11 Record: 2 Source + 3 Claim + 4 Evidence Use + Context + Scope; World Bank WGI comparative evidence.
- `vertical-slices/education-systems` — 11 Record: 2 Source + 3 Claim + 4 Evidence Use + Context + Scope; OECD Education at a Glance comparative evidence.
- `vertical-slices/culture-and-language` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/networks-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/materials-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/manufacturing-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

- `vertical-slices/infrastructure-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/chronology-methods` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/archaeology-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/early-agriculture` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/urbanization` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/writing-systems` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/trade-networks` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/state-formation` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/fire` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/flood` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.


## Fifth ten-slice expansion — semantic closure

Completed slices:
- `vertical-slices/units-and-measurement` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/geology-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/weather-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/climate-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/ocean-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/soil-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/agriculture-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/food-preservation-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/shelter-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/construction-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

These ten slices require dedicated regression, Human View, package/recovery evidence and full Reference/Release Gate before release-baseline promotion.

## Machine-checked slice registry — fifth ten expansion

- `vertical-slices/units-and-measurement`
- `vertical-slices/geology-basics`
- `vertical-slices/weather-basics`
- `vertical-slices/climate-basics`
- `vertical-slices/ocean-basics`
- `vertical-slices/soil-basics`
- `vertical-slices/agriculture-basics`
- `vertical-slices/food-preservation-basics`
- `vertical-slices/shelter-basics`
- `vertical-slices/construction-basics`


## Fifth ten-slice expansion

- units-and-measurement
- geology-basics
- weather-basics
- climate-basics
- ocean-basics
- soil-basics
- agriculture-basics
- food-preservation-basics
- shelter-basics
- construction-basics

Each slice uses Source → 3 Claims → 3 Evidence Use → Context → Scope and has dedicated regression coverage.


## Sixth ten-slice expansion — 30 September 2026

New slices:
- `vertical-slices/astronomy-observation-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/electricity-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/statistics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/maps-and-navigation-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/telecommunications-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/money-and-banking-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/public-health-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/waste-management-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/transportation-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/information-literacy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

The sixth expansion adds 90 Records without introducing a new Record type.


## Seventh ten-slice expansion — 30 September 2026

New slices:
- `vertical-slices/chemical-reactions-basics`
- `vertical-slices/thermodynamics-basics`
- `vertical-slices/waves-and-sound-basics`
- `vertical-slices/optics-basics`
- `vertical-slices/magnetism-basics`
- `vertical-slices/evolution-basics`
- `vertical-slices/microbiology-basics`
- `vertical-slices/plant-biology-basics`
- `vertical-slices/geographic-coordinates-basics`
- `vertical-slices/ancient-civilizations-basics`

The seventh expansion adds 90 Records without introducing a new Record type.


## Eighth ten-slice expansion — 30 September 2026

New slices:
- vertical-slices/neuroscience-basics
- vertical-slices/immunology-basics
- vertical-slices/epidemiology-basics
- vertical-slices/ethics-basics
- vertical-slices/linguistics-basics
- vertical-slices/philosophy-basics
- vertical-slices/architecture-basics
- vertical-slices/food-science-basics
- vertical-slices/renewable-energy-basics
- vertical-slices/robotics-basics

The eighth expansion adds 90 Records without introducing a new Record type.


## Ninth ten-slice expansion — 30 September 2026

- vertical-slices/genomics-basics
- vertical-slices/biochemistry-basics
- vertical-slices/organic-chemistry-basics
- vertical-slices/mechanics-basics
- vertical-slices/fluid-mechanics-basics
- vertical-slices/electromagnetism-basics
- vertical-slices/computer-science-algorithms-basics
- vertical-slices/data-science-basics
- vertical-slices/psychology-basics
- vertical-slices/sociology-basics

The ninth expansion adds 90 Records without introducing a new Record type.


## Tenth ten-slice expansion — 30 September 2026

- vertical-slices/cell-biology-basics
- vertical-slices/genetics-basics
- vertical-slices/ecology-basics
- vertical-slices/geology-basics
- vertical-slices/climate-science-basics
- vertical-slices/oceanography-basics
- vertical-slices/materials-science-basics
- vertical-slices/civil-engineering-basics
- vertical-slices/computer-networks-basics
- vertical-slices/operating-systems-basics

The tenth expansion adds 90 Records without introducing a new Record type.


Tenth expansion completion note: the tenth wave is now complete with two previously unregistered slices added: vertical-slices/logic-basics and vertical-slices/anthropology-basics. Final target: 127 vertical slices / 1098 Records.


## v2.1 — fifty-domain expansion wave

Добавлены 50 новых предметных срезов. Каждый использует существующую цепочку Source → 3 Claims → 3 Evidence Use → Context → Scope и отдельный regression test; новые Record types не вводились.

- `vertical-slices/algebra-basics` — 9 Record.
- `vertical-slices/geometry-basics` — 9 Record.
- `vertical-slices/trigonometry-basics` — 9 Record.
- `vertical-slices/calculus-basics` — 9 Record.
- `vertical-slices/linear-algebra-basics` — 9 Record.
- `vertical-slices/number-theory-basics` — 9 Record.
- `vertical-slices/combinatorics-basics` — 9 Record.
- `vertical-slices/numerical-methods-basics` — 9 Record.
- `vertical-slices/measurement-uncertainty-basics` — 9 Record.
- `vertical-slices/scientific-method-basics` — 9 Record.
- `vertical-slices/hydrology-basics` — 9 Record.
- `vertical-slices/meteorology-basics` — 9 Record.
- `vertical-slices/volcanology-basics` — 9 Record.
- `vertical-slices/seismology-basics` — 9 Record.
- `vertical-slices/paleontology-basics` — 9 Record.
- `vertical-slices/geomorphology-basics` — 9 Record.
- `vertical-slices/mineralogy-basics` — 9 Record.
- `vertical-slices/petrology-basics` — 9 Record.
- `vertical-slices/atmospheric-science-basics` — 9 Record.
- `vertical-slices/remote-sensing-basics` — 9 Record.
- `vertical-slices/zoology-basics` — 9 Record.
- `vertical-slices/conservation-biology-basics` — 9 Record.
- `vertical-slices/developmental-biology-basics` — 9 Record.
- `vertical-slices/virology-basics` — 9 Record.
- `vertical-slices/parasitology-basics` — 9 Record.
- `vertical-slices/microbiome-basics` — 9 Record.
- `vertical-slices/behavioral-biology-basics` — 9 Record.
- `vertical-slices/plant-physiology-basics` — 9 Record.
- `vertical-slices/biodiversity-basics` — 9 Record.
- `vertical-slices/ecophysiology-basics` — 9 Record.
- `vertical-slices/databases-basics` — 9 Record.
- `vertical-slices/programming-languages-basics` — 9 Record.
- `vertical-slices/software-engineering-basics` — 9 Record.
- `vertical-slices/cybersecurity-basics` — 9 Record.
- `vertical-slices/cryptography-basics` — 9 Record.
- `vertical-slices/human-computer-interaction-basics` — 9 Record.
- `vertical-slices/distributed-systems-basics` — 9 Record.
- `vertical-slices/cloud-computing-basics` — 9 Record.
- `vertical-slices/computer-architecture-basics` — 9 Record.
- `vertical-slices/artificial-intelligence-basics` — 9 Record.
- `vertical-slices/accounting-basics` — 9 Record.
- `vertical-slices/macroeconomics-basics` — 9 Record.
- `vertical-slices/microeconomics-basics` — 9 Record.
- `vertical-slices/finance-basics` — 9 Record.
- `vertical-slices/organizational-behavior-basics` — 9 Record.
- `vertical-slices/education-science-basics` — 9 Record.
- `vertical-slices/public-administration-basics` — 9 Record.
- `vertical-slices/demographic-methods-basics` — 9 Record.
- `vertical-slices/urban-planning-basics` — 9 Record.
- `vertical-slices/history-methods-basics` — 9 Record.

Контрольная точка после расширения: **177 вертикальных срезов / 1548 Records / 19 Record types** (до финального полного аудита и release baseline).


## Methods and reasoning working expansion

- `vertical-slices/critical-thinking-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/causal-inference-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/research-design-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/decision-theory-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/risk-analysis-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/information-theory-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/data-visualization-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/scientific-communication-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/modeling-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/systems-thinking-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.


## BLOCK 1 — Wave 1
- `vertical-slices/epistemology-basics` — 9 Record
- `vertical-slices/philosophy-of-science-basics` — 9 Record
- `vertical-slices/philosophy-of-mind-basics` — 9 Record
- `vertical-slices/philosophy-of-language-basics` — 9 Record
- `vertical-slices/metaphysics-basics` — 9 Record
- `vertical-slices/philosophy-of-mathematics-basics` — 9 Record

Контрольная точка: **193 vertical slices / 1692 Records / 19 Record types**.


## BLOCK 1 — Wave 2

- `vertical-slices/communication-basics` — 9 Record
- `vertical-slices/logistics-basics` — 9 Record
- `vertical-slices/supply-chain-basics` — 9 Record
- `vertical-slices/project-management-basics` — 9 Record
- `vertical-slices/quality-control-basics` — 9 Record
- `vertical-slices/labor-markets-basics` — 9 Record
- `vertical-slices/negotiation-basics` — 9 Record
- `vertical-slices/conflict-resolution-basics` — 9 Record
- `vertical-slices/reliability-basics` — 9 Record
- `vertical-slices/requirements-engineering-basics` — 9 Record

Working expansion target: **203 vertical slices / 1782 Records / 19 Record types**. Full audit and release evidence remain pending until all gates are green.


## Next content expansion — 1 October 2026

Clean checkpoint: `68d75aa7dc9a1199ab754c8d5a457cf956bd1c54`.

Next ten slices:
- `vertical-slices/game-theory-basics`
- `vertical-slices/optimization-basics`
- `vertical-slices/control-systems-basics`
- `vertical-slices/compiler-basics`
- `vertical-slices/signal-processing-basics`
- `vertical-slices/metrology-basics`
- `vertical-slices/queueing-theory-basics`
- `vertical-slices/graph-theory-basics`
- `vertical-slices/formal-methods-basics`
- `vertical-slices/software-testing-basics`

Each slice uses Source → 3 Claims → 3 Evidence Use → Context → Scope and a dedicated regression. No new Record types. Closure requires full content-depth, cross-domain, adversarial, corpus, Human View, offline/recovery, Reference Tests and Release Gate evidence.

- `vertical-slices/modeling-and-simulation-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/operations-research-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/systems-engineering-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/safety-engineering-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/reliability-engineering-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/maintenance-engineering-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/structural-engineering-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/heat-transfer-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/agrifood-systems-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/ergonomics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

## Next content expansion — physical sciences, cognition and culture — 2 October 2026

- statistics-basics
- thermodynamics-basics
- optics-basics
- quantum-physics-basics
- astronomy-basics
- geophysics-basics
- neuroscience-basics
- archaeology-basics
- art-history-basics
- music-theory-basics

Each slice uses Source → 3 Claims → 3 Evidence Use → Context → Scope and a dedicated regression test. No new Record types are introduced. Working target after this wave: **228 vertical slices / 2007 Records / 19 Record types**.

- vertical-slices/quantum-physics-basics
- vertical-slices/astronomy-basics
- vertical-slices/geophysics-basics
- vertical-slices/art-history-basics
- vertical-slices/music-theory-basics


## 2026-10-02 — Practical resilience expansion registration

The current working corpus adds ten practical continuity and resilience domains:
- vertical-slices/forestry-basics
- vertical-slices/fisheries-basics
- vertical-slices/livestock-systems-basics
- vertical-slices/food-safety-basics
- vertical-slices/wastewater-basics
- vertical-slices/disaster-risk-reduction-basics
- vertical-slices/emergency-management-basics
- vertical-slices/energy-storage-basics
- vertical-slices/electrical-safety-basics
- vertical-slices/public-risk-communication-basics

Current working target: **238 vertical slices / 2097 Records / 19 Record types**.


## 2026-10-02 — Society and institutions expansion

- `vertical-slices/political-science-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/international-relations-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/diplomacy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/human-rights-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/constitutional-systems-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/public-policy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/labor-relations-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/public-finance-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/development-economics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/behavioral-economics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

Machine-checked registration is provided by the dedicated regression tests and full-corpus coverage checks.


## 2026-10-02 — Gap Map R1 accelerated wave 1

Ten new non-duplicate slices were added from the Gap Map:
- molecular-biology-basics
- particle-physics-basics
- physical-chemistry-basics
- analytical-chemistry-basics
- web-systems-basics
- information-retrieval-basics
- software-architecture-basics
- water-infrastructure-basics
- housing-systems-basics
- environmental-health-basics

Each new slice uses Source + 3 Claims + 3 Evidence Use + Context + Scope and a dedicated regression test. No new Record type was introduced. Wave target: **258 vertical slices / 2277 Records / 19 Record types**.


## Gap Map R1 — accelerated Wave 1 registry

- vertical-slices/molecular-biology-basics
- vertical-slices/particle-physics-basics
- vertical-slices/physical-chemistry-basics
- vertical-slices/analytical-chemistry-basics
- vertical-slices/web-systems-basics
- vertical-slices/information-retrieval-basics
- vertical-slices/software-architecture-basics
- vertical-slices/water-infrastructure-basics
- vertical-slices/housing-systems-basics
- vertical-slices/environmental-health-basics

Wave 1 adds 90 Records: 258 vertical slices / 2277 Records / 19 Record types.


## Gap Map R2 — accelerated Wave 2 registry — 2 October 2026

Selected after CLEAN CHECKPOINT R4 using the Gap Map prioritization rule. These ten domains are new to the corpus, use existing Record types only, and are intended as one controlled 10-slice CI unit.

- vertical-slices/pathology-basics
- vertical-slices/pharmacology-information-basics
- vertical-slices/public-health-surveillance-basics
- vertical-slices/rehabilitation-basics
- vertical-slices/reproductive-health-information-boundaries
- vertical-slices/nuclear-physics-information-basics
- vertical-slices/physiology-of-systems-basics
- vertical-slices/marine-biology-basics
- vertical-slices/environmental-biology-basics
- vertical-slices/electrical-grid-basics

Wave 2 target: **268 vertical slices / 2367 Records / 19 Record types**.


## Gap Map R3 — accelerated Wave 3 registry — 3 October 2026

Ten new non-duplicate slices were added from the Gap Map after CLEAN CHECKPOINT R5. Each uses the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope pattern and existing Record types only.

- vertical-slices/soil-science-basics
- vertical-slices/water-quality-basics
- vertical-slices/wastewater-treatment-basics
- vertical-slices/geotechnical-engineering-basics
- vertical-slices/bridge-engineering-basics
- vertical-slices/railway-systems-basics
- vertical-slices/semiconductor-basics
- vertical-slices/power-electronics-basics
- vertical-slices/biostatistics-basics
- vertical-slices/occupational-health-basics

Wave 3 target: **278 vertical slices / 2457 Records / 19 Record types**.

## Gap Map R4 — accelerated Wave 4 registry — 3 October 2026

Ten new non-duplicate slices were added after CLEAN CHECKPOINT R6. Each uses the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope pattern and existing Record types only.

- vertical-slices/bioinformatics-basics
- vertical-slices/biomedical-engineering-basics
- vertical-slices/environmental-engineering-basics
- vertical-slices/toxicology-basics
- vertical-slices/epigenetics-basics
- vertical-slices/systems-biology-basics
- vertical-slices/genetic-engineering-basics
- vertical-slices/medical-imaging-basics
- vertical-slices/water-resource-management-basics
- vertical-slices/geochemistry-basics

Wave 4 target: **288 vertical slices / 2547 Records / 19 Record types**. Full Reference Tests and Release Gate validation are required before checkpoint closure.


## Wave 5 — 3 October 2026

- vertical-slices/clinical-trials-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/health-systems-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/disaster-response-logistics-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/agricultural-engineering-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/building-science-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/industrial-process-safety-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/data-governance-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/digital-preservation-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/supply-chain-risk-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- vertical-slices/public-works-basics — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

## Machine-checked slice registry — Wave 5

- vertical-slices/clinical-trials-basics
- vertical-slices/health-systems-basics
- vertical-slices/disaster-response-logistics-basics
- vertical-slices/agricultural-engineering-basics
- vertical-slices/building-science-basics
- vertical-slices/industrial-process-safety-basics
- vertical-slices/data-governance-basics
- vertical-slices/digital-preservation-basics
- vertical-slices/supply-chain-risk-basics
- vertical-slices/public-works-basics


## Gap Map R6 — Wave 6

- `vertical-slices/database-systems-basics`
- `vertical-slices/energy-systems-basics`
- `vertical-slices/geographic-information-systems-basics`
- `vertical-slices/public-transport-basics`
- `vertical-slices/sanitation-basics`
- `vertical-slices/telemedicine-basics`
- `vertical-slices/wastewater-engineering-basics`
- `vertical-slices/fire-safety-basics`
- `vertical-slices/nutrition-science-basics`
- `vertical-slices/pharmacovigilance-basics`

Wave 6 adds 90 Records: **308 vertical slices / 2727 Records / 19 Record types**.


## Gap Map R7 — Wave 7

Ten new non-duplicate slices were added after CLEAN CHECKPOINT R9. Each uses the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope pattern, existing Record types only, and a dedicated regression test.

- `vertical-slices/computer-graphics-basics`
- `vertical-slices/embedded-systems-basics`
- `vertical-slices/human-ai-interaction-basics`
- `vertical-slices/industrial-safety-basics`
- `vertical-slices/information-security-operations-basics`
- `vertical-slices/sensor-systems-basics`
- `vertical-slices/supply-and-demand-infrastructure-basics`
- `vertical-slices/transportation-infrastructure-basics`
- `vertical-slices/version-control-basics`
- `vertical-slices/waste-infrastructure-basics`

Wave 7 adds 90 Records: **318 vertical slices / 2817 Records / 19 Record types**.


## Gap Map R7 — Wave 7 — 3 October 2026

- political-economy-basics
- comparative-law-basics
- administrative-law-basics
- international-law-basics
- civil-society-basics
- social-policy-basics
- taxation-basics
- labor-economics-basics
- migration-and-mobility-basics
- comparative-civilizations-basics

Wave 7 adds 90 Records: **318 vertical slices / 2817 Records / 19 Record types**.


## Gap Map R7 — Wave 7 completion — 3 October 2026

The second controlled Wave 7 unit adds ten new non-duplicate society and institutions slices. Each uses the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope pattern and existing Record types only.

- `vertical-slices/political-economy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/comparative-law-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/administrative-law-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/international-law-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/civil-society-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/social-policy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/taxation-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/labor-economics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/migration-and-mobility-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/comparative-civilizations-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

Wave 7 completion target: **328 vertical slices / 2907 Records / 19 Record types**.

## Machine-checked slice registry — Wave 7 completion

- `vertical-slices/political-economy-basics`
- `vertical-slices/comparative-law-basics`
- `vertical-slices/administrative-law-basics`
- `vertical-slices/international-law-basics`
- `vertical-slices/civil-society-basics`
- `vertical-slices/social-policy-basics`
- `vertical-slices/taxation-basics`
- `vertical-slices/labor-economics-basics`
- `vertical-slices/migration-and-mobility-basics`
- `vertical-slices/comparative-civilizations-basics`


## Gap Map R8 — Wave 8

- `vertical-slices/historical-geography-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/economic-history-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/history-of-science-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/history-of-technology-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/religious-studies-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/literature-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/cultural-anthropology-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/water-security-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/climate-adaptation-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/infrastructure-resilience-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

Wave 8 adds 90 Records without introducing a new Record type.


## Gap Map R9 — controlled Wave 9 — 3 October 2026

- `vertical-slices/history-of-medicine-basics`
- `vertical-slices/history-of-mathematics-basics`
- `vertical-slices/history-of-engineering-basics`
- `vertical-slices/cartography-basics`
- `vertical-slices/hydraulic-engineering-basics`
- `vertical-slices/food-systems-basics`
- `vertical-slices/cultural-heritage-basics`
- `vertical-slices/library-science-basics`
- `vertical-slices/archival-science-basics`
- `vertical-slices/settlement-geography-basics`

Wave 9 target: **348 vertical slices / 3090 Records / 19 Record types**. Selection is governed by RELEASE/CONTENT-GAP-MAP-2026-10-03-R9; closure requires preflight, CI and substantive audit evidence.


## Gap Map R9 — substantive audit — 3 October 2026

Wave 9 substantive audit added three evidence-disciplined cross-slice relations for cartography ↔ settlement geography, library science ↔ archival science, and history of mathematics ↔ history of engineering. Audited corpus: **348 vertical slices / 3093 Records / 19 Record types**. Independent-source depth remains non-blocking follow-up work.

> CI note: changes under `CONTENT/**` are covered by the Reference implementation test workflow.


## Gap Map R10 — 3 October 2026

New controlled engineering, spatial, recovery and acquisition layers:
- `vertical-slices/mechanical-engineering-basics`
- `vertical-slices/chemical-engineering-basics`
- `vertical-slices/industrial-engineering-basics`
- `vertical-slices/geodesy-basics`
- `vertical-slices/surveying-basics`
- `vertical-slices/mining-engineering-basics`
- `vertical-slices/disaster-recovery-basics`
- `vertical-slices/public-procurement-basics`
- `vertical-slices/building-services-engineering-basics`
- `vertical-slices/metallurgy-basics`

Wave 10 uses Source → 3 Claims → 3 Evidence Use → Context → Scope for each slice and adds 90 Records without introducing a new Record type.

CI coverage: changes to CONTENT, ROADMAP.md, or RELEASE/CONTENT-COVERAGE.json are covered by the Reference implementation test trigger.


## R10 CLEAN CHECKPOINT — Wave 10 — 3 October 2026

- verified audited state: `4c284e0b1a3d8d4042cc04e4d3a2f1fa8ff9c9d8`
- corpus: **358 vertical slices / 3187 Records / 19 Record types**
- substantive audit: `RELEASE/WAVE-10-SUBSTANTIVE-AUDIT-2026-10-03.md`
- blocking findings: **0**
- final CI: Offline Edition #484, Release Conformance Gate #1322, Reference implementation tests #1015 — all success.
- next: Gap Map R11 ten-slice expansion.


## Gap Map R11 — 4 October 2026

- `vertical-slices/measurement-science-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/calibration-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/standards-and-certification-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/research-methods-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/statistics-inference-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/quantum-mechanics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/manufacturing-processes-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/quality-management-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/human-factors-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/environmental-policy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

Wave 11 target: **368 vertical slices / 3277 Records / 19 Record types**. Closure requires preflight, CI and substantive audit.


## R11 substantive audit / CLEAN checkpoint — 4 October 2026

- audited corpus: **368 vertical slices / 3282 Records / 19 Record types**
- substantive audit: `RELEASE/WAVE-11-SUBSTANTIVE-AUDIT-2026-10-04.md`
- blocking findings: **0**
- architectural changes: **0**
- deterministic validator gaps: **0**
- cross-slice relations added: **5**
- audit SHA: `33d3930150acd08aa164cc9f1bdb0b3b2c074611`
- audit CI: Offline Edition #494, Release Conformance Gate #1332, Reference implementation tests #1025 — all success.
- disposition: pending final CI on checkpoint metadata; next controlled step is Gap Map R12 ten-slice expansion.


## Gap Map R12 — 4 October 2026

- groundwater-basics
- air-quality-basics
- plant-pathology-basics
- entomology-basics
- antimicrobial-resistance-basics
- electrical-machines-basics
- power-systems-basics
- econometrics-basics
- ethnobotany-basics
- soil-microbiology-basics

Wave 12 target: **378 vertical slices / 3372 Records / 19 Record types**. Closure requires preflight, CI, substantive audit and final CLEAN checkpoint.


## Gap Map R12 — canonical registration

- `vertical-slices/groundwater-basics`
- `vertical-slices/air-quality-basics`
- `vertical-slices/plant-pathology-basics`
- `vertical-slices/entomology-basics`
- `vertical-slices/antimicrobial-resistance-basics`
- `vertical-slices/electrical-machines-basics`
- `vertical-slices/power-systems-basics`
- `vertical-slices/econometrics-basics`
- `vertical-slices/ethnobotany-basics`
- `vertical-slices/soil-microbiology-basics`


## R12 substantive audit — 4 October 2026

Audited state: **378 vertical slices / 3377 Records / 19 Record types**. Five cross-slice relations added. Blocking findings: **0**. Audit artifact: `RELEASE/WAVE-12-SUBSTANTIVE-AUDIT-2026-10-04.md`.


## R12 CLEAN CHECKPOINT — 4 October 2026

R12 substantive audit is complete with **0 blocking findings**. Audited content state: **378 vertical slices / 3377 Records / 19 Record types**. Final audited content SHA: `03529dfd19ce1e8dac1dc53bf8b78d298d32be4d`.

Final CI on audited content: Offline Edition #500, Reference implementation tests #1031, Release Conformance Gate #1338 — all success. This checkpoint is official after the audited content and checkpoint metadata each passed all three release gates.


## Gap Map R13 — canonical registration

- `vertical-slices/international-trade-basics`
- `vertical-slices/energy-markets-basics`
- `vertical-slices/risk-management-basics`
- `vertical-slices/labor-law-basics`
- `vertical-slices/social-statistics-basics`
- `vertical-slices/democratic-institutions-basics`
- `vertical-slices/migration-basics`
- `vertical-slices/water-governance-basics`
- `vertical-slices/public-budgeting-basics`
- `vertical-slices/energy-policy-basics`


## R14 — controlled ten-slice expansion — 4 October 2026

- `vertical-slices/disaster-financing-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/energy-efficiency-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/environmental-economics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/food-distribution-basics` — 12 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/insurance-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/medical-devices-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/public-data-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/social-protection-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/traceability-systems-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/water-treatment-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.

## R15 — controlled ten-slice expansion — 4 October 2026

- `vertical-slices/financial-markets-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/central-banking-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/competition-policy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/consumer-protection-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/human-rights-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/electoral-systems-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/constitutional-law-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/public-administration-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/intellectual-property-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/social-insurance-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.



## R15 replacement registrations
- `vertical-slices/financial-literacy-basics`
- `vertical-slices/payment-systems-basics`


## R16 — controlled ten-slice expansion — 4 October 2026

- `vertical-slices/planetary-science-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/astrophysics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/atmospheric-chemistry-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/health-economics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/vaccination-information-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/privacy-and-data-protection-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/digital-identity-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/media-literacy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/corporate-governance-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/scientific-reproducibility-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.

Wave 16 adds 90 Records without introducing a new Record type. Medical/public-health content remains general information; jurisdictional, privacy, governance, media-literacy and reproducibility boundaries are explicit.

## Machine-checked slice registry — R16

- `vertical-slices/planetary-science-basics`
- `vertical-slices/astrophysics-basics`
- `vertical-slices/atmospheric-chemistry-basics`
- `vertical-slices/health-economics-basics`
- `vertical-slices/vaccination-information-basics`
- `vertical-slices/privacy-and-data-protection-basics`
- `vertical-slices/digital-identity-basics`
- `vertical-slices/media-literacy-basics`
- `vertical-slices/corporate-governance-basics`
- `vertical-slices/scientific-reproducibility-basics`


## R17 — controlled ten-slice expansion — 4 October 2026

- `vertical-slices/open-science-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/research-integrity-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/science-policy-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/data-ethics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/information-ethics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/health-technology-assessment-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/public-health-ethics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/economic-geography-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/urban-economics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/ecotoxicology-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.

## Machine-checked slice registry — R17

- `vertical-slices/open-science-basics`
- `vertical-slices/research-integrity-basics`
- `vertical-slices/science-policy-basics`
- `vertical-slices/data-ethics-basics`
- `vertical-slices/information-ethics-basics`
- `vertical-slices/health-technology-assessment-basics`
- `vertical-slices/public-health-ethics-basics`
- `vertical-slices/economic-geography-basics`
- `vertical-slices/urban-economics-basics`
- `vertical-slices/ecotoxicology-basics`


## R18 — controlled ten-slice expansion — 4 October 2026

R18 adds ten non-duplicate practical built-environment domains. Each slice uses the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope profile and a dedicated regression test.

- vertical-slices/timber-engineering-basics
- vertical-slices/fire-protection-and-life-safety-basics
- vertical-slices/foundation-engineering-basics
- vertical-slices/building-envelope-basics
- vertical-slices/indoor-air-quality-basics
- vertical-slices/acoustics-basics
- vertical-slices/accessibility-basics
- vertical-slices/construction-safety-basics
- vertical-slices/land-use-planning-basics
- vertical-slices/construction-project-management-basics

R18 adds 90 Records: **438 vertical slices / 3917 Records / 19 Record types**.


## R19 — controlled ten-slice expansion — 5 October 2026

R19 adds ten non-duplicate cross-domain foundation slices. Each uses Source → 3 Claims → 3 Evidence Use → Context → Scope, existing Record types only, and a dedicated regression.

- `vertical-slices/asset-management-basics`
- `vertical-slices/environmental-monitoring-basics`
- `vertical-slices/water-resources-management-basics`
- `vertical-slices/resource-allocation-basics`
- `vertical-slices/systems-modeling-basics`
- `vertical-slices/inspection-basics`
- `vertical-slices/infrastructure-governance-basics`
- `vertical-slices/network-analysis-basics`
- `vertical-slices/geospatial-analysis-basics`
- `vertical-slices/sampling-basics`

R19 target: **448 vertical slices / 4007 Records / 19 Record types**.

## R19 — controlled ten-slice expansion — 5 October 2026

R19 adds ten non-duplicate foundational domains using the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope profile and dedicated regression tests.

- `vertical-slices/asset-management-basics`
- `vertical-slices/environmental-monitoring-basics`
- `vertical-slices/water-resources-management-basics`
- `vertical-slices/resource-allocation-basics`
- `vertical-slices/systems-modeling-basics`
- `vertical-slices/inspection-basics`
- `vertical-slices/infrastructure-governance-basics`
- `vertical-slices/network-analysis-basics`
- `vertical-slices/geospatial-analysis-basics`
- `vertical-slices/sampling-basics`

R19 adds 90 Records: **448 vertical slices / 4007 Records / 19 Record types**.


## R21 — controlled ten-slice expansion — 5 October 2026

R21 adds ten non-duplicate domains using the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope profile and dedicated regressions.

- `vertical-slices/electronics-basics`
- `vertical-slices/digital-communications-basics`
- `vertical-slices/robotics-engineering-basics`
- `vertical-slices/sustainable-development-basics`
- `vertical-slices/energy-security-basics`
- `vertical-slices/organizational-management-basics`
- `vertical-slices/measurement-instrumentation-basics`
- `vertical-slices/engineering-design-basics`
- `vertical-slices/scientific-publishing-basics`
- `vertical-slices/research-data-management-basics`

R21 target after authoring: **458 vertical slices / 4097 Records / 19 Record types**.


## R22 controlled ten-slice expansion

1. legal-research-basics
2. decision-analysis-basics
3. manufacturing-systems-basics
4. physiology-of-exercise-basics
5. water-resources-basics
6. disaster-response-basics
7. humanitarian-logistics-basics
8. food-security-basics
9. occupational-safety-basics
10. operations-management-basics

Target: **468 vertical slices / 4187 Records / 19 Record types**. Full corpus audit remains deferred to the next periodic checkpoint.

## R22 machine-checked slice registry

- vertical-slices/water-resources-basics
- vertical-slices/disaster-response-basics
- vertical-slices/humanitarian-logistics-basics
- vertical-slices/food-security-basics
- vertical-slices/occupational-safety-basics
- vertical-slices/operations-management-basics

- vertical-slices/legal-research-basics

- vertical-slices/decision-analysis-basics
- vertical-slices/manufacturing-systems-basics
- vertical-slices/physiology-of-exercise-basics


## R23 controlled ten-slice expansion

- `vertical-slices/market-design-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/linguistic-typology-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/planetary-geology-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/hydropower-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/ai-ethics-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/records-management-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/disaster-behavioral-health-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/food-fermentation-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/geologic-mapping-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/archival-description-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.


## P13 — Human Settlement Systems — 7 October 2026

- `vertical-slices/human-settlement-systems-basics` — 11 Record: 3 Source + 3 Claim + 3 Evidence Use + Context + Scope.
- Six justified cross-slice Relations connect the settlement-system layer with housing, infrastructure, transportation, water infrastructure, energy systems and public health.
- P13 uses existing Record types only; no new Record type is introduced.
- The slice is descriptive and source-bounded and does not provide site-specific planning, engineering design, legal determinations or live emergency instructions.


## M2 controlled maturation — current audited registration — 8 October 2026

The following existing slices were matured under the locked M2 scope. This section is the current reconciliation for these slices; earlier expansion notes remain historical records.

- `vertical-slices/measurement-uncertainty-basics` — 9 Records; 2 sources; independent BIPM/JCGM VIM evidence added.
- `vertical-slices/statistics-basics` — 9 Records; 2 sources; independent OpenStax evidence added.
- `vertical-slices/risk-management-basics` — 9 Records; 2 sources; independent COSO ERM evidence added.
- `vertical-slices/agriculture-basics` — **11 Records; 2 sources (FAO + USDA)**; no content rewrite required.
- `vertical-slices/energy-security-basics` — 9 Records; 2 sources; independent European Commission evidence added.
- `vertical-slices/geographic-coordinates-basics` — 9 Records; 2 sources; independent OGC/ISO-aligned evidence added.

M2 also adds six material cross-domain Relations, each covered by a dedicated regression. No new Record type was introduced.


## M3 controlled maturation — correction pass — 8 October 2026

The following existing slices were corrected under the locked M3 scope:
- `vertical-slices/fire-safety-basics` — 12 Records; 2 Sources; 4 Evidence Use; 1 M3 Relation.
- `vertical-slices/shelter-basics` — 12 Records; 2 Sources; 4 Evidence Use; 1 M3 Relation.
- `vertical-slices/water-resources-basics` — 12 Records; 2 Sources; 4 Evidence Use; 1 M3 Relation; substantive Claims revised to remove editorial suffixes and add domain substance.
- `vertical-slices/food-preservation-basics` — 12 Records; 2 Sources; 4 Evidence Use; 1 M3 Relation.
- `vertical-slices/scientific-method-basics` — 13 Records; 2 Sources; 4 Evidence Use; 1 additional Claim; 1 M3 Relation.
- `vertical-slices/emergency-management-basics` — 12 Records; 2 Sources; 4 Evidence Use; 1 M3 Relation.

This section is the current M3 reconciliation; earlier expansion entries remain historical. M3 remains procedurally open until post-correction re-audit and exact-head release CI are complete.


## M5 — controlled content maturation — 9 October 2026

M5 matures nine existing vertical slices; it creates no new vertical slice and no new Record type. The working baseline is the accepted M4 HEAD `83b2e3185cd92c55d53a5ce661be384508870e1a`. M4 remains closed; M5 work is isolated to `m5-content-maturation-2026-10-09`.

M5 current per-slice record shapes (content pass; subsequently accepted CLEAN at `c911c6b4ad791cb933293608e298e318a608a02f`):
- `vertical-slices/materials-science-basics` — 15 Records: 2 Source + 4 Claim + 7 Evidence Use + Context + Scope.
- `vertical-slices/energy-systems-basics` — 15 Records: 2 Source + 4 Claim + 7 Evidence Use + Context + Scope.
- `vertical-slices/water-treatment-basics` — 17 Records: 3 Source + 4 Claim + 8 Evidence Use + Context + Scope.
- `vertical-slices/sanitation-basics` — 16 Records: 3 Source + 4 Claim + 7 Evidence Use + Context + Scope.
- `vertical-slices/manufacturing-basics` — 15 Records: 2 Source + 4 Claim + 7 Evidence Use + Context + Scope.
- `vertical-slices/transportation-basics` — 15 Records: 2 Source + 4 Claim + 7 Evidence Use + Context + Scope.
- `vertical-slices/supply-chain-basics` — 16 Records: 3 Source + 4 Claim + 7 Evidence Use + Context + Scope.
- `vertical-slices/environmental-engineering-basics` — 16 Records: 3 Source + 4 Claim + 7 Evidence Use + Context + Scope.
- `vertical-slices/telecommunications-basics` — 15 Records: 3 Source + 4 Claim + 6 Evidence Use + Context + Scope.

Every M5 slice has a dedicated regression test covering record shape, source/evidence references, schema validation and semantic validation. Evidence is claim-specific; a source is not treated as supporting a claim outside its actual scope. Existing Relations are preserved; one claim-level Relation connects telecommunications continuity to energy-grid resilience.

M5 content-level substantive, evidence-independence, Human View and Relation audits are PASS. M5 was subsequently accepted CLEAN at `c911c6b4ad791cb933293608e298e318a608a02f` after exact-head CI and independent verification. The sentence above records the earlier pre-checkpoint state, not the current M5 status.


## M6 — controlled content correction — 9 October 2026

M6 is isolated to `m6-gap-map-2026-10-09`, based on the protected M5 CLEAN checkpoint `c911c6b4ad791cb933293608e298e318a608a02f`. M4 and M5 remain closed; `main` is unchanged. The locked M6 scope is six existing slices: `sleep-basics`, `learning-basics`, `law-basics`, `demography-basics`, `governance-basics`, and `education-systems`. No new vertical slice or Record type was added.

The controlled correction pass narrowed four Claims to their traceable scope, normalized the demography Context language, made all 18 existing Evidence Use descriptions claim-specific, and added targeted claim-linked Sources/Evidence Use for sleep health, comparative governance indicators, comparative education systems, and WPP age-structure/projection methodology. The WPP methodology is a companion from the same UN institution, not independent institutional corroboration. No Relation was added.

M6 slice shapes after this correction pass:
- `vertical-slices/sleep-basics` — 11 Records; 2 Sources; 4 Evidence Use; Context + Scope.
- `vertical-slices/learning-basics` — 9 Records; 1 Source; 3 Evidence Use; Context + Scope.
- `vertical-slices/law-basics` — 9 Records; 1 Source; 3 Evidence Use; Context + Scope.
- `vertical-slices/demography-basics` — 12 Records; 2 Sources; 5 Evidence Use; Context + Scope.
- `vertical-slices/governance-basics` — 11 Records; 2 Sources; 4 Evidence Use; Context + Scope.
- `vertical-slices/education-systems` — 11 Records; 2 Sources; 4 Evidence Use; Context + Scope.

The working corpus is 479 vertical slices / 4,763 Records / 605 Sources / 1,639 Evidence Use / 64 Relations / 19 Record types. M6 remains OPEN until post-correction substantive, evidence, Human View, and Relation checks are complete, the exact final HEAD passes Reference + Release Conformance Gate + Offline Edition 3/3, and independent verification is recorded.


## M7 focused craft slices (2026-10-09)

- `vertical-slices/woodworking-basics` — 12 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope.
- `vertical-slices/papermaking-basics` — 12 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope.
- `vertical-slices/ceramics-basics` — 12 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope.
- `vertical-slices/textile-fibre-processing-basics` — 12 Record: 2 Source + 4 Claim + 4 Evidence Use + Context + Scope.
