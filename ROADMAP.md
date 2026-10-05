# ROADMAP — Энциклопедия цивилизации

## Назначение

Этот документ описывает последовательность развития проекта после закрытия нормативного implementation-контура 000–021.

Он является **планом работ, а не новым нормативным слоем**.

Нормативными источниками остаются FOUNDATION, STANDARD, IMPLEMENTATION/000–021 и принятые ADR.

## Текущий архитектурный статус

По состоянию на 30 сентября 2026 года:

- FOUNDATION определяет базовую философию и архитектуру;
- STANDARD 001–019 определяют предметные и эпистемические семантики;
- IMPLEMENTATION 000–021 определяет техническую реализацию и conformance/release process;
- Reference Implementation имеет исполняемый Release Conformance Gate;
- текущий Reference Implementation applicability contour имеет состояние **CONFORMING**;
- Количество тестов меняется вместе с corpus regression suite; актуальное состояние определяется CI.
- Release Gate G01–G25 расширяется вместе с корпусом; G25 автоматически обнаруживает и проверяет регистрацию каждого вертикального среза;
- это не является утверждением истинности содержащихся или будущих знаний.

# Фаза 1 — Содержательное наполнение

## Цель

Перейти от проверки самой системы к созданию реальных, проверяемых и воспроизводимых знаний.

Основной принцип: сначала создаётся корректный вертикальный срез знания, затем он проходит весь существующий pipeline от Record до публикации и recovery.

Фаза 1 не должна создавать новые фундаментальные типы только ради нового предметного домена.

## 1.1. Authoring Contract

Зафиксировать практический процесс создания записи:

    предмет / вопрос
        ↓
    источник
        ↓
    утверждение или другой тип Record
        ↓
    Evidence Use / Assessment / Inference при необходимости
        ↓
    Scope + Context + Provenance
        ↓
    проверка
        ↓
    версионирование
        ↓
    публикация

Нужно отдельно определить:

- минимальный пакет данных для новой записи;
- требования к источникам;
- правила неизвестности;
- правила фиксации ограничений;
- критерии готовности записи;
- требования к опасным практическим знаниям.

## 1.2. Первый предметный вертикальный срез

Первый срез должен:

- использовать существующие 19 типов;
- содержать реальные Record;
- иметь источники и Evidence Use;
- демонстрировать Scope и Context;
- сохранять Provenance;
- проходить Validator;
- проходить Semantic Conformance;
- проходить Publication;
- проходить Recovery;
- сохранять историю версий.

Для первого среза предпочтителен базовый жизненно важный домен, позволяющий проверить большое количество архитектурных границ на небольшом объёме содержания.

## 1.2.1. Зафиксированные вертикальные срезы

- `vertical-slices/water` — 7 Record: Source + Claim + Evidence Use;
- `vertical-slices/power-outage-food` — 13 Record: Source + Claim + Evidence Use + Context + Scope;
- `vertical-slices/emergency-hand-hygiene` — 9 Record: Source + Claim + Evidence Use + Context + Scope + Process + Action + Result;
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

Третий срез проверяет Process → Action → Result; четвёртый — Claim → Assessment → Inference; пятый — Event → Decision → Action → Result; шестой — State → Relation → Identity с явным subject; седьмой — Source → Provenance / Authorship Contribution / Trust boundary; восьмой — отдельный практический аварийный домен с явными Context/Scope; девятый — холодовая безопасность и гипотермия с двумя независимыми Claim→Evidence Use; десятый — безопасность переносного генератора и предотвращение воздействия CO. Все связки используют существующие Record types.

## 1.3. Content Package

После первого вертикального среза создать воспроизводимый пакет содержания:

- canonical Records;
- manifest;
- integrity metadata;
- source references;
- conformance evidence;
- publication output;
- recovery test result.

Пакет не должен становиться новым нормативным источником.

## 1.4. Offline Sufficiency

Отдельно проверить, что опубликованный срез может быть использован без исходного сервиса:

- идентичность записей сохраняется;
- ссылки разрешаются или явно маркируются как недоступные;
- история не теряется;
- источники и ограничения не скрываются;
- неизвестность не превращается в заполненное значение;
- публикация не меняет семантику Record.

## 1.5. Human Usability

Проверить не только machine conformance, но и практическую пригодность:

- человек может понять содержание без чтения архитектурных документов;
- важные ограничения видимы;
- источник и его роль различимы;
- неизвестное отличается от отрицательного;
- версия и дата понятны;
- опасные действия имеют необходимые предупреждения;
- публикационное представление не создаёт ложного впечатления большей достоверности.

# Фаза 2 — Расширение корпуса

После успешного первого вертикального среза добавлять новые предметные области, переиспользуя существующие типы и проверяя реальные пробелы модели.

Новые типы не добавляются без доказанной семантической необходимости.

# Фаза 3 — Offline / Physical Editions

После накопления достаточного корпуса:

- печатное издание;
- статический offline-сайт;
- архивные пакеты;
- локальное хранилище;
- экспорт в долговечные форматы;
- проверка восстановления на независимой среде.

# Правило перехода между фазами

Переход выполняется только после evidence. Нельзя считать фазу завершённой только потому, что соответствующий документ написан.

Для каждого этапа должны существовать:

- конкретный artifact;
- проверяемый результат;
- regression evidence;
- audit trail.

# Архитектурное ограничение

Новый предметный домен **не является автоматически основанием для нового Record type**.

Перед добавлением нового типа необходимо пройти Entity Discipline из IMPLEMENTATION/003-TYPE-REGISTRY.md и оформить отдельное архитектурное решение, если существующих типов недостаточно.

# Ближайшая работа

1. Согласовать практический Authoring Contract с существующими Standards.
2. Выбрать и построить первый предметный вертикальный срез.
3. Прогнать его через полный Reference pipeline.
4. Проверить offline sufficiency.
5. Выпустить первый содержательный content package.
6. Масштабировать корпус вертикальными срезами с отдельным regression evidence.
7. После накопления корпуса перейти к Offline / Physical Editions с отдельным evidence.

Фаза 2 уже начата: десять вертикальных срезов покрывают основные проверенные связки текущей модели и расширяют предметный охват; окончательное закрытие каждого среза требует успешного CI.

## Новые срезы
- carbon-monoxide-heating-safety — 7 Record.
- flood-cleanup-safety — 7 Record.
- burn-first-aid — 7 Record.

## Новый срез
- chemical-water-advisory — 7 Record: химическое загрязнение воды и режим питьевого запрета.

## Контрольная точка 23 среза
- seed-storage-basics — 8 Record.
- hand-tool-safety — 8 Record.
- Корпус: 27 вертикальных срезов / 202 Record.


## Phase 2 subject-matter expansion — 30 сентября 2026

Добавлены два нейтральных предметных среза без новых Record types: `si-units-basics` и `time-standard-basics`. Оба используют существующую цепочку Source → Claim → Evidence Use → Context → Scope и отдельные официальные источники NIST.

Корпус: **27 вертикальных срезов / 202 Record / 19 Record types**.

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

- `vertical-slices/emergency-alert-warning` — 7 Record.


## Authoring Contract — executable closure — 30 сентября 2026

Практический Authoring Contract теперь имеет отдельный executable regression suite: structural, semantic, provenance/evidence, immutability, publication/package/recovery и cross-slice/history boundary checks. Новые Record types не требуются. Этот слой закрывается только после зелёного Reference CI и Release Conformance Gate.


## Phase 3 — Offline / Physical Editions — closure — 30 сентября 2026

Фундамент Фазы 3 закрыт: полный корпус имеет воспроизводимое offline-представление, durable local storage, статическую публикацию и print-ready surface. Canonical Records не изменяются производными представлениями; package integrity, audit trail и recovery сохраняются. Evidence: RELEASE/OFFLINE-PHYSICAL-EDITION-CONFORMANCE.json и RELEASE/OFFLINE-PHYSICAL-EDITION-2026-09-30.md. Reference run 36701858077 PASS; Release Conformance Gate 36701858052 PASS.


## Content Domain Roadmap — 30 сентября 2026

Создан `CONTENT/DOMAIN-ROADMAP.md`: системная очередь расширения корпуса от фундаментальных знаний к человеку, обществу, технологиям, истории и практической безопасности. Следующая рабочая десятка определена без искусственного quota по Records и без новых типов.

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


## Full-project audit checkpoint — 30 сентября 2026

Первая десятка Content Domain Roadmap закрыта. После неё выполнен полный project/corpus regression: **37 slices / 378 Records / 19 types; 441 Reference tests PASS; Release Gate PASS**. Следующая десятка выбирается только после анализа этого checkpoint; закрытые архитектурные контуры не переоткрываются без новой причины.


## Phase 2 — second domain roadmap ten-slice checkpoint

Новые срезы текущего цикла:
- `vertical-slices/temperature-basics`
- `vertical-slices/mixtures-and-solutions`
- `vertical-slices/acid-base-basics`
- `vertical-slices/genetics-basics`
- `vertical-slices/ecosystems-basics`
- `vertical-slices/solar-system-basics`
- `vertical-slices/seasons-and-orbits`
- `vertical-slices/physiology-basics`
- `vertical-slices/nutrition-basics`
- `vertical-slices/sleep-basics`

Definition of Done: Source → Claim → Evidence Use → Context/Scope + dedicated regression test + full Reference CI + Release Gate. После закрытия десятки выполняется полный cross-domain audit и новый release baseline.


## Phase 3 — third domain-roadmap ten-slice checkpoint

Новые срезы: learning-basics, mental-health-information-boundaries, law-basics, demography-basics, governance-basics, education-systems, culture-and-language, networks-basics, materials-basics, manufacturing-basics.

Для law/governance/education фиксируются юрисдикция, дата и контекст; для human topics сохраняются границы между общей информацией и индивидуальной рекомендацией.


### Phase 3 slice registry

- `vertical-slices/learning-basics`
- `vertical-slices/mental-health-information-boundaries`
- `vertical-slices/law-basics`
- `vertical-slices/demography-basics`
- `vertical-slices/governance-basics`
- `vertical-slices/education-systems`
- `vertical-slices/culture-and-language`
- `vertical-slices/networks-basics`
- `vertical-slices/materials-basics`
- `vertical-slices/manufacturing-basics`


## Phase 4 — fourth domain-roadmap ten-slice checkpoint

Новые срезы: infrastructure-basics, chronology-methods, archaeology-basics, early-agriculture, urbanization, writing-systems, trade-networks, state-formation, fire, flood.

### Phase 4 slice registry

- `vertical-slices/infrastructure-basics`
- `vertical-slices/chronology-methods`
- `vertical-slices/archaeology-basics`
- `vertical-slices/early-agriculture`
- `vertical-slices/urbanization`
- `vertical-slices/writing-systems`
- `vertical-slices/trade-networks`
- `vertical-slices/state-formation`
- `vertical-slices/fire`
- `vertical-slices/flood`

Критерий закрытия: dedicated regression для каждого среза + полный Reference CI + Release Conformance Gate + release baseline. Исторические срезы явно разделяют chronology и causality; safety-срезы фиксируют зависимость от местных предупреждений и экстренных служб.


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


## Fifth ten-slice semantic expansion — 30 September 2026

The first ten-slice semantic expansion is represented by complete canonical content and dedicated regression coverage:
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

Closure requires Source → 3 Claims → 3 Evidence Use → Context → Scope, dedicated regression, corpus-wide semantic validation, Human View, package/recovery evidence, and a passing Reference/Release Gate. The release baseline is promoted only after the Gate is green.\n\n### Fifth ten-slice machine-checked slice registry

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


## Fifth ten-slice expansion — 30 September 2026

The next ten content slices after the 67-slice v1.4 corpus are:
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

Definition of Done: Source → 3 Claims → 3 Evidence Use → Context → Scope, dedicated regression, corpus-wide semantic/Human View/package audit, full Reference/Release Gate, then baseline promotion. No new Record type is introduced.


## Sixth ten-slice expansion — 30 сентября 2026

После v1.5 добавлены следующие десять новых предметных срезов без изменения набора Record types:
- vertical-slices/astronomy-observation-basics
- vertical-slices/electricity-basics
- vertical-slices/statistics-basics
- vertical-slices/maps-and-navigation-basics
- vertical-slices/telecommunications-basics
- vertical-slices/money-and-banking-basics
- vertical-slices/public-health-basics
- vertical-slices/waste-management-basics
- vertical-slices/transportation-basics
- vertical-slices/information-literacy-basics

Контрольная точка расширения: **87 vertical slices / 738 Records / 19 Record types**. Definition of Done: dedicated regression → corpus-wide semantic/Human View/package audit → full Reference/Release Gate → baseline promotion.


## Seventh ten-slice expansion — 30 September 2026

После v1.6 добавлены следующие десять предметных срезов без изменения набора Record types:
- vertical-slices/chemical-reactions-basics
- vertical-slices/thermodynamics-basics
- vertical-slices/waves-and-sound-basics
- vertical-slices/optics-basics
- vertical-slices/magnetism-basics
- vertical-slices/evolution-basics
- vertical-slices/microbiology-basics
- vertical-slices/plant-biology-basics
- vertical-slices/geographic-coordinates-basics
- vertical-slices/ancient-civilizations-basics

Контрольная точка расширения: **97 vertical slices / 828 Records / 19 Record types**. Definition of Done: dedicated regression → corpus-wide semantic/Human View/package audit → full Reference/Release Gate → v1.7 baseline.


## Eighth ten-slice expansion — 30 сентября 2026

После v1.7 добавлены следующие десять предметных срезов без изменения набора Record types:
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

Контрольная точка расширения: **107 vertical slices / 918 Records / 19 Record types**. Definition of Done: dedicated regression → corpus-wide semantic/Human View/package audit → full Reference/Release Gate → v1.8 baseline.


## Ninth ten-slice expansion — 30 сентября 2026

После v1.8 добавлены следующие десять предметных срезов без изменения набора Record types:
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

Контрольная точка расширения: **117 vertical slices / 1008 Records / 19 Record types**. Definition of Done: dedicated regression → corpus-wide semantic/Human View/package audit → full Reference/Release Gate → v1.9 baseline.


## Tenth ten-slice expansion — 30 сентября 2026

После v1.9 добавлены десять предметных срезов без изменения набора Record types:
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

Контрольная точка расширения: **127 vertical slices / 1098 Records / 19 Record types**. Definition of Done: dedicated regression → corpus-wide semantic/Human View/package audit → full Reference/Release Gate → v2.0 baseline.


Tenth expansion completion note: the tenth wave is now complete with two previously unregistered slices added: vertical-slices/logic-basics and vertical-slices/anthropology-basics. Final target: 127 vertical slices / 1098 Records.


## v2.1 — 50-domain expansion wave — 30 September 2026

Крупная содержательная волна выполнена пятью контролируемыми десятками. Все новые срезы используют существующие 19 Record types; каждый содержит Source → 3 Claims → 3 Evidence Use → Context → Scope и dedicated regression.

### Десятка 1 — математика и методология
- `vertical-slices/algebra-basics`
- `vertical-slices/geometry-basics`
- `vertical-slices/trigonometry-basics`
- `vertical-slices/calculus-basics`
- `vertical-slices/linear-algebra-basics`
- `vertical-slices/number-theory-basics`
- `vertical-slices/combinatorics-basics`
- `vertical-slices/numerical-methods-basics`
- `vertical-slices/measurement-uncertainty-basics`
- `vertical-slices/scientific-method-basics`

### Десятка 2 — науки о Земле
- `vertical-slices/hydrology-basics`
- `vertical-slices/meteorology-basics`
- `vertical-slices/volcanology-basics`
- `vertical-slices/seismology-basics`
- `vertical-slices/paleontology-basics`
- `vertical-slices/geomorphology-basics`
- `vertical-slices/mineralogy-basics`
- `vertical-slices/petrology-basics`
- `vertical-slices/atmospheric-science-basics`
- `vertical-slices/remote-sensing-basics`

### Десятка 3 — биология
- `vertical-slices/zoology-basics`
- `vertical-slices/conservation-biology-basics`
- `vertical-slices/developmental-biology-basics`
- `vertical-slices/virology-basics`
- `vertical-slices/parasitology-basics`
- `vertical-slices/microbiome-basics`
- `vertical-slices/behavioral-biology-basics`
- `vertical-slices/plant-physiology-basics`
- `vertical-slices/biodiversity-basics`
- `vertical-slices/ecophysiology-basics`

### Десятка 4 — вычисления и технологии
- `vertical-slices/databases-basics`
- `vertical-slices/programming-languages-basics`
- `vertical-slices/software-engineering-basics`
- `vertical-slices/cybersecurity-basics`
- `vertical-slices/cryptography-basics`
- `vertical-slices/human-computer-interaction-basics`
- `vertical-slices/distributed-systems-basics`
- `vertical-slices/cloud-computing-basics`
- `vertical-slices/computer-architecture-basics`
- `vertical-slices/artificial-intelligence-basics`

### Десятка 5 — экономика, общество и институты
- `vertical-slices/accounting-basics`
- `vertical-slices/macroeconomics-basics`
- `vertical-slices/microeconomics-basics`
- `vertical-slices/finance-basics`
- `vertical-slices/organizational-behavior-basics`
- `vertical-slices/education-science-basics`
- `vertical-slices/public-administration-basics`
- `vertical-slices/demographic-methods-basics`
- `vertical-slices/urban-planning-basics`
- `vertical-slices/history-methods-basics`

Контрольная точка волны: **177 vertical slices / 1548 Records / 19 Record types**. После расширения выполняются полный corpus audit, Reference Tests, Release Conformance Gate и v2.1 baseline.## v2.1 — fifty-domain expansion wave — 30 September 2026

Вместо искусственного ограничения десятью срезами выполнена крупная содержательная волна из пяти контролируемых десяток. Новые домены проверены на отсутствие дублей в текущем корпусе и используют существующие 19 Record types.

### Десятка 1 — математика и методология
- vertical-slices/algebra-basics
- vertical-slices/geometry-basics
- vertical-slices/trigonometry-basics
- vertical-slices/calculus-basics
- vertical-slices/linear-algebra-basics
- vertical-slices/number-theory-basics
- vertical-slices/combinatorics-basics
- vertical-slices/numerical-methods-basics
- vertical-slices/measurement-uncertainty-basics
- vertical-slices/scientific-method-basics

### Десятка 2 — науки о Земле
- vertical-slices/hydrology-basics
- vertical-slices/meteorology-basics
- vertical-slices/volcanology-basics
- vertical-slices/seismology-basics
- vertical-slices/paleontology-basics
- vertical-slices/geomorphology-basics
- vertical-slices/mineralogy-basics
- vertical-slices/petrology-basics
- vertical-slices/atmospheric-science-basics
- vertical-slices/remote-sensing-basics

### Десятка 3 — биология
- vertical-slices/zoology-basics
- vertical-slices/conservation-biology-basics
- vertical-slices/developmental-biology-basics
- vertical-slices/virology-basics
- vertical-slices/parasitology-basics
- vertical-slices/microbiome-basics
- vertical-slices/behavioral-biology-basics
- vertical-slices/plant-physiology-basics
- vertical-slices/biodiversity-basics
- vertical-slices/ecophysiology-basics

### Десятка 4 — вычисления и технологии
- vertical-slices/databases-basics
- vertical-slices/programming-languages-basics
- vertical-slices/software-engineering-basics
- vertical-slices/cybersecurity-basics
- vertical-slices/cryptography-basics
- vertical-slices/human-computer-interaction-basics
- vertical-slices/distributed-systems-basics
- vertical-slices/cloud-computing-basics
- vertical-slices/computer-architecture-basics
- vertical-slices/artificial-intelligence-basics

### Десятка 5 — экономика, общество и институты
- vertical-slices/accounting-basics
- vertical-slices/macroeconomics-basics
- vertical-slices/microeconomics-basics
- vertical-slices/finance-basics
- vertical-slices/organizational-behavior-basics
- vertical-slices/education-science-basics
- vertical-slices/public-administration-basics
- vertical-slices/demographic-methods-basics
- vertical-slices/urban-planning-basics
- vertical-slices/history-methods-basics

Каждый срез: Source → 3 Claims → 3 Evidence Use → Context → Scope + dedicated regression. Контрольная точка: **177 вертикальных срезов / 1548 Records / 19 Record types**; следующий этап — полный corpus audit → Reference Tests → Release Gate → v2.1 baseline.


## v2.2 — first Content Domain Roadmap ten-slice checkpoint — 30 September 2026

Следующая десятка из Content Domain Roadmap закрыта как содержательный контрольный блок:
- ratios-and-percentages
- probability-basics
- motion-basics
- energy-basics
- matter-basics
- cell-basics
- earth-system-basics
- anatomy-basics
- economics-basics
- computing-basics

В блоке добавлено **86 Records** без новых Record types. Профили: первые два среза — Source + 2 Claim + 2 Evidence Use + Context + Scope; остальные восемь — Source + 3 Claim + 3 Evidence Use + Context + Scope.

Проверка показала, что эти десять срезов уже присутствовали в корпусе v2.1. Поэтому добавление 86 Records не является новым расширением; контрольная точка 187 / 1638 / 19 восстановлена. Временный v2.2 не продвигается. Итог сверки зафиксирован отдельным audit trail.

No new Record type is introduced by this expansion.


## Next working ten — methods and reasoning

Новый рабочий блок после подтверждённого v2.1 control point:
- vertical-slices/critical-thinking-basics
- vertical-slices/causal-inference-basics
- vertical-slices/research-design-basics
- vertical-slices/decision-theory-basics
- vertical-slices/risk-analysis-basics
- vertical-slices/information-theory-basics
- vertical-slices/data-visualization-basics
- vertical-slices/scientific-communication-basics
- vertical-slices/modeling-basics
- vertical-slices/systems-thinking-basics.

Каждый срез: Source → 3 Claims → 3 Evidence Use → Context → Scope + dedicated regression. Цель блока — расширить методологическую и reasoning-coverage без введения новых Record types. После содержательной проверки выполняются corpus-wide semantic/content audit → Reference Tests → Release Gate → baseline promotion.


## BLOCK 1 — содержательное масштабирование корпуса — 1 октября 2026

Цель блока: превратить текущую conformance-ready инфраструктуру в существенно более широкое и связанное содержательное ядро без переоткрытия FOUNDATION, STANDARD или IMPLEMENTATION.

### Definition of Done блока

1. Выполнить серию из 10–15 контролируемых содержательных циклов.
2. Каждый цикл: новые неповторяющиеся доменные срезы, реальные источники, предметные Claims, Evidence Use, Context/Scope и dedicated regression.
3. После каждой волны проверять отсутствие дублей и семантическую совместимость с 19 существующими Record types.
4. После накопления широты провести отдельный cross-domain linkage pass: связи добавляются только там, где их семантика доказана.
5. Провести content-depth pass для новых Claims: определения, механизмы, ограничения, условия применимости и границы переноса.
6. Провести adversarial semantic/content review по опасным, историческим, причинным, медицинским и юрисдикционно-зависимым темам.
7. Выполнить полный corpus regression: schema, semantic conformance, provenance/evidence, Human View, offline/package/recovery.
8. Выполнить полный Reference Tests и Release Conformance Gate.
9. Сформировать отдельный audit trail и evidence package.
10. Только после зелёного полного Gate принять решение о следующем release baseline.

### Архитектурная граница

BLOCK 1 не расширяет набор Record types и не переоткрывает уже закрытые архитектурные решения. Если реальный контент обнаружит недостаточность модели, сначала применяется Entity Discipline + ADR; изменение архитектуры не смешивается с содержательным масштабированием.

### Контрольная точка

Исходное состояние блока: **187 vertical slices / 1638 Records / 19 Record types**.

Текущее состояние после полного corpus audit: **PASS / NO BLOCKING FINDINGS**.

Следующий результат должен фиксироваться как отдельная контрольная точка блока, а не как изменение стабильного v2.1 baseline до завершения всего Definition of Done.


### BLOCK 1 — Wave 1
- `vertical-slices/epistemology-basics`
- `vertical-slices/philosophy-of-science-basics`
- `vertical-slices/philosophy-of-mind-basics`
- `vertical-slices/philosophy-of-language-basics`
- `vertical-slices/metaphysics-basics`
- `vertical-slices/philosophy-of-mathematics-basics`

Шесть новых философских срезов; новые Record types не вводятся. Контрольная точка: **203 / 1782 / 19**. v2.1 не изменяется до полного Definition of Done блока.

## BLOCK 1 — Wave 2 — operational and organizational foundations

New non-duplicate slices after the saved philosophy checkpoint:
- communication-basics
- logistics-basics
- supply-chain-basics
- project-management-basics
- quality-control-basics
- labor-markets-basics
- negotiation-basics
- conflict-resolution-basics
- reliability-basics
- requirements-engineering-basics

Each slice uses Source → 3 Claims → 3 Evidence Use → Context → Scope and a dedicated regression test. No new Record types are introduced. Working corpus: **203 vertical slices / 1782 Records / 19 Record types**. Block 1 DoD remains open until content-depth review, cross-domain linkage audit, adversarial review, full regression, Human View, offline/package recovery, Reference Tests and Release Gate are green.


## BLOCK 1 — Wave 2 registry

- `vertical-slices/communication-basics`
- `vertical-slices/logistics-basics`
- `vertical-slices/supply-chain-basics`
- `vertical-slices/project-management-basics`
- `vertical-slices/quality-control-basics`
- `vertical-slices/labor-markets-basics`
- `vertical-slices/negotiation-basics`
- `vertical-slices/conflict-resolution-basics`
- `vertical-slices/reliability-basics`
- `vertical-slices/requirements-engineering-basics`

## BLOCK 1 — clean checkpoint closed — 1 October 2026

BLOCK 1 Definition of Done is closed. The corpus checkpoint is **203 vertical slices / 1782 Records / 19 Record types**. Content-depth, cross-domain linkage, adversarial semantic/content review, Human View, provenance/evidence, offline/package/recovery, Reference Tests, and Release Gate are all closed on the common final commit `3c0a25e7d8efd5981bd0fde3eb2c915e770d881f`.

Evidence:
- `RELEASE/BLOCK-1-CLEAN-CHECKPOINT-2026-10-01.json`
- `RELEASE/BLOCK-1-CLEAN-CHECKPOINT-2026-10-01.md`

The checkpoint does not reopen FOUNDATION, STANDARD, or IMPLEMENTATION and introduces no new Record types. It is the clean evidence baseline from which the next content-expansion block proceeds.



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


## Next content expansion — engineering, operations and human factors — 1 October 2026

- `vertical-slices/modeling-and-simulation-basics`
- `vertical-slices/operations-research-basics`
- `vertical-slices/systems-engineering-basics`
- `vertical-slices/safety-engineering-basics`
- `vertical-slices/reliability-engineering-basics`
- `vertical-slices/maintenance-engineering-basics`
- `vertical-slices/structural-engineering-basics`
- `vertical-slices/heat-transfer-basics`
- `vertical-slices/agrifood-systems-basics`
- `vertical-slices/ergonomics-basics`

Each slice uses Source → 3 Claims → 3 Evidence Use → Context → Scope and a dedicated regression. No new Record types. Closure requires corpus-wide semantic/content audit, Human View, offline/package/recovery, Reference Tests and Release Gate evidence.


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

Next controlled ten-slice wave after the 238-slice clean checkpoint:
- political-science-basics
- international-relations-basics
- diplomacy-basics
- human-rights-basics
- constitutional-systems-basics
- public-policy-basics
- labor-relations-basics
- public-finance-basics
- development-economics-basics
- behavioral-economics-basics

Each slice uses Source → 3 Claims → 3 Evidence Use → Context → Scope and a dedicated regression. Political and institutional content is descriptive and jurisdiction/context bounded; no electoral recommendation or evaluative ranking is encoded.

Target after closure: 248 vertical slices / 2187 records / 19 Record types.


## 2026-10-02 — Machine-checked 248-slice registry

The 248-slice corpus registry is synchronized with `CONTENT/vertical-slices` at the 2187-record checkpoint:

- `vertical-slices/accounting-basics`
- `vertical-slices/acid-base-basics`
- `vertical-slices/agriculture-basics`
- `vertical-slices/agrifood-systems-basics`
- `vertical-slices/algebra-basics`
- `vertical-slices/anatomy-basics`
- `vertical-slices/ancient-civilizations-basics`
- `vertical-slices/anthropology-basics`
- `vertical-slices/archaeology-basics`
- `vertical-slices/architecture-basics`
- `vertical-slices/art-history-basics`
- `vertical-slices/artificial-intelligence-basics`
- `vertical-slices/astronomy-basics`
- `vertical-slices/astronomy-observation-basics`
- `vertical-slices/atmospheric-science-basics`
- `vertical-slices/behavioral-biology-basics`
- `vertical-slices/behavioral-economics-basics`
- `vertical-slices/biochemistry-basics`
- `vertical-slices/biodiversity-basics`
- `vertical-slices/burn-first-aid`
- `vertical-slices/calculus-basics`
- `vertical-slices/carbon-monoxide-heating-safety`
- `vertical-slices/causal-inference-basics`
- `vertical-slices/cell-basics`
- `vertical-slices/cell-biology-basics`
- `vertical-slices/chemical-reactions-basics`
- `vertical-slices/chemical-water-advisory`
- `vertical-slices/chronology-methods`
- `vertical-slices/civil-engineering-basics`
- `vertical-slices/climate-basics`
- `vertical-slices/climate-science-basics`
- `vertical-slices/cloud-computing-basics`
- `vertical-slices/cold-weather-hypothermia`
- `vertical-slices/combinatorics-basics`
- `vertical-slices/communication-basics`
- `vertical-slices/compiler-basics`
- `vertical-slices/computer-architecture-basics`
- `vertical-slices/computer-networks-basics`
- `vertical-slices/computer-science-algorithms-basics`
- `vertical-slices/computing-basics`
- `vertical-slices/conflict-resolution-basics`
- `vertical-slices/conservation-biology-basics`
- `vertical-slices/constitutional-systems-basics`
- `vertical-slices/construction-basics`
- `vertical-slices/control-systems-basics`
- `vertical-slices/critical-thinking-basics`
- `vertical-slices/cross-slice-linkage`
- `vertical-slices/cryptography-basics`
- `vertical-slices/culture-and-language`
- `vertical-slices/cybersecurity-basics`
- `vertical-slices/data-science-basics`
- `vertical-slices/data-visualization-basics`
- `vertical-slices/databases-basics`
- `vertical-slices/decision-theory-basics`
- `vertical-slices/demographic-methods-basics`
- `vertical-slices/demography-basics`
- `vertical-slices/development-economics-basics`
- `vertical-slices/developmental-biology-basics`
- `vertical-slices/diplomacy-basics`
- `vertical-slices/disaster-risk-reduction-basics`
- `vertical-slices/distributed-systems-basics`
- `vertical-slices/early-agriculture`
- `vertical-slices/earth-system-basics`
- `vertical-slices/earthquake-aftershock-safety`
- `vertical-slices/earthquake-protective-action`
- `vertical-slices/ecology-basics`
- `vertical-slices/economics-basics`
- `vertical-slices/ecophysiology-basics`
- `vertical-slices/ecosystems-basics`
- `vertical-slices/education-science-basics`
- `vertical-slices/education-systems`
- `vertical-slices/electrical-safety-basics`
- `vertical-slices/electricity-basics`
- `vertical-slices/electromagnetism-basics`
- `vertical-slices/emergency-alert-warning`
- `vertical-slices/emergency-hand-hygiene`
- `vertical-slices/emergency-lighting-safety`
- `vertical-slices/emergency-management-basics`
- `vertical-slices/emergency-waste-sanitation`
- `vertical-slices/emergency-water-storage-state`
- `vertical-slices/energy-basics`
- `vertical-slices/energy-storage-basics`
- `vertical-slices/epidemiology-basics`
- `vertical-slices/epistemology-basics`
- `vertical-slices/ergonomics-basics`
- `vertical-slices/ethics-basics`
- `vertical-slices/evolution-basics`
- `vertical-slices/extreme-heat-safety`
- `vertical-slices/finance-basics`
- `vertical-slices/fire`
- `vertical-slices/fisheries-basics`
- `vertical-slices/flood`
- `vertical-slices/flood-cleanup-safety`
- `vertical-slices/flood-food-safety`
- `vertical-slices/fluid-mechanics-basics`
- `vertical-slices/food-preservation-basics`
- `vertical-slices/food-safety-basics`
- `vertical-slices/food-science-basics`
- `vertical-slices/forestry-basics`
- `vertical-slices/formal-methods-basics`
- `vertical-slices/game-theory-basics`
- `vertical-slices/generator-carbon-monoxide-safety`
- `vertical-slices/genetics-basics`
- `vertical-slices/genomics-basics`
- `vertical-slices/geographic-coordinates-basics`
- `vertical-slices/geology-basics`
- `vertical-slices/geometry-basics`
- `vertical-slices/geomorphology-basics`
- `vertical-slices/geophysics-basics`
- `vertical-slices/governance-basics`
- `vertical-slices/graph-theory-basics`
- `vertical-slices/hand-tool-safety`
- `vertical-slices/heat-transfer-basics`
- `vertical-slices/history-methods-basics`
- `vertical-slices/home-fire-smoke-safety`
- `vertical-slices/human-computer-interaction-basics`
- `vertical-slices/human-rights-basics`
- `vertical-slices/hydrology-basics`
- `vertical-slices/immunology-basics`
- `vertical-slices/information-literacy-basics`
- `vertical-slices/information-theory-basics`
- `vertical-slices/infrastructure-basics`
- `vertical-slices/international-relations-basics`
- `vertical-slices/labor-markets-basics`
- `vertical-slices/labor-relations-basics`
- `vertical-slices/law-basics`
- `vertical-slices/learning-basics`
- `vertical-slices/linear-algebra-basics`
- `vertical-slices/linguistics-basics`
- `vertical-slices/livestock-systems-basics`
- `vertical-slices/logic-basics`
- `vertical-slices/logistics-basics`
- `vertical-slices/macroeconomics-basics`
- `vertical-slices/magnetism-basics`
- `vertical-slices/maintenance-engineering-basics`
- `vertical-slices/manufacturing-basics`
- `vertical-slices/maps-and-navigation-basics`
- `vertical-slices/materials-basics`
- `vertical-slices/materials-science-basics`
- `vertical-slices/matter-basics`
- `vertical-slices/measurement-uncertainty-basics`
- `vertical-slices/mechanics-basics`
- `vertical-slices/mental-health-information-boundaries`
- `vertical-slices/metaphysics-basics`
- `vertical-slices/meteorology-basics`
- `vertical-slices/metrology-basics`
- `vertical-slices/microbiology-basics`
- `vertical-slices/microbiome-basics`
- `vertical-slices/microeconomics-basics`
- `vertical-slices/mineralogy-basics`
- `vertical-slices/mixtures-and-solutions`
- `vertical-slices/modeling-and-simulation-basics`
- `vertical-slices/modeling-basics`
- `vertical-slices/money-and-banking-basics`
- `vertical-slices/motion-basics`
- `vertical-slices/music-theory-basics`
- `vertical-slices/negotiation-basics`
- `vertical-slices/networks-basics`
- `vertical-slices/neuroscience-basics`
- `vertical-slices/number-theory-basics`
- `vertical-slices/numerical-methods-basics`
- `vertical-slices/nutrition-basics`
- `vertical-slices/ocean-basics`
- `vertical-slices/oceanography-basics`
- `vertical-slices/operating-systems-basics`
- `vertical-slices/operations-research-basics`
- `vertical-slices/optics-basics`
- `vertical-slices/optimization-basics`
- `vertical-slices/organic-chemistry-basics`
- `vertical-slices/organizational-behavior-basics`
- `vertical-slices/paleontology-basics`
- `vertical-slices/parasitology-basics`
- `vertical-slices/petrology-basics`
- `vertical-slices/philosophy-basics`
- `vertical-slices/philosophy-of-language-basics`
- `vertical-slices/philosophy-of-mathematics-basics`
- `vertical-slices/philosophy-of-mind-basics`
- `vertical-slices/philosophy-of-science-basics`
- `vertical-slices/physiology-basics`
- `vertical-slices/plant-biology-basics`
- `vertical-slices/plant-physiology-basics`
- `vertical-slices/political-science-basics`
- `vertical-slices/power-outage-food`
- `vertical-slices/probability-basics`
- `vertical-slices/programming-languages-basics`
- `vertical-slices/project-management-basics`
- `vertical-slices/psychology-basics`
- `vertical-slices/public-administration-basics`
- `vertical-slices/public-finance-basics`
- `vertical-slices/public-health-basics`
- `vertical-slices/public-policy-basics`
- `vertical-slices/public-risk-communication-basics`
- `vertical-slices/quality-control-basics`
- `vertical-slices/quantum-physics-basics`
- `vertical-slices/queueing-theory-basics`
- `vertical-slices/ratios-and-percentages`
- `vertical-slices/reliability-basics`
- `vertical-slices/reliability-engineering-basics`
- `vertical-slices/remote-sensing-basics`
- `vertical-slices/renewable-energy-basics`
- `vertical-slices/requirements-engineering-basics`
- `vertical-slices/research-design-basics`
- `vertical-slices/risk-analysis-basics`
- `vertical-slices/robotics-basics`
- `vertical-slices/safety-engineering-basics`
- `vertical-slices/scientific-communication-basics`
- `vertical-slices/scientific-method-basics`
- `vertical-slices/seasons-and-orbits`
- `vertical-slices/seed-storage-basics`
- `vertical-slices/seismology-basics`
- `vertical-slices/septic-system-emergency`
- `vertical-slices/shelter-basics`
- `vertical-slices/si-units-basics`
- `vertical-slices/signal-processing-basics`
- `vertical-slices/sleep-basics`
- `vertical-slices/sociology-basics`
- `vertical-slices/software-engineering-basics`
- `vertical-slices/software-testing-basics`
- `vertical-slices/soil-basics`
- `vertical-slices/solar-system-basics`
- `vertical-slices/source-provenance-authorship-trust`
- `vertical-slices/state-formation`
- `vertical-slices/statistics-basics`
- `vertical-slices/structural-engineering-basics`
- `vertical-slices/supply-chain-basics`
- `vertical-slices/systems-engineering-basics`
- `vertical-slices/systems-thinking-basics`
- `vertical-slices/telecommunications-basics`
- `vertical-slices/temperature-basics`
- `vertical-slices/thermodynamics-basics`
- `vertical-slices/time-standard-basics`
- `vertical-slices/trade-networks`
- `vertical-slices/transportation-basics`
- `vertical-slices/trigonometry-basics`
- `vertical-slices/units-and-measurement`
- `vertical-slices/urban-planning-basics`
- `vertical-slices/urbanization`
- `vertical-slices/virology-basics`
- `vertical-slices/volcanology-basics`
- `vertical-slices/waste-management-basics`
- `vertical-slices/wastewater-basics`
- `vertical-slices/water`
- `vertical-slices/water-filter-assessment`
- `vertical-slices/waves-and-sound-basics`
- `vertical-slices/weather-basics`
- `vertical-slices/wildfire-smoke-safety`
- `vertical-slices/writing-systems`
- `vertical-slices/zoology-basics`


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

Selected after CLEAN CHECKPOINT R5 using the Gap Map prioritization rule. These ten domains are new to the corpus, use existing Record types only, and form one controlled 10-slice CI unit.

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

Selected after CLEAN CHECKPOINT R6 to strengthen biological-computational, environmental, and applied-science linkage. These ten domains use existing Record types only and form one controlled 10-slice CI unit. Substantive audit is pending.

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

Wave 4 working target: **288 vertical slices / 2547 Records / 19 Record types**.


## CI execution discipline — no unfinished-test accumulation — 3 October 2026

The project must not create a growing backlog of abandoned, duplicated, or simultaneously running validation workflows.

Operational rule:
- Work in one controlled validation cycle at a time.
- Do not start a new substantive wave while the current validation cycle is unresolved.
- Every triggered Reference Test / Release Conformance Gate run must be brought to a terminal state (PASS, FAIL with a documented corrective action, or CANCELLED as an explicitly superseded run).
- When a newer commit supersedes an older validation run, the older run must not be allowed to remain indefinitely queued or in progress.
- Do not compensate for an unresolved CI run by creating additional commits or duplicate test runs merely to obtain a fresh result.
- Investigate and resolve the actual blocking condition first; then run validation against the current canonical commit.
- A checkpoint is not closed until the current commit has complete evidence from the required validation gates.
- At any point, the working state must have one clearly identified canonical validation target and an explicit explanation for any non-terminal historical run.

This rule exists to preserve runner capacity, auditability, reproducibility, and a clear chain from change → validation → correction → final evidence. The objective is not merely to make tests run, but to work each problem through to a complete, evidenced resolution before moving on.


## R7 CLEAN CHECKPOINT — 3 October 2026

Wave 4 substantive audit completed on canonical commit 6580124fccf9cc3717f9bc825d6317cd66169518.

- Audit: FULL-CORPUS-AUDIT-2026-10-03-R7
- Release Conformance Gate #1167: PASS
- Offline Edition #324: PASS
- Corpus: **288 vertical slices / 2547 Records / 19 Record types**
- Blocking findings: **0**
- Architectural changes required: **0**
- Status: **CLEAN WITH NON-BLOCKING DEBT**

Carried forward: cross-domain linkage, further content-depth expansion, and domain-specific editorial evidence for safety-sensitive/high-consequence domains.


## Gap Map R5 — accelerated Wave 5 registry — 3 October 2026

Selected after CLEAN CHECKPOINT R7 to address carried-forward content-depth, continuity/resilience, health-system, infrastructure, data-lifecycle, and operational-risk gaps. These ten domains use existing Record types only and form one controlled 10-slice CI unit.

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

Wave 5 working target: **298 vertical slices / 2637 Records / 19 Record types**.


## R8 CLEAN CHECKPOINT — 3 October 2026

Wave 5 substantive audit completed across the 298-slice / 2637-record corpus.

- Audit: FULL-CORPUS-AUDIT-2026-10-03-R8
- Wave 5 content baseline Release Gate #1170: PASS
- Current Offline Edition #328: PASS
- Corpus: **298 vertical slices / 2637 Records / 19 Record types**
- Blocking findings: **0**
- Architectural changes required: **0**
- Status: **CLEAN WITH NON-BLOCKING DEBT**

Carried forward: cross-domain linkage, further content-depth expansion, and domain-specific editorial evidence for safety-sensitive/high-consequence domains.

Next: controlled Gap Map Wave 6 → CI → substantive audit → next checkpoint.


## Gap Map R6 — accelerated Wave 6 registry — 3 October 2026

Selected after CLEAN CHECKPOINT R8 to continue domain breadth while strengthening data systems, energy, geospatial infrastructure, public services, sanitation, digital health, wastewater, fire safety, nutrition, and medicine-safety coverage. These ten domains are new to the corpus, use existing Record types only, and form one controlled 10-slice CI unit.

- vertical-slices/database-systems-basics
- vertical-slices/energy-systems-basics
- vertical-slices/geographic-information-systems-basics
- vertical-slices/public-transport-basics
- vertical-slices/sanitation-basics
- vertical-slices/telemedicine-basics
- vertical-slices/wastewater-engineering-basics
- vertical-slices/fire-safety-basics
- vertical-slices/nutrition-science-basics
- vertical-slices/pharmacovigilance-basics

Wave 6 working target: **308 vertical slices / 2727 Records / 19 Record types**.


## R9 CLEAN CHECKPOINT — 3 October 2026

Wave 6 substantive audit completed across the 308-slice / 2727-record corpus.

- Audit: FULL-CORPUS-AUDIT-2026-10-03-R9
- Reference implementation tests #947: PASS on 56ab81e
- Release Conformance Gate #1174: PASS on 56ab81e
- Corpus: **308 vertical slices / 2727 Records / 19 Record types**
- Blocking findings: **0**
- Architectural changes required: **0**
- Status: **CLEAN WITH NON-BLOCKING DEBT**

The corpus validation baselines are now data-driven from the coverage manifest or actual corpus, reducing repeated stale-count failures during controlled expansion.

Carried forward: cross-domain linkage, further content-depth expansion, and domain-specific editorial evidence for safety-sensitive/high-consequence domains.

Next: controlled Gap Map Wave 7 → CI → substantive audit → next checkpoint.


## Gap Map R7 — accelerated Wave 7 registry — 3 October 2026

Selected after CLEAN CHECKPOINT R9 to expand computing, embedded systems, human–AI interaction, industrial safety, information security operations, sensing, infrastructure economics, transportation, version control, and waste infrastructure. These ten domains use existing Record types only and form one controlled 10-slice CI unit.

- vertical-slices/computer-graphics-basics
- vertical-slices/embedded-systems-basics
- vertical-slices/human-ai-interaction-basics
- vertical-slices/industrial-safety-basics
- vertical-slices/information-security-operations-basics
- vertical-slices/sensor-systems-basics
- vertical-slices/supply-and-demand-infrastructure-basics
- vertical-slices/transportation-infrastructure-basics
- vertical-slices/version-control-basics
- vertical-slices/waste-infrastructure-basics

Wave 7 working target: **318 vertical slices / 2817 Records / 19 Record types**.

The authoritative corpus baseline is RELEASE/CONTENT-COVERAGE.json; fixed historical counts must not be used by current regression tests.


## Gap Map R7 — Wave 7 completion — 3 October 2026

The second controlled Wave 7 unit adds ten non-duplicate society and institutions domains:

- vertical-slices/political-economy-basics
- vertical-slices/comparative-law-basics
- vertical-slices/administrative-law-basics
- vertical-slices/international-law-basics
- vertical-slices/civil-society-basics
- vertical-slices/social-policy-basics
- vertical-slices/taxation-basics
- vertical-slices/labor-economics-basics
- vertical-slices/migration-and-mobility-basics
- vertical-slices/comparative-civilizations-basics

Wave 7 completion target: **328 vertical slices / 2907 Records / 19 Record types**.

The authoritative corpus baseline is RELEASE/CONTENT-COVERAGE.json. Current validation must derive corpus size from the actual CONTENT/vertical-slices tree and the coverage manifest; historical Wave 7 counts are checkpoint evidence only.


## Gap Map R8 — accelerated Wave 8 registry — 3 October 2026

Selected after CLEAN checkpoint R10 by reconciling the actual corpus with the current Gap Map. Seven domains close still-missing historical/cultural G1 gaps; three additional domains strengthen water, climate and infrastructure-resilience linkage. All use existing Record types only.

- vertical-slices/historical-geography-basics
- vertical-slices/economic-history-basics
- vertical-slices/history-of-science-basics
- vertical-slices/history-of-technology-basics
- vertical-slices/religious-studies-basics
- vertical-slices/literature-basics
- vertical-slices/cultural-anthropology-basics
- vertical-slices/water-security-basics
- vertical-slices/climate-adaptation-basics
- vertical-slices/infrastructure-resilience-basics

Wave 8 target: **338 vertical slices / 2997 Records / 19 Record types**.


## Gap Map R9 — accelerated Wave 9 registry — 3 October 2026

Selected after CLEAN checkpoint `222061e3752c2079a4fc7defb83875395dbfb404` by reconciling the actual corpus with absent-domain candidates. The ten domains strengthen history of knowledge, spatial systems, hydraulic engineering, food systems, cultural heritage and documentary preservation. All use existing Record types only.

- vertical-slices/history-of-medicine-basics
- vertical-slices/history-of-mathematics-basics
- vertical-slices/history-of-engineering-basics
- vertical-slices/cartography-basics
- vertical-slices/hydraulic-engineering-basics
- vertical-slices/food-systems-basics
- vertical-slices/cultural-heritage-basics
- vertical-slices/library-science-basics
- vertical-slices/archival-science-basics
- vertical-slices/settlement-geography-basics

Wave 9 target: **348 vertical slices / 3090 Records / 19 Record types**.

The authoritative corpus baseline remains RELEASE/CONTENT-COVERAGE.json. Current validation must derive corpus size from actual content and the coverage manifest; historical counts are checkpoint evidence only.


## Wave 9 substantive audit — 3 October 2026

R9 passed substantive audit with **0 blocking findings** and **0 architectural changes required**. Three explicit cross-slice relations were added under the existing linkage frame. Audited corpus: **348 vertical slices / 3093 Records / 19 Record types**. Non-blocking debt remains: content depth, independent-source triangulation, broader linkage, and domain-specific editorial evidence. Next: full CI on the audited tree, then CLEAN checkpoint if green.


## R10 CLEAN CHECKPOINT and Gap Map Wave 10 — 3 October 2026

R10 CLEAN checkpoint was verified on `7d649cb56ad0cafc893d9e9df8187be6c6437767` with Reference implementation tests #994, Release Conformance Gate #1296, Offline Edition #458, and Content Preflight all passing. The Reference Tests workflow was corrected to trigger on `CONTENT/**` so content-only changes cannot bypass the reference regression suite.

Gap Map R10 selects ten non-duplicate domains: mechanical engineering, chemical engineering, industrial engineering, geodesy, surveying, mining engineering, disaster recovery, public procurement, building services engineering, and metallurgy. Target: **358 vertical slices / 3183 Records / 19 Record types**.

R10 controlled domain registry:
- vertical-slices/mechanical-engineering-basics
- vertical-slices/chemical-engineering-basics
- vertical-slices/industrial-engineering-basics
- vertical-slices/geodesy-basics
- vertical-slices/surveying-basics
- vertical-slices/mining-engineering-basics
- vertical-slices/disaster-recovery-basics
- vertical-slices/public-procurement-basics
- vertical-slices/building-services-engineering-basics
- vertical-slices/metallurgy-basics


## Gap Map R11 — 4 October 2026

Controlled Wave 11 adds ten absent domains: measurement-science-basics, calibration-basics, standards-and-certification-basics, research-methods-basics, statistics-inference-basics, quantum-mechanics-basics, manufacturing-processes-basics, quality-management-basics, human-factors-basics, environmental-policy-basics. The wave uses the existing Source → 3 Claims → 3 Evidence Use → Context → Scope profile and dedicated regression tests; no new Record type is introduced. Target: **368 vertical slices / 3277 Records / 19 Record types**. The unit remains open until preflight, Reference Tests, Release Gate, Offline Edition and substantive audit evidence are green.


R11 canonical slice registry:
- vertical-slices/measurement-science-basics
- vertical-slices/calibration-basics
- vertical-slices/standards-and-certification-basics
- vertical-slices/research-methods-basics
- vertical-slices/statistics-inference-basics
- vertical-slices/quantum-mechanics-basics
- vertical-slices/manufacturing-processes-basics
- vertical-slices/quality-management-basics
- vertical-slices/human-factors-basics
- vertical-slices/environmental-policy-basics


## R11 CLEAN CHECKPOINT — 4 October 2026

R11 substantive audit is complete with **0 blocking findings**. Audited state: **368 vertical slices / 3282 Records / 19 Record types**. Final audited SHA `33d3930150acd08aa164cc9f1bdb0b3b2c074611` passed Offline Edition #494, Reference implementation tests #1025 and Release Conformance Gate #1332. This checkpoint becomes official after the checkpoint metadata itself passes all three gates.


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
- `vertical-slices/food-distribution-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/insurance-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/medical-devices-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/public-data-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/social-protection-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/traceability-systems-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.
- `vertical-slices/water-treatment-basics` — 9 Record: Source + 3 Claim + 3 Evidence Use + Context + Scope; dedicated regression.

## R15 — controlled ten-slice expansion — 4 October 2026

Selected after CLEAN R14 by reconciling the actual corpus registry. The final controlled ten-slice set contains only domains absent from the R14 CLEAN checkpoint.

- `vertical-slices/financial-markets-basics`
- `vertical-slices/central-banking-basics`
- `vertical-slices/competition-policy-basics`
- `vertical-slices/consumer-protection-basics`
- `vertical-slices/electoral-systems-basics`
- `vertical-slices/constitutional-law-basics`
- `vertical-slices/intellectual-property-basics`
- `vertical-slices/social-insurance-basics`
- `vertical-slices/financial-literacy-basics`
- `vertical-slices/payment-systems-basics`

R15 target: **408 vertical slices / 3647 Records / 19 Record types**. Closure requires preflight, Reference Tests, Release Gate, Offline Edition, substantive audit and final checkpoint.


## R15 replacement domains
- `vertical-slices/financial-literacy-basics`
- `vertical-slices/payment-systems-basics`


## R16 — controlled ten-slice expansion — 4 October 2026

R16 is selected from the current corpus Gap Map after R15 CLEAN. The ten candidates were checked against the actual `CONTENT/vertical-slices` tree and are absent. The wave uses the existing 19 Record types and the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope profile.

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

Target after authoring: **418 vertical slices / 3737 Records / 19 Record types**.

Definition of Done: dedicated regressions → corpus/semantic/Human View checks → package/recovery → Reference Tests → Release Gate → Offline Edition → substantive R16 audit → CLEAN checkpoint.

No new Record type is introduced by R16.


## R16 CI recheck state — 4 October 2026

R16 authoring is complete at the canonical controlled-wave commit. Final CI validation is required before substantive audit and CLEAN checkpoint promotion.


## R17 — controlled ten-slice expansion — 4 October 2026

R17 begins from the R16 CLEAN checkpoint at **418 vertical slices / 3737 Records / 19 Record types**. The wave is registered in `RELEASE/CONTENT-GAP-MAP-2026-10-04-R17.md` and uses the existing Source → 3 Claims → 3 Evidence Use → Context → Scope profile.

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

Target after authoring: **428 vertical slices / 3827 Records / 19 Record types**.

Definition of Done: dedicated regressions → corpus/semantic/Human View checks → package/recovery → Reference Tests → Release Gate → Offline Edition → substantive R17 audit → CLEAN checkpoint.

No new Record type is introduced by R17.

The full R1–R17 project/corpus audit remains deferred to the planned R20 gate.


## R18 — controlled ten-slice expansion — 4 October 2026

R18 begins from the R17 CLEAN state at **428 vertical slices / 3827 Records / 19 Record types**. The wave strengthens practical built-environment knowledge needed for later System-in-Action scenarios while preserving the existing 19-type architecture.

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

Target after authoring: **438 vertical slices / 3917 Records / 19 Record types**.

Definition of Done: dedicated regressions → corpus/semantic/Human View checks → package/recovery → Reference Tests → Release Gate → Offline Edition → substantive R18 audit → CLEAN checkpoint.

No new Record type is introduced by R18. The full project/corpus audit remains reserved for the planned R20 gate.


## R19 — controlled ten-slice expansion — 5 October 2026

R19 adds ten non-duplicate foundation and cross-domain slices using the canonical Source → 3 Claims → 3 Evidence Use → Context → Scope profile and existing Record types only.

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

R19 adds 90 Records: **448 vertical slices / 4007 Records / 19 Record types**. Full R1–R19 corpus audit remains reserved for R20.

## R19 — controlled ten-slice expansion — 5 October 2026

R19 begins from the R18 CLEAN state at **438 vertical slices / 3917 Records / 19 Record types**. Candidate selection was reconciled against the actual corpus; overlapping domains were replaced before authoring.

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

Target after authoring: **448 vertical slices / 4007 Records / 19 Record types**.

Definition of Done: dedicated regressions → corpus/semantic/Human View checks → package/recovery → Reference Tests → Release Gate → Offline Edition → substantive R19 audit → CLEAN checkpoint.

No new Record type is introduced by R19. The full R1–R19 project/corpus audit remains reserved for the planned R20 gate.


## R21 — controlled ten-slice expansion — 5 October 2026

R21 follows the R20 FULL-CORPUS CLEAN checkpoint at **448 vertical slices / 4007 Records / 19 Record types**. Candidate selection was reconciled against the actual corpus; all ten selected domains are absent and use existing Record types only.

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

Target after authoring: **458 vertical slices / 4097 Records / 19 Record types**.

Definition of Done: dedicated regressions → corpus/semantic/Human View checks → package/recovery → Reference Tests → Release Gate → Offline Edition → substantive R21 audit → CLEAN checkpoint.

No new Record type is introduced by R21. The next periodic full-corpus audit remains deferred by plan.


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

R23 target after authoring: **478 vertical slices / 4277 Records / 19 Record types**.


## R23 CLEAN CHECKPOINT — 5 October 2026

R23 substantive audit is CLEAN. Audited state: **478 vertical slices / 4277 Records / 19 Record types**. Final audited content commit `f9975a8c2351bee5e13a338773adad2e94c31251` passed Reference implementation tests #37301464581, Release Conformance Gate #37301464562 and Offline Edition #37301464595. The dedicated cross-slice linkage baseline is 26 Relation records; the corpus has 27 Relation records total including the pre-existing domain Relation in `emergency-water-storage-state`. Checkpoint metadata is now subject to the same three-gate validation before R24 authoring begins.


## Readiness maturation phase — 5 October 2026

The project readiness audit confirms that the system is working and the corpus is substantial, while encyclopedic completeness has not yet been claimed. Development now prioritizes **depth → independent triangulation → cross-domain integration → Human View validation**, with new breadth added where Gap Maps identify meaningful missing coverage.

Authoritative records:
- `RELEASE/PROJECT-READINESS-AUDIT-2026-10-05.md`
- `RELEASE/READINESS-ROADMAP-2026-10-05.md`

The R23 CLEAN baseline remains the protected starting point for this maturation phase.
