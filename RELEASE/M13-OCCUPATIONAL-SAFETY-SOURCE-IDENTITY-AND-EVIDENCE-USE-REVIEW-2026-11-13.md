# M13 — occupational-safety-basics source identity and Evidence Use review

Date: 2026-11-13
Branch: `m13-system-wide-depth-audit-2026-10-09`
Baseline: `38d121de86acc67cdf7ebdbd231733947ff245f5`
Status: noncanonical audit correction/proposal only; no canonical edits or editorial authorization.

## 1. Why this follow-up was necessary

The 2026-11-12 report `M13-EVIDENCE-LOCATOR-REVIEW-ENVIRONMENTAL-HEALTH-OCCUPATIONAL-SAFETY-DISASTER-2026-11-12.md` labels EU-OSHA OSHwiki, “OSH in general”, as the canonical source for the three occupational-safety Claims and proposes EU-OSHA line locators.

The current canonical slice does not point to EU-OSHA. Its actual Source record is:

- `SRC-OCCUPATIONAL_SAFETY_BASICS@1`
- Identity: “ILO — Safety and Health at Work”
- URI: `https://www.ilo.org/safework/`

The ILO URI currently redirects to the ILO “Safety and health at work” topic portal. The EU-OSHA OSHwiki page is a different institution, author and publication. Its passages cannot be inserted into the current ILO Evidence Use records as though they were passages from the linked Source.

This is a source-identity/reproducibility discrepancy in the prior audit report, not merely a missing locator. The EU-OSHA page may be a useful candidate source, but it is not part of the current canonical evidence chain.

## 2. Current canonical record inspection

Slice: `CONTENT/vertical-slices/occupational-safety-basics`

Claims:
- `CLM-OCCUPATIONAL_SAFETY_BASICS-A@1`
- `CLM-OCCUPATIONAL_SAFETY_BASICS-B@1`
- `CLM-OCCUPATIONAL_SAFETY_BASICS-C@1`

Evidence Uses:
- `EU-OCCUPATIONAL_SAFETY_BASICS-A@1`
- `EU-OCCUPATIONAL_SAFETY_BASICS-B@1`
- `EU-OCCUPATIONAL_SAFETY_BASICS-C@1`

Source:
- `SRC-OCCUPATIONAL_SAFETY_BASICS@1`

All three current Evidence Use descriptions are generic and repeat the same sentence. Each links to the ILO Source @1, but none identifies a page section, paragraph, chapter or page.

Additional Claim defect:
- Claim A currently ends with the literal suffix `(occupational-safety-basics).`
- This appears to be an editorial/source-generation residue, not part of the proposition.
- Do not remove it without a separate, explicit versioned Claim correction authorization and regression.

## 3. Direct check of the existing ILO Source

Current ILO page:
- Title: “Safety and health at work”
- URI in the canonical Source: `https://www.ilo.org/safework/`
- Current redirect destination: `https://www.ilo.org/topics-and-sectors/safety-and-health-work`

The opening body paragraphs under “Safety and health at work” state that occupational safety and health concerns protecting lives, preventing harm and ensuring safe and dignified work; the following paragraph describes ILO work with governments, employers and workers to improve safety and health at national, sectoral and workplace levels.

This is direct support for the broad purpose in Claim A and useful context for the multilevel scope in Claim C. It does not, by itself, provide the detailed risk-identification/control process or worker-participation system claimed in B.

## 4. A more directly relevant ILO publication discovered

The existing ILO topic portal links to a separate official publication:

- International Labour Organization, *Guidelines on occupational safety and health management systems (ILO-OSH 2001)*.
- Official publication landing page: `https://www.ilo.org/publications/guidelines-occupational-safety-and-health-management-systems-ilo-osh-2001`
- Official PDF: `https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@dgreports/@dcomm/@publ/documents/publication/wcms_publ_9221116344_en.pdf`

The publication is a separate Source identity and is not currently represented by a Source record in this slice.

Verified PDF passages (PDF page numbers and section labels):

- **p. 1, §1.2(a)–(c):** national OSH management-system framework, compliance with regulations and standards, and national/tailored guidance responding to organizational needs, size and nature of activities.
- **p. 4, §2.3.1(a)–(b):** tailored guidance considers organizational size/infrastructure and the types of hazards and degree of risks.
- **pp. 6–8, §§3.1–3.3:** organizational OSH policy, worker participation, responsibility/accountability and arrangements for identifying, eliminating or controlling hazards and risks.
- **p. 10, §3.7.2(a)–(c):** initial review identifies applicable national laws/regulations and other requirements, assesses hazards/risks arising from the work environment and work organization, and determines whether controls are adequate.

These are direct, claim-relevant passages for B and C. They are not already linked in the canonical records and must not be treated as if they were.

## 5. Claim-by-Claim findings

### Claim A

Current statement:
“Охрана труда направлена на предотвращение вреда и создание безопасных и здоровых условий работы. (occupational-safety-basics).”

Existing ILO portal passage:
- Page section “Safety and health at work”, opening body paragraph.
- The following paragraph describes ILO action with governments, employers and workers to improve OSH at national, sectoral and workplace levels.

Fit:
- The core proposition is directly supported by the existing ILO Source.
- The literal trailing suffix is an editorial defect and should be removed only through a separate versioned Claim authorization.

Proposed EU locator description (pending authorization):
> ILO, “Safety and health at work”, section “Safety and health at work”, opening body paragraph: describes occupational safety and health as protecting lives, preventing harm and ensuring that workers can carry out their work safely and with dignity. The following paragraph describes ILO action to improve safety and health at national, sectoral and workplace levels. This supports the general purpose stated in the Claim; it is not a jurisdiction-specific legal standard.

Disposition: source fit DIRECT at the broad stated scope; Claim wording still requires separate editorial correction. HOLD.

### Claim B

Current statement:
“Управление охраной труда включает идентификацию и контроль рисков, организационные процессы и участие работников.”

Existing ILO portal:
- The portal provides high-level context and points to ILO OSH management resources.
- It does not itself give sufficient detailed passage support for all three components of this Claim.

Separate ILO-OSH 2001 publication:
- §§3.1–3.2, pp. 6–7: policy and worker participation.
- §3.3, pp. 7–8: responsibility/accountability and the identification, elimination or control of hazards and risks.
- §3.7.2, p. 10: review of applicable requirements, hazards/risks and adequacy of controls.

Fit:
- These passages directly support the management-process, risk-identification/control and worker-participation components.
- The separate ILO-OSH 2001 publication must be registered as a distinct Source and linked by an authorized versioned Evidence Use; do not point the existing EU to the new PDF while retaining the old ILO portal identity.

Disposition: PARTIAL in the current canonical chain; direct support is available from a separate ILO publication, pending bounded authorization and source registration. HOLD.

### Claim C

Current statement:
“Безопасность труда зависит от применимых национальных и отраслевых требований, условий конкретного рабочего места и характера опасностей.”

Existing ILO portal:
- Opening section and second body paragraph identify national, sectoral and workplace levels.

Separate ILO-OSH 2001 publication:
- §1.2, p. 1: national framework, regulations/standards and tailored guidance.
- §2.3.1, p. 4: organizational size/infrastructure and types of hazards/degree of risk.
- §3.7.2, p. 10: applicable national laws/regulations and hazards arising from the work environment and work organization.

Fit:
- The combined passages support the Claim's context-dependent and multilevel character.
- Keep the distinction between international guidance and binding domestic requirements. ILO-OSH 2001 describes practical recommendations and expressly says they are not legally binding or a replacement for national laws, regulations or accepted standards (Introduction, p. IX / PDF p. 10).
- The EU-OSHA page may be useful corroboration but must not be presented as the existing ILO Source.

Disposition: PARTIAL in the current canonical chain; direct support is available from the existing ILO portal plus a separate ILO-OSH 2001 Source, pending authorization. HOLD.

## 6. Rights and source-use note

The ILO-OSH 2001 PDF identifies copyright © International Labour Organization 2001 and states that short excerpts may be reproduced with source indication; rights of reproduction or translation require an application to the ILO Publications Bureau.

This review uses section/page locators and factual paraphrase only. It does not reproduce figures or long passages and does not decide whether the encyclopedia's intended publication model requires additional permission. The exact public-edition rights/attribution basis must be documented before pilot publication.

## 7. Required bounded remediation proposal

A safe correction would require two separately scoped decisions:

### A. Evidence/source authorization

- Keep the existing ILO portal Source @1 and its identity/URI unchanged.
- Version the existing Evidence Use A with a pinpoint to the ILO portal's opening body paragraph.
- Add a distinct Source record for ILO-OSH 2001 only if the project explicitly authorizes that new source.
- Add versioned Evidence Use links for B and C to the new ILO-OSH 2001 Source, preserving the existing ILO portal link where useful.
- Preserve the source's non-binding-guidance limitation and its national/organizational scope.
- Add dedicated regression checks for exact Source/Evidence Use references, version numbers, PDF page/section pinpoints, source identity and the non-binding limitation.
- Update only the slice README, M13 audit documentation and required coverage metadata.

### B. Separate Claim-A editorial authorization

- Version Claim A to remove the literal trailing `(occupational-safety-basics)` suffix only if the editorial owner confirms this is an unintended artifact.
- Preserve the intended proposition and existing provenance.
- Add a regression asserting the exact corrected statement and absence of the suffix.
- Do not include this Claim edit inside an Evidence Use-only authorization.

No authorization for either change is granted by this review.

## 8. Required correction to the prior audit trail

The 2026-11-12 report should not be used as evidence that EU-OSHA OSHwiki is the canonical source for this slice. Its locator proposals are for a different source identity. Before closing the occupational-safety locator finding, reconcile the report against the actual ILO Source record and record the separate ILO-OSH 2001 Source proposal explicitly.

## 9. Integrity and disposition

- Claims inspected: 3.
- Current canonical Source records inspected: 1.
- Current generic Evidence Uses inspected: 3.
- Exact source-identity discrepancy identified between the 2026-11-12 report and the canonical tree: 1.
- Claim A editorial suffix defect identified: 1.
- Canonical Claim/Evidence Use/Source JSON changed: 0.
- D/E/B scores assigned or changed: 0.
- New Source records created: 0.
- All three Claims remain HOLD.
- No specialist occupational-safety review, independent Human View, rights clearance or publication approval is claimed.

---
This is a noncanonical source-passage and identity review. It is not a correction authorization, final D/E/B scoring, independent specialist review, or publication approval.
