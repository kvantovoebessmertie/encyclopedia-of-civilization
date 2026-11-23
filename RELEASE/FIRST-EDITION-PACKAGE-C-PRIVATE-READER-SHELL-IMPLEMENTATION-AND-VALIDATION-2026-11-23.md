# Первая редакция — Package C: работающая offline reader shell и проверки интерфейса

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: реализованный внутренний navigation prototype; не production reader и не public release.

## 1. Что создано

Добавлен автономный статический интерфейс:

- `REFERENCE/first_edition_shell/index.html`
- `REFERENCE/first_edition_shell/reader.css`
- `REFERENCE/first_edition_shell/reader.js`
- `REFERENCE/first_edition_shell/README.md`
- `REFERENCE/tests/test_first_edition_shell.py`

Он содержит:
- две части и 19 глав первой редакции;
- редакционную структуру подтем для каждой главы;
- навигацию по главам;
- поиск по названию главы и её подтемам;
- адаптивную раскладку для узкого экрана;
- поддержку клавиатурного фокуса и prefers-reduced-motion;
- локальные CSS/JS без внешних зависимостей;
- Content Security Policy, запрещающую внешние подключения и inline script;
- явный статус «материалы готовятся» для каждой из 19 глав.

## 2. Принцип честного пустого состояния

Сейчас в corpus нет ни одного production INCLUDE manifest. Поэтому интерфейс не показывает canonical Claims как публичные статьи, не читает весь корпус, не строит случайный граф и не делает вид, что HOLD означает проверенное знание.

В каждой главе явно написано, что публикационно допущенных статей пока нет. Это сделано намеренно: рабочая программа должна показывать реальные доступные материалы, а не маскировать отсутствие допуска автоматически сгенерированным текстом.

Статическая навигация — это первый работающий слой программы, но не сама первая редакция Энциклопедии по содержанию.

## 3. Безопасность и автономность

- Нет внешних скриптов, шрифтов, аналитики, API и сетевых запросов.
- Нет динамического HTML injection; поиск обновляет только textContent/hidden.
- Встроенный CSP: default-src none; разрешены только локальные CSS/JS и локальные/data images.
- Никакой загрузки записей из CONTENT в reader shell.
- Никаких форм приёма пользовательских данных.
- Никакого автоматического допуска или преобразования HOLD → INCLUDE.
- Состояние интерфейса не интерпретируется как publication status.

## 4. Тесты

Добавлен pytest suite, который проверяет:
1. ровно 19 chapter sections в ожидаемом порядке и обе части;
2. отсутствие внешних CSS/JS ресурсов и inline scripts;
3. disclosure о неподготовленном/неодобренном содержимом во всех 19 главах;
4. наличие безопасного поиска и числовой классификации глав по частям;
5. responsive breakpoints и reduced-motion support.

Тесты добавлены в существующий REFERENCE test suite, который запускается на PR при изменении REFERENCE. До завершения GitHub Actions на текущем immutable HEAD статус остаётся «не подтверждён CI». Не объявлять тесты PASS по факту наличия тестового файла.

## 5. Как открыть

Скачать/клонировать PR branch и открыть локально:

```text
REFERENCE/first_edition_shell/index.html
```

Сборка не требует установки зависимостей и не обращается к сети. Она предназначена для внутренней оценки структуры, навигации и пустого состояния.

## 6. Что ещё нужно для настоящего production reader

1. Freeze approved schema-1.1 exact-version selection manifest.
2. Подключить только selected exact-version records, а не весь corpus.
3. Валидировать полную dependency closure и record profile pins.
4. Рендерить Claim, Evidence Use, Source, Context, Scope и approved Relations с явной областью действия.
5. Показать источники и pinpoint locators, ограничения, дату/версию и attribution.
6. Скрывать HOLD/EXCLUDE, private preview и внутренние аудиты.
7. Добавить редакторские статусы, accessible navigation, cross-reference and offline search только по включённым записям.
8. Добавить права/лицензии на уровне конкретных материалов и исключить неразрешённые assets.
9. Собрать воспроизводимый offline artifact и провести независимую проверку на разных устройствах.
10. Подписать exact artifact hash и получить release approver decision.

## 7. Release boundary

Этот package закрывает только первый UI/navigation prototype. Он не заменяет существующий selection-aware offline builder и не создаёт released state. Его нельзя публиковать, развёртывать или выдавать за завершённую первую редакцию.

PR #22 остаётся Draft. Никакие canonical records, publication decisions, rights decisions, allowlist, main branch, merge или deployment не изменены.
