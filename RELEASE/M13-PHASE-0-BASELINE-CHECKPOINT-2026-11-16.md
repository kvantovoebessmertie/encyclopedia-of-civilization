# M13 — контрольная точка Phase 0: фиксация базового состояния

**Дата:** 16 ноября 2026 года  
**Статус:** Phase 0 пройдена на зафиксированной вершине `005470fcb3899b7e5db8dc4f3017e8c1f85f14c2`.

## 1. Зафиксированная версия репозитория

| Параметр | Значение |
|---|---|
| Репозиторий | `kvantovoebessmertie/encyclopedia-of-civilization` |
| Рабочая ветка | `m13-system-wide-depth-audit-2026-10-09` |
| Контрольный HEAD Phase 0 | `005470fcb3899b7e5db8dc4f3017e8c1f85f14c2` |
| PR | #21 |
| Состояние PR | Open, Draft, не слит |
| Базовая ветка PR | `m12-human-factors-source-and-human-view-2026-10-09` |
| SHA базовой ветки | `e87e5bba60c9ed1101ecd4d53493c968c4760dac` |
| SHA `main` | `203a7028e08da394fd44630fe38727be07bc8849` |

`main` не изменялся. PR #21 не переводился из Draft и не сливался.

## 2. CI на точном HEAD

Все три обязательные PR-проверки были настроены на checkout точного `pull_request.head.sha`, а не синтетического merge commit. Отдельный шаг `Verify exact source revision` подтвердил совпадение фактического `git rev-parse HEAD` с ожидаемым SHA.

| Проверка | Workflow run | Результат |
|---|---:|---|
| Reference implementation tests | 43860046002 | PASS — 1 039 тестов |
| Release Conformance Gate | 43860045967 | PASS — CONFORMING, 1 039 тестов |
| Offline Edition | 43860045867 | PASS |
| M13 Audit Queue Automation | 43860036005 | PASS |
| M13 Generic Evidence Use Report Coverage | 43858044332 | PASS на предыдущем HEAD `12eafbc`; не считается exact-HEAD проверкой для `005470f` |

В Reference Tests все шаги генерации M13-артефактов и тестовый набор завершились успешно. Release Gate не сообщил блокирующих или ограничивающих ворот. Offline Edition собрала корпус из 4 851 записи.

Проверка Generic Evidence Use Report Coverage будет повторно запущена на следующем контрольном commit: добавление этого документа в `RELEASE/M13-**` входит в её фильтр путей.

## 3. Артефакты, привязанные к контрольному HEAD

| Артефакт | Run / Artifact ID | SHA-256 |
|---|---|---|
| M13 review queue и provenance mention ledger | 43860036005 / 14222758371 | `786746641db5280da027f6c47c3a8c5b211e8e7b867e65a934ff706155b4f31b` |
| M13 claim audit worksheet | 43860046002 / 14222498531 | `05bded70bfebdd17080a26455c3ab686efb3cd0342bb59566bbbae94f6ff151e` |
| Scored Claim reconciliation ledger | 43860046002 / 14223086616 | `f98c2e9d980a0b3cfaace561e30d98d803506d89eea1ef24cdec96d0ce1cdf4e` |
| Evidence linkage audit | 43860046002 / 14223246586 | `50a92c9773eb224d966b542751b2763620e3f58a554aa3d6eb54d6e57bd2ceed` |
| Release gate report | 43860045967 / 14222913501 | `582d230e02539fe69c2abe087bf12e189cc5362b5149cb96a730b28b752f10f6` |
| Offline Edition | 43860045867 / 14222982459 | `f79cab5803bad0dd8f60a2e37d78b253bc71d11fe59d56bb0b6a082ddbd42c87` |

Worksheet `source_revision` равен контрольному HEAD `005470fcb3899b7e5db8dc4f3017e8c1f85f14c2`. Queue и provenance ledger содержат ту же привязку.

## 4. Инвентарная база

| Показатель | Значение |
|---|---:|
| Всего записей корпуса | 4 851 |
| Claim records | 1 494 |
| Evidence Use records | 1 679 |
| Source records | 627 |
| Вертикальных срезов | 483 |

Основа инвентаря сформирована из фактических `record_type` и ссылок между записями. Машинные флаги являются сигналами маршрутизации, а не семантическими оценками и не доказательством низкого риска.

### 4.1. Состояние очереди без риск-метаданных

| Показатель | Значение |
|---|---:|
| Claims без `risk_domains` и `machine_triage_flags` | 751 |
| Из них с упоминаниями в прежних отчётах | 749 |
| Исторические holdout | 17 |
| Пересечение holdout с группой упоминаний | 15 |
| Новые кандидаты | **0** |
| Выбранные Claims | **0** |
| Evidence Packets | **0** |

Новый пакет создавать нельзя: автоматизация не обнаружила новых кандидатов. Это не основание считать 749 Claims полностью проверенными.

### 4.2. Provenance mention ledger

Ledger охватывает именно 751 Claim без риск-метаданных, а не весь корпус из 1 494 Claims.

- 749 Claims имеют хотя бы одно упоминание в настроенных отчётах.
- 2 Claims не имеют совпадений.
- Найдено 979 строк упоминаний в 47 документах.
- Типы совпадений: 905 exact, 73 grouped suffix, 1 separator alias.

Каждая строка содержит путь отчёта, номер строки, тип совпадения и текстовый фрагмент. Само упоминание — только поисковая зацепка: оно не доказывает содержательную проверку конкретной версии Claim, проверку первоисточника, завершённость D/E/B или прохождение публикационных ворот.

### 4.3. Holdout

15 Claims, пересекающихся с прежними отчётами:

- `CLM-DISASTER_RESPONSE_BASICS-A`
- `CLM-DISASTER_RESPONSE_BASICS-B`
- `CLM-DISASTER_RESPONSE_BASICS-C`
- `CLM-DISASTER_RISK_REDUCTION_BASICS-B`
- `CLM-INDUSTRIAL_SAFETY_BASICS-A`
- `CLM-INDUSTRIAL_SAFETY_BASICS-B`
- `CLM-INFRASTRUCTURE_RESILIENCE-A`
- `CLM-INFRASTRUCTURE_RESILIENCE-B`
- `CLM-INFRASTRUCTURE_RESILIENCE-C`
- `CLM-INFRASTRUCTURE_RESILIENCE-D`
- `CLM-SAFETY_ENGINEERING_BASICS-A`
- `CLM-SAFETY_ENGINEERING_BASICS-B`
- `CLM-SAFETY_ENGINEERING_BASICS-C`
- `CLM_PUBLIC_HEALTH_SURVEILLANCE_BASICS_B`
- `CLM_PUBLIC_HEALTH_SURVEILLANCE_BASICS_C`

Два holdout без совпадений:

- `CLM-DISASTER_RISK_REDUCTION_BASICS-C`
- `CLM-HYDROPOWER_BASICS-C`

### 4.4. Неустранённое расхождение 14 Claim ID

Первоначальный предварительный отчёт называет 17 просмотренных записей, но раскрывает только 3 точных Claim ID. История GitHub не содержит более ранней редакции этого файла с полным перечнем. Поэтому остальные 14 ID остаются невосстановленными.

Их нельзя заменять предположительными ID из последующих пакетов или автоматически отождествлять с 15 holdout-пересечениями.

## 5. Объяснение изменения 711 → 751

Сравнение worksheet от 15 и 16 ноября:

| Показатель | 15 ноября | 16 ноября |
|---|---:|---:|
| Records scanned | 4 834 | 4 851 |
| Claims | 1 494 | 1 494 |
| Claims с любым риск-сигналом | 783 | 743 |
| High-consequence screen | 591 | 520 |
| Legal/financial domain | 216 | 131 |
| Claims без риск-сигналов | 711 | 751 |

Причина основного изменения установлена. Прежнее правило `legal_financial` искало подстроку `tax` без границ слова. Из-за этого слово `OpenStax` ошибочно трактовалось как налоговый сигнал.

Из 85 Claims, потерявших прежнюю отметку `legal_financial`, 84 содержат `OpenStax` в связанной Evidence Use / Source информации. Из этих 84:

- 41 Claim теперь не имеет других риск-флагов; все 41 уже упомянуты в Package 32;
- 31 Claim сохраняет другие machine-triage flags;
- 12 Claims сохраняют другие risk domains.

Ещё один Claim, `CLM-ELECTRICAL_SAFETY_BASICS-A`, потерял только ошибочную legal/financial отметку, но сохраняет домены `emergency_fire_co` и `electricity_energy`.

Одновременно обнаружены два новых кандидата на избыточную классификацию:

- `CLM-MANUFACTURING_SYSTEMS_BASICS-C`: `health_medical` сработал на фразу об equipment performance/health;
- `CLM-MATTER_BASICS-A`: `chemicals_hazards` сработал на общее описание chemical properties.

Эти два случая пока не исправлены. Их нужно отдельно проверить при калибровке риск-правил. Машинные флаги не должны автоматически трактоваться как содержательные выводы.

## 6. Структурные результаты, требующие отдельной сверки

### Scored Claim reconciliation ledger

- 1 501 строка прежних оценочных отчётов;
- 1 494 уникальных нормализованных Claim ID;
- 7 групп дублирующихся строк (14 строк);
- 0 unmatched scored rows;
- 1 separator-normalized match требует ручного подтверждения;
- 163 различия между ID имени файла и внутренним ID: 160 различий только в разделителях и 3 настоящих mismatch.

Три настоящих mismatch находятся в `web-systems-basics`:

- `records/CLM-A.json` → internal ID `CLM-WEB_SYSTEMS_BASICS-A`;
- `records/CLM-B.json` → internal ID `CLM-WEB_SYSTEMS_BASICS-B`;
- `records/CLM-C.json` → internal ID `CLM-WEB_SYSTEMS_BASICS-C`.

### Evidence linkage audit

Обнаружено 1 117 структурных finding rows:

- 496 generic material description candidates;
- 493 separator-only filename ID aliases;
- 75 duplicate Source URI candidates;
- 47 source identity sentence candidates;
- 6 documented filename ID aliases.

Это статические сигналы для проверки, а не автоматическое доказательство дефекта. Записи не изменялись.

## 7. Ограничения и запреты на следующем этапе

1. Не создавать искусственный Batch: новых кандидатов нет.
2. Не считать ID mention завершённым аудитом.
3. Не объединять `Claim ID` и `Claim ID@version`.
4. Не менять канонические Claim, Evidence Use или Source без отдельного подтверждения дефекта и bounded authorization.
5. Не закрывать расхождение 14 ID предположениями.
6. Не переносить агрегированные показатели со старых HEAD на новую контрольную точку.

## 8. Решение Phase 0 и следующий этап

Phase 0 закрыта на контрольном HEAD `005470fcb3899b7e5db8dc4f3017e8c1f85f14c2`: точная вершина установлена, PR и базовая ветка сверены, обязательные CI прошли, queue artifact и provenance mention ledger созданы и проверены.

**Следующий этап — Phase 1: authoritative corpus inventory.** Он должен сформировать единую таблицу для всех 1 494 Claims с точными `Claim ID@version`, путём, срезом, связанными Evidence Use и Source, структурными finding, risk metadata и текущим статусом. Затем — полная историческая трассировка отчётов для всех Claims, а не только для 751 записей без риск-метаданных.

До завершения этой сверки не создавать новые пакеты и не менять канонические записи.
