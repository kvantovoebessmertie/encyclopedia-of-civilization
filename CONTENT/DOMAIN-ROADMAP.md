# CONTENT DOMAIN ROADMAP — карта расширения корпуса

Версия: 1.0
Дата: 30 сентября 2026

## Принцип

Расширяем не количество JSON, а покрытие человеческих вопросов. Каждый новый домен обязан иметь:
- понятную пользовательскую цель;
- реальные проверяемые источники;
- минимально достаточный набор Record;
- Scope/Context там, где они меняют смысл;
- Evidence Use для Claims;
- Provenance;
- regression test;
- Human View;
- package/recovery evidence.

Новый предметный домен сам по себе не является основанием для нового Record type.

## Волна A — фундаментальные знания

### A1. Математика
Цель: базовые понятия количества, измерения, вероятности и математических утверждений.
Кандидатные срезы: units-and-measurement, ratios-and-percentages, probability-basics.
Основные паттерны: Source → Claim → Evidence Use → Scope/Context.
Источники: национальные метрологические/образовательные стандарты и первичные учебные материалы.

### A2. Физика
Цель: базовые наблюдаемые физические величины и законы с явными ограничениями применимости.
Кандидатные срезы: motion-basics, energy-basics, temperature-basics.
Паттерны: Claim → Evidence Use; Scope/Context; при необходимости Assessment/Inference.
Источники: национальные метрологические и научные институты.

### A3. Химия
Цель: базовые вещества, реакции и свойства без перехода к опасным практическим инструкциям.
Кандидатные срезы: matter-basics, mixtures-and-solutions, acid-base-basics.
Паттерны: Claim → Evidence Use → Context/Scope.
Опасные процедуры не входят в срез без отдельной safety review.

### A4. Биология
Цель: базовые клеточные, генетические и экосистемные понятия.
Кандидатные срезы: cell-basics, genetics-basics, ecosystems-basics.
Паттерны: Claim → Evidence Use; Context/Scope.

### A5. Земля и космос
Цель: базовые процессы Земли и наблюдаемой астрономии.
Кандидатные срезы: earth-system-basics, solar-system-basics, seasons-and-orbits.
Паттерны: Event/State/Relation там, где это действительно необходимо.

## Волна B — человек

- anatomy-basics
- physiology-basics
- nutrition-basics
- sleep-basics
- learning-basics
- mental-health-information-boundaries

Для медицинских тем: источник и ограничения обязательны; публикация не превращается в индивидуальную медицинскую рекомендацию.

## Волна C — общество и институты

- law-basics
- economics-basics
- demography-basics
- governance-basics
- education-systems
- culture-and-language

Для политических/правовых тем фиксируются юрисдикция, дата действия и исторический контекст.

## Волна D — технологии и инфраструктура

- computing-basics
- networks-basics
- energy-basics
- materials-basics
- manufacturing-basics
- infrastructure-basics

## Волна E — история цивилизаций

- chronology-methods
- archaeology-basics
- early-agriculture
- urbanization
- writing-systems
- trade-networks
- state-formation

Исторические Claims не должны автоматически превращаться в причинные объяснения: temporal sequence ≠ causality.

## Волна F — практическая безопасность

Уже начатый emergency-контур продолжается только там, где есть реальная потребность и качественные источники:
- fire;
- flood;
- heat/cold;
- water;
- sanitation;
- first aid;
- infrastructure outages.

Опасные действия проходят усиленную semantic + human-safety проверку.

## Приоритизация нового среза

Перед созданием среза фиксируются:

1. вопрос пользователя;
2. ценность покрытия;
3. источники;
4. применимые Record types;
5. семантические паттерны;
6. Scope/Context;
7. риски неправильного применения;
8. критерий завершения;
9. regression test;
10. release evidence.

## Размер волны

Не устанавливается искусственный лимит Records. Срез считается завершённым по Definition of Done, а не по количеству.

## Следующая рабочая очередь

1. Математика: units-and-measurement.
2. Математика: ratios-and-percentages.
3. Физика: motion-basics.
4. Физика: energy-basics.
5. Химия: matter-basics.
6. Биология: cell-basics.
7. Земля: earth-system-basics.
8. Человек: anatomy-basics.
9. Общество: economics-basics.
10. Технологии: computing-basics.

После первой десятки — cross-domain semantic audit и новый release baseline.

## Архитектурная граница

Ни один из перечисленных доменов не требует нового Record type на этапе планирования. Если реальный контент покажет недостаточность существующей модели, сначала оформляется Entity Discipline + ADR, затем меняются schema/validator/tests и только после этого создаётся контент.


## Phase 4 — fourth ten-slice expansion (30 сентября 2026)

Следующая десятка закрывает оставшийся контур Волны D и основную часть Волны E, затем начинает Волную F:
- infrastructure-basics
- chronology-methods
- archaeology-basics
- early-agriculture
- urbanization
- writing-systems
- trade-networks
- state-formation
- fire
- flood

Критерий завершения: каждый срез имеет Source → 3 Claims → 3 Evidence Use → Context → Scope, dedicated regression, документационный registry и прохождение полного Reference/Release Gate. Для исторических срезов temporal sequence ≠ causality; для safety-срезов публикация не заменяет указания местных экстренных служб.


## Wave F — practical safety conformance checkpoint — 30 сентября 2026

Wave F is treated as a content-coverage and evidence checkpoint, not as a new architectural layer. The existing emergency/safety corpus already covers the roadmap domains: fire, flood, heat/cold, water, sanitation, first aid, and infrastructure/outages.

### Coverage matrix

| Domain | Existing slices | Coverage boundary |
|---|---|---|
| Fire | fire; home-fire-smoke-safety; wildfire-smoke-safety | basic fire/smoke/wildfire safety; no hazardous firefighting procedures |
| Flood | flood; flood-cleanup-safety; flood-food-safety | warning/response, cleanup and food-safety boundaries |
| Heat/cold | extreme-heat-safety; cold-weather-hypothermia | environmental exposure and basic protective information |
| Water | water; water-filter-assessment; chemical-water-advisory; emergency-water-storage-state | water availability, treatment assessment, contamination advisories, storage state |
| Sanitation | emergency-hand-hygiene; emergency-waste-sanitation; septic-system-emergency | hygiene, waste and septic emergency boundaries |
| First aid | burn-first-aid | basic burn first aid; not a substitute for emergency medical care |
| Infrastructure/outages | infrastructure-basics; power-outage-food; emergency-lighting-safety; emergency-alert-warning; generator-carbon-monoxide-safety | outage continuity, alerts, lighting, food and generator/CO safety |
| Related hazard coverage | earthquake-protective-action; earthquake-aftershock-safety; carbon-monoxide-heating-safety | cross-cutting emergency safety already represented in the corpus |

### Wave F closure criteria

A Wave F slice is closed only when its canonical records, source/evidence boundary, Context/Scope, dedicated regression, Human View, package/recovery evidence and Reference/Release Gate are green. Existing slices are not re-authored merely because the wave is being closed; they are audited against the same criteria.

### Safety-specific semantic checks

1. A warning is not converted into a universal instruction when local authority guidance controls the action.
2. Emergency-service escalation remains visible where the consequence of delay can be material.
3. Hazardous procedures are not inferred from descriptive safety knowledge.
4. Context and Scope remain attached to claims whose validity depends on conditions, equipment or jurisdiction.
5. Unknown/unverified information is never rendered as a safe default.
6. Human View must preserve warnings, limitations and source role rather than only the action text.
7. Offline/package recovery must preserve the same safety semantics as canonical records.

### Closure status

The Wave F coverage map is complete at the roadmap-category level. Remaining work is evidence closure: dedicated regression and full Reference/Release Gate confirmation for the current corpus. No new Record type is introduced by Wave F.


## Fifth ten-slice expansion — 30 September 2026

Next working ten after the v1.4 67-slice corpus:
1. units-and-measurement
2. geology-basics
3. weather-basics
4. climate-basics
5. ocean-basics
6. soil-basics
7. agriculture-basics
8. food-preservation-basics
9. shelter-basics
10. construction-basics

Closure sequence: dedicated regression → full cross-domain audit → Reference/Release Gate → release baseline.
