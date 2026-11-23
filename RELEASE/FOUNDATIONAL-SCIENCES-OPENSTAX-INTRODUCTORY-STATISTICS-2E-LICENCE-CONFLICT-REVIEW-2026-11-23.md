# OpenStax Introductory Statistics 2e — official licence-text conflict review

Date: 2026-11-23  
Branch: `mvp-public-contribution-design-2026-10-11`  
PR #22: report-only follow-up  
Status: PRIMARY-SOURCE RIGHTS VERIFICATION — NO RIGHTS CLEARANCE / NO CANONICAL WRITES

## 1. Finding

The bounded foundational-sciences audit dated 2026-11-23 treated *OpenStax Introductory Statistics 2e* as CC BY-NC-SA 4.0 based on the current OpenStax HTML preface. A direct check of the official OpenStax PDF for the same title and edition reveals a material conflict:

- The live HTML preface states CC BY-NC-SA 4.0 and repeats noncommercial / ShareAlike conditions, plus a restriction on LLM training or ingestion without prior written permission.
- The official PDF front matter states CC BY 4.0, explicitly describes commercial reuse as permitted under attribution, and repeats CC BY 4.0 in its own Preface.
- The official OpenStax general licensing help pages describe the general library as CC BY-NC-SA, but that general statement does not resolve the title-specific HTML/PDF contradiction.

This is not a minor metadata discrepancy. It changes the stated commercial-use permission and ShareAlike obligations. The current record cannot safely assign one licence to the title as a whole without clarification from OpenStax.

## 2. Exact primary-source observations

### 2.1 Current HTML preface

URL: https://openstax.org/books/introductory-statistics-2e/pages/preface

Observed 2026-11-23:
- The Customization section says *Introductory Statistics 2e* is licensed under CC BY-NC-SA 4.0.
- The Citation/Attribution section says reuse is noncommercial, derivatives must use the same licence, and commercial printing requires OpenStax approval.
- The same section says the book may not be used for LLM training or ingested into generative-AI offerings without prior written permission.
- It separately states that copyrighted images, activities, assessments and similar components require permission for commercial use.

### 2.2 Official PDF, same title / second edition

URL: https://assets.openstax.org/oscms-prodcms/media/documents/Introductory_Statistics_2e_-_WEB.pdf

Observed in the official PDF:
- Front-matter copyright/licence statement identifies ©2023 Rice University and CC BY 4.0.
- The PDF Preface independently says the title is licensed under CC BY 4.0.
- The PDF instructs users to retain the “Access for free at openstax.org” attribution on every page when redistributing all or part of the book.
- The PDF does not contain the HTML preface's LLM-training prohibition in the inspected text.

The PDF is an official OpenStax-hosted asset and not a third-party mirror. Its licence statement must be treated as a real primary-source statement, not silently discarded.

### 2.3 General OpenStax licensing pages

- https://help.openstax.org/s/article/Openstax-textbook-licensing-and-customization?language=en_US
- https://help.openstax.org/s/article/Licensing-information-of-OpenStax-textbooks

These pages describe the general OpenStax textbook library as CC BY-NC-SA. They are useful context but do not reconcile the title-specific official PDF that says CC BY 4.0.

## 3. Bounded interpretation

The available primary sources are internally inconsistent for the same title/edition. Possible explanations (not established facts) include a stale HTML page, a stale PDF, a publishing-system error, or different rights treatment for different components. This review does not choose among them.

Do not:
- declare the whole book CC BY 4.0 based only on the PDF;
- declare the whole book CC BY-NC-SA based only on the HTML;
- infer that the PDF licence supersedes the HTML licence, or vice versa;
- assume the LLM-training restriction is void because it is absent from the PDF;
- copy or adapt textbook text, tables, figures, exercises, solutions or images into the Encyclopedia;
- use the source as a cleared commercial-distribution asset.

A licence notice is not by itself a determination of the rights status of every separately credited third-party asset. The PDF and HTML may also differ by update/version. Exact asset provenance and current version must be preserved.

## 4. Required resolution before any reuse

1. Request written clarification from OpenStax/Rice University identifying the controlling licence for *Introductory Statistics 2e*, publication date 13 December 2023, digital edition ISBN 978-1-961584-32-7, and the specific HTML/PDF URLs above.
2. Ask explicitly whether CC BY 4.0 applies to the textbook text in the current PDF, whether the HTML CC BY-NC-SA notice is erroneous or applies to a distinct version, and whether any LLM-ingestion restriction applies independently of the Creative Commons licence.
3. Ask whether figures, tables, activities, assessments, solutions and separately credited assets have different rights.
4. Archive the written response, the exact downloaded PDF checksum, retrieval date, and the exact HTML preface version used.
5. Until resolved, mark this source chain as RIGHTS-UNRESOLVED / HOLD for redistribution and commercial-use planning.

The factual propositions in the Statistics Basics slice may still be independently checked against NIST and other suitable primary sources. This licence conflict does not invalidate the scientific content review, but it prevents treating the OpenStax source as cleared for reuse.

## 5. Impact on the first-edition candidate review

- The existing OpenStax Evidence Use for Statistics Basics Claim A remains a candidate for factual corroboration only, not a cleared reusable-text or asset source.
- Do not remove the NIST source or transfer its Evidence Use to OpenStax.
- Do not count this report as a new canonical Source, Evidence Use, candidate, INCLUDE decision, rights clearance, or publication approval.
- All three Statistics Basics Claims remain HOLD.
- The broader first-edition rights register must distinguish factual citation from copying/adaptation of protected expression and assets.

## 6. Change control

- Report-only review.
- No canonical JSON, Evidence Use, Source, Context, Scope, Claim, Relation, Decision, candidate master, allowlist, coverage manifest, reader, workflow or release state changed.
- No D/E/B score or INCLUDE/EXCLUDE decision assigned.
- No rights clearance inferred.
- No merge, deployment or public distribution performed.
- This documentation-only commit does not establish exact-head CI PASS; required checks must be evaluated on the resulting exact PR head.

## 7. Primary references

1. OpenStax, *Introductory Statistics 2e*, live HTML Preface: https://openstax.org/books/introductory-statistics-2e/pages/preface
2. OpenStax, *Introductory Statistics 2e*, official WEB PDF: https://assets.openstax.org/oscms-prodcms/media/documents/Introductory_Statistics_2e_-_WEB.pdf
3. OpenStax, textbook licensing and customization: https://help.openstax.org/s/article/Openstax-textbook-licensing-and-customization?language=en_US
4. OpenStax, licensing information for textbooks: https://help.openstax.org/s/article/Licensing-information-of-OpenStax-textbooks
