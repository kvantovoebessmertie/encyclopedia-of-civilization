# 014 — Эталонная реализация

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: рабочая нормативная спецификация  
Дата: 29 сентября 2026 года

---

## 1. Назначение

Эталонная реализация — минимальная реализация архитектуры, предназначенная для проверки того, что спецификации действительно реализуемы.

Она не является единственной реализацией проекта.

## 2. Требование независимости

Эталонная реализация должна быть:

- локальной;
- воспроизводимой;
- минимальной;
- документированной;
- заменяемой;
- пригодной для работы без сети.

Выбор языка и библиотек не должен становиться частью канонической семантики.

## 3. Минимальный вертикальный срез

Реализация должна поддерживать первый рабочий набор:

- record;
- claim;
- source;
- evidence_use;
- assessment.

Для каждого типа должны применяться соответствующие Content Profiles и Schema.

## 4. Pipeline

Минимальный pipeline:

    input Record
        ↓
    Schema validation
        ↓
    Type/Profile validation
        ↓
    Reference validation
        ↓
    Semantic/Standard validation
        ↓
    integrity/history checks
        ↓
    Storage Adapter
        ↓
    Query/Edit Interface
        ↓
    Portable Package
        ↓
    Publication Builder
        ↓
    Recovery test

## 5. Determinism

Одинаковый вход и одинаковые версии компонентов должны давать эквивалентный результат.

Случайность должна быть либо исключена, либо явно контролироваться seed/configuration.

## 6. Configuration

Конфигурация должна быть явной.

Нельзя хранить критическую семантику только в:

- environment variables;
- локальном UI;
- скрытом cache;
- незафиксированной конфигурации.

## 7. Fixtures

Эталонная реализация должна использовать Fixtures из 007.

Обязательно должны присутствовать:

- positive;
- negative;
- unknown;
- conflict;
- history;
- reference;
- integrity;
- migration;
- package;
- recovery;
- anti-inference fixtures.

## 8. Golden outputs

Для детерминированных тестов должны сохраняться ожидаемые результаты.

Изменение Golden output требует объяснения и проверки архитектурного воздействия.

## 9. Error model

Реализация должна использовать стабильные коды ошибок Validator и Storage Adapter там, где они определены.

Текст сообщения может изменяться, но машинный код должен оставаться стабильным в пределах совместимой версии.

## 10. Logging

Логи должны позволять диагностировать:

- component;
- version;
- operation;
- Record identity;
- result;
- error code.

Логи не должны содержать секреты без необходимости.

## 11. Test execution

Минимальный прогон должен включать:

- Schema tests;
- Validator tests;
- Fixture tests;
- Migration tests;
- Package tests;
- Storage tests;
- Query/Edit tests;
- Publication tests;
- Recovery tests;
- anti-inference tests.

## 12. Offline operation

Эталонная реализация должна работать без внешних API для базового набора тестов.

## 13. Security baseline

Запрещены:

- выполнение данных как кода;
- произвольные внешние загрузки;
- небезопасное распаковывание;
- path traversal;
- неявная миграция;
- запись поверх исторической версии.

## 14. Compatibility

Реализация должна явно объявлять:

- Schema version;
- Profile versions;
- Standard versions;
- Validator version;
- Migration versions;
- Package version.

## 15. Acceptance tests

- I01 — минимальный Record проходит pipeline;
- I02 — неверный Record отклоняется;
- I03 — Claim/Source/Evidence Use/Assessment различаются;
- I04 — historical reference сохраняется;
- I05 — unknown discipline сохраняется;
- I06 — migration не выполняется скрыто;
- I07 — package round-trip сохраняет Record;
- I08 — storage backend можно заменить;
- I09 — publication не меняет Record;
- I10 — recovery проходит в clean environment.

## 16. Stress tests

- I11 — большое число Record;
- I12 — большая история;
- I13 — большой graph;
- I14 — большие тексты;
- I15 — Unicode;
- I16 — массовая миграция;
- I17 — массовый import/export;
- I18 — concurrent updates;
- I19 — повреждение данных;
- I20 — повторный recovery.

## 17. Invariants

1. Эталонная реализация не является источником семантики.
2. Она не заменяет Standards.
3. Она не определяет истинность Claim.
4. Она должна быть воспроизводимой.
5. Она должна быть offline-capable.
6. Она должна сохранять историю.
7. Она должна сохранять unknown states.
8. Она должна проверять anti-inference rules.

## 18. Критерии готовности

014 готов, если минимальный вертикальный срез может пройти полный pipeline от Record до Recovery в чистой среде.

## 19. Статус

Документ определяет требования к эталонной реализации, но не выбирает конкретный язык программирования.
