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


## Sixth ten-slice expansion — 30 September 2026

New working ten after the v1.5 77-slice control point:
1. astronomy-observation-basics
2. electricity-basics
3. statistics-basics
4. maps-and-navigation-basics
5. telecommunications-basics
6. money-and-banking-basics
7. public-health-basics
8. waste-management-basics
9. transportation-basics
10. information-literacy-basics

Closure sequence: dedicated regression → full cross-domain semantic/content audit → Reference/Release Gate → v1.6 baseline.
No new Record type is introduced by this expansion.


## Seventh ten-slice expansion — 30 September 2026

Working ten after the v1.6 control point:
1. chemical-reactions-basics
2. thermodynamics-basics
3. waves-and-sound-basics
4. optics-basics
5. magnetism-basics
6. evolution-basics
7. microbiology-basics
8. plant-biology-basics
9. geographic-coordinates-basics
10. ancient-civilizations-basics

Closure sequence: dedicated regression → full cross-domain semantic/content audit → Reference/Release Gate → v1.7 baseline.
No new Record type is introduced by this expansion.


## Eighth ten-slice expansion — 30 September 2026

Working ten after the v1.7 control point:
1. neuroscience-basics
2. immunology-basics
3. epidemiology-basics
4. ethics-basics
5. linguistics-basics
6. philosophy-basics
7. architecture-basics
8. food-science-basics
9. renewable-energy-basics
10. robotics-basics

Closure sequence: dedicated regression → full cross-domain semantic/content audit → Reference/Release Gate → v1.8 baseline.
No new Record type is introduced by this expansion.


## Ninth ten-slice expansion — 30 September 2026

Working ten after the v1.8 control point:
1. genomics-basics
2. biochemistry-basics
3. organic-chemistry-basics
4. mechanics-basics
5. fluid-mechanics-basics
6. electromagnetism-basics
7. computer-science-algorithms-basics
8. data-science-basics
9. psychology-basics
10. sociology-basics

Closure sequence: dedicated regression → full cross-domain semantic/content audit → Reference/Release Gate → v1.9 baseline.
No new Record type is introduced by this expansion.


## Tenth ten-slice expansion — 30 September 2026

Working ten after the v1.9 control point:
1. cell-biology-basics
2. genetics-basics
3. ecology-basics
4. geology-basics
5. climate-science-basics
6. oceanography-basics
7. materials-science-basics
8. civil-engineering-basics
9. computer-networks-basics
10. operating-systems-basics

Closure sequence: dedicated regression → full cross-domain semantic/content audit → Reference/Release Gate → v2.0 baseline.
No new Record type is introduced by this expansion.


Tenth expansion completion note: the tenth wave is now complete with two previously unregistered slices added: vertical-slices/logic-basics and vertical-slices/anthropology-basics. Final target: 127 vertical slices / 1098 Records.


## v2.1 — fifty-domain expansion wave — 30 September 2026

Вместо искусственного ограничения десятью срезами выполнена крупная содержательная волна из пяти контролируемых десяток. Новые домены проверены на отсутствие дублей в текущем корпусе и используют существующие 19 Record types.

### Десятка 1 — математика и методология
- algebra-basics
- geometry-basics
- trigonometry-basics
- calculus-basics
- linear-algebra-basics
- number-theory-basics
- combinatorics-basics
- numerical-methods-basics
- measurement-uncertainty-basics
- scientific-method-basics

### Десятка 2 — науки о Земле
- hydrology-basics
- meteorology-basics
- volcanology-basics
- seismology-basics
- paleontology-basics
- geomorphology-basics
- mineralogy-basics
- petrology-basics
- atmospheric-science-basics
- remote-sensing-basics

### Десятка 3 — биология
- zoology-basics
- conservation-biology-basics
- developmental-biology-basics
- virology-basics
- parasitology-basics
- microbiome-basics
- behavioral-biology-basics
- plant-physiology-basics
- biodiversity-basics
- ecophysiology-basics

### Десятка 4 — вычисления и технологии
- databases-basics
- programming-languages-basics
- software-engineering-basics
- cybersecurity-basics
- cryptography-basics
- human-computer-interaction-basics
- distributed-systems-basics
- cloud-computing-basics
- computer-architecture-basics
- artificial-intelligence-basics

### Десятка 5 — экономика, общество и институты
- accounting-basics
- macroeconomics-basics
- microeconomics-basics
- finance-basics
- organizational-behavior-basics
- education-science-basics
- public-administration-basics
- demographic-methods-basics
- urban-planning-basics
- history-methods-basics

Каждый срез: Source → 3 Claims → 3 Evidence Use → Context → Scope + dedicated regression. Следующий контроль: полный corpus audit → Reference Tests → Release Gate → v2.1 baseline.


## First Content Domain Roadmap ten-slice closure — 30 September 2026

Закрываемая рабочая десятка:
1. ratios-and-percentages
2. probability-basics
3. motion-basics
4. energy-basics
5. matter-basics
6. cell-basics
7. earth-system-basics
8. anatomy-basics
9. economics-basics
10. computing-basics

Контроль: **10 slices / 86 Records / 19 Record types**, dedicated regression для каждого среза, без изменения архитектурного набора типов. После Gate следующий рабочий набор: temperature-basics, mixtures-and-solutions, acid-base-basics, genetics-basics, ecosystems-basics, solar-system-basics, seasons-and-orbits, physiology-basics, nutrition-basics, sleep-basics.


## 2026-10-02 — Practical continuity expansion (package 1)

Закрываемая первая часть новой волны:
1. forestry-basics
2. fisheries-basics
3. livestock-systems-basics
4. food-safety-basics
5. wastewater-basics
6. energy-storage-basics

Следующая часть волны проходит отдельным safety/conformance пакетом. Архитектура остаётся закрытой на 19 Record types.


## 2026-10-02 — Practical resilience and continuity expansion — complete working wave

Десять новых отсутствовавших доменов:
1. forestry-basics
2. fisheries-basics
3. livestock-systems-basics
4. food-safety-basics
5. wastewater-basics
6. disaster-risk-reduction-basics
7. emergency-management-basics
8. energy-storage-basics
9. electrical-safety-basics
10. public-risk-communication-basics

Каждый срез использует существующий профиль Source → 3 Claims → 3 Evidence Use → Context → Scope и dedicated regression. Safety-срезы содержат явную границу компетентности и не превращаются в инструкции по опасным действиям.


## 2026-10-02 — Gap Map R1 adopted

The current 248-slice corpus is now governed for expansion by:
- RELEASE/CONTENT-GAP-MAP-2026-10-02-R1.md
- RELEASE/CONTENT-GAP-MAP-2026-10-02-R1.json

The gap map supersedes stale historical “next ten” lists for prioritization. It distinguishes missing subject domains, content-depth gaps, cross-domain linkage gaps, Record-type depth, evidence/source diversity, Human View/safety depth, and geographic/jurisdictional/temporal context.

No content is added merely because an old roadmap item is still named. The actual CONTENT/vertical-slices registry is the presence authority.

Accelerated expansion policy: identify 20–40 high-value non-duplicate candidates, deliver them as controlled 10-slice CI units, accumulate clean units, then perform deep cross-domain/content-depth/adversarial review and the full release gates before a new CLEAN checkpoint.


## 2026-10-02 — Gap Map R1 accelerated wave 1

The first accelerated wave closes ten high-value non-duplicate gaps:
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

Wave result: **258 vertical slices / 2277 Records / 19 Record types** before corpus-wide closure checks. The wave does not introduce a new Record type. Cross-domain linkage, content-depth and adversarial review remain release-level checks rather than being declared closed by content creation alone.
