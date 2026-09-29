# 012 — PROCESS
## Стандарт представления процессов

**Проект:** Энциклопедия цивилизации  
**Статус:** зафиксированный рабочий стандарт  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляются Процессы — протяжённые во времени проявления, деятельности, динамика, преобразования, взаимодействия, поддержание, циклы, прогрессии и иная процессная семантика, разворачивающиеся или поддерживаемые во времени.

Цель стандарта — позволить сохранять:

- какой Процесс представлен;
- является ли представление типом Процесса, моделью Процесса или конкретным проявлением Процесса;
- в какой рамке участников происходит конкретное проявление Процесса;
- какие субъекты, системы, популяции, среды, отношения или участники вовлечены;
- в каком Контексте представлен Процесс;
- когда Процесс происходит настолько, насколько это установимо;
- какова известная временная структура Процесса;
- какие Состояния связаны с Процессом;
- какие События связаны с его границами, фазами или внутренними проявлениями;
- какие Действия связаны с Процессом;
- какие входы, выходы, ресурсы или условия существенно значимы;
- какие фазы, стадии или подпроцессы представлены;
- является ли Процесс непрерывным, прерывистым, циклическим, повторяющимся или иным образом структурированным;
- насколько известна его внутренняя динамика;
- насколько известен механизм;
- является ли Процесс наблюдаемым, измеренным, вычисленным, выведенным, смоделированным или реконструированным;
- какие существуют неопределённость и происхождение;
- какие причинные или механистические связи атрибутируются;
- какие исторические представления или версии Процесса существовали.

Стандарт не предназначен для автоматического определения:

- причины Процесса;
- полного механизма;
- внутренней динамики;
- Агента;
- намерения;
- цели или назначения;
- Objective;
- ответственности;
- эффективности;
- успешности;
- желательности;
- статуса Результата;
- достижения Цели;
- полного разложения на фазы;
- того, что Процесс обязательно имеет одного субъекта;
- того, что Процесс обязательно имеет чёткое физическое начало/конец;
- того, что Процесс обязан состоять из дискретных Событий;
- того, что Процесс обязан иметь единственно правильную декомпозицию;
- того, что наблюдаемое направление или конечную точку являются inherent цели или назначения;
- того, что Процесс будет продолжаться в будущем.

Сохранить Процесс означает сохранить максимально честное представление о **протяжённого во времени проявления Процесса или динамики**, не превращая временную последовательность в причинность, последовательность Состояний — в полный Процесс, границу Процесса — в Событие автоматически, модель Процесса — в конкретное проявление Процесса, а наблюдаемую прогрессию — в внутреннее назначение.

---

# 1. Основное понятие

## 1.1. Process

**Process (Процесс)** — семантическая конструкция, представляющая протяжённое во времени проявление, деятельность, динамику, преобразование, взаимодействие, поддержание, прогрессию, цикл или другую семантику процесса.

Процесс отвечает на основной вопрос:

> **Что и каким образом разворачивается, продолжается, взаимодействует, преобразуется или поддерживается во времени?**

Процесс МОЖЕТ быть:

- физическим;
- биологическим;
- химическим;
- техническим;
- вычислительным;
- институциональным;
- социальным;
- экологическим;
- информационным;
- экономическим;
- распределённым;
- реляционным;
- иным предметно-специфическим процессом.

Процесс не требует наблюдаемого суммарного изменения.

Например:

    heating

может изменять Состояние.

Но:

    temperature regulation

МОЖЕТ поддерживать приблизительно постоянное Состояние.

---

# 2. Process representation ≠ Process truth

Процесс является представлением знания, а не автоматическим доказательством объективной исторической реальности.

Следовательно:

    Process representation exists
    ≠ Процесс действительно произошёл именно так, как представлен

Процесс МОЖЕТ быть:

- observed;
- measured;
- inferred;
- reconstructed;
- computed;
- modeled;
- hypothesized;
- partially known;
- disputed.

Эпистемический статус ДОЛЖЕН оставаться разрешимым, когда это существенно для смысла.

---

# 3. Process как семантическая конструкция

Процесс не обязан всегда существовать как отдельная фундаментальная Сущность.

Процесс МОЖЕТ быть представлен через:

- специализированную Запись;
- временную структуру;
- отношения;
- историю Состояний;
- отношения с Событиями;
- временные ряды;
- модель;
- граф;
- другое подходящее представление.

Если существенно важны независимая идентичность, происхождение, повторное использование, декомпозиция или историческое отслеживание, Процесс МОЖЕТ быть материализован как отдельная Запись.

Следовательно:

    семантика Процесса
    ≠ обязательная Сущность Процесса

---

# 4. Process type ≠ Process model ≠ Process occurrence

Необходимо различать три уровня:

    Process type
    ≠ Process model
    ≠ Process occurrence

**Process type** — повторно используемая общая категория/вид Процесса.

Например:

    fermentation
    photosynthesis
    erosion

**Process model** — представление того, как тип Процесса или конкретное проявление Процесса может протекать, изменяться или быть объяснено.

Например:

    kinetic model of fermentation

**Process occurrence** — конкретный Процесс, представленный как происходящий или происходивший в определённой рамке.

Например:

    fermentation of Batch 24
    during interval T1–T2

Модель Процесса МОЖЕТ представлять:

- Process type;
- Process occurrence;
- оба на разных уровнях абстракции.

Но:

    Идентичность модели
    ≠ идентичность представленного Процесса

И:

    Process type exists
    ≠ Process occurrence exists

И:

    Process model exists
    ≠ Process occurrence proven

---

# 5. Process Content ≠ Process type automatically

**Process Content** представляет семантику конкретного представления Процесса.

**Process type** представляет повторно используемую классификацию/общий вид.

Следовательно:

    Process Content
    ≠ Process type automatically

Конкретное проявление Процесса МОЖЕТ иметь определённое Process Content без формально назначенного типа Процесса.

И наоборот:

    Process type
    ≠ свидетельство конкретного проявления

---

# 6. Generic Process knowledge ≠ historical occurrence

Общее знание:

    iron corrodes under certain conditions

не означает автоматически:

    this historical iron object
    corroded through exactly that mechanism

в конкретном историческом случае.

Следовательно:

    generic Process knowledge
    ≠ историческое свидетельство конкретного проявления

Перенос от общего типа/модели Процесса к конкретному проявлению требует:

- Evidence;
- Inference;
- применения модели;
- другой обоснованной семантики.

---

# 7. Не каждая временная последовательность является Процессом

Sequence:

    Event A
    then Event B

не означает автоматически:

    Process P

Likewise:

    State S1
    State S2
    State S3

не является Процессом автоматически.

Представление Процесса уместно, когда существенно присутствует процессная временная семантика:

- activity;
- dynamics;
- progression;
- transformation;
- maintenance;
- interaction;
- recurrence;
- cycle;
- другое протяжённое во времени поведение.

Следовательно:

    temporal sequence
    ≠ Process automatically

---

# 8. Минимальная структура Процесса

Для завершённой семантики конкретного проявления Процесса необходимо как минимум:

1. определённое содержание Процесса;
2. разрешимую рамку участников;
3. достаточное семантическое отнесение Процесса;
4. разрешимую временную/процессную рамку.

Минимальная формула:

    определённое содержание Процесса
    +
    разрешимую рамку участников
    +
    достаточное семантическое отнесение Процесса
    +
    разрешимую временную/процессную рамку

Точные временные метки начала/конца не являются универсальным требованием.

Тип Процесса или модель Процесса МОГУТ иметь другую структуру представления и не обязаны удовлетворять требованиям для конкретного проявления без соответствующей роли проявления.

---

# 9. Process Content

**Process Content** — содержание, представляющее процессное проявление/динамику в конкретном представлении.

Process Content МОЖЕТ включать:

- transformation;
- progression;
- maintenance;
- interaction;
- circulation;
- diffusion;
- growth;
- decay;
- movement;
- computation;
- synchronization;
- institutional review;
- feedback-related behavior;
- oscillation;
- cycle;
- repeated activity;
- other семантику процесса.

Process Content не требует отдельной фундаментальной Сущности.

---

# 10. Participating frame

Конкретное проявление Процесса не требует одного привилегированного субъекта.

**Participating frame** — разрешимая рамка, определяющая то, в чём, между чем или относительно чего Процесс происходит.

Она МОЖЕТ включать:

- one subject;
- multiple subjects;
- system;
- subsystem;
- population;
- environment;
- territory;
- network;
- relation;
- field;
- institution;
- interacting participants;
- other domain frame.

Например:

    heat exchange between Body A and Body B

не требует выбора одного тела как единственного субъекта Процесса.

Likewise:

    migration between Regions A and B

МОЖЕТ иметь распределённую рамку участников.

---

# 11. Participating frame ≠ Context

Необходимо различать:

    Participating frame
    ≠ Context automatically

**Participating frame** отвечает:

> Что участвует в Процессе, несёт Процесс или образует отношение Процесса?

**Context** отвечает:

> При каких обстоятельствах, условиях или внешней рамке представлен Процесс?

Например:

    fermentation of Batch X
    in Vessel V
    at 25°C

МОЖЕТ быть представлено как:

    participating frame:
    Batch X + Vessel V

    Context:
    temperature = 25°C

Один и тот же объект/условие МОЖЕТ занимать разные семантические роли в разных представлениях.

Но различие ролей ДОЛЖНО оставаться разрешимым, когда это существенно для смысла.

---

# 12. Multi-participant Process

Процесс МОЖЕТ быть изначально реляционным или распределённым.

Например:

    trade between regions

    heat exchange

    ecosystem interaction

    network synchronization

Core MUST NOT force:

    one Process
    → one privileged subject

Роли участников ДОЛЖНЫ оставаться разрешимыми, когда это существенно для смысла.

---

# 13. Process attribution

**Process attribution** — семантика, связывающая Process Content с рамкой участников и применимой временной/процессной рамкой.

Она является семантическим требованием.

Она МОЖЕТ быть выражена через:

- structure;
- отношения;
- fields;
- граф;
- temporal representation;
- embedded модель;
- other implementation.

Но:

    Process attribution
    ≠ mandatory dedicated field
    ≠ mandatory Core Entity

---

# 14. Process ≠ Claim

Claim отвечает:

> Что утверждается?

Процесс отвечает:

> Какой Процесс представлен как происходящий/происходивший?

Следовательно:

    Claim about Process
    ≠ Process

Например:

    Source states:
    corrosion progressed rapidly

является Claim.

Представление Процесса МОЖЕТ отдельно представлять:

    corrosion Process
    involving Object X
    during Frame T

Но:

    Process representation exists
    ≠ Claim proven

---

# 15. Известность существования Процесса ≠ известность его внутренней динамики

Фундаментальное правило:

    Process existence known
    ≠ известной внутренней динамики

Например:

    construction continued for 40 years

может быть известно, даже если неизвестны:

- internal stages;
- day-to-day progression;
- mechanism;
- exact workforce;
- intermediate States;
- exact trajectory.

Следовательно:

    Process known
    ≠ Process fully characterized

---

# 16. Known Process ≠ known mechanism

Процесс МОЖЕТ быть хорошо установлен, тогда как механизм остаётся:

- unknown;
- partial;
- disputed;
- modeled;
- inferred.

Следовательно:

    Process observed
    ≠ mechanism known

И:

    mechanism model exists
    ≠ mechanism historically occurred exactly as modeled

---

# 17. Process ≠ Event

Событие отвечает:

> Что произошло / какое проявление или какая граница возникли?

Процесс отвечает:

> Как протяжённая во времени динамика/деятельность разворачивается?

Например:

    Event:
    fire started

    Process:
    fire spreading

Следовательно:

    Event
    ≠ Process

---

# 18. Duration ≠ Event/Process classification

Большая длительность не делает явление Процессом автоматически.

Малая длительность не делает явление Событием автоматически.

Следовательно:

    duration alone
    ≠ Event/Process classification

Semantic function determines representation.

---

# 19. Process boundary ≠ Event automatically

Начало или конец Процесса МОГУТ быть:

- physical occurrence;
- conventional boundary;
- threshold-defined boundary;
- analytical boundary;
- model-defined boundary;
- fuzzy boundary;
- inferred boundary;
- unknown boundary.

Следовательно:

    граница Процесса
    ≠ Событие автоматически

Начало/конец Процесса МОГУТ быть представлены как Событие только при независимом обосновании семантики События.

---

# 20. Process start

Начало Процесса МОЖЕТ быть:

- exact;
- approximate;
- inferred;
- threshold-defined;
- model-relative;
- fuzzy;
- unknown.

Например:

    corrosion began before inspection

не означает:

    corrosion began at inspection

Beginning of observation:

    ≠ Process beginning automatically

---

# 21. Process end

Конец Процесса МОЖЕТ быть:

- exact;
- approximate;
- inferred;
- conventional;
- threshold-defined;
- unknown;
- open-ended.

End of observation:

    ≠ Process end automatically

Unknown end:

    ≠ permanent continuation

---

# 22. Observation boundary ≠ Process boundary

Если Процесс наблюдался от T1 до T2:

    observation began at T1
    ≠ Process began at T1

И:

    observation ended at T2
    ≠ Process ended at T2

Окно наблюдения ДОЛЖНО оставаться отличимым от временной протяжённости Процесса, когда это существенно.

---

# 23. Event inside Process

Процесс МОЖЕТ иметь События.

Например:

    Process:
    fermentation

может быть связан с:

    Event:
    threshold reached

или:

    Event:
    vessel ruptured

Но:

    Event occurring during Process
    ≠ subprocess automatically

И:

    Event part of narrative
    ≠ Process identity

---

# 24. Процесс без дискретных Событий

Непрерывный Процесс МОЖЕТ не иметь полезной дискретной декомпозиции на События.

Например:

    diffusion

    gradual cooling

    erosion

Ядро НЕ ДОЛЖНО требовать:

    Process
    → sequence of Events

---

# 25. Event ≠ full Process explanation

Known Event:

    engine stopped

не означает, что известен:

- failure Process;
- внутренней динамики;
- mechanism;
- complete causal history.

Следовательно:

    Event known
    ≠ Process known

---

# 26. Phase boundary ≠ Event automatically

Переход фазы Процесса МОЖЕТ быть:

- threshold-defined;
- model-defined;
- conventional;
- gradual;
- fuzzy;
- analytical.

Следовательно:

    Phase boundary
    ≠ Event automatically

Example:

    childhood → adolescence

не требует одного дискретного События перехода.

---

# 27. Process ≠ State

Состояние отвечает:

> Каким представлен объект или конфигурация в рамке?

Процесс отвечает:

> Как протяжённая во времени деятельность/динамика разворачивается или поддерживается?

Например:

    State:
    water temperature = 80°C

    Process:
    water heating

Следовательно:

    State
    ≠ Process

---

# 28. State sequence ≠ Process

Sequence:

    S1 @ T1
    S2 @ T2
    S3 @ T3

MAY support Process Inference.

Но сама последовательность НЕ ДОЛЖНА автоматически определять:

- Process identity;
- continuity;
- mechanism;
- causality;
- intermediate dynamics.

---

# 29. Process MAY maintain State

Процесс не обязательно изменяет макросостояние.

Например:

    regulatory Process

может поддерживать:

    temperature ≈ constant

Likewise:

    metabolism

может поддерживать:

    organism alive

Следовательно:

    Process
    ≠ mandatory net State change

---

# 30. Steady State with ongoing Process

Stable/steady State MAY coexist with active internal Process.

Например:

    tank level constant

при:

    inflow active
    outflow active

Следовательно:

    no net State change
    ≠ no Process

---

# 31. Process ≠ Action

Действие отвечает:

> Что было сделано?

Процесс отвечает:

> Как разворачивалась деятельность/динамика?

Например:

    Action:
    operator opened valve

    Process:
    fluid flowing

Следовательно:

    Action
    ≠ Process

---

# 32. Activity boundary

`Activity` является пограничным понятием.

Целенаправленная или агентная Activity МОЖЕТ содержать:

- Action semantics;
- семантика Процесса;
- both.

Например:

    person walking

MAY be represented as:

- Action;
- Process;
- Activity-related semantics;

depending on purpose.

Внешняя метка `Activity` не определяет онтологию автоматически.

`012` не определяет полную онтологию `Activity`.

---

# 33. Action-generated Process

Действие МОЖЕТ быть связано с началом, изменением или поддержанием Процесса.

Например:

    Action:
    ignite burner

    Process:
    combustion

Но:

    Action occurred
    ≠ Process necessarily occurred

И:

    Process occurred
    ≠ Action caused it automatically

Causal relation требует independent attribution.

---

# 34. Process without Actor

Процесс МОЖЕТ не иметь Агента.

Examples:

- erosion;
- diffusion;
- evaporation;
- tectonic movement;
- biological evolution.

Следовательно:

    no Actor
    ≠ incomplete Process

---

# 35. Process ≠ Result

Process MAY participate in Result semantics relative to a frame.

Но:

    Process
    ≠ Result intrinsically

Семантика роли Результата определяется `010-RESULT`.

---

# 36. Process ≠ Objective

Цель МОЖЕТ задавать желаемое поведение Процесса.

Например:

    maintain fermentation for 24h

Но:

    desired Process
    ≠ actual Process

Objective role MUST remain distinct.

---

# 37. Anti-teleology principle

Наблюдаемые направление Процесса, прогрессия, адаптация, регулярность или конечная точка НЕ ДОЛЖНЫ автоматически интерпретироваться как внутренняя Цель, намерение или назначение.

Следовательно:

    Process direction
    ≠ внутреннее назначение автоматически

    Process endpoint
    ≠ intended destination automatically

    adaptation
    ≠ intention automatically

Траектория Процесса НЕ ДОЛЖНА преобразовываться в телеологическую семантику без независимого обоснования.

Это особенно важно для:

- biological Processes;
- evolution;
- historical Processes;
- social Processes;
- ecological Processes;
- institutional development.

---

# 38. Process ≠ Procedure

Procedure отвечает:

> Как prescribed действия должны выполняться?

Процесс отвечает:

> Что фактически разворачивается или представляется как разворачивающееся?

Например:

    Procedure:
    fermentation protocol

    Process:
    actual fermentation

Следовательно:

    Procedure
    ≠ Process

---

# 39. Workflow definition ≠ Process execution

Workflow definition MAY specify:

- stages;
- transitions;
- responsibilities;
- allowed paths.

Actual institutional/technical execution MAY form Process occurrence.

Но:

    workflow definition
    ≠ actual Process execution

---

# 40. Process ≠ Mechanism model

Mechanism model attempts to explain how Process works.

Process occurrence MAY be known without full mechanism.

Следовательно:

    Process occurrence
    ≠ mechanism model

И:

    mechanism model
    ≠ historical mechanism proof

---

# 41. Process mechanism

Mechanistic semantics MAY include:

- causal steps;
- intermediate States;
- interactions;
- transformations;
- feedback;
- flows.

Но `012` устанавливает границы семантики механизма, а не полную онтологию Механизма.

---

# 42. Temporal/process frame

Каждое конкретное проявление Процесса ДОЛЖНО иметь разрешимую временную/процессную рамку.

Frame MAY include:

- exact bounds;
- approximate bounds;
- open-ended duration;
- recurring windows;
- multiple temporal scales;
- phase frame;
- Context;
- system version;
- environmental conditions;
- domain semantics.

Exact timestamps are not universally required.

---

# 43. Multiple temporal scales

Process MAY have multiple materially relevant temporal scales simultaneously.

Например:

    climate Process:
    daily oscillation
    seasonal cycle
    multi-year trend

или:

    biological system:
    heartbeat scale
    respiratory scale
    metabolic scale

One temporal scale MUST NOT silently replace another.

---

# 44. Process duration

Duration MAY be:

- exact;
- estimated;
- approximate;
- unknown.

Duration MUST NOT automatically determine:

- Process identity;
- mechanism;
- phase structure;
- completion;
- Result;
- Effectiveness.

---

# 45. Open-ended Process

Process MAY have open-ended temporal representation.

Но:

    no recorded end
    ≠ Process currently ongoing automatically

И:

    open-ended
    ≠ infinite/permanent

Continuation requires Evidence, Inference or domain semantics.

---

# 46. Process continuity

Process MAY be:

- continuous;
- intermittent;
- episodic;
- cyclic;
- recurrent;
- interrupted;
- resumed;
- partially observed.

Core MUST NOT assume uninterrupted continuity.

---

# 47. Observation gap

If Process evidence is absent during interval:

    no observation
    ≠ Process stopped automatically

И:

    no observation
    ≠ Process continued automatically

Unknown interval remains unknown unless justified Inference exists.

---

# 48. Process interruption

Process MAY be interrupted.

Interruption MAY relate to:

- Event;
- Action;
- State;
- external Process;
- unknown occurrence.

Но:

    interruption
    ≠ termination automatically

---

# 49. Process resumption

Process MAY resume after interruption.

Но:

    resumed
    ≠ same Process identity automatically

Continuity/identity requires semantic justification.

---

# 50. Process identity

Identity/continuity of represented Process MAY depend on:

- participating frame;
- Process Content;
- temporal continuity;
- interruption/resumption semantics;
- Scope;
- Context;
- Profile;
- other materially relevant distinctions.

Process identity MUST NOT be established only from label or Content equality.

---

# 51. Same Process Content ≠ same Process

Например:

    heating Batch A on Monday
    heating Batch A on Tuesday

может быть двумя проявлениями Процесса.

Следовательно:

    same Process Content
    ≠ same Process identity automatically

---

# 52. Different descriptions ≠ different Process automatically

Например:

    wound healing

и:

    tissue repair

MAY describe:

- same Process;
- overlapping Process;
- different abstraction levels.

Different wording:

    ≠ different Process automatically

---

# 53. Process representation identity ≠ идентичность представленного Процесса

Необходимо различать:

    identity of Process representation
    ≠ identity/continuity of represented Process

Two independent Sources MAY represent one Process.

Следовательно:

    different provenance
    ≠ different Process automatically

---

# 54. Merge / split / branching

Processes MAY:

- merge;
- split;
- branch;
- converge;
- diverge.

Например:

    Process A ─┐
               ├→ Process C
    Process B ─┘

или:

    Process A
      ├→ Process B
      └→ Process C

Merge/split/branching MUST NOT automatically determine Process identity continuity.

Следовательно:

    successor after merge
    ≠ predecessor identity automatically

И:

    branch
    ≠ same Process continuation automatically

Identity relations require explicit semantics when material.

---

# 55. Process granularity

Process MAY be represented:

    digestion

or more finely:

    chewing
    gastric processing
    enzymatic breakdown
    absorption

Granularity depends on:

- цели или назначения;
- provenance;
- Profile;
- materially relevant distinctions.

---

# 56. Granularity ≠ identity

Purpose MAY alter representation/decomposition.

But MUST NOT invent:

- phases;
- mechanism;
- temporal continuity;
- causal отношения;
- participants;
- Scope;
- boundaries.

---

# 57. Composite Process

Process MAY include multiple interacting subprocess-like structures.

Example:

    ecosystem succession

MAY involve:

- plant growth;
- soil transformation;
- migration;
- nutrient cycling.

But:

    Composite Process
    ≠ complete decomposition automatically

---

# 58. Subprocess

A Process MAY have subprocess relation.

But:

    temporal containment
    ≠ subprocess automatically

A Process occurring entirely during another Process may simply overlap temporally.

Subprocess relation requires process-part semantics, not just time containment.

---

# 59. Temporal containment ≠ Process part-of

Fundamental distinction:

    P2 occurs during P1
    ≠ P2 is part of P1 automatically

Example:

    famine occurs during war

does not automatically mean:

    famine is subprocess of war

---

# 60. Process overlap ≠ part-of

Processes MAY overlap in time and Scope without hierarchy.

Thus:

    overlaps
    ≠ part-of

И:

    interacts-with
    ≠ part-of automatically

---

# 61. Process decomposition

Process MAY be decomposed by:

- phases;
- stages;
- subprocesses;
- mechanisms;
- functions;
- temporal segments;
- spatial regions.

No universal decomposition is required.

---

# 62. Multiple valid decompositions

One Process MAY admit several valid decompositions.

Например, биологический Процесс МОЖЕТ быть декомпозирован по:

- anatomical structures;
- chemical reactions;
- functional roles;
- temporal phases.

Different decompositions:

    ≠ contradiction automatically

---

# 63. Phase ≠ Process universally

Phase MAY represent:

- Process segment;
- State-like classification;
- analytical period;
- developmental frame.

External `phase` label MUST NOT determine ontology.

---

# 64. Stage ≠ Process universally

Stage MAY represent:

- Process segment;
- workflow stage;
- State classification;
- developmental State.

Semantic function determines mapping.

---

# 65. Process sequence

Процесс МОЖЕТ иметь упорядоченные компоненты.

But:

    order
    ≠ causality

Одна последовательность НЕ ДОЛЖНА становиться причинной цепью.

---

# 66. Process causality

Causal relations MAY occur within Process.

Но они НЕ ДОЛЖНЫ выводиться только из:

- temporal succession;
- proximity;
- repetition;
- correlation;
- phase ordering;
- narrative order.

---

# 67. Mechanistic relation provenance

Mechanistic or causal relation SHOULD preserve when materially relevant:

- provenance;
- uncertainty;
- assumptions;
- модель;
- Scope;
- Context;
- alternative explanations.

Mechanistic relation:

    ≠ unquestionable fact automatically

---

# 68. Observed pattern ≠ feedback mechanism

Observed oscillation, stabilization or recurrence MUST NOT automatically establish feedback loop.

Thus:

    observed pattern
    ≠ feedback mechanism automatically

Feedback MAY be:

- observed;
- inferred;
- modeled;
- hypothesized.

Status MUST remain resolvable when material.

---

# 69. Process input

Process MAY have inputs:

- material;
- energy;
- information;
- resources;
- participants;
- preconditions.

Input semantics is conditional.

It is NOT universal mandatory Process field.

---

# 70. Process output

Process MAY have outputs:

- State;
- Event;
- material;
- information;
- product;
- by-product;
- other phenomenon.

But:

    Process output
    ≠ Result intrinsically

И:

    Process output
    ≠ Effect automatically

---

# 71. Input ≠ cause

Providing or observing an input:

    ≠ sole/full cause automatically

Input relation and causal relation MUST remain distinguishable.

---

# 72. Resource consumption

Process MAY consume resource.

Но:

    resource quantity decreased
    ≠ Process consumed resource automatically

Attribution requires separate support.

---

# 73. Process conditions

Process MAY have:

- required conditions;
- enabling conditions;
- inhibiting conditions;
- boundary conditions;
- environmental conditions.

These are conditional semantics.

---

# 74. Required condition ≠ sufficient cause

If condition C is required:

    C present
    ≠ Process occurs automatically

Likewise:

    Process absent
    ≠ C absent automatically

---

# 75. Enabling condition

Enabling condition MAY permit Process.

But:

    enabled
    ≠ initiated automatically

---

# 76. Inhibiting condition

Inhibitor presence MAY affect Process.

But:

    inhibitor present
    ≠ Process absent automatically

unless domain-specific semantics supports this Inference.

---

# 77. Feedback

Process MAY include feedback.

Feedback terminology MAY include:

- positive;
- negative;
- stabilizing;
- destabilizing.

These terms are domain-sensitive and MUST preserve defined meaning.

---

# 78. Cycle

Process MAY be cyclic.

Cycle MAY have:

- period;
- phase;
- recurrence;
- State sequence;
- feedback.

But:

    repeating
    ≠ identical every cycle

---

# 79. Recurring Process

Необходимо различать:

    one recurring Process
    vs
    multiple similar Process occurrences

Similarity/repetition alone MUST NOT determine identity.

---

# 80. Periodicity

Periodicity MAY be:

- exact;
- approximate;
- irregular;
- inferred;
- modeled.

Label `periodic` MUST NOT imply perfect repetition unless supported.

---

# 81. Oscillation

Oscillatory Process MAY be represented as:

- continuous trajectory;
- State sequence;
- модель фазы;
- frequency/rate structure;
- other domain representation.

Core does not require one universal representation.

---

# 82. Process rate

Process MAY have rate.

Examples:

    corrosion rate
    growth rate
    flow rate

Rate MUST preserve when material:

- quantity;
- unit;
- time basis;
- measurement/model provenance.

---

# 83. Rate at T ≠ constant rate over interval

Fundamental rule:

    rate = r at T
    ≠ rate = r throughout interval automatically

Therefore:

    rate × duration
    ≠ total change automatically

unless constancy/integration assumptions are justified.

---

# 84. Rate ≠ cumulative change

Instantaneous or local Process rate does not automatically determine cumulative Result.

Cumulative change MAY require:

- integration;
- time-varying rate;
- additional Measurements;
- model assumptions.

---

# 85. Rate ≠ Process

Rate is Process dimension.

It is not Process itself.

---

# 86. Process intensity

Intensity MAY be Profile/domain-defined.

`012` does not impose universal intensity semantics.

---

# 87. Process direction

Process MAY have:

- spatial direction;
- increase/decrease direction;
- progression direction;
- reverse/forward semantics.

Direction MUST have defined meaning when materially relevant.

Но:

    direction
    ≠ inherent Objective

---

# 88. Process speed ≠ rate universally

Terms speed/rate MAY vary by domain.

External vocabulary MUST NOT determine semantics without definition.

---

# 89. Process State

Process itself MAY have State dimensions.

Example:

    Process operational State:
    active
    paused
    completed

But:

    Process State
    ≠ Process identity/content

---

# 90. Process lifecycle labels

Terms:

- planned;
- active;
- paused;
- completed;
- terminated;
- failed;

MAY correspond to:

- State;
- Event;
- Assessment;
- workflow label;
- семантика Процесса.

External label alone is insufficient.

---

# 91. Process completion

Completion MUST have defined semantics.

It MAY mean:

- natural endpoint reached;
- target stage reached;
- Procedure-defined termination;
- observation-defined completion;
- other domain semantics.

Therefore:

    completed
    ≠ successful automatically

И:

    completion
    ≠ Objective achieved automatically

---

# 92. Process termination

Process MAY terminate without completion.

Example:

    fermentation stopped because equipment failed

Then:

    Process ended
    ≠ intended Process completed

---

# 93. Process success

`012` does not introduce universal:

    Process.success

Success belongs to Objective/Result/Assessment semantics.

---

# 94. Process failure

`Failure` MAY represent:

- unexpected termination;
- undesirable State;
- Objective non-achievement;
- system malfunction;
- Assessment.

Therefore:

    Process failed

requires defined semantics.

---

# 95. Process quality

Terms:

- efficient;
- safe;
- stable;
- healthy;
- degraded;
- optimal;
- controlled;

usually belong to Assessment/Profile semantics.

They are not universal intrinsic Process properties.

---

# 96. Natural Process

Natural Process MAY occur without Actor.

Examples:

- erosion;
- evaporation;
- tectonic movement;
- ecological succession.

No Actor is required.

---

# 97. Technical Process

Technical Process MAY include:

- computation;
- manufacturing;
- regulation;
- signal processing;
- synchronization;
- startup sequence.

Logs are not the Process itself.

---

# 98. Process log ≠ Process

A log MAY contain:

- Events;
- States;
- timestamps;
- Measurements;
- Process-related records.

But:

    log
    ≠ Process

И:

    log gap
    ≠ Process gap automatically

---

# 99. Institutional Process

Institutional Process MAY include:

- review;
- approval;
- registration;
- appeal;
- governance;
- legal proceedings.

But:

    institutional rule/procedure
    ≠ actual institutional Process occurrence

---

# 100. Biological Process

Examples:

- growth;
- healing;
- metabolism;
- reproduction;
- immune response.

`012` does not define complete biological ontology.

Наблюдаемая биологическая прогрессия НЕ ДОЛЖНА автоматически получать телеологическую интерпретацию.

---

# 101. Chemical Process

Examples:

- reaction;
- oxidation;
- fermentation;
- decomposition.

Chemical reaction model:

    ≠ observed historical Process automatically

---

# 102. Ecological Process

Ecological Process MAY include:

- succession;
- migration;
- nutrient cycling;
- population change.

Aggregate representation MUST NOT erase materially relevant heterogeneity.

Ecological progression:

    ≠ внутреннее назначение автоматически

---

# 103. Social Process

Social Process MAY include:

- migration;
- institutionalization;
- demographic change;
- diffusion of practice.

Terminology MAY be model-dependent.

Historical sequence or direction:

    ≠ inevitable or purposeful progression automatically

---

# 104. Informational Process

Informational Process MAY include:

- transmission;
- computation;
- synchronization;
- encoding;
- replication;
- transformation.

Носитель ДОЛЖЕН оставаться отличимым от семантики Процесса.

---

# 105. Process Scope

Process Scope MAY include:

- participating subjects;
- system;
- population;
- territory;
- subsystem;
- network;
- component;
- other extent dimensions.

Temporal extent belongs to temporal/process frame and SHOULD NOT be silently collapsed into other Scope dimensions.

---

# 106. Process Scope ≠ Observation/Data Scope

A Process MAY occur across broader Scope than observed evidence.

Therefore:

    Process Scope
    ≠ Observation/Data Scope automatically

For example:

    process measured in 20% of system
    ≠ Process only existed in that 20%

unless independently established.

---

# 107. Local ≠ global Process

Process observed locally:

    ≠ global Process automatically

Generalization requires Inference or Model.

---

# 108. Sample ≠ population Process

Process dynamics observed in sample MUST NOT automatically become population dynamics.

---

# 109. Aggregate Process

Aggregate dynamics MAY represent multiple individual Processes.

But:

    aggregate Process
    ≠ identical individual dynamics

---

# 110. Process Context

Context MAY include:

- environment;
- system version;
- temperature;
- pressure;
- population;
- jurisdiction;
- season;
- load;
- Procedure version;
- concurrent Processes;
- other materially relevant conditions.

Context MUST NOT silently drift.

Context MUST remain distinguishable from participating frame when materially relevant.

---

# 111. Context-dependent Process

Same Process label MAY hide materially different dynamics under different Context.

Example:

    fermentation at 10°C
    ≠ fermentation at 35°C automatically

Transfer requires reasoning.

---

# 112. Concurrent Processes

One participating frame MAY contain multiple simultaneous Processes.

Examples:

    organism:
    respiration
    digestion
    healing

Coexistence:

    ≠ contradiction

---

# 113. Interacting Processes

Processes MAY interact.

Но:

    interaction
    ≠ complete causal mechanism known

Interaction relation MUST preserve materially relevant semantics.

---

# 114. Competing Processes

Processes MAY oppose each other.

Example:

    heating
    cooling

Net State MAY remain stable while both Processes continue.

---

# 115. Hidden / unobserved Process

Process MAY occur without direct Observation.

It MAY be inferred from:

- States;
- Events;
- Measurements;
- material traces;
- other Evidence.

But:

    inferred Process
    ≠ observed Process

---

# 116. Observed Process

Observed Process MAY be directly/continuously observed.

But:

    observed
    ≠ complete
    ≠ mechanism known
    ≠ causal explanation known

---

# 117. Measured Process

Measurements MAY characterize Process dynamics.

But:

    Measurement series
    ≠ Process ontology automatically

---

# 118. Inferred Process

Process MAY be inferred.

Inference SHOULD preserve when material:

- Evidence;
- assumptions;
- uncertainty;
- alternatives.

---

# 119. Reconstructed Process

Historical Process MAY be reconstructed from:

- States;
- Events;
- Actions;
- Sources;
- Measurements;
- material Evidence.

Reconstructed Process MUST NOT masquerade as direct Observation.

---

# 120. Modeled Process

Model MAY simulate or represent Process.

But:

    modeled Process
    ≠ observed/historical Process automatically

Model assumptions/version SHOULD remain resolvable when material.

Идентичность модели ДОЛЖНА оставаться отличимой от идентичности представленного Процесса.

---

# 121. Computed Process

Process representation MAY be computed from data/time series.

Computed:

    ≠ directly observed

even when based on observed inputs.

---

# 122. Provenance dimensions MAY overlap

Observed, measured, computed, inferred, modeled and reconstructed semantics MAY coexist.

Representation MUST NOT force one exclusive status if multiple dimensions are materially true.

---

# 123. Process uncertainty

Uncertainty MAY apply to:

- existence;
- participating frame;
- timing;
- duration;
- continuity;
- rate;
- phase;
- Scope;
- mechanism;
- causality;
- Context;
- reconstruction.

Core does not require universal:

    Process.confidence

---

# 124. Unknown Process

If Process existence or Content is unknown:

    Process unknown
    ≠ no Process

Likewise:

    no observed Process
    ≠ Process absent automatically

---

# 125. Process absence

Defined Process absence MAY be represented only where Evidence/domain semantics supports it.

Thus:

    not observed
    ≠ absent

    not recorded
    ≠ absent

---

# 126. Negated Process occurrence

Statement:

    Process P did not occur

is normally:

- Claim;
- absence semantics;
- Assessment;
- Inference;

depending on Context.

It MUST NOT automatically create:

    negative Process Entity

Thus:

    negation of Process occurrence
    ≠ Process automatically

---

# 127. Process conflict

Different Sources MAY represent competing Processes or mechanisms.

System MUST allow:

- competing Claims;
- competing Process representations;
- alternative mechanisms;
- different bounds;
- different decompositions;
- different identities.

Conflict MUST NOT be resolved by arbitrary merge.

---

# 128. Apparent Process conflict

Different Process descriptions MAY both be valid if they concern different:

- temporal periods;
- Scope;
- Context;
- granularity;
- phases;
- models;
- mechanisms.

Alignment required before contradiction is asserted.

---

# 129. Process normalization

External systems MAY use:

- process;
- pathway;
- workflow;
- cycle;
- progression;
- mechanism;
- sequence;
- operation;
- activity;
- phase.

Одна внешняя метка НЕ ДОЛЖНА определять каноническую семантику Процесса.

---

# 130. Pathway ≠ Process universally

Pathway MAY be:

- модель Механизма;
- модель Процесса;
- route;
- biological pathway;
- conceptual relation.

Semantic function determines mapping.

---

# 131. Workflow ≠ Process universally

Workflow MAY be:

- Procedure definition;
- actual Process;
- system State machine;
- institutional framework.

External term alone is insufficient.

---

# 132. Operation ≠ Process universally

Operation MAY represent:

- Action;
- Process;
- Procedure;
- institutional Activity;
- system State.

Semantic function determines mapping.

---

# 133. Activity ≠ Process universally

Activity МОЖЕТ пересекаться с семантикой Процесса.

But:

    Activity label
    ≠ Process automatically

Agentive Activity MAY involve:

- Action;
- Process;
- both.

---

# 134. Process comparison

Comparing Processes requires materially sufficient alignment.

Relevant alignment MAY include:

- Process Content;
- Process type;
- participating frame;
- temporal frame;
- Scope;
- Context;
- rate/unit;
- phase/decomposition;
- mechanism assumptions;
- measurement method.

---

# 135. Process equivalence

Different representations MAY be semantically equivalent.

But equivalence MUST NOT be established only from similar labels.

Эквивалентность моделей Процесса, эквивалентность типов и идентичность проявлений ДОЛЖНЫ оставаться различимыми.

---

# 136. Process similarity

Processes MAY be similar without being identical.

Similarity criteria SHOULD be defined when materially relevant.

---

# 137. Process transfer/generalization

Process observed in Context X:

    ≠ same Process dynamics in Context Y automatically

Transfer requires:

- Inference;
- Model;
- Assessment;
- другой обоснованной семантики.

---

# 138. Process and Result

Process MAY serve as reference frame for Result.

Example:

    Result:
    gas output
    relative to fermentation Process P

But:

    Process
    ≠ Result intrinsically

---

# 139. Process and State

Process MAY be represented as related to:

- emergence of State;
- maintenance of State;
- transformation between States;
- destabilization of State.

Но:

    Process–State relation
    ≠ causal relation automatically

unless causal/constitutive semantics is independently established.

Process itself does not automatically explain why a State exists.

---

# 140. Process and Event

Event MAY be represented as:

- marking Process onset;
- associated with Process initiation;
- associated with interruption;
- associated with termination;
- marking threshold;
- coinciding with phase transition.

Но:

    Event associated with Process
    ≠ causal relation automatically

И:

    граница Процесса
    ≠ Событие автоматически

If an Event is specifically asserted to initiate, cause or terminate Process, that stronger relation MUST be independently represented.

---

# 141. Process and Action

Action MAY be associated with:

- initiation;
- modification;
- maintenance;
- regulation;
- interruption;
- termination of Process.

Но:

    Action associated with Process
    ≠ Action controls Process fully

И:

    Действие, предшествующее Процессу
    ≠ Действие автоматически вызвало Процесс

---

# 142. Process and Decision

Решение МОЖЕТ разрешать Действия или изменять правила институционального Процесса.

Но:

    Decision
    ≠ Process

Decision Outcome also MUST NOT be confused with actual Process execution.

---

# 143. Process and Objective

Цель МОЖЕТ задавать желаемое поведение Процесса.

Но:

    desired семантика Процесса
    ≠ actual Process

Observed direction toward an endpoint:

    ≠ Objective automatically

---

# 144. Process and Assessment

Оценка МОЖЕТ оценивать:

- stability;
- safety;
- quality;
- efficiency;
- compliance;
- rate;
- Effectiveness.

These evaluations are not intrinsic Process truth.

---

# 145. Process and Inference

Вывод МОЖЕТ устанавливать:

- Process existence;
- identity;
- mechanism;
- phase;
- continuity;
- cause;
- classification as Process type.

Inferred semantics MUST preserve provenance.

---

# 146. Historical Process preservation

Исторический Процесс НЕ ДОЛЖЕН незаметно наследовать:

- текущую версию системы;
- текущую Процедуру;
- текущие институциональные правила;
- современную таксономию;
- текущий Контекст;
- текущую модель Процесса.

Историческое представление ДОЛЖНО оставаться разрешимым в исторической рамке.

---

# 147. Process versioning

Необходимо различать:

- изменилась модель Процесса;
- изменилось определение типа Процесса;
- изменился фактический Процесс;
- возникло новое проявление Процесса;
- пересмотрена реконструкция;
- Correction;
- decomposition changed.

Thus:

    пересмотр модели
    ≠ исторический Процесс автоматически изменился

И:

    пересмотр типа Процесса
    ≠ историческое проявление Процесса автоматически изменилось

---

# 148. Process representation fidelity

Представление НЕ ДОЛЖНО существенно изменять:

- Process Content;
- Process type/model/occurrence role;
- participating frame;
- Context;
- temporal frame;
- temporal scales;
- continuity;
- phase/stage semantics;
- Scope;
- provenance;
- uncertainty;
- causal/mechanistic status;
- purpose/Objective status.

---

# 149. Translation Fidelity

Перевод ДОЛЖЕН сохранять такие различия, как:

    heating
    ≠ heated

    spreading
    ≠ spread completed

    maintained
    ≠ created

    interrupted
    ≠ terminated

    recurring
    ≠ continuous

    Process type
    ≠ Process model

    Process model
    ≠ Process occurrence

    modeled
    ≠ observed

    progressing toward
    ≠ intending to reach

---

# 150. Logical Fidelity

Представление СЛЕДУЕТ сохранять:

- negation;
- temporal order;
- recurrence;
- intervals;
- conditionality;
- alternatives;
- uncertainty;
- phase boundaries;
- continuity status;
- type/model/occurrence distinctions;
- teleological vs non-teleological semantics.

---

# 151. Summary Fidelity

Сводка НЕ ДОЛЖНА превращать:

    intermittent Process
    → continuous Process

    observed phase
    → complete Process

    Process type
    → historical occurrence

    Process model
    → Process occurrence

    modeled Process
    → observed Process

    local Process
    → global Process

    associated Action
    → causal Action

    temporal sequence
    → mechanism

    Process boundary
    → Event automatically

    observed direction
    → внутреннее назначение

---

# 152. Process compression

Представление Процесса МОЖЕТ опускать несущественные детали.

Но сжатие НЕ ДОЛЖНО стирать существенно значимые:

- discontinuities;
- multiple temporal scales;
- uncertainty;
- competing mechanisms;
- stage boundaries;
- Scope;
- Context;
- provenance;
- identity uncertainty;
- type/model/occurrence role;
- participating-frame roles;
- safety-critical dynamics;
- teleology uncertainty.

---

# 153. Damaged archives

Исторический Источник МОЖЕТ сохранять частичное представление Процесса:

    "... river shifted course over years ..."

Missing:

- exact start;
- exact end;
- rate;
- full trajectory;
- mechanism;

НЕ ДОЛЖНЫ быть выдуманы.

Likewise отсутствие указанной причины или цели НЕ ДОЛЖНО заполняться правдоподобным повествованием.

---

# 154. Process reconstruction

Реконструкция исторического Процесса ДОЛЖНА сохранять:

- Source provenance;
- assumptions;
- uncertainty;
- competing models;
- temporal bounds;
- participating frame;
- Scope;
- Context.

Реконструкция НЕ ДОЛЖНА незаметно повышать модель Процесса до статуса исторического факта Процесса.

---

# 155. Offline preservation

Процесс СЛЕДУЕТ представлять без зависимости от современной платформы.

Когда это существенно, следует сохранять:

- Process Content;
- Process type/model/occurrence role;
- participating frame;
- Context;
- temporal/process frame;
- multiple temporal scales;
- continuity;
- phases/stages;
- Scope;
- relations to State/Event/Action;
- provenance;
- uncertainty.

---

# 156. Carrier neutrality

семантика Процесса не зависит от:

- database;
- Markdown;
- JSON;
- граф;
- timeline;
- simulation;
- diagram;
- printed archive;
- other durable carrier.

Носитель не определяет онтологию Процесса.

---

# 157. High-risk Profiles

Профили повышенного риска МОГУТ требовать более строгого представления Процесса.

Examples:

- medical;
- биологическим;
- химическим;
- engineering;
- electrical;
- environmental;
- survival;
- industrial;
- institutional.

Профиль МОЖЕТ требовать:

- phase definitions;
- Process type classification;
- rates;
- units;
- temporal bounds;
- multiple temporal scales;
- critical thresholds;
- interruption semantics;
- inputs/outputs;
- conditions;
- causal assumptions;
- monitoring method;
- provenance;
- uncertainty.

Это не универсальные требования Ядра.

---

# 158. Process quality

`012` не вводит универсальное внутреннее качество Процесса.

Такие термины, как:

- efficient;
- safe;
- stable;
- healthy;
- optimal;
- normal;
- degraded;
- successful;

обычно требуют семантики Оценки/Профиля.

---

# 159. Conformance and Integrity

Необходимо различать:

    Core structural/semantic conformance
    ≠ historical/provenance integrity
    ≠ Process occurrence certainty
    ≠ mechanism validity
    ≠ causal certainty
    ≠ Process quality
    ≠ Representation Fidelity

Core PASS does not mean:

- Process certainly occurred;
- Process occurred exactly as modeled;
- mechanism known;
- Process safe;
- Process successful;
- Process caused a Result;
- Процесс имеет внутреннее назначение.

---

# 160. Profiles

Профиль МОЖЕТ усиливать требования Ядра.

Profile MUST NOT weaken Core while claiming compatibility with `012`.

---

# 161. Diagnostic families

Диагностическая терминология описывает семантические модели ошибок.

## 161.1. Type / model / occurrence failures

Examples:

- Process type → historical occurrence;
- Process model → Process type automatically;
- Process model → occurrence;
- Process Content → Process type automatically;
- generic Process knowledge → case evidence;
- workflow definition → actual execution.

## 161.2. Process/Event failures

Examples:

- Event → full Process;
- Process boundary → Event automatically;
- phase boundary → Event automatically;
- duration used as sole classifier;
- Event treated as full mechanism.

## 161.3. State/Process failures

Examples:

- State sequence → Process automatically;
- stable State → no Process;
- Process → mandatory State change;
- Process–State relation → causality automatically.

## 161.4. Continuity failures

Examples:

- observation gap → interruption;
- observation gap → continuity;
- no Process end record → permanent continuation;
- interruption → termination;
- resumption → same identity automatically.

## 161.5. Identity / topology failures

Examples:

- same Content → same Process;
- different wording → different Process;
- идентичность представления → идентичность представленного Процесса;
- merge → continuity automatically;
- split → identity inherited automatically;
- temporal containment → subprocess;
- overlap → part-of.

## 161.6. Granularity / decomposition failures

Examples:

- Composite Process → complete decomposition;
- different valid decompositions → contradiction;
- observed phase → complete Process.

## 161.7. Causality / mechanism failures

Examples:

- sequence → causality;
- input → sole cause;
- output → Effect;
- observed oscillation → feedback;
- modeled mechanism → observed mechanism;
- Event associated with onset → Event caused Process;
- Action association → full causal control.

## 161.8. Rate / temporal-scale failures

Examples:

- rate at T → constant rate;
- rate × duration → cumulative change without assumptions;
- one temporal scale → entire Process structure.

## 161.9. Participating-frame / Context failures

Examples:

- Context → participant automatically;
- participant → Context automatically;
- environmental condition → Process participant without basis;
- Process relation roles flattened.

## 161.10. Teleology failures

Examples:

- направление Процесса → цели или назначения;
- adaptation → намерения;
- endpoint → Objective;
- historical progression → inevitable destination.

## 161.11. Scope / Context failures

Examples:

- local → global Process;
- sample → population Process;
- Data Scope → Process Scope;
- Context X → Context Y;
- current system version → historical Process.

## 161.12. Provenance / import failures

Examples:

- modeled → observed;
- inferred → directly observed;
- log → Process;
- pathway/workflow/activity label → canonical Process;
- negated Process → negative Process Entity.

Diagnostic label itself does not establish:

- fraud;
- intent;
- negligence;
- ответственности;
- blame.

---

# 162. Machine validation

Валидатор МОЖЕТ проверять:

- Process Content;
- Process role/type references;
- participating frame;
- temporal/process frame;
- reference integrity;
- phase consistency;
- Profile-defined transitions;
- units/rates;
- required Profile conditions;
- structural consistency.

But:

    validator PASS
    ≠ Process historically true
    ≠ Process occurrence proven
    ≠ mechanism correct
    ≠ causality established
    ≠ Process safe
    ≠ Process successful
    ≠ Process purposeful

Валидатор не имеет привилегии истины.

---

# 163. Cross-standard compatibility

`012-PROCESS` MUST preserve neighboring boundaries.

In compact form:

    State
    → каким представлен объект или конфигурация
      в applicable frame

    Event
    → что произошло /
      какое проявление или какая граница возникли

    Process
    → какая протяжённая во времени
      activity/dynamics unfolds
      or is maintained

    Action
    → что было сделано

    Result
    → какую результирующую роль
      phenomenon занимает
      относительно reference frame

    Objective
    → какое целевое/желаемое состояние
      или behavior задан

Therefore:

    State
    ≠ Process

    Event
    ≠ Process

    Action
    ≠ Process

    Result
    ≠ Process intrinsically

    Objective
    ≠ Process

    State sequence
    ≠ Process automatically

    Event sequence
    ≠ Process automatically

    Procedure
    ≠ Process

    Workflow definition
    ≠ Process occurrence

    Mechanism model
    ≠ Process occurrence

    Process type
    ≠ Process model
    ≠ Process occurrence

    observed Process direction
    ≠ inherent Objective/purpose

---

# 164. Boundary concepts outside full 012 ontology

`012` uses neighboring concepts only to establish Process boundaries.

These include:

- State;
- Event;
- Action;
- Result;
- Objective;
- Procedure;
- Workflow;
- Activity;
- Mechanism;
- Phase;
- Stage;
- Pathway;
- Assessment;
- Observation;
- Measurement;
- Process type;
- Process model.

`012` does not assert that their complete ontology belongs inside Process standard.

---

# 165. Entity Explosion Test

`012` НЕ требует введения следующих фундаментальных Сущностей Ядра только ради Процесса:

- ProcessContent;
- ProcessSubject;
- ProcessParticipant;
- ParticipatingFrame;
- ProcessContext;
- ProcessAttribution;
- ProcessFrame;
- ProcessScope;
- ProcessPhase;
- ProcessStage;
- Subprocess;
- CompositeProcess;
- ProcessCycle;
- ProcessRate;
- ProcessIntensity;
- ProcessInput;
- ProcessOutput;
- ProcessCondition;
- ProcessMechanism;
- ProcessState;
- ProcessTrajectory;
- ProcessSequence;
- ProcessInterruption;
- ProcessResumption;
- ProcessBoundary;
- ProcessMerge;
- ProcessSplit;
- ProcessBranch;
- ProcessType;
- ProcessModel;
- ProcessInstance;
- ProcessOccurrence;
- ProcessPurpose;
- NaturalProcess;
- TechnicalProcess;
- BiologicalProcess;
- InstitutionalProcess;
- ChemicalProcess;
- EcologicalProcess;
- ProcessConfidence;
- ProcessQuality.

These MAY be represented through:

- semantic roles;
- отношения;
- States;
- Events;
- Profiles;
- Records;
- Models;
- temporal structures;
- generic infrastructure;
- future standards.

Absence of separate Core Entity does not mean absence of corresponding semantics.

---

# 166. Core invariants

Следующие положения образуют минимальное нормативное ядро `012-PROCESS`.

### P-01
Процесс является семантической конструкцией, представляющей протяжённое во времени проявление, деятельность, динамику, преобразование, взаимодействие, поддержание или прогрессию.

### P-02
Семантика Процесса МОЖЕТ быть материализована как специализированная Запись, когда это существенно полезно, но отдельная Сущность Процесса не является универсально обязательной.

### P-03
Process type, Process model and Process occurrence MUST remain semantically distinguishable.

### P-04
Process type MUST NOT automatically be treated as Process model or Process occurrence.

### P-05
Process model MUST NOT automatically be treated as Process type, Process occurrence or historical evidence.

### P-06
Идентичность модели ДОЛЖНА оставаться отличимой от идентичности представленного типа Процесса или его конкретного проявления.

### P-07
Process Content MUST NOT automatically be treated as Process type.

### P-08
Generic Process knowledge MUST NOT automatically be treated as evidence that a particular historical Process occurred.

### P-09
`012` MUST NOT require every temporal sequence to be represented as Process.

### P-10
Конкретное проявление Процесса ДОЛЖНО иметь определённое содержание Процесса.

### P-11
Конкретное проявление Процесса ДОЛЖНО иметь разрешимую рамку участников.

### P-12
Participating frame MUST NOT require one privileged subject and MAY be distributed, relational or multi-participant.

### P-13
Participating frame and Context MUST remain distinguishable when materially relevant.

### P-14
Participating roles MUST remain resolvable when flattening would materially alter meaning.

### P-15
Процесс ДОЛЖЕН сохранять достаточное семантическое отнесение.

### P-16
Process attribution is semantic requirement and MUST NOT require dedicated Core Entity solely for conformance.

### P-17
Конкретное проявление Процесса ДОЛЖНО иметь разрешимую временную/процессную рамку.

### P-18
Process representation existence MUST NOT automatically imply epistemic certainty that Process occurred exactly as represented.

### P-19
Claim about Process MUST remain distinct from Process.

### P-20
Известность существования Процесса НЕ ДОЛЖНА автоматически означать известность его внутренней динамики, структуры фаз, траектории или механизма.

### P-21
Process MUST remain distinct from Event.

### P-22
Duration alone MUST NOT determine Event vs Process classification.

### P-23
Process boundary MUST NOT automatically be represented as Event.

### P-24
Beginning/end of Observation MUST NOT automatically be treated as beginning/end of Process.

### P-25
Phase boundary MUST NOT automatically be treated as Event.

### P-26
Process MUST NOT require discrete Event decomposition.

### P-27
Known Event MUST NOT automatically imply known Process or mechanism.

### P-28
State MUST remain distinct from Process.

### P-29
State sequence MUST NOT automatically establish Process, mechanism or continuity.

### P-30
Process MUST NOT require net State change and MAY maintain State.

### P-31
Action MUST remain distinct from Process.

### P-32
Метка Activity НЕ ДОЛЖНА автоматически определять онтологию Процесса; агентная Activity МОЖЕТ нести семантику Действия, семантику Процесса или обе.

### P-33
Process MUST NOT require Actor attribution.

### P-34
Action associated with Process MUST NOT automatically imply Action caused or fully controlled Process.

### P-35
Process MUST NOT automatically be treated as Result, Objective or Procedure.

### P-36
Observed Process direction, progression, adaptation or endpoint MUST NOT automatically be treated as inherent Objective, intention or purpose.

### P-37
Procedure/workflow definition MUST remain distinct from actual Process occurrence.

### P-38
Process occurrence MUST remain distinct from Mechanism model.

### P-39
Unknown Process start/end MUST NOT be replaced by invented exact boundaries.

### P-40
Open-ended Process MUST NOT automatically be treated as permanently ongoing.

### P-41
Process MAY have multiple materially relevant temporal scales, and one scale MUST NOT silently replace another.

### P-42
Observation gaps MUST NOT automatically establish either Process interruption or Process continuity.

### P-43
Process interruption MUST NOT automatically imply termination.

### P-44
Process resumption MUST NOT automatically imply same Process identity.

### P-45
Same Process Content MUST NOT automatically imply same Process identity.

### P-46
Different descriptions MUST NOT automatically imply different Processes.

### P-47
Identity of Process representation MUST remain distinct from identity/continuity of represented Process.

### P-48
Different provenance MUST NOT automatically imply different represented Process.

### P-49
Merge, split or branching MUST NOT automatically establish identity continuity.

### P-50
Purpose/granularity MAY alter Process decomposition but MUST NOT invent stages, mechanisms, continuity, participants or causal links.

### P-51
Composite Process MUST NOT imply complete decomposition.

### P-52
Temporal containment MUST NOT automatically imply subprocess relation.

### P-53
Process overlap MUST NOT automatically imply part-of relation.

### P-54
Different valid decompositions MUST NOT automatically be treated as contradiction.

### P-55
Phase/stage labels MUST NOT automatically determine Process ontology.

### P-56
Temporal order inside Process MUST NOT automatically establish causality.

### P-57
Mechanistic/causal relations MUST preserve materially relevant provenance, uncertainty, assumptions, Scope and Context.

### P-58
Observed pattern MUST NOT automatically establish feedback mechanism.

### P-59
Inputs, outputs and conditions are conditional semantics and MUST NOT be universal mandatory Process fields.

### P-60
Input MUST NOT automatically imply sole/full causation.

### P-61
Выход Процесса НЕ ДОЛЖЕН автоматически рассматриваться как Результат или Эффект.

### P-62
Required/enabling condition MUST NOT automatically imply Process occurrence.

### P-63
Recurring/cyclic semantics MUST NOT automatically imply identical Process cycles or one continuous Process identity.

### P-64
Rate/intensity/direction are Process dimensions and MUST NOT automatically determine Process identity.

### P-65
Rate observed at a point/time MUST NOT automatically be treated as constant over an interval.

### P-66
Rate × duration MUST NOT automatically be interpreted as cumulative change without justified assumptions/integration semantics.

### P-67
Process lifecycle labels such as active, paused, completed or failed MUST preserve domain semantics.

### P-68
Process completion MUST NOT automatically imply success or Objective Achievement.

### P-69
Natural Process MUST NOT require Actor.

### P-70
Logs or Measurements MUST NOT automatically be treated as Process itself.

### P-71
Workflow/institutional rule MUST NOT automatically be treated as actual institutional Process occurrence.

### P-72
Область Процесса ДОЛЖНА оставаться отличимой от Области наблюдения/данных, когда это существенно.

### P-73
Локальная/выборочная/агрегированная семантика Процесса НЕ ДОЛЖНА автоматически становиться глобальной/популяционной/индивидуальной семантикой.

### P-74
Process Context MUST NOT silently drift.

### P-75
Одновременные Процессы НЕ ДОЛЖНЫ автоматически считаться противоречащими друг другу.

### P-76
Interaction between Processes MUST NOT automatically establish complete causal mechanism.

### P-77
Происхождение наблюдаемого, измеренного, вычисленного, выведенного, смоделированного и реконструированного Процесса МОЖЕТ перекрываться и ДОЛЖНО оставаться разрешимым, когда это существенно.

### P-78
Семантика неизвестности/отсутствия наблюдения ДОЛЖНА оставаться отличимой от отсутствия Процесса.

### P-79
Negation of Process occurrence MUST NOT automatically create a Process entity or Process occurrence.

### P-80
Конфликт Процессов НЕ ДОЛЖЕН утверждаться до достаточного согласования времени, Области, Контекста, гранулярности и механизма.

### P-81
Внешние метки, такие как workflow, pathway, operation, Activity, phase или process, НЕ ДОЛЖНЫ автоматически определять каноническую семантику Процесса.

### P-82
Исторический Процесс НЕ ДОЛЖЕН незаметно наследовать текущую версию системы, Процедуру, таксономию, модель или Контекст.

### P-83
Пересмотр модели/типа НЕ ДОЛЖЕН автоматически означать изменение исторического Процесса.

### P-84
Связь Процесс–Состояние НЕ ДОЛЖНА автоматически рассматриваться как причинная связь.

### P-85
Событие, связанное с началом, прерыванием или завершением Процесса, НЕ ДОЛЖНО автоматически рассматриваться как причинное Событие.

### P-86
Representation MUST preserve materially relevant Process Content, type/model/occurrence role, participating frame, Context, temporal frame, continuity, Scope, provenance and uncertainty.

### P-87
Core structural/semantic conformance MUST remain distinct from historical/provenance integrity, Process occurrence certainty, mechanism validity, causal certainty, Process quality and Representation Fidelity.

### P-88
Profile MAY strengthen Core requirements but MUST NOT weaken Core while claiming compatibility with `012`.

### P-89
Materially relevant uncertainty, provenance, participating frame, Context, temporal scales, continuity and Scope MUST remain resolvable.

---

# 167. Stress-test framework

Архитектура `012-PROCESS` ДОЛЖНА выдерживать как минимум следующие классы атак:

1. Process representation vs epistemic truth;
2. тип Процесса vs модель Процесса;
3. Process type vs Process occurrence;
4. Process model vs Process occurrence;
5. Идентичность модели vs идентичность представленного Процесса;
6. Process Content vs Process type;
7. generic Process knowledge vs historical occurrence;
8. temporal sequence vs Process;
9. distributed Process without privileged subject;
10. relational Process;
11. participating frame vs Context;
12. Process vs Claim;
13. известный Процесс vs неизвестная внутренняя динамика;
14. Process vs Event;
15. short Process vs Event;
16. extended Event vs Process;
17. Process boundary vs Event;
18. fuzzy Process boundary;
19. threshold-defined Process boundary;
20. observation boundary vs Process boundary;
21. Процесс без дискретных Событий;
22. Event without known Process;
23. Phase boundary vs Event;
24. Process vs State;
25. State sequence without Process certainty;
26. Process maintaining State;
27. steady State with Process;
28. Process vs Action;
29. Activity vs Action vs Process;
30. Action associated with Process onset;
31. Процесс без Агента;
32. Process vs Result;
33. Process vs Objective;
34. Process direction vs Objective;
35. adaptation vs намерения;
36. endpoint vs цели или назначения;
37. historical progression vs teleology;
38. Process vs Procedure;
39. workflow definition vs Process occurrence;
40. Процесс vs модель Механизма;
41. unknown Process start;
42. unknown Process end;
43. open-ended Process;
44. observation gap;
45. intermittent Process;
46. interrupted Process;
47. resumed Process;
48. same Process Content at different times;
49. Process identity after interruption;
50. different descriptions of same Process;
51. идентичность представления vs идентичность представленного Процесса;
52. different provenance of same Process;
53. merge;
54. split;
55. branching;
56. convergence;
57. coarse vs fine Process;
58. Composite Process;
59. incomplete decomposition;
60. subprocess relation;
61. temporal containment vs subprocess;
62. overlap vs part-of;
63. multiple valid decompositions;
64. phase ambiguity;
65. stage ambiguity;
66. sequence vs causality;
67. mechanism provenance;
68. observed pattern vs feedback;
69. Process input;
70. Process output;
71. input vs cause;
72. output vs Result;
73. output vs Effect;
74. Process–State relation vs causality;
75. Event–Process association vs causality;
76. resource consumption attribution;
77. precondition;
78. enabling condition;
79. inhibiting condition;
80. feedback;
81. cyclic Process;
82. recurring Process;
83. repeated Process occurrences;
84. identical-cycle assumption;
85. periodicity uncertainty;
86. oscillation;
87. multiple temporal scales;
88. Process rate;
89. instantaneous rate vs interval rate;
90. rate × duration vs cumulative change;
91. rate vs Process identity;
92. Process intensity;
93. Process direction;
94. Process State;
95. lifecycle labels;
96. завершение vs успешность;
97. завершение vs достижение Цели;
98. termination vs completion;
99. failure semantics;
100. natural Process;
101. technical Process;
102. Process log vs Process;
103. institutional Process;
104. institutional rule vs execution;
105. biological Process;
106. chemical Process;
107. ecological Process;
108. social Process;
109. informational Process;
110. Process Scope vs Observation Scope;
111. local vs global Process;
112. sample vs population Process;
113. aggregate vs individual Process;
114. Context-dependent Process;
115. concurrent Processes;
116. interacting Processes;
117. competing Processes;
118. hidden/inferred Process;
119. observed Process;
120. measured Process;
121. modeled Process;
122. reconstructed Process;
123. computed Process;
124. overlapping provenance;
125. Process uncertainty;
126. unknown vs absent Process;
127. negated Process occurrence;
128. conflicting Process representations;
129. apparent conflict due to granularity;
130. apparent conflict due to phase;
131. external process/workflow/pathway/activity labels;
132. Process comparison;
133. Process equivalence;
134. Process transfer/generalization;
135. Process as Result reference frame;
136. Process related to State;
137. Event associated with Process onset;
138. Action associated with Process regulation;
139. Process related to Decision;
140. Process related to Objective;
141. Process Assessment;
142. historical Process model drift;
143. historical system-version drift;
144. пересмотр типа Процесса;
145. пересмотр модели Процесса;
146. damaged archives;
147. historical reconstruction;
148. translation corruption;
149. summary corruption;
150. offline preservation;
151. high-risk Profiles;
152. cross-standard collisions.

Stress-test cases не создают Core requirements самостоятельно.

Если новый test выявляет необходимое фундаментальное правило, оно должно быть внесено в соответствующий normative section.

Прохождение stress-test не является доказательством полноты или окончательности модели.

---

# 168. Принцип сохранения

При конфликте между полнотой и честностью представления предпочтение отдаётся честности.

    partial Process
    > invented complete Process

    Process type
    > invented occurrence

    Process model
    > falsely historical Process

    known Process existence
    > invented внутренней динамики

    observed dynamics
    > invented mechanism

    temporal sequence
    > invented Process

    Process boundary uncertainty
    > invented Event

    observation window
    > invented Process bounds

    unknown interval
    > invented continuity

    observation gap
    > invented stop or continuation

    modeled Process
    > falsely observed Process

    generic Process knowledge
    > falsely historical mechanism

    incomplete decomposition
    > false complete Process model

    rate observation
    > invented constant rate

    observed direction
    > invented purpose

    historical Context
    > current-context substitution

Цель стандарта — сохранить Процесс настолько полно, насколько позволяют данные, **не превращая временную последовательность в причинность, общий тип Процесса — в историческое проявление, модель Процесса — в наблюдаемый Процесс, границу Процесса — в Событие, известность существования Процесса — в известность механизма, наблюдаемое направление — во внутреннее назначение, пробелы в свидетельствах — в выдуманную непрерывность/прерывание или реконструкцию — в непосредственно наблюдаемую реальность**.

---

# 169. Итоговая формула

В наиболее компактной форме:

    State
    → каким представлен объект или конфигурация
      в applicable frame

    Event
    → что произошло /
      какое проявление или какая граница возникли

    Process
    → какая протяжённая во времени
      activity, dynamics, interaction,
      maintenance или transformation
      unfolds

    Action
    → что было сделано

    Result
    → какую результирующую роль
      phenomenon занимает
      относительно reference frame

    Process type
    → к какому general kind
      относится семантика Процесса

    Process model
    → как тип Процесса или конкретное проявление
      представлен в модели

    Process occurrence
    → какой конкретный Процесс
      представлен как происходящий
      или происходивший

Центральный принцип `012-PROCESS`:

> **Сохранить Процесс — значит сохранить максимально честное представление о протяжённого во времени проявления Процесса или динамики вместе с существенно значимыми типом/моделью/ролью проявления, рамкой участников, Контекстом, временной структурой, непрерывностью, Областью, происхождением и неопределённостью.**

Факт представления Процесса сам по себе не означает:

- что конкретное проявление Процесса доказано;
- что тип Процесса и модель Процесса совпадают;
- что известна внутренняя динамика;
- что известен полный механизм;
- что Процесс имеет Агента;
- что Процесс имеет внутренние цели или назначение;
- что Процесс непрерывен;
- что start/end являются Events;
- что Событие, связанное с границей, является причиной;
- что выход является Результатом или Эффектом;
- что Процесс успешен;
- что Процесс эффективен;
- что Процесс будет продолжаться в будущем.

---

# 170. Статус версии

**012-PROCESS v0.1**

Стандарт прошёл:

- первичную полную сборку;
- сквозную архитектурную атаку;
- внесение всех обязательных исправлений после атаки;
- контрольный аудит собранной версии;
- проверку представления Процесса / эпистемической обоснованности;
- проверку типа Процесса / модели Процесса / конкретного проявления;
- проверку Process Content / типа Процесса;
- проверку общего знания о Процессе / исторического проявления;
- проверку распределённого/реляционного Процесса;
- проверку рамки участников / Контекста;
- проверку Процесса / События;
- проверку границы Процесса / События;
- проверку границы фазы / События;
- проверку Процесса / Состояния;
- проверку Процесса / Действия;
- проверку Activity / Действия / Процесса;
- проверку Процесса / Результата;
- проверку Процесса / Цели;
- проверку anti-teleology semantics;
- проверку Процесса / Процедуры;
- проверку определения workflow / конкретного проявления Процесса;
- проверку Процесса / Механизма;
- проверку известного Процесса / неизвестной внутренней динамики;
- проверку continuity / interruption / resumption;
- проверку идентичности Процесса;
- проверку merge / split / branching;
- проверку temporal containment / overlap / subprocess;
- проверку decomposition / phases / stages;
- проверку multiple temporal scales;
- проверку causal/mechanistic semantics;
- проверку причинной границы Процесс–Состояние;
- проверку причинной границы Событие–Процесс;
- проверку семантики обратной связи;
- проверку входов/выходов/условий;
- проверку скорости / накопленного изменения;
- проверку Области / Области наблюдения;
- проверку sample / population;
- проверку Context;
- проверку provenance;
- проверку отрицания конкретного проявления Процесса;
- проверку сохранения исторического Процесса;
- проверку совместимости с `008-ACTION`, `009-EVENT`, `010-RESULT`, `011-STATE`;
- Entity Explosion Test.

**Критических архитектурных противоречий: 0.**  
**Новых обязательных Core Entities: 0.**  
**Невнесённых обязательных изменений: 0.**

`012-PROCESS v0.1` считается зафиксированным рабочим стандартом проекта.

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.
