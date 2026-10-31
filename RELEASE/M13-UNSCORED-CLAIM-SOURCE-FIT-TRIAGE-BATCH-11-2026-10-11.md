# M13 Unscored Claim Source-Fit Triage — Batch 11

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **source-fit triage only; no D/E/B scores assigned**

## Scope and controls

- Frozen corpus denominator: **1,494 Claims**.
- Inventory rows reviewed: **481–510 inclusive (30 Claims)**.
- Current Claims without a scored ledger row remain **1,242**; this batch does not change the score ledger.
- This pass inspects Claim wording, provenance/source identity, and representative paired Evidence Use records. It is not proof that every underlying source passage supports every proposition; exact passage/page/section verification remains open.
- No canonical Claim, Evidence Use, Source, or Relation JSON was changed.

## Findings by Claim

| Inventory row(s) | Claim ID(s) | Source-fit / classification finding | Disposition |
|---|---|---|---|
| 481 | `CLM-EPIDEMIOLOGY_BASICS-C` | Statement is a general caution about the limits of a slice and the need for specialist assessment, not an epidemiology-domain proposition. Its paired EU describes no exact passage. | Adjudicate with the cross-slice editorial/methodology-template family; do not score as a domain fact until classified. |
| 482 | `CLM-EPIDEMIOLOGY_BASICS-D` | WHO-style definition of epidemiology is plausible as a domain fact, but the Claim provenance points to `SRC-WHO-EPIDEMIOLOGY-2024`; the expected local EU filename was not found in the inspected slice listing. The CDC source record used by A/B/C is a different source. | Globally resolve the exact EU and Source IDs and pinpoint the official WHO definition before scoring. |
| 483–485 | `CLM-EPIGENETICS_BASICS-A/B/C` | All three Claims have separator-only filename/internal `record_id` variants (hyphens in filenames, underscores in IDs). Their EUs use the same generic description, “Источник используется в пределах заявленного материала,” with no passage, section, or page. The Source identity/locator must be read as a specific work, not inferred from the generic EU wording. | Record aliases for comparison only; do not merge IDs. Replace generic EUs only through an authorized, passage-verified correction. |
| 486–488 | `CLM-EPISTEMOLOGY_BASICS-A/B/C` | Claims cover the scope of epistemology, the distinction between knowledge and justified belief, and criteria for evaluating knowledge claims. The current source reference is a single general epistemology source; exact arguments/definitions and counterexamples require pinpoint locators. | Verify each proposition against a specific entry section or other authoritative philosophical reference; distinguish textbook framing from universally settled facts. |
| 489–491 | `CLM-ERGONOMICS_BASICS-A/B/C` | Claims concern worker capability/limitations, physical risk factors, and workplace risk-control programmes. These are plausible occupational ergonomics propositions, but the current record-level provenance alone does not establish support for all three scopes. | Check the paired EU text and exact authoritative occupational-safety/ergonomics passages, particularly the broad “programmes” proposition. |
| 492–494 | `CLM-ETHICS_BASICS-A/B/C` | A describes the purpose of the ethics slice; B advises readers to consider source/context/limitations; C says general information does not replace specialist review. These are editorial/methodological statements rather than ethics-domain facts and repeat the known cross-slice template family. | Adjudicate as a family against the shared methodology/template rule; do not count repeated guidance as three independent ethics facts. |
| 495–497 | `CLM-ETHNOBOTANY_BASICS-A/B/C` | Claims address the field’s definition, local cultivation systems/crop diversity and cultural practices, and land-use/production effects on plant diversity. The cited Kew source is a specific ethnobotanical case study about enset in Ethiopia, which may be relevant to a case but is not automatically sufficient for the broad field definition and general causal wording. | Separate field definition from case-specific and general ecological propositions; add fit-for-purpose sources and exact locators where needed. |
| 498–500 | `CLM-EVOLUTION_BASICS-A/B/C` | Claims cover evolution across generations, natural selection changing inherited-trait frequencies, and heritable variation as a condition of selection. The OpenStax Biology evolution chapter is plausibly relevant; current EU descriptions are generic and do not identify exact passages. | Pinpoint the relevant section(s); ensure B/C are not presented as a complete list of all conditions or mechanisms. |
| 501 | `CLM-HEAT-EXHAUSTION-SIGNS` | High-consequence warning lists symptoms and escalation advice. CDC source is official and relevant, and the EU names several symptoms, but the linked source is a broad landing page. Symptom groupings and when to escalate need precise matching. | Priority source-fit review: exact CDC symptom page/section and wording; keep escalation language consistent with authoritative guidance. |
| 502 | `CLM-HEAT-HEATSTROKE-EMERGENCY` | High-consequence emergency advice combines recognition, immediate emergency response, and rapid cooling. NWS is an official source and broadly relevant, but the EU’s short description does not demonstrate every operational detail in the Claim. | Priority source-fit review against the exact NWS/CDC emergency guidance; verify no delay in emergency help is implied. |
| 503 | `CLM-HEAT-STAY-COOL-HYDRATED` | General hot-weather recommendation to stay cool and drink enough fluid; CDC source is relevant but the source URI is a broad page and “enough fluid” can depend on context and individual constraints. | Pinpoint the CDC prevention passage; preserve appropriate scope and avoid overgeneralizing hydration advice. |
| 504–506 | `CLM-FINANCE_BASICS-A/B/C` | Claims concern time-related cash flows, uncertainty of future outcomes, and valuation conditional on instrument/model. The Source identity is a descriptive sentence rather than a bibliographic title, while its URI is the broad Investor.gov investing-basics page. EU-A uses generic language with no pinpoint. | Confirm source identity/title, select claim-matched financial references, and add exact passages. Do not treat a broad investing landing page as evidence for every finance concept. |
| 507–509 | `CLM-FINANCIAL_LITERACY_BASICS-A/B/C` | OECD Financial Education is a credible topical source, but its broad landing page and title-level EU do not independently establish the definitions and product-evaluation propositions in A/B/C. B/C also approach individualized financial decision-making. | Pinpoint OECD passages or add relevant authoritative consumer-finance sources; retain context/individual-circumstance caveats and avoid personalized recommendations. |
| 510 | `CLM-FINANCIAL_MARKETS_BASICS-A` | IMF Financial Markets is a credible topical source, but the landing page and title-level EU do not yet pinpoint the claim that markets facilitate asset exchange and capital allocation. | Identify a precise IMF section or a suitable textbook/official reference and verify the full proposition. |

## Cross-cutting findings

1. **Editorial-template classification:** Epidemiology C and Ethics A/B/C appear to be instances of the known cross-slice purpose/context/specialist-checking family. They require family-level adjudication, not isolated scoring.
2. **Evidence specificity:** Several EUs describe a source generically or name only a publisher/topic. A valid `source_ref` and a relevant domain do not prove that the exact passage supports the entire Claim.
3. **Source identity quality:** Finance Basics uses a descriptive sentence as `source_identity` and a broad Investor.gov URL. This is a metadata-quality issue to verify before any content correction.
4. **Safety priority:** The three extreme-heat Claims are high-consequence guidance. Their official sources are directionally relevant, but precise wording and escalation details must be verified against the actual guidance.
5. **ID reconciliation:** Epigenetics A/B/C contain separator-only filename/internal-ID variants. Preserve exact identifiers; comparison normalization is not authorization to rename or merge records.

## Batch outcome

- Claims triaged: **30**.
- D/E/B scores assigned: **0**.
- Canonical JSON edits: **0**.
- Claims without scored rows: **1,242 (unchanged)**.
- M13 status: **OPEN**. Exact-passage verification, family-level adjudication, scoring, independent review, and exact-head CI remain required.
