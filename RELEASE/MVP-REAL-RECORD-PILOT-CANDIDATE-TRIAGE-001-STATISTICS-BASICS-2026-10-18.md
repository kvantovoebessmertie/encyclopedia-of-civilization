# MVP real-record pilot — candidate triage 001: statistics basics

Date: 2026-10-18  
Branch: `mvp-reader-prototype-2026-10-11`  
State: **HOLD — candidate review only; not approved for pilot**

## Candidate

- Claim: `CLM-STATISTICS_BASICS-A@1`
- Current Evidence Use: `EU-STATISTICS_BASICS-A@1`
- Current primary Source: `SRC-STATISTICS_BASICS@1` — NIST/SEMATECH Engineering Statistics Handbook
- Additional Evidence Use: `EU-STATISTICS_BASICS-OPENSTAX@1`
- Additional Source: `SRC-OPENSTAX-STATISTICS-BASICS@1`

Claim statement:

> Статистика предоставляет методы для описания данных, анализа вариации и количественного обоснования выводов.

This is a relatively low-consequence educational candidate compared with emergency or prescriptive safety guidance. It is a useful candidate for testing source navigation, scope notes, and explanatory rendering. Low consequence alone is not approval.

## Passage-fit review

OpenStax, *Introductory Statistics 2e*, section 1.1 directly states that statistics deals with “the collection, analysis, interpretation, and presentation of data.” The same section describes descriptive statistics as organizing and summarizing data, and inferential statistics as formal methods for drawing conclusions from data.

Source:
https://openstax.org/books/introductory-statistics-2e/pages/1-1-definitions-of-statistics-probability-and-key-terms

This directly supports the core definition, but the existing Claim additionally mentions “analysis of variation” and “quantitative justification of conclusions.” The currently linked Evidence Use is generic and has no section/paragraph locator. The NIST source is an engineering-statistics handbook landing page, not a pinpointed handbook passage. The exact full Claim therefore remains only partially substantiated by the current record chain.

## Rights and reuse check

OpenStax's *Introductory Statistics 2e* preface identifies the textbook as CC BY-NC-SA 4.0 and states that reuse/adaptation is for noncommercial purposes, requires attribution, and requires derivatives to be shared under the same licence. Its reuse guidance also calls out restrictions on commercial reuse.

License information:
https://openstax.org/books/introductory-statistics-2e/pages/preface

This means the project must not assume the OpenStax material can be reused in any future commercial or investor-supported distribution model without a documented rights analysis. A short factual summary and a link may be treated differently from reproducing or adapting textbook prose, but that decision must be documented by the responsible rights reviewer. Do not copy textbook text into the reader during this candidate triage.

## Preliminary D/E/B and disposition

- D=1: foundational educational concept; the claim itself is not an operational instruction.
- E=1: the current linked NIST Evidence Use has no pinpoint; OpenStax directly supports the core definition but not every phrase in the Claim.
- B=1: the current record chain is broad/generic and the full proposition is not yet matched to exact passages.

**Decision: HOLD.** Do not include this record in a real-record build yet.

Required follow-up before reconsideration:
1. Locate exact NIST handbook section(s) for variation and quantitative inference, or narrow the proposed reader summary to the exact OpenStax-supported proposition through a separately authorized, versioned content change.
2. Add a claim-specific locator to the relevant Evidence Use record only through the project's approved correction workflow.
3. Record a rights decision for OpenStax use and attribution, including the implications of CC BY-NC-SA 4.0 for any future distribution model.
4. Obtain an independent reviewer’s sign-off.
5. Re-run reproducible build and all release gates on the exact candidate commit.

No canonical Claim, Evidence Use, or Source record was changed by this triage. This file does not authorize publication, a pilot allowlist, or a public release.
