# Эталонная реализация — первый вертикальный срез

## Назначение

Этот каталог содержит исполняемую эталонную реализацию архитектуры проекта «Энциклопедия цивилизации».

Это **не новый нормативный слой**. Нормативным источником остаются FOUNDATION, STANDARD и документы IMPLEMENTATION 000–021.

Текущий вертикальный срез реализует 19 зарегистрированных типов:

- `record`
- `claim`
- `source`
- `evidence_use`
- `assessment`
- `inference`
- `decision`
- `action`
- `event`
- `result`
- `trust_reputation`
- `authorship_contribution`
- `provenance`
- `scope`
- `context`
- `identity`
- `relation`
- `process`
- `state`

## Требования

- Python 3.11+
- пакет `jsonschema`
- работа без сети после установки зависимостей

## Запуск

Из каталога репозитория:

```bash
python -m pytest REFERENCE/tests
```

Для установки:

```bash
python -m pip install -e REFERENCE
```

## Границы

Реализация:

- валидирует Record относительно канонической схемы;
- выполняет базовые проверки Type Profile и ссылочной целостности;
- сохраняет версии в файловом Storage Adapter;
- не перезаписывает исторические версии;
- поддерживает Query/Edit с optimistic concurrency;
- строит производное публикационное представление;
- выполняет offline recovery;
- содержит anti-inference проверки.

Реализация **не определяет истинность Claim** и не выводит её из publication_status, provenance, integrity или результата валидации.


CI: тестовый набор запускается GitHub Actions после изменений в `REFERENCE/**`.


Последняя контрольная правка resolver: синтаксис исправлен после CI.


Контроль: профили 011–019 и разделение provenance envelope/profile завершены.


Контроль: восстановлен канонический Envelope provenance.


Stress suite: destructive scenarios are maintained in `REFERENCE/tests/test_stress.py`.

Stress regression pass 2.

Stress regression pass 3: versions, package traversal, malformed manifests, duplicate entries.

Stress profile documented in IMPLEMENTATION/007.

Deterministic fuzz/property tests are maintained in `REFERENCE/tests/test_fuzz_properties.py`.

Fuzz/property suite expanded; CI rerun.

Completion-status lifecycle tests added; schema artifact version 0.4.

Semantic conformance audit: completion lifecycle and Trust subject/goal aligned; remaining conditional rules documented as LIMITED.

Trust profile 1.1 vertical slice updated.


## Runtime conformance status

Последний **подтверждённый** GitHub Actions runtime run для Reference Implementation:

- commit: a2f1dec0cbb08dc6f77302604fc7cc8b43073733
- workflow: Reference implementation tests
- Python: 3.11.16
- pytest: успешно
- результат: PASS

Этот runtime run относится к 29 сентября 2026 года. Более позднее обновление conformance evidence от 4 октября не переименовывается в runtime PASS без отдельного подтверждения самого workflow run.

Текущий статус Reference Implementation:

- L1 Structural — EXECUTED
- L2 Type/Profile — EXECUTED
- L3 Reference Integrity — EXECUTED
- L4 Semantic/Standard — EXECUTED
- L5 Integrity/History/Integration — EXECUTED

Runtime PASS не означает доказательство истинности данных и не означает полного semantic conformance всех будущих Standard rules.
