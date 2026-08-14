# 009 — EVENT
## Стандарт представления событий

**Проект:** Энциклопедия цивилизации  
**Статус:** рабочий стандарт  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляются события — природные, человеческие, технические, институциональные, биологические, системные, исторические и иные occurrences, которым приписывается temporal occurrence/boundary semantics.

Цель стандарта — позволить сохранять:

- что произошло;
- когда это произошло настолько, насколько это установимо;
- где это произошло;
- какие объекты, системы или участники были вовлечены;
- какие States существовали до и после события, если это известно;
- насколько событие было единичным, составным, повторяющимся или продолжительным;
- являлось ли оно частью Process;
- было ли связано с Action;
- какие причины ему атрибутируются;
- какие Effects, Results или Consequences связываются с ним;
- что наблюдалось непосредственно;
- что сообщалось;
- что реконструировано;
- что оспаривается;
- что неизвестно.

Стандарт не предназначен для автоматического определения:

- причины Event;
- Actor;
- ответственности;
- намерения;
- виновности;
- законности;
- значимости;
- опасности;
- благоприятности;
- Result status;
- downstream causality.

Сохранить Event означает сохранить максимально честное представление о том, **что представлено как произошедшее**, не превращая временную последовательность в причинность, участие — в ответственность, State — в Event, а интерпретацию — в сам occurrence.

---

# 1. Основное понятие

## 1.1. Event

**Event (Событие)** — специализированный Record, представляющий определённый occurrence, которому в модели приписана temporal occurrence/boundary semantics: возникновение, изменение, переход, начало, завершение, прекращение или иное различимое наступление во времени.

Event отвечает на основной вопрос:

> **Что произошло?**

Event MAY относиться:

- к физическому изменению;
- природному явлению;
- техническому событию;
- социальному происшествию;
- институциональному изменению;
- системному событию;
- началу или завершению Process;
- возникновению или прекращению State;
- threshold crossing;
- иной event-like occurrence.

Event не требует:

- Actor;
- Decision;
- Action;
- intention;
- known cause;
- known Result;
- known Effect.

---

# 2. Минимальная структура Event

Для представления завершённого Event необходимо как минимум:

1. определённый occurrence, представленный как произошедший;
2. определённый Event Content;
3. достаточная event attribution.

Минимальная формула:

    defined occurrence represented as having happened
    +
    defined Event Content
    +
    sufficient event attribution

**Event attribution** — достаточная semantics, представляющая Content как occurrence, transition или temporal boundary, а не только как:

- State;
- proposition;
- Claim;
- Plan;
- prediction;
- counterfactual;
- abstract description.

Event attribution является **semantic requirement**, а не обязательным отдельным field, Record или Core Entity.

Следовательно:

    bridge is broken
    → State MAY be represented

не равно автоматически:

    bridge collapsed
    → Event

Не обязательно, чтобы для Event были известны:

- точное время;
- точное место;
- cause;
- participants;
- Actor;
- Action;
- Process;
- prior State;
- resulting State;
- Result;
- Consequence;
- significance.

Неизвестные элементы MUST NOT изобретаться.

---

# 3. Event Content

**Event Content** — содержание, представляющее то, что произошло в рамках конкретного Event.

Например:

    мост обрушился

Event Content:

    обрушение моста

Event Content является semantic role/content construct и не требует отдельной Core Entity.

Он MAY представлять:

- появление;
- исчезновение;
- переход;
- разрушение;
- соединение;
- разделение;
- начало;
- завершение;
- изменение параметра;
- threshold crossing;
- столкновение;
- сбой;
- вспышку;
- иной occurrence.

Event Content MAY быть простым или структурированным.

---

# 4. Event ≠ Claim

Claim отвечает:

> Что утверждается?

Event отвечает:

> Что произошло?

Следовательно:

    Claim about Event
    ≠ Event

Например:

    Source S states:
    bridge collapsed

является Claim about Event.

Event Record MAY быть представлен отдельно.

Но наличие Event Record MUST NOT автоматически означать epistemic certainty того, что occurrence действительно произошёл именно так, как представлен.

Event Record является representation occurrence, а не гарантией исторической истины.

---

# 5. Event ≠ Action

Action отвечает:

> Что было сделано?

Event отвечает:

> Что произошло?

Следовательно:

    Action
    ≠ Event

Например:

    Action:
    operator opened valve

    Event:
    valve opened

Один и тот же underlying occurrence MAY поддерживать несколько semantic representations.

Например:

    Action Record:
    operator opened valve

и:

    Event Record:
    valve opened

могут относиться к одному underlying occurrence.

Но:

    distinct semantic Records
    ≠ distinct underlying occurrences automatically

Следовательно:

    Event occurred
    ≠ Action existed automatically

И:

    Action occurred
    ≠ every downstream Event is part of that Action

---

# 6. Event ≠ Process

**Process** обычно представляет разворачивающееся течение, механизм, последовательность или устойчивую динамику.

**Event** представляет occurrence или temporal boundary.

Например:

    Process:
    forest fire spreading

    Event:
    fire started

или:

    Event:
    fire crossed River X

или:

    Event:
    fire ended

Один Process MAY включать множество Events.

Event MAY обозначать:

- начало Process;
- milestone;
- interruption;
- change;
- completion.

Duration, internal complexity или количество внутренних subchanges MUST NOT сами по себе определять Event vs Process classification.

Не существует универсального временного порога:

    > N hours
    → Process

или:

    < N seconds
    → Event

---

# 7. Event ≠ State

**State** отвечает:

> В каком состоянии что-либо находится или находилось?

Event отвечает:

> Что произошло / какой transition или temporal boundary произошёл?

Например:

    State:
    valve is open

    Event:
    valve opened

или:

    State:
    city is flooded

    Event:
    flooding began

Mere State attribution at a time MUST NOT автоматически становиться Event.

Например:

    temperature = 100°C at T1

может быть:

- State;
- Observation;
- Measurement;
- Result;
- частью Event reconstruction.

Но это не является Event автоматически.

---

# 8. State difference ≠ one Event automatically

Если известно:

    State S1 @ T1
    State S2 @ T2

это MAY поддерживать Inference, что между ними произошло изменение.

Но различие States само по себе MUST NOT определять:

- Event count;
- Event identity;
- Event granularity;
- transition mechanism;
- exact transition time;
- отсутствие intermediate States;
- наличие одного discrete Event.

Например:

    intact @ T1
    destroyed @ T2

может отражать:

- один catastrophic Event;
- постепенный Process;
- множество Events;
- комбинацию Actions и Events.

Event reconstruction должна сохранять uncertainty.

---

# 9. Event ≠ Result

Event представляет occurrence semantics.

**Result** представляет relational downstream semantics относительно определённого reference frame.

Например:

    river level increased

MAY быть Event.

То же occurrence MAY быть Result относительно:

    dam-release Action

если такая relation установлена.

Следовательно:

    Event
    ≠ Result intrinsically

Result не является обязательно evaluative concept.

Его оценка MAY быть отдельным Assessment.

---

# 10. Event ≠ Consequence

Consequence предполагает consequential attribution относительно чего-либо.

Event сам по себе такую attribution не содержит.

    Event E occurred after A
    ≠ E is Consequence of A automatically

Consequence является contextual relation/role, а не intrinsic property Event.

---

# 11. Event ≠ Observation

Observation представляет акт или Record наблюдения.

Event представляет occurrence.

Например:

    Event:
    flash occurred

    Observation:
    observer P saw flash

Следовательно:

    observed Event
    ≠ Observation

И:

    unobserved Event
    MAY still have occurred

Observation не является existential requirement Event.

---

# 12. Event ≠ Report

Report, Source или Claim MAY сообщать о Event.

Но:

    report of Event
    ≠ Event

Report cardinality MUST NOT определять Event cardinality.

Следовательно:

    10 reports
    ≠ 10 Events

И обратное:

    1 report
    MAY describe 0, 1 or multiple Events

Document structure MUST NOT определять Event identity автоматически.

---

# 13. Event identity

Event identity следует represented occurrence, а не совпадению wording.

    same Event Content
    ≠ same Event

Например:

    earthquake at T1
    earthquake at T2

MAY быть разными Events.

Но:

    different wording
    ≠ different Event automatically

Например:

    the bridge collapsed

и:

    the central span failed

MAY описывать один occurrence на разных abstraction levels.

---

# 14. Time/place ≠ identity

Temporal и spatial co-location сами по себе не определяют Event identity.

Например в одном месте и в одно время могут произойти:

- power failure;
- alarm activation;
- fire ignition;
- connection loss.

Следовательно:

    same time
    +
    same place
    ≠ same Event automatically

---

# 15. Granularity

Event может быть представлен на разных уровнях.

Например:

    aircraft crashed

или:

    engine failed
    aircraft lost altitude
    aircraft struck terrain
    fuel ignited

Ни один уровень не является универсально правильным.

Granularity определяется:

- provenance;
- materially relevant distinctions;
- Profile;
- целью representation.

Purpose MAY влиять на выбранный уровень representation и granularity, но MUST NOT сам по себе создавать, уничтожать или изменять underlying Event identity.

Granularity MUST NOT использоваться для искусственного:

- дробления одного occurrence;
- объединения независимых occurrences;
- скрытия causal distinctions;
- скрытия temporal distinctions;
- искажения participation;
- искажения safety-critical meaning.

---

# 16. Composite Event

Один Event MAY иметь structured Event Content.

Но Composite Event MUST NOT выводиться только из:

- causal linkage;
- close timing;
- same location;
- common participant;
- shared Source;
- thematic similarity.

Например:

    explosion
    pipeline rupture
    fire

MAY быть:

- одним composite Event;
- тремя Events;
- event chain;
- частью Process.

Identity должна следовать represented occurrence semantics, boundaries и provenance.

Purpose MAY определять уровень представления, но не является достаточным основанием исторической Event identity.

Отдельная CompositeEvent Entity не требуется.

---

# 17. Event boundaries

Event MAY иметь:

- точные границы;
- приблизительные границы;
- naturally defined boundaries;
- conventionally defined boundaries;
- disputed boundaries;
- unknown boundaries.

Неопределённость MUST NOT заменяться artificial precision.

Например:

    eruption began sometime overnight

не должно автоматически становиться:

    eruption began at 02:00

---

# 18. Instantaneous и extended Events

Некоторые Events представлены как практически мгновенные:

    circuit breaker tripped

Другие MAY иметь extended duration:

    battle occurred from T1 to T2

или:

    storm affected region for six hours

Extended Event MAY содержать:

- subevents;
- Actions;
- Processes;
- State transitions.

Extended Event representation не означает отсутствия внутренней Process structure.

---

# 19. Repeated Events

Повторяющиеся occurrences не становятся автоматически одним Event.

    alarm at T1
    alarm at T2
    alarm at T3

MAY быть тремя Events.

Но aggregate representation MAY использоваться:

    repeated alarms occurred overnight

если individual identities не materially важны.

Если segmentation неизвестна:

    unknown segmentation
    ≠ one Event automatically

    unknown segmentation
    ≠ many Events automatically

---

# 20. Event sequence

Events MAY иметь temporal relations:

- before;
- after;
- overlaps;
- begins before;
- ends after;
- simultaneous;
- approximately simultaneous.

Но:

    E1 before E2
    ≠ E1 caused E2

И:

    simultaneous
    ≠ causally connected automatically

Temporal chain MUST NOT автоматически становиться causal chain.

---

# 21. Simultaneity

Same recorded timestamp не доказывает exact simultaneity.

Timestamp equality MAY отражать:

- rounding;
- clock resolution;
- synchronization limitations;
- batching;
- missing precision.

Следовательно:

    same timestamp
    ≠ exact simultaneity automatically

---

# 22. Event time

Необходимо различать, когда materially relevant:

- occurrence time;
- start time;
- end time;
- effective time;
- detection time;
- observation time;
- announcement time;
- report time;
- record creation time;
- import time.

Они MUST NOT автоматически отождествляться.

Например:

    occurred at T1
    detected at T2
    reported at T3

---

# 23. Institutional/system effective time

Для institutional и system Events occurrence/effective time MAY отличаться от:

- Decision time;
- approval time;
- registration time;
- publication time;
- announcement time;
- record time.

Например:

    treaty signed at T1
    entered into force at T2

Это разные temporal semantics.

---

# 24. Temporal uncertainty

Event time MAY быть:

- exact;
- approximate;
- bounded;
- interval;
- relative;
- disputed;
- unknown.

Приблизительная дата MUST NOT превращаться в exact date без основания.

---

# 25. Spatial semantics

Необходимо различать:

- occurrence location;
- origin location;
- observation location;
- reporting location;
- participant location;
- affected area;
- other Profile-defined spatial roles.

Например:

    explosion occurred at Facility A
    observed from Hill B
    effects reached District C

Core не вводит один универсальный:

    Event.location

без определения location role.

---

# 26. Event Scope

**Event Scope** — область непосредственного occurrence или extent, включённая в Event representation.

Event Scope MAY включать:

- spatial extent;
- objects;
- systems;
- population;
- system components;
- другие extent dimensions.

Temporal extent хранится как temporal semantics и MAY участвовать в общей boundary representation, но не должна автоматически смешиваться с другими Scope dimensions.

Unknown Scope MUST NOT становиться:

- global;
- complete;
- unrestricted;
- all-inclusive.

---

# 27. Event Scope ≠ Effect Scope

Необходимо различать:

    Event Scope
    → extent самого occurrence

    Effect Scope
    → что оказалось затронуто downstream effects

Например:

    Event:
    explosion at plant

    Event Scope:
    plant

    Effect Scope:
    surrounding district

Они не наследуют друг друга автоматически.

---

# 28. Participants

Event MAY иметь participants, objects или systems involved.

Но participation является role-qualified semantics.

Возможные роли:

- direct participant;
- Actor;
- affected object;
- observer;
- victim;
- responder;
- initiator;
- system component;
- other Profile-defined role.

Generic:

    involved in Event

MUST NOT заменять более точную materially relevant participant role, если такая distinction известна и важна.

Participation MUST NOT автоматически означать:

- causation;
- responsibility;
- intention;
- control;
- authorship.

---

# 29. Actor not applicable ≠ Actor unknown

Для некоторых Events Actor concept не применим.

Например:

    earthquake

В других случаях Actor MAY существовать, но быть неизвестным.

Следовательно:

    Actor not applicable
    ≠ Actor unknown

И:

    no Actor
    ≠ incomplete Event

Natural Event не требует Actor attribution.

---

# 30. Natural Events

Event MAY быть полностью природным.

Например:

- earthquake;
- lightning strike;
- volcanic eruption;
- flood onset;
- meteor impact.

Такие Events не требуют Decision, Action или Actor.

---

# 31. Technical / system Events

Technical или system Event MAY включать:

- reboot;
- timeout;
- fault;
- threshold crossing;
- state transition;
- connection loss;
- service restoration.

Но:

    log record
    ≠ underlying Event automatically

    alert
    ≠ underlying Event automatically

    detected condition
    ≠ actual condition automatically

---

# 32. Log Event ≠ logged Event

Создание log entry само MAY быть Event.

Например:

    Event E1:
    system emitted log entry

Но содержание log entry:

    "motor failure"

MAY быть Claim/Evidence about another Event E2.

Следовательно:

    log-generation Event
    ≠ system or physical Event described by log

---

# 33. Sensor layers

Необходимо различать:

    physical Event
    system Event
    sensor detection Event
    sensor notification/log Event
    Observation/Measurement

Например:

    physical threshold crossing

и:

    alarm emitted

могут быть разными Events.

Они MAY быть связаны, но MUST NOT автоматически схлопываться.

---

# 34. Detection ≠ occurrence

    detected at T2
    ≠ occurred at T2 automatically

Late detection MUST NOT переписывать occurrence time.

---

# 35. No detection ≠ no Event

    no sensor detection
    ≠ Event did not occur automatically

Это зависит от:

- detection capability;
- coverage;
- reliability;
- calibration;
- Context.

И наоборот:

    sensor detection
    ≠ underlying Event verified automatically

---

# 36. Institutional Events

Некоторые Events имеют institutional/normative nature:

- office became vacant;
- treaty entered into force;
- organization dissolved;
- registration completed;
- legal status changed.

Такие Events MAY зависеть от governance semantics.

Но institutional Event MUST NOT автоматически означать unrelated physical change.

---

# 37. Decision and constitutive Event

Decision MAY конституировать institutional/normative State.

Если applicable governance semantics определяет:

    Decision D
    → status changes at T

изменение статуса MAY быть представлено как Event.

Но:

    Decision
    ≠ Event

И:

    Decision time
    ≠ Event/effective time automatically

---

# 38. Action-generated Event

Action MAY быть связан с Event.

Например:

    Action:
    operator activated igniter

    Event:
    ignition occurred

Но:

    Action occurred
    ≠ Event occurred automatically

И:

    Event occurred
    ≠ Action caused Event automatically

Связь требует отдельной relational/causal semantics.

---

# 39. Cause

Cause не является mandatory intrinsic field Event.

Event MAY иметь:

- one attributed cause;
- multiple causes;
- contributing factors;
- unknown cause;
- disputed cause;
- model-relative causal explanation;
- отсутствие meaningful singular cause.

Causal attribution является отдельным relational knowledge.

---

# 40. Causal provenance principle

Любая causal relation/attribution должна, когда materially relevant, сохранять:

- provenance;
- uncertainty;
- scope;
- causal meaning;
- model assumptions;
- temporal context.

Следовательно:

    causal relation/attribution
    ≠ timeless unquestionable fact automatically

Causality MAY быть:

- directly supported;
- inferred;
- modeled;
- probabilistic;
- disputed;
- reconstructed.

---

# 41. Temporal sequence ≠ causality

Фундаментальное правило:

    E1 happened before E2
    ≠ E1 caused E2

Также:

    immediately before
    ≠ caused

    correlated with
    ≠ caused

    associated with
    ≠ caused

---

# 42. Trigger semantics

Event E1 MAY trigger Event E2.

Но:

    E1 triggered E2
    ≠ E1 caused every downstream consequence of E2

Trigger relation должна иметь defined semantics и не должна незаметно усиливаться до sole/full causality.

---

# 43. Multi-causality

Event MAY иметь несколько contributing causes.

Например:

    equipment condition
    +
    operator Action
    +
    weather
    +
    system configuration
    →
    Event E

Ни один contributor не получает complete causal attribution автоматически.

---

# 44. Unknown cause

Unknown cause MUST NOT заменяться plausible cause.

Следовательно:

    cause unknown
    ≠ random

    cause unknown
    ≠ natural

    cause unknown
    ≠ human-caused

    cause unknown
    ≠ no cause

---

# 45. Result relation

Event MAY играть роль Result относительно:

- Action;
- Process;
- Decision implementation;
- Intervention;
- experiment;
- other reference frame.

Но:

    Event
    ≠ Result intrinsically

Result relation должна быть separately represented.

---

# 46. Consequence relation

Event MAY быть Consequence другого Event, Action или Process.

Но Consequence status требует consequential attribution.

    Event after X
    ≠ Consequence of X automatically

---

# 47. Effect

Effect является boundary concept относительно Event.

Необходимо различать:

    Event
    ≠ Effect

    Effect
    ≠ Consequence automatically

    Event Scope
    ≠ Effect Scope

`009` не определяет полную ontology Effect/Consequence.

---

# 48. Severity

Event severity не является universal intrinsic property.

Severity зависит от:

- metric;
- Profile;
- domain;
- affected population;
- duration;
- consequences;
- comparison baseline.

Поэтому:

    Event.severity = high

не должно использоваться без defined semantics.

Severity MAY быть Assessment.

---

# 49. Significance

Historical, social, scientific или operational significance является evaluative semantics.

Следовательно:

    occurred
    ≠ significant

    widely reported
    ≠ significant automatically

    large
    ≠ important for all purposes

---

# 50. Event existence ≠ explanation

Event representation сама по себе не означает, что известно:

- почему он произошёл;
- кто его вызвал;
- был ли он intentional;
- был ли preventable;
- был ли inevitable;
- кто несёт responsibility;
- что он означает.

Occurrence и explanation должны оставаться различимыми.

---

# 51. Unknown, partial и disputed semantics

Unknown, partial или disputed Event semantics MUST NOT заменяться:

- invented;
- default;
- current;
- merely plausible semantics.

Например:

    cause unknown
    ≠ plausible cause

    exact time unknown
    ≠ guessed exact time

    location partial
    ≠ exact location

    participant unknown
    ≠ no participant automatically

    disputed
    ≠ false automatically

---

# 52. Disputed occurrence

Сам факт occurrence MAY быть disputed.

Система MUST позволять сохранять:

- Claim that Event occurred;
- Claim that Event did not occur;
- competing reconstructions;
- uncertainty;
- provenance.

Event Record MAY представлять occurrence, историческая реальность которого uncertain или disputed.

Следовательно:

    Event Record exists
    ≠ occurrence proven

Record existence является representational fact, а не epistemic guarantee occurrence.

---

# 53. Event confidence

`009` не вводит universal intrinsic:

    Event.confidence

Uncertainty MAY представляться через:

- Claims;
- Evidence;
- Assessments;
- provenance;
- Profile-defined mechanisms.

---

# 54. Predicted Event

Prediction:

    storm will occur tomorrow

не является occurred Event.

Prediction MAY быть Claim / Inference / Assessment.

Следовательно:

    predicted
    ≠ occurred

---

# 55. Planned Event

External systems MAY использовать слово `event` для будущего scheduled occurrence.

Но `009` Core представляет occurrence как happened.

Следовательно:

    planned/scheduled Event
    ≠ occurred Event

Planning/calendar semantics должны оставаться отдельными.

---

# 56. Counterfactual Event

Statements:

    E would have occurred if X

не являются historical Event Records.

Это counterfactual Claim/Inference.

Следовательно:

    counterfactual Event description
    ≠ occurred Event

---

# 57. Cancellation

Если planned occurrence отменено до начала:

    cancelled planned occurrence
    ≠ occurred planned Event

Но:

    cancellation

MAY сама быть отдельным Event.

---

# 58. Event probability

Необходимо различать:

    probability before occurrence
    ≠ occurrence

И:

    Event occurred
    ≠ Event was likely beforehand

Prior probability MAY принадлежать Assessment/Inference, а не Event ontology.

---

# 59. Preventability

Preventability является evaluative/counterfactual semantics.

    Event occurred
    ≠ Event preventable

Preventability MAY требовать:

- causal analysis;
- counterfactual reasoning;
- Assessment.

---

# 60. Inevitability

Likewise:

    Event occurred
    ≠ Event inevitable

И:

    cause known
    ≠ inevitable

Inevitability требует отдельного reasoning.

---

# 61. Intention

Event MAY быть:

- intended downstream effect;
- unintended effect;
- accidental occurrence;
- natural occurrence;
- mixed case.

Но:

    human involved
    ≠ Event intended

    foreseeable
    ≠ intended

    caused by Action
    ≠ desired

---

# 62. Responsibility

Event representation MUST NOT автоматически назначать:

- responsibility;
- fault;
- liability;
- moral blame.

Например:

    accident occurred
    ≠ participant P responsible

Responsibility требует отдельной governance/legal/ethical/evidential semantics.

---

# 63. Event reconstruction

Historical Event MAY быть reconstructed из нескольких Sources.

Reconstruction MUST сохранять materially relevant:

- provenance;
- uncertainty;
- temporal bounds;
- spatial bounds;
- competing interpretations;
- reconstruction status.

Reconstructed Event MUST NOT masquerade as directly observed Event.

---

# 64. Damaged archives

Fragment:

    "... bridge ... fell ..."

MAY поддерживать partial Event reconstruction.

Но отсутствующие:

- date;
- cause;
- exact object;
- exact place;
- participants;

MUST NOT изобретаться.

Partial knowledge is preferable to invented completion.

---

# 65. Duplicate reports

Multiple reports MAY описывать один Event.

Один report MAY описывать несколько Events.

Следовательно:

    report cardinality
    ≠ Event cardinality

Duplicate reports MUST NOT создавать duplicate Events автоматически.

---

# 66. Event clustering

Related Events MAY группироваться для:

- анализа;
- UI;
- historical narrative;
- incident review.

Но:

    cluster
    ≠ one Event automatically

Grouping MUST NOT уничтожать individual Event identities, если они materially важны.

EventCluster Entity не требуется.

---

# 67. Event series

Последовательность похожих Events MAY быть представлена как:

- individual Events;
- series;
- Process;
- aggregate representation.

Но:

    same type
    ≠ one Event

И:

    series
    ≠ Process automatically

---

# 68. Beginning and end Events

Process MAY иметь:

    start Event
    end Event

Но отсутствие отдельно зарегистрированного start/end Event не доказывает отсутствие Process.

Process beginning или termination MAY быть gradual.

---

# 69. Threshold Events

Некоторые Events определяются threshold crossing.

Например:

    temperature exceeded 100°C

Event identity MAY зависеть от:

- variable;
- threshold;
- direction;
- occurrence time;
- measurement semantics.

Repeated crossings MAY быть отдельными Events.

Measurement uncertainty MAY делать exact transition time uncertain.

---

# 70. State-transition Events

Event MAY представляться как:

    State S1
    → State S2

Но observed snapshots:

    S1 @ T1
    S2 @ T2

MUST NOT автоматически materialize exact transition Event.

Transition MAY быть:

- inferred;
- gradual;
- multiple;
- uncertain.

---

# 71. Impossible / erroneous Event descriptions

Historical Source MAY сообщать occurrence, который современное знание считает невозможным или ошибочным.

Например:

    Source reports:
    the sun fell from the sky

Это MAY быть:

- historical Claim;
- metaphor;
- misconception;
- report about another Event.

Source content MUST NOT автоматически materialize canonical physical Event.

---

# 72. Event correction

Correction исправляет representation того же occurrence.

Например:

    recorded date: 12 May
    corrected date: 13 May

MAY быть Correction, если evidence относится к тому же Event.

Но новый occurrence того же типа является новым Event.

    correction
    ≠ new Event

---

# 73. Historical-state preservation

Event MUST NOT silently inherit current States участников или referenced objects.

Например:

    City boundary@T1
    ≠ City boundary@current

    Organization@T1
    ≠ Organization@current

    Device version@T1
    ≠ Device version@current

Если historical State materially влияет на interpretation, он должен оставаться resolvable.

---

# 74. Event relations

Events MAY иметь relations:

- before;
- after;
- overlaps;
- triggers;
- causes;
- contributes to;
- prevents;
- interrupts;
- begins;
- ends;
- part of;
- associated with;
- other Profile-defined relations.

`009` SHOULD использовать generic project relation infrastructure.

Relation label MUST NOT иметь более сильную semantics, чем реально represented.

Generic relation, например:

    associated with

SHOULD NOT заменять более точную known relation, если различие materially relevant.

---

# 75. Relation provenance

Relation между Events является самостоятельной knowledge semantics.

Она MAY быть:

- directly observed;
- recorded;
- inferred;
- computed;
- reconstructed;
- disputed.

Materially relevant provenance должна сохраняться.

Следовательно:

    observed sequence
    ≠ proven causation

    inferred common cause
    ≠ recorded common cause

    computed overlap
    ≠ historically asserted overlap

---

# 76. Relation symmetry / transitivity

Core MUST NOT предполагать universal symmetry или transitivity.

Например:

    E1 overlaps E2
    E2 overlaps E3

не означает:

    E1 overlaps E3

И causal transitivity также требует отдельно определённой semantics.

---

# 77. Event chains

Event chain MAY быть аналитически полезен.

Но:

    temporal chain
    ≠ causal chain

    narrative chain
    ≠ causal chain

    process sequence
    ≠ causal chain automatically

---

# 78. Observation provenance

Если Event основан на Observation, необходимо различать:

- Event occurrence;
- observation act;
- measurement/data;
- interpretation;
- Event inference.

Например:

    sensor recorded pressure spike

не означает автоматически:

    explosion occurred

Sensor record MAY быть Evidence for Event Claim.

---

# 79. Missing evidence

Absence of Event evidence не доказывает отсутствие occurrence.

    no record
    ≠ no Event

Но и:

    plausible Event
    ≠ Event occurred

Обе стороны должны сохраняться.

---

# 80. Import

External systems MAY использовать labels:

- event;
- incident;
- occurrence;
- alert;
- accident;
- failure;
- episode;
- transition.

External label MUST NOT автоматически определять canonical Event.

Semantic function determines mapping.

---

# 81. Event vs Incident

`Incident` MAY быть domain/Profile concept.

Core не вводит universal Incident subtype.

---

# 82. Event vs Accident

Accident часто включает дополнительные semantics:

- unintendedness;
- harm;
- operational context;
- insurance/legal meaning.

Поэтому:

    Accident label
    ≠ neutral Event semantics automatically

Отдельный Accident subtype Core не требуется.

---

# 83. Event vs Disaster

Disaster включает severity/social/evaluative semantics.

Не каждый Event является Disaster.

Disaster classification MAY быть Assessment/Profile concept.

---

# 84. Event vs Failure

Failure MAY быть:

- Event;
- State;
- Result;
- Assessment relative to expected function.

Например:

    component stopped functioning
    → Event MAY be appropriate

Но:

    mission failed
    → Result/Assessment MAY be more appropriate

Core не вводит universal Failure ontology.

---

# 85. Event vs Error

Error MAY обозначать:

- mistaken Action;
- technical Event;
- incorrect State;
- deviation;
- Assessment.

External term `error` MUST NOT автоматически определять ontology.

---

# 86. Representation Fidelity

Representation MUST NOT materially изменять:

- what happened;
- occurrence status;
- time;
- location;
- Scope;
- participants;
- Event/Action distinction;
- causal status;
- uncertainty;
- provenance;
- relation semantics.

---

# 87. Historical Event ≠ current warning/instruction

Historical:

    flood occurred in 1920

не означает:

    flood will occur now

или:

    evacuate now

Historical Event MUST NOT автоматически превращаться в:

- Recommendation;
- warning;
- prediction;
- Instruction.

---

# 88. Translation Fidelity

Translation MUST сохранять materially relevant Event semantics.

Необходимо различать:

    occurred
    ≠ may have occurred

    began
    ≠ ended

    one
    ≠ several

    before
    ≠ after

    caused
    ≠ followed

    affected
    ≠ occurred in

    reportedly occurred
    ≠ occurred with certainty

---

# 89. Passive/agentless wording

Translation или summarization MUST NOT добавлять Actor или cause, отсутствующие в Source.

Например:

    "The bridge was destroyed"

MUST NOT автоматически становиться:

    "Army X destroyed the bridge"

без independent attribution.

---

# 90. Logical Fidelity

Representation SHOULD сохранять materially relevant:

- negation;
- quantifiers;
- exclusions;
- alternatives;
- conditionality;
- temporal ordering;
- uncertainty.

Например:

    no explosion occurred
    ≠ explosion occurred

    at least three Events
    ≠ exactly three Events

    before midnight
    ≠ after midnight

---

# 91. Representation compression

Summary MAY опускать non-material details.

Но omission MUST NOT превращать:

    reported Event
    → certain Event

    local Event
    → global Event

    partial Scope
    → complete Scope

    possible cause
    → established cause

    multiple Events
    → one Event

---

# 92. Offline preservation

Event SHOULD представляться так, чтобы materially relevant semantics могла быть восстановлена без зависимости от конкретной современной платформы.

Где возможно, SHOULD сохраняться:

- Event Content;
- temporal information;
- spatial roles;
- Scope;
- participants;
- provenance;
- uncertainty;
- historical States;
- relations.

Completeness MUST NOT достигаться invented semantics.

---

# 93. Carrier neutrality

Event semantics не зависит от carrier.

Event MAY быть сохранён в:

- database;
- Markdown;
- JSON;
- printed archive;
- sensor log;
- chronicle;
- other durable representation.

Carrier не определяет ontology Event.

---

# 94. High-risk Profiles

High-risk Profiles MAY требовать более строгую Event representation для:

- accidents;
- epidemics;
- industrial incidents;
- medical adverse events;
- disasters;
- cyber incidents.

Profile MAY требовать:

- bounded/exact time;
- location roles;
- affected Scope;
- causal uncertainty;
- severity Assessment;
- provenance;
- monitoring data;
- participant roles.

Но эти требования не становятся universal Core.

---

# 95. Event quality

`009` не вводит intrinsic Event Quality.

Понятия:

- severity;
- significance;
- preventability;
- detectability;
- impact;
- novelty;
- relevance;

обычно являются Assessment/Profile semantics.

---

# 96. Conformance и Integrity

Необходимо различать:

    Core structural/semantic conformance
    ≠ historical/provenance integrity
    ≠ occurrence certainty
    ≠ causal certainty
    ≠ Event significance
    ≠ Representation Fidelity

Core Conformance отвечает на вопрос, соответствует ли Event требованиям `009`.

Historical/Provenance Integrity отвечает на вопрос, насколько честно сохранены:

- Sources;
- reconstruction;
- uncertainty;
- historical States;
- disputed semantics.

Следовательно:

    Core PASS
    ≠ Event certainly occurred
    ≠ cause known
    ≠ Event important
    ≠ Event correctly explained

---

# 97. Profiles

Profile MAY усиливать Core requirements.

Profile MUST NOT ослаблять Core, продолжая заявлять compatibility с `009`.

---

# 98. Диагностические семейства

Diagnostic terminology описывает semantic failure patterns и не создаёт Core Entities.

## 98.1. Identity / granularity failures

Примеры:

- one Event split into many without basis;
- multiple Events collapsed;
- repeated Events aggregated improperly;
- Correction represented as new Event;
- same time/place treated as identity.

## 98.2. Temporal / spatial failures

Примеры:

- occurrence time → report time;
- detection time → occurrence time;
- approximate time → exact time;
- observation location → occurrence location;
- Event Scope → Effect Scope.

## 98.3. Attribution / provenance failures

Примеры:

- reported → observed;
- reconstructed → directly recorded;
- disputed → certain;
- passive wording → invented Actor;
- unknown Actor → no Actor.

## 98.4. Causality failures

Примеры:

- before → caused;
- correlation → causation;
- trigger → sole cause;
- participant → responsible actor;
- plausible cause → known cause.

## 98.5. Representation / import failures

Примеры:

- planned Event → occurred Event;
- predicted Event → historical Event;
- Source label → canonical Event without analysis;
- duplicate reports → duplicate Events;
- one report → one Event automatically.

Diagnostic label сам по себе не устанавливает:

- fraud;
- intent;
- negligence;
- responsibility;
- blame.

---

# 99. Machine validation

Validator MAY проверять:

- required structure;
- reference integrity;
- temporal format;
- Profile requirements;
- logical consistency;
- candidate duplicates.

Но:

    validator PASS
    ≠ Event certainly occurred
    ≠ cause established
    ≠ Event correctly interpreted
    ≠ Event significant

Validator не обладает privilege of truth и сам MAY быть ошибочным.

---

# 100. Cross-standard compatibility

`009-EVENT` должен сохранять границы соседних Records и semantics.

В компактной форме:

    Claim
    → что утверждается

    Evidence Use
    → что используется как evidence

    Assessment
    → как что-либо оценивается

    Inference
    → что выводится

    Decision
    → что решено

    Action
    → что сделано

    Event
    → что произошло

    Result
    → downstream role относительно reference frame

Следовательно:

    Claim about Event
    ≠ Event

    Action associated with Event
    ≠ Event

    Process containing Event
    ≠ Event

    State before/after Event
    ≠ Event

    Event used as Result
    ≠ Event intrinsically Result

`009` не должен поглощать ontology соседних стандартов.

---

# 101. Boundary concepts outside full 009 ontology

`009` использует соседние concepts только для определения границ Event.

К ним относятся:

- State;
- Process;
- Result;
- Effect;
- Consequence;
- Observation;
- Incident;
- Accident;
- Disaster;
- Failure.

`009` не утверждает, что их полная ontology должна находиться внутри Event standard.

---

# 102. Entity Explosion Test

`009` НЕ требует введения следующих фундаментальных Core Entities только ради представления Event:

- EventContent;
- EventParticipant;
- EventContext;
- EventScope;
- EventLocation;
- EventTime;
- EventCause;
- EventEffect;
- EventResult;
- EventConsequence;
- EventSeries;
- EventChain;
- EventCluster;
- CompositeEvent;
- RepeatedEvent;
- ContinuousEvent;
- NaturalEvent;
- TechnicalEvent;
- InstitutionalEvent;
- ThresholdEvent;
- StateTransitionEvent;
- Incident;
- Accident;
- Disaster;
- FailureEvent;
- EventSeverity;
- EventSignificance;
- EventConfidence.

Эти concepts MAY быть представлены через:

- semantic roles;
- relations;
- States;
- Profiles;
- existing Records;
- generic infrastructure;
- future standards.

Отсутствие отдельной Core Entity не означает отсутствия соответствующей semantics.

---

# 103. Core invariants

Следующие положения образуют минимальное нормативное ядро `009-EVENT`.

### E-01
Event является specialized Record, представляющим defined occurrence с temporal occurrence/boundary semantics, представленное как произошедшее.

### E-02
Event MUST иметь defined Event Content.

### E-03
Event MUST сохранять sufficient event attribution как temporal occurrence / transition / boundary semantics.

### E-04
Event attribution является semantic requirement и MUST NOT требовать отдельной Core Entity только ради соответствия `009`.

### E-05
Mere State attribution MUST NOT автоматически составлять Event.

### E-06
State difference MUST NOT самостоятельно определять Event count, identity, granularity, mechanism или exact transition time.

### E-07
Event MUST оставаться различимым от Claim, Action, Process, State, Observation и Result.

### E-08
Existence Event Record MUST NOT автоматически означать epistemic certainty occurrence.

### E-09
Same Event Content MUST NOT автоматически означать same Event.

### E-10
Different wording или abstraction MUST NOT автоматически создавать different Event identities.

### E-11
Same time and place MUST NOT автоматически означать same Event.

### E-12
Duration, complexity или internal subchanges MUST NOT индивидуально определять Event vs Process.

### E-13
Composite Event MUST NOT выводиться только из causality, temporal proximity, shared location или shared Source.

### E-14
Purpose MAY влиять на representation/granularity, но MUST NOT сам по себе определять underlying Event identity.

### E-15
Repeated occurrences MUST NOT автоматически считаться one Event.

### E-16
Unknown segmentation MUST NOT автоматически означать one Event или many Events.

### E-17
Occurrence time, effective time, detection time, observation time, report time и record time MUST оставаться различимыми when material.

### E-18
Occurrence location, observation location, reporting location и Effect Scope MUST оставаться различимыми when material.

### E-19
Event Scope MUST оставаться различимым от temporal extent и Effect Scope when material.

### E-20
Participation MUST оставаться role-qualified when materially relevant.

### E-21
Participation MUST NOT автоматически означать causation, responsibility, intention или control.

### E-22
Natural Event MUST NOT требовать Actor attribution.

### E-23
Actor not applicable MUST оставаться различимым от Actor unknown.

### E-24
System log, alert или detection MUST NOT автоматически считаться underlying Event.

### E-25
Temporal succession или correlation MUST NOT автоматически интерпретироваться как causation.

### E-26
Causal relations/attributions MUST сохранять materially relevant provenance, uncertainty, scope и semantics.

### E-27
Trigger relation MUST NOT автоматически означать sole/full downstream causation.

### E-28
Unknown cause MUST NOT заменяться plausible cause.

### E-29
Event MUST NOT автоматически считаться Result какого-либо Action, Process или other reference frame.

### E-30
Event MUST NOT автоматически считаться Consequence другого occurrence.

### E-31
Unknown, partial или disputed Event semantics MUST NOT заменяться invented, default, current или merely plausible semantics.

### E-32
Event Record MAY представлять disputed/uncertain occurrence; Record existence MUST NOT рассматриваться как доказательство occurrence.

### E-33
Counterfactual, predicted или planned occurrence MUST NOT автоматически представляться как occurred historical Event.

### E-34
Source/report cardinality MUST NOT определять Event cardinality.

### E-35
Distinct semantic Records MUST NOT автоматически считаться distinct underlying occurrences.

### E-36
Historical Event semantics MUST NOT silently drift to current States связанных objects, systems или institutions.

### E-37
Correction MUST сохранять identity того же occurrence; новый occurrence MUST быть новым Event.

### E-38
Event relations MUST сохранять materially relevant provenance.

### E-39
Relation symmetry или transitivity MUST NOT предполагаться универсально.

### E-40
Generic relation SHOULD NOT заменять более точную известную relation, если distinction materially relevant.

### E-41
Representation MUST NOT silently upgrade reported, inferred или reconstructed Event to directly observed/certain Event.

### E-42
Translation или summarization MUST NOT вводить Actor, cause, precision или certainty, отсутствующие в Source.

### E-43
Historical Event MUST NOT автоматически становиться current Recommendation, warning, Instruction или prediction.

### E-44
Core structural/semantic conformance MUST оставаться различимым от historical/provenance integrity, occurrence certainty, causal certainty, significance и Representation Fidelity.

### E-45
Profile MAY усиливать Core requirements, но MUST NOT ослаблять Core, продолжая заявлять compatibility с `009`.

### E-46
Materially relevant uncertainty и provenance MUST оставаться resolvable.

---

# 104. Stress-test framework

Архитектура `009-EVENT` должна выдерживать как минимум следующие классы атак:

1. Event с unknown cause;
2. natural Event without Actor;
3. Actor unknown vs Actor not applicable;
4. disputed occurrence;
5. Event known only through Claim;
6. Event vs Action;
7. same underlying occurrence represented as Action + Event;
8. distinct semantic Records vs occurrence count;
9. Event vs Process;
10. extended Event;
11. Event vs State;
12. State snapshots without known transition;
13. Event vs Result;
14. Event vs Consequence;
15. Event vs Observation;
16. composite Events;
17. repeated Events;
18. uncertain segmentation;
19. uncertain boundaries;
20. same timestamp ≠ same Event;
21. same time/place ≠ same Event;
22. occurrence time ≠ detection/report time;
23. institutional effective time;
24. observation location ≠ occurrence location;
25. Event Scope ≠ Effect Scope;
26. temporal extent ≠ Event Scope automatically;
27. role-qualified participation;
28. technical/system Events;
29. log Event vs logged Event;
30. sensor detection;
31. absence of detection;
32. institutional Events;
33. constitutive Decision-generated Events;
34. Action-generated Events;
35. multiple causes;
36. unknown cause;
37. sequence without causality;
38. trigger without sole causation;
39. causal model uncertainty;
40. Result role;
41. Consequence role;
42. duplicate reports;
43. one report describing multiple Events;
44. Event clustering;
45. Event series;
46. threshold Events;
47. State-transition reconstruction;
48. predicted Events;
49. planned Events;
50. counterfactual Events;
51. cancellation;
52. historical reconstruction;
53. damaged archives;
54. impossible historical reports;
55. import-label ambiguity;
56. Incident / Accident / Disaster / Failure terminology;
57. passive wording;
58. translation corruption;
59. generic vs specific relations;
60. historical-state drift;
61. high-risk Profiles;
62. future-system Events;
63. offline preservation;
64. cross-standard collisions.

Stress-test cases не создают Core requirements самостоятельно.

Если новый test выявляет необходимое фундаментальное правило, оно должно быть внесено в соответствующий normative section.

Прохождение stress-test не является доказательством полноты или окончательности модели.

---

# 105. Принцип сохранения

При конфликте между полнотой и честностью representation предпочтение отдаётся честности.

    partial occurrence knowledge
    > invented completion

    approximate time
    > invented exact time

    unknown cause
    > plausible invented cause

    disputed Event
    > false certainty

    reported Event
    > falsely observed Event

    multiple plausible reconstructions
    > forced single narrative

    uncertain Event granularity
    > invented Event count

Цель стандарта — сохранить Event настолько полно, насколько позволяют данные, **не выдавая неизвестное за известное и не превращая State difference, sequence, participation, report или interpretation в Event identity, causality, responsibility или certainty**.

---

# 106. Итоговая формула

В наиболее компактной форме:

    Decision
    → что было решено

    Action
    → что было сделано

    Event
    → что произошло

    Result
    → что рассматривается как downstream result
      относительно reference frame

    Assessment
    → как это оценивается

    Inference
    → что из этого выводится

Центральный принцип `009-EVENT`:

> **Сохранить Event — значит сохранить максимально честное представление о том, что представлено как произошедшее, какие temporal/spatial границы этому occurrence могут быть обоснованно приписаны и какие uncertainty, provenance и relations с ним связаны.**

Факт Event сам по себе не означает известность причины, Actor, намерения, ответственности, значимости, Result status или причинность последующих Events.

---

## Статус версии

**009-EVENT v0.1**

Архитектура прошла:

- первичную полную сборку;
- сквозную атаку всего стандарта;
- контрольный аудит собранного файла;
- проверку Event / Action;
- проверку Event / Process;
- усиленную проверку Event / State;
- проверку Event / Result;
- проверку Event / Observation;
- проверку identity / granularity;
- проверку composite и repeated Events;
- проверку temporal / spatial semantics;
- проверку Natural и Technical/System Events;
- проверку institutional Events;
- проверку causal boundaries;
- проверку disputed и reconstructed Events;
- проверку compatibility с `007-DECISION` и `008-ACTION`;
- Entity Explosion Test.

**Критических архитектурных противоречий: 0.**  
**Новых обязательных Core Entities: 0.**  
**Невнесённых замечаний контрольного аудита: 0.**

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.
