# 007 — Тестовые данные и Validation Fixtures

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: рабочая нормативная спецификация  
Дата: 29 сентября 2026 года

---

## 1. Назначение

Этот документ определяет архитектуру тестовых данных, fixtures и сценариев, необходимых для проверки реализации Энциклопедии цивилизации.

Fixture — контролируемый набор данных, предназначенный для воспроизводимой проверки конкретного правила или поведения системы.

Fixture не является частью канонического знания проекта и не должен незаметно смешиваться с производственными Record.

## 2. Место в архитектуре

FOUNDATION → STANDARD → IMPLEMENTATION → SCHEMA → VALIDATOR → TEST FIXTURES → IMPLEMENTATION VERIFICATION.

Fixtures проверяют реализацию. Они не изменяют нормативный смысл Foundation или Standard.

## 3. Цели

Fixtures должны позволять проверять:

- структурную валидность;
- типизацию;
- Content Profiles;
- ссылки;
- версии;
- publication_status;
- provenance;
- Scope и Context;
- unknown discipline;
- integrity;
- семантические инварианты;
- импорт и миграцию;
- portable package;
- offline recovery;
- отказоустойчивость.

Тестовый набор обязан содержать и успешные, и намеренно повреждённые данные.

## 4. Fixture не является канонической Record

Fixture не получает автоматически статус канонической Record.

Тестовое пространство должно быть отделено от production namespace.

Реальные идентификаторы production не следует использовать в fixtures без специального правила.

## 5. Воспроизводимость

Каждый fixture должен иметь:

- стабильный fixture_id;
- fixture_version;
- назначение;
- входные данные;
- применимые Schema;
- применимые Type Profiles;
- применимые Standards;
- ожидаемый статус;
- ожидаемые findings или error codes;
- описание проверяемого правила.

Ожидаемый результат не должен зависеть от интерфейса.

## 6. Классы fixtures

Минимально:

- F-VALID — корректные Record;
- F-INVALID — нарушающие ограничения Record;
- F-UNKNOWN — Record с допустимой неизвестностью;
- F-CONFLICT — конфликтующие Record;
- F-HISTORY — исторические цепочки;
- F-REFERENCE — ссылочные графы;
- F-INTEGRITY — integrity и повреждения;
- F-MIGRATION — старые версии и миграции;
- F-PACKAGE — переносимые пакеты;
- F-RECOVERY — восстановление offline.

## 7. Fixture Manifest

Manifest должен позволять установить:

- fixture_id;
- fixture_version;
- purpose;
- schema_version;
- type_profile_versions;
- standard_versions;
- expected_status;
- expected_findings;
- входные файлы.

Manifest описывает тестовый набор и не заменяет Validation Run.

## 8. Ожидаемые результаты

Допустимые ожидаемые статусы:

- pass;
- fail;
- indeterminate.

При ожидаемом failure должны указываться конкретные классы нарушений.

Тест не считается успешным только потому, что Validator завершился без исключения.

## 9. Позитивные fixtures

Минимальный набор:

- минимальная Record;
- Claim;
- Source;
- Evidence Use;
- Assessment;
- Record с provenance;
- Record с Scope;
- Record с Context;
- Record с временным интервалом;
- несколько версий одной Record.

## 10. Негативные fixtures

Минимально:

- отсутствует обязательное поле;
- неверный тип значения;
- неизвестный publication_status;
- неизвестный record_type;
- registered, но unsupported type;
- несовместимый type_version;
- повреждённая ссылка;
- отсутствующая версия цели;
- неверная provenance;
- нарушение profile constraint;
- повреждённый digest;
- повреждённая version chain;
- запрещённое семантическое преобразование.

## 11. Unknown fixtures

Отдельно тестируются:

- unknown;
- absent;
- not_applicable;
- not_observed;
- not_recorded.

Тест должен обнаруживать ошибочное преобразование unknown → absent и not_observed → false.

## 12. Reference fixtures

Минимальная матрица:

| Сценарий | Ожидание |
|---|---|
| существующая Record | pass |
| отсутствующая Record | reference finding |
| неверный тип цели | reference-type finding |
| нужная версия существует | pass |
| нужной версии нет | reference-version finding |
| историческая ссылка заменена текущей | failure |
| циклическая ссылка | проверка по применимому правилу |
| внешний ресурс недоступен | indeterminate, если необходим |

## 13. Version fixtures

Нужно тестировать:

- первую версию;
- последовательные версии;
- допустимое ветвление;
- неправильный predecessor;
- цикл;
- дубликат версии;
- ссылку на конкретную историческую версию;
- ссылку без версии там, где она допустима;
- ссылку без версии там, где требуется историческая точность.

## 14. Semantic fixtures

Обязательны тесты границ:

    published ≠ true
    Source ≠ Evidence
    Evidence Use ≠ truth
    provenance ≠ truth
    hash valid ≠ truth
    conflict ≠ falsehood
    pass ≠ truth
    fail ≠ falsehood
    unknown ≠ absent

## 15. Deterministic fixtures

Одинаковые входы, версии правил, конфигурация и зависимости должны давать эквивалентный результат.

По возможности тесты не должны обращаться в интернет.

## 16. Regression fixtures

Каждая обнаруженная архитектурная ошибка должна по возможности получать regression fixture.

Исправленная ошибка не должна возвращаться незаметно.

Regression fixture должен быть минимальным, воспроизводимым и привязанным к правилу.

## 17. Golden fixtures

Golden fixture содержит:

- вход;
- ожидаемый ValidationResult;
- версии правил;
- дату создания/обновления;
- причину появления теста.

Изменение golden result требует объяснимого изменения правила или теста.

## 18. Mutation и property testing

По мере развития следует добавлять:

- property-based tests;
- mutation tests;
- fuzzing;
- повреждение случайных полей;
- перестановку Record;
- изменение порядка файлов;
- удаление необязательных полей;
- дублирование Record.

## 19. Stress fixtures

Минимум:

- большая Record;
- большой граф ссылок;
- глубокая цепочка версий;
- много конфликтующих Claim;
- повреждённый пакет;
- много неизвестных полей;
- много внешних зависимостей;
- циклический граф;
- повторяющиеся Record;
- смешение версий Schema и Type Profile.

## 20. Security fixtures

Нужно тестировать:

- огромные строки;
- глубоко вложенные объекты;
- повреждённый JSON;
- неожиданные типы;
- вредоносный текст;
- поддельные внешние идентификаторы;
- недоверенные пути;
- попытки заставить систему выполнить данные как инструкции.

Record является данными, а не исполняемым кодом.

## 21. Migration fixtures

Для каждой поддерживаемой миграции должны существовать:

    before
    migration
    after
    expected semantic invariants

Проверяется не только техническая валидность, но и сохранение существенно значимой семантики.

## 22. Package fixtures

Минимальный пакет должен проверять:

- manifest;
- Record;
- Schema;
- Type Profiles;
- Validator metadata;
- integrity;
- восстановление;
- итоговую проверку.

Повреждение каждого существенного компонента должно иметь тест.

## 23. Recovery fixtures

Recovery fixture должен позволять:

    clean environment
        ↓
    acquire archive
        ↓
    verify integrity
        ↓
    load schema
        ↓
    load records
        ↓
    run validator
        ↓
    rebuild representation

Результат сравнивается с ожидаемым recovery result.

## 24. Anti-inference fixtures

Особенно важны тесты, запрещающие скрытый вывод:

- тип из имени файла;
- Scope из местоположения пользователя;
- Context из текущей даты;
- Truth из publication_status;
- Evidence из Source;
- версия из последнего доступного состояния;
- значение из похожего поля;
- авторство из аккаунта;
- семантика из визуального оформления.

## 25. Fixture naming

Рекомендуемый формат:

    FIX-L1-001
    FIX-L2-001
    FIX-L3-001
    FIX-L4-001
    FIX-L5-001
    FIX-MIG-001
    FIX-PKG-001
    FIX-REC-001

Имя файла не является единственным источником идентичности fixture.

## 26. Тестовая матрица

| Слой | Positive | Negative | Unknown | Conflict | History |
|---|---:|---:|---:|---:|---:|
| L1 | ✓ | ✓ | ✓ | — | — |
| L2 | ✓ | ✓ | ✓ | — | ✓ |
| L3 | ✓ | ✓ | ✓ | ✓ | ✓ |
| L4 | ✓ | ✓ | ✓ | ✓ | ✓ |
| L5 | ✓ | ✓ | ✓ | ✓ | ✓ |

Прочерк означает, что категория не обязательна для слоя.

## 27. Acceptance criteria

007 считается готовым, если:

- определён формат fixture;
- определён manifest;
- разделены positive/negative/unknown/conflict/history;
- предусмотрены regression fixtures;
- предусмотрены migration/package/recovery fixtures;
- предусмотрены security fixtures;
- предусмотрена deterministic проверка;
- определена naming policy;
- определена тестовая матрица;
- fixtures не смешиваются с каноническим знанием;
- ожидаемый результат привязан к версиям правил.

## 28. Инварианты

1. Fixture не становится канонической Record автоматически.
2. Тест имеет воспроизводимый вход.
3. Ожидаемый результат проверяем.
4. Failure привязан к правилу.
5. Unknown не превращается в absent.
6. Positive test не доказывает истинность предметного содержания.
7. Regression test сохраняется после исправления дефекта.
8. Migration test проверяет сохранение семантики.
9. Recovery test проверяет восстановимость.
10. Security test не выполняет данные как код.

## 29. Статус

Версия 0.1.

Документ определяет архитектуру тестовых данных. Он не заменяет конкретный test runner и не создаёт новые нормативные правила предметного знания.
