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
- `vertical-slices/cold-weather-hypothermia` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/generator-carbon-monoxide-safety` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/wildfire-smoke-safety` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/extreme-heat-safety` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/home-fire-smoke-safety` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.
- `vertical-slices/flood-food-safety` — 7 Record: Source + 2 Claim + 2 Evidence Use + Context + Scope.

Все практические утверждения в срезах должны иметь явный источник и Evidence Use; для опасных доменов границы применимости фиксируются отдельно.

- carbon-monoxide-heating-safety — 7 Record.
- flood-cleanup-safety — 7 Record.
- burn-first-aid — 7 Record.

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
- `vertical-slices/emergency-waste-sanitation`
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
- `vertical-slices/nutrition-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/sleep-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.

- `vertical-slices/learning-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/mental-health-information-boundaries` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/law-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/demography-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/governance-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
- `vertical-slices/education-systems` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope.
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
