# First Edition — Batch 16 Migration Basics Evidence and Legal-Status Boundaries

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
PR #22 branch: `mvp-public-contribution-design-2026-10-11`  
Inspection baseline: `7e2fa0cc8a9286c3037cd595865390e35f07abb3`  
Status: **3 CANDIDATE CLAIMS / 3 EUS RESEARCHED; IOM DIRECT DEFINITIONS AND DRIVER LOCATORS FOUND; REFUGEE/IDP LEGAL BOUNDARIES PINNED TO UN SOURCES; ALL HOLD; NO CANONICAL JSON CHANGED**

## 1. Scope and selection controls

Migration Basics was the only candidate slice in the current exact-version master that remained outside Batches 1–15, active bounded authorizations and prior-screened batches. Water Security is not repeated because it has a separate P8 re-audit.

Current records re-fetched:
- `CLM-MIGRATION_BASICS-A/B/C@1`
- `EU-MIGRATION_BASICS-A/B/C@1`
- `SRC-MIGRATION_BASICS@1`

All seven exact records are present in the candidate master. The three EUs currently contain only generic descriptions and have no claim-specific `material.locator` values.

No canonical Claim, Evidence Use, Source, Context, Scope or Relation was edited. No record version, publication/completion status, allowlist or INCLUDE/HOLD/EXCLUDE decision changed. Migration Basics remains HOLD.

## 2. Claim-by-claim evidence

| Claim / EU | Current proposition | Direct locator candidate |
|---|---|---|
| A | Migration includes movement of people from one place of residence to another, including across international borders | IOM World Migration Report Educators' Toolkit Glossary, entry “Migration”; entry defines movement away from usual residence either across an international border or within a State |
| B | Causes/forms of migration can include economic, family, education, conflict and other circumstances | IOM World Migration Report Educators' Toolkit, Module 3 “Why do people migrate?”, “Why do people migrate?” and “Drivers of migration”; work, family and study are common reasons; conflict, persecution and disasters can compel movement |
| C | Migrant, refugee and other displaced-person categories are not interchangeable; classification depends on applicable legal and factual criteria | IOM Toolkit Glossary entries “Migrant”, “Refugee (1951 Convention)” and “Internally Displaced Persons (IDPs)”; UNHCR 1951 Refugee Convention, Article 1 definition; UN Guiding Principles on Internal Displacement, para. 2 |

Sources:
- IOM World Migration Report Educators' Toolkit, Glossary: https://wmr-educatorstoolkit.iom.int/glossary
- IOM World Migration Report Educators' Toolkit, Module 3 PDF: https://worldmigrationreport.iom.int/sites/g/files/tmzbdl1691/files/2021-12/Updated%20WMR%20Toolkit_30%20Nov.pdf
- UNHCR, “The 1951 Refugee Convention”, “What is the definition of a refugee?”: https://www.unhcr.org/about-unhcr/overview/1951-refugee-convention
- UN Guiding Principles on Internal Displacement, Introduction, para. 2: https://digitallibrary.un.org/nanna/record/251017/files/E_CN-4_1998_53_Add-2-EN.pdf
- UNHCR, “Internally Displaced People”, definition and “What is the difference between an IDP and a refugee?”: https://www.unhcr.org/about-unhcr/who-we-protect/internally-displaced-people

### Claim A — migration definition

The IOM Toolkit Glossary entry “Migration” defines migration as movement away from a person's usual place of residence, either across an international border or within a State. It covers movement regardless of length, composition or cause. This directly supports the current Claim.

Preserve the distinction between:
- migration as a broad movement concept;
- international migration (crossing an international border);
- internal migration (movement within a State).

Do not imply that all migration is international or that every migrant has the same legal status.

### Claim B — drivers and forms

The IOM Toolkit Module 3 states that many international migrants move for work, family and study. It also describes people leaving because of conflict, persecution and disaster. The module explicitly frames drivers as multi-faceted and interlinked, with movement ranging along a continuum from voluntary to forced.

This supports the Claim's examples. The EU should cite Module 3 and record the boundary that the list is illustrative, not exhaustive; migration decisions may have multiple interacting drivers. Do not classify all economic, family or educational migration as forced migration.

### Claim C — legal categories

The IOM Toolkit Glossary provides distinct entries for “Migrant”, “Refugee (1951 Convention)” and “Internally Displaced Persons (IDPs)”. The legal and factual boundaries are important:

- **Migrant:** IOM uses a broad movement-based definition; it is not a synonym for refugee.
- **Refugee:** Article 1 of the 1951 Refugee Convention defines a refugee through a well-founded fear of persecution on specified grounds, being outside the country of nationality/former habitual residence, and inability/unwillingness to avail oneself of that country's protection.
- **IDP:** paragraph 2 of the UN Guiding Principles describes a person forced to leave home/usual residence who has not crossed an internationally recognized State border.

UNHCR also distinguishes refugees from IDPs: crossing an international border is a central distinction. The Guiding Principles are not a treaty and do not create a separate legal status in the same way as the 1951 Refugee Convention; UNHCR's guidance notes that IDPs remain within their own country and retain the rights of citizens/habitual residents.

**Claim boundary:** legal recognition of refugee status and other protection categories depends on the applicable international, regional and national framework and individual circumstances. Do not imply that every displaced person meets the 1951 Convention definition or that IOM's broad term “migrant” is a formal legal status in every jurisdiction.

## 3. Source identity and graph recommendation

The current Source record identifies “IOM — World Migration Report” and points to the general World Migration Report landing page. The direct material used here is more specific: the World Migration Report Educators' Toolkit (2022) and its glossary/module pages.

Recommended bounded remediation:
1. Version `SRC-MIGRATION_BASICS` to an exact identity for the IOM World Migration Report Educators' Toolkit (edition/year) and a stable official toolkit URI, or retain the current WMR Source and add a distinct Toolkit Source.
2. Version `EU-MIGRATION_BASICS-A/B` with exact Toolkit Glossary/Module 3 locators and the corresponding current Source reference.
3. For `EU-MIGRATION_BASICS-C`, add separate UNHCR and UN Guiding Principles source/Evidence Use dependencies. Do not combine IOM, UNHCR and UN sources in one Source record.
4. Preserve `evidence_role: supports`; no new base Evidence Use role is needed.
5. Do not invent canonical Source or EU IDs. Allocate IDs under the project's canonical ID policy and update the exact-version master only after the records are created and verified.

## 4. Rights and high-consequence review

- IOM reports and the Educators' Toolkit are copyrighted institutional publications. Use attribution and factual paraphrase; no permission to reproduce toolkit pages, diagrams or photographs is inferred.
- The 1951 Refugee Convention and UN Guiding Principles are official legal instruments/documents. Quote only where necessary and retain exact article/paragraph locators.
- UNHCR explanatory pages are authoritative guidance but do not replace the treaty text or applicable national/regional law.
- This slice contains legal-status distinctions affecting rights and protection. It requires qualified migration/refugee-law review and independent Human View before any release decision.
- All Claims remain HOLD.

## 5. Recommended execution order after owner authorization

1. Pin Claim A to the IOM Toolkit Glossary “Migration” entry.
2. Pin Claim B to Module 3 “Why do people migrate?” and state that drivers are illustrative and often interlinked.
3. Expand Claim C's evidence graph with separate IOM, UNHCR and UN Guiding Principles records; preserve the distinction between migrant, refugee and IDP.
4. Re-fetch all authorized records at one frozen HEAD, apply only approved versioned changes, validate exact Claim→EU→Source references, run affected-slice tests and then full release gates on the final immutable HEAD.

## 6. Explicit non-actions

This report does not:
- authorize or perform any canonical JSON change;
- change Claim statements or versions;
- create new canonical Source/Evidence Use IDs;
- change publication/completion status or INCLUDE/HOLD/EXCLUDE decisions;
- modify Relations, validators, storage, recovery, allowlists or release-gate semantics;
- merge PR #22, deploy or approve publication.

**Owner decision required:** approve the Toolkit Source alignment and the additional UNHCR/UN Guiding Principles source/EU chains for Claim C under exact canonical IDs.
