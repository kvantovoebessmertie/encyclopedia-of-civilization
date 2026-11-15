# M13 cross-queue OpenStax Evidence Use pinpoint checkpoint

Date: 2026-11-15
Branch: `m13-system-wide-depth-audit-2026-10-09`
Authorization: `M13-CROSS-QUEUE-OPENSTAX-EU-001`
Basis HEAD: `d60a9db44ca7a344834c83036f7adf8b651d211d`
State: **10 Evidence Use records versioned with claim-specific locators; exact-head verification pending**

## Finding

The cross-queue screen identified ten Claims whose Claim→Evidence Use→Source references were internally consistent but whose Evidence Use descriptions were generic textbook-level references. Direct inspection of the exact OpenStax sections confirmed suitable support for the bounded propositions. The correction versions only the ten existing Evidence Use descriptions and preserves their Claim/Source v1 references.

## Passage review and bounded dispositions

- Cell A: Biology 2e §4.1 supports cells as the basic unit/building blocks of living organisms.
- Cell B: Biology 2e §§4.2–4.3 directly distinguish prokaryotes without a membrane-bound nucleus from eukaryotes with one.
- Computing A: Introduction to Computer Science §5.1 supports hardware/software components and programs operating on data.
- Computing B: §3.2 defines an algorithm as precise instructions mapping input to output.
- Computing C: §5.1 describes conventional electronic computer storage of programs and data as bits/bytes; non-classical computing models are excluded from the generalization.
- Constitutional Systems B: §10.1 and Chapter 10 Key Terms support the textbook's parliamentary-regime definition: chief executive selected by legislature and member of it.
- Constitutional Systems C: §10.1 and Chapter 10 Key Terms support the basic split between president and prime minister in semi-presidential regimes; the source notes cross-country variation.
- Matter A: Chemistry 2e §§1.1–1.3 cover composition, classification as elements/compounds/mixtures, and physical/chemical properties.
- Political Science B: §1.5 supports empirical political inquiry through verifiable facts, evidence and hypothesis testing.
- Political Science C: §§1.4–1.5 distinguish normative “what should be” from empirical “what is” questions.

## Exact changes

- Versioned ten existing Evidence Use records v1→v2, changing only `record_version` and `content.material.description`.
- Updated five slice READMEs with the exact source sections and support boundaries.
- Strengthened five dedicated slice tests to assert Evidence Use v2, exact Claim/Source v1 references, locator markers, unchanged Claim statements and existing slice structure.
- Registered the bounded authorization in `RELEASE/EDITORIAL-CORRECTION.json`.
- Added the exact authorization and this checkpoint.

No Claim wording/version, Source record/version/URI, Context, Scope, Relation, risk metadata, D/E/B score, record count, schema, or release allowlist was changed. Each slice remains at nine records.

## Rights and assessment limitations

OpenStax book pages identify a CC BY-NC-SA license. This metadata correction and paraphrased locator descriptions do not constitute rights clearance for a public edition. Non-commercial/share-alike compatibility, attribution and any commercial-use restrictions require a separate rights review. A single textbook per slice does not establish independent evidence corroboration. No final D/E/B or risk assessment is assigned, and no Claim is cleared for publication by this checkpoint.

## Verification still required

Run dedicated regressions, content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact field-level diffs, all ten Claim/Source links, unchanged Claims and Sources, five unchanged nine-record slice counts, unchanged `main`, and PR #21 Draft/unmerged. M13 remains OPEN / NOT RELEASE-READY.
