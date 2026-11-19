# Engineering and Computing Remediation Addendum — 2026-11-19

Date: 2026-11-19  
Authorization: `ENGINEERING-COMPUTING-REMEDIATION-001`  
Audit: `RELEASE/DOMAIN-AUDIT-ENGINEERING-AND-COMPUTING-2026-11-19.md`  
Branch: `mvp-public-contribution-design-2026-10-11`

## Result

Completed the bounded source, Claim, Evidence Use, Context and Scope remediation for all eight authorized Part II slices.

- **8 Source records** versioned with identifiable sources, stable editions where applicable, and exact source locators.
- **24 Claims** versioned and rewritten as substantive, falsifiable, source-bounded propositions.
- **24 Evidence Use records** versioned with claim-specific pinpoint locators and exact current Claim/Source references.
- **8 Context records** and **8 Scope records** versioned to state domain-specific assumptions and exclusions.
- **8 slice READMEs** updated to match the canonical records.
- **72 canonical records total** changed across the eight slices.
- All publication and completion states were preserved.
- All eight slices remain **HOLD** for first-edition selection.

The ordinary final versions are v2. In `civil-engineering-basics` and `databases-basics`, Source records were advanced to v3 during the sequential remediation; dependent Claims, Evidence Use, Context and Scope were then advanced to v3 to keep every versioned reference aligned. This was provenance/reference alignment only and did not change the final Claim wording after the substantive rewrite.

## Slice-level source and evidence map

| Slice | Canonical Source | Claim substance | Pinpoint Evidence Use |
|---|---|---|---|
| `mechanics-basics` | OpenStax University Physics Vol. 1, Chapter 5 | Newton's first, second and third laws | §§5.2, 5.3, 5.5 |
| `civil-engineering-basics` | ASCE CEBOK3 outcomes, official ASCE Committee on Education PDF | 21 outcomes; engineering fundamentals; technical outcomes | Q10–Q12, pp. 6–7; Appendix D, Table F-5, pp. 16–17 |
| `software-engineering-basics` | IEEE Computer Society SWEBOK Guide V4.0a | 18 knowledge areas; named KAs; general scope/limits of the Guide | Introduction to the Guide, pp. xxxvii–xli; Table I.1 |
| `computer-science-algorithms-basics` | Runestone Academy, Foundations of Python Programming | Algorithm definition; pseudocode; distinction between algorithm and program | §1.2 “Algorithms” |
| `databases-basics` | PostgreSQL 18.7 Documentation | RDBMS/relations; table-row-column structure; SELECT and JOIN | §§2.2–2.6 |
| `cybersecurity-basics` | NIST CSF 2.0, NIST CSWP 29 | Risk-management framework; six Core Functions; non-prescriptive nature | Abstract, pp. i–1; §2, pp. 3–5; Appendix A |
| `distributed-systems-basics` | van Steen & Tanenbaum, “A brief introduction to distributed systems” (2016) | Autonomous computing elements; coherent system; networked nodes | §1, pp. 968–969; §2, p. 969 |
| `artificial-intelligence-basics` | NIST AI RMF 1.0, NIST AI 100-1 | Risk-management outcomes; four functions; lifecycle continuity | §2, pp. 6–10; §5, pp. 19–21 |

## Reference integrity verification

Fetched the exact current canonical JSON records after the changes and checked all eight 9-record graphs.

For every slice:
- Source record is at its current version and contains an external source locator.
- Claims A–C point through `provenance.created_from` to the current Source version.
- Evidence Use A–C point to the current Claim and Source versions, with `provenance.created_from` aligned to the current Source and non-empty claim-specific locator text.
- Context and Scope point to the current Claim A version.
- No missing or mismatched version reference was found in this eight-slice verification.

This is a record-graph/reference check, not proof of all scientific or engineering truth and not a substitute for full exact-head CI.

## Rights and editorial limits

- Public accessibility is not treated as permission to redistribute source material.
- SWEBOK V4.0a explicitly permits limited educational/personal use under stated conditions and requires IEEE permission for commercial or promotional reproduction and certain collective works. No source text, figures or tables were copied into the Encyclopedia records. Rights review remains open.
- ASCE, NIST, PostgreSQL, OpenStax and Runestone source terms and attribution requirements still need the applicable release-level rights review.
- The distributed-systems article is identified as open access; its specific license and permitted reuse must still be checked before any reproduction beyond factual paraphrase and attribution.
- No source images, diagrams, tables or extended source text were copied.
- No engineering design, cybersecurity configuration, AI safety procedure or operational instruction was introduced.

## Decisions preserved

- `mechanics-basics`: HOLD
- `civil-engineering-basics`: HOLD
- `software-engineering-basics`: HOLD
- `computer-science-algorithms-basics`: HOLD
- `databases-basics`: HOLD
- `cybersecurity-basics`: HOLD
- `distributed-systems-basics`: HOLD
- `artificial-intelligence-basics`: HOLD

No first-edition allowlist was created or modified. No INCLUDE or EXCLUDE decision was made. No publication state was changed. No main-branch change, merge, deployment or release action was performed.

## Remaining work under the release plan

1. Resolve rights and attribution for every exact source/version.
2. Complete independent editorial review and Human View of the rendered reader presentation.
3. Run and pass all required checks on one exact final HEAD, including Reference implementation tests, Release Conformance Gate, Offline Edition and MVP Contribution Form Browser Tests.
4. Keep all eight slices HOLD until every applicable release gate is closed.
