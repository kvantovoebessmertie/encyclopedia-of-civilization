# 017 — PROVENANCE

Статус: ACCEPTED / BASELINE  
Версия: 0.1  
Проект: Энциклопедия цивилизации

---

# 1. Назначение

Настоящий стандарт определяет модель происхождения и линии происхождения (Provenance) в системе «Энциклопедия цивилизации».

Provenance отвечает на вопросы:

- откуда происходит объект, запись, содержание, значение или утверждение;
- какие предшествующие объекты или представления участвовали в его появлении;
- какие преобразования произошли между ними;
- какие версии или состояния использовались;
- какие агенты, инструменты или процессы участвовали;
- какая часть объекта имеет конкретное происхождение;
- является ли связь происхождения прямой, косвенной, установленной, предполагаемой или неизвестной;
- существуют ли общие линии происхождения у нескольких источников;
- какие сведения о происхождении известны, неизвестны, утрачены, ограничены или оспариваются.

Provenance предназначен для сохранения проверяемой истории происхождения знания и связанных с ним объектов.

Provenance не является:

- доказательством истинности;
- показателем качества;
- показателем надёжности;
- автоматической оценкой независимости источников;
- доказательством авторства;
- доказательством подлинности;
- полным описанием причинности;
- заменой Evidence;
- заменой Inference;
- заменой Assessment;
- заменой Identity;
- заменой State;
- заменой Observation или Measurement.

---

# 2. Основной принцип

Минимальная формула:

> Provenance — это представление материально значимой линии происхождения объекта относительно определённой цели, аспекта и уровня детализации.

Следовательно:

> Provenance representation ≠ actual lineage automatically.

Записанная системой линия происхождения не обязана быть самой линией происхождения в мире.

Она может быть:

- непосредственно зарегистрированной системой;
- сообщённой источником;
- импортированной;
- реконструированной;
- выведенной;
- предположенной;
- частично известной;
- оспариваемой.

Поэтому необходимо различать:

> actual lineage  
> ≠ represented lineage  
> ≠ knowledge about lineage at a particular time.

---

# 3. Provenance как утверждение

Если система сама не наблюдала и не зарегистрировала операцию происхождения как часть собственной операционной истории, утверждение о происхождении должно рассматриваться как проверяемое представление знания.

Например:

> Рукопись B была переписана с рукописи A.

является Claim о происхождении.

Оно может иметь:

- Evidence;
- Source;
- Scope;
- Context;
- State;
- Assessment;
- uncertainty;
- competing Claims;
- собственный Provenance.

Наличие provenance metadata само по себе не превращает такую связь в установленный факт.

---

# 4. Операционный и представленный Provenance

Следует различать по меньшей мере два фундаментальных случая.

## 4.1. Operational Provenance

Происхождение, непосредственно зарегистрированное системой в ходе выполняемой ею операции.

Например:

Record A  
→ normalization operation  
→ Record B

Система может непосредственно знать, что конкретная операция была запущена и что конкретный результат был создан в рамках этой операции.

Но даже здесь:

> recorded operation ≠ correct semantic description of operation.

Лог может быть полным технически, но ошибочно классифицировать фактическое преобразование.

## 4.2. Represented Provenance

Происхождение, утверждаемое, реконструируемое или предполагаемое относительно внешнего мира.

Например:

Manuscript B  
probably copied from Manuscript A

Такое происхождение требует обычной эпистемической обработки.

Operational Provenance и Represented Provenance MUST NOT автоматически считаться эквивалентными.

---

# 5. Цель Provenance

Provenance существует не ради накопления истории как таковой.

Сохраняется материально значимое происхождение.

Материальность определяется тем, влияет ли происхождение на:

- интерпретацию;
- проверяемость;
- воспроизводимость;
- независимость Evidence;
- обнаружение ошибок;
- историю изменений;
- происхождение данных;
- происхождение содержания;
- авторство или вклад;
- реконструкцию;
- безопасность;
- историческую достоверность;
- возможность восстановления знания офлайн.

Несущественные технические детали MAY быть опущены.

---

# 6. Provenance Target

Provenance всегда относится к некоторому Target.

Target MAY быть:

- Record;
- Claim;
- Source;
- Evidence;
- Dataset;
- Model;
- Artifact;
- Sample;
- Procedure;
- Expression;
- Representation;
- Fragment;
- Field;
- Value;
- Component;
- Result;
- Snapshot;
- иной объект, для которого происхождение материально значимо.

Provenance не обязан существовать только на уровне целого Record.

---

# 7. Гранулярность Provenance

Происхождение MAY относиться к:

- whole object;
- section;
- fragment;
- paragraph;
- field;
- row;
- column;
- cell;
- value;
- Claim;
- component;
- range;
- group.

Гранулярность определяется Profile, задачей и материальностью.

> Record-level provenance MUST NOT automatically propagate to every component or Claim.

Например, если книга частично заимствует другой источник, это не означает, что каждое утверждение книги происходит из него.

И наоборот, отдельный Claim может иметь происхождение, отличающееся от происхождения Record в целом.

Система MUST избегать как чрезмерного укрупнения, так и бесконтрольного дробления Provenance.

---

# 8. Scoped Provenance

Связь происхождения сама может иметь Scope.

Например:

paragraphs 3–7 of B  
copied-from  
pages 20–24 of A

или:

value V  
derived-from  
dataset column X

Если Provenance относится только к части Target, он MUST NOT автоматически распространяться на весь Target.

Component binding и Scope qualification MAY сосуществовать и в некоторых представлениях частично пересекаться, но их семантические роли MUST оставаться различимыми.

Component binding отвечает прежде всего на вопрос:

> какая часть Target или Input участвует в линии происхождения?

Scope qualification отвечает:

> в какой области, границах или условиях применимо само provenance-представление или Claim о происхождении?

Component binding MUST NOT автоматически интерпретироваться как полный Scope provenance Claim, и наоборот.

---

# 9. Provenance Dimensions

Разные виды происхождения могут описывать разные аспекты одного объекта.

Система MAY различать, где материально:

- representation lineage;
- content lineage;
- information-origin lineage;
- physical/material lineage;
- custody lineage;
- execution lineage;
- transformation lineage;
- selection lineage;
- derivation lineage;
- authorship/contribution lineage;
- dataset lineage;
- model lineage.

Этот список не является закрытым.

Общая инфраструктура Provenance MUST NOT превращать эти измерения в одну недифференцированную связь.

Например:

> физическое происхождение носителя ≠ происхождение содержащегося на нём текста.

И:

> происхождение файла ≠ происхождение Claim внутри файла.

Authorship и contribution MAY участвовать в описании Provenance, однако полная семантика авторства, вклада, прав, ответственности и владения не определяется настоящим стандартом.

---

# 10. Provenance Relation

Связь происхождения должна быть семантически определённой настолько, насколько это возможно.

Примеры:

- copied-from;
- translated-from;
- transcribed-from;
- extracted-from;
- derived-from;
- adapted-from;
- summarized-from;
- reconstructed-from;
- restored-from;
- merged-from;
- synthesized-from;
- generated-from;
- digitized-from;
- converted-from;
- selected-from.

Список расширяем.

Generic relation:

> derived-from

MAY использоваться, если более точный тип неизвестен или не требуется.

Но:

> generic ancestry MUST NOT substitute for a materially known specific operation.

---

# 11. Неизвестная или неоднозначная операция

Если известно, что происхождение существует, но тип преобразования неизвестен, система MUST позволять сохранить:

> derived-from — operation unknown.

Если известно несколько возможных вариантов:

> translated OR paraphrased

система MUST NOT произвольно выбирать один.

Неоднозначность происхождения должна сохраняться как неоднозначность.

> ambiguous provenance language MUST NOT be normalized into invented certainty.

Фразы вроде:

- «основано на»;
- «по материалам»;
- «согласно»;
- «версия»;
- «из архивов»

сами по себе не доказывают конкретный тип происхождения.

---

# 12. Direct и Indirect Provenance

Необходимо различать direct provenance и indirect provenance.

Если:

> A → B → C

то C может иметь A как ancestor.

Но:

> C derived indirectly from A

не означает:

> C directly copied from A.

Транзитивное происхождение MUST NOT автоматически превращаться в прямую операцию.

---

# 13. Derived Provenance Relations

Некоторые provenance relations могут вычисляться из других.

Например:

> A → B  
> B → C

может позволять вывести:

> C descends-from A.

Такое отношение должно оставаться отличимым от непосредственно зарегистрированной связи.

> inferred/transitive provenance relation ≠ directly recorded provenance relation.

Материализованный transitive closure MUST NOT маскироваться под первичную историю операций.

---

# 14. Provenance и транситивность

Не все типы Provenance транзитивны одинаково.

Например:

> B translated-from A  
> C translated-from B

не означает:

> C directly translated-from A.

Также композиция нескольких операций не должна автоматически получать конкретный тип без определённого правила композиции.

> operation composition MUST NOT invent a direct operation semantics.

---

# 15. Provenance Graph

Provenance обычно образует граф.

Граф MAY содержать:

- линейные цепочки;
- ветвления;
- слияния;
- несколько родителей;
- несколько потомков;
- неизвестные участки;
- competing lineage hypotheses;
- частичные связи;
- групповые связи.

Provenance не обязан быть деревом.

---

# 16. Частичный порядок

История Provenance не обязана иметь полный временной порядок.

Может быть известно:

> A before C  
> B before C

но неизвестно отношение между A и B.

Система MUST позволять сохранять partial ordering.

Отсутствие точного timestamp не должно заставлять систему придумывать точный порядок.

---

# 17. Multi-input Provenance

Один результат может происходить из нескольких входов.

Например:

> A + B → synthesis → C.

Это не обязательно эквивалентно:

> C derived-from A  
> C derived-from B

если при таком разложении теряется смысл совместного использования входов.

> Multi-input provenance operation ≠ independent pairwise provenance edges automatically.

---

# 18. Joint Input Integrity

Если результат зависит от совместной комбинации нескольких входов, их совместность MUST оставаться восстанавливаемой.

Например:

> base text: A  
> variant witness: B  
> editorial evidence: C  
> → reconstructed text D.

Роли входов материально различны.

Система SHOULD позволять сохранять:

- input roles;
- input grouping;
- input ordering;
- required combination;
- alternatives;
- optional inputs.

---

# 19. Альтернативные входы

Следует различать:

> derived from A AND B

и:

> derived from A OR B.

Если неизвестно, какой из альтернативных источников был фактически использован, система MUST NOT превращать альтернативы в совместное происхождение.

---

# 20. Multi-output Provenance

Одна операция MAY создавать несколько результатов.

Например:

> Source A  
> → processing  
> → transcript B  
> → metadata C  
> → summary D.

Результаты могут иметь разные роли и разную семантическую связь с входом.

---

# 21. Compound Transformations

Преобразование MAY быть составным.

Например:

> OCR → correction → normalization → translation → human editing.

Если эти этапы материальны, система SHOULD сохранять их отдельно или в форме, позволяющей восстановить их семантический порядок.

Система MUST NOT заменять известную составную историю неопределённым `derived-from`, если это уничтожает материально важную информацию.

---

# 22. Intended и Actual Transformation

Необходимо различать:

> declared/intended transformation ≠ actual transformation.

Например, операция была объявлена как `translate`, но фактически результат оказался одновременно переводом и сокращённым пересказом.

Намерение операции не доказывает её фактическую семантику.

---

# 23. Статус операции

Где материально, система MAY различать:

- attempted;
- executed;
- completed;
- succeeded;
- failed;
- partially completed;
- validated.

Запуск операции не доказывает успешность результата.

---

# 24. Transformation Fidelity

Происхождение и качество преобразования — разные вопросы.

Для преобразования MAY быть важно сохранять fidelity относительно:

- текста;
- смысла;
- структуры;
- числовых значений;
- Scope;
- Context;
- modality;
- quantifiers;
- units;
- uncertainty;
- formatting.

Например:

> маленькое текстовое изменение ≠ маленькое смысловое изменение.

И:

> большое изменение формулировки ≠ обязательно большое изменение Claim.

---

# 25. Lossy Transformations

Некоторые операции по природе являются lossy:

- summarization;
- compression;
- selection;
- abstraction;
- simplification;
- redaction;
- partial extraction.

Если потеря информации материальна, она SHOULD оставаться обнаружимой.

---

# 26. Transformation Parameters

Где результат существенно зависит от параметров преобразования, Provenance MAY сохранять:

- software;
- software version;
- model;
- model version;
- configuration;
- prompt;
- random seed;
- locale;
- rounding mode;
- library version;
- algorithm;
- execution environment;
- иные материальные параметры.

Не каждый параметр обязан сохраняться.

Критерий — материальность для проверки, интерпретации или воспроизводимости.

---

# 27. Provenance и воспроизводимость

> complete provenance ≠ reproducibility.

Полная известная линия происхождения не гарантирует возможность воспроизвести результат.

И наоборот:

> reproducibility ≠ complete provenance.

Воспроизводимый результат может иметь неизвестную интеллектуальную или историческую предысторию.

Также следует различать:

> semantic reproducibility ≠ exact/bitwise reproducibility.

---

# 28. Недетерминированные преобразования

Одинаковые входы не всегда создают одинаковые выходы.

Это особенно важно для:

- stochastic models;
- AI systems;
- simulations;
- Monte Carlo methods;
- concurrent systems.

Provenance MUST NOT автоматически подразумевать детерминированность.

---

# 29. Authorship и Provenance

Следует жёстко различать:

- record creator;
- uploader;
- scanner;
- operator;
- translator;
- editor;
- model;
- tool developer;
- content author;
- original author;
- contributor;
- rights holder;
- owner.

Эти роли MAY пересекаться, но не эквивалентны автоматически.

В частности:

> uploader ≠ author  
> scanner ≠ author  
> record creator ≠ content author  
> translator ≠ original author  
> operator ≠ model developer  
> owner ≠ author.

Настоящий стандарт использует такие роли только в той мере, в которой они материальны для происхождения. Он не определяет исчерпывающую модель authorship, contribution, ownership, rights или responsibility.

---

# 30. Вклад в содержание

Преобразование MAY вводить новое семантическое содержание.

Например, редактор может не просто исправить текст, а добавить новый Claim.

В таком случае система SHOULD позволять отличать:

> transformed content

от:

> newly contributed content.

Один Record может иметь смешанное происхождение содержания.

---

# 31. Collective и Mixed Provenance

Объект MAY иметь:

- одного автора;
- нескольких авторов;
- коллективное происхождение;
- распределённое происхождение;
- неизвестного автора;
- смешанное human/machine происхождение;
- постепенное эволюционное происхождение.

Provenance MUST NOT требовать единственного creator.

---

# 32. Diffuse и Emergent Provenance

Не всякое происхождение имеет дискретный первый Record или единичное событие создания.

Традиция, рецепт, устная история или коллективная практика могут возникать постепенно.

Система MUST позволять представлять:

- diffuse origin;
- emergent origin;
- collective evolving lineage

без изобретения фиктивного первого автора или первого объекта.

---

# 33. Influence ≠ Derivation

Не всякое влияние является линией происхождения в строгом смысле.

Автор мог:

- читать Source;
- знать общепринятый факт;
- вдохновляться произведением;
- пользоваться общей методологией.

Это не означает автоматически:

> content derived-from Source.

Provenance MUST избегать превращения любого интеллектуального влияния в ancestry edge.

---

# 34. Citation ≠ Provenance

Наличие citation не доказывает происхождение содержания.

Citation может выполнять роль:

- Evidence;
- contrast;
- historical note;
- see-also;
- attribution;
- quotation source;
- data source;
- methodological reference.

Следовательно:

> citation existence ≠ content derivation automatically.

Также:

> absence of citation ≠ absence of provenance.

---

# 35. Bibliography ≠ Lineage

Наличие Source в библиографии не означает, что каждый Claim документа происходит из этого Source.

Автоматический ingest MUST NOT превращать всю библиографию в provenance parents документа или его Claims.

---

# 36. Consultation, Basis и Derivation

Следует различать:

- consulted;
- referenced;
- used-as-basis;
- selected-from;
- extracted-from;
- derived-from;
- synthesized-from.

Например, автор мог прочитать 20 Sources перед созданием нового Claim.

Это не означает, что Claim непосредственно derived-from каждого из них.

---

# 37. Synthesis

Synthesis представляет особый случай происхождения.

Результат может возникнуть после совместного рассмотрения нескольких источников без механического копирования или формального вывода.

Если это материально, система SHOULD позволять представить `synthesized-from` с сохранением ролей входов и различием между:

- direct extraction;
- inference;
- editorial synthesis;
- consultation.

---

# 38. Provenance и Evidence

Provenance может быть важным входом в анализ Evidence.

Но:

> Provenance graph ≠ Evidence dependency graph.

И:

> provenance independence ≠ evidential independence.

Два Evidence могут не иметь общего известного контентного предка, но зависеть от:

- одного dataset;
- одного witness;
- одного instrument;
- одного software;
- одной ошибки;
- одного посредника;
- одного процесса обработки.

---

# 39. Независимость

Следующие выводы запрещены:

> no known common provenance → independent Evidence.

и:

> common provenance → completely dependent Evidence.

Оба являются чрезмерными.

Provenance — один из входов в Assessment независимости.

Независимость должна оцениваться относительно:

- конкретного Claim;
- конкретного evidential contribution;
- конкретного аспекта зависимости.

---

# 40. Общий источник информации

Два Records могут быть независимо созданы, но происходить от одного информационного источника.

Например:

> Witness X  
> → independently tells A  
> → independently tells B.

A и B имеют независимое представление, но общий information origin.

Поэтому:

> representation independence ≠ information-source independence.

---

# 41. Общий объект наблюдения

Два независимых наблюдателя могут наблюдать один Event или один объект.

Это само по себе не создаёт общего Provenance.

> same observed Event ≠ common provenance.

> same observed object ≠ common provenance.

Иначе система уничтожила бы смысл независимых наблюдений.

---

# 42. Tool и Method Dependencies

Использование одного:

- инструмента;
- software;
- метода;
- calibration;
- pipeline

может создавать коррелированные ошибки.

Но:

> shared tool/method ≠ common content ancestry automatically.

Такие зависимости могут быть важны для Evidence Assessment, не становясь обычной линией происхождения содержания.

---

# 43. Physical Provenance

Provenance MAY относиться к физическим объектам.

Например:

- artifact;
- sample;
- specimen;
- material;
- component.

Физическая линия происхождения может включать:

- создание;
- разделение;
- объединение;
- хранение;
- передачу;
- транспортировку;
- реставрацию;
- замену частей;
- contamination;
- sampling.

Но:

> physical provenance ≠ content provenance.

---

# 44. Chain of Custody

Chain of custody является видом Provenance, но не доказывает автоматически:

- подлинность;
- отсутствие вмешательства;
- истинность содержания;
- правильность идентификации объекта.

> documented custody ≠ authenticity automatically.

---

# 45. Material vs Artifact Provenance

Возраст материала не обязан совпадать с возрастом объекта.

Например, современный объект может быть изготовлен из древнего материала.

Поэтому:

> material provenance ≠ artifact creation provenance.

---

# 46. World Causality

Причинность в мире и Provenance не являются одним и тем же.

Например:

> Event → causes sensor signal

не означает автоматически, что Event является provenance parent Record в том же смысле, что исходный Dataset.

> world cause ≠ provenance ancestry automatically.

Observation и Measurement должны сохранять собственную семантику.

---

# 47. Model Provenance

Для Model MAY быть важно различать:

- model ancestry;
- training provenance;
- fine-tuning provenance;
- input provenance;
- execution provenance;
- output provenance.

Например, fine-tuned Model может происходить от base Model.

Но:

> inclusion of item in training data ≠ proof that a particular output was derived from that item.

Система MUST NOT изобретать output-level lineage из одного факта training inclusion.

---

# 48. Dynamic Provenance

Некоторые Target являются динамическими:

- live datasets;
- database views;
- streams;
- dynamic pages;
- transclusions;
- generated views;
- cached results.

Их Provenance может зависеть от времени и State используемых входов.

---

# 49. State Binding

Где Source или Target изменяемы, Provenance SHOULD связываться с конкретным:

- State;
- version;
- snapshot;
- revision;
- edition;
- execution instance

где это материально.

Например:

> B derived-from A@v3

значительно точнее, чем:

> B derived-from A

если A изменяется со временем.

---

# 50. Mutable References

URL, filename, repository path или другой location identifier не гарантирует неизменность содержания.

Следовательно:

> location identity ≠ content identity.

Где возможно и материально, система SHOULD сохранять:

- version;
- snapshot;
- timestamp;
- stable identifier;
- hash;
- archived reference;
- иной способ идентифицировать фактически использованное состояние.

Hash помогает обнаруживать различия, но:

> hash equality/inequality ≠ semantic identity automatically.

---

# 51. Live Reference vs Materialized Copy

Следует различать:

- copy;
- snapshot;
- transclusion;
- live reference;
- database view;
- symlink/reference;
- cached output.

Внешне одинаковое содержание может иметь разное поведение происхождения.

Материализованная копия и динамическая ссылка MUST NOT автоматически считаться одним типом Provenance.

---

# 52. Deletion, Redaction и Withdrawal

Следует различать:

- deleted;
- redacted;
- withdrawn;
- deprecated;
- superseded;
- archived;
- restricted;
- restored.

Удаление содержимого является изменением истории объекта и MAY быть материальной provenance operation.

Redaction не обязательно означает физическое удаление данных.

Withdrawal не означает, что Record никогда не существовал.

---

# 53. Restoration

Восстановленный объект SHOULD сохранять связь `restored-from` с использованными предшествующими состояниями, резервными копиями или источниками восстановления, если это материально.

Восстановление MUST NOT маскироваться под новое независимое создание.

---

# 54. Merge Provenance

При merge нескольких ветвей недостаточно только перечислить родителей.

Где материально, Provenance SHOULD позволять восстановить:

- какие компоненты пришли из какой ветви;
- какие варианты были выбраны;
- какие были отвергнуты;
- какие были синтезированы;
- какое содержание было создано заново при разрешении конфликта.

---

# 55. Branching

Provenance MAY ветвиться.

Например:

> A  
> ├── B  
> └── C

B и C имеют общего предка, но дальнейшая история может быть независимой.

Наличие общего предка не означает одинаковость всех последующих компонентов.

---

# 56. Rollback

Возврат к старому содержанию не возвращает объект в прошлое.

Если:

> State 1 → State 2 → rollback to content of State 1

новый State остаётся новым историческим состоянием.

> same content ≠ same historical State automatically.

---

# 57. Technical Version History

История системы контроля версий может быть полезна для Provenance.

Но:

> VCS history ≠ semantic provenance automatically.

Такие операции, как:

- rebase;
- squash;
- cherry-pick;
- force rewrite

могут менять техническую историю без точного соответствия семантической истории содержания.

---

# 58. Version Labels

Version number, edition number или filename не доказывают происхождение.

> version order ≠ derivation order automatically.

> later version label ≠ descendant automatically.

`v2` может быть независимо реконструированным объектом, а не производным `v1`.

---

# 59. Earliest Known ≠ Origin

Система MUST жёстко различать:

- earliest known occurrence;
- oldest surviving copy;
- first registered Record;
- first digitized copy;
- first publication;
- actual creation/origin.

Следовательно:

> earliest known occurrence ≠ origin.

> oldest surviving copy ≠ original.

> first digital appearance ≠ first existence.

> no earlier source found ≠ original creation.

Отсутствие известного предшественника не доказывает независимое происхождение.

---

# 60. Unknown Provenance

Неизвестное происхождение является допустимым состоянием знания.

Система MUST NOT заполнять пробелы предположениями ради полноты графа.

Следует различать:

- unknown;
- unrecorded;
- not yet investigated;
- lost;
- unresolvable;
- inaccessible;
- restricted;
- redacted.

Эти состояния неэквивалентны.

---

# 61. Provenance Gaps

Линия происхождения MAY содержать пробелы.

Например:

> A → unknown intermediary/intermediaries → C.

Если количество промежуточных этапов неизвестно, система MUST NOT придумывать их число.

---

# 62. Hypothesized Ancestors

Допускается представление:

- неизвестного общего предка;
- предполагаемого посредника;
- competing ancestors;
- alternative lineage hypotheses.

При этом гипотетический предок MUST NOT автоматически становиться установленным Entity или фактом.

---

# 63. Competing Provenance Hypotheses

Для одного Target могут существовать несколько несовместимых или частично совместимых моделей происхождения.

Например:

> Hypothesis A: B copied from X.  
> Hypothesis B: B independently created.  
> Hypothesis C: B partially copied from X and partially independently created.

Система MUST сохранять их различия и эпистемический статус.

---

# 64. Provenance Knowledge Changes

Знание о происхождении может меняться.

Например:

> 2026: origin unknown  
> 2028: likely derived from A  
> 2031: new evidence supports A + B mixed origin.

Это не означает, что историческое происхождение объекта изменилось.

Изменилось знание о нём.

---

# 65. Historical Epistemic State

Система SHOULD позволять восстановить:

> что было известно о Provenance в момент конкретного Assessment, Decision или публикации.

Новые сведения о происхождении MUST NOT переписывать старые Assessments так, словно эти сведения были доступны тогда.

Следует различать:

- actual historical lineage;
- current representation of lineage;
- representation available at time T.

---

# 66. Provenance Assertion Time

Где материально, следует различать:

- time of lineage event;
- time provenance assertion was created;
- time provenance assertion entered system;
- time provenance assertion was assessed.

Например, происхождение объекта может относиться к 1500 году, а Claim об этом происхождении — к 2026 году.

---

# 67. Provenance of Provenance

Утверждение о Provenance само может иметь происхождение.

Например:

> archival note → historian interpretation → database provenance assertion.

Это допустимо.

Однако система не обязана создавать бесконечный мета-граф.

Неполная глубина meta-provenance не делает запись автоматически недействительной.

---

# 68. Provenance Capture Method

Где материально, система SHOULD позволять различать происхождение самой provenance information:

- system-recorded;
- manually entered;
- reported by source;
- imported;
- inferred;
- algorithmically inferred;
- reconstructed;
- curator-reviewed.

Эти категории не являются уровнями истинности.

Например:

> curator-reviewed ≠ objectively true.

Для asserted, inferred, imported, reported или reconstructed Provenance эпистемический статус SHOULD оставаться явно представимым там, где он материален.

Operational Provenance, непосредственно зарегистрированный системой, MUST NOT получать искусственный Claim-level epistemic status только ради формального заполнения схемы, если такой статус не несёт дополнительной семантической информации.

При этом operational registration сама по себе не гарантирует правильность семантической классификации операции.

---

# 69. Imported Provenance

Импортированная система может содержать собственные утверждения о происхождении.

Импорт MUST NOT автоматически превращать доверие внешней системы во внутреннюю установленность.

Следует сохранять, где материально:

- откуда пришла provenance information;
- какие semantics использовала внешняя система;
- какие преобразования произошли при mapping.

---

# 70. Provenance Mapping

При переносе между системами provenance semantics могут быть потеряны.

Например:

> translated-from  
> copied-from  
> summarized-from

могут быть сведены внешней системой к:

> derived-from.

Такое преобразование является lossy.

> lossy provenance mapping MUST remain detectable.

Система MUST NOT позднее реконструировать потерянную специфику как будто она сохранилась.

---

# 71. Provenance Projection

Profile или export MAY показывать только часть полной линии происхождения.

Это допустимо.

Но:

> projected provenance ≠ complete provenance automatically.

Если projection является lossy, это SHOULD быть обнаружимо.

---

# 72. Vocabulary Stability

Типы provenance relations имеют семантику.

Изменение определения типа со временем может изменить интерпретацию старых данных.

Поэтому controlled vocabularies SHOULD иметь стабильные определения или версионирование.

Одинаковая метка в разных Profiles или системах MUST NOT автоматически считаться семантически идентичной.

---

# 73. Provenance Granularity Alignment

Две модели происхождения могут описывать одну историю на разной детализации.

Например:

> A → translation → B

и:

> A → OCR → cleanup → translation → human edit → B

не обязаны противоречить друг другу.

Различная гранулярность:

> ≠ conflict automatically.

---

# 74. Provenance Conflict

Перед объявлением двух provenance representations конфликтующими SHOULD быть согласованы:

- Target;
- component;
- provenance dimension/role;
- State/version;
- temporal position;
- granularity;
- directness;
- epistemic status.

Только после этого может оцениваться реальное противоречие.

---

# 75. Missing Relation ≠ Conflict

Open-world semantics применяются и к Provenance.

Отсутствие связи в одном графе не означает отрицание этой связи.

Дополнительная связь в другой модели также не означает конфликт автоматически.

---

# 76. Provenance Closure

Система MAY утверждать полноту Provenance только относительно явно определённого Scope.

Например:

> complete operational history since import into repository

не означает:

> complete historical provenance of content.

Closure MUST быть scoped.

---

# 77. Earliest Recorded Root

Корневой узел известного provenance graph не обязан быть реальным origin.

> graph root ≠ actual origin automatically.

Это особенно важно для:

- древних текстов;
- устных традиций;
- утраченных источников;
- импортированных datasets;
- архивных объектов.

---

# 78. Provenance Cycles

Цикл в semantic derivation graph обычно является сильным сигналом проблемы.

Но необходимо различать:

- semantic derivation cycle;
- reference cycle;
- citation cycle;
- metadata self-reference;
- audit-log self-recording.

Они не эквивалентны.

Validator SHOULD выявлять потенциально невозможные derivation cycles, но MUST NOT объявлять любой графовый цикл ошибкой происхождения.

---

# 79. Epistemic Cycles

Ацикличный Provenance graph не гарантирует корректность обоснования.

Например, Claim о происхождении может быть доказан Evidence, которое само зависит от предположения об этом происхождении.

Это epistemic dependency problem.

> acyclic provenance ≠ non-circular justification.

Такие случаи относятся к Evidence/Inference/Assessment architecture.

---

# 80. Provenance и Identity

Provenance не определяет Identity автоматически.

Два объекта могут:

- иметь общее происхождение, но быть разными;
- иметь одинаковое содержание, но разную историю;
- быть версиями одного объекта;
- быть независимыми объектами с одинаковым содержанием.

Следовательно:

> shared provenance ≠ same Identity.

> same content ≠ same Provenance.

---

# 81. Provenance и State

State и Provenance связаны, но не взаимозаменяемы.

State отвечает:

> каким был объект в определённом состоянии.

Provenance отвечает:

> как это состояние или содержание связано с предшествующей историей.

Provenance SHOULD ссылаться на конкретный State там, где изменение State меняет смысл происхождения.

---

# 82. Provenance и Scope

Scope определяет область применимости Claim.

Provenance определяет происхождение.

Они не должны смешиваться.

Но provenance relation сама MAY иметь Scope относительно части Target или условий применимости соответствующего provenance Claim.

Component binding при этом остаётся отдельным вопросом гранулярности Target/Input и MUST NOT автоматически считаться эквивалентным Scope.

---

# 83. Provenance и Context

Context MAY быть необходим для правильной интерпретации происхождения.

Например, одна и та же операция может иметь разные значения в:

- software;
- manuscript studies;
- archaeology;
- datasets;
- scientific measurement.

Контекст не должен стираться при переносе Provenance между Profiles.

---

# 84. Provenance и Assessment

Assessment MAY оценивать:

- достоверность provenance Claim;
- completeness;
- consistency;
- fidelity;
- directness;
- independence implications;
- authenticity implications;
- reconstruction quality.

Но Provenance сам не содержит автоматической оценки качества.

---

# 85. Provenance и Authenticity

Происхождение может быть Evidence для подлинности.

Но:

> known provenance ≠ authentic automatically.

И:

> incomplete provenance ≠ fake automatically.

Authenticity требует отдельного Assessment.

---

# 86. Provenance и Reliability

Длинная цепочка происхождения не означает низкую надёжность автоматически.

Короткая цепочка не означает высокую надёжность.

Derivative Source может быть единственным сохранившимся свидетельством утраченного оригинала.

Provenance не является рейтингом доверия.

---

# 87. Provenance и Truth

Идеально сохранённая линия происхождения может вести к ложному Claim.

И неизвестное происхождение может сопровождать истинный Claim.

Поэтому:

> provenance quality ≠ truth.

---

# 88. Provenance и Responsibility

Факт участия Agent в операции не устанавливает автоматически:

- юридическую ответственность;
- авторство;
- владение;
- права;
- намерение;
- одобрение результата.

Эти отношения требуют собственной семантики.

---

# 89. Restricted Provenance

Некоторая информация о происхождении может быть известна системе, но недоступна конкретному пользователю или публичному изданию.

Следует различать:

- unknown;
- known but restricted;
- redacted;
- not recorded;
- lost.

Restricted provenance MUST NOT отображаться как будто происхождение неизвестно, если политика позволяет сообщить хотя бы факт ограничения.

---

# 90. Privacy и Minimality

Требование сохранять Provenance не означает требование хранить неограниченную историю персональной активности.

Provenance SHOULD соблюдать:

- materiality;
- data minimization;
- privacy;
- access restrictions;
- applicable governance rules.

Если персональные данные не нужны для проверки происхождения, они SHOULD NOT сохраняться только ради максимальной детализации.

---

# 91. Tombstones

Если lineage-critical Target удалён или недоступен, система SHOULD, где возможно и допустимо, сохранять минимальную разрешимую ссылку или tombstone.

Tombstone MAY содержать:

- stable identifier;
- object type;
- historical label;
- deletion/withdrawal status;
- minimal temporal information;
- reason for unavailability, если допустимо.

Tombstone не должен восстанавливать удалённые данные вопреки требованиям privacy или governance.

---

# 92. Offline Provenance

Критически важная Provenance information должна оставаться понятной без доступа к:

- API;
- database;
- graph viewer;
- external resolver;
- internet;
- proprietary platform.

Для материально значимых случаев offline representation SHOULD позволять понять:

- что является Target;
- откуда оно происходит;
- является ли связь прямой или косвенной;
- какой тип преобразования известен;
- какой Source/State/version использовался;
- существуют ли gaps;
- существуют ли competing hypotheses;
- какая часть Target затронута.

---

# 93. Offline Source Binding

Для изменяемых источников простой URL недостаточен.

Где материально, offline export SHOULD сохранять человекочитаемую идентификацию фактически использованного Source/State.

Например:

- Source title;
- edition/version;
- date;
- fragment/page;
- stable identifier;
- snapshot reference

в той степени, в которой это доступно.

---

# 94. Offline Snapshot Semantics

Печатное или offline издание является историческим snapshot.

Если Provenance позже уточнён, старое издание не становится ложной записью о том, что система знала на момент публикации.

Где материально, export SHOULD позволять определить:

> provenance state/version as of publication/export time.

---

# 95. Provenance Compression

Для человекочитаемого представления полный граф MAY быть сокращён.

Например:

> Sources B–F share ancestor A.

Но compression MUST NOT создавать ложную:

- directness;
- authorship;
- independence;
- operation type;
- completeness.

Display summary MAY быть проще сохранённой семантической модели.

---

# 96. Provenance Fidelity

При копировании, экспорте, печати, миграции или преобразовании Provenance следует оценивать, сохранились ли материально важные lineage semantics.

Provenance Fidelity может быть снижена, если потеряны:

- directness;
- operation type;
- input roles;
- component binding;
- version binding;
- uncertainty;
- competing hypotheses;
- temporal semantics;
- provenance dimension;
- provenance status.

---

# 97. Минимальная структура Provenance

Минимальное представление Provenance SHOULD позволять, где применимо, выразить:

- Target;
- Predecessor/Input;
- Relation or Operation;
- Directness;
- Target component/scope;
- Input component/scope;
- State/version binding;
- Time or ordering;
- Agent/role;
- Epistemic status where applicable;
- Uncertainty;
- Source of provenance assertion.

Не каждое поле обязательно в каждом случае.

Неизвестные поля MUST оставаться неизвестными.

Epistemic status особенно применим к asserted, reported, imported, inferred и reconstructed Provenance.

Для непосредственно зарегистрированного Operational Provenance отсутствие отдельного Claim-level epistemic status допустимо, если это не уничтожает материально значимую информацию.

---

# 98. Qualified Provenance

Простой бинарной связи:

> B derived-from A

может быть недостаточно.

Provenance relation MAY требовать квалификаторов:

- Target;
- Input(s);
- Operation;
- Input role;
- Target component;
- Input component;
- State;
- Time;
- Agent;
- Method;
- Directness;
- Uncertainty;
- Assertion status.

Это не требует создания отдельной фундаментальной Core Entity для каждого Provenance edge.

Система SHOULD использовать существующие механизмы Relations, Claims, Events, Actions, States и Profiles.

---

# 99. Entity Discipline

Настоящий стандарт не вводит автоматически новые фундаментальные Core Entities:

- ProvenanceEdge;
- Lineage;
- Transformation;
- Contribution;
- LineageHypothesis;
- ProvenanceAssertion

как обязательные сущности.

Они MAY существовать как:

- Relations;
- qualified Relations;
- Claims;
- Events;
- Actions;
- Records;
- profile-level structures

в зависимости от требуемой семантики.

Новая Core Entity вводится только если существующая архитектура принципиально не способна сохранить необходимое различие.

---

# 100. Validation

Validator MAY проверять:

- broken references;
- impossible direct self-derivation;
- suspicious derivation cycles;
- missing State binding;
- incompatible temporal ordering;
- unresolved operation type;
- unsupported relation type;
- loss of component scope;
- lossy mapping;
- ambiguous directness;
- merge lineage loss;
- missing input roles;
- impossible version references;
- lineage claims represented as operational facts;
- prohibited automatic independence inference;
- invalid propagation of Record provenance to all components.

Validator MUST NOT автоматически исправлять исторические или эпистемические неопределённости.

---

# 101. Diagnostic Warnings

Система SHOULD уметь предупреждать о случаях:

- citation treated as provenance;
- bibliography treated as ancestry;
- uploader treated as author;
- record creator treated as content author;
- earliest known treated as original;
- URL treated as immutable source;
- version order treated as derivation;
- shared Event treated as common provenance;
- no common lineage treated as independent Evidence;
- common lineage treated as total dependence;
- record provenance propagated to every Claim;
- transitive ancestor treated as direct source;
- inferred lineage treated as operational fact;
- lossy provenance mapping hidden;
- ambiguous provenance language over-normalized.

---

# 102. Запрещённые упрощения

Система MUST NOT автоматически считать:

> citation → derivation

> same bibliography → common provenance

> same Event observed → common provenance

> same author → common provenance

> same tool → common content provenance

> same wording → common provenance

> different wording → independent provenance

> earliest known → original

> no known predecessor → independent creation

> version 2 → derived from version 1

> upload time → creation time

> file creator → content author

> common provenance → unreliable

> unknown provenance → unreliable

> complete provenance → true

> provenance graph → Evidence dependency graph

---

# 103. Natural-Language Safety

При извлечении Provenance из естественного языка система должна предпочитать сохранение исходной неопределённости ложной структурной точности.

Например:

> «текст основан на древних источниках»

не должен автоматически становиться:

> directly copied from Source X

без дополнительного основания.

При необходимости исходная формулировка MAY сохраняться вместе со структурированной интерпретацией.

---

# 104. High-Risk Knowledge

Для знаний с высоким риском ошибки Provenance SHOULD сохраняться подробнее.

Особенно для:

- медицины;
- воды;
- пищи;
- токсикологии;
- химии;
- электричества;
- строительства;
- аварийных процедур;
- идентификации опасных организмов;
- дозировок;
- критических измерений.

Материально важными могут быть:

- exact Source;
- version;
- procedure;
- transformation;
- translation;
- adaptation;
- dataset;
- calculation lineage;
- known gaps.

---

# 105. Historical Knowledge

Для исторических материалов система SHOULD особенно защищать различия:

- original;
- earliest known;
- oldest surviving;
- copy;
- translation;
- edition;
- reconstruction;
- reported attribution;
- inferred attribution;
- oral predecessor;
- unknown predecessor.

Историческая миссия проекта несовместима с превращением «самого раннего найденного» в «первоначальное».

---

# 106. Provenance Profiles

Domain Profile MAY устанавливать дополнительные требования.

Например:

## Manuscript Profile

может требовать:

- witness;
- copy relationship;
- fragment;
- edition;
- reconstruction;
- scribal intervention.

## Dataset Profile

может требовать:

- source dataset;
- row/field provenance;
- transformation;
- merge;
- filter;
- calculation.

## Software Profile

может требовать:

- repository;
- commit;
- build;
- dependency;
- toolchain.

## Physical Sample Profile

может требовать:

- collection;
- split;
- merge;
- storage;
- transport;
- contamination;
- measurement chain.

Core определяет общие инварианты, а не полную предметную модель каждого домена.

---

# 107. Group Provenance

Для больших datasets или составных объектов MAY использоваться Provenance групп.

Например:

> rows 1–10000 derived from Dataset A  
> except rows 531–547 derived from Dataset B.

Это позволяет сохранять достаточную детализацию без создания миллионов отдельных объектов.

---

# 108. Inheritance и Overrides

Profile MAY позволять наследование Provenance от контейнера или группы.

Но локальное происхождение MUST иметь возможность переопределить унаследованное.

Правило:

> inherited provenance is a default, not an irreversible fact.

---

# 109. Provenance Purpose

Один и тот же объект может требовать разных представлений Provenance для разных задач:

- историческая передача;
- Evidence independence;
- reproducibility;
- authorship;
- physical custody;
- software processing;
- legal traceability.

Это не означает, что истина о происхождении относительна.

Это означает, что разные задачи выделяют разные материальные аспекты одной истории.

---

# 110. Provenance Views

Система MAY создавать разные views одного Provenance graph.

Например:

- content lineage view;
- physical custody view;
- execution view;
- Evidence-dependency-oriented view.

View MUST NOT выдавать себя за полный Provenance, если показывает только часть.

---

# 111. Independence Reassessment

Если позже обнаружен общий источник или посредник, текущая оценка независимости Evidence MAY измениться.

Но исторические Assessments MUST сохраняться как исторические состояния.

Например:

> Assessment 2026: Sources considered independent.  
> Provenance discovery 2028: common witness identified.  
> Assessment 2028: independence reduced.

Система MUST NOT переписывать Assessment 2026 так, словно common witness был известен тогда.

---

# 112. Provenance Uncertainty

Неопределённость MAY относиться к:

- existence of relation;
- relation type;
- directness;
- predecessor identity;
- operation time;
- Agent;
- component scope;
- transformation fidelity;
- number of intermediaries.

Эти виды неопределённости SHOULD оставаться различимыми там, где это материально.

---

# 113. Negative Provenance Claims

Утверждения вроде:

> B was not copied from A

являются Claims и требуют основания.

Отсутствие положительной provenance edge не означает отрицательной provenance relation.

Open-world semantics сохраняются.

---

# 114. Provenance Closure Claims

Утверждение:

> no other ancestors exist

сильнее, чем:

> no other ancestors are currently known.

Первое требует явного основания и Scope closure.

По умолчанию система SHOULD предпочитать вторую интерпретацию.

---

# 115. Minimality

Provenance SHOULD быть настолько подробным, насколько необходимо для сохранения материальных различий, но не подробнее без причины.

Цель:

> maximum semantic preservation with minimum unnecessary structural complexity.

---

# 116. Human Readability

Даже при машинной структуре Provenance должен быть переводим в понятную человеку форму.

Например:

> Этот текст является русским переводом версии 3 документа X.  
> Перевод выполнен в 2026 году.  
> Разделы 4–6 дополнительно адаптированы редактором.  
> Происхождение исходного документа до версии 1 неизвестно.

Такое представление предпочтительнее непрозрачного графа идентификаторов при offline использовании.

---

# 117. Основные инварианты

### P-01
represented provenance ≠ actual lineage automatically

### P-02
operational provenance ≠ represented historical provenance

### P-03
Provenance Claim remains epistemically assessable

### P-04
record provenance ≠ provenance of every component automatically

### P-05
provenance dimensions MUST NOT be silently collapsed

### P-06
generic ancestry ≠ specific operation

### P-07
indirect ancestry ≠ direct provenance

### P-08
multi-input operation ≠ independent pairwise edges automatically

### P-09
joint input semantics MUST remain preservable where material

### P-10
intended transformation ≠ actual transformation

### P-11
operation execution ≠ operation success

### P-12
textual change magnitude ≠ semantic change magnitude

### P-13
complete provenance ≠ reproducibility

### P-14
reproducibility ≠ complete provenance

### P-15
uploader / operator / scanner ≠ content author automatically

### P-16
citation ≠ provenance proof

### P-17
bibliography ≠ ancestry

### P-18
influence ≠ derivation automatically

### P-19
same observed Event ≠ common provenance

### P-20
same tool/method ≠ common content provenance automatically

### P-21
Provenance graph ≠ Evidence dependency graph

### P-22
provenance independence ≠ evidential independence

### P-23
no known common provenance ≠ independent Evidence

### P-24
common provenance ≠ complete evidential dependence

### P-25
physical provenance ≠ content provenance

### P-26
world causality ≠ provenance ancestry automatically

### P-27
location identifier ≠ immutable content identity

### P-28
version order ≠ derivation order automatically

### P-29
earliest known ≠ origin

### P-30
graph root ≠ actual origin

### P-31
unknown provenance MUST remain representable

### P-32
unknown ≠ unrecorded ≠ restricted ≠ redacted ≠ lost

### P-33
actual lineage ≠ knowledge about lineage at time T

### P-34
new provenance knowledge MUST NOT rewrite historical epistemic state

### P-35
imported provenance ≠ internally established provenance automatically

### P-36
lossy provenance mapping MUST remain detectable

### P-37
different provenance granularity ≠ conflict automatically

### P-38
provenance conflict requires semantic alignment

### P-39
missing provenance edge ≠ negative provenance claim

### P-40
provenance completeness requires explicit closure Scope

### P-41
derivation cycle ≠ every reference cycle

### P-42
acyclic provenance ≠ valid justification automatically

### P-43
shared provenance ≠ same Identity

### P-44
same content ≠ same Provenance

### P-45
known provenance ≠ authenticity automatically

### P-46
known provenance ≠ reliability automatically

### P-47
provenance quality ≠ truth

### P-48
natural-language ambiguity MUST NOT become invented provenance certainty

### P-49
training inclusion ≠ specific AI output derivation

### P-50
projected provenance ≠ complete provenance automatically

### P-51
component binding ≠ Scope qualification automatically

### P-52
authorship/contribution provenance ≠ complete authorship semantics

### P-53
operational provenance MUST NOT require artificial epistemic status where no material epistemic distinction exists

---

# 118. Архитектурный принцип

Provenance не должен становиться отдельной параллельной онтологией проекта.

Он использует уже существующие архитектурные механизмы:

- Entity;
- Claim;
- Relation;
- Source;
- Evidence;
- Scope;
- Context;
- State;
- Event;
- Action;
- Assessment;
- Profile

где это соответствует их семантике.

Provenance определяет правила их использования для представления происхождения.

---

# 119. Критерий достаточности

Provenance representation считается структурно достаточным, если для требуемого Profile и Risk можно восстановить материально значимые ответы на вопросы:

- WHAT is the target?
- WHAT did it materially originate from?
- WHICH part originated from which input?
- HOW was it transformed?
- WAS the relation direct or indirect?
- WHICH State/version was used?
- WHEN did the relevant operation occur, if known and material?
- WHO or WHAT performed the operation, if known and material?
- HOW is this provenance known?
- WHAT remains uncertain or unknown?
- ARE there competing lineage hypotheses?
- HAS material provenance information been lost during mapping/export?

Не каждый вопрос обязан иметь известный ответ.

Неизвестность является допустимым результатом.

---

# 120. Итоговая формула

> Provenance  
> = target-relative  
> + role-qualified  
> + state/version-aware  
> + component-capable  
> + multi-input-capable  
> + temporally preservable  
> + epistemically explicit where applicable  
> + uncertainty-preserving  
> + open-world  
> + offline-survivable  
> representation of materially relevant lineage.

При этом:

> represented lineage ≠ actual lineage automatically

> Provenance ≠ Truth

> Provenance ≠ Reliability

> Provenance ≠ Evidence

> Provenance ≠ Evidence independence

> Provenance ≠ Identity

> Provenance ≠ State

> Provenance ≠ Authorship

> Provenance ≠ World causality

---

# 121. Критерий успеха стандарта

Стандарт выполняет свою задачу, если система способна сохранить происхождение знания так, чтобы спустя годы — в другой базе, другом программном обеспечении или на бумаге — человек мог отличить:

- оригинал от известной копии;
- прямой источник от косвенного;
- перевод от исходного текста;
- реконструкцию от сохранившегося оригинала;
- общий информационный источник от независимого наблюдения;
- происхождение Record от происхождения отдельного Claim;
- совместный synthesis от независимых derivation edges;
- известную линию происхождения от предполагаемой;
- неизвестную линию от утраченной или скрытой;
- нынешнее знание о происхождении от того, что было известно раньше;
- реальную сохранённую семантику от потерянной при миграции;
- component binding от Scope qualification;
- provenance-релевантный вклад от полной модели авторства;
- Provenance от Evidence, Truth, Reliability, Identity и Assessment.

И при этом система не должна изобретать происхождение там, где оно неизвестно.

---

Конец документа.
