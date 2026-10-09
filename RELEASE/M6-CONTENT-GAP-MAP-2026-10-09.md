# M6 Content Gap Map — 2026-10-09

## Purpose and protected baseline

M5 CLEAN is accepted at checkpoint `c911c6b4ad791cb933293608e298e318a608a02f` after Reference implementation tests, Release Conformance Gate, and Offline Edition all passed on that exact HEAD.

M6 is an isolated planning/audit branch. M4 and M5 are not reopened or modified; `main` is not changed by this map.

Corpus scan at the M5 checkpoint:
- 479 vertical slices
- 4,754 Records
- 19 Record types
- 601 Sources
- 1,634 Evidence Use
- 64 Relations

The structural scan of `CONTENT/vertical-slices/*/records/*.json` counted 4,754 record files across 479 slices. Distribution by per-slice record count:

| Records per slice | Slice count |
|---:|---:|
| 7 | 1 |
| 9 | 366 |
| 10 | 11 |
| 11 | 20 |
| 12 | 30 |
| 13 | 28 |
| 14 | 1 |
| 15 | 16 |
| 16 | 3 |
| 17 | 1 |
| 22 | 1 |
| 58 | 1 |

A 9-record profile is a screening signal, not a quality verdict, quota, or automatic authorization to expand. Candidate choice must consider claim substance, source-to-claim fit, evidence independence, consequence, Context/Scope, Human View risk, existing cross-domain links, and prior maturation.

## Prior-maturation exclusions

Do not reopen the targets already matured under M1–M5. In particular, the M1, M2 and M3 scope locks are retained as closed history; M4's six targets and M5's nine targets are also excluded from M6 candidate selection. Do not duplicate the prior emergency, water, infrastructure, energy-system, materials, manufacturing, transportation, supply-chain, environmental-engineering, or telecommunications maturation work.

## Candidate screen for M6 verification

The following six existing slices form a *candidate verification set only*. No content change is authorized by this Gap Map.

| Candidate | Initial signal | Why verify | Principal audit concern |
|---|---|---|---|
| `sleep-basics` | 9 Records / 1 Source | Broad human-health relevance and reuse across learning, health, and daily functioning | A single NHLBI/NIH source supports introductory claims; check claim-specific coverage, evidence independence, and medical boundaries |
| `learning-basics` | 9 / 1 | Foundational knowledge with links to education and cognition | Current source is the NIMH Learning and Memory Program; verify that its neuroscience focus adequately supports every general learning claim |
| `law-basics` | 9 / 1 | Important for interpreting rules, rights, institutions, and jurisdiction | Current Cornell LII/Wex source is a US-law teaching example; jurisdiction and date boundaries must remain explicit |
| `demography-basics` | 9 / 1 | Useful for understanding population change, planning, and historical/social context | UN World Population Prospects is authoritative for projections; check source coverage, reference dates, and observation-versus-projection distinction |
| `governance-basics` | 9 / 1 | Cross-domain relevance to public policy, institutions, and collective decisions | OECD framework may represent one policy framework rather than all governance arrangements; avoid universalization |
| `education-systems` | 9 / 1 | High reuse across human development, institutions, and public policy | UNESCO right-to-education framing may not independently support every system-level claim; jurisdiction and period matter |

## Screened but not selected for this candidate set

- `nutrition-basics`: its current structure is already beyond the 9-record/one-source profile and includes additional claims/evidence; record count alone does not justify reopening it. Reconsider only if a specific unresolved substantive or evidence defect is found.
- `mental-health-information-boundaries`: it already has a more developed evidence structure, including an additional NIMH source. Do not select it solely because it is high consequence; a separate verified debt would be needed.

These are preliminary structural decisions, not assertions that either slice is fully mature or factually exhaustive.

## Next step

Perform candidate verification on all six proposed slices before scope lock:
1. read every Claim, Source, Evidence Use, Context, and Scope record;
2. verify source identity, locator, and claim-level relevance;
3. review existing Relations and prior audit history;
4. assess substantive depth and uncertainty/applicability boundaries;
5. decide include/exclude with a documented reason for each candidate.

Only after this verification may M6 lock its scope. The subsequent sequence is: scope lock → substantive audit → evidence-independence audit → Human View/adversarial audit → Relation audit → unified Debt Map → controlled correction → post-correction re-audit → registry/coverage/regressions → exact-HEAD Reference + Release Gate + Offline CI → CLEAN checkpoint.

## Non-negotiable rules

- No new Record type.
- No fixed Record/Claim/Source quota.
- No Relations added for metric growth.
- No content edits authorized by this map alone.
- No weakened tests, schema, semantic rules, or conformance.
- Do not merge or promote M6 based on this planning artifact.
- Keep M4 and M5 checkpoints protected.
