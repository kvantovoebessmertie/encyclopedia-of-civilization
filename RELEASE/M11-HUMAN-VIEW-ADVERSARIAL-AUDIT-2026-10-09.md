# M11 Human View and Adversarial Audit — 2026-10-09

## Review method

Desk review of the three READMEs, Claims, Context/Scope and existing regressions from the perspective of a reader who does not know the record architecture. No live novice usability study or external human review is claimed.

## Findings

### M11-HV-001 — accessibility
The README is English-only while the Claims and Context/Scope are Russian-facing. It names the source and boundary but does not explain the core concept in Russian or make the international-framework/local-rules distinction discoverable. Add a concise Russian orientation and one bounded example (e.g., a service may be technically present but not independently usable if relevant barriers remain), explicitly marked illustrative rather than a legal or design test.

Adversarial risk: readers could mistake an international convention for a complete local technical standard or treat the general principle as certification of a specific building, service or digital interface.

### M11-HV-002 — ergonomics
The README is predominantly English. The three Claims are concise but do not provide an ordinary-reader orientation. Add a short Russian introduction explaining the fit between task demands and worker capabilities, and state that the slice is educational—not an individual medical assessment, workplace risk assessment or substitute for applicable occupational-safety procedures.

Adversarial risk: readers could treat general risk factors as a complete assessment or assume one intervention is appropriate for every worker and workplace.

### M11-HV-003 — human factors
The README is English-only. Add a Russian orientation explaining that people, tools/interfaces, environment and task conditions interact, with a boundary against treating NASA's spaceflight-oriented material as universal requirements for all systems.

Adversarial risk: readers could overgeneralize spaceflight/system-design examples to other domains or interpret general human-performance principles as a complete engineering standard.

## Regression implications

The existing dedicated tests mainly protect record counts, record types and linkage. Preserve those checks and add content-specific assertions for:
- distinct claim-specific Evidence Use descriptions;
- the confirmed Claim C boundaries;
- Russian-facing introductions and visible limits;
- absence of universal, site-specific or individualized advice.

## Limitation

This is a desk-based adversarial review. It does not establish that a novice user has successfully completed a task using the corpus.
