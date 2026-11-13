# M13 duplicate-source adjudication: FAO Agrifood Systems, UNESCO AI Ethics, and ACRL Information Literacy

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Reviewed baseline: `785122e02177f777c9b7f3e49762aa69713019f6`  
Scope: three academic/knowledge-framework shared-URI groups. Source, Evidence Use and Claim records were inspected directly; official source pages were checked separately.

## 1. Executive findings

| Shared URI group | Source IDs | Linked Claims | Adjudication |
|---|---:|---:|---|
| FAO Agrifood Systems | 2 | 6 | One current FAO topic page. It directly defines agrifood systems and enumerates the value chain; broader systems-analysis claims need more precise sources. |
| UNESCO Recommendation on AI Ethics | 2 | 6 | One UNESCO topic page summarizing one Recommendation. It directly supports most AI/data ethics Claims; one “not reducible to one metric” Claim is only partially explicit. |
| ACRL Framework for Information Literacy | 2 | 0 in the inspected critical-thinking and information-literacy slices | One ACRL Framework page, revised September 2026. The duplicate Source records are not linked by the Evidence Use records in those two slices; the current Claims point to OpenStax and UNESCO Media and Information Literacy instead. |

**Totals: 6 Source records and 12 Claims linked to the FAO and UNESCO duplicate groups, plus 2 ACRL Source records with no linked Evidence Use found in the two relevant slices inspected.** Same-URL Source IDs do not create independent corroboration.

No canonical JSON, Claim wording, Source identity, Evidence Use locator, Relation, historical assessment or D/E/B score was changed. This report is an adjudication record only.

## 2. FAO Agrifood Systems — two IDs, one current topic page

### Source identity

Both records point to `https://www.fao.org/food-systems/en`:

- `SRC-AGRIFOOD_SYSTEMS_BASICS`
- `SRC-FOOD_SYSTEMS`

Both identify “FAO — Agrifood Systems”. The current page is retrievable and defines agrifood systems as the people, activities, investments and choices involved in producing and delivering food and agricultural goods. It enumerates the chain from growing and harvesting through processing, packaging, transport, distribution, trade, purchase, preparation, consumption and disposal. It also includes non-food agricultural products such as forestry, biomass and fibres.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-AGRIFOOD_SYSTEMS_BASICS-A` — agrifood systems include people, activities, investments and decisions involved in producing and delivering food/agricultural goods | Direct. The page’s opening definition uses those elements almost verbatim. |
| `CLM-AGRIFOOD_SYSTEMS_BASICS-B` — the chain can include growing, harvesting, processing, packaging, transport, distribution, trade, preparation, consumption and disposal | Direct. The page explicitly lists these stages. |
| `CLM-AGRIFOOD_SYSTEMS_BASICS-C` — systems analysis must account for production, economic, social and environmental relationships together | Partial. The page defines a broad chain and names people, investments, choices and non-food agricultural outputs, but the complete economic/social/environmental analytical framework is not stated explicitly on the landing page. The 2026 FAO systems-approach report and policy-methods handbook are better candidates for a specific analysis-method Claim. |
| `CLM-FOOD_SYSTEMS-A` — food systems include production, processing, distribution, consumption and disposal | Direct. These stages are explicitly listed on the FAO page. |
| `CLM-FOOD_SYSTEMS-B` — food systems include people, activities, investments and decisions linked to production and delivery | Direct. The page’s definition directly supports the proposition. |
| `CLM-FOOD_SYSTEMS-C` — analysis requires links among natural resources, technology, trade, food access and other chain elements | Partial. The page supports the chain and broader agrifood scope, but does not fully enumerate the stated resource, technology and access dimensions. Add a specific FAO systems-analysis publication or narrow the Claim. |

### Disposition

- Two Source IDs, one FAO topic-page identity; no independent corroboration is created by the duplicate IDs.
- Add a separate Source record for a specific FAO publication if it is used to support systems-analysis methods. The current page links to distinct 2026 publications, including _Transforming Food and Agriculture through a Systems Approach_ and _Tools and methods to support the design and implementation of policies for agrifood systems transformation_. These are distinct publications, not aliases for the topic page.
- The six Evidence Use records contain generic descriptions and no exact section locators.

## 3. UNESCO Recommendation on the Ethics of Artificial Intelligence — two IDs, one topic page

### Source identity

Both records point to `https://www.unesco.org/en/artificial-intelligence/recommendation-ethics`:

- `SRC-AI_ETHICS_BASICS`
- `SRC-DATA_ETHICS_BASICS`

Both identify the **UNESCO Recommendation on the Ethics of Artificial Intelligence**. The current UNESCO page is retrievable and summarizes the Recommendation adopted by UNESCO Member States in November 2021. It explicitly identifies human rights and human dignity, transparency, fairness, environmental sustainability and human oversight, and links the full Recommendation. The page also addresses risk assessment, privacy/data protection, accountability, auditability, explainability and lifecycle impacts.

The full Recommendation is a separate document with its own publication identity and URI. It is the underlying normative text summarized by the landing page; it is not an independent corroborating source from the same Recommendation.

### Claim/Evidence Use adjudication

| Claim | Source fit |
|---|---|
| `CLM-AI_ETHICS_BASICS-A` — the Recommendation frames AI ethics around dignity, human rights and prevention of harm | Direct. The page states the centrality of human rights/dignity and the “do no harm” principle, including risk assessment. |
| `CLM-AI_ETHICS_BASICS-B` — transparency, fairness, sustainability and human oversight are principles for responsible AI governance | Direct. These principles are explicitly named in the page’s summary and core-principles list. |
| `CLM-AI_ETHICS_BASICS-C` — ethical assessment should consider context, risks and impacts across the AI lifecycle, not only technical performance | Direct. The page describes risks arising through development, design, deployment and use; it calls for risk assessment, lifecycle privacy protection, impact assessment and context-appropriate transparency. |
| `CLM-DATA_ETHICS_BASICS-A` — privacy and data protection matter throughout data-intensive AI lifecycles | Direct. The page explicitly says privacy must be protected and promoted throughout the AI lifecycle and calls for data-protection frameworks. |
| `CLM-DATA_ETHICS_BASICS-B` — ethical frameworks emphasize fairness, accountability, transparency and human oversight | Direct. These are separately enumerated as core principles. |
| `CLM-DATA_ETHICS_BASICS-C` — ethical data assessment is context-dependent and cannot be reduced to one technical metric | Partial. The page explicitly makes transparency/explainability context-dependent and recognizes tensions with privacy, safety and security; it also uses multiple values and policy principles. It does not literally state that assessment cannot be reduced to one metric. Either narrow the Claim to context-dependent multi-principle assessment or add a source that explicitly supports the broader formulation. |

### Disposition

- Two Source IDs, one UNESCO Recommendation/topic-page identity; no independent corroboration is created by the duplicate IDs.
- All six Claims have relevant support, but Claim C in the data-ethics slice needs wording or evidence refinement.
- Add the full Recommendation as a distinct Source record only if the actual text is used for section-level locators. Do not count the page summary and the underlying Recommendation as independent corroboration of each other.
- All six Evidence Use records currently lack section/paragraph locators.

## 4. ACRL Framework for Information Literacy — two IDs, one framework page, no linked EU in the inspected slices

### Source identity

Both records point to `https://www.ala.org/acrl/standards/ilframework`:

- `SRC-ACRL-CRITICAL-INQUIRY-2026`
- `SRC-ACRL-INFORMATION-LITERACY-2026`

Both identify the **Association of College and Research Libraries — Framework for Information Literacy for Higher Education**. The current ACRL page is retrievable. It records a revision approved September 2, 2026 and presents the Framework’s definition, introduction and six frames, including “Authority Is Constructed and Contextual”, “Research as Inquiry”, and “Searching as Strategic Exploration”.

### Linkage finding

The ACRL Source records are present in the repository, but the six Evidence Use records inspected in the corresponding slices do **not** reference either ACRL Source ID:

- In `critical-thinking-basics`, the three current EUs reference `SRC-CRITICAL_THINKING_BASICS`, which is **OpenStax — College Success, 7.4 Critical Thinking**.
- In `information-literacy-basics`, the three current EUs reference `SRC-INFORMATION_LITERACY_BASICS`, which is **UNESCO — Media and Information Literacy**.

Therefore, the ACRL duplicate pair currently contributes no linked evidence to those six Claims in the inspected slices. Do not report ACRL as corroborating those Claims unless an authorized Evidence Use link is actually created. The ACRL framework may be a useful additional source for higher-education information literacy and contextual source evaluation, but its scope is not a universal professional standard for all forms of critical thinking.

### Disposition

- Two ACRL Source IDs, one Framework page; no independent corroboration between them.
- No Evidence Use link to either ACRL ID was found in the corresponding critical-thinking and information-literacy slices.
- Keep the currently linked OpenStax and UNESCO sources distinct. If ACRL is intended as additional support, create a bounded, explicit Evidence Use link with the relevant Frame and higher-education scope.
- Do not delete the unlinked Source records without a separate orphan-source/record-integrity review.

## 5. Consolidated audit decision and next actions

1. Count one source identity per shared URI: FAO Agrifood Systems = 1; UNESCO AI Ethics = 1; ACRL Information Literacy Framework = 1.
2. Keep the 12 linked FAO/UNESCO Claims in the audit denominator. Record the ACRL pair as unlinked in the two slices inspected, not as evidence for those Claims.
3. Add exact page/section locators to the relevant Evidence Use records only through authorized versioned corrections.
4. For FAO systems-analysis Claims, inspect the specific 2026 FAO systems-approach publications; do not assume the landing page supports the entire economic/social/environmental analysis framework.
5. For UNESCO, distinguish the topic-page summary from the full Recommendation. They are related representations of one normative work, not independent sources.
6. For ACRL, resolve intended linkage and orphan status separately; do not silently attach ACRL to existing Claims or remove the records.
7. After any authorized canonical correction, run Reference Tests, Release Conformance Gate and Offline Edition on the exact final SHA.

## 6. Change boundary

- Source records changed: 0.
- Evidence Use records changed: 0.
- Claim records changed: 0.
- Historical D/E/B assessments changed: 0.
- Canonical locators added: 0.
- Independent specialist review completed: 0.
- PR #21 remains Draft/unmerged; `main` remains unchanged.

This report records inspected source identity, linkage and source fit. It is not a release approval or authorization to edit canonical records.
