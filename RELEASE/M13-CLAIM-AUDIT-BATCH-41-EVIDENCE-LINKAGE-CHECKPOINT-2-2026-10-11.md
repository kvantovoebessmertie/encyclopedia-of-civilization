# M13 Batch 41 — Evidence-Linkage Checkpoint 2 — 2026-10-11

## Scope and gate
Diagnostic review of five additional Batch 41 candidates: Algebra Basics A–C and Analytical Chemistry Basics A–B. Claim, Evidence Use, and Source JSON records were inspected on `m13-system-wide-depth-audit-2026-10-09`; public source material was checked directly. This is not D/E/B scoring and does not complete Batch 41. No content records were edited.

## Findings

### Algebra Basics A — `CLM-ALGEBRA_BASICS-A`
- Claim: “Алгебраические выражения состоят из чисел, переменных и операций над ними.”
- Identity: filename ID and internal `record_id` match; `record_type: claim`.
- Evidence Use: `EU-ALGEBRA_BASICS-A`; Claim/Source refs resolve to the intended IDs; `evidence_role: supports`. Description is generic and has no section locator.
- Source record `SRC-ALGEBRA_BASICS` points to the OpenStax College Algebra 2e book landing page, not the exact section.
- Direct check: OpenStax section 1.1 explicitly defines an algebraic expression as constants and variables joined by algebraic operations.
- **Disposition:** substantive support PASS; traceability PARTIAL because the stored Source URL is a book landing page and the Evidence Use has no pinpoint. A correction should cite section 1.1.

### Algebra Basics B — `CLM-ALGEBRA_BASICS-B`
- Claim: “Уравнение задаёт условие равенства двух выражений и решается относительно неизвестных при допустимых преобразованиях.”
- Identity and structural links: PASS; Evidence Use role is `supports`; description is generic.
- Direct check: OpenStax section 1.1 defines an equation as a mathematical statement that two expressions are equal and explains solutions as values making the equation true. The source also illustrates solving by substituting a value and using properties of real numbers.
- **Disposition:** core definition supported. The “допустимых преобразованиях” clause is mathematically reasonable but should be tied to the text's explanation of properties/solution methods, not left as an unlocated extension. Pinpoint section 1.1 (and relevant equation-solving section if a more procedural reading is intended).

### Algebra Basics C — `CLM-ALGEBRA_BASICS-C`
- Claim: “Функция связывает элементы области определения с элементами области значений по заданному правилу.”
- Identity and structural links: PASS; Evidence Use role is `supports`; description is generic.
- Direct check: OpenStax College Algebra 2e section 3.1 states that a function assigns exactly one output to each input in its domain and describes domain/range.
- **Disposition:** substantive support PASS; local traceability PARTIAL. Stored Source points only to the book landing page; Evidence Use should point to section 3.1 and its function definition.

### Analytical Chemistry Basics A — `CLM-ANALYTICAL_CHEMISTRY_BASICS-A`
- Claim: “Аналитическая химия включает методы получения и интерпретации измерительных данных о составе и свойствах образцов.”
- Identity and structural links: PASS; `EU-ANALYTICAL_CHEMISTRY_BASICS-A` points to the intended Claim and Source, with role `supports`.
- Source: NIST Tutorials in Analytical Chemistry landing page. It explicitly covers analysis of complex-matrix samples, sample extraction/processing, data treatment, quantitative analysis, chromatography, calibration and method validation.
- This source family supports the methodological/data-treatment part of the claim. The current landing page is a catalogue of tutorials rather than a single direct definition of the discipline; “properties” is broad and not pinned to a particular tutorial.
- **Disposition:** source family relevant; claim support PARTIAL pending specific tutorial/passage or a direct analytical-chemistry definition. Evidence Use description is generic.

### Analytical Chemistry Basics B — `CLM-ANALYTICAL_CHEMISTRY_BASICS-B`
- Claim: “Качество аналитического измерения зависит не только от прибора, но и от применяемого метода, образца и обработки данных.”
- Identity and structural links: PASS; `EU-ANALYTICAL_CHEMISTRY_BASICS-B` points to the intended Claim and Source, with role `supports`.
- NIST's tutorial index lists sample preparation/processing, calibration, method validation, and quality-management materials. The calibration material states that model choice/details matter for accurate results; sample-processing material explains preparation affects method sensitivity and solvent environment; quality-management material addresses achieving and maintaining measurement accuracy.
- Together these are relevant to the synthesis, but the Source record only links the general tutorial index and the local Evidence Use does not identify the specific tutorials. “Not only the instrument” is a synthesis, not a direct quotation from the landing page.
- **Disposition:** plausible and broadly supported by the NIST material family; source fit PARTIAL until specific tutorials/pinpoints are recorded. Do not infer that instrument effects are unimportant.

## Cross-cutting result
All five inspected Claim → Evidence Use → Source chains are structurally coherent, and all five Claim filename IDs match their internal IDs. Structural coherence does not establish evidence sufficiency.

- Algebra A–C: the claims are directly supported by OpenStax sections 1.1 and 3.1, but local Source URLs and Evidence Use descriptions omit precise section locators.
- Analytical Chemistry A–B: NIST is a relevant authoritative source family, but the landing page is not sufficiently specific for a final claim-level evidence score; identify and link the particular tutorials/passages supporting each clause.
- No D/E/B scores assigned. No Claim, Evidence Use, Source, or Relation records modified. Batch 41 scoring gate remains closed pending the prior-score/alias reconciliation and evidence-ledger requirements.

## Public source passages checked
- OpenStax, College Algebra 2e, 1.1 Real Numbers: Algebra Essentials: https://openstax.org/books/college-algebra-2e/pages/1-1-real-numbers-algebra-essentials
- OpenStax, College Algebra 2e, 3.1 Functions and Function Notation: https://openstax.org/books/college-algebra-2e/pages/3-1-functions-and-function-notation
- NIST, Tutorials in Analytical Chemistry: https://www.nist.gov/programs-projects/tutorials-analytical-chemistry
- NIST, Sample Concentration and Processing: https://www.nist.gov/video/sample-concentration-and-processing
- NIST, Quality Management Systems in Analytical Chemistry: https://www.nist.gov/video/quality-management-systems-analytical-chemistry
- NIST, Calibration: https://www.nist.gov/publications/calibration
