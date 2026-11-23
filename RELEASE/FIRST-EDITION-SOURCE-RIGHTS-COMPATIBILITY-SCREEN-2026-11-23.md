# Первая редакция — предварительная проверка совместимости прав источников

Дата: 2026-11-23  
PR #22: OPEN / DRAFT / NOT MERGED  
Статус: preliminary source-rights research; не юридическое заключение, не permission grant и не решение R-01–R-10.

## 1. Зачем проведена проверка

Первая редакция должна иметь понятную модель распространения. Пока проектная лицензия R-02 и source reuse policy R-05 не приняты, нельзя считать, что любой публичный источник подходит для публикации.

Проверка проведена для реальных источников из представительского 19-главного shortlist и наиболее перспективных кандидатов Package A. Разделены:
- лицензия на оригинальный текст/данные источника;
- ограничения на коммерческое использование;
- ограничения на LLM/generative-AI ingestion;
- права на изображения, карты, таблицы и third-party assets;
- возможность использовать только независимо сформулированный factual paraphrase с точной ссылкой.

**Публичная доступность не равна праву на копирование, переработку или коммерческое распространение.** В этой проверке ни один источник не получает автоматическую clearance.

## 2. Критические результаты по конкретным источникам

### 2.1. OpenStax World History Volume 1, to 1500

Используется в ancient-civilizations-basics как SRC-ANCIENT_CIVILIZATIONS_BASICS@1.

Официальный OpenStax Preface указывает:
- CC BY-NC-SA 4.0;
- запрет использования книги для обучения LLM или иного ingestion в LLM/generative-AI offerings без предварительного письменного разрешения;
- отдельные ограничения на изображения/материалы и коммерческое использование.

Официальные страницы:
- https://openstax.org/books/world-history-volume-1/pages/preface
- https://openstax.org/books/world-history-volume-1/pages/3-1-early-civilizations

**Влияние на первую редакцию:** Claim A/B/C v1 имеют provenance.created_from → этот Source@1. Selection-aware builder считает provenance references обязательными exact dependencies. Поэтому выбор Claim B@1 требует включить OpenStax Source@1, даже если в manifest также выбраны новые CC BY 4.0 Evidence Use tracks.

**Следствие:** для CC BY-only release и AI-assisted content pipeline этот Source нельзя считать совместимым без письменного разрешения/отдельного юридического решения. Для Claim B подготовлен отдельный owner authorization request на versioned provenance migration к трём уже утверждённым CC BY 4.0 Sources. Claim A/C требуют отдельной проверки и не считаются решёнными.

### 2.2. OpenStax Biology 2e

Используется в cell-basics.

Официальный Preface указывает CC BY-NC-SA 4.0 и прямо запрещает LLM/generative-AI ingestion без предварительного письменного разрешения:
https://openstax.org/books/biology-2e/pages/preface

**Влияние:** Cell basics Claim A остаётся HOLD. Варианты — письменное разрешение для точного intended use, замена на rights-compatible источник с новым Evidence Use graph или сохранение HOLD. Не путать Biology 2e с более ранней книгой OpenStax Biology, которая имеет другую лицензию.

### 2.3. OpenStax Chemistry 2e

Используется в mixtures-and-solutions и chemical-reactions-basics, а также в других химических срезах.

Официальный Preface указывает CC BY-NC-SA 4.0 и запрет LLM/generative-AI ingestion без предварительного письменного разрешения:
https://openstax.org/books/chemistry-2e/pages/preface

Точные Evidence Use locators уже присутствуют:
- Mixtures and Solutions A@2 → §11.1 “The Dissolution Process”.
- Chemical Reactions A@4 → §4.3 “Reaction Stoichiometry”, Source@2.

**Влияние:** локаторы и versioned remediation уже выполнены, но это не закрывает права. Если проект выбирает CC BY-only или допускает коммерческое распространение, эти OpenStax Chemistry 2e dependencies остаются incompatible без разрешения. Нельзя переносить CC BY 4.0 с книги OpenStax Chemistry (первое издание) на Chemistry 2e.

### 2.4. OpenStax Physics

Используется в motion-basics и energy-basics.

Официальный Preface содержит несколько разных формулировок:
- в разделе Customization указана CC BY 4.0;
- в блоке Reuse and redistribution указано ограничение на LLM/generative-AI ingestion без предварительного письменного разрешения;
- там же упоминаются TEA attribution и ограничения на часть art/assets; внизу страницы присутствует общий CC BY-NC-SA notice.

Официальная страница:
https://openstax.org/books/physics/pages/preface

**Влияние:** нельзя свести это к простой отметке «CC BY 4.0 — свободно для любого использования». До письменного разъяснения OpenStax/TEA или rights review конкретного текста и assets этот источник не следует включать в публичную CC BY-only редакцию и нельзя использовать для новых AI-assisted content transformations. Motion Claim A и Energy Claim A остаются HOLD либо должны получить альтернативный Source/EU graph.

### 2.5. PostgreSQL 18.7 Documentation

Используется в databases-basics.

Официальная страница лицензии PostgreSQL прямо распространяет PostgreSQL License на software и documentation и разрешает использование, копирование, изменение и распространение для любых целей при сохранении уведомления об авторских правах и текста лицензии:
https://www.postgresql.org/about/licence/

**Влияние:** это один из наиболее благоприятных source paths для первой редакции. Для databases Claim A/B/C @3:
- exact PostgreSQL 18.7 locators уже присутствуют в EU@3;
- Source@3 pin-ит §§2.2–2.6;
- Context/Scope@3 ограничивают утверждения конкретной версией PostgreSQL 18.7.

Необходимо сохранить требуемые copyright/license notices и не представлять документацию PostgreSQL 18.7 как последнюю major version: PostgreSQL 19 был выпущен 19 ноября 2026 года. Rights clearance самой документации не заменяет редакционную проверку содержания.

### 2.6. American Red Cross — Be Informed

Используется в emergency-alert-warning.

Официальные Terms of Use устанавливают personal, revocable, non-transferable, non-exclusive license для personal non-commercial use; ограничивают копирование/распространение и запрещают воспроизводить страницы целиком в другом сервисе без отдельного разрешения:
https://www.redcross.org/terms-of-use.html

**Влияние:** существующий Claim/EU@2 — factual paraphrase о местных каналах оповещения, watch/warning и protective actions, а не копия Red Cross текста. Это снижает риск копирования выразительного материала, но не создаёт автоматического разрешения на коммерческое использование или на включение Red Cross content/assets в продукт.

Рекомендуемый путь: сохранить независимый краткий factual paraphrase и прямую ссылку; не копировать текст, изображения, графику, логотипы или page layout; получить rights/terms review до выпуска, особенно если проект будет коммерческим.

### 2.7. FAO Food Security handbook

Используется в food-security-basics.

Официальная страница FAO Rights and Permissions говорит, что все публикации FAO защищены copyright; без отдельного указания допускается использование для private study, research, teaching и non-commercial products/services при attribution. Reproduction, translation и adaptation требуют permission:
https://www.fao.org/publications/about-fao-publishing/permissions/

**Влияние:** FAO §1.4 является хорошим фактическим источником для Claim A, но это не автоматическая коммерческая или CC BY-only clearance. Если первая редакция будет коммерческой или распространяться под CC BY-only, требуется permission или rights-compatible alternative. До этого допустимость только factual paraphrase + citation должна быть отдельно зафиксирована владельцем/юристом.

### 2.8. World Bank poverty/food/economics pages

Используются в части economic-systems candidate sources.

Официальные World Bank Terms of Use разрешают personal, educational and non-commercial use с attribution; reproduction, redistribution или commercial use требуют предварительного письменного разрешения, если отдельно не указано иное:
https://www.worldbank.org/ext/en/legal/terms-conditions/reproduction-and-use

**Влияние:** World Bank homepage/report/page не становится открытой лицензией только из-за бесплатного доступа. Economics Claim A остаётся HOLD, пока source fit и права для конкретного материала не закрыты. Для первой редакции предпочтителен альтернативный open-license или government source, если он прямо поддерживает Claim.

## 3. Government sources — важная оговорка

Для CDC, NOAA, NIST, USGS, USDA NRCS и других федеральных источников США factual government information часто может использоваться шире, чем copyrighted expressive content. Но официальное USAGov разъяснение подчёркивает, что не всё размещённое на федеральных сайтах является government work: сайты могут содержать third-party intellectual property, используемую по разрешению:
https://www.usa.gov/government-copyright

Практический стандарт для первой редакции:
- использовать собственный factual paraphrase и прямую ссылку;
- не копировать изображения, карты, схемы, таблицы, логотипы, фотографии и third-party content;
- проверять attribution и notices на конкретной странице;
- для USDA Soil page учитывать, что определения ссылаются на Soil Science Society of America и Soil Taxonomy;
- для NIST/NOAA/USGS/CDC проверять конкретные assets, а не делать вывод по домену в целом.

Это предварительная оценка, не blanket public-domain determination.

## 4. OpenStax title-specific matrix

| Точное издание | Проверенная страница лицензии | Лицензия | LLM/generative-AI restriction | First-edition disposition |
|---|---|---|---|---|
| Physics (TEA/OpenStax) | Preface | Внутренне неоднозначные формулировки: CC BY 4.0 в Customization и более сложный Reuse notice | Да | HOLD; получить разъяснение или заменить Source |
| Chemistry 2e | Preface | CC BY-NC-SA 4.0 | Да | HOLD; permission или alternative |
| Biology 2e | Preface | CC BY-NC-SA 4.0 | Да | HOLD; permission или alternative |
| World History Volume 1, to 1500 | Preface | CC BY-NC-SA 4.0 | Да | HOLD; permission или provenance migration/alternative |
| Chemistry (first edition) | Preface | CC BY 4.0 | Проверить exact use terms отдельно | Не переносить эту лицензию на Chemistry 2e |
| Biology (first edition) | Preface | CC BY 4.0 | Проверить exact use terms отдельно | Не переносить эту лицензию на Biology 2e |

Ключевое правило: лицензия относится к точному названию и версии книги, а не к бренду OpenStax в целом.

## 5. Практическая стратегия для первой редакции

### Приоритетно использовать после item-level review

- PostgreSQL documentation: permissive documentation license with notice retention.
- Уже owner-approved CC BY 4.0 scholarly article tracks in ancient-civilizations-basics, subject to exact dependency closure and no third-party asset reuse.
- Government factual sources (CDC/NOAA/NIST/USGS/USDA) только после page-level check и исключения third-party assets.

### Не использовать в публичном выпуске до permission/alternative

- OpenStax Chemistry 2e.
- OpenStax Biology 2e.
- OpenStax World History Volume 1, to 1500.
- OpenStax Physics until its inconsistent title-specific reuse/AI terms are clarified.
- Red Cross content beyond independent factual paraphrase/link unless specific permission is obtained.
- FAO and World Bank publications/pages for commercial or CC BY-only redistribution unless applicable permission or a rights-compatible source path is established.

### Candidate-level impact

- Databases basics: strongest rights-compatible path currently identified; retain exact version boundary 18.7 and required notices.
- Mixtures and solutions / Chemical reactions: exact locators are present, but Chemistry 2e rights block public release under a CC BY-only/commercial model without permission.
- Cell basics: Biology 2e rights block.
- Ancient Civilizations Claim B: new CC BY 4.0 article tracks exist, but Claim B@1 provenance still requires the old World History Source@1; separate provenance migration request is prepared.
- Motion/Energy: OpenStax Physics rights terms require clarification or replacement.
- Emergency alerts: Red Cross terms are restrictive; factual paraphrase/link only is not blanket clearance.
- Food security: FAO non-commercial permission boundary must be resolved.
- Economics: World Bank non-commercial/permission boundary must be resolved.

## 6. Что не решено этим screen

- Project rights holder, content/data license, code license, contributor terms, source reuse policy, editor, release approver, correction/takedown process, attribution/authorship policy and rights-evidence register remain R-01–R-10 OPEN.
- No permission request has been sent.
- No project license is adopted.
- No item is promoted to INCLUDE.
- No canonical record, source graph, candidate denominator, coverage manifest, allowlist, deployment, merge or main branch changed.

Следующий шаг — владелец выбирает intended distribution/license model and approves a source reuse policy; после этого item-level review может решать, какие sources can be retained, which need permission, and which must be replaced.
