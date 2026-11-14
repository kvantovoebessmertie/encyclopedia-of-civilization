# M13 thematic source-passage review — Demographic Methods Basics

Date: 2026-11-13  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Review type: source-passage desk review; noncanonical audit artifact  
Scope: 3 Claims, 3 Evidence Uses, 1 Source, 1 Context, 1 Scope record

## Executive result

All three Claims are substantively plausible and have identifiable authoritative UN material that can support them. The current record set is not release-ready: the sole Source points only to the UN Population Division landing page, and all three Evidence Uses contain a generic description rather than a reproducible passage locator. No canonical record, score, publication state, manifest, or release artifact was changed.

**Disposition: HOLD for all 3 Claims** until exact source identity/edition and locators are entered through an authorized canonical correction, then independently reviewed.

## Records reviewed

| Record | Current content | Finding |
|---|---|---|
| `CLM-DEMOGRAPHIC_METHODS_BASICS-A` | Demography studies population size, structure and dynamics | Supported in substance by UN Population Division's description of estimates/projections of population size by age and sex and indicators of fertility, mortality and migration. |
| `CLM-DEMOGRAPHIC_METHODS_BASICS-B` | Births, deaths and migration are principal components of population change | Directly supported by the demographic balancing equation: initial population plus births minus deaths plus immigration minus emigration. |
| `CLM-DEMOGRAPHIC_METHODS_BASICS-C` | Demographic indicators require period, population and calculation method | Supported in substance, but wording should distinguish indicator-specific reference population/exposure, time interval, numerator/denominator and operational definition. The UN glossary defines a rate as events in a given period divided by average population or appropriate subpopulation during that period. |
| `EU-DEMOGRAPHIC_METHODS_BASICS-A/B/C` | Generic “source used…” description | Insufficient pinpointing; no section, paragraph, table, definition, page or URL fragment. |
| `SRC-DEMOGRAPHIC_METHODS_BASICS` | Source identity says demography measures population size, structure and change; URI is the generic UN Population Division homepage | Identity is not a bibliographic identity and the URL does not identify the specific publication or passage used. |

## Passage-level evidence map

### Claim A — scope of demography

Candidate authoritative support:
- UN DESA Population Division, *Population Trends*: describes estimates and projections of population size by age and sex and indicators of fertility, mortality, migration and urbanization. URL: https://www.un.org/development/desa/pd/content/population-trends-0
- UN DESA Population Division, *World Population Prospects 2024: Methodology of the United Nations population estimates and projections*. Landing page and report entry: https://www.un.org/development/desa/pd/world-population-prospects-2024/

Assessment: **SUBSTANTIVE SUPPORT FOUND**. The current claim is a concise disciplinary summary, not a verbatim formal definition. The cited UN material covers size, age/sex structure and demographic dynamics/components. Prefer citing the WPP methodology report with the exact section defining population estimates and demographic components, or the Population Trends page as a concise overview.

### Claim B — components of population change

Candidate authoritative support:
- UN DESA Population Division, *Methodology of the United Nations population estimates and projections*, section 2.1 “The general balancing demographic equation”. Public report copy: https://www.unpopulation.org/development/desa/pd/sites/un.org.development.desa.pd/files/undesa_pd_tp_2020_population1.pdf
- The section expresses population at time t as initial population plus births minus deaths plus arrivals minus departures, and explains the three demographic components as fertility, mortality and net migration.

Assessment: **DIRECT SUPPORT FOUND**. This is the strongest match among the three Claims. The source passage directly states the equation and defines its terms. Canonical EU should identify section 2.1 and the equation, not merely the document URL.

### Claim C — metadata needed to interpret indicators

Candidate authoritative support:
- UN Statistics Division, UNdata Demographic Glossary, entry “rate”: a rate is most appropriately the number of events in a given period divided by average population or the appropriate subpopulation during that period. URL: https://data.un.org/Glossary.aspx?q=rate
- UN DESA Population Division, *World Population Prospects 2024: Methodology of the United Nations population estimates and projections*, definitions of crude birth rate, crude death rate and crude net migration rate. URL: https://population.un.org/wpp/assets/Files/WPP2024_Methodology-Report_Final.pdf

Assessment: **PARTIAL / WORDING NEEDS PRECISION**. Period and denominator/population-at-risk are explicit in the UN rate definition. “Method of calculation” is implicit in the operational formula but should be made explicit in the claim or supported by a source passage that documents indicator definitions and methods. The claim should not imply that every demographic indicator uses the same denominator or population concept.

## Source quality and identity

The current Source URI is a general Population Division homepage. It is a credible institutional gateway, but it is not a sufficiently specific source identity for these three claims. The candidate evidence above is authoritative and relevant, but it comprises at least two distinct UN sources:
1. UN DESA Population Division WPP methodology (population balance, fertility, mortality, migration, estimation methods).
2. UN Statistics Division UNdata Demographic Glossary (meaning and denominator logic of “rate”).

Do not silently replace the existing Source record with a different publication. A canonical correction should either create separately identified Source records for the exact publications or revise the current Source only if the record's provenance and identity rules permit it. Then split or link Evidence Uses so each claim points to its actual supporting source.

## Required canonical correction packet

1. Replace the homepage-only identity with publication-level metadata: issuing body, exact title, edition/year, stable URL and access date.
2. Add a distinct Source for the UNdata Demographic Glossary if Claim C continues to rely on that definition.
3. Rewrite EU-A to pinpoint the Population Trends overview or the relevant WPP methodology sections on population size and age/sex structure.
4. Rewrite EU-B to pinpoint §2.1 and the demographic balancing equation.
5. Rewrite EU-C to pinpoint the UNdata “rate” entry and the relevant WPP 2024 indicator definitions; clarify reference period, denominator/population-at-risk, numerator and operational method.
6. Re-run schema/reference validation and source identity checks after the authorized edit.
7. Obtain independent reviewer assessment; this desk review is not an independent specialist review and does not assign D/E/B scores.

## Decision

| Claim | Desk-review evidence finding | D/E/B disposition | Release disposition |
|---|---|---|---|
| A | Substantive support found | Not newly scored | HOLD |
| B | Direct support found | Not newly scored | HOLD |
| C | Partial support; wording/locator precision required | Not newly scored | HOLD |

## Limits

This review checks the fit of identified source passages to the claim wording. It does not establish source independence, current canonical validity, editorial authorization, specialist consensus, or publication readiness. No score winner is selected, no canonical record is edited, and no release gate is waived.
