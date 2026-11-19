# Human Sciences Remediation Addendum — 2026-11-19

Date: 2026-11-19  
Authorization: `HUMAN-SCIENCES-REMEDIATION-001`  
Audit: `RELEASE/DOMAIN-AUDIT-HUMAN-SCIENCES-2026-11-19.md`  
Branch: `mvp-public-contribution-design-2026-10-11`

## Result

Completed the bounded remediation for the three authorized Human Sciences slices.

- **3 Source records** versioned to exact source identities and pinpoint locators.
- **9 Claims** versioned; psychology's three editorial/meta Claims replaced with factual propositions, neuroscience Claims narrowed to the NINDS primer, and developmental-biology Claims rewritten to exact animal embryology/organogenesis material.
- **9 Evidence Use records** versioned with claim-specific locators and exact current Claim/Source references.
- **3 Context records** and **3 Scope records** versioned to define the domain boundaries and exclude clinical overreach.
- **3 slice READMEs** updated.
- **27 canonical records total** changed across the three slices.
- Publication and completion states were preserved.
- All three slices remain **HOLD** for first-edition selection.

## Source and evidence map

| Slice | Canonical Source | Claim substance | Pinpoint Evidence Use |
|---|---|---|---|
| `psychology-basics` | APA Dictionary of Psychology, entry “psychology”, updated 2026-03-06 | Definition of psychology; research methods; research branches | Entry “psychology”, definition 1 |
| `neuroscience-basics` | NINDS, *Know Your Brain*, NIH Publication No. 23-NS-3440a (Nov. 2023) | Brain functions; neuron as functional unit; dendrite/cell-body/axon signaling | Introduction, p. 1; “The Neuron”, p. 4 |
| `developmental-biology-basics` | OpenStax Biology 2e, Chapter 43 | Fertilization; cleavage/gastrulation/germ layers; organogenesis/differentiation/signaling | §§43.6 and 43.7 |

## Reference integrity verification

The remediation versions the full 9-record graph in each slice. Each Claim's provenance points to the current Source version; each Evidence Use points to the current Claim and Source versions and contains a non-empty pinpoint locator; Context and Scope target the current Claim A version. Publication and completion states are unchanged.

This is a record-graph check, not proof of all scientific truth or publication eligibility.

## Rights and editorial boundaries

- APA Dictionary of Psychology is copyrighted by the American Psychological Association. Records contain factual paraphrases and attribution only; no dictionary text is reproduced. Rights clearance remains open.
- The NINDS primer is a public educational publication. No source diagrams or images are copied. Any separately credited third-party material requires separate rights review.
- OpenStax Biology 2e is licensed CC BY-NC-SA, and its page carries additional restrictions on LLM training/ingestion and commercial reuse. No source text, table, figure or diagram is reproduced. The release team must assess the exact planned use and license obligations before any publication.
- Public availability is not treated as permission to redistribute source material.

## Decisions preserved

- `psychology-basics`: HOLD
- `neuroscience-basics`: HOLD
- `developmental-biology-basics`: HOLD

No first-edition allowlist was created or modified. No INCLUDE or EXCLUDE decision was made. No publication state was changed. No main-branch change, merge, deployment or release action was performed.

## Remaining release work

1. Complete source-specific rights and attribution review, including the OpenStax terms.
2. Complete independent editorial review and Human View of the rendered reader presentation.
3. Run and pass all required checks on one exact final HEAD: Reference implementation tests, Release Conformance Gate, Offline Edition and MVP Contribution Form Browser Tests.
4. Keep all three slices HOLD until every applicable release gate is closed.
