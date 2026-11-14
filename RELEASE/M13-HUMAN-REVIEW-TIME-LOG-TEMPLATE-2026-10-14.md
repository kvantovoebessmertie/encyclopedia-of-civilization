# M13 human review effort log — template

**Status: TEMPLATE ONLY — no review-time observations recorded here.**

Purpose: measure human effort required to review a 100-Claim batch separately from machine pipeline runtime. Do not claim a speedup until comparable baseline data exists.

## Batch identity

- Batch / worklist ID:
- Exact source commit SHA:
- Exact worklist file and hash:
- Review protocol version:
- Reviewer role(s) (use role labels, not personal details):
- Start date:
- Completion date:
- Total Claims assigned:
- Claims with completed review:
- Claims deferred / blocked:
- Independent reviewer used: YES / NO
- Notes on changes to scope or protocol:

## Per-session log

Record active work time, not elapsed calendar time. Pause the timer during breaks, unrelated work, and waiting for external replies. Use one row per uninterrupted review session.

| Session | Reviewer role | Lane / Claim range | Start (local time) | End (local time) | Active minutes | Claims touched | Claims completed | Blocked / deferred | Reason / short note |
|---|---|---|---|---|---:|---:|---:|---:|---|
| NOT RECORDED | | | | | | | | | |

## Review outcome summary

| Measure | Value |
|---|---|
| Total active human-review minutes | NOT MEASURED |
| Claims with a completed D/E/B assessment | NOT MEASURED |
| Claims requiring source retrieval or pinpoint verification | NOT MEASURED |
| Claims escalated for specialist review | NOT MEASURED |
| Claims blocked by missing/ambiguous source identity | NOT MEASURED |
| Claims requiring contradiction or independence adjudication | NOT MEASURED |
| Rework minutes after independent review | NOT MEASURED |
| Median active minutes per completed Claim | NOT MEASURED |
| Total machine pipeline runtime for same commit | Populate from m13-runtime-metrics.json |
| Comparable historical/manual baseline | NOT AVAILABLE UNTIL DOCUMENTED |

## Quality guardrails

- A Claim is completed only when its evidence chain and required D/E/B judgement have been checked under the active protocol; merely opening a record or filling a provisional field is not completion.
- Do not treat the number of machine-generated packets as the number of reviewed Claims.
- Record source edition, pinpoint, context, rights, evidence independence, contradictions, and specialist escalations where applicable.
- Keep provisional review distinct from final review. Never overwrite canonical records from this log.
- Do not compare batches if the protocol, Claim risk mix, evidence complexity, or reviewer experience materially differs without documenting the limitation.
- Report throughput and quality together. Faster completion is not an improvement if error rate, unresolved blockers, or rework rises.
- Do not publish reviewer-identifying or sensitive personal data in the repository.

## Comparison decision

**Current decision: NOT EVALUATED.** A speedup claim requires:
1. at least one recorded batch under the current workflow;
2. a comparable, documented baseline;
3. comparable scope and protocol, with differences disclosed;
4. active human-review time and rework included;
5. quality / independent-review outcomes considered alongside throughput.

- Comparison owner:
- Comparison date:
- Conclusion:
- Limitations:
