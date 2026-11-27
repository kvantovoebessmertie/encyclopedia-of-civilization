# R7 Labour Economics — ILO Path B Exact-Record and Rights-Boundary Verification

Date: 2026-11-20  
Inspection PR HEAD: `c177cbf0def595b4d478d0eddb512db5b33c18d4`  
Owner authorization: `R7-LABOUR-ECONOMICS-ILO-PATH-B-OWNER-DECISION-2026-11-20`  
Status: **OWNER-APPROVED PATH B IMPLEMENTED; 13/13 CURRENT RECORDS RE-FETCHED; RIGHTS BOUNDARIES PRESERVED; SLICE AND DEPENDENT RELATIONS REMAIN HOLD**

## 1. Supersession

This report supersedes the “Path A/B/C pending” status in the 2026-11-19 OpenStax decision packet for the bounded Labour Economics remediation only. On 2026-11-20 the project owner explicitly selected Path B: an ILO-led replacement source chain. The corresponding bounded authorization is present in `RELEASE/EDITORIAL-CORRECTION.json`.

OpenStax is excluded from the authorized Labour Economics source chain. This is not a general OpenStax rights decision for other slices.

## 2. Exact current 13-record graph

All 13 records named by the owner authorization were re-fetched at the same inspection HEAD. Every record is current version @2.

| Record | Type | Current version | Exact reference result |
|---|---|---:|---|
| `SRC-LABOR_ECONOMICS_BASICS` | Source | @2 | ILOSTAT hub; item-level page licences not asserted |
| `SRC-LABOR_ECONOMICS_BASICS-INDEPENDENT` | Source | @2 | ILO WESO 2023; work-level CC BY 4.0 recorded |
| `CLM-LABOR_ECONOMICS_BASICS-A` | Claim | @2 | provenance → primary Source @2 |
| `CLM-LABOR_ECONOMICS_BASICS-B` | Claim | @2 | provenance → primary Source @2 |
| `CLM-LABOR_ECONOMICS_BASICS-C` | Claim | @2 | provenance → primary Source @2 |
| `EU-LABOR_ECONOMICS_BASICS-A` | Evidence Use | @2 | Claim A@2 + primary Source@2 |
| `EU-LABOR_ECONOMICS_BASICS-B` | Evidence Use | @2 | Claim B@2 + primary Source@2 |
| `EU-LABOR_ECONOMICS_BASICS-C` | Evidence Use | @2 | Claim C@2 + primary Source@2 |
| `EU-LABOR_ECONOMICS_BASICS-INDEPENDENT-A` | Evidence Use | @2 | Claim A@2 + independent Source@2 |
| `EU-LABOR_ECONOMICS_BASICS-INDEPENDENT-B` | Evidence Use | @2 | Claim B@2 + independent Source@2 |
| `EU-LABOR_ECONOMICS_BASICS-INDEPENDENT-C` | Evidence Use | @2 | Claim C@2 + independent Source@2 |
| `CTX-LABOR_ECONOMICS_BASICS` | Context | @2 | target_ref → Claim A@2 |
| `SCP-LABOR_ECONOMICS_BASICS` | Scope | @2 | target_ref → Claim A@2 |

No OpenStax Source is present in the two current Source records or in the six current Evidence Use records.

## 3. Claim and Evidence Use review

The current Claim statements are:

- Claim A@2: labour economics studies labour markets, employment, wages and related institutions.
- Claim B@2: wages are both workers' income and part of employers' labour costs.
- Claim C@2: labour-market analysis uses employment, earnings, working time, productivity and labour-underutilization indicators.

The primary Evidence Use records have exact Claim/Source references and specific ILOSTAT locators:
- EU A@2: ILOSTAT LFS/RURBAN, ILO Thesaurus “Labour economics”, and Concepts and Definitions. Boundary: introductory scope, not an exhaustive discipline account.
- EU B@2: ILOSTAT COND wages and working-time description. Boundary: employee earnings versus employer labour cost; not a numerical estimate.
- EU C@2: LFS employment/unemployment/participation; COND wages/working time; productivity/hours; ILO labour-underutilization measures. Boundary: indicators differ by series and reference period and are not interchangeable without methodological checks.

The independent WESO Evidence Use records @2 cite:
- A: Chapter 1 “Who are the key workers?” and Chapter 3 “Working conditions of key workers”.
- B: Chapter 3 sections on wages and working hours.
- C: Chapter 1 and Chapter 3 sections on working hours and wages.

The independent WESO source provides international context but does not independently establish the full indicator family, especially productivity and labour underutilization. Those remain supported by the primary ILOSTAT locator set, subject to the source-page licence caveat.

## 4. Rights boundary verification

### Primary ILOSTAT Source @2

The current Source record expressly says:
- citation and locator reference only;
- item-level publication date/licence for the referenced ILOSTAT pages is not established;
- no CC BY 4.0 is asserted for those pages;
- independently worded factual paraphrase and citations only;
- no page text, datasets or third-party assets reproduced.

This is the correct conservative boundary. Do not infer that every ILOSTAT web page inherits the licence of the WESO report or the separate ILO 2026 practical guide.

### Independent ILO WESO 2023 Source @2

The Source record identifies *World Employment and Social Outlook 2023: The value of essential work*, DOI 10.54394/OQVF7543, published 8 March 2023, and records the report PDF's explicit CC BY 4.0 notice. It excludes the third-party cover photograph and separately credited assets, requires ILO attribution, and prohibits use of the ILO emblem.

### New ILO 2026 Migration/Labour Guide

The 2026 *Mapping and assessing sources for statistics of international labour migration and temporary labour mobility* was identified during the separate cross-slice research audit. Its own copyright page states CC BY 4.0. **It is not one of the 13 authorized Labour Economics records and has not been added to this graph.** Adding it as a Source/Evidence Use or Relation provenance reference would require a separate bounded authorization. The 2026 guide does not silently amend the existing ILOSTAT Source @2.

## 5. Dependent Relations

The owner authorization expressly allowed the Labour Claim C provenance/participant alignment in:
- `REL-CROSS-MIGRATION-LABOR-ECONOMICS@4` ↔ `CTX-REL-CROSS-MIGRATION-LABOR-ECONOMICS@1`.
- `REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY@4` ↔ `CTX-REL-CROSS-LABOR-ECONOMICS-SOCIAL-POLICY@1`.

Both current Relations have exact Claim C@2 participants/provenance; both Contexts target their exact Relation @4; both Relation frame_refs target their exact Context @1. The direct Claim provenance pattern was expressly included in the owner-approved Path B authorization for these two Relations. It is not an unapproved change in this bounded case.

The Migration/Labour Relation remains semantically HOLD. The new ILO 2026 guide is a promising direct bridge between migration and labour statistics, but is not yet in the canonical graph. No Relation/Evidence Use update is authorized by this verification report.

## 6. Disposition and release gates

- Labour Economics Basics remains **HOLD**.
- Both dependent Relations remain **HOLD**.
- No INCLUDE/EXCLUDE decision or allowlist entry was created.
- No canonical record was changed by this report.
- The OpenStax-specific blocker for this Labour Economics source chain is superseded by the owner-selected ILO Path B; the item-level ILOSTAT licence question remains open and explicitly bounded.
- Independent labour-economics/statistical editorial review, project distribution/rights compatibility, Human View and all first-edition gates remain open.

## 7. Change-control statement

This is a read-only verification of the owner-approved Path B implementation. It does not expand the authorization, add the 2026 ILO guide to canonical records, adopt a project licence, or permit publication.

**Acceptance:** 13/13 exact records verified at @2; dependent relation/context links exact; all records and Relations remain HOLD.
