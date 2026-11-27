# Society and Institutions Gap Audit — 2026-11-19

Date: 2026-11-19  
Branch: `mvp-public-contribution-design-2026-10-11`  
Scope: two remaining, not-yet-adjudicated Part II slices in the Society and Institutions family. Existing audits of law, governance, demography, education systems and the five-slice economics addendum are reused and not repeated.

## Scope and method

Reviewed all 18 exact current canonical JSON records in:

- `sociology-basics`
- `public-administration-basics`

The review checked exact record identity/version, source relevance, Claim substance and scope, Evidence Use specificity, provenance/reference alignment, and Context/Scope usefulness. This is a record-level screening pass, not a complete legal/jurisdictional or source-rights clearance.

## Record inventory

| Slice | Records | Source | Claims | Evidence Use | Context | Scope | Decision |
|---|---:|---:|---:|---:|---:|---:|---|
| `sociology-basics` | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| `public-administration-basics` | 9 | 1 | 3 | 3 | 1 | 1 | HOLD |
| **Total** | **18** | **2** | **6** | **6** | **2** | **2** | **0 INCLUDE / 2 HOLD / 0 EXCLUDE** |

## Findings by slice

### sociology-basics — HOLD

- Claims A–C are editorial/meta placeholders: they describe what the slice introduces, that interpretation depends on context, and that specialist review may be needed. They are not sociological propositions.
- The Source identifies the American Sociological Association's “What Is Sociology?” page. This is a relevant professional-association source candidate for a bounded definition of sociology and its subject matter, but the canonical record contains no exact section or stable pinpoint.
- All three Evidence Use records contain only generic support descriptions and no passage-level locator.
- Context and Scope are boilerplate and do not define sociology's subject matter, methods, or boundaries.

Required remediation: replace the three meta-Claims with substantive, falsifiable paraphrases of the ASA definition and description of social groups, institutions, interaction and research methods; add exact page/section locators; define Context/Scope around social science rather than normative political or individual advice. APA/ASA-style copyrighted material must not be copied; verify ASA reuse terms before publication.

### public-administration-basics — HOLD

- Claims A–C are substantive at a high level: public functions/services, administrative processes under authority/procedures, and jurisdictional dependence of public powers.
- The Source points only to the OECD Directorate for Public Governance landing page. It is not a precise publication or legal instrument that directly supports the three Claims.
- All three Evidence Use records lack exact OECD publication, chapter, paragraph or instrument locators.
- Claim C is inherently jurisdiction- and date-dependent. The current record does not identify a jurisdiction or date, so it cannot be read as a statement of any particular legal authority.
- Context and Scope are generic and do not distinguish comparative public-administration concepts from binding domestic law.

Required remediation: choose a precise OECD public-governance framework or public-service instrument for comparative institutional concepts; use the exact legal instruments and jurisdiction/date for any claim about formal powers or procedures; add claim-specific locators and an explicit comparative/non-binding boundary.

## Cross-slice findings

1. **Reference graph:** both slices have the expected 9-record structure. Claim provenance points to the current Source; Evidence Use links each Claim and Source; Context and Scope target Claim A. No stale version reference was identified.
2. **Claim substance:** sociology has three editorial/meta Claims requiring replacement. Public administration has three substantive but broad Claims requiring direct source support and a jurisdictional boundary.
3. **Evidence Use:** all six Evidence Use records lack claim-specific pinpoint locators.
4. **Source quality:** ASA is a relevant candidate for sociology but needs exact locator and rights review; the OECD landing page is insufficiently specific for public-administration propositions.
5. **Context/Scope:** sociology needs a subject/method boundary; public administration needs a comparative-governance versus domestic-law boundary.
6. **Publication:** existing `publication_status=published` values are not first-edition approval. Both slices remain HOLD.

## Reused prior work — not repeated

- `law-basics`, `governance-basics`, `demography-basics` and `education-systems` remain covered by the prior third domain-roadmap ten-slice expansion audit in `RELEASE/DOMAIN-EXPANSION-AUDIT-2026-09-30.md`.
- The five-slice economics addendum is preserved and not repeated.
- This audit adds only the two uncovered slices above.

## Aggregate decision

**0 INCLUDE / 2 HOLD / 0 EXCLUDE.**

No canonical JSON was modified. No publication state, first-edition allowlist, or release decision was changed. This report does not authorize Claim replacement, source substitution or versioned corrections.

## Next remediation order

1. Obtain bounded authorization for `sociology-basics` and `public-administration-basics`.
2. Replace sociology's three editorial/meta Claims with source-bounded propositions and add exact ASA locators.
3. Replace the OECD landing-page Source in public administration with precise publication/instrument identities and map each Claim to its locator.
4. Add explicit jurisdiction/date limits to any public-authority proposition.
5. Re-run exact-head preflight, Reference tests, Release Conformance Gate and Offline Edition.
6. Keep both slices HOLD until rights and independent editorial/Human View gates are resolved.
