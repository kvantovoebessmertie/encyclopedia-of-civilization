006-INFERENCE

Проект: Энциклопедия цивилизации
Раздел: STANDARD
Статус: финальная версия стандарта
Язык: русский
Версия: v0.1

────────

1. Назначение и область стандарта

Inference нужен для представления производного знания: случаев, когда определённое содержание не было непосредственно сообщено источником, а было получено посредством рассуждения, вычисления, применения правила, модели, процедуры или иного процесс вывода.

Ключевой вопрос Inference:

> **Из чего и посредством какого переход вывода был получен данный Conclusion?**

Базовые границы:

```text
Source
→ откуда происходит зафиксированное содержание

Evidence Use
→ как материал используется evidentially относительно Claim

Assessment
→ как определённый объект оценивается

Inference
→ как определённый Conclusion представлен как derived
```

Inference является специализированным Record.

Inference не является:

```text
Claim
Evidence Use
Assessment
Source
Decision
Truth
Project endorsement
```

Наличие Inference означает только то, что определённый derivational act сохранён или представлен. Оно не означает автоматически, что Premises истинны, reasoning корректен, а Conclusion верен.

1.1. Базовое определение

> **Inference — специализированный Record, представляющий определённый акт вывода, в котором один определённый Conclusion construct представлен как выведенный посредством определённой derivational relation.**

Для обычного дискретного случая один Inference соответствует одному представленному исторический акт вывода.

Profile MAY определить непрерывный жизненный цикл, в котором последовательные derivational updates представлены как historical States одного Inference. Это lifecycle extension, а не отдельный Core type.

1.2. Draft и completed Inference

Draft / in-progress Inference MAY быть временно неполным в соответствии с общей инфраструктурой Record lifecycle.

Completed Inference MUST:

1. иметь exactly one defined Conclusion construct;
2. содержать resolvable attribution, что данный Conclusion представлен как derived.

1.3. Основные термины

Defined / определённый — имеющий достаточно установленную semantics для корректной интерпретации в рамках применимого Standard/Profile; отдельный Record не обязателен.

Resolvable / разрешимый — такой, semantic role, object, State, relation или historical meaning которого могут быть восстановлены из сохранённой структуры, references, provenance/history без изобретения отсутствующего смысла.

Resolvable не означает «доступный онлайн».

Materially required / материально необходимый — такой элемент semantics, отсутствие, изменение или неверное представление которого способно существенно изменить:

• идентификацию акт вывода;
• понимание derivation;
• интерпретацию Conclusion;
• transfer/applicability;
• dependency analysis;
• заявленную reproducibility;
• historical attribution.

────────

2. Посылки, допущения и основание вывода (Inference Basis)

2.1. Premise

> **Premise — семантическая роль определённого содержания внутри конкретного Inference, в которой это содержание используется как основание вывода.**

Premise не является отдельной Core Entity.

```text
Claim C
≠ intrinsically Premise

Claim C
used in Inference I
→ Premise role in I
```

Completed Inference MAY иметь:

```text
0..N explicit Premise roles
```

Zero-premise Inference допустим только тогда, когда derivational semantics позволяют понять, почему Conclusion получен без explicit Premises. Bare Conclusion сам по себе не является Inference.

2.2. Точность ссылки на Premise

Premise reference MUST разрешать фактически используемое содержание, а не только содержащий его объект, если без этого materially искажается derivation. В остальных случаях MAY использоваться более общая ссылка, если её смысл остаётся однозначно resolvable.

Например, если reasoning использует только результат Assessment, ссылка на весь Assessment может быть недостаточно точной.

PremiseUse как отдельная Core Entity не требуется.

2.3. Premise не равно Evidence Use и Assessment Input

```text
Premise
→ input role in акт вывода

Assessment Input
→ input role in evaluative act

Evidence Use
→ evidential relation относительно Claim
```

Один и тот же Record MAY участвовать в нескольких этих ролях, но сами роли не тождественны.

Evidence Use MUST NOT автоматически порождать Inference.

Inference MUST NOT автоматически порождать Evidence Use.

2.4. Assumption

> **Assumption — Premise role или qualifier, указывающий, что соответствующее содержание принимается условно, рабоче или без утверждения о его установленности в рамках данного Inference.**

То есть Assumption не является отдельным вторым классом inputs и не требует отдельной Core Entity.

```text
Assumption
⊂ premise-role semantics
```

Assumption не определяется качеством Premise:

```text
poorly supported Premise
≠ Assumption automatically
```

Фундаментальные границы:

```text
unknown assumption
≠ no assumption

no recorded assumption
≠ assumption-free inference
```

Known/reconstructable materially necessary assumptions MUST NOT быть скрыты в representation, заявляющей достаточную derivational fidelity.

2.5. Assumption discharge

Использование assumption не означает, что она навсегда остаётся внешним условием downstream reasoning.

Formal/Profile semantics MAY определять:

• active assumption;
• discharged assumption;
• conditionalized assumption;
• local proof assumption.

Если assumption legitimately discharged, downstream Conclusion не обязан наследовать её как active Context.

2.6. Inference Basis

> **Inference Basis — materially relevant derivational rules, methods, models, procedures или иная semantics, посредством которой Conclusion выводится.**

```text
Premise
→ ground/content

Inference Basis
→ derivational mechanism
```

Inference Basis MAY быть composite.

Отдельная Entity InferenceBasis не требуется.

Фундаментальные границы:

```text
Premise
≠ Inference Basis
≠ execution provenance
```

И:

```text
Basis unknown
≠ no Basis
```

2.7. THAT derivation ≠ HOW derivation

Нужно различать:

```text
известно, ЧТО
Conclusion был выведен

≠

известно, КАК
Conclusion был выведен
```

Для самого Inference фундаментально первое.

Полный Inference Basis требуется настолько, насколько он materially необходим для честной интерпретации, проверки, transfer или заявленной reproducibility.

Unknown Basis MUST NOT заменяться invented Basis.

2.8. Composition principle

Inference Basis SHOULD представлять derivational mechanism.

Premise, Assumption, State и Context semantics SHOULD оставаться отдельно различимыми, когда различие materially возможно и важно.

Inference Basis не должен превращаться в универсальный контейнер «всего, что относится к reasoning».

────────

3. Заключение (Conclusion), производное содержание и цепочки выводов

3.1. Conclusion

> **Conclusion — content role, в которой определённое содержание представлено как заключение конкретного акт вывода.**

Conclusion не является отдельной обязательной Core Entity.

```text
Claim C
≠ intrinsically Conclusion

Claim C
used as output of Inference I
→ Conclusion role in I
```

3.2. Cardinality

Completed Inference MUST иметь:

```text
exactly 1 defined Conclusion construct
```

Conclusion construct MAY быть:

• atomic;
• structured;
• Profile/formal-system defined multi-component.

Unrestricted bag of unrelated outputs не является legitimate Conclusion construct одного Inference.

3.3. Conclusion role не заменяет ontology content

```text
Claim in Conclusion role
→ remains Claim

Measurement-like content in Conclusion role
→ retains its own semantic type
```

Conclusion role задаёт derivational function, а не заменяет intrinsic semantics содержимого.

3.4. Conclusion не обязана быть Claim

Conclusion MAY быть:

• Claim;
• numeric result;
• probability distribution;
• classification;
• structured datum;
• иной defined content.

Proposition-like Conclusion SHOULD быть representable как самостоятельный Claim, когда появляется independent semantic lifecycle/use.

Intermediate propositions внутри derivation не обязаны автоматически materialize как global Claims.

3.5. Одинаковый Conclusion ≠ один и тот же Inference

```text
I1:
A + B → C

I2:
D + E → C
```

Один и тот же Conclusion MAY иметь несколько derivational paths.

```text
same Conclusion
≠ same Inference
```

Также:

```text
same Premises
+
same Basis
+
same Conclusion
≠ same исторический акт вывода
```

3.6. Inference chains

Если Conclusion одного Inference используется как Premise другого:

```text
I1:
A → C

I2:
C → D
```

возникает derivational chain.

C одновременно выполняет:

```text
Conclusion role in I1
Premise role in I2
```

Отдельные Entities InferenceChain и IntermediateConclusion не требуются.

3.7. Вычисляемая derivational ancestry ≠ материализованный Inference

Из:

```text
A → B
B → C
```

system MAY вычислить derivational ancestry A ... C.

Но это MUST NOT автоматически materialize новый historical Inference:

```text
A → C
```

Materialized transitive derivation является отдельным акт вывода, если она действительно создаётся.

3.8. Granularity

Inference MAY быть macro-level representation сложной derivation.

Внутренние steps не обязаны становиться отдельными Inference Records.

Но materially necessary intermediate reasoning MUST оставаться resolvable до степени, требуемой заявленной representation/Profile.

Macro-Inference является descriptive granularity label, а не Core type.

3.9. Historical States

Если Conclusion или Premise ссылаются на mutable Records, materially relevant historical State/version MUST оставаться resolvable.

Historical Inference MUST NOT silently drift from:

```text
C@v1
```

к:

```text
C@current
```

если semantic content materially изменилось.

────────

4. Типы Inference и граница оценки корректности вывода

4.1. Нейтральность Core

006-INFERENCE описывает derivational provenance, а не устанавливает одну нормативную теорию reasoning.

Core должен поддерживать определённые derivational systems, включая:

• deductive;
• inductive;
• abductive;
• probabilistic;
• Bayesian;
• defeasible;
• analogical;
• causal;
• formal;
• computational;
• expert;
• future/unknown systems.

4.2. Inference Type

Core не определяет closed universal taxonomy типов Inference.

Classification MAY быть:

• Profile-defined;
• Method-defined;
• descriptive;
• overlapping;
• disputed;
• unknown.

Отдельное mandatory поле InferenceType не требуется.

4.3. Type ≠ Basis ≠ quality

```text
Inference Type
≠ Inference Basis

deductive
≠ valid automatically

Bayesian
≠ correct automatically

expert
≠ authoritative truth

AI-generated
≠ objective
```

Type label не заменяет materially required actual Basis semantics.

4.4. Validity, soundness, strength

Core MUST NOT требовать universal intrinsic fields:

```text
Inference.valid
Inference.sound
Inference.strength
Inference.confidence
```

Если inferential adequacy independently represented как знание, canonical model — Assessment.

Например:

```text
Assessment
Target: Inference I
Aspect: formal validity
Result: valid
```

Internal implementation state validator не обязан materialize как отдельный Assessment Record.

4.5. Premise status, adequacy и Conclusion status

Фундаментально:

```text
epistemic/content status of Premises
≠ inferential adequacy
≠ correctness/truth status of Conclusion where applicable
```

True Conclusion не исправляет плохой historical reasoning.

Bad Inference не делает Conclusion автоматически false.

4.6. Probability и modality

Materially relevant modal/probabilistic semantics MUST сохраняться.

```text
probably C
≠ C

P(C)=0.8
≠ confidence in Inference = 0.8

vote fraction 0.82
≠ P(C)=0.82
```

Inference Type MUST NOT автоматически определять modal/probabilistic force Conclusion, если такое mapping явно не задано Basis/Profile.

4.7. Deduction, induction, abduction

Deductive classification не означает validity автоматически.

Inductive strength является evaluative concept и при самостоятельном утверждении может оцениваться через Assessment.

Abductive Conclusion вида «H является лучшим доступным объяснением» не означает автоматически «H истинно».

Materially relevant candidate/explanation set SHOULD оставаться resolvable, если без него меняется смысл «лучшего».

4.8. Defeasible reasoning и Defeaters

Defeater является contextual role/relation, а не intrinsic object type или отдельной обязательной Core Entity.

MAY различаться:

• rebuttal;
• undercutting;
• premise challenge;
• assumption challenge;
• Basis challenge;
• Context challenge.

Core не определяет closed taxonomy и universal defeated/reinstated state machine.

```text
Inference subject to defeat
≠ Conclusion false automatically
```

Defeat MAY быть partial; scope SHOULD оставаться resolvable, когда material.

4.9. Необоснованная круговая поддержка

Graph cycle сам по себе не является failure.

Нужно различать:

```text
recursive computation
recursive definition
unsupported circular epistemic support
```

Необоснованная круговая поддержка (Unsupported Circular Support) возникает, когда зависимые/самоссылочные основания представлены как независимая внешняя поддержка без достаточной Basis.

4.10. Необоснованное причинное усиление

Causal inference допустим.

Failure заключается не в самом causal Conclusion, а в скрытом/необоснованном semantic upgrade.

Необоснованное причинное усиление (Unsupported Causal Upgrade) — представление causal Conclusion без resolvable materially necessary causal Basis/assumptions либо как directly contained in non-causal Premises.

────────

5. Идентичность, жизненный цикл, исправление и повторный вывод

5.1. Identity

Inference Identity MUST NOT вычисляться только из:

```text
Premises
+
Basis
+
Conclusion
```

Same semantic derivation MAY соответствовать разным исторический акт выводаs.

5.2. Correction

Correction MAY сохранять Identity, только если исправляется representation того же исторический акт вывода и его materially represented semantics остаётся той же.

Например:

• typo;
• wrong reference;
• omitted historical metadata;
• recovered historical Basis;
• corrected transcription.

Absence of rerun alone не делает semantic rewrite legitimate Correction.

5.3. Re-inference

Re-inference — новый derivational act, связанный с предыдущим.

```text
Correction
→ representation of same historical act repaired

Re-inference
→ new derivational act
```

Отдельная Entity ReInference не требуется.

5.4. Recovery vs new use

Если Premise/Basis реально участвовали в original historical act, но были omitted from Record, их восстановление MAY быть enrichment/correction.

Если Premise/Basis впервые используются сейчас при новом reasoning:

```text
→ new Inference
```

5.5. Conclusion correction

Correction of Conclusion требует достаточного основания считать, что corrected content действительно представлял original historical act.

Если historical Conclusion unresolved, uncertainty MUST сохраняться, а не заменяться наиболее удобной реконструкцией.

5.6. Continuous lifecycle

Profile MAY определить непрерывный жизненный цикл для одного Inference.

В таком случае historical States MUST сохранять или иным образом делать resolvable все materially relevant элементы, включая при применимости:

• Premise membership/state;
• assumptions;
• Basis/version;
• Context;
• Conclusion construct/state;
• execution configuration where applicable;
• time.

Continuous identity MUST NOT изобретаться ретроспективно только для сохранения прежнего ID.

Profile-defined States одной continuous identity MUST NOT искусственно представляться как independent акт выводаs, если это создаёт ложную множественность (False Multiplicity).

5.7. Execution identity ≠ Inference identity

```text
execution identity
≠ Inference identity
```

Несколько executions могут быть:

• отдельными Inferences;
• reproduction;
• States continuous Inference.

Один execution тоже не определяет автоматически отдельную Inference Identity.

5.8. Supersession

Supersession является contextual lifecycle/governance relation.

```text
superseded
≠ false
≠ deleted
```

Supersession MAY быть Profile/Context-relative и branching.

Latest ≠ preferred ≠ true.

5.9. Withdrawal

```text
withdrawn
≠ deleted
≠ Conclusion false
```

Material withdrawal reason и withdrawal provenance/authority SHOULD оставаться resolvable, когда это materially важно.

Withdrawal Inference MUST NOT автоматически удалять/негировать его Conclusion Records.

5.10. Downstream impact

Upstream correction, withdrawal или supersession MUST NOT silently rewrite historical downstream Records.

Affected downstream MAY включать:

• Inferences;
• Claims;
• Evidence Uses;
• Assessments;
• Decisions;
• иные Records.

```text
affected
≠ automatically invalid
```

Known materially relevant downstream dependencies SHOULD оставаться discoverable where feasible.

5.11. Lineage types

Когда distinction materially важно, следует различать:

```text
derivational lineage
re-inference lineage
identity/history lineage
provenance lineage
defeat relations
```

Они MAY пересекаться, но не тождественны.

────────

6. Контекст, семантическая граница, применимость и перенос

6.1. Inference Context

> **Inference Context — materially relevant внешние условия интерпретации или применения derivation.**

Context MAY включать:

• jurisdiction;
• population;
• formal system;
• historical period;
• environmental conditions;
• domain setting;
• Profile-defined conditions.

InferenceContext не является обязательной Core Entity.

Context conditionally required.

6.2. Role boundaries

```text
Premise
→ основание

Assumption
→ условно принятое Premise-content

Inference Basis
→ derivational mechanism

Context
→ внешние условия интерпретации/применения
```

Один underlying content MAY участвовать в нескольких ролях, если различия остаются resolvable when material.

6.3. Семантическая граница Inference

> **Семантическая граница Inference — совокупность materially relevant semantics, внутри которых derivational relation и Conclusion сохраняют свой заявленный смысл.**

Концептуально включает:

```text
Premise contents / States
Assumption qualifiers
Inference Basis / versions
Context where material
Conclusion construct / qualifiers
```

Inference Semantic Boundary является analytical concept:

```text
≠ Core Entity
≠ mandatory storage field
```

6.4. Applicability

Core не требует universal:

```text
Inference.applicable = true/false
```

Inference интерпретируется внутри собственной Semantic Boundary.

Applicability возникает как отдельный вопрос при transfer/reuse вне исходных условий.

6.5. Conclusion reuse ≠ Inference transfer

Повторное использование Conclusion/Claim в другом месте не означает автоматически transfer original Inference.

6.6. Transfer

Применение derivational semantics в materially другом Context MAY требовать нового Inference, Assessment или Profile-defined mapping.

Existing Inference MUST NOT silently broaden its original Context.

6.7. Выход за семантическую границу (Semantic Boundary Escape)

Conclusion/derivation MUST NOT silently представляться как имеющие более широкую applicability, чем позволяют materially relevant Premise/Assumption/Basis/Context semantics.

Context stripping или substitution, меняющие meaning, являются semantic failures.

6.8. Historical Context

Current Profile/Context MUST NOT silently replace historical Profile/Context.

Temporal roles MUST оставаться различимыми, когда различие materially важно:

• акт вывода time;
• recording time;
• Premise State time;
• Context validity time;
• Conclusion applicability time.

6.9. Context unknown

```text
no recorded Context
≠ context-free inference

unknown Context
≠ current/default Context
```

Partial historical Record MAY сохранять unresolved Context.

Recorded Context не доказывает автоматически completeness of Context.

6.10. Assumption leakage

Active assumption MUST NOT silently исчезать downstream, если Conclusion remains assumption-dependent.

Это не относится к legitimately discharged/encoded assumptions.

────────

7. Конкурирующие выводы, зависимость и независимость

7.1. Competing Inferences

Competing Inferences MAY coexist.

Одинаковый Conclusion ≠ один и тот же Inference.

Different Conclusions ≠ substantive conflict automatically.

Перед classification substantive conflict SHOULD сравниваться materially relevant Semantic Boundaries.

Inference.competing не является universal intrinsic bool.

7.2. Dependency

Dependency является relational concept.

```text
distinct Inference
≠ independent Inference
```

Different IDs/authors/models/Premise labels не доказывают independence.

Same model/author не доказывают dependence автоматически.

7.3. Independence

Independence MAY быть:

• relational;
• dimension-relative;
• partial;
• unknown.

Core не требует universal binary:

```text
Inference.independent = true/false
```

Фундаментально:

```text
unknown dependence
≠ independence
```

7.4. Same Conclusion ≠ dependency

Совпадающий Conclusion сам по себе не создаёт dependency.

Dependency требует shared ancestry/process/data/source/model/other relation.

7.5. Shared Method

Shared Basis/Method MAY быть одной dimension dependency, но MUST NOT автоматически считаться materially significant informational dependence.

7.6. Inference independence ≠ Evidence Use independence

Эти relations связаны, но не тождественны.

Одна MUST NOT silently подменять другую.

7.7. Ложная множественность (False Multiplicity)

> **Ложная множественность (False Multiplicity) — представление одной или materially dependent informational/derivational basis как нескольких independent или существенно более plural contributions.**

Примеры:

• duplicate import;
• paraphrase counted as new independent ground;
• repeated deterministic run counted as independent derivation.

Ложная множественность (False Multiplicity) является diagnostic concept, не Core Entity.

7.8. Dependency ≠ defect

Dependency сама по себе не является качественной ошибкой.

Failure возникает при misleading representation of dependency, unsupported independence или unsupported additive use.

7.9. Corroboration, agreement и consensus

```text
agreement
≠ corroboration automatically
≠ consensus automatically
≠ truth automatically
```

Conclusion о нескольких independent derivational paths требует отдельного basis for independence.

Raw count Inferences не является universal truth/confidence rule.

────────

8. Синтез, агрегация и множественные входы

8.1. Synthesis

Synthesis используется в этом стандарте как descriptive process/function term.

Он не является обязательной Core Entity.

Aggregation — одна возможная synthesis strategy, а не synonym всех forms synthesis.

8.2. Ordinary Inference for synthesis

Prior Inference Conclusions, Claims, Assessments, Evidence Uses, Measurements и другие defined contents MAY выполнять Premise roles нового Inference.

Новые Entities AggregateInference, MetaInference, MetaSynthesis не требуются.

8.3. Whole-record reference

Whole Inference/Assessment/other Record MAY быть Premise, если используются свойства самого Record.

Если используется specific conclusion/result/content, reference SHOULD разрешать именно materially used content.

Storage syntax implementation-specific.

8.4. Использование Record как Premise ≠ endorsement его содержания

Использование Record как Premise MUST различать:

• факт существования Record;
• то, что Record сообщает;
• использование его content;
• endorsement/correctness этого content.

Например:

```text
Assessment A reports high risk
```

не равно:

```text
risk is objectively high
```

8.5. Aggregate Assessment ≠ Inference synthesis

```text
new evaluative Result
→ Assessment

new derivational Conclusion
→ Inference
```

Semantic role, а не surface wording, определяет Record type.

Один process MAY производить несколько Records разных semantic types.

8.6. Voting

Voting MAY быть defined Basis.

Он может вывести proposition about procedural result:

```text
majority selected C
```

Но это не автоматически:

```text
C is true
```

Vote outcome ≠ truth/confidence/evidential strength automatically.

8.7. Weighting

Weight/priority operation-relative.

Он MAY быть:

• numeric;
• ordinal;
• categorical;
• rule-based.

Нет universal intrinsic Inference.weight.

Assessment/confidence values не становятся weights без explicit mapping.

8.8. Dependency-sensitive synthesis

Known dependency MUST NOT игнорироваться/искажаться там, где synthesis semantics реально опираются на:

• independence;
• multiplicity;
• additive contribution;
• independent corroboration.

Ordinary logical synthesis не обязан моделировать independence, если Basis этого не требует.

Unknown dependence ≠ independence.

8.9. Selection

Нужно различать:

```text
selection criterion
≠ selected membership
```

Selection criterion MAY быть частью Basis.

Historical selected membership относится к actual input state.

Absence from membership не означает автоматически explicit exclusion.

8.10. Completeness

```text
recorded membership
≠ complete universe
```

Claim «рассмотрены все relevant Inferences» требует отдельного resolvable basis.

8.11. Принудительный консенсус (Forced Consensus)

Core MUST NOT требовать one winner.

Legitimate Conclusion MAY быть structured status disagreement/plurality/unresolved state, если exact semantics определена Profile/Basis.

Такие labels не являются closed Core vocabulary.

8.12. Scalarization, scores и uncertainty

```text
vote fraction
≠ probability

score
≠ confidence

missing uncertainty
≠ zero uncertainty

missing quality Assessment
≠ high quality
```

Unsupported scalarization/weighting не являются implicit Core operations.

Uncertainty propagation требует defined Basis.

8.13. Synthesis lifecycle

Rolling synthesis MAY использовать Profile-defined continuous Inference lifecycle.

Historical membership MUST NOT silently absorb later inputs.

Synthesis MUST NOT destructively replace its input Records.

Competing syntheses MAY coexist.

────────

9. Соответствие стандарту, целостность и точность представления

9.1. Diagnostic architecture

A. Canonical Inference Record

1. Ontology / Core invariants
2. Conformance
  • Structural
  • Referential
  • Semantic
  • Contextual-Historical
3. Integrity / Provenance
4. Epistemic / Methodological
5. Governance / Operational

B. Representation

6. Representation Fidelity

Dimensions MAY overlap.

Representation Fidelity orthogonal to canonical Record conformance.

9.2. Core Conformance

Core-conformant completed Inference MUST:

• удовлетворять Core ontology;
• иметь exactly one defined Conclusion construct;
• иметь resolvable derivational attribution;
• сохранять materially required semantic/historical conditions.

Но:

```text
Core Conformance
≠ inferential adequacy
≠ Conclusion correctness/truth
≠ project endorsement
```

9.3. Structural Conformance

Относится к допустимой форме Record и Profile-defined requirements.

Draft/in-progress Record MAY быть временно неполным.

9.4. Referential Conformance

Materially required references должны быть resolvable.

Broken historical reference ≠ fabricated reference.

9.5. Semantic Conformance

Present/materially required roles должны быть достаточно ясны:

• Premise;
• Conclusion;
• Assumption;
• Basis;
• Context;
• modal/probability semantics;
• used content.

9.6. Contextual-Historical Conformance

Historical Premise/Conclusion/Basis/Profile/Context States MUST NOT silently resolve to materially different current States.

9.7. Integrity / Provenance

Integrity concerns fidelity of recorded history/provenance.

```text
false Premise content
≠ fabricated claim that Premise was historically used
```

Missing provenance ≠ false provenance.

Unknown Basis/Context/State MUST NOT заменяться invented semantics.

Error ≠ fraud automatically.

9.8. Inferential adequacy

Core-conformant Inference MAY быть methodologically poor.

If adequacy independently represented, it MAY be assessed through ordinary Assessment.

9.9. Representation Fidelity

Full fidelity означает semantic recoverability, а не byte-for-byte serialization identity.

```text
JSON
Markdown
paper
```

MAY быть semantically equivalent representations.

Lossy representation MAY быть legitimate, если она соответствует declared/reasonably implied purpose.

9.10. Derivational compression

Compression MAY omit non-material steps.

Но MUST NOT fabricate direct attribution.

```text
Source S says A
Inference derives B
Inference derives C
```

не должно превращаться в:

```text
Source S says C
```

Legitimate summary MAY говорить:

> На основании Source S и последующего reasoning получено C.

9.11. Translation fidelity

Full-fidelity translation MUST сохранять materially relevant:

• modality;
• negation;
• quantifiers;
• scope;
• conditionality;
• probability.

Language label itself не определяет semantic identity.

9.12. Partial historical/imported Records

Partial historical representation MAY сохраняться как valuable record, даже если она не соответствует full completed Core conformance.

Unknown import semantics MUST оставаться unknown.

Importer MUST NOT assign Method/Type/Basis без основания.

Import ≠ endorsement.

9.13. Semantic preservation ≠ executable reproduction

Semantic preservation не гарантирует future executable reproduction.

Historical proprietary/opaque mechanisms MAY быть unavailable.

Core representation SHOULD оставаться interpretable offline в максимально возможной степени, поддерживаемой сохранённой semantics.

Unavailable mechanism MUST оставаться обозначенным как unavailable/unknown, а не реконструироваться догадкой.

9.14. Carrier neutrality

Carrier migration:

```text
DB → Markdown → paper → future DB
```

не создаёт new Inference автоматически.

Core MUST NOT зависеть от:

• JSON;
• RDF;
• SQL;
• Markdown;
• Git;
• HTTP;
• current AI model;
• current software stack.

────────

10. Диагностические антипаттерны и результаты стресс-тестирования

10.1. Статус этого раздела

Этот раздел является diagnostic/стресс-тестирование layer.

Он:

```text
≠ Core ontology
≠ closed taxonomy
≠ allegation of malicious intent
```

ПРОЙДЕН в стресс-тест означает только то, что архитектура способна корректно представить случай без противоречия и без введения новой фундаментальной Entity. Это не оценка истинности или качества reasoning.

Полный набор рабочих стресс-тесты относится к истории валидации стандарта. Настоящий раздел сохраняет их сгруппированное резюме и не превращает каждый тест в отдельное нормативное правило Core.

10.2. Основные diagnostic families

Semantic origin failures

• Подмена происхождения Premise (Premise Laundering);
• Подмена происхождения Conclusion (Conclusion Laundering);
• Подмена происхождения Assumption (Assumption Laundering);
• Подмена основания вывода (Basis Laundering);
• Подмена контекста (Context Laundering);
• Подмена вероятности и уверенности (Probability/Confidence Laundering);
• Подмена авторитетом (Authority Laundering).

Boundary failures

• Выход за семантическую границу (Semantic Boundary Escape);
• Удаление контекста (Context Stripping);
• Подмена контекста (Context Substitution);
• Утечка допущения (Assumption Leakage);
• Дрейф состояния/версии (State/Version Drift);
• Дрейф Profile (Profile Drift).

Lifecycle failures

• Ложное исправление (Fake Correction);
• Скрытый повторный вывод (Silent Re-inference);
• Ложное непрерывное слияние (False Continuous Merge);
• Ложная фрагментация (False Fragmentation);
• Подмена жизненного цикла (Lifecycle Laundering).

Dependency failures

• Ложная множественность (False Multiplicity);
• Необоснованная независимость (Unsupported Independence);
• Сокрытие зависимости (Dependency Hiding);
• Подмена зависимости (Dependency Laundering);
• Двойной учёт (Double Counting);
• Ошибочное схлопывание дубликатов (Duplicate Collapse).

Synthesis failures

• Скрытый отбор (Hidden Selection);
• misleading Selective Input Omission;
• Принудительный консенсус (Forced Consensus);
• Необоснованное взвешивание (Unsupported Weighting);
• Необоснованная скаляризация (Unsupported Scalarization);
• Искусственное усиление уверенности множественностью (Confidence Amplification by Multiplicity).

Reasoning-specific failures

• Необоснованное причинное усиление (Unsupported Causal Upgrade);
• Необоснованная круговая поддержка (Unsupported Circular Support).

10.3. Selective omission

Selective omission не является failure автоматически.

Failure возникает, когда omission:

• нарушает declared scope/Profile;
• скрывает materially relevant selection;
• поддерживает ложную completeness claim;
• materially искажает Conclusion.

Intent не выводится автоматически.

10.4. Machine validation

Machine validator MAY проверять implemented/decidable:

• structure;
• cardinality;
• references;
• Profile requirements;
• formal syntax;
• formal rule application.

Machine validation ≠ truth privilege.

Следует различать:

```text
proof object
≠ proof execution
≠ proof verification
```

Повторное выполнение или независимое воспроизведение derivation не является автоматически тем же historical Inference и не доказывает independence без соответствующей provenance.

Closed-world и open-world assumptions, если они materially меняют смысл derivation, MUST быть resolvable как часть Assumption/Basis/Context semantics.

Validator output MAY itself be assessed.

10.5. Core vs Profile

Record MAY:

```text
Core PASS
Profile FAIL
```

без противоречия.

Profiles MAY strengthen Core requirements.

Profile MUST NOT weaken Core invariants while claiming Core compatibility.

10.6. Stress-test families

Модель была проверена на следующих классах случаев:

1. simple/zero-premise/draft Inference;
2. Premises, Assumptions и unknown Basis;
3. structured Conclusions и long chains;
4. formal, inductive, abductive, probabilistic, causal и defeasible reasoning;
5. human, expert, AI и black-box derivations;
6. Context, transfer и Semantic Boundary;
7. identity, correction, re-inference и continuous lifecycle;
8. dependency, independence, competition и Ложная множественность (False Multiplicity);
9. synthesis, weighting, voting, selection и consensus;
10. import/export, translation, offline preservation и damaged archives.

Результат системного стресс-тест:

```text
Новая fundamental Core Entity: не требуется
Forced ontology rewrite: не требуется
Premise Entity: не требуется
Conclusion Entity: не требуется
Defeater Entity: не требуется
InferenceContext Entity: не требуется
AggregateInference: не требуется
MetaInference: не требуется
Universal validity field: не требуется
Universal consensus engine: не требуется
```

────────

11. Инварианты ядра (Core invariants)

Ниже находится компактное нормативное ядро 006-INFERENCE.

Этот раздел является каноническим сводом фундаментальных требований Core. Нормативные формулировки в предыдущих разделах конкретизируют применение этих инвариантов к отдельным semantic situations и MUST NOT интерпретироваться как создание параллельного или более широкого Core.

При кажущемся противоречии между пояснительным текстом и инвариантом Core приоритет имеет инвариант Core.

1. Inference является specialized Record.
2. Completed Inference MUST иметь exactly one defined Conclusion construct.
3. Completed Inference MUST представлять resolvable derivational attribution: Conclusion представлен как derived.
4. Inference MAY иметь 0..N explicit Premise roles.
5. Zero-premise Inference MUST иметь достаточную derivational semantics; bare Conclusion не является Inference автоматически.
6. Premise и Conclusion являются roles, а не intrinsic object types.
7. Conclusion role MUST NOT уничтожать или заменять ontology occupying content.
8. Materially required historical States, qualifiers, Basis, Context и derivational semantics MUST оставаться resolvable.
9. Unknown semantics MUST NOT заменяться invented semantics.
10. Derived content MUST NOT falsely be attributed as directly stated, contained or observed upstream.
11. Existence или Core Conformance Inference MUST NOT автоматически означать correctness, truth, soundness, adequacy или project endorsement.
12. Materially new акт вывода MUST NOT masquerade as Correction старого act.
13. Historical Inference MUST NOT silently drift to materially different current Premise/Basis/Profile/Context States.
14. Distinct Inference Identity MUST NOT автоматически означать independence.
15. Unknown dependence MUST NOT автоматически трактоваться как independence.
16. Representation compression MUST NOT fabricate direct source/derivational attribution.
17. Core Conformance MUST оставаться distinct from inferential adequacy.
18. Profiles MAY strengthen requirements, but MUST NOT weaken Core invariants while claiming compatibility with 006-INFERENCE.

────────

12. Ключевые семантические границы

```text
Inference
≠ Claim
≠ Evidence Use
≠ Assessment
≠ Source
≠ Decision
≠ Truth/Correctness
≠ Endorsement
```

```text
Premise
≠ Assessment Input
≠ Evidence Use
```

```text
Premise
≠ Inference Basis
≠ Context
```

```text
Assumption
= qualified Premise role
≠ established fact
```

```text
Conclusion role
≠ ontology of occupying content
```

```text
Inference Type
≠ Inference Basis
≠ inferential adequacy
```

```text
derivational lineage
≠ re-inference lineage
≠ identity/history lineage
≠ defeat relation
```

```text
distinct
≠ independent
```

```text
agreement
≠ corroboration
≠ consensus
≠ truth
```

```text
Core Conformance
≠ inferential adequacy
≠ Conclusion correctness
≠ project endorsement
```

────────

13. Принципы сохранения

1. Historical semantics SHOULD сохраняться независимо от carrier.
2. Current mutable content MUST NOT silently substitute materially different historical States.
3. Partial records MAY сохраняться честно без invented completion.
4. Unknown MUST оставаться unknown, если нет достаточного основания для уточнения.
5. Offline preservation SHOULD максимизировать future semantic interpretability.
6. Semantic preservation ≠ guaranteed executable reproduction.
7. При full-fidelity translation materially relevant semantic force MUST сохраняться. При намеренно lossy representation требования определяются заявленным уровнем fidelity, однако representation MUST NOT materially искажать смысл.
8. Competing derivations, unresolved plurality и historical erroneous reasoning MAY сохраняться без project endorsement.

────────

14. Итог

006-INFERENCE задаёт минимальную архитектуру для сохранения производного знания.

Его центральная функция — не решать, какой вывод истинный, а сохранять:

```text
что использовалось как основание;
что было выведено;
что это действительно было derived content;
каким способом и при каких условиях — насколько это materially известно;
как derivation связана с другими Records и historical States.
```

Главная защита стандарта:

```text
Source says A
Inference derives B
Chain derives C

≠

Source says C
```

006-INFERENCE тем самым обеспечивает разделение между непосредственно зафиксированным содержанием и знаниями, возникшими позднее посредством reasoning.

────────

Статус после сборки: единый исправленный документ, подготовленный по результатам локальных аудитов глав 1–10, сквозной атаки глав 1–9, stress-test главы 10 и финального системного аудита глав 1–10.
