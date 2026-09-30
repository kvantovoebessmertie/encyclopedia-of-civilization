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
