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

- `vertical-slices/cross-slice-linkage` — 6 Record: 1 Context + 5 Relation records связывают существующие доменные срезы без объединения их Claims.
