# M13 Batch 41 — Evidence-Linkage Checkpoint 7 — 2026-10-11

## Scope and gate
Diagnostic review of Architecture Basics Claims A–C. Verified Claim record types/internal IDs, Evidence Use pointers, stored Source identity/URI, and the linked Encyclopaedia Britannica article. No D/E/B scores assigned; no content records modified. Batch 41 remains open.

## Findings

### A — `CLM-ARCHITECTURE_BASICS-A`
- Claim: “Архитектура объединяет проектирование и организацию пространственной среды, зданий и сооружений с учётом функциональных, эстетических и технических требований.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHITECTURE_BASICS-A` points to the intended Claim and `SRC-ARCHITECTURE_BASICS`; role `supports`.
- The Britannica architecture article's definition describes architecture as the art and technique of designing and building, serving practical/utilitarian and expressive/aesthetic ends. This supports the functional + aesthetic/design core. “Organization of spatial environment” and the full phrase “technical requirements” are not directly established by the source excerpt reviewed.
- **Disposition:** partial-to-strong source fit for the core definition; remaining clauses are broader synthesis and need specific source support or careful qualification. Evidence Use description supplies no pinpoint locator.

### B — `CLM-ARCHITECTURE_BASICS-B`
- Claim: “Для интерпретации сведений по срезу необходимо учитывать источник, контекст и ограничения применимости.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHITECTURE_BASICS-B` structurally points to the intended Claim and Source; role `supports`.
- The cited Britannica article explains architecture and its practical/expressive dimensions; it does not substantiate this general rule about evaluating claims or interpreting this repository slice.
- **Disposition:** substantive evidence mismatch/category error. This reads as a cross-cutting evidence-evaluation policy, not an architecture fact. It needs an appropriate epistemology/source-evaluation reference or an explicitly scoped corpus policy, subject to authorized correction.

### C — `CLM-ARCHITECTURE_BASICS-C`
- Claim: “Обобщённые сведения среза не заменяют специализированную проверку там, где вывод зависит от условий, измерений или профессиональной оценки.”
- Identity: `record_type=claim`; internal `record_id` matches filename.
- Evidence Use `EU-ARCHITECTURE_BASICS-C` structurally points to the intended Claim and Source; role `supports`.
- The Britannica overview does not establish this warning about specialized checking, measurement, or professional assessment.
- **Disposition:** substantive evidence mismatch/category error. The statement is a general scope/safety limitation, not a supported proposition about architecture as such. It needs a domain-specific reference or explicit corpus policy, subject to authorized correction.

## Structural and metadata observations
- All three Claim IDs match filenames; all Claim → Evidence Use → Source references resolve correctly.
- All Evidence Use descriptions are generic (“source is used within the stated material”) and provide no actual passage locator. Structural validity must not be confused with substantive support.
- Stored Source URI https://www.britannica.com/art/architecture is the intended public Britannica article.
- Claims B and C resemble the cross-slice template/policy classification concern observed in Anthropology Basics. This is a repeated corpus-level pattern worth tracking in the global ledger, not permission to alter records.
- No D/E/B scores assigned. No content JSON changed. Any reclassification, source change, or wording correction must wait for a separately authorized correction scope.

## Public source consulted
- Encyclopaedia Britannica, “Architecture”: https://www.britannica.com/art/architecture
