# M13 Unscored Claim Source-Fit Triage — Batch 01

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **30-Claim diagnostic pass; no D/E/B scores assigned and no content JSON changed**

## Scope

Reviewed 30 Claims selected in inventory order from the 1,242 Claims not yet represented by a scored row in the M13 inventory-to-ledger join. The batch includes one building-science Claim, climate-adaptation/climate/climate-science Claims, clinical-trial and cloud-computing Claims, combinatorics, communication, comparative-civilizations, comparative-law and competition-policy Claims.

For each Claim, the Claim statement, linked Evidence Use (EU), and Source record were inspected. The pass distinguishes structural linkage from actual support. The listed sources were checked at their public pages where accessible; the National Academies chapter and Wolfram MathWorld pages could not be fully retrieved by the web checker in this pass, so no pinpoint support is asserted for them.

## Claim-level dispositions

| # | Claim ID | Source | Finding and next action |
|---:|---|---|---|
| 1 | `CLM-M4-BUILDING-MOISTURE-A` | U.S. DOE Building Science Education — Moisture Flow | The source topic directly matches moisture movement in building enclosures and the Claim links to it with `supports`. The EU says only “Additional foundational building-science claim supported…” and does not map water/capillary/air/vapour mechanisms to a passage. Keep source-fit provisional; add a claim-specific locator during authorized correction. Do not count the separate DOE EU for `CLM_BUILDING_SCIENCE_BASICS_B` as support for this Claim; it targets a different Claim. |
| 2 | `CLM-CLIMATE_ADAPTATION-A` | IPCC AR6 WGII | Hazard, exposure and vulnerability are relevant to climate risk framing, but the stored EU is generic and the Source points to the report landing page. Locate the exact risk-framework passage; no falsity finding. |
| 3 | `CLM-CLIMATE_ADAPTATION-B` | IPCC AR6 WGII | Context-specific adaptation is a plausible synthesis, but the EU does not identify the source passage. Pinpoint the relevant adaptation-context section or clarify that this is an editorial principle. |
| 4 | `CLM-CLIMATE_ADAPTATION-C` | IPCC AR6 WGII | Limits and residual risks are relevant to the report, but the current EU is boilerplate. Identify the specific limits/residual-risk material before treating source fit as closed. |
| 5 | `CLM-CLIMATE_BASICS-A` | NASA Climate Change | NASA material defines climate through long-term patterns and explains climate change. The broad stored locator may be relevant, but the EU is generic. Pinpoint the climate-definition passage and avoid conflating “climate” with “climate change.” |
| 6 | `CLM-CLIMATE_BASICS-B` | NASA Climate Change | NASA describes observations and models used to study climate change, which is relevant to the Claim. The EU is generic; add a specific locator for observations, measurements/models and long time scales. |
| 7 | `CLM-CLIMATE_BASICS-C` | NASA Climate Change | NASA explicitly distinguishes short-term weather from long-term climate. This is likely supportable from the source, but the EU does not identify that passage. Add the precise section/URL. |
| 8 | `CLM-CLIMATE_SCIENCE_BASICS-A` | NASA Climate Change: Evidence | **Type/placement mismatch candidate.** The statement says what this local slice introduces; an external climate-science page cannot establish that this corpus slice provides adequate concepts and relations. Reclassify as editorial/learning-design metadata or validate against an internal acceptance specification. |
| 9 | `CLM-CLIMATE_SCIENCE_BASICS-B` | NASA Climate Change: Evidence | **Type/placement mismatch candidate.** The statement is a general epistemic rule about source/context/applicability, not a climate-science fact established by the NASA page. Move to shared methodology/policy or cite a suitable epistemology source; review `claim_type: documented_fact`. |
| 10 | `CLM-CLIMATE_SCIENCE_BASICS-C` | NASA Climate Change: Evidence | **Type/placement mismatch candidate.** The specialist-checking rule is cross-cutting governance/methodology, not a domain fact demonstrated by the climate source. Reclassify or move to shared policy under an authorized plan. This Claim is also part of the 20-slice boilerplate family identified in the semantic-duplicate triage report. |
| 11 | `CLM_CLINICAL_TRIALS_BASICS_A` | WHO — Clinical trials | WHO directly describes clinical trials as research involving people that evaluates health-related interventions. The EU says only “Source supports the claim within the stated scope.” Add a direct section/locator and claim-specific description. |
| 12 | `CLM_CLINICAL_TRIALS_BASICS_B` | WHO — Clinical trials | WHO's overview discusses effects on health outcomes, phases and risks/adverse effects, so the Claim is broadly relevant. The EU remains generic; identify the exact material supporting benefits/risks/effects. |
| 13 | `CLM_CLINICAL_TRIALS_BASICS_C` | WHO — Clinical trials | WHO says trials are carefully designed and reviewed, but the Claim's full formulation about predefined methods to collect/analyze participant and outcome information is more specific. Add a protocol/methods source or narrow the proposition; do not infer full support from the overview alone. |
| 14 | `CLM-CLOUD_COMPUTING_BASICS-A` | NIST SP 800-145, *The NIST Definition of Cloud Computing* | NIST's abstract directly defines network access to a shared pool of configurable resources. The Claim is well aligned, but the EU is generic. Pinpoint the definition and preserve NIST's “on-demand network access” and “shared pool” terms. |
| 15 | `CLM-CLOUD_COMPUTING_BASICS-B` | NIST SP 800-145 | NIST directly describes resources being rapidly provisioned and released with minimal management effort/provider interaction. Strong source relevance; EU still lacks a pinpoint. Add the exact NIST definition locator during authorized correction. |
| 16 | `CLM-COMBINATORICS_BASICS-A` | Wolfram MathWorld — Combinatorics | The Claim about ordered arrangements is standard and plausibly within the source's scope, but the source page was not fully retrievable in this pass and the EU is boilerplate. Verify the exact permutation definition and add a locator. |
| 17 | `CLM-COMBINATORICS_BASICS-B` | Wolfram MathWorld — Combinatorics | The Claim about selection without regard to order is standard; the EU is generic and no pinpoint was verified. Locate a direct combinations definition. **Source metadata defect:** `source_identity` is a descriptive sentence (“Комбинаторика изучает способы подсчёта…”) rather than the actual source title/identity represented by the Wolfram URL. Correct only under authorized Source-metadata scope. |
| 18 | `CLM-COMBINATORICS_BASICS-C` | Wolfram MathWorld — Combinatorics | Sum/product counting rules are plausible combinatorics content, but a general topic page and boilerplate EU do not show the exact support. Verify the rule definitions and add a pinpoint. |
| 19 | `CLM-COMMUNICATION_BASICS-A` | National Academies, *Communicating Science Effectively*, ch. 4 | The source is relevant to audience and communication, but the EU is generic and the chapter was rate-limited during this check. Verify that it supports all listed factors (goal, content, format, audience and channel) and add a specific locator. |
| 20 | `CLM-COMMUNICATION_BASICS-B` | National Academies, *Communicating Science Effectively*, ch. 4 | The audience/context part is plausible, but the stronger boundary that not every interpretation is equivalent to the intended meaning needs direct support or should be identified as a methodological synthesis. EU is generic; source passage not verified in this pass. |
| 21 | `CLM-COMMUNICATION_BASICS-C` | National Academies, *Communicating Science Effectively*, ch. 4 | The audience/task-relative quality claim is plausible, but the “simplification does not guarantee correct understanding or preserve precision” clauses need pinpoint support. EU is generic; source passage not verified in this pass. |
| 22 | `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-A` | UNESCO Multimedia Archives — *History of Civilizations of Central Asia* | **Confirmed source identity/scope mismatch.** The stored Source identity says “Comparative civilizations — public reference,” but the URI resolves to a specific six-volume history of Central Asia, not a general comparative-civilization method. It does not directly establish the “no universal trajectory” proposition. Replace with a better-matched methodology source or narrow the Claim. |
| 23 | `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-B` | Same UNESCO Central Asia history page | The source may contain examples of contact/exchange within Central Asia, but it is too geographically specific to support the general cross-civilizational proposition as written without a relevant passage. The EU is boilerplate. Add a suitable comparative-history source or narrow scope. |
| 24 | `CLM-COMPARATIVE_CIVILIZATIONS_BASICS-C` | Same UNESCO Central Asia history page | The distinction between sequence and causality is a methodological rule, not directly established by a regional history landing page. Replace/narrow the source basis or place the rule in shared historical-methodology guidance. |
| 25 | `CLM-COMPARATIVE_LAW_BASICS-A` | Cornell Wex — Legal systems | Cornell describes legal systems as rules, procedures and institutions and explicitly notes jurisdictional variation. The source is relevant, but the EU is generic and the identity “Comparative law — public reference” is less specific than the linked page title. Add a locator and preserve jurisdictional limits. |
| 26 | `CLM-COMPARATIVE_LAW_BASICS-B` | Cornell Wex — Legal systems | The EU is comparatively specific and the page directly describes rules, procedures and institutions through which law is interpreted/applied. This is a plausible match; still add a pinpoint and avoid implying one universal legal-system structure. |
| 27 | `CLM-COMPARATIVE_LAW_BASICS-C` | Cornell Wex — Legal systems | Cornell discusses variation in judge roles, sources of law, standards of evidence and jurisdiction. This supports part of the list, but the claim's process-powers and period-specific clauses need direct evidence. The EU's jurisdiction caveat is useful; pin down the remaining support. |
| 28 | `CLM-COMPETITION_POLICY_BASICS-A` | OECD — Competition | OECD directly discusses competition policy, enforcement and anti-competitive conduct. The EU is generic; point to the relevant policy/enforcement passage. |
| 29 | `CLM-COMPETITION_POLICY_BASICS-B` | OECD — Competition | OECD discusses enforcement tools and competition authorities' work, broadly supporting the Claim. The EU is generic; cite the section on tools/market assessment rather than the landing page alone. |
| 30 | `CLM-COMPETITION_POLICY_BASICS-C` | OECD — Competition | The caution that a violation depends on facts, market and applicable law is prudent, but the general OECD overview does not itself establish a jurisdiction-specific legal test. Add a legal/analytical authority or explicitly treat this as a methodological boundary, with jurisdiction limits. |

## Cross-batch observations

- The reviewed 30 Claims have structurally plausible Claim → EU → Source ID links and `supports` roles; that is not proof of claim-specific evidence fit.
- Most of the 30 EUs are generic or near-generic. The two comparative-law EUs B/C are more specific but still need locators.
- Three climate-science Claims (A–C) are type/placement mismatch candidates and overlap with a wider templated family.
- One Source identity/scope mismatch is confirmed for comparative civilizations; a second Source identity quality defect is confirmed for combinatorics.
- No D/E/B scores were assigned in this pass. These Claims remain unscored and inside the fixed 1,494-Claim denominator.

## Public source checks used

- DOE moisture flow: https://bsesc.energy.gov/energy-basics/building-enclosure-building-science-intro-moisture-flow
- IPCC AR6 WGII: https://www.ipcc.ch/report/ar6/wg2/
- NASA climate overview: https://science.nasa.gov/climate-change/
- NASA climate-change definition/details surfaced in the current site: https://science.nasa.gov/climate-change/what-is-climate-change/
- WHO clinical trials: https://www.who.int/health-topics/clinical-trials
- NIST cloud definition: https://www.nist.gov/publications/nist-definition-cloud-computing
- Wolfram MathWorld combinatorics: https://mathworld.wolfram.com/Combinatorics.html
- National Academies communication report: https://nap.nationalacademies.org/read/23674/chapter/4
- UNESCO Central Asia history: https://www.unesco.org/archives/multimedia/document-1595
- Cornell Wex legal systems: https://www.law.cornell.edu/wex/legal_systems
- OECD competition: https://www.oecd.org/en/topics/competition.html

## Protected-state boundary

No Claim, Evidence Use, Source or Relation JSON was changed. No IDs were normalized in storage or rewritten. The findings are a diagnostic source-fit pass, not final D/E/B scoring or permission to modify content. PR #21 must remain open as Draft and `main` unchanged. M13 remains open.
