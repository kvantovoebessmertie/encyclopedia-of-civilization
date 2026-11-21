# M13 — независимая проверка семи групп повторных оценок

Дата проверки: 2026-11-18

Ветка: `m13-system-wide-depth-audit-2026-10-09`

Проверенный HEAD: `e6b6741cebbded03259f81dfd969ef43c14a9a0c`
Объём: 7 групп, 14 исторических строк Batch 12/17/21/27. Это проверка происхождения и сопоставимости оценок, а не новая D/E/B-оценка и не решение споров.

Обозначения ссылок в таблице: `B12` = `RELEASE/M13-CLAIM-REVIEW-BATCH-12-NUCLEAR-PHYSICS-2026-10-09.md`; `B17` = `RELEASE/M13-CLAIM-REVIEW-BATCH-17-NUCLEAR-AND-WATER-2026-10-10.md`; `B21` = `RELEASE/M13-CLAIM-REVIEW-BATCH-21-WATER-BURNS-ELECTRICAL-2026-10-10.md`; `B27` = `RELEASE/M13-CLAIM-REVIEW-BATCH-27-WATER-TREATMENT-2026-10-10.md`. Префиксы `N/` и `W/` обозначают соответственно `CONTENT/vertical-slices/nuclear-physics-information-basics/records/` и `CONTENT/vertical-slices/water-treatment-basics/records/`.

## Результат

По строкам исходных отчётов шесть Claims имеют разные исторические баллы, один Claim повторяет те же D/E/B. Ни одна из шести конфликтных оценок не выбрана победившей. Совпадающая строка по emergency-disinfection классифицирована как повтор оценки, а не независимое подтверждение.

Для всех семи групп текущие канонические записи имеют `record_version: "1"`. Однако исходные batch-отчёты не фиксируют версию Claim/Evidence Use/Source на дату каждой оценки, а доступная Git-история — shallow, содержит только текущий commit и не имеет доступного родителя. Поэтому нельзя подтвердить неизменность записей с дат оценок или доказать тождество исторических версий. Имена авторов/рецензентов в первичных отчётах не указаны; дата отчёта известна, но не заменяет идентичность рецензента.

## Таблица семи групп

| Claim | Исходные оценки и строки | Сверка цепочки по первичным отчётам и текущим записям | Вывод |
|---|---|---|---|
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_A` | Batch 12, 2026-10-09, D1/E1/B2 (`B12:15,18,22`); Batch 17, 2026-10-10, D2/E1/B2 (`B17:18`). | Batch 12 явно указывает EU и источник IAEA; Batch 17 сообщает о generic EU и том же широком IAEA overview, но не называет EU ID/version. Текущие Claim, EU и Source — v1 (`N/CLM-NUCLEAR_PHYSICS_INFORMATION_BASICS-A.json:1`, `N/EU-NUCLEAR_PHYSICS_INFORMATION_BASICS-A.json:1`, `N/SRC-NUCLEAR_PHYSICS_INFORMATION_BASICS.json:1`). | **Конфликт D.** Обе строки: E1/B2; Batch 12 называет утверждение определением-ярлыком без различий между структурой, реакциями и распадом; Batch 17 также считает механизм недостаточным. Тождество версии и EU-версии не доказано. |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_B` | Batch 12: D2/E1/B3 (`B12:26,29,33`); Batch 17: D2/E1/B2 (`B17:19`). | Batch 12 явно указывает EU-B → IAEA; Batch 17 описывает generic EU и IAEA, но без точных EU ID/version. Текущие Claim, EU-B и IAEA Source — v1 (`N/CLM-NUCLEAR_PHYSICS_INFORMATION_BASICS-B.json:1`, `N/EU-NUCLEAR_PHYSICS_INFORMATION_BASICS-B.json:1`, `N/SRC-NUCLEAR_PHYSICS_INFORMATION_BASICS.json:1`). | **Конфликт B.** В обоих отчётах D2/E1; Batch 12 считает оговорки «могут» и зависимость от ядра/перехода достаточными сильными границами, Batch 17 сохраняет тезис, но считает нужным конкретизировать поддержку и различия. |
| `CLM_NUCLEAR_PHYSICS_INFORMATION_BASICS_C` | Batch 12: D1/E1/B3 (`B12:37,40,42`); Batch 17: D2/E1/B2 (`B17:20`). | Batch 12 указывает EU-C → широкий IAEA source; Batch 17 говорит, что тот же широкий источник не обосновывает методологическое положение, но точные EU ID/version не указывает. Текущие Claim, EU-C и IAEA Source — v1 (`N/CLM-NUCLEAR_PHYSICS_INFORMATION_BASICS-C.json:1`, `N/EU-NUCLEAR_PHYSICS_INFORMATION_BASICS-C.json:1`, `N/SRC-NUCLEAR_PHYSICS_INFORMATION_BASICS.json:1`). | **Конфликт D и B.** Batch 12: корректная, но абстрактная методологическая граница без примера; Batch 17: полезное различение механизма, величины и условий, но неподтверждённое и с неопределённым предметным типом. |
| `CLM-M5-WATER-EMERGENCY-DISINFECTION-D` | Batch 21: D3/E3/B3 (`B21:13`); Batch 27: D3/E3/B3 (`B27:16`). | Оба отчёта прямо связывают оценку с EPA emergency-disinfection и границей между микробным обеззараживанием и удалением химических/прочих загрязнителей. Batch 27 также указывает EU; текущие Claim/EU/Source v1 (`W/CLM-M5-WATER-EMERGENCY-DISINFECTION-D.json:1`, `W/EU-M5-WATER-EMERGENCY-DISINFECTION-D.json:2,7,19-25`, `W/SRC-EPA-WATER-TREATMENT-2026.json:1`). | **Одинаковая повторная оценка по опубликованным строкам** (все баллы совпадают). Это не независимая вторая оценка; историческое равенство версий не доказано. |
| `CLM-WATER_TREATMENT_BASICS-A` | Batch 21: D2/E2/B3 (`B21:14`); Batch 27: D2/E3/B3 (`B27:13`). | Batch 21 описывает EPA technology material и foundational source, без EU ID; Batch 27 прямо называет WHO и EPA technology overview. Текущие Claim/EU-WHO-A/EU-EPA-tech-A и Sources v1 (`W/CLM-WATER_TREATMENT_BASICS-A.json:1`, `W/EU-WATER_TREATMENT_BASICS-A.json:2,7,19-25`, `W/EU-M5-EPA-DRINKING-WATER-A.json:2,7,19-25`, `W/SRC-WATER_TREATMENT_BASICS.json:1`, `W/SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES.json:2,7,15-17`). | **Конфликт E.** Batch 21 связывает цель обработки с назначением и допустимыми уровнями загрязнителей; Batch 27 считает WHO/EPA совместно достаточными. Поскольку Batch 21 не перечисляет точные EU/Source IDs, равенство цепочки не установлено. |
| `CLM-WATER_TREATMENT_BASICS-B` | Batch 21: D2/E3/B3 (`B21:15`); Batch 27: D3/E3/B3 (`B27:14`). | Batch 21 указывает EPA treatment guidance и foundational source, без точных EU IDs; Batch 27 описывает WHO/EPA и различие их ролей. В текущем срезе Claim v1 связан с WHO-EU-B, EPA emergency EU-B и EPA technology EU-B; связанные Source records — WHO, EPA emergency, EPA technology, все v1 (`W/CLM-WATER_TREATMENT_BASICS-B.json:1`, `W/EU-WATER_TREATMENT_BASICS-B.json:2,7,19-25`, `W/EU-EPA-WATER-TREATMENT-B.json:1`, `W/EU-M5-EPA-DRINKING-WATER-B.json:2,7,19-25`, `W/SRC-WATER_TREATMENT_BASICS.json:1`, `W/SRC-EPA-WATER-TREATMENT-2026.json:1`, `W/SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES.json:2,7,15-17`). | **Конфликт D.** Обе строки E3/B3. Batch 21 считает зависимость от исходной воды, целей и результата достаточной для D2; Batch 27 присваивает D3, ссылаясь на эти зависимости и технологические условия. Перечни исторических EU/Source IDs отсутствуют. |
| `CLM-WATER_TREATMENT_BASICS-C` | Batch 21: D2/E2/B3 (`B21:16`); Batch 27: D2/E3/B3 (`B27:15`). | Batch 21 не перечисляет точные EU IDs; Batch 27 сообщает о WHO и EPA. Текущие Claim/EU-WHO-C/EU-EPA-tech-C и Sources v1 (`W/CLM-WATER_TREATMENT_BASICS-C.json:1`, `W/EU-WATER_TREATMENT_BASICS-C.json:2,7,19-25`, `W/EU-M5-EPA-DRINKING-WATER-C.json:2,7,19-25`, `W/SRC-WATER_TREATMENT_BASICS.json:1`, `W/SRC-M5-EPA-DRINKING-WATER-TECHNOLOGIES.json:2,7,15-17`). | **Конфликт E.** Обе строки D2/B3. Batch 21 указывает на общий принцип и нехватку точных подтверждений; Batch 27 ссылается на поддержку ограничений технологий и некорректность универсального метода. Точное совпадение исторического набора EU/Source не проверяемо по строкам Batch 21. |

Первичные документы фиксируют дату и баллы, но не называют индивидуального reviewer: `B12:2`, `B17:2`, `B21:2`, `B27:2`. Указание Git автора как рецензента было бы необоснованным.

## Что требуется для независимой адъюдикации шести конфликтов

Ниже — минимальные сведения, необходимые до выбора или выставления нового балла. Это не выбор победившей строки.

| Claim | Конфликт | Требуемые факты для решения |
|---|---|---|
| Nuclear A | D1/D2 | Зафиксировать точный текст и версию Claim на каждую дату; применить D-рубрику к уровню объяснения, а не к институциональному авторитету источника; определить, входит ли «взаимодействия» в заявленную introductory-область и подтверждена ли эта часть конкретным passage. |
| Nuclear B | B3/B2 | Проверить точную редакцию Claim и точный поддерживающий passage для «могут», ядра и перехода; обосновать по B-рубрике, какие существенные границы/условия остаются неявными. Нужно решить, насколько оговорка «могут» действительно предотвращает ошибочное обобщение. |
| Nuclear C | D1/B3 против D2/B2 | Сначала определить, является ли это Claim по ядерной физике или общенаучным методологическим правилом. Текущий IAEA landing page не задаёт точной поддержки этого тезиса; до разрешения области/типа и подходящего источника D/B-сопоставление преждевременно. |
| Water A | E2/E3 | Получить точные EU/Source версии, claim-specific locator и процитированные passages, существовавшие при каждой оценке; проверить, относятся ли они к снижению загрязнителей до целевого назначения, а не лишь к общей программе/набору технологий. Отдельно оценить, даёт ли независимое подтверждение основание для E3. |
| Water B | D2/D3 | Зафиксировать версии Claim и рубрики; оценивать объяснительную глубину самого утверждения, а не широту источников. Независимый reviewer должен показать, какие механизм/условия объяснены в тексте Claim и почему они достигают либо не достигают порога D3. |
| Water C | E2/E3 | Установить точные EU/Source версии и воспроизводимые passages для ограничения универсальности, включая охват разных загрязнителей/технологий; отделить поддержку общей границы от emergency-disinfection контекста и проверить, не требует ли E3 дополнительного независимого подтверждения. |

Для всех шести нужны reviewer/role и дата, версии Claim/EU/Source, полный список Evidence Use, точные локаторы и просмотренный текст passages, версия рубрики и rationale по каждому различающемуся D/E/B. Пока этого нет, обе исторические строки сохраняются; ни одна не считается разрешённой.

## Проверка текущих записей и ограничение истории

- Текущий snapshot содержит все семь Claims, перечисленные выше, с `record_version: "1"`, и текущие ссылки EU на версии 1 Source. Текущие записи читаются в `CONTENT/vertical-slices/nuclear-physics-information-basics/records/` и `CONTENT/vertical-slices/water-treatment-basics/records/`; точные релевантные пути и строки приведены в таблице.
- В первичных отчётах Batch 12/17/21/27 нет поля с версиями канонических Claim/EU/Source или сведений об изменениях записи после оценки. У Batch 12 для Nuclear приведены link names; Batch 17 приводит общий EU-текст без полного списка EU IDs; Batch 21 не перечисляет EU IDs; Batch 27 указывает, что проверял WHO/EPA links и перечисляет записи (`RELEASE/M13-CLAIM-REVIEW-BATCH-27-WATER-TREATMENT-2026-10-10.md:5-7,25-36`).
- Git сообщает `true` для `--is-shallow-repository`, `1` для `git rev-list --count HEAD`; `HEAD^` недоступен. Поэтому сравнение дерева на 2026-10-09/10 с нынешним состоянием невозможно в этой копии. Корректный вывод — **изменение канонических версий после оценок не установлено**, а не «записи точно не менялись».
- Текущая проверка не переоценивает источники извне и не пересчитывает баллы. Исторические E2/E3 также не переносились на текущий скоринг автоматически; протокол требует E=1 до воспроизводимых claim-specific locator (`RELEASE/M13-SYSTEM-WIDE-DEPTH-AUDIT-PROTOCOL-2026-10-09.md`, раздел B, критерий E).

## Отделение от 14 неназванных наблюдений 14 ноября

Это разные provenance-наборы, и в этом отчёте они не объединяются:

- Семь дублирующихся scored-report групп — 14 строк с точными Claim ID и D/E/B из Batch 12/17/21/27; они перечислены в reconciliation 12 ноября (`RELEASE/M13-SCORED-REPORT-DUPLICATE-AND-CLAIM-ID-RECONCILIATION-2026-11-12.md`, раздел 2).
- «14 observations» относятся к preliminary content-level risk screen в очереди из 711 Claims; в его первичном перечне отсутствуют ID 14 наблюдений. Reconciliation прямо оставляет их `UNRESOLVED — historical identity not recoverable` и исключает из ID-verified/D/E/B подсчётов (`RELEASE/M13-UNASSESSED-RISK-SCREEN-COVERAGE-RECONCILIATION-2026-11-14.md:9-10,21,36,46-48`).
- Поэтому нет оснований отождествлять 14 неизвестных с 14 историческими scored rows либо включать их в эти семь групп. Но поскольку ID неизвестны, **невозможно доказать и отсутствие пересечения на уровне Claims**. Для этого потребовалась бы новая первичная запись с ID; арифметика или предположение по темам не подходят.

## Граница результата

Подтверждены только значения и rationale, записанные в исходных batch-отчётах, и состояние текущих канонических JSON на HEAD. Шесть конфликтов не адъюдицированы; точное равенство исторических версий/цепочек и отсутствие последующих канонических изменений не подтверждены из-за пробелов в первичных отчётах и shallow Git. Канонические записи, оценки, workflow, ветка, `main` и PR #21 не изменялись; создан только этот отчёт.
