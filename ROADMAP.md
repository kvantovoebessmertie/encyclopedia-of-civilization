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
