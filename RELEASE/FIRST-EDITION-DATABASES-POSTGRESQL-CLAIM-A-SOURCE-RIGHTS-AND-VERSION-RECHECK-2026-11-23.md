# Первая редакция — точечная перепроверка кандидата PostgreSQL / реляционная модель

Дата проверки: 2026-11-23  
Проверенная ветка: `mvp-public-contribution-design-2026-10-11`  
Базовый HEAD проверки: `cc11964c4b031e88a871d7006c9553eb214e87fb`; документ зафиксирован коммитом `88bd1b02d7797ecb95395c9cc8ac4c3d2ee54837`  
Статус: **SOURCE FIT CONFIRMED FOR BOUNDED CLAIM; VERSION-CURRENCY WARNING; RIGHTS PATH IDENTIFIED; NO PUBLIC APPROVAL**

## 1. Зачем выполнена проверка

Продолжена работа по уже существующему 19-главному shortlist, без запуска нового общего аудита. Проверен один из наиболее зрелых кандидатов Part II — вводное утверждение о реляционной модели PostgreSQL. Проверка ограничена точной цепочкой Claim A и его зависимостями; она не сертифицирует весь срез `databases-basics`.

## 2. Точная каноническая цепочка, повторно полученная с HEAD

| Record | Версия | Тип | Blob SHA |
|---|---:|---|---|
| `CLM-DATABASES_BASICS-A` | 3 | Claim | `[captured from repository tree at inspection HEAD]` |
| `EU-DATABASES_BASICS-A` | 3 | Evidence Use | `[captured from repository tree at inspection HEAD]` |
| `SRC-DATABASES_BASICS` | 3 | Source | `[captured from repository tree at inspection HEAD]` |
| `CTX-DATABASES_BASICS` | 3 | Context | `[captured from repository tree at inspection HEAD]` |
| `SCP-DATABASES_BASICS` | 3 | Scope | `[captured from repository tree at inspection HEAD]` |

Фактические поля повторно прочитаны из пяти JSON-файлов. Claim утверждает, что PostgreSQL является реляционной СУБД и управляет данными, хранящимися в отношениях, представленных таблицами. EU-A v3 связан именно с Claim A v3 и Source v3; locator — PostgreSQL 18.7 Tutorial, §2.2 “Concepts”. Context и Scope адресованы только Claim A v3. Scope прямо запрещает обобщать утверждение на все типы баз данных и подменять им документацию по эксплуатации, безопасности, резервному копированию и администрированию.

Blob SHA выше получены из Git tree на коммите `88bd1b02d7797ecb95395c9cc8ac4c3d2ee54837`; JSON содержимое этих записей было повторно получено с родительского HEAD `cc11964c4b031e88a871d7006c9553eb214e87fb` и не менялось новым отчётом.

## 3. Прямая проверка первичного источника

Официальная страница PostgreSQL 18, §2.2, прямо определяет PostgreSQL как relational database management system (RDBMS), объясняет relation как математический термин для table и описывает таблицу как именованную коллекцию строк с одинаковым набором именованных столбцов; каждый столбец имеет тип данных.

Вывод по source fit: текущая формулировка Claim A поддерживается указанным разделом в своей узкой границе. Claim не следует расширять до утверждения, что все базы данных реляционные, что все отношения всегда физически хранятся как простые таблицы или что одна модель описывает внутреннее устройство всех СУБД.

Проверенный locator:
- https://www.postgresql.org/docs/18/tutorial-concepts.html
- PostgreSQL 18.7 Documentation, Part I, Chapter 2, §2.2 “Concepts”.

## 4. Права и атрибуция

Официальная страница PostgreSQL License прямо распространяет разрешение на использование, копирование, изменение и распространение программного обеспечения и документации при условии сохранения copyright notice, текста разрешения и двух следующих disclaimer paragraphs во всех копиях.

Практическое следствие:
- Для текущего подхода «собственная фактическая формулировка + ссылка на первоисточник», без копирования прозы, кода, иллюстраций или таблиц PostgreSQL, не требуется включать в энциклопедию копию документации целиком.
- Если в выпуск будет включён любой скопированный фрагмент документации или её переработанная/распространяемая копия, необходимо выполнить точные условия PostgreSQL License, включая copyright notice и оба disclaimer paragraphs.
- Не использовать логотип, слоника PostgreSQL или товарные знаки как иллюстрацию/элемент брендинга без отдельной проверки trademark policy.
- Разрешение сторонней лицензии не заменяет решения владельца Энциклопедии R-01—R-10 и не устанавливает правообладателя самой Энциклопедии.

Проверенный правовой locator:
- https://www.postgresql.org/about/licence/

## 5. Существенное обнаружение: PostgreSQL 18 больше не текущая основная версия

Официальная документация на дату проверки сообщает, что PostgreSQL 19 выпущен 19 ноября 2026 года; версия 18 остаётся поддерживаемой. Следовательно, PostgreSQL 18.7 больше нельзя называть текущей/последней версией.

Это не опровергает Claim: он явно ограничен PostgreSQL 18.7, а проверенный источник относится к ветке 18. Но при подготовке reader нужно:
1. показывать версию в явном виде — «пример на PostgreSQL 18.7»;
2. не использовать формулировки «актуальная версия» или «последняя версия»;
3. не менять канонические Claim/EU/Source с v3 автоматически;
4. если редакции нужен пример на текущей версии 19, открыть отдельную авторизованную versioned remediation-задачу: перепроверить текст §2.2 в документации 19, зафиксировать новый exact locator и создать новую версию зависимых записей только в рамках разрешённого процесса.

Ссылки для проверки:
- https://www.postgresql.org/docs/18/
- https://www.postgresql.org/docs/current/

## 6. Решение по кандидату

| Gate | Результат этой проверки |
|---|---|
| Exact identity/version chain | Пять точных JSON-записей повторно прочитаны; связи Claim → EU → Source и Claim → Context/Scope подтверждены |
| Direct source support | Поддержка Claim A в §2.2 подтверждена |
| Scope/applicability | Граница Context/Scope соответствует одному Claim и не должна переноситься на другие Claims |
| Source rights | Условия PostgreSQL License найдены; конкретное соблюдение зависит от фактического способа использования материала |
| Version currency | Предупреждение: PostgreSQL 19 выпущен; 18 остаётся поддерживаемым |
| Independent Human View | Не выполнен этой проверкой |
| Project-level rights/editorial decisions R-01–R-10 | Остаются открыты |
| Public release approval | Не предоставлено |

**Диспозиция: HOLD сохраняется.** Это закрывает source-fit вопрос для Claim A на указанной версии и уточняет rights/version boundary, но не является INCLUDE и не даёт разрешения на публикацию.

## 7. Следующий конкретный шаг

Не тратить время на повторный аудит всего среза. Следующий узкий пакет:
1. сверить точные blob SHA пяти записей на HEAD, который будет выбран для кандидата;
2. выполнить reader Human View именно для Claim A с явным ярлыком «PostgreSQL 18.7»;
3. проверить, что Context/Scope визуально прикреплены только к Claim A;
4. проверить, что Reader показывает официальный locator и не создаёт впечатления, будто Claim описывает все СУБД;
5. сохранить кандидата HOLD до закрытия owner-level rights/editorial decisions и явного release approval.

## Источники

- PostgreSQL 18.7, §2.2 Concepts: https://www.postgresql.org/docs/18/tutorial-concepts.html
- PostgreSQL License: https://www.postgresql.org/about/licence/
- PostgreSQL 18 documentation/version support: https://www.postgresql.org/docs/18/
- PostgreSQL documentation landing page and release information: https://www.postgresql.org/docs/current/

