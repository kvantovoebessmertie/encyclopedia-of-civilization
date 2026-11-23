# M13 bounded correction authorization — cross-queue OpenStax Evidence Use pinpoints

Date: 2026-11-15
Authorization ID: M13-CROSS-QUEUE-OPENSTAX-EU-001
Branch: `m13-system-wide-depth-audit-2026-10-09`
Basis HEAD: `d60a9db44ca7a344834c83036f7adf8b651d211d`

## Finding

The cross-queue review identified ten Claims whose Claim→Evidence Use→Source IDs and versions are internally consistent, but whose Evidence Use descriptions are generic textbook references rather than reproducible, claim-specific source locations. Direct review of the linked OpenStax books identified suitable sections for all ten propositions. The authorized correction is limited to versioning the ten existing Evidence Use records with exact section locators and bounded paraphrased descriptions.

## Exact authorized Evidence Use changes

On the named M13 branch only, version each listed Evidence Use from v1 to v2. Change only `record_version` and `content.material.description`. Preserve record ID/type, Claim and Source references (both remain v1), evidence role, provenance, publication/completion status, schema and every other field.

1. `CONTENT/vertical-slices/cell-basics/records/EU-CELL_BASICS-A.json`
   - Claim: `CLM-CELL_BASICS-A@1`; Source: `SRC-CELL_BASICS@1`
   - Pinpoint: OpenStax Biology 2e §4.1, “Studying Cells”, https://openstax.org/books/biology-2e/pages/4-1-studying-cells
   - Limit: supports cells as the basic building blocks/unit of living organisms; do not imply this section is a complete account of all cell functions.

2. `CONTENT/vertical-slices/cell-basics/records/EU-CELL_BASICS-B.json`
   - Claim: `CLM-CELL_BASICS-B@1`; Source: `SRC-CELL_BASICS@1`
   - Pinpoints: OpenStax Biology 2e §§4.2–4.3, “Prokaryotic Cells” and “Eukaryotic Cells”, https://openstax.org/books/biology-2e/pages/4-2-prokaryotic-cells and https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells
   - Limit: supports absence of a membrane-bound nucleus in prokaryotes and presence of a membrane-bound nucleus in eukaryotes; preserve the biological distinction and do not generalize other cell features.

3. `CONTENT/vertical-slices/computing-basics/records/EU-COMPUTING_BASICS-A.json`
   - Claim: `CLM-COMPUTING_BASICS-A@1`; Source: `SRC-COMPUTING_BASICS@1`
   - Pinpoint: OpenStax Introduction to Computer Science §5.1, “Computer Systems Organization”, https://openstax.org/books/introduction-computer-science/pages/5-1-computer-systems-organization
   - Limit: supports hardware/software components and the processing of programs with data; do not imply every computer architecture has an identical component set.

4. `CONTENT/vertical-slices/computing-basics/records/EU-COMPUTING_BASICS-B.json`
   - Claim: `CLM-COMPUTING_BASICS-B@1`; Source: `SRC-COMPUTING_BASICS@1`
   - Pinpoint: OpenStax Introduction to Computer Science §3.2, “Algorithm Design and Discovery”, https://openstax.org/books/introduction-computer-science/pages/3-2-algorithm-design-and-discovery
   - Limit: supports an algorithm as a sequence of precise instructions mapping input to output; do not imply all algorithms are necessarily implemented as a literal linear list.

5. `CONTENT/vertical-slices/computing-basics/records/EU-COMPUTING_BASICS-C.json`
   - Claim: `CLM-COMPUTING_BASICS-C@1`; Source: `SRC-COMPUTING_BASICS@1`
   - Pinpoint: OpenStax Introduction to Computer Science §5.1, “Computer Systems Organization”, https://openstax.org/books/introduction-computer-science/pages/5-1-computer-systems-organization
   - Limit: supports programs and corresponding data being stored as sequences of bits/bytes in conventional electronic computers; avoid implying this description covers all emerging or non-classical computing models.

6. `CONTENT/vertical-slices/constitutional-systems-basics/records/EU-CONSTITUTIONAL_SYSTEMS_BASICS-B.json`
   - Claim: `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-B@1`; Source: `SRC-CONSTITUTIONAL_SYSTEMS_BASICS@1`
   - Pinpoint: OpenStax Introduction to Political Science §10.1, “Democracies: Parliamentary, Presidential, and Semi-Presidential Regimes”, and Chapter 10 Key Terms, https://openstax.org/books/introduction-political-science/pages/10-1-democracies-parliamentary-presidential-and-semi-presidential-regimes and https://openstax.org/books/introduction-political-science/pages/10-key-terms
   - Limit: supports the textbook's definition of parliamentary regimes in which the chief executive is selected by the legislature and is a member of it; preserve this as a comparative-politics definition, not a claim that every country uses an identical constitutional procedure.

7. `CONTENT/vertical-slices/constitutional-systems-basics/records/EU-CONSTITUTIONAL_SYSTEMS_BASICS-C.json`
   - Claim: `CLM-CONSTITUTIONAL_SYSTEMS_BASICS-C@1`; Source: `SRC-CONSTITUTIONAL_SYSTEMS_BASICS@1`
   - Pinpoint: OpenStax Introduction to Political Science §10.1 and Chapter 10 Key Terms, URLs as listed above.
   - Limit: supports the basic division of executive power between a president and prime minister in semi-presidential regimes; retain the source's caveat that arrangements and authority vary across countries.

8. `CONTENT/vertical-slices/matter-basics/records/EU-MATTER_BASICS-A.json`
   - Claim: `CLM-MATTER_BASICS-A@1`; Source: `SRC-MATTER_BASICS@1`
   - Pinpoints: OpenStax Chemistry 2e §§1.1–1.3, “Chemistry in Context”, “Phases and Classification of Matter”, and “Physical and Chemical Properties”, https://openstax.org/books/chemistry-2e/pages/1-1-chemistry-in-context, https://openstax.org/books/chemistry-2e/pages/1-2-phases-and-classification-of-matter, and https://openstax.org/books/chemistry-2e/pages/1-3-physical-and-chemical-properties
   - Limit: §1.2 supports classification as elements, compounds and mixtures; §1.1 and §1.3 support composition and properties. Do not imply the three categories exhaust all possible material classifications or phases.

9. `CONTENT/vertical-slices/political-science-basics/records/EU-POLITICAL_SCIENCE_BASICS-B.json`
   - Claim: `CLM-POLITICAL_SCIENCE_BASICS-B@1`; Source: `SRC-POLITICAL_SCIENCE_BASICS@1`
   - Pinpoint: OpenStax Introduction to Political Science §1.5, “Empirical Political Science”, https://openstax.org/books/introduction-political-science/pages/1-5-empirical-political-science
   - Limit: supports empirical inquiry through observable/verifiable facts, evidence and hypothesis testing; it does not imply that political facts are always easy to observe or uncontested.

10. `CONTENT/vertical-slices/political-science-basics/records/EU-POLITICAL_SCIENCE_BASICS-C.json`
    - Claim: `CLM-POLITICAL_SCIENCE_BASICS-C@1`; Source: `SRC-POLITICAL_SCIENCE_BASICS@1`
    - Pinpoints: OpenStax Introduction to Political Science §§1.4–1.5, “Normative Political Science” and “Empirical Political Science”, https://openstax.org/books/introduction-political-science/pages/1-4-normative-political-science and https://openstax.org/books/introduction-political-science/pages/1-5-empirical-political-science
    - Limit: supports the distinction between empirical/descriptive questions about what is and normative questions about what ought to be; do not imply the two modes of inquiry can never inform one another.

## Authorized supporting files

- Update only the five slice READMEs listed below to record the exact section pinpoints and scope boundaries:
  - `CONTENT/vertical-slices/cell-basics/README.md`
  - `CONTENT/vertical-slices/computing-basics/README.md`
  - `CONTENT/vertical-slices/constitutional-systems-basics/README.md`
  - `CONTENT/vertical-slices/matter-basics/README.md`
  - `CONTENT/vertical-slices/political-science-basics/README.md`
- Strengthen only the five dedicated slice tests:
  - `REFERENCE/tests/test_content_cell_basics_vertical_slice.py`
  - `REFERENCE/tests/test_content_computing_basics_vertical_slice.py`
  - `REFERENCE/tests/test_content_constitutional_systems_basics_vertical_slice.py`
  - `REFERENCE/tests/test_content_matter_basics_vertical_slice.py`
  - `REFERENCE/tests/test_content_political_science_basics_vertical_slice.py`
- Register this authorization and exactly these five slices in `RELEASE/EDITORIAL-CORRECTION.json`.
- Add one M13 checkpoint document recording the source review, exact changes, exclusions and verification state.

## Explicit exclusions

No Claim wording/version/type, Source identity/version/URI, Context, Scope, Relation, risk metadata, D/E/B score, rights clearance, publication approval, coverage count, schema, release allowlist, unrelated file/slice, `main`, or PR merge change is authorized. No new/deleted Record is authorized; each slice remains at nine records. This authorization establishes neither independent evidence corroboration nor final semantic/risk assessment. OpenStax pages also state that the books may not be used to train language models or otherwise be ingested into LLMs or generative-AI offerings without prior written permission. This is a material rights blocker for an AI-enabled knowledge system: all five affected slices remain RIGHTS HOLD for any LLM/generative-AI ingestion or public-edition reuse unless written permission is obtained or the source is replaced with a rights-compatible alternative. CC BY-NC-SA non-commercial/share-alike and attribution conditions also require separate review. The metadata correction itself does not authorize ingestion or publication.

## Acceptance

Run the dedicated tests, content preflight, full Reference Tests, Release Conformance Gate and Offline Edition on one identical final HEAD. Independently verify exact field-level diffs, all ten EU→Claim/Source references, five unchanged nine-record slice counts, unchanged Claim statements and Source records, and unchanged `main`. Keep PR #21 Draft/unmerged. M13 remains OPEN / NOT RELEASE-READY.
