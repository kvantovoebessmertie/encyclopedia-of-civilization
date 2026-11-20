# CO heating / generator emergency-escalation Relation — current-head desk review

Date: 2026-11-20  
Inspection ref: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `302f1082f0b9de08b71553a80f59dbc9682c9a55`  
Disposition: report-only; preserve all canonical records and HOLD states.

## Exact records re-fetched

- `REL-CROSS-CO-EMERGENCY-ESCALATION@2`
- `CTX-REL-CROSS-CO-EMERGENCY-ESCALATION@1` → exact target Relation @2; reciprocal pair is coherent.
- Heating endpoint: `CLM-CO-HEATING-EMERGENCY@1`; Evidence Use `EU-CO-HEATING-EMERGENCY@1`; Source `SRC-CPSC-CO-ALARM-EMERGENCY-2026@1`.
- Generator endpoint: `CLM-GENERATOR-CO-ALARM-EMERGENCY@1`; Evidence Use `EU-GENERATOR-CO-ALARM-EMERGENCY@1`; Source `SRC-CDC-GENERATOR-CO-2026@1`.

The Relation participants, order, roles, undirected direction, type, provenance and publication/completion fields were read only and not changed.

## Semantic assessment

The two Claims state substantially the same emergency action: move immediately to fresh air, seek emergency/medical help, and do not re-enter before safety is confirmed. The heating Claim is sourced to CPSC's CO alarm guidance; the generator Claim is sourced to CDC generator/outage guidance. Their cross-slice relation is therefore a defensible contextual-navigation bridge between general residential CO alarm response and the generator-specific exposure context.

The overlap is also a potential duplication concern: the relation must not imply two independent emergency procedures or that the generator-specific case has a different first response. The distinct value is the source/context pathway (general household CO alarm vs generator/outage), not a materially different clinical instruction. A reviewer should verify that the generator source's exact page locator supports all wording in the generator Claim; the current EU material descriptions are summaries without pinpoint locators.

## Official source checks

1. CPSC, *Carbon Monoxide Questions and Answers / Carbon Monoxide Fact Sheet*: https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Carbon-Monoxide-Questions-and-Answers  
   The current CPSC fact sheet states that when a CO alarm sounds, occupants should move outside to fresh air, call emergency services/fire department, and not re-enter until responders give permission. It separately advises people with suspected symptoms to get outside immediately and seek medical attention. The canonical CPSC Q&A URL is retained as the source identity for the heating Claim.
2. CDC, *What to Do to Protect Yourself During a Power Outage / Generator Safety*: https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html  
   The existing canonical Source identifies this page. A separate CDC/NIOSH CO hazards page also supports moving to fresh air and seeking medical help immediately when symptoms occur: https://www.cdc.gov/niosh/carbon-monoxide/about/index.html

The external CPSC fact sheet was retrieved during this review and directly confirms the alarm-response elements. The current canonical Evidence Use records do not contain section/heading-level pinpoint locators, so this review does not certify every clause of either Claim from the existing EUs alone.

## Rights / editorial boundary

This review records source identity and short factual paraphrase only; it does not copy source text. No item-level reuse licence or project-wide distribution compatibility is established here. Rights review, independent emergency/clinical subject-matter review, and Human View remain separate gates.

## Disposition and next action

- Keep `REL-CROSS-CO-EMERGENCY-ESCALATION@2`, its Context @1, both Claims @1, both Evidence Uses @1, both Sources @1, and the affected slices on HOLD.
- No endpoint substitution, Claim rewrite, Source/Evidence Use versioning, publication-state change, allowlist or release decision is authorized by this desk review.
- Recommended bounded follow-up: an independent reviewer confirms (a) equivalence of immediate protective action, (b) distinct educational value of cross-navigation, and (c) exact CDC locator for generator-specific emergency advice. If accepted, retain the Relation as navigation only and add exact locators only under explicit record-level authorization.
- No canonical JSON or implementation file was changed. No CI result is claimed for this documentation-only report.
