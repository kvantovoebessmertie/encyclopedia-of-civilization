# Domain Audit — Society and Public Institutions (Part II) — 2026-11-19

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR workstream: #22, Work Package 1 — first-edition candidate selection  
Scope: exact canonical records in ten social-systems/public-institutions slices  
Disposition: **0 INCLUDE / 10 HOLD / 0 EXCLUDE**

## Scope and duplicate control

The Part II map defines society and institutions as a core domain family. This package screened ten distinct slices that were not covered by the earlier economics addendum or the prior engineering/computing and human-sciences remediation:

1. `sociology-basics`
2. `law-basics`
3. `demography-basics`
4. `governance-basics`
5. `public-administration-basics`
6. `education-systems`
7. `democratic-institutions-basics`
8. `public-budgeting-basics`
9. `social-statistics-basics`
10. `migration-basics`

Each slice was screened at its current canonical 9-record structure: one Source, three Claims, three Evidence Use records, one Context and one Scope. Total: **90 records** (10 Sources, 30 Claims, 30 Evidence Use, 10 Context, 10 Scope).

This is a record-level candidate screen. It is not a legal opinion, a rights clearance, a full subject-matter peer review, or release approval. No canonical JSON, publication status, allowlist or decision was changed.

## Inventory and decisions

| Slice | Records | Source | Claims | Evidence Use | Context | Scope | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| sociology-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| law-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| demography-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| governance-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| public-administration-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| education-systems | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| democratic-institutions-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| public-budgeting-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| social-statistics-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| migration-basics | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| **Total** | **90** | **10** | **30** | **30** | **10** | **10** | **0 INCLUDE / 10 HOLD / 0 EXCLUDE** |

All inspected records currently carry `record_version=1`, `publication_status=published`, and `completion_status=complete`. Those stored publication/completion fields are not first-edition approval.

## Slice findings

### 1. sociology-basics — HOLD

- All three Claims are editorial/meta statements about the slice, source/context dependence and the need for specialist checking. They are not substantive sociology propositions.
- The American Sociological Association source family is relevant. Its published introductory material defines sociology as the scientific study of social life and describes study of social structure, social change, interactions and research methods.
- All three Evidence Use records contain only a generic description; none identifies a definition, passage, or method locator.
- Context and Scope are generic and do not define the subject's central concepts.

Required work: replace the three meta-Claims with substantive, bounded propositions (e.g. social life/social structure, institutions and interaction, or research methods) and pin each to an exact ASA source passage. Keep claims descriptive, not ideological or prescriptive.

### 2. law-basics — HOLD

- Claims A and B are substantive and substantially supported by Cornell Legal Information Institute's Wex entry on jurisdiction: legal authority, personal jurisdiction, subject-matter jurisdiction and territorial jurisdiction.
- Claim C is primarily a scope/editorial caution about jurisdiction-specific law and U.S. examples; it is useful but is not a distinct legal proposition directly established by the same Wex page.
- The current source is explicitly U.S.-law-oriented. Context correctly identifies it as a U.S. educational example, but the slice title `law-basics` is broader than the single jurisdiction topic represented.
- Evidence Use A–C contain no pinpoint locators. A single Wex page cannot support a general introduction to all law.

Required work: either narrow the slice's scope/title to jurisdiction basics or add distinct, authoritative foundational legal sources for the broader law concepts. Keep the U.S. jurisdiction limitation explicit. Move the general warning in Claim C into Context/Scope if it is retained as editorial guidance. Add exact Wex subtopic locators and independent support for any additional concepts.

### 3. demography-basics — HOLD

- Claims A–C are substantive: fertility, mortality and international migration as components of population change; age structure/population momentum; and the model- and assumption-dependent nature of estimates and projections.
- UN World Population Prospects 2024 directly supports the first two propositions. Its Summary of Results §1.5 describes fertility, mortality and international migration and identifies population momentum as a further driver arising from past age structure.
- The source family is strong, but the Source record points to a summary landing page and Evidence Use is generic. Claim C needs the WPP methodology report and its assumptions/uncertainty sections, not merely the results page.
- Context correctly distinguishes projections from observations and requires a reference date. Scope is generic.

Required work: pin WPP 2024 Summary of Results §1.5 for Claims A/B and the exact methodology sections for Claim C; record reference dates and scenario/assumption boundaries. Keep projections distinct from observations.

### 4. governance-basics — HOLD

- Claims A–C are substantive and closely aligned with the OECD Policy Framework on Sound Public Governance.
- The OECD framework defines public governance in its introductory section/Box 1.1 and describes three interconnected elements: values, enablers, and instruments/tools. It also states that governance values are shaped by country-specific cultural traditions.
- The Source is a good direct source candidate, but all Evidence Use records are generic and lack exact chapter/box/page locators.
- Context appropriately avoids political ranking or recommendation. Scope remains generic.

Required work: pin the OECD definition (Box 1.1), the section describing the three elements, and the country-context discussion. Preserve the framework's descriptive character; do not convert OECD guidance into a universal constitutional model or endorsement.

### 5. public-administration-basics — HOLD

- Claims A–C are substantive but broad: public functions/services, administrative powers/procedures, and jurisdiction-specific mandates.
- The current Source is the OECD Government portal landing page, not a specific publication or recommendation. It does not provide a traceable locator for the three propositions.
- Evidence Use A–C are generic and do not identify a chapter, recommendation or paragraph.
- Context and Scope are boilerplate and do not distinguish public administration from public governance or public service delivery.

Required work: select exact OECD materials (for example, the Recommendation on Public Service Leadership and Capability and/or the human-centred public administrative services recommendation) and pin specific provisions. Use jurisdiction-specific legal sources for claims about statutory powers. Clarify the boundary between governance, administration and service delivery.

### 6. education-systems — HOLD

- Claim A contains a material overstatement: UNESCO describes education as a human right and promotes lifelong-learning opportunities, but UNESCO explicitly notes that a general right to lifelong learning is not itself an explicit right under international human-rights law; it is expressed in SDG 4 language. The current wording, “lifelong learning as part of that right,” conflates these distinctions.
- Claim B is supported by UNESCO's four essential features of the right to education: availability, accessibility, acceptability and adaptability.
- Claim C (national differences in law, financing, governance, curriculum and delivery) is plausible but not supported by the current single right-to-education page.
- Evidence Use A–C are generic. Context appropriately requires country, period and applicable law, but does not cure the overstatement in Claim A.

Required work: correct Claim A to distinguish the right to education from the SDG 4 commitment to promote lifelong-learning opportunities; retain Claim B with the four-A locator; find separate comparative education-systems evidence for Claim C. Do not present an international policy commitment as identical to a directly enforceable domestic right in every jurisdiction.

### 7. democratic-institutions-basics — HOLD

- Claims A–C are substantive and broadly align with International IDEA's State of Democracy Assessment Framework and work on political participation and representation.
- IDEA's framework distinguishes citizenship/law/rights, representative and accountable government, civil society/participation, and democracy beyond the state. Its mediating values include participation, authorization, representation, accountability, transparency, responsiveness and solidarity.
- The current Source is the general IDEA Democracy page rather than the specific framework or framework version. Evidence Use has no precise framework/section locator.
- The Source provenance method is recorded as `editorial_context`, and Evidence Use provenance is recorded as `source_based_claim_representation` with Claim references. These methods should be reviewed for semantic consistency with the actual Source and Evidence Use record roles during any authorized remediation.
- Context is appropriately descriptive and non-causal; Scope is bounded but still generic.

Required work: identify the exact IDEA framework/version and pin the relevant pillars and mediating-value sections. Align provenance methods with the actual record roles without altering the substantive Claims unnecessarily. Avoid implying that IDEA's framework is the only valid model of democracy.

### 8. public-budgeting-basics — HOLD

- Claims A–C are substantive: budgets connect revenue/expenditure with public priorities; budget processes include preparation, approval, execution and review; and approved priorities are not automatically funded outcomes.
- The IMF Public Financial Management landing page is relevant as a topic portal but not a precise supporting source.
- IMF fiscal transparency materials directly describe fiscal forecasting/budgeting, budget objectives and policy intentions, public revenue/expenditure classification, budget preparation, execution and reporting. These are stronger source candidates for A/B.
- Claim C needs precise support about appropriations, resource constraints, execution and deviations; the current broad portal does not establish it.
- Evidence Use A–C are generic. Source and Scope provenance metadata should be checked for role consistency during remediation.

Required work: pin the IMF Fiscal Transparency Code (Pillar II, fiscal forecasting and budgeting), Manual on Fiscal Transparency, and/or current PFM guidance to exact sections. Keep budget preparation, legislative approval, execution and audit/review distinct; avoid implying a single universal sequence across all jurisdictions.

### 9. social-statistics-basics — HOLD

- Claims A–C are substantive: subject coverage, importance of definitions/classifications/methodology for comparability, and the distinction between an operational statistical indicator and causal explanation.
- The UN Statistics Division Demographic and Social Statistics portal is a relevant institutional source family and identifies social/demographic topics and standards/methods. It is not a pinpoint source for the three Claims.
- UN Fundamental Principles / international standards guidance directly supports the importance of common concepts, classifications and methods for consistency and comparability.
- Claim C needs a dedicated statistical-methods source for operational definitions and the non-equivalence of descriptive indicators and causal inference.
- All Evidence Use records are generic; Context and Scope are boilerplate.

Required work: select exact UN statistical standards and methods, pin the relevant concepts/classification/method sections, and add a suitable methods source for Claim C. Preserve the distinction between official statistics, survey estimates and causal inference.

### 10. migration-basics — HOLD

- Claims A–C are substantive: migration as movement/change of usual residence, diverse drivers, and the non-equivalence of migrant/refugee/other displaced-person categories.
- The IOM World Migration Report is a relevant source family, but the canonical Source points only to the report portal. Evidence Use A–C contain no chapter, section, definition or page locators.
- Claim C is legally sensitive: “migrant,” “refugee,” asylum-seeker and internally displaced person are not interchangeable, but the legal definitions and protections arise from distinct international instruments and operational definitions. A general IOM report alone may not establish all legal boundaries.
- Context and Scope are generic and do not identify the report edition or jurisdiction-specific legal framework.

Required work: pin a specific World Migration Report edition/chapter for migration definitions and drivers; use UNHCR/1951 Convention and relevant IDP instruments for the legal distinction in Claim C. Record edition/year and avoid collapsing different categories into one umbrella definition.

## Cross-slice findings

1. **Record shape:** the ten inspected slices each contain the expected nine record roles.
2. **Evidence Use:** all 30 Evidence Use records lack claim-specific pinpoint locators. The repeated generic material descriptions do not show which passage supports each Claim.
3. **Substantive Claims:** six slices have mostly substantive Claims (law, demography, governance, education, democratic institutions, public budgeting, social statistics, migration), but one or more claims need narrower support or correction. Sociology has three editorial/meta Claims.
4. **Source identity:** broad landing pages are used where a precise source is required in public administration, social statistics and migration; education uses a rights page for a wider systems claim; democracy uses a general IDEA page rather than the exact framework. Demography, governance and law have stronger source families but still lack precise locators.
5. **Provenance metadata:** democratic institutions and public budgeting use differing `provenance.method` patterns on Source/Evidence Use records. Confirm role semantics against the record standard before any changes; do not infer a validation failure solely from the method label.
6. **Context/Scope:** some contexts are useful (law, demography, governance, education, democracy), while several scopes remain generic. Every slice needs a reader-facing boundary that is specific to its subject.
7. **Rights and editorial:** public availability does not establish permission to redistribute or adapt source expression. No rights clearance or independent subject-matter/Human View review is asserted.
8. **Selection:** all ten slices remain HOLD. Existing `publication_status=published` values are not first-edition approval.

## Group result

**90/90 records screened; 0 INCLUDE / 10 HOLD / 0 EXCLUDE.**

No canonical JSON was modified. No Source, Claim, Evidence Use, Context or Scope version was changed. No first-edition allowlist, publication status, completion status or release decision was changed. No main-branch change, merge, deployment or release action was performed.

## Next work under the first-edition plan

1. Reconcile this audit with the exact-version candidate register; do not overwrite prior historical decisions.
2. Obtain bounded correction authorization before any canonical changes. Priority corrections: sociology's three meta-Claims; education Claim A's lifelong-learning overstatement; law's jurisdiction-only scope; source and locator repairs across the ten slices.
3. Complete exact-source rights/attribution screens and identify any required permission before release.
4. Continue the next Part II family only after duplicate control against prior candidate reviews. Do not repeat M13 or previously completed audits.
5. Keep all ten slices HOLD until exact-version evidence, rights, independent editorial review, Human View and exact-head CI gates are closed.

## Source references consulted

- American Sociological Association, “What Is Sociology?” brochure: https://www.asanet.org/wp-content/uploads/2023/11/Brochure_Sociology_21st_Century_Major.pdf
- Cornell Legal Information Institute, Wex, “Jurisdiction”: https://www.law.cornell.edu/wex/Jurisdiction
- United Nations, *World Population Prospects 2024*, Summary of Results, §1.5: https://population.un.org/wpp/assets/Files/WPP2024_Summary-of-Results.pdf
- OECD, *Policy Framework on Sound Public Governance*, Box 1.1 and Part I: https://www.oecd.org/en/publications/policy-framework-on-sound-public-governance_c03e01b3-en/full-report.html
- OECD, *Recommendation on Public Service Leadership and Capability*: https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0445/
- UNESCO, “State obligations and responsibilities on the right to education”: https://www.unesco.org/en/right-education/state-obligations-responsibilities
- International IDEA, *State of Democracy Assessment Framework*: https://www.idea.int/data-tools/tools/state-democracy-assessments/state-democracy-framework
- IMF, *Fiscal Transparency Code 2019*: https://www.imf.org/external/np/fad/trans/Code2019.pdf
- IMF, *Manual on Fiscal Transparency*, Chapter III: https://www.imf.org/external/np/fad/trans/manual/sec03a.htm
- UN Statistics Division, “Demographic and Social Statistics”: https://unstats.un.org/unsd/demographic-social/
- UN Statistics Division, “Principle 9 — Use of international standards”: https://unstats.un.org/capacity-development/handbook/html/Handbook/C3/UN_Fundamental_Principles_of_Official_Statistics.htm
- IOM, *World Migration Report 2024*: https://publications.iom.int/system/files/pdf/pub2023-047-l-world-migration-report-2024_0.pdf
