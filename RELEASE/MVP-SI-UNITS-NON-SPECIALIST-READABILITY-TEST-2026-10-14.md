# MVP SI Units — Non-Specialist Readability Test — 2026-10-14

Status: **protocol prepared; no participant testing has been performed and no readability PASS is claimed**.

## Purpose

Check whether a reader without prior SI/metrology expertise can correctly explain the two conditional pilot Claims and their limitations. This is a comprehension check, not a factual source review, rights decision, expert review, or release approval.

## Materials and version control

- Claim A: `CLM-SI-SEVEN-BASE@1` and Evidence Use `EU-SI-SEVEN-BASE@2`.
- Claim B: `CLM-SI-DERIVED@1` and Evidence Use `EU-SI-DERIVED@2`.
- Source: `SRC-NIST-SI-UNITS@1`, NIST “SI Units”.
- Test only the exact displayed text and reader interface from one pinned preview build. Record the preview source revision, builder/policy versions, artifact hash, and the exact Claim/Evidence Use/Source versions shown.
- Do not add the claims to a release allowlist just to run this test. If the real-record preview gate is not ready, use a clearly labelled private paper/mock-up test and do not describe it as a renderer test.

## Participant and privacy

- Recruit 3 readers who have not worked on the repository and do not routinely work in metrology or standards. One reader can provide an early signal but is not enough for a strong usability conclusion.
- Do not collect names, contact details, employer, health information, or other unnecessary personal data. Use anonymous labels R1–R3 and retain only task responses and observed confusion.
- Give no explanation of the intended answers before the test. Ask the reader to think aloud only if it does not lead them toward the answer.

## Tasks and neutral prompts

### Claim A — seven base units

Show the exact candidate text and its source/evidence navigation, then ask:

1. “In your own words, what is this statement saying?”
2. “What is the difference, if any, between the seven base units and the defining constants?”
3. “Where would you look to check this statement, and what part of the source would you use?”

Expected comprehension signal: the reader distinguishes the seven base units from the defining constants and understands that the definitions are expressed using fixed values of defining constants. Do not count memorized repetition without a correct distinction as a pass.

### Claim B — derived units

Show the exact candidate text and its source/evidence navigation, then ask:

1. “What does the number 22 refer to here?”
2. “Does this statement say that SI has only 22 derived units in total? Why or why not?”
3. “How would you verify the qualification in the cited source?”

Expected comprehension signal: the reader understands that 22 refers specifically to derived units with special names and symbols, not to all possible SI derived units.

## Observation rubric

For each task, record only:

- **Correct unaided** — the reader explains the intended distinction without a hint.
- **Correct after navigation** — the reader resolves it by using the linked Evidence Use/Source.
- **Misunderstood** — the reader gives an incompatible interpretation or cannot locate the supporting passage.
- The exact phrase, label, link or navigation step that caused confusion.

Do not infer a general population success rate from this small sample.

## Acceptance and remediation

- Both distinctions must be explained correctly by all three readers without the moderator supplying the answer.
- At least two readers must independently locate the relevant source section using the interface.
- Any interpretation of “22” as the total number of derived units is a blocker: revise the visible wording/qualification and repeat the affected task.
- If readers cannot distinguish base units from defining constants, revise the Claim gloss and repeat the task.
- If source navigation or review-state labels are missed or misunderstood, fix the interface and repeat the relevant task.
- Record failures as findings, not participant shortcomings. Do not silently rewrite the test criteria after seeing responses.

## Result record — intentionally blank

| Reader | Claim A comprehension | Claim A source navigation | Claim B “22” distinction | Claim B source navigation | Confusion / evidence |
|---|---|---|---|---|---|
| R1 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| R2 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |
| R3 | NOT RUN | NOT RUN | NOT RUN | NOT RUN | — |

Final disposition: **NOT RUN / NOT APPROVED** until observations, resulting revisions, and the exact tested artifact revision are recorded.

## Boundary

This protocol does not approve a real-record allowlist, publication, hosting, public intake, or the third Claim `CLM-SI-ACCURACY-BOUNDARY@1`. Rights/attribution, editorial ownership, operational policy, technical release checks and the other publication gates remain separate blockers.
