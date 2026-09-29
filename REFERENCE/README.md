# Эталонная реализация — первый вертикальный срез

## Назначение

Этот каталог содержит исполняемую эталонную реализацию архитектуры проекта «Энциклопедия цивилизации».

Это **не новый нормативный слой**. Нормативным источником остаются FOUNDATION, STANDARD и документы IMPLEMENTATION 000–016.

Текущий срез реализует пять типов:

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
