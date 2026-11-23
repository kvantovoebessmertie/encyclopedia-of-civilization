# Motion Basics — пакет терминологического решения и исправления доказательств

Дата: 2026-11-23  
Ветка: `mvp-public-contribution-design-2026-10-11`  
Проверенный исходный HEAD: `e006904a55ec1c4ee33d923e65d782892ab8d813`  
Статус: **EDITORIAL DECISION REQUIRED; VERSIONED EU REMEDIATION PROPOSED; NO CANONICAL WRITE; ALL RECORDS HOLD**

## 1. Результат повторного чтения полного среза

Повторно получены все 9 канонических JSON-записей с указанного HEAD:

- `CLM-MOTION_BASICS-A@1`
- `CLM-MOTION_BASICS-B@1`
- `CLM-MOTION_BASICS-C@1`
- `EU-MOTION_BASICS-A@1`
- `EU-MOTION_BASICS-B@1`
- `EU-MOTION_BASICS-C@1`
- `SRC-MOTION_BASICS@1`
- `CTX-MOTION_BASICS@1`
- `SCP-MOTION_BASICS@1`

У всех трёх Evidence Use есть корректные claim_ref и source_ref, но отсутствуют конкретные section locators. Context и Scope адресованы только Claim A. Их нельзя автоматически отображать как ограничения для Claims B и C.

## 2. Проверка Claim B — обнаружено существенное терминологическое расхождение

Текущий Claim B v1:

> «Средняя скорость определяется отношением изменения положения к соответствующему интервалу времени.»

Эта формулировка смешивает два разных физических понятия:

- average speed — пройденное расстояние / время; скалярная величина;
- average velocity — перемещение / интервал времени; векторная величина.

В официальном OpenStax Physics §2.2 эти определения разделены. В Key Equations также отдельно приведены обе формулы. Текущая фраза «изменение положения» соответствует перемещению, следовательно, описывает среднюю векторную скорость (average velocity), а не среднюю путевую скорость (average speed).

**Предлагаемое редакционное решение (не внесено в канонический Claim):**

Вариант B1 — сохранить смысл исходной формулы и уточнить термин:
«Средняя векторная скорость определяется отношением перемещения тела к интервалу времени, за который это перемещение произошло».

Вариант B2 — если автор хотел определить среднюю путевую скорость, изменить формулировку:
«Средняя путевая скорость определяется отношением длины пройденного пути к интервалу времени движения».

Эти варианты не взаимозаменяемы. Выбор должен быть сделан редактором по замыслу Claim, а не автоматически по источнику. До решения Claim B остаётся HOLD и не должен выводиться как проверенная формулировка.

Прямые источники:
- OpenStax Physics, §2.2 “Speed and Velocity”: https://openstax.org/books/physics/pages/2-2-speed-and-velocity
- OpenStax Physics, Chapter 2 Key Equations: https://openstax.org/books/physics/pages/2-key-equations
- OpenStax Physics, Chapter 2 Section Summary: https://openstax.org/books/physics/pages/2-section-summary

## 3. Claim A — locator и граница поддержки

Claim A v1: «Положение объекта задаётся относительно выбранной системы отсчёта».

OpenStax Physics §2.1 “Relative Motion, Distance, and Displacement” прямо указывает, что описание движения зависит от системы отсчёта, из которой оно описывается.

Предлагаемый versioned Evidence Use locator для EU-A:
- OpenStax Physics, §2.1 “Relative Motion, Distance, and Displacement”;
- pinpoint: абзац, определяющий зависимость описания движения от reference frame;
- прямой URL: https://openstax.org/books/physics/pages/2-1-relative-motion-distance-and-displacement

Поддержка Claim A прямая. Context/Scope v1 остаются только для Claim A. Нельзя переносить их на Claims B/C без отдельных target-specific записей.

## 4. Claim C — уточнение понятия ускорения

Текущий Claim C v1:
«Ускорение описывает изменение скорости во времени».

Формулировка в целом согласуется с источником, но для точности нужно не допустить бытового прочтения «ускорение — только увеличение быстроты». Вектор скорости может изменяться как по величине, так и по направлению.

OpenStax Physics §2.4 “Acceleration” указывает, что изменение скорости-вектора может быть изменением величины, направления или обоих параметров; автомобиль, поворачивающий при постоянной быстроте, всё равно имеет ускорение.

Предлагаемая более точная версия Claim (только предложение для редакторского решения):
«Ускорение характеризует изменение вектора скорости за единицу времени».

Если проект сохраняет текущую общую формулировку, EU-C должен явно указывать, что velocity является вектором и что изменение направления также означает изменение скорости-вектора. Нельзя приравнивать ускорение только к увеличению модуля скорости.

Прямой locator:
- OpenStax Physics, §2.4 “Acceleration”;
- подразделы “Average Acceleration” и “Acceleration as a Vector”;
- https://openstax.org/books/physics/pages/2-4-acceleration

## 5. Предлагаемая карта Evidence Use v2 (не каноническая запись)

| Запись | Предлагаемый pinpoint | Что именно поддерживается |
|---|---|---|
| EU-MOTION_BASICS-A@2 | OpenStax Physics §2.1, “Relative Motion, Distance, and Displacement” | Описание движения зависит от выбранной системы отсчёта |
| EU-MOTION_BASICS-B@2 | OpenStax Physics §2.2, “Speed and Velocity” | Только после редакторского выбора: либо average speed = distance/time, либо average velocity = displacement/time |
| EU-MOTION_BASICS-C@2 | OpenStax Physics §2.4, “Acceleration”; “Average Acceleration”; “Acceleration as a Vector” | Ускорение — скорость изменения вектора скорости; изменение направления тоже учитывается |

Source v1 уже указывает на официальный учебник OpenStax Physics и на главу 2. В этом пакете Source JSON не меняется. Перед любой canonical remediation необходимо проверить, что его URI и identity соответствуют указанному изданию и что ссылки на section pages ведут к той же книге.

## 6. Права и ограничения использования источника

Проверка страницы OpenStax Physics показывает лицензию Creative Commons Attribution 4.0 International (CC BY 4.0) для этого конкретного учебника. Это отличается от лицензии OpenStax Biology 2e и некоторых других учебников OpenStax; лицензии нельзя переносить между названиями.

Практические последствия:
- собственная краткая формулировка факта с точной ссылкой не должна превращаться в копирование учебного текста;
- при перераспространении или адаптации материалов учебника необходимо выполнять CC BY 4.0 и точные attribution requirements из preface;
- не копировать изображения/графики автоматически: отдельные иллюстрации могут иметь индивидуальные credits/rights;
- Source v1 должен оставаться связанным именно с учебником Physics, а не с College Physics 2e или Physics for AP Courses;
- проектные решения R-01–R-10 остаются отдельным обязательным release gate.

Источник по лицензии:
- OpenStax Physics, Preface: https://openstax.org/books/physics/pages/preface
- OpenStax Physics subject listing: https://openstax.org/subjects/physics

## 7. Что закрыто и что нет

| Проверка | Результат |
|---|---|
| Все 9 canonical JSON повторно прочитаны | Да |
| Claim A direct support | Подтверждена §2.1 |
| Claim B terminology | Существенное расхождение обнаружено; требуется выбор B1/B2 |
| Claim C conceptual support | Подтверждена §2.4; рекомендуется уточнение векторного смысла |
| Точные section locators | Найдены для всех трёх |
| Source rights | CC BY 4.0 для конкретного OpenStax Physics; требуется точная атрибуция при повторном использовании |
| Context/Scope applicability | Оба target только Claim A |
| Canonical JSON изменён | Нет |
| INCLUDE назначен | Нет |
| Независимый Human View | Не выполнен |
| Project rights/editorial owner decisions | R-01–R-10 открыты |

## 8. Следующий безопасный шаг

1. Принять отдельное редакторское решение по Claim B: B1 (средняя векторная скорость) или B2 (средняя путевая скорость).
2. Подтвердить, сохраняется ли Claim C в текущем виде или требуется версия с явным «вектора скорости».
3. После этого запросить ограниченную авторизацию на создание EU v2 и, если требуется, Claim v2. До авторизации canonical JSON не менять.
4. Проверить точные record type/schema/version и dependency closure после разрешённой записи.
5. Выполнить reader Human View; отдельно проверить, что Context/Scope показываются только рядом с Claim A.
6. Оставить все записи HOLD до завершения rights/editorial gates и явного release approval.

## 9. Change-control

Этот пакет является исследовательским и редакционным предложением. Он не меняет canonical Claims, Evidence Use, Source, Context, Scope, Relations, assessments, inferences, decisions, candidate dispositions, denominator, manifest или allowlist. Он не разрешает публикацию и не заменяет owner authorization.

