# Первая редакция — Package B: исправление научных Claim и границы доказательств/прав

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: предметная remediation-карта; не canonical edit и не допуск к публикации.

## 1. Результат

Проведена дополнительная точечная проверка пяти фундаментальных направлений: движение, растворы, клеточная биология, ранние цивилизации и статистика/измерительная неопределённость. Пакет не запускает повторный широкий аудит и не переписывает canonical Claims. Он фиксирует, какие exact-version кандидаты можно двигать дальше, а какие должны оставаться HOLD из-за содержательной ошибки, слабого локатора или несовместимых прав.

## 2. Движение — терминологическая ошибка в Claim B

Проверенные записи:
- `CLM-MOTION_BASICS-A@1`, `CLM-MOTION_BASICS-B@1`, `CLM-MOTION_BASICS-C@1`
- `EU-MOTION_BASICS-A@1`, `EU-MOTION_BASICS-B@1`, `EU-MOTION_BASICS-C@1`
- `SRC-MOTION_BASICS@1`, `CTX-MOTION_BASICS@1`, `SCP-MOTION_BASICS@1`

### Claim A — положение и система отсчёта
OpenStax Physics §2.1 “Position, Displacement, and Average Velocity” — предметный раздел для position/reference frame. Текущий EU A generic; нужен конкретный section locator. Claim A можно оставить в ограниченном кандидате после точного locator и rights review.

### Claim B — смешение средней скорости и средней векторной скорости
Существующая формулировка использует «средняя скорость» для отношения перемещения к интервалу времени. Это терминологически неоднозначно: отношение displacement/time соответствует average velocity (векторная величина), тогда как average speed использует distance/time (скалярная величина).

Варианты для отдельного редакционного решения:
1. **Если Claim о средней векторной скорости:** «Средняя векторная скорость равна отношению перемещения к интервалу времени».
2. **Если Claim о средней путевой скорости:** «Средняя путевая скорость равна отношению пройденного пути к затраченному времени».

Не выбирать вариант автоматически: они выражают разные понятия. Для исправления потребуется новая версия Claim, новая версия EU с точным §2.2 locator, обновлённые ссылки зависимостей и предусмотренная оценка. Исторические оценки исходной формулировки не переносятся автоматически.

### Claim C — ускорение
OpenStax Physics §2.4 “Acceleration” объясняет ускорение как скорость изменения вектора velocity; оно возникает при изменении величины скорости, направления или обоих параметров. Текущий Claim следует читать именно как изменение velocity vector, а не только изменение численного значения speed. EU нужен точный locator и явная формулировка границы.

### Rights
OpenStax Physics — отдельная лицензия CC BY 4.0, но это не разрешает автоматически использовать другие книги OpenStax на тех же условиях. Перед выпуском проверить конкретный титульный блок/лицензию и отдельно credits для фигур, фото, видео и сторонних компонентов. Текстовый paraphrase с атрибуцией предпочтительнее копирования материалов.

**Disposition:** A — HOLD pending locator; B — HOLD pending editorial choice and new version; C — HOLD pending vector clarification and locator.

## 3. Растворы — доказательная связь существует, но canonical EU locator needs verification

Проверенные записи:
- `CLM-MIXTURES_AND_SOLUTIONS-A@1`
- `EU-MIXTURES_AND_SOLUTIONS-A@2`
- `SRC-MIXTURES_AND_SOLUTIONS@1`
- `CTX-MIXTURES_AND_SOLUTIONS@1`
- `SCP-MIXTURES_AND_SOLUTIONS@1`

Claim: «Раствор является однородной смесью двух или более веществ».

OpenStax Chemistry 2e §11.1 “The Dissolution Process” прямо описывает растворы как homogeneous mixtures и поясняет равномерность состава по всему объёму. Страница также указывает, что раствор может быть газообразным, жидким или твёрдым, поэтому Claim не должен быть ограничен водными растворами. <https://openstax.org/books/chemistry-2e/pages/11-1-the-dissolution-process>

Существующий EU v2 имеет в description общую фразу о добавлении locator, но видимое описание не называет §11.1 и не содержит воспроизводимого pinpoint. Нужно перепроверить полный payload/locator field, не считать короткую summary-фразу достаточной.

**Предложение для EU description (не canonical edit):**

> OpenStax Chemistry 2e, §11.1 “The Dissolution Process,” defines solutions as homogeneous mixtures and explains that their composition is uniform throughout. The section gives examples of gaseous, liquid and solid solutions. This supports the bounded Claim that a solution is a homogeneous mixture of two or more substances. Do not infer that every mixture forms a solution or that every solution is aqueous.

Context/Scope относятся только к Claim A@1. Scope — базовый образовательный срез, не лабораторная инструкция. Не добавлять процедуры смешивания химикатов, концентрации, токсикологию или рекомендации по обращению с реагентами.

**Rights:** проверять именно Chemistry 2e license page и отдельные asset credits; нельзя выводить лицензию Chemistry из Biology или Physics. Пока не внесён item-level rights evidence, HOLD.

## 4. Клеточная биология — источник поддерживает Claim, но лицензия является blocker

Проверенные записи:
- `CLM-CELL_BASICS-A@1`
- `EU-CELL_BASICS-A@1`
- `SRC-CELL_BASICS@1`
- `CTX-CELL_BASICS@1`
- `SCP-CELL_BASICS@1`

Claim: клетка является основной структурной и функциональной единицей живых организмов.

OpenStax Biology 2e §4.1 “Studying Cells” прямо описывает клетку как smallest unit of a living thing и basic building block of organisms; раздел также содержит unified cell theory. <https://openstax.org/books/biology-2e/pages/4-1-studying-cells>

EU A generic; section locator должен быть добавлен versioned remediation. Контекст/Scope таргетируют только Claim A; нельзя распространять их на Claims B/C без отдельной проверки.

### Rights blocker
Для Biology 2e ранее установлен режим CC BY-NC-SA 4.0 и дополнительное ограничение, связанное с использованием/ingestion материалов в LLM/generative AI без разрешения. Это не эквивалентно обычной CC BY. Нельзя предполагать, что:
- некоммерческая публикация автоматически разрешена в любом проектном режиме;
- генерация paraphrase снимает условия источника;
- лицензия распространяется на все картинки, микрофотографии, таблицы и third-party credits;
- разрешение на обучение/ingestion автоматически следует из права читать открытую книгу.

**Варианты без принятия решения за владельца:**
1. Получить письменное разрешение OpenStax/Rice University на intended use, включая обработку/ingestion и распространение.
2. Заменить источник на rights-compatible первичный/официальный источник, проверив прямую поддержку и условия.
3. Оставить Claim в HOLD и не включать Biology 2e source в первую редакцию.

**Disposition:** HOLD — factual support is strong, rights are not cleared.

## 5. Ранние цивилизации — прямой locator, но нужны границы исторического обобщения

Проверенные записи:
- `CLM-ANCIENT_CIVILIZATIONS_BASICS-A@1`
- `EU-ANCIENT_CIVILIZATIONS_BASICS-A@1`
- `SRC-ANCIENT_CIVILIZATIONS_BASICS@1`
- дополнительные corroboration Evidence Use/Source tracks в том же срезе — обязательны к полному учёту.

OpenStax World History Volume 1, §3.1 “Early Civilizations” описывает оседлые поселения, сельскохозяйственные излишки, специализацию труда, обмен и социальную стратификацию. <https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations>

Claim перечисляет несколько признаков ранних цивилизаций. Источник показывает их на определённых исторических примерах и регионах, а не как обязательный универсальный набор для любого общества. Следует:
- сохранить региональную и временную конкретику;
- избегать утверждения, что все общества проходили одинаковую последовательность;
- проверить все дополнительные Evidence Use/Sources, а не только EU A;
- отделять интерпретацию учебника от первичных археологических данных;
- выполнить историческую редакционную проверку и rights review.

Не использовать общую фразу о “характерных признаках” как доказательство универсального определения цивилизации без соответствующего контекста.

**Disposition:** HOLD — direct section found; full multi-source dependency and historical scope review required.

## 6. Статистика и измерительная неопределённость — не смешивать NIST и OpenStax

### Statistics basics
Проверенные exact-version candidates включают:
- `CLM-STATISTICS_BASICS-A@1`, B@1, C@1;
- три NIST Evidence Use v1;
- `EU-STATISTICS_BASICS-OPENSTAX@1`;
- `SRC-STATISTICS_BASICS@1`, `SRC-OPENSTAX-STATISTICS-BASICS@1`;
- `CTX-STATISTICS_BASICS@1`, `SCP-STATISTICS_BASICS@1`.

NIST/SEMATECH e-Handbook of Statistical Methods содержит разделы по exploratory data analysis, process improvement и measurement process characterization; отдельные EUs требуют точных section locators, не только homepage/TOC. OpenStax Introductory Statistics 2e §1.1 может служить независимым вводным источником для Claim A, но права этой книги должны быть проверены по её собственной license notice. Не наследовать CC BY 4.0 Physics.

### Measurement uncertainty
Проверенный Claim A говорит, что результат измерения следует интерпретировать с оценкой неопределённости. NIST TN 1297 §2.1 и §§7.1–7.2 дают соответствующий методологический материал, но сама NIST страница предупреждает, что TN 1297 больше не обновляется и может устареть. Текущая NIST Measurement Uncertainty topic page может быть дополнительным maintained source, но не следует смешивать историческую нормативную основу и современную справочную страницу.

В Evidence Use необходимо явно различать:
- measurement error — разность между измеренным значением и reference value;
- measurement uncertainty — параметр, характеризующий разброс значений, которые обоснованно приписываются измеряемой величине.

Не сводить неопределённость к «ошибке прибора», не обещать точность, не делать выводов о конкретном измерении без данных.

**Disposition:** both slices HOLD pending exact NIST pinpoints, source versioning, rights checks and preservation of the error/uncertainty distinction.

## 7. Минимальные критерии закрытия Package B

| Область | Что должно быть выполнено до нового review |
|---|---|
| Motion A | точный OpenStax Physics §2.1 locator, source version and asset credits |
| Motion B | явный выбор velocity vs speed; новый Claim version and EU; no historical score carryover |
| Motion C | vector interpretation made explicit; §2.4 pinpoint |
| Mixtures A | actual EU locator field verified and section §11.1 named; title-specific license review |
| Cell A | written permission or rights-compatible replacement; section §4.1 locator |
| Ancient civilizations A | all corroboration tracks and §3.1 locators; contextualized regional/time scope |
| Statistics A/B/C | precise NIST handbook sections; title-specific OpenStax rights review |
| Measurement uncertainty A | current-vs-legacy NIST source distinction and exact locator; error/uncertainty boundary |

## 8. Ограничения изменения

Этот пакет не:
- редактирует canonical Claim/EU/Source/Context/Scope JSON;
- меняет версии, оценки D/E/B, candidate denominator или publication state;
- переводит HOLD в INCLUDE;
- исключает зависимости или дополнительные corroboration tracks;
- утверждает лицензию на книги OpenStax;
- разрешает публичную публикацию или deployment.

Следующий шаг — versioned remediation proposals только после подтверждения действующей authority и изменения в рамках разрешённого change-control процесса.


## Addendum — title-specific OpenStax license verification — 2026-11-23

The title-level prefaces were checked directly after the initial package draft. This resolves two formerly open license checks:

### Chemistry 2e

OpenStax Chemistry 2e preface explicitly identifies CC BY-NC-SA 4.0, requires attribution and ShareAlike for derivatives, and states that the book may not be used to train or otherwise be ingested into LLMs or generative-AI offerings without prior written permission. Commercial reuse requires permission. This is a rights blocker for any edition whose distribution model or AI processing is not demonstrably compatible. Source: https://openstax.org/books/chemistry-2e/pages/preface

Therefore the Chemistry 2e §11.1 locator is factually useful, but the mixtures Claim remains HOLD until the project documents an allowed use path or substitutes a rights-compatible source. Do not treat “link-only + independent paraphrase” as a blanket legal conclusion for all processing and distribution.

### World History Volume 1, to 1500

The OpenStax preface also states CC BY-NC-SA 4.0 and the same no-LLM-ingestion/no-generative-AI-use without prior written permission condition. It also requires ShareAlike for derivative works and commercial permission. Source: https://openstax.org/books/world-history-volume-1/pages/preface

Accordingly, the ancient-civilizations candidate is now explicitly rights-blocked for any incompatible commercial or generative-AI use. The exact §3.1 locator supports the historical propositions, but factual fit does not cure the license blocker. A rights-compatible replacement source or written permission is required before inclusion.

### Rights correction

Do not rely on third-party catalogues or generic OpenStax-wide assumptions to determine an individual title's license. The official preface for the exact title is the controlling item-level starting point. Physics, Chemistry 2e, Biology 2e and World History Volume 1 have distinct source records and must retain their own verified terms.

No canonical record, rights decision, candidate status or publication state changed. All affected candidates remain HOLD.
