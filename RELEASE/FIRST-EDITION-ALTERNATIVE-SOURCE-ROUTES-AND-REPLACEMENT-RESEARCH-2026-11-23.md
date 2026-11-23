# Первая редакция — альтернативные источники для правово-ограниченных кандидатов

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: bounded alternative-source research; не canonical replacement, не permission grant и не INCLUDE.

## 1. Цель

После source-rights screen выявлены несколько важных тем, для которых текущий OpenStax/FAO/World Bank Source может быть несовместим с предполагаемой моделью распространения или AI-assisted workflow. Вместо остановки темы исследованы альтернативные официальные и open-license маршруты.

Результат разделяет:
- прямую альтернативу, которую можно дальше проверять;
- полезное corroboration, не покрывающее Claim целиком;
- альтернативу с собственной лицензией/ограничениями;
- источник, который следует отвергнуть из-за устаревания или несоответствия.

Никакие Source/Evidence Use/Claim records не добавлены и не изменены.

## 2. Науки о жизни — замена OpenStax Biology 2e

### Найденный кандидат: NHGRI Cell glossary

Официальный National Human Genome Research Institute, *Cell*:
https://www.genome.gov/genetics-glossary/Cell?id=25

Страница обновлена 23 ноября 2026 года. Она прямо определяет клетку как базовый строительный элемент живых организмов и различает эукариотические и прокариотические клетки по наличию ядра и мембранных органелл.

**Почему это перспективно**
- Прямая государственная научно-образовательная страница NIH/NHGRI.
- Определение и различие prokaryote/eukaryote прямо соответствуют базовой теме Cell Basics.
- Нет зависимости от OpenStax Biology 2e, у которого CC BY-NC-SA 4.0 и отдельный LLM ingestion restriction.

**Границы**
- Страница содержит изображение и видео/аудио; не переносить их в Энциклопедию.
- Проверить точную редакцию Claim A: если она говорит о «структурной и функциональной единице», NHGRI wording напрямую говорит о basic building block; функциональный аспект может потребовать отдельной опоры.
- Для government page всё равно проверить page-level notices и third-party content. Использовать только независимый factual paraphrase и ссылку.

**Рекомендация:** подготовить новый Source/Evidence Use track на NHGRI для базового определения клетки и отдельный track для prokaryote/eukaryote, если Claim это требует. Текущие OpenStax Source/EU оставить исторически неизменными; новые записи создавать только после bounded authorization.

## 3. Науки о человеке — усиление Learning Basics

### Найденный прямой locator: NIMH Learning and Memory Program

https://www.nimh.nih.gov/about/organization/dnbbs/behavioral-science-and-integrative-neuroscience-research-branch/learning-and-memory-program

В разделе Overview NIMH прямо перечисляет working memory, episodic encoding, consolidation и retrieval. Это точное совпадение с процессами, перечисленными в CLM-LEARNING_BASICS-A@1.

**Почему это важно**
- Canonical Source уже указывает на NIMH Learning and Memory Program.
- EU-A сейчас выглядит generic, но источник фактически содержит прямую поддержку.
- Не требуется искать новый Source; потенциально достаточно versioned EU с точным section/page locator и краткой границей поддержки.

**Граница**
- Страница описывает область исследовательской программы и cognitive processes; она не является учебником, который исчерпывающе определяет все процессы или объясняет их механизмы.
- Claim не должен трактовать перечень NIMH как исчерпывающую классификацию обучения и памяти.
- NIMH — федеральный институт; исключить third-party assets и использовать собственный factual paraphrase.

**Рекомендация:** высокий приоритет для EU locator remediation после проверки действующей authorization scope. Claim wording не менять без отдельного editor approval.

## 4. Продовольственная безопасность — альтернатива FAO / World Bank

### Найденный кандидат: USDA ERS EIB-175

Sharad Tandon et al., *Progress and Challenges in Global Food Security*, USDA Economic Research Service, EIB-175 (31 July 2017):
https://www.ers.usda.gov/publications/84525
Full report PDF:
https://www.ers.usda.gov/sites/default/files/_laserfiche/publications/84526/EIB-175.pdf

В разделе “Measurement of Food Security”, печатная страница 9, report описывает четыре измерения:
- availability;
- access;
- utilization;
- stability.

Текст связывает эти измерения с физическим и экономическим доступом, безопасностью/питательностью и устойчивостью условий во времени. Это полезный глобальный аналитический источник и более перспективный федеральный rights route, чем World Bank/FAO для потенциальной коммерческой редакции.

**Границы**
- Доклад 2017 года — хороший концептуальный источник, но не актуальная статистика на 2026 год.
- Он описывает четыре измерения, но не заменяет автоматически глобальное определение, которое сейчас находится в Claim A.
- В PDF присутствуют cover image и charts/data assets; не копировать их. Использовать только factual paraphrase и точный locator.
- Проверить, что конкретный материал является работой федерального агентства, а не third-party contribution; U.S. federal site presence alone does not prove public-domain status.

**Рекомендация:** использовать EIB-175 §“Measurement of Food Security”, p. 9 как corroborating Source. Для самостоятельного Claim о глобальном определении нужно проверить точную поддержку каждого элемента или оставить FAO Source с отдельно разрешённой non-commercial boundary.

## 5. Химические науки — условная альтернатива OpenStax Chemistry 2e

### IUPAC Gold Book — отдельные термины

- “solution”: https://goldbook.iupac.org/terms/view/S05746
- “chemical reaction”: https://goldbook.iupac.org/terms/view/C01033
- Usage license: https://goldbook.iupac.org/

Текущая версия Compendium — 5.0.0 (2025). Для individual terms Gold Book указывает CC BY-SA 4.0. Страница одновременно сообщает, что коммерческое лицензирование всей коллекции следует согласовывать с IUPAC Secretariat.

**Поддержка**
- “solution” описывает liquid or solid phase containing more than one substance, with solvent/solute distinction.
- “chemical reaction” описывает процесс interconversion of chemical species.
- Это авторитетные терминологические источники, пригодные для точного определения терминов.

**Границы прав и смысла**
- CC BY-SA 4.0 — не CC BY 4.0; адаптация отдельного термина требует attribution и ShareAlike.
- Для коммерческого использования Compendium IUPAC просит обращаться за лицензией; не считать коммерческое использование автоматически разрешённым.
- Термин “solution” в IUPAC не буквально совпадает с учебной фразой OpenStax “homogeneous mixture”; не подменять одно определение другим без научной проверки.
- В самом Gold Book есть предупреждение, что некоторые определения могут быть superseded; следует сохранить версию термина и исходную recommendation.

**Рекомендация:** это возможный альтернативный source path, если проект выбирает совместимую CC BY-SA модель или получает разрешение IUPAC. До решения R-02 и проверки R-05 не использовать как автоматическую замену OpenStax Chemistry 2e.

## 6. Физические науки — NASA Frames of Reference не подходит как replacement

Проверен NASA GSFC *Frames of Reference: The Basics*:
https://pwg.gsfc.nasa.gov/stargaze/Lframes1.htm

Страница прямо содержит disclaimer:
- материал оставлен онлайн для архивных целей;
- он больше не обновляется;
- возможны broken links и устаревшие элементы;
- последняя редакция — 24 октября 2004 года.

Содержательно она объясняет систему отсчёта, но её собственный статус archival-only не соответствует требованию первой редакции к актуальным и воспроизводимым источникам.

**Решение:** не использовать как primary Source для Motion Basics. Оставить только как исторический/учебный справочный след, если это отдельно нужно. Продолжить поиск актуального rights-compatible source или получить письменное разрешение на OpenStax Physics.

## 7. Общество и экономика — найденные источники не дают чистого решения

### Federal Reserve Education — “What Is Economics?”

https://www.federalreserveeducation.org/teaching-resources/economics/scarcity/what-is-economics

Транскрипт объясняет экономику как изучение того, как люди принимают решения с учётом доступных альтернатив и ресурсов, а также scarcity и opportunity cost. По смыслу это полезно для базовой темы.

Но это материал Federal Reserve Bank of St. Louis, а не автоматически public-domain federal agency material. Отдельные Federal Reserve Education handouts содержат ограниченное разрешение на educational reprinting only. Поэтому это не чистая коммерческая/CC BY-only замена World Bank.

### CORE Econ — The Economy 2.0

Официальный copyright page:
https://books.core-econ.org/the-economy/macroeconomics/0-2-copyright.html

Лицензия — CC BY-NC-ND 4.0. Это допускает sharing с attribution, но запрещает commercial use и распространение modified/adapted derivatives. Такой режим не подходит для свободного включения изменённого/переведённого содержания в проект, который может выбрать коммерческую или CC BY-only модель.

### Вывод

Не заменять World Bank на Federal Reserve или CORE Econ автоматически. Оставить Economics Claim A HOLD до поиска источника с точной поддержкой и совместимой лицензией либо отдельного owner permission.

## 8. Приоритет альтернативных маршрутов

| Приоритет | Тема | Альтернативный Source | Результат |
|---:|---|---|---|
| 1 | Cell basics | NHGRI Cell glossary | Сильная потенциальная замена OpenStax Biology 2e; нужна exact Claim fit и page-level rights check |
| 2 | Learning basics | NIMH Learning and Memory Program | Прямой locator для уже существующего Source; подготовить EU version |
| 3 | Food security | USDA ERS EIB-175, p. 9 | Хороший глобальный corroboration по четырём измерениям; не полностью заменяет глобальное определение |
| 4 | Mixtures / Chemical reactions | IUPAC Gold Book individual terms | Сильная терминология, но CC BY-SA 4.0 и коммерческая оговорка IUPAC |
| 5 | Motion basics | NASA Frames of Reference | Отклонить как primary replacement: archival-only, last updated 2004 |
| 6 | Economics basics | Federal Reserve Education / CORE Econ | Смысловая опора есть, но лицензии/terms не решают commercial/derivative constraints |

## 9. Изменения, которые можно подготовить после разрешения

- Cell: новый Source@1 NHGRI + EU@1 для Claim A; сохранить старый OpenStax Source/EU как историю, не перезаписывать.
- Learning: versioned EU с прямым NIMH locator, если существующая bounded authorization покрывает точный record.
- Food security: новый USDA ERS Source/EU track; не удалять FAO Source и не переписывать Claim без отдельного разрешения.
- Chemistry: новый IUPAC Source/EU только после решения по CC BY-SA compatibility and commercial permission.
- Motion: искать альтернативу; NASA archival page не использовать.

Никакие из этих Source/EU records не созданы и не изменены в этой работе.

## 10. Что остаётся открытым

- R-02/R-05: проектная лицензия и source reuse policy.
- Item-level rights evidence для NHGRI/NIMH/USDA/IUPAC и исключение third-party assets.
- Bounded authorizations на новые Source/EU IDs и versioned updates.
- Claim-level source-fit, Context/Scope applicability, Human View и editorial review.
- Все кандидатные записи остаются HOLD; production INCLUDE manifest отсутствует.

Этот документ завершает исследовательский пакет альтернативных источников, но не является разрешением на canonical edits или публикацию.
