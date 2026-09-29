# 017 — Соответствие и выпуск

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: рабочая нормативная спецификация  
Дата: 29 сентября 2026 года

---

## 1. Назначение

Документ определяет, когда реализация может считаться соответствующей Implementation Architecture и когда результат может быть выпущен как проверяемый артефакт.

Conformance не означает истинность содержания.

## 2. Conformance levels

Для технического контроля используются:

- not_ready — обязательные компоненты отсутствуют;
- partial — реализована только часть архитектуры;
- conforming — обязательные требования выполнены;
- conforming_with_limitations — требования выполнены с явно задокументированными ограничениями.

Эти состояния не являются оценкой качества знаний.

## 3. Required components

Полный Implementation слой должен иметь:

    000 Model
    001 Envelope
    002 Schema Architecture
    003 Type Registry
    004 Content Profiles
    005 Machine Schema
    006 Validator Architecture
    007 Test Fixtures
    008 Versioning/Migration
    009 Portable Package
    010 Storage Adapter
    011 Query/Edit Interface
    012 Publication Builder
    013 Recovery/Reproducibility
    014 Reference Implementation
    015 Context
    016 Operations/Security
    017 Conformance/Release

## 4. Conformance matrix

Проверяются как минимум:

- Foundation compatibility;
- Standard compatibility;
- envelope consistency;
- schema consistency;
- type registry consistency;
- profile consistency;
- validator coverage;
- fixture coverage;
- versioning/migration;
- package portability;
- storage independence;
- query/edit safety;
- publication independence;
- recovery;
- reproducibility;
- Context enforcement;
- security;
- operational controls.

## 5. Release artifact

Каждый выпуск должен иметь:

- release_id;
- дата;
- commit/reference;
- Implementation version;
- Schema versions;
- Profile versions;
- Standard versions;
- Validator version;
- migration versions;
- package version;
- test result;
- known limitations;
- integrity metadata.

## 6. Release gates

Минимальные gates:

1. Schema parses;
2. implemented profiles validate;
3. Validator architecture checks pass;
4. Fixtures pass;
5. migration tests pass;
6. package integrity passes;
7. storage tests pass;
8. query/edit tests pass;
9. publication tests pass;
10. recovery test passes;
11. security baseline passes;
12. no unresolved critical contradiction.

### 6.1. Semantic Standard → Implementation matrix

Release gate 3 считается выполненным для 011–018 только в части правил, которые относятся к Validator. Для остальных нормативных правил должна быть зафиксирована ответственность соответствующего слоя.

Минимальное требование перед объявлением полного semantic conformance:

- каждое правило 011–018 имеет owner-layer;
- каждое машинно диагностируемое правило имеет стабильный finding/error code;
- каждое такое правило имеет fixture/test;
- context-dependent правила имеют явные условия применимости;
- anti-inference правила имеют негативные тесты;
- transformation-fidelity правила проверяются Migration/Publication/Recovery, а не имитируются через required-поля.

Для 015 Context дополнительно должны быть видимы:

- target-resolution boundary;
- historical-context boundary;
- inheritance/precedence status;
- transferability status;
- Context Fidelity status;
- enforcement debt.

## 7. Failure policy

Если обязательный gate не пройден, release не должен объявляться conforming.

Known limitation должна быть явно указана.

Нельзя скрывать failure удалением теста или ослаблением критерия без отдельного архитектурного решения.

## 8. Regression

Каждый release должен прогонять ранее принятые:

- fixtures;
- golden outputs;
- migration tests;
- package tests;
- recovery tests;
- anti-inference tests;
- Context tests.

Изменение ожидаемого результата требует объяснения.

## 9. Audit record

Audit должен фиксировать:

- набор проверенных файлов;
- commit;
- время проверки;
- правила;
- результаты;
- найденные проблемы;
- исправления;
- итоговый статус.

## 10. Ten-pass audit

Для полного Implementation audit используются десять независимых проходов:

### A1 — структура
Все обязательные файлы существуют, имена и зависимости корректны.

### A2 — Foundation
Нет противоречий с FOUNDATION.

### A3 — Standards
Нет переопределения STANDARD.

### A4 — Identity/Version
Разделены identity, Record version, Type version, Schema version, Standard version, Validator version и Package version.

### A5 — Epistemic anti-inference
Не допускается вывод truth из publication, provenance, integrity, validation pass или storage success.

### A6 — History/Unknown
Сохраняются история, исторические ссылки и различия unknown/absent/not_applicable/not_observed/not_recorded.

### A7 — Portability
Пакет, Storage Adapter и Recovery не зависят от конкретной платформы.

### A8 — Security
Проверяются path traversal, code execution, external resources, secrets, permissions, package extraction и недоверенные данные.

### A9 — Tests
Все заявленные test/stress suites имеют место и не противоречат архитектуре.

### A10 — Language/Consistency
Нормативный текст преимущественно на русском; термины согласованы; старые названия полей не остались; cross-document references корректны.

## 11. Release decision

Итоговый технический статус определяется только по установленным gates:

- PASS;
- FAIL;
- INDETERMINATE.

PASS означает техническое соответствие проверенным требованиям, а не истинность содержания.

## 12. Invariants

1. Conformance не означает truth.
2. Release не меняет Record.
3. Failure не скрывается.
4. Historical versions сохраняются.
5. Package остаётся переносимым.
6. Schema и Standards не подменяются Release metadata.
7. Audit воспроизводим.
8. Все критические ограничения явно указаны.

## 13. Критерии готовности

017 готов, если определены conformance states, required components, matrix, release artifact, gates, failure policy, regression, audit record и ten-pass audit.

## 14. Статус

Документ является последним нормативным слоем Implementation Architecture.

После него изменения реализации должны проходить через conformance/audit process, а не добавляться в архитектуру неформально.
