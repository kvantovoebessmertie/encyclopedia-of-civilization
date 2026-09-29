# 013 — RELATION
## Стандарт представления отношений

**Проект:** Энциклопедия цивилизации  
**Статус:** действующий базовый стандарт  
**Версия:** 0.1  
**Совместимость:** FOUNDATION / CORE MODEL / действующие стандарты проекта

---

# 0. Назначение

Этот стандарт определяет, как в Энциклопедии цивилизации представляются Relations — семантические связи между определённый semantic positions, participants, records, entities, values или другими referenceable elements.

Relations используются для представления таких семантик, как:

- part-of;
- contains;
- located-in;
- precedes;
- follows;
- overlaps;
- associated-with;
- depends-on;
- supports;
- contradicts;
- derived-from;
- based-on;
- refers-to;
- participates-in;
- affects;
- caused-by;
- enables;
- inhibits;
- corresponds-to;
- same-as;
- similar-to;
- version-of;
- replaces;
- supersedes;
- other domain-specific relations.

Цель стандарта — позволить сохранять:

- какая Relation представлена;
- является ли representation Relation type, Relation model или Relation instance;
- какие semantic positions участвуют в Relation;
- какие participants занимают эти positions;
- каковы participant roles;
- какова arity Relation;
- направлена ли Relation;
- какие formal properties определены для её type/frame;
- в какой applicable frame Relation представлена;
- каков Scope Relation;
- когда Relation применима, если temporal validity материально relevant;
- при каких условиях Relation считается действующей;
- какие qualifiers материально relevant;
- является ли Relation asserted, observed, measured, computed, inferred, modeled или reconstructed;
- насколько Relation определена;
- какие uncertainty и provenance существуют;
- может ли Relation быть contested;
- относится ли Relation к object/domain layer, knowledge layer или meta-model layer.

Стандарт не предназначен для автоматического определения:

- истинности Relation;
- причинности;
- направления causality;
- симметрии;
- транзитивности;
- reflexivity;
- equivalence;
- identity;
- coreference;
- part-whole structure;
- temporal order;
- responsibility;
- authority;
- support strength;
- contradiction;
- dependency;
- ownership;
- similarity;
- quantification;
- того, что Relation сохраняется во времени;
- того, что generic/class-level Relation действует для каждого instance;
- того, что несколько instance-level Relations образуют generic/class-level Relation;
- того, что relation, выраженная естественным языком, имеет одну универсальную canonical semantics.

Сохранить Relation означает сохранить максимально честное представление о semantic linkage между определённый semantic positions/participants в resolvable applicable frame, не превращая близость в причинность, association — в dependency, similarity — в identity, coreference — в Record identity, temporal order — в causality, generic Relation — в universal instance-level assertion, несколько instances — в generic rule, а storage edge — в canonical Relation semantics автоматически.

---

# 1. Основное понятие

## 1.1. Relation

**Relation (Отношение)** — semantic construct, представляющий определённую связь между двумя или более semantic positions, которые могут быть заняты participants, values или другими referenceable elements.

Relation отвечает на основной вопрос:

> **Как определённый semantic positions/participants связаны между собой в данной applicable frame?**

Relation МОЖЕТ быть:

- binary;
- ternary;
- n-ary;
- directed;
- undirected;
- symmetric;
- asymmetric;
- temporal;
- spatial;
- causal;
- structural;
- evidential;
- epistemic;
- logical;
- classificatory;
- normative;
- institutional;
- historical;
- statistical;
- domain-specific.

---

# 2. Relation representation ≠ Relation truth

Наличие Relation representation не означает автоматически, что представленный Relation objectively holds.

Следовательно:

    Relation representation exists
    ≠ Relation certainly holds

Relation МОЖЕТ быть:

- asserted;
- observed;
- measured;
- inferred;
- computed;
- modeled;
- reconstructed;
- hypothesized;
- disputed;
- provisional.

Epistemic/provenance status ДОЛЖЕН оставаться resolvable когда материально relevant.

---

# 3. Relation как semantic construct

Relation не обязана всегда быть отдельной фундаментальной Entity.

Relation МОЖЕТ быть представлена через:

- graph edge;
- typed reference;
- field;
- embedded structure;
- Record;
- n-ary structure;
- statement;
- relation node;
- other implementation.

Если independent identity, provenance, temporal validity, dispute handling, n-ary role structure, qualifiers или reuse материально важны, Relation МОЖЕТ быть materialized как отдельный Record.

Следовательно:

    Relation semantics
    ≠ mandatory Relation Entity

Также:

    storage edge
    ≠ canonical Relation semantics automatically

Техническая реализация данных не определяет canonical ontology проекта.

---

# 4. Relation не является универсальным контейнером любого predicate

Не каждое property, attribute или predicate обязано представляться canonical Relation.

Например:

    Person P
    height = 180 cm

МОЖЕТ технически храниться как edge:

    P → has-height → 180 cm

Но это не означает автоматически, что `имеет-height` должен становиться canonical Relation type проекта.

Следовательно:

    property
    ≠ Relation automatically

    attribute
    ≠ Relation automatically

    predicate
    ≠ canonical Relation automatically

    storage edge
    ≠ canonical Relation automatically

Relation representation уместна там, где linkage/role semantics между semantic positions материально relevant.

Implementation МОЖЕТ использовать graph edges без изменения canonical semantic classification.

---

# 5. Co-occurrence ≠ specific Relation

Факт, что два elements:

- появляются рядом в тексте;
- существуют одновременно;
- находятся рядом пространственно;
- часто упоминаются вместе;
- относятся к одной статье;
- имеют похожие properties;

не определяет canonical Relation автоматически.

Следовательно:

    co-occurrence
    ≠ specific Relation automatically

И:

    proximity
    ≠ causality
    ≠ dependency
    ≠ part-of
    ≠ similarity automatically

---

# 6. Relation type ≠ Relation model ≠ Relation instance

Необходимо различать три уровня:

    Relation type
    ≠ Relation model
    ≠ Relation instance

**Relation type** — reusable general semantics Relation.

Например:

    part-of
    causes
    located-in
    supports

**Relation model** — model-level representation структуры, поведения, ограничений, взаимодействий или hypothesized/определённый linkages одного или нескольких Relation types.

Например:

    causal graph model
    kinship model
    taxonomic model

Простое перечисление, каталогизация или документация Relation types:

    ≠ Relation model automatically

**Relation instance** — конкретная представленный Relation между определённый semantic positions/participants в applicable frame.

Например:

    Wheel W part-of Bicycle B

или:

    A owns B during T1–T2

`Relation occurrence` МОЖЕТ использоваться как более узкое domain term только для Relation instances, которым действительно присущи occurrence-like/temporally instantiated semantics.

Canonical general term в `013`:

    Relation instance

Следовательно:

    Relation type exists
    ≠ Relation instance exists

    Relation model exists
    ≠ Relation instance proven

    model edge
    ≠ represented Relation instance automatically

    Relation model
    ≠ Relation truth

---

# 7. Generic Relation knowledge ≠ specific Relation instance

Generic knowledge:

    metal МОЖЕТ react с acid

не означает автоматически:

    this historical metal object
    reacted with this acid

Likewise:

    generic Relation type/model
    ≠ specific historical Relation evidence

Transfer from generic/type-level knowledge to specific instance requires:

- Evidence;
- Inference;
- Model application;
- other justified semantics.

---

# 8. Class-level Relation ≠ universal instance-level Relation

Relation between classes/categories НЕ ДОЛЖЕН автоматически становиться universal Relation among their instances.

Например:

    birds eat insects

НЕ ДОЛЖЕН автоматически означать:

    every bird eats insects

или:

    every bird eats every insect

Generic/class-level Relation МОЖЕТ encode semantics such as:

- all;
- some;
- most;
- typically;
- often;
- sometimes;
- may;
- can;
- under defined conditions;
- probabilistically;
- other quantified/modal semantics.

материально relevant quantification ДОЛЖЕН оставаться разрешимым.

Следовательно:

    class-level Relation
    ≠ universal instance-level Relation automatically

И:

    generic Relation
    ≠ universal quantified Claim automatically

полный quantified proposition МОЖЕТ belong primarily to Claim semantics.

`013` требует that Relation representation НЕ ДОЛЖЕН erase материально relevant quantification.

---

# 9. Instance-level Relations ≠ generic Relation automatically

Наличие нескольких конкретных Relation instances:

    A1 R B
    A2 R B
    A3 R B

не устанавливает автоматически:

    Class A R B

или иной generic/class-level Relation.

Следовательно:

    multiple instance-level Relations
    ≠ class-level/generic Relation automatically

Generalization from instances requires explicit:

- Inference;
- statistical support;
- Model;
- aggregation rule;
- other justified semantics.

Так же как generic Relation не должна автоматически распространяться на каждый instance, набор instances не должен автоматически превращаться в generic rule.

---

# 10. Минимальная структура Relation

Для завершённой Relation semantics необходимо как минимум:

1. defined Relation semantics;
2. resolvable semantic positions;
3. resolvable participants/values where applicable;
4. resolvable participant roles when materially relevant;
5. sufficient Relation attribution;
6. resolvable applicable frame.

Минимальная формула:

    defined Relation semantics
    +
    resolvable semantic positions
    +
    resolvable participants
    +
    resolvable roles when material
    +
    sufficient Relation attribution
    +
    resolvable applicable frame

---

# 11. Applicable frame

Every Relation ДОЛЖЕН иметь Один resolvable applicable frame.

**Applicable frame** определяет semantic/reference system, внутри которой Relation имеет определённый смысл и может корректно интерпретироваться.

Applicable frame МОЖЕТ включать:

- semantic/domain frame;
- temporal frame;
- Context;
- jurisdiction;
- spatial/reference frame;
- ontology/taxonomy version;
- system version;
- measurement/reference conventions;
- model;
- Profile;
- other materially relevant interpretive conditions.

Not every component is universally required.

Но:

    Relation without explicit timestamp
    ≠ Relation without frame

Например:

    Dog subclass-of Mammal

МОЖЕТ требовать taxonomy/ontology frame.

А:

    A owns B

МОЖЕТ требовать temporal + jurisdictional frame.

Frame МОЖЕТ быть implicit только где Это remains unambiguous и resolvable.

---

# 12. Applicable frame ≠ Scope

Applicable frame и Scope являются связанными, но различными понятиями.

**Applicable frame** отвечает прежде всего:

> В какой semantic/reference system Relation имеет смысл и интерпретируется?

**Scope** отвечает прежде всего:

> К какой части domain, participants, population, time range или предметной области данная Relation фактически применяется?

Например:

    Relation:
    Drug A associated-with Outcome B

    Applicable frame:
    clinical-study definitions,
    measurement model,
    relevant domain conventions

    Scope:
    participants age 65+
    in cohort X

Следовательно:

    applicable frame
    ≠ Scope automatically

Некоторые сведения МОЖЕТ участвовать в обоих аспектах representation, но система ДОЛЖЕН сохранять distinction где conflation would материально alter meaning.

---

# 13. Relation semantics

**Relation semantics** — смысл связи, которую Relation представляет.

Examples:

    A part-of B

    A precedes B

    A supports Claim C

    Event E associated-with Process P

    Result R derived-from Measurement M

Relation semantics ДОЛЖЕН быть sufficiently specific, чтобы материально different relations не схлопываться into generic edge когда distinction важна.

---

# 14. Semantic positions и participants

Relation связывает semantic positions.

Positions МОЖЕТ быть заняты:

- Entity;
- Record;
- Claim;
- Source;
- State;
- Event;
- Action;
- Process;
- Result;
- Objective;
- Measurement;
- Observation;
- Value;
- Time interval;
- Location;
- other referenceable semantic element.

Core НЕ ДОЛЖЕН предполагать, что все participants имеют один ontology class.

---

# 15. Relation arity

**Arity** — число semantic positions Relation.

Следовательно:

    Relation arity
    ≠ number of distinct participant identities

Например ternary Relation МОЖЕТ иметь три semantic positions, даже если один Entity занимает две из них.

Arity belongs to Relation structure, not merely count of unique referenced objects.

---

# 16. Binary Relation

Binary Relation имеет две semantic positions.

Например:

    A located-in B

    Event E precedes Event F

    Source S supports Claim C

Binary Relation МОЖЕТ иметь различимый roles:

    container / contained

    supporter / supported

    predecessor / successor

Role semantics ДОЛЖЕН оставаться разрешимым когда material.

---

# 17. N-ary Relation

Не все Relations корректно представляются binary edge.

Example:

    A owes B amount X under Contract C

может требовать:

- debtor;
- creditor;
- amount;
- contract;
- temporal validity.

Likewise:

    Person P administered Substance S
    to Person Q
    at Time T
    by Route R

может быть n-ary structure.

Core НЕ ДОЛЖЕН принуждать every Relation into pairwise binary edges Если материально relevant semantics would быть lost.

---

# 18. N-ary decomposition

N-ary Relation МОЖЕТ быть decomposed into binary relations только Если decomposition preserves материально relevant semantics.

Следовательно:

    n-ary Relation
    ≠ arbitrary set of binary edges automatically

Example:

    A owes B $100 under Contract C

cannot safely become only:

    A related-to B
    A related-to $100
    A related-to C

without preserving roles and qualifiers.

---

# 19. Participant roles

Relation positions МОЖЕТ иметь различимый semantic roles.

Examples:

    parent / child

    source / target

    cause / effect

    owner / owned object

    evidence / supported Claim

    container / contained

Role labels НЕ ДОЛЖЕН быть omitted когда omission causes material ambiguity.

---

# 20. Participant role ≠ participant identity

Participant role является semantic role within Relation.

Следовательно:

    participant role
    ≠ participant identity

One Entity МОЖЕТ occupy different roles в different Relations.

One Entity МОЖЕТ also occupy multiple semantic positions в one Relation где Relation semantics permits Это.

---

# 21. Role ordering ≠ graph directionality

Ordered/asymmetric participant roles and graph directionality are related but not identical concepts.

Например:

    A owes B

имеет roles:

    debtor
    creditor

Но semantic meaning не исчерпывается стрелкой:

    A → B

Следовательно:

    ordered roles
    ≠ graph directionality automatically

Direction МОЖЕТ encode role ordering в an implementation, Но role semantics ДОЛЖЕН оставаться independently resolvable когда материально relevant.

---

# 22. Directionality

Relation МОЖЕТ быть directed.

Например:

    A causes B

    A contains B

    A precedes B

Direction ДОЛЖЕН быть сохранённый когда материально relevant.

Следовательно:

    A → B
    ≠ B → A automatically

---

# 23. Inverse Relation

Some Relation types МОЖЕТ иметь определённый inverse.

Например:

    A contains B
    ↔
    B part-of A

Но inverse semantics НЕ ДОЛЖЕН быть придуманный если не Relation type definition supports Это.

Следовательно:

    Relation has direction
    ≠ inverse Relation defined automatically

---

# 24. Formal properties

Formal properties МОЖЕТ включать:

- reflexive;
- irreflexive;
- symmetric;
- asymmetric;
- antisymmetric;
- transitive;
- intransitive;
- functional;
- inverse-functional;
- other defined properties.

Such properties normally characterize:

    Relation type
    within a defined frame/model

rather than one isolated Relation instance.

Следовательно:

    formal property in Frame X
    ≠ same formal property in Frame Y automatically

Core НЕ ДОЛЖЕН assign universal formal properties to Relation merely из label или intuition.

---

# 25. Symmetry

Some Relation types МОЖЕТ быть symmetric.

Например under Один определённый semantics:

    A overlaps B
    ↔
    B overlaps A

Но symmetry ДОЛЖЕН быть определённый, not предполагаемым.

---

# 26. Asymmetry

Some Relation types МОЖЕТ быть asymmetric.

Например:

    A precedes B

does not imply:

    B precedes A

Asymmetry belongs to defined Relation type/frame semantics.

---

# 27. Transitivity

Transitivity НЕ ДОЛЖЕН быть предполагаемым universally.

Например:

    A part-of B
    B part-of C

МОЖЕТ поддерживать:

    A part-of C

under some mereological models.

But:

    A knows B
    B knows C

does not imply:

    A knows C

Следовательно:

    R(A,B) + R(B,C)
    ≠ R(A,C) automatically

unless defined Relation logic licenses it.

---

# 28. Relation composition ≠ transitivity

Composition МОЖЕТ involve different Relation types.

Example:

    A parent-of B
    B parent-of C

may license:

    A grandparent-of C

This is not transitivity of `parent-of`.

Likewise:

    A located-in B
    B part-of C

МОЖЕТ или МОЖЕТ NOT license:

    A located-in C

depending on defined semantics.

Therefore:

    Relation composition
    ≠ transitivity

Heterogeneous composition rules ДОЛЖЕН быть explicitly определённый когда used.

---

# 29. Relation chaining

Один chain из Relations МОЖЕТ поддерживать Inference.

But:

    Relation chain
    ≠ implied direct Relation automatically

unless explicit logic licenses the Inference.

---

# 30. Relation closure

Closure operations МОЖЕТ generate inferred Relations.

Generated Relations ДОЛЖЕН сохранять:

- derivation;
- rule used;
- source relations;
- uncertainty;
- distinction from directly asserted/observed Relations.

---

# 31. Reflexivity

Some Relation types МОЖЕТ допускать:

    R(A,A)

Others МОЖЕТ forbid Это.

Core НЕ ДОЛЖЕН предполагать reflexivity или irreflexivity universally.

---

# 32. Relation ≠ Claim

Claim отвечает:

> Что утверждается?

Relation отвечает:

> Какая связь представлена?

Следовательно:

    Claim about Relation
    ≠ Relation

Example:

    Source S claims:
    A caused B

Этот Claim МОЖЕТ представлять/поддерживать Один causal Relation.

But:

    Claim exists
    ≠ causal Relation proven

---

# 33. Relation ≠ Evidence Use

Relation МОЖЕТ connect Evidence to Claim.

Example:

    Evidence E supports Claim C

Но relation edge alone НЕ ДОЛЖЕН означать:

    Claim C true

Evidential strength, independence, relevance и reliability МОЖЕТ требовать additional semantics.

---

# 34. Relation ≠ Inference

Inference МОЖЕТ derive Один Relation.

But:

    inferred Relation
    ≠ Inference itself

Need preserve when material:

- Relation;
- basis;
- rule/model;
- Inference provenance;
- uncertainty.

---

# 35. Relation ≠ Assessment

Assessment МОЖЕТ evaluate Relation.

Example:

    causal relation is weakly supported

But:

    Assessment
    ≠ Relation itself

---

# 36. Relation ≠ Event

Some Relations change over time.

Example:

    Relation/State:
    A owns B

    Event:
    ownership transferred

Этот ownership Relation и переносить Event ДОЛЖЕН оставаться различимым.

---

# 37. Relation ≠ State universally

Some persistent Relations МОЖЕТ участвовать в State-like semantics.

Example:

    A owns B during T1–T2

МОЖЕТ быть представлен как relational State.

But:

    Relation
    ≠ State universally

Relation describes semantic linkage.

State describes condition/configuration in applicable frame.

Один relational State МОЖЕТ reuse Relation instance semantics без requiring duplicate fundamental objects.

---

# 38. Relation ≠ Process

Process МОЖЕТ contain changing Relations.

Example:

    negotiation Process

includes changing relations among participants.

But:

    Relation
    ≠ Process

Relation changing over time does not itself automatically become Process.

---

# 39. Relation ≠ Action

Action МОЖЕТ устанавливать, terminate или modify Relation.

Example:

    Action:
    sign contract

МОЖЕТ быть associated с establishment из institutional Relation.

But:

    Action
    ≠ Relation

---

# 40. Relation ≠ Result

Relation МОЖЕТ occupy Result semantics relative to Один reference frame.

Example:

    Result:
    connection established between A and B

But:

    Relation
    ≠ Result intrinsically

---

# 41. Relation temporal validity

Some Relations hold only during defined periods.

Example:

    A owned B
    from T1 to T2

Temporal validity МОЖЕТ быть:

- exact;
- approximate;
- inferred;
- open-ended;
- disputed;
- unknown.

---

# 42. Domain Relation validity ≠ representation time

Необходимо различать:

    when Relation held in represented domain/world
    ≠ when Relation was recorded
    ≠ when assertion was published
    ≠ when representation was created
    ≠ when representation was revised
    ≠ when Relation was epistemically accepted

Example:

    ownership held: 1800–1810
    archive record created: 1950
    interpretation revised: 2000

эти temporal dimensions НЕ ДОЛЖЕН быть collapsed.

---

# 43. Relation snapshot ≠ interval

Need distinguish:

    Relation observed at T
    ≠ Relation held continuously during interval automatically

Snapshot evidence НЕ ДОЛЖЕН незаметно expand into interval validity.

---

# 44. Open-ended Relation validity

Relation МОЖЕТ иметь:

    start known
    end unknown

But:

    unknown end
    ≠ Relation still holds currently automatically

And:

    open-ended
    ≠ permanent

---

# 45. Relation persistence

Absence of evidence that Relation ended:

    ≠ evidence that Relation persisted

unless domain semantics or justified Inference supports continuity.

---

# 46. Relation establishment ≠ full Relation history

Event/Action associated с Relation establishment МОЖЕТ быть известным.

But:

    establishment occurrence known
    ≠ exact Relation validity interval fully known

Likewise:

    Relation exists
    ≠ establishment Event known

---

# 47. Relation termination

Termination Event МОЖЕТ end Relation.

But:

    Relation terminated
    ≠ Relation never re-established

And:

    termination
    ≠ permanent absence automatically

---

# 48. Current Relation ≠ historical Relation

Current Relation НЕ ДОЛЖЕН незаметно overwrite historical Relation.

Example:

    Country A borders Country B today

does not imply identical border Relation historically.

---

# 49. Relation history

Historical Relation representation МОЖЕТ сохранять:

- participants;
- participant roles;
- Relation type;
- qualifiers;
- temporal validity;
- Context;
- Scope;
- provenance;
- uncertainty;
- competing interpretations;
- applicable taxonomy/jurisdiction/model.

---

# 50. Relation revision

Need distinguish:

- Correction;
- new Evidence;
- revised interpretation;
- new historical reconstruction;
- Relation changed in represented domain;
- Relation type definition changed;
- ontology mapping changed;
- participant identity resolution changed.

Changed representation:

    ≠ represented Relation changed automatically

---

# 51. Relation representation identity ≠ Relation instance identity

Two records МОЖЕТ describe Этот same Relation instance.

Likewise same participants и same Relation type МОЖЕТ describe различимый Relation instances.

Therefore:

    representation identity
    ≠ Relation instance identity

---

# 52. Relation instance identity

Relation instance identity МОЖЕТ зависеть от материально relevant:

- Relation type;
- semantic positions;
- participant identities;
- participant roles;
- qualifiers;
- reference object/contract;
- amount/value;
- temporal validity;
- continuity;
- Scope;
- Context;
- applicable frame.

Therefore:

    same participants
    +
    same Relation type
    ≠ same Relation instance automatically

Example:

    A owes B $100 under Contract C

and:

    A owes B $200 under Contract D

НЕ ДОЛЖЕН автоматически схлопываться into one Relation instance.

---

# 53. Qualifier/value change ≠ automatic identity decision

Change в Один материально relevant qualifier или value НЕ ДОЛЖЕН автоматически определять either:

- continuity of the same Relation instance;
- replacement by a new Relation instance.

Example:

    A owns 30% of Company B

later:

    A owns 60% of Company B

Это МОЖЕТ представлять:

- changing state of one broader ownership Relation;
- two temporal Relation instances;
- two snapshots of one relational State;
- another Profile/domain-defined structure.

Therefore:

    qualifier/value changed
    ≠ same Relation instance automatically

and:

    qualifier/value changed
    ≠ new Relation instance automatically

Relation continuity/identity depends on defined domain/Profile semantics.

---

# 54. Repeated Relation

Example:

    A connected-to B in 2020
    relation ended
    A connected-to B in 2025

Same participants/type:

    ≠ one continuous Relation automatically

Continuity requires semantic justification.

---

# 55. Different provenance ≠ different Relation instance automatically

Two Sources МОЖЕТ independently представлять/поддерживать Этот same Relation instance.

Different provenance НЕ ДОЛЖЕН принуждать duplicate представленный Relations.

---

# 56. Relation granularity

Relation МОЖЕТ быть представлен broadly:

    A associated-with B

or more specifically:

    A inhibits B

    A causes B

    A physically-connected-to B

Specific Relation СЛЕДУЕТ быть preferred когда материально установленный.

Но stronger specificity НЕ ДОЛЖЕН быть придуманный.

---

# 57. Generic Relation

Generic Relations such as:

    related-to
    associated-with

МОЖЕТ быть used когда more specific semantics неизвестный или unavailable.

Но generic Relation НЕ ДОЛЖЕН незаметно inherit:

- causality;
- direction;
- dependency;
- support;
- equivalence;
- responsibility.

---

# 58. Specificity preservation

If exact Relation is known:

    A part-of B

representation НЕ СЛЕДУЕТ degrade Это to:

    A related-to B

when loss materially affects knowledge.

Thus:

    known specific Relation
    > unnecessarily generic Relation

---

# 59. Relation strengthening

Representation НЕ ДОЛЖЕН strengthen:

    associated-with
    → depends-on

    depends-on
    → caused-by

    correlated-with
    → caused-by

    similar-to
    → same-as

    precedes
    → causes

without independent justification.

---

# 60. Relation weakening

If evidence supports only:

    associated-with

system НЕ ДОЛЖЕН придумывать:

    caused-by

Uncertainty СЛЕДУЕТ оставаться явным.

---

# 61. Part-whole Relation

Part-whole semantics МОЖЕТ включать:

- component-of;
- member-of;
- portion-of;
- structural-part-of;
- temporal-part-of;
- phase-of;
- material-part-of.

`part-из` НЕ ДОЛЖЕН быть предполагаемым to иметь one universal mereology.

---

# 62. Part-of ≠ member-of

Example:

    wheel part-of bicycle

vs:

    person member-of organization

эти Relations ДОЛЖЕН оставаться различимым когда material.

---

# 63. Containment ≠ part-of

Example:

    water in bottle

does not necessarily mean:

    water part-of bottle

Spatial containment и structural part-из ДОЛЖЕН оставаться различимым.

---

# 64. Temporal containment ≠ part-of

Event E occurs during Process P:

    ≠ Event E part-of Process P automatically

Temporal inclusion and structural/process decomposition are different relations.

---

# 65. Membership

Membership МОЖЕТ быть:

- institutional;
- set-theoretic;
- social;
- biological;
- classificatory.

External `member-из` labels ДОЛЖЕН сохранять domain semantics.

---

# 66. Spatial Relation

Spatial Relation МОЖЕТ включать:

- inside;
- outside;
- adjacent-to;
- north-of;
- intersects;
- overlaps;
- contains;
- near.

Spatial Relations МОЖЕТ зависеть от coordinate/reference frame.

---

# 67. Spatial reference frame

Relation:

    A north-of B

requires applicable orientation/reference frame.

Frame ДОЛЖЕН оставаться разрешимым когда материально relevant.

---

# 68. Near ≠ universal distance

`near` is context-dependent.

Это НЕ ДОЛЖЕН receive universal distance threshold если не Profile/domain semantics defines one.

---

# 69. Temporal Relation

Temporal Relations МОЖЕТ включать:

- before;
- after;
- during;
- overlaps;
- starts;
- finishes;
- simultaneous-with;
- approximately-before.

Temporal precision и uncertainty ДОЛЖЕН оставаться разрешимым когда material.

---

# 70. Before ≠ causes

Fundamental rule:

    A before B
    ≠ A caused B

Temporal order НЕ ДОЛЖЕН незаметно становиться causality.

---

# 71. Simultaneous ≠ associated

Two occurrences at the same time:

    ≠ meaningful association automatically

Temporal coincidence alone does not establish semantic linkage.

---

# 72. Causal Relation

Causal Relation is specialized Relation semantics.

Это НЕ ДОЛЖЕН быть inferred solely из:

- temporal order;
- correlation;
- proximity;
- sequence;
- co-occurrence;
- narrative order;
- shared Context.

Causal semantics requires separate support.

---

# 73. Causal direction

If causal direction is represented:

    A causes B

ДОЛЖЕН оставаться различимым из:

    B causes A

and:

    A associated-with B

---

# 74. Causal contribution

Causal Relations МОЖЕТ представлять:

- necessary contribution;
- sufficient contribution;
- partial contribution;
- enabling cause;
- inhibiting cause;
- mediated influence;
- probabilistic contribution.

`013` does not define complete causal ontology.

---

# 75. Cause ≠ responsibility

Causal Relation НЕ ДОЛЖЕН автоматически означать:

- legal responsibility;
- moral responsibility;
- blame;
- intention;
- negligence.

These are separate semantics.

---

# 76. Dependency Relation

Dependency МОЖЕТ означать:

- logical dependency;
- operational dependency;
- causal dependency;
- resource dependency;
- software dependency;
- institutional dependency.

External label `depends-on` ДОЛЖЕН сохранять domain meaning.

---

# 77. Dependency ≠ causality universally

    A depends-on B
    ≠ B caused A automatically

Dependency may be structural, conditional or operational.

---

# 78. Enabling Relation

Один МОЖЕТ enable B.

But:

    enabled
    ≠ occurred

And:

    enabling condition
    ≠ sufficient cause

---

# 79. Inhibiting Relation

Один МОЖЕТ inhibit B.

But:

    inhibitor present
    ≠ B absent automatically

without defined domain semantics.

---

# 80. Evidential Relation

Evidence-related Relations МОЖЕТ включать:

- supports;
- contradicts;
- is-basis-for;
- derived-from;
- corroborates;
- weakens;
- consistent-with.

эти Relations НЕ ДОЛЖЕН автоматически assign truth.

---

# 81. Supports ≠ proves

Fundamental rule:

    Evidence E supports Claim C
    ≠ Claim C proven

Support МОЖЕТ различаться в:

- strength;
- relevance;
- independence;
- reliability;
- Scope;
- Context.

---

# 82. Multiple support edges ≠ independent evidence

Multiple supporting Relations НЕ ДОЛЖЕН автоматически быть interpreted as multiple independent evidence lines.

Example:

    Source B cites Source A
    Source C cites Source A
    Source D copies Source A

does not automatically provide three independent confirmations.

Evidence independence МОЖЕТ itself требовать provenance/relation analysis.

---

# 83. Contradicts ≠ false

If Evidence E contradicts Claim C:

    ≠ Claim C necessarily false

Contradiction МОЖЕТ зависеть от:

- interpretation;
- assumptions;
- Scope;
- timing;
- measurement validity.

---

# 84. Consistent-with ≠ confirms

Один datum МОЖЕТ быть consistent с many hypotheses.

Thus:

    consistent-with
    ≠ confirms
    ≠ strongly supports automatically

---

# 85. Derived-from Relation

Derived-из МОЖЕТ connect:

- Claim to Source;
- Result to Measurement;
- computed value to inputs;
- reconstruction to Evidence.

But:

    derived-from
    ≠ causally-produced-by automatically

---

# 86. Source Relation

Relations to Source МОЖЕТ express:

- asserts;
- documents;
- records;
- mentions;
- contains;
- derived-from;
- cites.

эти ДОЛЖЕН оставаться semantically различимый когда material.

---

# 87. Citation ≠ evidential support

A Source citing another Source:

    ≠ independent corroboration

Likewise:

    citation
    ≠ agreement
    ≠ truth

---

# 88. Reference Relation

Один Record МОЖЕТ refer-to another Record.

Reference relation НЕ ДОЛЖЕН автоматически означать:

- endorsement;
- support;
- dependency;
- identity.

---

# 89. Identity-like semantics

Identity-like relations require special care.

Need distinguish:

    entity identity
    ≠ coreference
    ≠ Record identity
    ≠ representation identity
    ≠ semantic equivalence
    ≠ value equivalence

---

# 90. Coreference ≠ Record identity

Two Records МОЖЕТ refer to Этот same real-world Entity.

Example:

    Record A:
    Alexander III

    Record B:
    Александр III

They МОЖЕТ быть coreferential.

But:

    same referent
    ≠ same Record

Therefore:

    coreference
    ≠ Record identity

---

# 91. `same-as` is not universal identity bucket

`same-as` НЕ ДОЛЖЕН быть used as universal container for all identity-like semantics.

System СЛЕДУЕТ distinguish когда material:

- same Entity;
- same referent;
- duplicate Record;
- equivalent representation;
- same value;
- same concept;
- coreference.

---

# 92. Identity Relation

Identity semantics is especially strong.

Это НЕ ДОЛЖЕН быть inferred solely из:

- same label;
- similar name;
- same value;
- same location;
- overlapping properties;
- likely match.

Identity resolution requires sufficient support.

---

# 93. Similarity ≠ identity

Fundamental rule:

    similar-to
    ≠ same-as

Similarity МОЖЕТ быть graded, contextual или feature-dependent.

---

# 94. Similarity basis

Similarity СЛЕДУЕТ сохранять когда материально relevant:

- comparison dimensions;
- selected features;
- metric;
- weights;
- threshold;
- comparison population;
- model/version.

Therefore:

    similarity
    ≠ intrinsic universal property automatically

Example:

    visually similar
    ≠ chemically similar
    ≠ functionally similar

---

# 95. Equivalence ≠ identity universally

Two things МОЖЕТ быть equivalent for Один purpose без being identical.

Example:

    1000 mm
    equivalent-to 1 m

Different representations МОЖЕТ encode equivalent quantity.

Likewise two Procedures МОЖЕТ быть functionally equivalent без being Этот same Procedure.

---

# 96. Version Relation

Version Relations МОЖЕТ включать:

- version-of;
- supersedes;
- revises;
- derived-version-of;
- translation-of.

эти НЕ ДОЛЖЕН автоматически означать полный semantic identity.

---

# 97. Supersedes ≠ deletes history

If Record B supersedes Record A:

    ≠ Record A should disappear

Historical dependency и provenance МОЖЕТ требовать preserving Один.

---

# 98. Correction Relation

Correction МОЖЕТ indicate later representation corrects earlier representation.

But:

    Correction
    ≠ underlying historical reality changed

---

# 99. Replacement Relation

`заменяет` МОЖЕТ означать:

- physical replacement;
- document replacement;
- institutional succession;
- semantic update;
- component replacement.

Domain semantics ДОЛЖЕН оставаться определённый.

---

# 100. Successor Relation

Successor МОЖЕТ indicate sequence или institutional continuity.

But:

    successor-of
    ≠ same identity automatically

---

# 101. Parent/child Relation

`parent`, `child`, `ancestor`, `descendant` МОЖЕТ иметь:

- biological;
- genealogical;
- taxonomic;
- data-tree;
- organizational meanings.

External vocabulary НЕ ДОЛЖЕН определять canonical semantics без domain frame.

---

# 102. Classification Relation

Classification МОЖЕТ включать:

    instance-of
    subclass-of
    type-of

эти ДОЛЖЕН оставаться различимым.

---

# 103. Instance-of ≠ subclass-of

Example:

    Dog A instance-of Dog

vs:

    Dog subclass-of Mammal

These are not interchangeable.

---

# 104. Class membership ≠ identity

Being instances of the same class:

    ≠ same Entity

---

# 105. Taxonomic Relation

Taxonomy МОЖЕТ быть:

- scientific;
- folk;
- historical;
- institutional;
- project-specific.

Taxonomic Relation ДОЛЖЕН сохранять taxonomy/version когда material.

---

# 106. Taxonomy drift

Historical classification НЕ ДОЛЖЕН незаметно inherit current taxonomy.

Example:

    classification at T1
    ≠ modern classification automatically

---

# 107. Normative Relation

Relations МОЖЕТ представлять:

- requires;
- permits;
- prohibits;
- authorizes;
- obliges.

Normative Relation НЕ ДОЛЖЕН автоматически становиться actual Action/State relation.

---

# 108. Authorization ≠ Action

    A authorizes B to do X
    ≠ B did X

Likewise:

    permission
    ≠ execution

---

# 109. Obligation ≠ compliance

    A obligated-to perform X
    ≠ X performed

Normative и actual layers ДОЛЖЕН оставаться различимым.

---

# 110. Prohibition ≠ absence

Fundamental rule:

    X prohibited
    ≠ X did not occur

Likewise:

    prohibited Relation/Action
    ≠ absent Relation/Action automatically

Normative prohibition и empirical absence ДОЛЖЕН оставаться различимым.

---

# 111. Institutional Relation

Institutional Relations МОЖЕТ включать:

- owns;
- governs;
- employs;
- appoints;
- represents;
- licenses;
- recognizes;
- controls.

Their semantics МОЖЕТ зависеть от jurisdiction и time.

---

# 112. Legal Relation ≠ de facto Relation

Example:

    legal owner = A
    de facto controller = B

эти МОЖЕТ coexist.

They НЕ ДОЛЖЕН быть collapsed.

---

# 113. Ownership Relation

Ownership МОЖЕТ зависеть от:

- jurisdiction;
- time;
- legal system;
- type of property.

`owns` НЕ ДОЛЖЕН receive one universal cross-domain ontology без Profile semantics.

---

# 114. Control Relation

`controls` МОЖЕТ означать:

- operational control;
- legal control;
- technical control;
- causal control;
- ownership influence.

External label ДОЛЖЕН сохранять intended domain meaning.

---

# 115. Participation Relation

Participation МОЖЕТ connect Actor/Entity to:

- Event;
- Action;
- Process;
- organization;
- group.

Но participation НЕ ДОЛЖЕН автоматически означать:

- causation;
- responsibility;
- leadership;
- intention.

---

# 116. Actor Relation

Action МОЖЕТ иметь:

    performed-by

But:

    participant-in
    ≠ performed-by automatically

And:

    present-at
    ≠ participated-in

---

# 117. Presence Relation

Being present at Event:

    ≠ participant
    ≠ witness
    ≠ cause
    ≠ responsible

unless separately established.

---

# 118. Witness Relation

Witnessing Event:

    ≠ causing Event
    ≠ participating in Event

---

# 119. Location Relation

An Entity МОЖЕТ иметь:

    located-at
    located-in
    passes-through
    originated-in

эти Relations ДОЛЖЕН сохранять role и temporal frame когда material.

---

# 120. Origin Relation

`originated-в` МОЖЕТ означать:

- physical origin;
- historical origin;
- conceptual origin;
- manufacturing origin;
- biological origin.

Это НЕ ДОЛЖЕН автоматически означать present location.

---

# 121. Derivation Relation

Один МОЖЕТ быть derived из B.

Это МОЖЕТ означать:

- data derivation;
- textual derivation;
- material derivation;
- genealogical descent;
- logical inference.

Generic `derived-из` ДОЛЖЕН сохранять domain semantics.

---

# 122. Transformation Relation

Один transformed-into B МОЖЕТ involve:

- Process;
- Event;
- identity continuity;
- material continuity;
- semantic replacement.

Transformation Relation НЕ ДОЛЖЕН автоматически устанавливать same identity across transformation.

---

# 123. Identity through transformation

Whether Один before transformation is same Entity as B after transformation МОЖЕТ быть domain-specific.

Core НЕ ДОЛЖЕН decide identity solely из transformation Relation.

---

# 124. Relation uncertainty

Uncertainty МОЖЕТ apply to:

- existence of Relation;
- Relation type;
- participant identity;
- participant roles;
- direction;
- temporal validity;
- Scope;
- Context;
- strength;
- mechanism;
- qualifiers;
- quantification;
- provenance.

Core does not require universal:

    Relation.confidence

---

# 125. Unknown Relation

Unknown Relation between A and B:

    ≠ no Relation

Likewise:

    no recorded Relation
    ≠ Relation absent

---

# 126. Relation absence

Defined absence из Relation МОЖЕТ быть представлен Если Evidence/domain semantics supports Это.

But:

    not observed
    ≠ absent

    not recorded
    ≠ absent

---

# 127. Negated Relation

Need distinguish:

    not-R
    ≠ unknown-R
    ≠ no-record-of-R
    ≠ incompatible-with-R
    ≠ prohibited-R

Statement:

    A does not own B

МОЖЕТ быть:

- Claim;
- absence semantics;
- logical assertion;
- Profile-defined negation.

Это НЕ ДОЛЖЕН автоматически create Один special negative Relation Entity.

---

# 128. Incompatibility ≠ negation

Один Relation МОЖЕТ быть incompatible с another Relation under определённый constraints.

But:

    incompatible-with
    ≠ negation automatically

Likewise:

    disjoint-with
    ≠ absence of every other Relation

Formal incompatibility requires defined semantics.

---

# 129. Relation conflict

Different Sources МОЖЕТ поддерживать conflicting Relations.

Examples:

    A caused B

vs:

    A did not cause B

or:

    A part-of B

vs:

    A independent-of B

System ДОЛЖЕН допускать competing representations с provenance.

---

# 130. Apparent conflict

Relations МОЖЕТ appear conflicting Но concern different:

- time periods;
- jurisdictions;
- Scopes;
- Relation types;
- participants;
- identity resolutions;
- Contexts;
- taxonomies;
- versions;
- qualifiers;
- quantifiers.

Alignment ДОЛЖЕН precede contradiction judgment.

---

# 131. Relation comparison

Comparing Relations requires materially sufficient alignment.

Relevant alignment МОЖЕТ включать:

- participant identity;
- semantic positions;
- participant roles;
- Relation type;
- direction;
- temporal frame;
- Context;
- Scope;
- qualifiers;
- quantification;
- Profile;
- taxonomy/version.

---

# 132. Relation normalization

External systems МОЖЕТ использовать different vocabularies.

Normalization МОЖЕТ map external Relation labels to canonical semantics.

Но normalization НЕ ДОЛЖЕН erase материально relevant distinctions.

---

# 133. External Relation label ≠ canonical Relation

Words such as:

- linked;
- connected;
- related;
- associated;
- tied;
- dependent;
- derived;
- based;
- influenced;

are often ambiguous.

External wording alone НЕ ДОЛЖЕН определять canonical Relation type.

---

# 134. Natural-language ambiguity

Natural language often leaves:

- direction;
- roles;
- causality;
- strength;
- temporality;
- Scope;
- quantification;
- modality;

implicit.

Representation НЕ ДОЛЖЕН придумывать missing semantics без basis.

---

# 135. Relation provenance

Relation provenance МОЖЕТ включать:

- assertion;
- direct Observation;
- Measurement;
- Claim;
- Source;
- Inference;
- computation;
- Model;
- reconstruction;
- imported relation;
- Assessment.

Multiple provenance dimensions МОЖЕТ coexist.

---

# 136. Observed Relation

Some Relations МОЖЕТ быть directly observed.

Example:

    Object A physically touching B

But:

    observed Relation
    ≠ permanent Relation
    ≠ causal Relation
    ≠ complete Relation history

---

# 137. Measured Relation

Relations МОЖЕТ derive из Measurements.

Example:

    distance(A,B) = 5 m

Measurement-derived Relation ДОЛЖЕН сохранять когда material:

- method;
- units;
- uncertainty;
- time;
- reference frame.

---

# 138. Inferred Relation

Relation МОЖЕТ быть inferred.

Then:

    inferred
    ≠ observed

Inference basis и assumptions ДОЛЖЕН оставаться разрешимым когда material.

---

# 139. Reconstructed Relation

Historical Relation МОЖЕТ быть reconstructed.

Examples:

- ownership;
- political alliance;
- trade relation;
- family relation.

Reconstruction ДОЛЖЕН сохранять provenance и uncertainty.

---

# 140. Modeled Relation

Model МОЖЕТ включать Relations.

But:

    modeled Relation
    ≠ observed/historical Relation automatically

Model identity и представленный Relation instance identity ДОЛЖЕН оставаться различимым.

---

# 141. Computed Relation

Some Relations МОЖЕТ быть computed.

Examples:

- similarity;
- network relation;
- spatial overlap;
- temporal overlap;
- statistical association.

Computation method СЛЕДУЕТ оставаться разрешимым когда material.

---

# 142. Provenance dimensions МОЖЕТ overlap

Observed, measured, computed, inferred, modeled и reconstructed Relation provenance МОЖЕТ overlap.

Core НЕ ДОЛЖЕН принуждать one exclusive status Если multiple are материально true.

---

# 143. Relation strength

Some Relation types МОЖЕТ иметь strength.

Examples:

    strong correlation
    weak evidential support
    high dependency

Strength semantics is Relation-type-specific.

Core does not impose one universal Relation strength scale.

---

# 144. Relation probability

Some Relations МОЖЕТ быть probabilistic.

Example:

    A increases probability of B

Probability semantics НЕ ДОЛЖЕН быть collapsed into deterministic Relation.

---

# 145. Statistical Relation

Statistical Relations МОЖЕТ включать:

- correlation;
- association;
- conditional association;
- probabilistic dependence;
- other defined structures.

They ДОЛЖЕН сохранять когда материально relevant:

- variables;
- population;
- sample;
- period;
- method;
- conditioning variables;
- coefficient/effect representation;
- uncertainty;
- Context.

Statistical Relation НЕ ДОЛЖЕН незаметно generalize across population, period или conditioning frame.

---

# 146. Correlation Relation

Correlation is statistical Relation.

And:

    correlation
    ≠ causation

Also:

    marginal correlation
    ≠ conditional correlation automatically

---

# 147. Association Relation

Association МОЖЕТ быть:

- statistical;
- observational;
- semantic;
- operational;
- historical.

Generic association НЕ ДОЛЖЕН receive causal semantics автоматически.

---

# 148. Similarity Relation

Similarity ДОЛЖЕН сохранять материально relevant comparison basis когда necessary.

Thus:

    visually similar
    ≠ chemically similar
    ≠ functionally similar

---

# 149. Contradiction Relation

Contradiction МОЖЕТ exist between Claims.

Need distinguish:

    Claim C1 contradicts Claim C2

from:

    represented world States are incompatible

Logical contradiction и empirical incompatibility МОЖЕТ требовать different semantics.

---

# 150. Support Relation

Support Relation МОЖЕТ exist:

    Evidence → Claim

    Claim → Inference

    Source → Claim

Но exact поддерживать semantics ДОЛЖЕН оставаться typed когда material.

---

# 151. Basis Relation

`basis-for` МОЖЕТ connect:

- Evidence to Decision;
- Claim to Inference;
- State knowledge to Action;
- Result to Assessment.

But:

    basis-for
    ≠ cause-of automatically

---

# 152. Decision Basis preservation

Later Relation НЕ ДОЛЖЕН быть inserted retroactively into earlier Decision Basis.

If Relation was discovered at T2:

    ≠ available to Decision at T1 automatically

---

# 153. Relation historical drift

Current Relation НЕ ДОЛЖЕН незаметно alter earlier historical interpretation.

Examples:

- current ownership;
- current borders;
- current taxonomy;
- current organization membership.

Historical frame ДОЛЖЕН оставаться сохранённым.

---

# 154. Relation versioning

Need distinguish:

- Relation instance changed;
- Relation representation changed;
- Relation type semantics changed;
- Relation model changed;
- ontology mapping changed;
- Source corrected;
- participant identity resolution changed.

Thus:

    Relation type/model revision
    ≠ represented historical Relation changed automatically

---

# 155. Ontology Relation ≠ domain Relation

Some Relations exist in ontology/meta-model:

    subclass-of
    defined-by
    compatible-with

Others describe domain/world:

    located-in
    owns
    causes

эти layers СЛЕДУЕТ оставаться различимым когда material.

---

# 156. Meta-Relation

Один Relation МОЖЕТ itself быть referenced as participant в another Relation Если representation permits reference to Это.

Example:

    Relation R1:
    A causes B

    R1 disputed-by Source S

or:

    R1 valid-during Interval T

But:

    higher-order Relation support
    ≠ universal Relation reification requirement

Core НЕ ДОЛЖЕН требовать every Relation to становиться an Entity merely because some Relations требовать higher-order reference.

---

# 157. Relation representation as participant ≠ represented Relation itself

когда Один Relation representation is used as participant в another Relation, Этот system ДОЛЖЕН сохранять whether Этот higher-order Relation concerns:

- the representation/Record;
- the assertion;
- the semantic Relation instance;
- another referenceable layer.

Example:

    Source S disputes Record R1

does not necessarily mean:

    Source S disputes the existence
    of the underlying world Relation itself

Therefore:

    Relation representation as participant
    ≠ represented Relation itself automatically

Higher-order semantics ДОЛЖЕН сохранять Этот intended reference layer когда материально relevant.

---

# 158. Relation about Relation

System МОЖЕТ представлять:

- provenance of Relation;
- uncertainty;
- contradiction;
- replacement;
- temporal validity;
- Relation between Relations.

Higher-order semantics СЛЕДУЕТ avoid unnecessary Entity Explosion.

---

# 159. Relation cardinality

Один participant МОЖЕТ иметь:

- zero;
- one;
- multiple;

Relations of a type.

Cardinality constraints МОЖЕТ быть Profile/domain-specific.

Core НЕ ДОЛЖЕН impose universal cardinality если не required by Relation definition.

---

# 160. Functional Relation

Some Relation types МОЖЕТ быть functional within Один определённый frame:

    each X has at most one Y

Но functionality ДОЛЖЕН быть explicitly определённый.

---

# 161. Exclusive Relation

Some Relation types МОЖЕТ быть mutually exclusive.

Example:

    married-to A
    married-to B

МОЖЕТ или МОЖЕТ NOT быть allowed depending on jurisdiction/time.

Core НЕ ДОЛЖЕН impose universal exclusivity.

---

# 162. Relation Scope

Relation МОЖЕТ apply только to:

- part of subject;
- subset of population;
- particular time;
- particular jurisdiction;
- specific variables;
- specific domain segment.

Scope ДОЛЖЕН оставаться разрешимым когда материально relevant.

Scope задаёт Этот extent/domain subset to which представленный Relation applies и НЕ ДОЛЖЕН автоматически быть collapsed into applicable frame.

---

# 163. Local Relation ≠ global Relation

Relation observed in local subset:

    ≠ Relation holds globally automatically

Generalization requires Inference/Model.

---

# 164. Sample Relation ≠ population Relation

Statistical Relation observed in sample:

    ≠ population Relation automatically

---

# 165. Aggregate Relation

Aggregate Relation МОЖЕТ differ из individual-level Relation.

Example:

    population-level correlation

does not imply identical individual relationship.

---

# 166. Ecological fallacy safeguard

Group-level Relation НЕ ДОЛЖЕН автоматически становиться individual-level Relation.

Likewise individual-level Relation НЕ ДОЛЖЕН автоматически generalize to aggregate level.

---

# 167. Context-dependent Relation

Relation МОЖЕТ hold только under specific Context.

Example:

    material A reacts-with B
    only above temperature T

Context ДОЛЖЕН оставаться разрешимым когда material.

---

# 168. Relation Context drift

Current Context НЕ ДОЛЖЕН незаметно заменять historical/context-specific Relation semantics.

---

# 169. Relation and Action

Action МОЖЕТ быть linked to:

- Actor;
- Object;
- Instrument;
- target;
- Result;
- Event;
- Process.

Relations ДОЛЖЕН сохранять role distinctions.

Example:

    Actor participated-in Action
    ≠ Actor performed Action automatically

---

# 170. Relation and Event

Event МОЖЕТ быть linked through:

- occurred-at;
- affected;
- preceded-by;
- participated-in;
- caused-by;
- associated-with.

эти Relations НЕ ДОЛЖЕН схлопываться into one generic Event relation Если distinction материально matters.

---

# 171. Relation and State

State МОЖЕТ использовать Relation semantics as content.

Example:

    A owns B

as relational State.

Но Relation temporal validity и State semantics ДОЛЖЕН оставаться различимым.

Relational State МОЖЕТ reuse Relation instance без requiring duplicate canonical semantics.

---

# 172. Relation and Process

Process МОЖЕТ иметь:

- participants;
- inputs;
- outputs;
- dependencies;
- phase Relations;
- interactions.

Temporal containment НЕ ДОЛЖЕН автоматически становиться subprocess Relation.

---

# 173. Relation and Result

Result МОЖЕТ relate to:

- reference frame;
- Comparison Reference;
- Measurement;
- population;
- Context;
- Objective.

Generic links НЕ ДОЛЖЕН erase role semantics.

---

# 174. Relation and Objective

Objective МОЖЕТ relate to:

- target State;
- Action;
- Decision;
- Result;
- criteria.

Desired Relation:

    ≠ actual Relation automatically

---

# 175. Relation and Procedure

Procedure МОЖЕТ определять prescribed Relations:

    step A before step B

But:

    prescribed order
    ≠ actual historical order

---

# 176. Relation and Model

Model МОЖЕТ определять Relations among variables/entities.

But:

    modeled Relation
    ≠ directly observed Relation

---

# 177. Relation and Measurement

Measurement МОЖЕТ quantify Relation.

Examples:

- distance;
- correlation;
- angle;
- overlap.

Measurement result НЕ ДОЛЖЕН автоматически определять stronger Relation semantics than measured.

---

# 178. Relation and Observation

Observation МОЖЕТ identify Relation.

But:

    observed association
    ≠ causal Relation

---

# 179. Relation and Inference

Inference МОЖЕТ derive Relation through:

- logical rule;
- statistical analysis;
- causal model;
- identity resolution;
- temporal reasoning.

Derived status ДОЛЖЕН оставаться разрешимым.

---

# 180. Relation and Assessment

Assessment МОЖЕТ evaluate:

- relevance;
- reliability;
- strength;
- validity;
- importance;
- plausibility.

These are not intrinsic generic Relation properties unless Relation type defines them.

---

# 181. Relation representation fidelity

Representation НЕ ДОЛЖЕН материально alter:

- Relation type/model/instance role;
- semantic positions;
- participant identity;
- participant roles;
- arity;
- direction;
- formal properties when known;
- quantification;
- qualifiers;
- temporal validity;
- Scope;
- Context;
- applicable frame;
- uncertainty;
- provenance;
- strength;
- causal/epistemic status.

---

# 182. Translation Fidelity

Translation ДОЛЖЕН сохранять distinctions such as:

    associated-with
    ≠ caused-by

    part-of
    ≠ contained-in

    supports
    ≠ proves

    authorized
    ≠ performed

    similar-to
    ≠ same-as

    coreferential-with
    ≠ same Record

    before
    ≠ causes

    member-of
    ≠ part-of automatically

    prohibited
    ≠ absent

    generic
    ≠ universal

    instance pattern
    ≠ generic rule

---

# 183. Logical Fidelity

Representation СЛЕДУЕТ сохранять:

- direction;
- negation;
- quantifiers;
- modality;
- semantic positions;
- participant roles;
- Relation Scope;
- temporal bounds;
- conditions;
- uncertainty;
- strength;
- formal logic where material.

---

# 184. Summary Fidelity

Summary НЕ ДОЛЖЕН convert:

    association
    → causality

    similarity
    → identity

    coreference
    → Record identity

    support
    → proof

    participation
    → responsibility

    temporal order
    → causality

    local Relation
    → universal Relation

    sample Relation
    → population Relation

    historical Relation
    → current Relation

    generic Relation
    → specific stronger Relation

    class-level Relation
    → universal instance-level Relation

    multiple Relation instances
    → generic/class-level Relation

    prohibition
    → empirical absence

    modeled Relation
    → observed Relation

    Relation representation
    → represented Relation itself

---

# 185. Relation compression

Relation representation МОЖЕТ omit non-material metadata.

Но compression НЕ ДОЛЖЕН erase материально relevant:

- Relation type/model/instance role;
- direction;
- roles;
- n-ary structure;
- qualifiers;
- quantification;
- temporal validity;
- uncertainty;
- causal status;
- Scope;
- Context;
- applicable frame;
- provenance;
- Relation specificity;
- reference layer in higher-order Relations.

---

# 186. Damaged archives

Historical Source МОЖЕТ сохранять partial Relation.

Example:

    "... allied with the northern kingdom ..."

Missing:

- exact counterpart identity;
- date;
- duration;
- type of alliance;
- legal status;

НЕ ДОЛЖЕН быть придуманный.

Likewise missing quantification, direction или role НЕ ДОЛЖЕН быть незаметно filled где ambiguity is material.

---

# 187. Relation reconstruction

Historical Relation reconstruction ДОЛЖЕН сохранять:

- Sources;
- assumptions;
- uncertainty;
- competing interpretations;
- temporal bounds;
- participant identity uncertainty;
- Context;
- applicable historical frame.

Reconstruction НЕ ДОЛЖЕН masquerade as direct Observation.

---

# 188. Offline preservation

Relation СЛЕДУЕТ быть representable без dependence on modern platform.

Where materially relevant, preserve:

- Relation type/model/instance role;
- semantic positions;
- participants;
- participant roles;
- arity;
- direction;
- temporal validity;
- qualifiers;
- quantification;
- Scope;
- Context;
- applicable frame;
- provenance;
- uncertainty;
- formal properties where needed;
- higher-order reference layer where needed.

---

# 189. Carrier neutrality

Relation semantics does not depend on:

- database;
- graph database;
- RDF;
- JSON;
- Markdown;
- table;
- diagram;
- printed text;
- other durable carrier.

Carrier does not define Relation ontology.

Likewise:

    graph edge
    ≠ canonical Relation automatically

---

# 190. High-risk Profiles

High-risk Profiles МОЖЕТ требовать stricter Relation representation.

Examples:

- medicine;
- engineering;
- law;
- chemistry;
- electrical systems;
- safety;
- historical reconstruction;
- survival procedures.

Profile МОЖЕТ требовать:

- exact Relation type;
- participant roles;
- units;
- causal status;
- temporal validity;
- Scope;
- Context;
- quantification;
- qualifiers;
- provenance;
- uncertainty;
- Relation logic;
- formal constraints.

These are not universal Core requirements.

---

# 191. Relation quality

`013` does not introduce universal intrinsic Relation Quality.

Quality concepts МОЖЕТ включать:

- strong;
- weak;
- reliable;
- uncertain;
- valid;
- invalid;
- useful;
- significant.

These usually require Relation-type-specific semantics or Assessment.

---

# 192. Conformance and Integrity

Need distinguish:

    Core structural/semantic conformance
    ≠ Relation truth
    ≠ provenance integrity
    ≠ causal validity
    ≠ logical validity
    ≠ Relation quality
    ≠ Representation Fidelity

Validator PASS does not mean Relation objectively holds.

---

# 193. Profiles

Profile МОЖЕТ strengthen Core.

Profile НЕ ДОЛЖЕН weaken Core пока claiming compatibility с `013`.

---

# 194. Diagnostic families

## 194.1. Type / model / instance failures

Examples:

- Relation type → Relation instance;
- Relation model → Relation instance;
- enumeration of Relation types → Relation model;
- model edge → historical Relation;
- generic Relation knowledge → specific occurrence;
- Relation instance → Relation type.

## 194.2. Participant / role failures

Examples:

- participant roles omitted;
- subject/object reversed;
- n-ary Relation flattened incorrectly;
- one participant mistaken for another;
- arity confused with number of unique participants.

## 194.3. Directionality failures

Examples:

- A causes B → B causes A;
- contains → part-of reversed incorrectly;
- before/after inverted;
- role ordering treated as sufficient semantic definition.

## 194.4. Formal-property failures

Examples:

- symmetry assumed from label;
- transitivity assumed universally;
- property from Frame X transferred to Frame Y;
- composition treated as transitivity.

## 194.5. Specificity failures

Examples:

- associated-with → caused-by;
- supports → proves;
- related-to used despite known specific Relation;
- part-of → member-of.

## 194.6. Quantification/generalization failures

Examples:

- generic Relation → universal Relation;
- some → all;
- may → always;
- typical → necessary;
- class-level Relation → every instance pair;
- multiple instances → generic Relation;
- observed instance pattern → universal rule.

## 194.7. Frame / Scope failures

Examples:

- applicable frame collapsed into Scope;
- Scope collapsed into applicable frame;
- semantic/reference system confused with population subset;
- jurisdictional interpretation confused with empirical extent.

## 194.8. Temporal failures

Examples:

- snapshot → interval;
- historical Relation → current Relation;
- no end Evidence → persistence;
- observation time → domain Relation validity;
- publication time → Relation validity.

## 194.9. Relation identity failures

Examples:

- same participants/type → same Relation instance;
- qualifier change → automatically same Relation;
- qualifier change → automatically new Relation;
- interrupted Relations → one continuous Relation;
- representation identity → Relation instance identity.

## 194.10. Identity/equivalence failures

Examples:

- similar-to → same-as;
- coreference → Record identity;
- same label → same Entity;
- functional equivalence → identity;
- successor → same identity.

## 194.11. Causal failures

Examples:

- before → cause;
- correlation → causality;
- participation → causal responsibility;
- input → sufficient cause.

## 194.12. Evidential failures

Examples:

- supports → proves;
- multiple citations → independent corroboration;
- citation → evidential support;
- consistent-with → confirms;
- contradicts → automatically false.

## 194.13. Structural failures

Examples:

- containment → part-of;
- temporal containment → subprocess;
- membership → component relation.

## 194.14. Normative failures

Examples:

- authorization → Action;
- obligation → compliance;
- prohibition → absence;
- legal relation → de facto relation.

## 194.15. Negation / absence failures

Examples:

- unknown-R → not-R;
- no-record-R → absent-R;
- prohibited-R → not-R;
- incompatible-R → negated-R.

## 194.16. Scope / Context failures

Examples:

- sample → population;
- local → global;
- group → individual;
- Context X → Context Y;
- jurisdiction A → jurisdiction B.

## 194.17. Provenance/import failures

Examples:

- modeled Relation → observed Relation;
- inferred Relation → direct fact;
- external label mapped blindly;
- historical taxonomy → modern taxonomy.

## 194.18. Higher-order reference failures

Examples:

- dispute of Relation Record → dispute of underlying world Relation automatically;
- provenance of representation → provenance of represented Relation automatically;
- Relation representation → semantic Relation instance without layer distinction.

## 194.19. Implementation failures

Examples:

- storage edge → canonical Relation;
- property field → new Relation type automatically;
- graph structure → ontology semantics automatically.

Diagnostic label itself does not establish:

- fraud;
- negligence;
- blame;
- intent;
- responsibility.

---

# 195. Machine validation

Validator МОЖЕТ check:

- participant references;
- semantic positions;
- required participant roles;
- arity;
- Relation type;
- direction;
- Profile-defined cardinality;
- temporal validity;
- Scope;
- applicable-frame presence/resolvability;
- qualifiers;
- quantification structure;
- formal constraints;
- reference integrity;
- higher-order reference layer where explicitly represented.

But:

    validator PASS
    ≠ Relation true
    ≠ causality established
    ≠ identity established
    ≠ evidential support sufficient
    ≠ historical accuracy proven

Validator has no truth privilege.

---

# 196. Межстандартная совместимость

`013-RELATION` ДОЛЖЕН сохранять neighboring semantic boundaries.

In compact form:

    Claim
    → что утверждается

    State
    → каким представлен condition/configuration
      в applicable frame

    Event
    → что произошло /
      какой occurrence или boundary возник

    Process
    → какая temporally extended
      activity/dynamics unfolds

    Action
    → что было сделано

    Result
    → какую downstream/result role
      phenomenon занимает

    Relation
    → как определённый semantic positions/
      participants связаны
      в applicable frame

Therefore:

    Claim about Relation
    ≠ Relation

    Relation
    ≠ Event

    Relation
    ≠ Process

    Relation
    ≠ Action

    Relation
    ≠ Result intrinsically

    Relation
    ≠ causality automatically

    Relation
    ≠ State universally

    Relation type
    ≠ Relation model
    ≠ Relation instance

    property/predicate
    ≠ Relation automatically

    storage edge
    ≠ canonical Relation automatically

    generic Relation
    ≠ universal instance-level Relation

    multiple Relation instances
    ≠ generic/class-level Relation automatically

    applicable frame
    ≠ Scope automatically

    Relation representation
    ≠ represented Relation itself

---

# 197. Boundary concepts outside full 013 ontology

`013` uses neighboring concepts only to establish Relation boundaries.

These include:

- Claim;
- State;
- Event;
- Process;
- Action;
- Result;
- Observation;
- Measurement;
- Assessment;
- Inference;
- Source;
- Identity;
- Coreference;
- Classification;
- Causality;
- Membership;
- Part-whole;
- Dependency;
- Evidence Use;
- Quantification;
- Scope;
- Context.

`013` does not assert that their complete ontology belongs inside Relation standard.

---

# 198. Тест на разрастание сущностей

`013` НЕ требует введения следующих fundamental Core Entities только ради Relations:

- RelationType;
- RelationModel;
- RelationInstance;
- RelationOccurrence;
- RelationParticipant;
- RelationPosition;
- RelationRole;
- RelationFrame;
- RelationContext;
- RelationScope;
- RelationQualifier;
- RelationInterval;
- RelationStrength;
- RelationConfidence;
- RelationProbability;
- BinaryRelation;
- NaryRelation;
- DirectedRelation;
- SymmetricRelation;
- CausalRelation;
- SpatialRelation;
- TemporalRelation;
- StatisticalRelation;
- EvidentialRelation;
- IdentityRelation;
- CoreferenceRelation;
- SimilarityRelation;
- MembershipRelation;
- PartOfRelation;
- DependencyRelation;
- NormativeRelation;
- InstitutionalRelation;
- RelationAssertion;
- RelationNegation;
- RelationAbsence;
- RelationConflict;
- RelationVersion;
- CompositionRule;
- RelationClosure.

эти МОЖЕТ быть представлен through:

- semantic roles;
- Relation definitions;
- generic Relation infrastructure;
- Records;
- Profiles;
- Claims;
- States;
- Models;
- temporal structures;
- provenance structures;
- future standards.

Absence of separate Core Entity does not mean absence of corresponding semantics.

---

# 199. Core invariants

Следующие положения образуют минимальное нормативное ядро `013-RELATION`.

### RL-01
Relation является semantic construct, representing Один определённый semantic linkage among resolvable semantic positions/participants within Один resolvable applicable frame.

### RL-02
Relation semantics МОЖЕТ быть materialized as specialized Record когда материально useful, Но separate Relation Entity is not universally mandatory.

### RL-03
Relation representation existence НЕ ДОЛЖЕН автоматически означать that представленный Relation objectively holds.

### RL-04
Storage/graph implementation НЕ ДОЛЖЕН определять canonical Relation ontology.

### RL-05
Property, attribute или predicate НЕ ДОЛЖЕН автоматически быть treated as canonical Relation.

### RL-06
Co-occurrence, spatial proximity, temporal proximity или textual proximity НЕ ДОЛЖЕН автоматически определять Один specific Relation type.

### RL-07
Relation type, Relation model и Relation instance ДОЛЖЕН оставаться semantically distinguishable.

### RL-08
Relation type НЕ ДОЛЖЕН автоматически быть treated as Relation model или Relation instance.

### RL-09
Relation model НЕ ДОЛЖЕН автоматически быть treated as Relation instance или Relation truth.

### RL-10
Mere enumeration, cataloguing или documentation из Relation types НЕ ДОЛЖЕН автоматически быть treated as Relation model.

### RL-11
Model edge НЕ ДОЛЖЕН автоматически быть treated as представленный/historical Relation instance.

### RL-12
Generic Relation knowledge НЕ ДОЛЖЕН автоматически устанавливать Один specific historical Relation instance.

### RL-13
Class-level/generic Relation НЕ ДОЛЖЕН автоматически становиться universal instance-level Relation.

### RL-14
Multiple instance-level Relations НЕ ДОЛЖЕН автоматически устанавливать class-level/generic Relation.

### RL-15
Generalization из Relation instances ДОЛЖЕН требовать explicit Inference, Model, aggregation rule или other justified semantics.

### RL-16
материально relevant quantification и modality ДОЛЖЕН оставаться разрешимым.

### RL-17
Relation ДОЛЖЕН иметь sufficiently определённый Relation semantics.

### RL-18
Relation ДОЛЖЕН иметь resolvable semantic positions и participants где applicable.

### RL-19
Relation ДОЛЖЕН иметь Один resolvable applicable frame.

### RL-20
Applicable frame и Scope ДОЛЖЕН оставаться различимым где conflation would материально alter meaning.

### RL-21
Participant roles ДОЛЖЕН оставаться разрешимым когда omission would материально alter meaning.

### RL-22
Relation attribution is semantic requirement и НЕ ДОЛЖЕН требовать dedicated Core Entity solely for conformance.

### RL-23
Relation arity ДОЛЖЕН оставаться различимым из number из различимый participant identities.

### RL-24
Core НЕ ДОЛЖЕН принуждать every Relation into binary representation когда материально relevant n-ary semantics would быть lost.

### RL-25
N-ary Relation НЕ ДОЛЖЕН быть decomposed into binary edges Если decomposition destroys материально relevant role/qualifier structure.

### RL-26
Participant role ДОЛЖЕН оставаться различимым из participant identity.

### RL-27
Ordered/asymmetric participant roles ДОЛЖЕН оставаться различимым из graph directionality когда материально relevant.

### RL-28
Direction ДОЛЖЕН быть сохранённый когда материально relevant.

### RL-29
Inverse Relation НЕ ДОЛЖЕН быть придуманный если не Relation semantics defines Это.

### RL-30
Symmetry, asymmetry, transitivity, reflexivity, functionality и other formal properties НЕ ДОЛЖЕН быть предполагаемым universally.

### RL-31
Formal Relation properties СЛЕДУЕТ быть understood relative to определённый Relation type/frame/model.

### RL-32
Formal property допустимый в Frame X НЕ ДОЛЖЕН автоматически быть transferred to Frame Y.

### RL-33
Relation chaining НЕ ДОЛЖЕН автоматически устанавливать Один new direct Relation если не explicit logic licenses Этот Inference.

### RL-34
Relation composition ДОЛЖЕН оставаться различимым из transitivity.

### RL-35
Heterogeneous composition НЕ ДОЛЖЕН быть inferred без определённый composition logic.

### RL-36
Inferred closure Relations ДОЛЖЕН сохранять derivation/provenance.

### RL-37
Claim about Relation ДОЛЖЕН оставаться различимым из Relation.

### RL-38
Inferred Relation ДОЛЖЕН оставаться различимым из Inference itself.

### RL-39
Relation ДОЛЖЕН оставаться различимым из Event, Process, Action и Result.

### RL-40
Relation и State МОЖЕТ overlap в relational-State semantics Но НЕ ДОЛЖЕН схлопываться universally.

### RL-41
Relation temporal/domain validity ДОЛЖЕН оставаться различимым из record time, assertion/publication time, representation history и epistemic acceptance interval.

### RL-42
Relation snapshot НЕ ДОЛЖЕН автоматически expand into interval validity.

### RL-43
Open-ended Relation validity НЕ ДОЛЖЕН автоматически означать current или permanent validity.

### RL-44
Absence из Evidence из Relation termination НЕ ДОЛЖЕН автоматически устанавливать persistence.

### RL-45
Current Relation НЕ ДОЛЖЕН незаметно overwrite historical Relation.

### RL-46
Changed Relation representation НЕ ДОЛЖЕН автоматически означать представленный Relation changed.

### RL-47
Identity из Relation representation ДОЛЖЕН оставаться различимым из identity/continuity из представленный Relation instance.

### RL-48
Relation instance identity МОЖЕТ зависеть от полный материально relevant participant-role/qualifier/frame structure.

### RL-49
Same participants и same Relation type НЕ ДОЛЖЕН автоматически означать same Relation instance.

### RL-50
Change в qualifier/value НЕ ДОЛЖЕН автоматически определять either continuity или replacement из Relation instance.

### RL-51
Relation continuity/identity under qualifier/value change ДОЛЖЕН зависеть от определённый domain/Profile semantics.

### RL-52
Different provenance НЕ ДОЛЖЕН автоматически означать different представленный Relation instance.

### RL-53
Generic Relation НЕ ДОЛЖЕН незаметно inherit stronger Relation semantics.

### RL-54
известный specific Relation НЕ СЛЕДУЕТ быть degraded to generic Relation когда specificity is материально relevant.

### RL-55
Association НЕ ДОЛЖЕН автоматически становиться dependency или causality.

### RL-56
Similarity НЕ ДОЛЖЕН автоматически становиться identity.

### RL-57
Similarity СЛЕДУЕТ сохранять материально relevant comparison basis.

### RL-58
Temporal order НЕ ДОЛЖЕН автоматически становиться causality.

### RL-59
Part-из, member-из, containment и temporal containment ДОЛЖЕН оставаться различимым когда материально relevant.

### RL-60
Causal Relation НЕ ДОЛЖЕН быть inferred solely из correlation, temporal order, proximity, co-occurrence, sequence или narrative.

### RL-61
Causal Relation НЕ ДОЛЖЕН автоматически означать responsibility, blame, intention или negligence.

### RL-62
Dependency НЕ ДОЛЖЕН автоматически означать causality.

### RL-63
Enabling Relation НЕ ДОЛЖЕН автоматически означать occurrence.

### RL-64
Evidence поддерживать НЕ ДОЛЖЕН автоматически означать proof или truth.

### RL-65
Multiple supporting Relations НЕ ДОЛЖЕН автоматически быть treated as independent evidence lines.

### RL-66
Contradiction Relation НЕ ДОЛЖЕН автоматически означать that one Claim is false без further epistemic analysis.

### RL-67
Consistent-с НЕ ДОЛЖЕН автоматически означать confirmation или strong поддерживать.

### RL-68
Derived-из НЕ ДОЛЖЕН автоматически означать causal production.

### RL-69
Citation НЕ ДОЛЖЕН автоматически означать evidential поддерживать или independent corroboration.

### RL-70
Reference Relation НЕ ДОЛЖЕН автоматически означать endorsement, dependency или identity.

### RL-71
Entity identity, coreference, Record identity, representation identity и semantic equivalence ДОЛЖЕН оставаться различимым когда материально relevant.

### RL-72
`same-as` НЕ ДОЛЖЕН быть used as universal bucket for identity-like semantics.

### RL-73
Identity Relation ДОЛЖЕН требовать stronger поддерживать than similarity, label equality или overlapping properties.

### RL-74
Equivalence ДОЛЖЕН оставаться различимым из identity когда материально relevant.

### RL-75
Version/supersession/replacement Relations ДОЛЖЕН сохранять historical provenance и НЕ ДОЛЖЕН автоматически erase prior representations.

### RL-76
Classification Relations such as instance-из и subclass-из ДОЛЖЕН оставаться различимым.

### RL-77
Normative Relation НЕ ДОЛЖЕН автоматически становиться actual Action/State Relation.

### RL-78
Authorization НЕ ДОЛЖЕН автоматически означать Action.

### RL-79
Obligation НЕ ДОЛЖЕН автоматически означать compliance.

### RL-80
Prohibition НЕ ДОЛЖЕН автоматически означать empirical absence.

### RL-81
Legal Relation и de facto Relation ДОЛЖЕН оставаться различимым когда материально relevant.

### RL-82
Participation НЕ ДОЛЖЕН автоматически означать causation, responsibility, leadership или intention.

### RL-83
Presence-at НЕ ДОЛЖЕН автоматически означать participation-в или witness-из.

### RL-84
Transformation Relation НЕ ДОЛЖЕН автоматически устанавливать identity continuity.

### RL-85
неизвестный Relation, no-record-из-Relation и Relation absence ДОЛЖЕН оставаться различимым.

### RL-86
Negated Relation ДОЛЖЕН оставаться различимым из неизвестный, unrecorded, incompatible и prohibited Relation semantics.

### RL-87
Negation из Relation НЕ ДОЛЖЕН автоматически требовать Один special negative Relation Entity.

### RL-88
Relation conflict НЕ ДОЛЖЕН быть asserted before материально sufficient participant, role, temporal, Context, Scope, qualifier, quantification и type alignment.

### RL-89
External Relation labels НЕ ДОЛЖЕН автоматически определять canonical Relation type.

### RL-90
Natural-language ambiguity НЕ ДОЛЖЕН быть resolved by inventing missing direction, causality, strength, quantification или role semantics.

### RL-91
Observed, measured, computed, inferred, modeled и reconstructed Relation provenance МОЖЕТ overlap и ДОЛЖЕН оставаться разрешимым когда материально relevant.

### RL-92
Relation strength ДОЛЖЕН оставаться Relation-type-specific и НЕ ДОЛЖЕН receive universal scale semantics.

### RL-93
Probabilistic Relation НЕ ДОЛЖЕН незаметно становиться deterministic Relation.

### RL-94
Statistical Relation ДОЛЖЕН сохранять материально relevant population, period и conditioning frame.

### RL-95
Correlation НЕ ДОЛЖЕН автоматически становиться causation.

### RL-96
Marginal association/correlation НЕ ДОЛЖЕН автоматически быть treated as conditional association/correlation.

### RL-97
Contradiction between Claims ДОЛЖЕН оставаться различимым из incompatibility between представленный world States.

### RL-98
Basis-for НЕ ДОЛЖЕН автоматически быть treated as cause-из.

### RL-99
Later-discovered Relation НЕ ДОЛЖЕН быть inserted retroactively into earlier Decision Basis.

### RL-100
Historical Relation НЕ ДОЛЖЕН незаметно inherit current participants, taxonomy, jurisdiction, Context, model или Relation-type semantics.

### RL-101
Ontology/meta-model Relations СЛЕДУЕТ оставаться различимым из domain/world Relations когда материально relevant.

### RL-102
Higher-order Relation semantics НЕ ДОЛЖЕН требовать universal reification из all Relations.

### RL-103
Один Relation representation used as participant в Один higher-order Relation ДОЛЖЕН оставаться различимым из Этот представленный Relation itself когда материально relevant.

### RL-104
Higher-order Relation ДОЛЖЕН сохранять whether its target is representation, assertion, semantic Relation instance или another referenceable layer когда Это distinction материально affects meaning.

### RL-105
Cardinality и exclusivity constraints НЕ ДОЛЖЕН быть предполагаемым universally.

### RL-106
Relation Scope ДОЛЖЕН оставаться разрешимым когда материально relevant.

### RL-107
Local/sample/aggregate Relation НЕ ДОЛЖЕН автоматически становиться global/population/individual Relation.

### RL-108
Group-level Relation НЕ ДОЛЖЕН автоматически становиться individual-level Relation, и vice versa.

### RL-109
Context-dependent Relation НЕ ДОЛЖЕН незаметно generalize across Contexts.

### RL-110
Relation role distinctions в Action/Event/Process/Result structures ДОЛЖЕН оставаться явным когда material.

### RL-111
Modeled Relation ДОЛЖЕН оставаться различимым из observed/historical Relation.

### RL-112
Representation ДОЛЖЕН сохранять материально relevant Relation type/model/instance role, semantic positions, participants, roles, arity, direction, qualifiers, quantification, temporal validity, Scope, Context, applicable frame, provenance и uncertainty.

### RL-113
Core structural/semantic conformance ДОЛЖЕН оставаться различимым из Relation truth, provenance integrity, causal validity, logical validity, Relation quality и Representation Fidelity.

### RL-114
Profile МОЖЕТ strengthen Core requirements Но НЕ ДОЛЖЕН weaken Core пока claiming compatibility с `013`.

### RL-115
материально relevant uncertainty, provenance, participant identity, participant roles, quantification, temporal validity, Scope и applicable frame ДОЛЖЕН оставаться разрешимым.

---

# 200. Stress-test framework

Архитектура `013-RELATION` должна выдерживать как минимум следующие классы атак:

1. Relation representation vs truth;
2. storage edge vs canonical Relation;
3. property/predicate vs Relation;
4. co-occurrence vs Relation;
5. Relation type vs model;
6. Relation type vs instance;
7. Relation model vs instance;
8. Relation-type enumeration vs Relation model;
9. model edge vs historical Relation;
10. generic Relation knowledge vs historical instance;
11. class-level Relation vs instance-level Relation;
12. generic quantification;
13. all/some/most/typically/may distinctions;
14. multiple instances vs generic Relation;
15. instance aggregation/generalization;
16. binary Relation;
17. n-ary Relation;
18. n-ary flattening;
19. arity vs distinct participants;
20. participant-role ambiguity;
21. repeated participant in multiple positions;
22. ordered roles vs graph directionality;
23. directed Relation;
24. inverse Relation;
25. symmetric Relation;
26. asymmetric Relation;
27. transitive Relation;
28. non-transitive Relation;
29. formal property across different frames;
30. relation chaining;
31. transitivity vs heterogeneous composition;
32. closure/inferred Relations;
33. reflexive/irreflexive semantics;
34. Relation vs Claim;
35. Relation vs Inference;
36. Relation vs Assessment;
37. Relation vs Event;
38. Relation vs State;
39. relational State reuse;
40. Relation vs Process;
41. Relation vs Action;
42. Relation vs Result;
43. applicable frame vs Scope;
44. temporal Relation validity;
45. domain validity vs record time;
46. domain validity vs publication time;
47. domain validity vs epistemic acceptance;
48. Relation snapshot vs interval;
49. open-ended Relation;
50. Relation persistence;
51. Relation establishment;
52. Relation termination;
53. current vs historical Relation;
54. Relation revision;
55. representation identity vs Relation instance identity;
56. qualified/n-ary Relation identity;
57. qualifier drift;
58. qualifier change vs Relation continuity;
59. repeated Relation after interruption;
60. different provenance of same Relation;
61. generic vs specific Relation;
62. Relation strengthening;
63. Relation weakening;
64. part-of vs member-of;
65. containment vs part-of;
66. temporal containment vs part-of;
67. membership semantics;
68. spatial Relation;
69. orientation/reference frame;
70. near semantics;
71. temporal Relation;
72. before vs cause;
73. simultaneity vs association;
74. causal Relation;
75. causal direction;
76. causal contribution;
77. cause vs responsibility;
78. dependency;
79. dependency vs causality;
80. enabling Relation;
81. inhibiting Relation;
82. evidential Relation;
83. supports vs proves;
84. multiple support edges vs independent Evidence;
85. contradicts vs false;
86. consistent-with vs confirms;
87. derived-from vs caused-by;
88. Source Relation;
89. citation vs corroboration;
90. reference vs endorsement;
91. entity identity;
92. coreference;
93. Record identity;
94. representation identity;
95. same-as bucket failure;
96. similarity vs identity;
97. similarity metric/basis;
98. equivalence vs identity;
99. version Relation;
100. supersedes vs erase-history;
101. Correction;
102. replacement;
103. successor vs identity;
104. parent/child domain ambiguity;
105. instance-of vs subclass-of;
106. class membership vs identity;
107. taxonomy/version drift;
108. normative Relation;
109. authorization vs Action;
110. obligation vs compliance;
111. prohibition vs absence;
112. institutional Relation;
113. legal vs de facto;
114. ownership;
115. control;
116. participation;
117. present-at vs participated-in;
118. witness Relation;
119. location Relation;
120. origin Relation;
121. derivation Relation;
122. transformation Relation;
123. transformation vs identity continuity;
124. Relation uncertainty;
125. unknown vs absent Relation;
126. no-record vs absent Relation;
127. negated Relation;
128. incompatible vs negated Relation;
129. prohibited vs negated Relation;
130. Relation conflict;
131. apparent conflict due to time;
132. apparent conflict due to jurisdiction;
133. apparent conflict due to quantification;
134. Relation comparison;
135. Relation normalization;
136. lexical ambiguity;
137. Relation provenance;
138. observed Relation;
139. measured Relation;
140. inferred Relation;
141. reconstructed Relation;
142. modeled Relation;
143. computed Relation;
144. overlapping provenance statuses;
145. Relation strength;
146. probabilistic Relation;
147. statistical Relation;
148. marginal vs conditional association;
149. correlation;
150. association;
151. similarity dimensions;
152. Claim contradiction vs world incompatibility;
153. support Relation;
154. basis Relation;
155. later Relation vs earlier Decision Basis;
156. historical Relation drift;
157. Relation versioning;
158. ontology Relation vs domain Relation;
159. meta-Relation;
160. Relation representation as participant;
161. represented Relation vs representation target;
162. dispute of representation vs dispute of underlying Relation;
163. higher-order Relation without universal reification;
164. Relation composition;
165. cardinality constraints;
166. functional Relation;
167. exclusive Relation;
168. Relation Scope;
169. local vs global Relation;
170. sample vs population Relation;
171. aggregate vs individual Relation;
172. ecological fallacy;
173. Context-dependent Relation;
174. Relation and Action;
175. Relation and Event;
176. Relation and State;
177. Relation and Process;
178. Relation and Result;
179. Relation and Objective;
180. Relation and Procedure;
181. Relation and Model;
182. Relation and Measurement;
183. Relation and Observation;
184. Relation and Inference;
185. Relation and Assessment;
186. translation corruption;
187. summary corruption;
188. damaged archives;
189. historical reconstruction;
190. offline preservation;
191. high-risk Profiles;
192. cross-standard collisions.

Stress-test cases не создают Core requirements самостоятельно.

Если новый test выявляет необходимое фундаментальное правило, оно должно быть внесено в соответствующий normative section.

Прохождение stress-test не является доказательством полноты или окончательности модели.

---

# 201. Принцип сохранения

При конфликте между полнотой и честностью representation предпочтение отдаётся честности.

    generic Relation
    > invented specific Relation

    association
    > invented causality

    similarity
    > invented identity

    coreference
    > invented Record identity

    support
    > invented proof

    temporal order
    > invented causal direction

    participant
    > invented responsibility

    snapshot
    > invented interval

    unknown Relation
    > false absence

    generic/class-level Relation
    > invented universal Relation

    observed instances
    > invented generic rule

    local Relation
    > false global Relation

    historical Relation
    > current-Relation substitution

    n-ary semantics
    > lossy binary flattening

    explicit uncertainty
    > invented certainty

    prohibition
    > invented empirical absence

    historical frame
    > modern-frame substitution

    explicit reference layer
    > ambiguous higher-order target

Цель стандарта — сохранить Relation настолько полно, насколько позволяют данные, **не превращая association в causality, similarity в identity, coreference в Record identity, поддерживать в proof, participation в responsibility, temporal order в causal chain, generic/class-level Relation в universal instance-level assertion, набор отдельных Relation instances в необоснованное generic rule, normative prohibition в empirical absence, storage edge в canonical ontology, Relation representation в сам представленный Relation или incomplete historical Relation в modern reconstructed certainty**.

---

# 202. Итоговая формула

В наиболее компактной форме:

    Entity / Record / Value
    → что может занимать
      semantic position

    Relation type
    → какой reusable kind
      semantic linkage определён

    Relation model
    → какая model-level structure
      Relations/types определена

    Relation instance
    → какая конкретная linkage
      представлена между определённый positions
      в applicable frame

    Applicable frame
    → в какой semantic/reference system
      Relation интерпретируется

    Scope
    → к какой части domain/population/
      participants Relation применяется

    Claim
    → что утверждается
      о Relation или других semantics

    State
    → каким представлен
      condition/configuration

    Event
    → что произошло

    Process
    → как dynamics unfolds

    Action
    → что было сделано

    Result
    → какую downstream/result role
      phenomenon занимает

Центральный принцип `013-RELATION`:

> **Сохранить Relation — значит сохранить максимально честное представление о semantic linkage между определённый semantic positions/participants вместе с материально relevant Relation type/model/instance role, participant roles, arity, direction, qualifiers, quantification, applicable frame, Scope, temporal validity, provenance, uncertainty и reference layer.**

Факт Relation representation сам по себе не означает:

- что Relation истинна;
- что Relation causal;
- что Relation symmetric;
- что Relation transitive;
- что Relation permanent;
- что generic Relation универсальна для всех instances;
- что несколько instances образуют generic rule;
- что participant несёт responsibility;
- что similarity означает identity;
- что coreference означает Record identity;
- что поддерживать означает proof;
- что prohibition означает absence;
- что multiple поддерживать edges являются independent corroboration;
- что model edge является historical Relation;
- что storage edge является canonical Relation;
- что Relation representation и представленный Relation являются одним объектом;
- что historical Relation совпадает с current Relation.

---

# 203. Статус версии

**013-RELATION v0.1**

Стандарт прошёл:

1. первичную архитектурную сборку;
2. сквозную архитектурную атаку;
3. исправление выявленных weaknesses;
4. повторную чистую сборку;
5. контрольный аудит;
6. финальную интеграцию audit corrections.

На момент фиксации:

    Критические архитектурные дефекты:       0
    Существенные архитектурные дефекты:          0
    Известные блокирующие противоречия:        0
    Новые обязательные Core-сущности:          0
    Тест на разрастание сущностей:                PASS
    Межстандартная совместимость:         PASS
    Статус:                               CLOSED v0.1
    Финальный hardening-аудит:                PASS
    Выбранные adversarial-проверки барьеров:  PASS

Версия `0.1` является первой зафиксированной базовой версией стандарта.

Фиксация версии не означает окончательность или абсолютную полноту модели.

Стандарт остаётся пересматриваемым в соответствии с фундаментальными принципами Энциклопедии цивилизации.

---

**Чтобы знания пережили нас.**
