# 013 — Восстановление и воспроизводимость

## Энциклопедия цивилизации

Версия: 0.1  
Класс: Implementation Specification  
Статус: рабочая нормативная спецификация  
Дата: 29 сентября 2026 года

---

## 1. Назначение

Документ замыкает требования к долговременному восстановлению проекта.

Recovery должен позволять получить проверяемую рабочую систему из Portable Package без исходного сервера, если пакет заявлен как self-contained.

## 2. Recovery target

Восстановление должно определять:

- какие Record восстановлены;
- какие версии доступны;
- какие Schema/Profile применены;
- какие Standards применимы;
- какая версия Validator использована;
- какие ссылки разрешены;
- какие зависимости отсутствуют;
- какой результат Validation получен.

## 3. Clean environment

Тест восстановления должен проводиться в среде, не содержащей скрытых зависимостей исходной системы.

Не допускается считать доступ к:

- исходной БД;
- исходному серверу;
- локальному cache;
- внешнему URL;
- незафиксированной версии инструмента

частью self-contained recovery.

## 4. Recovery phases

    1. acquire package
    2. verify manifest
    3. verify integrity
    4. load schemas/profiles/standards
    5. acquire validator
    6. load records
    7. resolve references
    8. validate
    9. reconstruct storage
    10. build publication
    11. produce recovery report

Каждый этап должен иметь проверяемый результат.

## 5. Reproducibility

Повторное восстановление одного и того же пакета с одинаковыми версиями инструментов должно давать эквивалентный результат.

Эквивалентность должна быть определена отдельно для:

- Record;
- reference graph;
- ValidationResult;
- publication;
- integrity metadata.

## 6. Environment manifest

Для воспроизводимости следует фиксировать:

- ОС или минимальные требования;
- версии инструментов;
- Schema versions;
- Profile versions;
- Standard versions;
- Validator version;
- Migration versions;
- Builder version;
- локальные зависимости.

## 7. Network independence

Self-contained recovery не должен требовать сети.

Если внешняя зависимость необходима, package completeness должен отражать это.

## 8. Failure recovery

При прерывании восстановления:

- исходный пакет не изменяется;
- частичный результат явно маркируется;
- повторный запуск определён;
- ошибки не маскируются;
- повреждённые компоненты не выдаются за восстановленные.

## 9. Recovery report

Минимум:

- package identity/version;
- environment identity;
- integrity result;
- Record counts;
- version counts;
- reference results;
- validation result;
- publication result;
- missing dependencies;
- warnings/errors;
- reproducibility result.

## 10. Golden recovery

Должен существовать эталонный Portable Package, для которого ожидаемые результаты заранее зафиксированы.

Golden recovery используется как регрессионный тест.

## 11. Disaster scenarios

Необходимо проверять:

- потерю Backend;
- потерю индексов;
- повреждение части пакета;
- отсутствие сети;
- отсутствие одной зависимости;
- несовместимую версию инструмента;
- прерванное восстановление;
- повторное восстановление;
- частичный пакет.

## 12. Security

Recovery не должен:

- выполнять код из пакета;
- доверять путям;
- раскрывать секреты;
- автоматически подключаться к внешним системам;
- выполнять произвольные scripts.

## 13. Tests

- R01 — recovery без исходного Backend;
- R02 — recovery без сети;
- R03 — integrity failure обнаруживается;
- R04 — отсутствующая зависимость обнаруживается;
- R05 — исторические версии восстанавливаются;
- R06 — ссылки сохраняются;
- R07 — ValidationResult воспроизводим;
- R08 — повторный recovery эквивалентен;
- R09 — прерванный recovery безопасен;
- R10 — golden package проходит ожидаемый recovery.

Стресс-тесты R11–R20:

- большой архив;
- большое число Record;
- большая история;
- большой reference graph;
- много фрагментов;
- много языков;
- Unicode;
- частично повреждённый пакет;
- ограниченная память;
- медленное хранилище.

## 14. Инварианты

1. Self-contained recovery не требует исходного сервера.
2. Пакет не изменяется во время recovery.
3. Повреждение не маскируется под успех.
4. История сохраняется.
5. Unknown сохраняется.
6. Повторный recovery воспроизводим.
7. Golden package имеет фиксированный ожидаемый результат.
8. Recovery не исполняет данные как код.

## 15. Критерии готовности

013 готов, если определены clean environment, phases, environment manifest, reproducibility, failure recovery, golden recovery, disaster scenarios, security и tests.

## 16. Статус

Документ уточняет и операционализирует recovery requirements из 009, не заменяя их.
