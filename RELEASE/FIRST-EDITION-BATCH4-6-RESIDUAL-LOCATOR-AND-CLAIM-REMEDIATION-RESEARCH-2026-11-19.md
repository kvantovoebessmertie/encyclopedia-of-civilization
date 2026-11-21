# First Edition — Batch 4–6 Residual Evidence Locator and Claim Remediation Research

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `247232ba9c4a976735df471a1f2547b41c2b20a3`  
Status: **18/18 CLAIMS REVIEWED ACROSS SIX RESIDUAL SLICES; DIRECT LOCATOR CANDIDATES FOUND FOR 12 SUBSTANTIVE CLAIMS; SIX PLACEHOLDER CLAIMS REQUIRE REPLACEMENT; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and exclusions

Batches 4–6 previously verified exact Claim→Evidence Use→Source graph edges. This follow-up addresses only residual slices not already covered by existing bounded authorizations or source-remediation dossiers.

Included:
- Batch 4: accounting-basics — 3 Claims, 3 EUs without pinpoints.
- Batch 5: calculus-basics — 3 Claims, 3 EUs without pinpoints; climate-science-basics — 3 placeholder Claims; computer-networks-basics — 3 placeholder Claims.
- Batch 6: democratic-institutions-basics — 3 Claims without pinpoints; demography-basics — 3 Claims without pinpoints.

Excluded to avoid repeating or exceeding existing work:
- Administrative law and comparative law: covered by the legal/trade/institutional bounded authorization.
- Archival science: covered by the R9 archival-science bounded authorization and addendum.
- Artificial intelligence and computer-science algorithms: covered by the engineering/computing bounded authorization.
- Biochemistry and chemical reactions: covered by the chemistry bounded authorization.
- Civil society and comparative civilizations: covered by the remaining R7 source-specific bounded authorization.
- No changes to any slice already authorized under those separate scopes.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation was edited by this report. No record version, publication/completion status, allowlist or INCLUDE/HOLD/EXCLUDE decision changed. All six residual slices remain HOLD.

## 2. Aggregate findings

| Slice | Claims / EUs | Current state | Research outcome |
|---|---:|---|---|
| accounting-basics | 3 / 3 | 0/3 EU pinpoints | IFRS source is relevant, but Claim A and C need narrower alignment; exact framework chapters identified |
| calculus-basics | 3 / 3 | 0/3 EU pinpoints | Direct OpenStax sections identified for limits, derivatives and definite integrals |
| climate-science-basics | 3 / 3 | 3 editorial placeholders | NASA evidence/causes/effects sources support three substantive replacement Claims |
| computer-networks-basics | 3 / 3 | 3 editorial placeholders | NIST glossary and RFC 1122 support three bounded replacement Claims |
| democratic-institutions-basics | 3 / 3 | 0/3 EU pinpoints | International IDEA Global State of Democracy framework provides direct conceptual and measurement locators |
| demography-basics | 3 / 3 | 0/3 EU pinpoints | UN World Population Prospects 2024 summary and methodology provide direct locators for all three Claims |

**Total:** 18 Claims / 18 EUs reviewed; 12 existing substantive Claims have direct locator candidates; six placeholder Claims (climate science and computer networks) require substantive replacement rather than mere locator insertion. No candidate is promoted.

## 3. Batch 4 — Accounting Basics

Current canonical records: `CLM-ACCOUNTING_BASICS-A/B/C@1`, `EU-ACCOUNTING_BASICS-A/B/C@1`, `SRC-ACCOUNTING_BASICS@1`.

The current Source identity is a generic sentence about accounting rather than a bibliographic identity. The URI points to the official IFRS Conceptual Framework page. The source is relevant to financial reporting, but the current Claims are broader than the Framework in places.

| Claim / EU | Current proposition | Direct locator candidate | Fit assessment |
|---|---|---|---|
| A | Accounting records business transactions and financial position | IFRS Conceptual Framework, Chapter 1 “The Objective of General Purpose Financial Reporting”; Chapter 3 “Financial Statements and the Reporting Entity” | Partial. The Framework supports the objective and information content of general-purpose financial reporting, not all operational bookkeeping or transaction-recording processes |
| B | Financial statements present information in structured form for users | Chapter 1 “The Objective of General Purpose Financial Reporting”; Chapter 3 “Financial Statements and the Reporting Entity”; Chapter 7 “Presentation and Disclosure” | Direct for structured general-purpose financial statements and information for users |
| C | Accounting estimates and classifications depend on standards and conditions | Chapter 4 “The Elements of Financial Statements”; Chapter 5 “Recognition and Derecognition”; Chapter 6 “Measurement” | Partial. The Framework supports definitions, recognition and measurement bases; it does not by itself establish every accounting-estimate rule |

Official source: https://www.ifrs.org/issued-standards/list-of-standards/conceptual-framework/

**Recommended Claim A narrowing, if approved:**

> Финансовая отчётность общего назначения предоставляет пользователям информацию об экономических ресурсах организации, требованиях к организации и изменениях этих ресурсов и требований.

**Recommended Claim C narrowing, if approved:**

> Признание и классификация элементов финансовой отчётности опираются на определения активов, обязательств, капитала, доходов и расходов, а также на критерии признания и выбранную основу оценки.

Source identity should be versioned to the exact title *Conceptual Framework for Financial Reporting* (2018 revised; IASB). The three EUs can then be versioned with claim-specific chapter locators and explicit limits. Do not present the Framework as a complete operational bookkeeping manual or as a substitute for individual IFRS Standards.

**Rights:** IFRS publications are copyright-controlled. Public availability is not permission to reproduce or adapt the text. Use factual paraphrase and attribution only unless the project obtains the required permission/licence.

## 4. Batch 5 — Calculus Basics

Current canonical records: `CLM-CALCULUS_BASICS-A/B/C@1`, `EU-CALCULUS_BASICS-A/B/C@1`, `SRC-CALCULUS_BASICS@1`.

The Source URI already points to the OpenStax *Calculus Volume 1* book page, but its identity is generic. Correct the Source identity to the exact title/edition and pin each EU to its section.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | A limit describes the behavior of a function as its argument approaches a specified value | §2.2 “The Limit of a Function”, “Intuitive Definition of a Limit” and formal definition |
| B | A derivative characterizes instantaneous rate of change when the derivative exists | §3.2 “The Derivative as a Function”, derivative as the limit of secant slopes / instantaneous rate of change |
| C | A definite integral describes accumulation under appropriate conditions | §5.2 “The Definite Integral”, definition as a limit of Riemann sums; §5.3 “The Fundamental Theorem of Calculus” for the connection to antiderivatives |

Official sources:
- §2.2: https://openstax.org/books/calculus-volume-1/pages/2-2-the-limit-of-a-function
- §3.2: https://openstax.org/books/calculus-volume-1/pages/3-2-the-derivative-as-a-function
- §5.2: https://openstax.org/books/calculus-volume-1/pages/5-2-the-definite-integral
- §5.3: https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus
- Book identity: https://openstax.org/details/books/calculus-volume-1

Claim C should retain the phrase “under appropriate conditions”: the definite integral exists only when the defining limit exists / the function is integrable on the interval. Distinguish definite integral (a number) from indefinite integral (a family of antiderivatives).

**Rights:** verify the exact current edition's OpenStax preface and licence terms before reuse. Do not infer commercial reuse or AI-ingestion permission from the book's public access.

## 5. Batch 5 — Climate Science Basics: three placeholder Claims

Current canonical records: `CLM-CLIMATE_SCIENCE_BASICS-A/B/C@1`, `EU-CLIMATE_SCIENCE_BASICS-A/B/C@1`, `SRC-CLIMATE_SCIENCE_BASICS@1`.

The current three Claims are not climate-science propositions:
- A says the slice introduces basic concepts.
- B says interpretation depends on source/context/boundaries.
- C says basic knowledge does not replace specialist verification.

These are editorial scaffolding and should not remain published as factual Claims. NASA's “Climate Change: Evidence” page is relevant but cannot make those generic statements into substantive subject-matter claims.

Proposed replacement Claims for owner/editor review:

| Claim | Proposed substantive statement | Direct source/locator |
|---|---|---|
| A | Различные линии наблюдений — измерения температуры, спутниковые данные и природные архивы — показывают современное изменение климата Земли | NASA “Evidence”, “Takeaways” and passages on temperature rise, ice sheets, ice cores, rocks, tree rings and satellite/instrument observations |
| B | Современная тенденция глобального потепления с середины XIX века обусловлена преимущественно деятельностью человека и ростом концентрации парниковых газов | NASA “Evidence” → current warming trend; NASA “Causes” → greenhouse gases and evidence excluding solar variability as the principal explanation |
| C | Среди наблюдаемых последствий изменения климата — потеря морского льда, ускорение повышения уровня моря и более продолжительные и интенсивные волны жары | NASA “Effects”, opening paragraphs and observed-effects list |

Sources:
- NASA “Evidence”: https://science.nasa.gov/climate-change/evidence/
- NASA “Causes”: https://science.nasa.gov/climate-change/causes/
- NASA “Effects”: https://science.nasa.gov/climate-change/effects/

Recommended source graph:
- Keep the existing NASA Evidence Source for Claim A and the directly supported part of Claim B.
- Correct its identity to the exact NASA Science page title.
- Add a distinct Source/Evidence Use chain for the Causes page if Claim B uses that independent passage.
- Add a distinct Source/Evidence Use chain for the Effects page for Claim C.
- New canonical IDs must be assigned through the canonical ID process; none are invented here.

Do not confuse attribution of recent warming with attribution of every individual weather event. NASA's Evidence page distinguishes long-term climate trends from short-term weather. All three replacement statements require subject-matter/editorial approval before canonical edits.

## 6. Batch 5 — Computer Networks Basics: three placeholder Claims

Current canonical records: `CLM-COMPUTER_NETWORKS_BASICS-A/B/C@1`, `EU-COMPUTER_NETWORKS_BASICS-A/B/C@1`, `SRC-COMPUTER_NETWORKS_BASICS@1`.

The three current Claims are generic placeholders (topic introduction, context caveat, and specialist-verification caveat). The current NIST CSRC glossary entry for “network” is relevant to Claim A but cannot support the other two placeholders as currently written.

Proposed replacement Claims for owner/editor review:

| Claim | Proposed substantive statement | Direct source/locator |
|---|---|---|
| A | Компьютерная сеть представляет собой систему взаимосвязанных компонентов, таких как маршрутизаторы, узлы и линии связи, которые обеспечивают обмен данными | NIST CSRC Glossary, entry “network”; use the definition and identify its underlying NIST source document |
| B | Сетевой протокол задаёт правила и форматы, по которым взаимодействующие системы организуют обмен сообщениями | NIST CSRC Glossary, entry “protocol”; use the definition from CNSSI 4009-2022 / IETF RFC 4949 or the NIST SP 800-175B definition |
| C | Архитектура Интернета использует уровни канала, Internet/IP и транспорта, а приложения используют верхний прикладной уровень | IETF RFC 1122, §1.1.3 “Protocol Layers” and §3 “Internet Layer Protocols”; RFC 1123 for application/support protocols if the full four-layer statement is retained |

Sources:
- NIST “network”: https://csrc.nist.gov/glossary/term/network
- NIST “protocol”: https://csrc.nist.gov/glossary/term/protocol
- IETF RFC 1122: https://www.rfc-editor.org/rfc/rfc1122.html
- IETF RFC 1123: https://www.rfc-editor.org/rfc/rfc1123.html

The NIST glossary page explicitly warns that a term definition should be understood in the context of its identified source document. Do not detach a definition from its underlying NIST/RFC source. RFC 1122 is a historical foundational host-requirements standard and has been updated by later RFCs; use it to explain layered architecture, not as a complete statement of all current Internet protocol practice.

Recommended source graph: update the current Source identity from one NIST term page to “NIST CSRC Glossary” with exact term locators for A/B; add a separate RFC Source/Evidence Use chain for C. Do not invent IDs. All three Claim replacements require approval.

## 7. Batch 6 — Democratic Institutions Basics

Current canonical records: `CLM-DEMOCRATIC_INSTITUTIONS_BASICS-A/B/C@1`, `EU-DEMOCRATIC_INSTITUTIONS_BASICS-A/B/C@1`, `SRC-DEMOCRATIC_INSTITUTIONS_BASICS@1`.

The current Source is the broad International IDEA “Democracy” portal. The strongest direct source is International IDEA's *Global State of Democracy Indices Methodology*, Version 10 (2026), which defines the conceptual framework and its indicators.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Democratic institutions include rules and bodies through which representation, participation and public decisions are organized | Version 10, §2 “The Global State of Democracy: Conceptual Framework”; two principles (popular control and political equality), seven mediating values, and four categories of democratic institutions/actors/processes |
| B | Elections are an important mechanism of political representation, but democracy is not reducible to elections alone | Version 10, Annex A; “Representation” contains “Credible Elections” as one subattribute, while the wider framework separately measures Rights, Rule of Law and Participation |
| C | Democratic-institution quality depends on rules, practices, accountability and country context | Version 10, §2 and Annex A; accountability, transparency, responsiveness, representation, rights, rule of law and participation are explicitly operationalized |

Official source:
- International IDEA, *The Global State of Democracy Indices Methodology, Version 10 (2026)*:
  https://www.idea.int/publications/catalogue/html/global-state-democracy-indices-methodology-version-10-2026

Recommended Claim C narrowing, if approved:

> Оценка демократических институтов учитывает не только выборы, но и представительство, права, верховенство права, участие граждан и подотчётность органов власти.

This is a description of the IDEA assessment framework, not a universal causal theory of democratic quality. Correct the Source identity from the generic portal to the exact methodology title/version/date; then version dependent Claims/EUs only as required by provenance and current references. Rights and reuse terms for the methodology publication remain to be checked.

## 8. Batch 6 — Demography Basics

Current canonical records: `CLM-DEMOGRAPHY_BASICS-A/B/C@1`, `EU-DEMOGRAPHY_BASICS-A/B/C@1`, `SRC-DEMOGRAPHY_BASICS@1`.

The existing Source identifies UN Population Division, *World Population Prospects 2024: Summary of Results*. It is suitable for Claims A/B and should be pinned to the exact PDF page/figure. Claim C requires the separate WPP 2024 methodology publication.

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Population change is shaped by fertility, mortality and international migration | WPP 2024 *Summary of Results*, Chapter 1, p. 9, paragraph accompanying Figure 1.5: population grows/declines as a function of the balance of fertility, mortality and international migration |
| B | Past demographic patterns affect current age structure and population momentum | Same p. 9, paragraph accompanying Figure 1.5: age structure resulting from past trends can be a major driver of population change; the report names this “population momentum” |
| C | Demographic estimates and projections are model-based and depend on data and assumptions | WPP 2024 Methodology, Introduction: new demographic information is incorporated and future paths of fertility, mortality and international migration are formulated as detailed assumptions; estimates/projections use the cohort-component method |

Sources:
- WPP 2024 Summary of Results PDF: https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/wpp2024_summary_of_results_final_web.pdf
- WPP 2024 Methodology PDF: https://population.un.org/wpp/assets/Files/WPP2024_Methodology.pdf
- UN Population Division WPP 2024 landing page: https://www.un.org/development/desa/pd/content/world-population-prospects-2024-summary-results-0

Claim A/B are directly supported by the summary report's p. 9 and Figure 1.5. Claim C is directly supported by the methodology introduction and the description of the cohort-component method. Create a distinct Source/Evidence Use chain for the methodology PDF if the current single-Source schema cannot accurately represent both publications. Do not invent a canonical ID.

Keep the international-migration boundary explicit: migration changes national and regional population totals, but global net migration is zero. The report itself notes this in footnote 8. Do not imply that international migration changes total world population.

## 9. Rights, scope and editorial controls

- IFRS Conceptual Framework: copyright-controlled; no permission to reproduce/adapt is inferred from public access.
- OpenStax Calculus Volume 1: verify exact current edition, licence and AI-ingestion terms in the book preface; do not infer commercial reuse.
- NASA Climate Change pages: factual source material is useful, but do not reproduce NASA images/graphics or assume every embedded item has the same rights status.
- NIST glossary: every definition cites an underlying source document; retain the underlying source identity/edition and do not detach a definition from its context.
- IETF RFCs: public standards documents; preserve RFC identity, date and current-update boundary.
- International IDEA methodology and UN WPP publications: complete source-specific attribution and reuse review; no blanket rights clearance is asserted.
- Climate-science and computer-network placeholder Claims require replacement by falsifiable subject-matter Claims, not merely a version bump or locator addition.
- All six slices remain HOLD pending independent subject/editorial review, rights, Human View and high-consequence checks.

## 10. Implementation order after owner authorization

1. Locator-only: Calculus A–C; Demography A/B; Democratic Institutions A/B/C (after Source identity correction); Accounting B.
2. Source/wording alignment: Accounting A/C; Demography C (methodology Source); Computer Networks A/B/C (NIST glossary + RFC source graph).
3. Substantive replacement: Climate Science A–C and Computer Networks A–C. Require subject-matter approval before canonical edits.
4. Re-fetch all exact records at one frozen HEAD; version Claims only when wording changes or provenance must align to a newly versioned Source; update dependent EUs and target references.
5. Preserve HOLD. Run affected-slice tests, graph preflight and full release gates only after the authorized changes are applied on a final immutable HEAD.

## 11. Explicit non-actions

This report does not:
- authorize or perform any canonical JSON changes;
- change Claim statements, versions, publication_status or completion_status;
- create new canonical Source/Evidence Use IDs;
- alter first-edition candidate keys, allowlists or INCLUDE/HOLD/EXCLUDE decisions;
- modify Relations, validators, storage, recovery or release-gate semantics;
- merge PR #22, deploy or approve publication.

**Owner decision required:** approve, reject or amend the six residual-slice scopes; approve the six substantive replacement Claims in Climate Science and Computer Networks separately from locator-only work.
