# First Edition — International Law v2 Substantive Dependency Re-review

Date: 2026-11-19  
Repository: `kvantovoebessmertie/encyclopedia-of-civilization`  
Branch: `mvp-public-contribution-design-2026-10-11`  
Inspection HEAD: `50d37a3da7c66fc383783d21cf3fd08d9aa6038f`  
Prior version-drift report: `FIRST-EDITION-INTERNATIONAL-LAW-VERSION-DRIFT-REVIEW-2026-11-19.md`  
Status: **13/13 CURRENT v2 RECORDS RE-FETCHED; IDENTITY/REFERENCE CHECKS PASS; SUBSTANTIVE REVIEW COMPLETE WITH EVIDENCE/SCOPE FINDINGS; ALL HOLD**

## 1. Scope and change control

This is a bounded substantive re-review of the 13 current v2 records in `international-law-basics`: two Sources, three Claims, six Evidence Use records, one Context and one Scope.

- Every record was fetched from canonical JSON at the exact inspection HEAD above.
- The review covers exact identity/version/type, Claim wording, EU target/source edges, locator-to-proposition fit, Context/Scope target identity, and consistency with the controlling Evidence Use Standard.
- No canonical JSON, identifier, version, Relation, allowlist, publication state or release manifest was changed.
- No v1 historical review row is deleted or silently transferred to v2.
- This is a bounded editorial/evidence review, not a legal opinion or qualified legal sign-off.
- All 13 v2 records remain HOLD. No INCLUDE or EXCLUDE is assigned.

## 2. Exact record inventory and graph result

| Record | Current version/type | Identity and graph result | Disposition |
|---|---|---|---|
| `SRC-INTERNATIONAL_LAW_BASICS@2` | Source | Official UN Charter full text; exact UN URL and relevant article locators present | HOLD |
| `SRC-INTERNATIONAL_LAW_BASICS-INDEPENDENT@2` | Source | ICRC Handbook (2013); official ICRC PDF; section/page locators present | HOLD |
| `CLM-INTERNATIONAL_LAW_BASICS-A@2` | Claim | Provenance resolves to primary UN Charter Source v2 | HOLD |
| `CLM-INTERNATIONAL_LAW_BASICS-B@2` | Claim | Provenance resolves to primary UN Charter Source v2 | HOLD |
| `CLM-INTERNATIONAL_LAW_BASICS-C@2` | Claim | Provenance resolves to primary UN Charter Source v2 | HOLD |
| `EU-INTERNATIONAL_LAW_BASICS-A@2` | Evidence Use | Claim A v2 → UN Charter Source v2; exact locator | HOLD |
| `EU-INTERNATIONAL_LAW_BASICS-B@2` | Evidence Use | Claim B v2 → UN Charter Source v2; exact locator | HOLD |
| `EU-INTERNATIONAL_LAW_BASICS-C@2` | Evidence Use | Claim C v2 → UN Charter Source v2; exact locator | HOLD |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-A@2` | Evidence Use | Claim A v2 → ICRC Source v2; exact locator | HOLD |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-B@2` | Evidence Use | Claim B v2 → ICRC Source v2; locator is a treaty-definition passage, not direct identification of the UN Charter | HOLD |
| `EU-INTERNATIONAL_LAW_BASICS-INDEPENDENT-C@2` | Evidence Use | Claim C v2 → ICRC Source v2; locator covers sources of international law, not the two principles stated in Claim C | HOLD |
| `CTX-INTERNATIONAL_LAW_BASICS@2` | Context | Exact target Claim A v2; context appropriately warns that the Charter is not exhaustive | HOLD |
| `SCP-INTERNATIONAL_LAW_BASICS@2` | Scope | Exact target Claim A v2; educational overview, excludes case-specific legal advice | HOLD |

Result: **13/13 exact IDs, v2 versions and record types match the inspected canonical files. All nine EU edges resolve to the declared Claim and Source versions.** The Context and Scope both target Claim A v2; neither is silently treated as applying to Claims B or C.

## 3. Claim-by-claim substantive findings

### Claim A — general definition of international law

Current proposition: international law regulates relations between States and other recognized subjects of international law in relevant areas.

- ICRC Handbook §2.1.0.1, p. 45, directly defines international law as the body of rules governing relations between subjects of international law, mostly States. This is a close and relevant match for the proposition.
- The Handbook's wording is narrower and more disciplined than an unqualified list of legal persons: it says “subjects of international law, mostly States.” The word “recognized” is a reasonable doctrinal qualifier but should not imply that the Handbook itself supplies an exhaustive test for international legal personality.
- The UN Charter Preamble and Articles 1–2 are not a general definition of international law. The primary UN Charter EU A is therefore contextual to the broad definition rather than the strongest direct support for it.
- The ICRC Handbook explicitly describes itself as a practical reference, not a legal textbook, and its scope is international law relevant to military operations. It is useful for the concise definition but does not settle every doctrinal boundary.

**Finding:** the proposition has a plausible direct source in the ICRC Handbook, but its scope and the independent role of the UN Charter EU need editorial confirmation. No wording is changed here.

### Claim B — treaty character and principles of the UN Charter

Current proposition: the UN Charter is an international treaty and establishes basic principles of international relations.

- The official UN Charter text identifies the agreement by which participating governments establish the United Nations. Articles 110–111 address ratification and entry into force. The current primary EU B locator includes the relevant provisions.
- Articles 1–2 set out the Purposes and Principles governing the Organization and its Members. The proposition's phrase “principles of international relations” risks overgeneralizing: the Charter text expressly frames these as principles on which the Organization and its Members act in pursuit of UN purposes.
- ICRC Handbook §§2.1.0.5–2.1.0.6, p. 46, defines treaties and explains consent to be bound. It provides relevant general doctrinal context, but the current independent EU B does not itself identify the UN Charter as a treaty. Its contribution to this specific Claim is therefore weaker than the primary UN text and should not be counted as independent direct confirmation without further review.

**Finding:** the treaty characterization and Charter provisions are well located in the primary source. The Claim's second clause should be narrowed to the principles governing the UN Organization and its Members. The independent EU B support role remains insufficiently demonstrated.

### Claim C — sovereign equality and peaceful settlement

Current proposition: Charter principles include sovereign equality of States and the obligation to settle international disputes peacefully.

- UN Charter Article 2(1) states the sovereign equality of all UN Members.
- Article 2(3) requires all Members to settle their international disputes by peaceful means in a manner that does not endanger international peace and security or justice.
- Article 33 further specifies peaceful means for parties to disputes whose continuance is likely to endanger international peace and security.
- The current primary EU C locator to Articles 2(1) and 2(3) directly supports both elements. However, the proposition should preserve the Charter's subject boundary: the express Article 2(1) and 2(3) obligations are framed for the Organization and its Members, not as an unqualified statement about every State in every circumstance.
- The current independent EU C locator points to §2.1.0.3 on the sources of international law. That passage lists treaties, customary law and general principles; it does not establish sovereign equality or peaceful settlement. The current EU C is therefore a source-fit mismatch for Claim C.

**Finding:** primary evidence is direct and precise. Scope should explicitly preserve the UN Member boundary. The independent EU C cannot be counted as support for the stated principles on its current locator.

## 4. Evidence Use Standard conformance

The controlling `STANDARD/004-EVIDENCE-USE.md` §3.5 permits exactly two base roles: `supports` and `contradicts`. It expressly distinguishes evidential role from strength, reliability, independence and confidence.

Consequences for this v2 set:

1. The three primary UN Charter EUs have direct locators for the propositions they are intended to support, subject to the Claim A/B/C scope qualifications above.
2. Independent EU A has a direct locator for the general definition in Claim A.
3. Independent EU B currently describes its contribution as doctrinal context and does not itself identify the UN Charter as a treaty. The present `supports` role needs a stronger direct evidential justification or a different authorized record design.
4. Independent EU C explicitly points to a general list of sources of international law, not to the sovereign-equality and peaceful-settlement principles. The present `supports` role is not justified by the stated locator.
5. “Contextualizes” or “background” must not be introduced as a third base role; the Standard does not permit it. If a source does not support or contradict the target proposition, do not retain a misleading `supports` edge merely to preserve source diversity.

## 5. Context and Scope applicability

- `CTX-INTERNATIONAL_LAW_BASICS@2` and `SCP-INTERNATIONAL_LAW_BASICS@2` both correctly target `CLM-INTERNATIONAL_LAW_BASICS-A@2`.
- Their target references are exact and current.
- They must not be assumed to govern Claims B and C merely because the records share a vertical slice.
- If the editor intends one shared educational boundary for all three Claims, the applicable Standard must permit that target model or separate target-specific Context/Scope records must be considered. No such change is authorized or made by this review.

## 6. Bounded remediation queue — no canonical authorization implied

| Priority | Exact issue | Minimum next step | Current status |
|---|---|---|---|
| P1 | Claim B overbroad phrase “principles of international relations” | Editorially consider narrowing to principles governing the UN Organization and its Members | HOLD |
| P1 | Claim C omits the UN Member boundary | Editorially consider making the subject boundary explicit | HOLD |
| P1 | Independent EU C locator does not support Claim C | Find a direct source passage for the stated principles or remove this EU from the Claim C support chain under authorization | HOLD |
| P1 | Independent EU B is only general treaty-definition context | Establish direct support for the UN Charter's treaty status or do not count this EU as direct support | HOLD |
| P2 | Primary UN Charter EU A is not a general definition of international law | Keep the ICRC definition as the direct support for Claim A; reconsider whether the Charter EU A belongs on Claim A | HOLD |
| P2 | Context/Scope target only Claim A | Confirm whether this is intentional; do not infer transfer to B/C | HOLD |
| P2 | ICRC Handbook is a military-operations reference, not a general legal textbook | Preserve its stated scope limitation in editorial assessment | HOLD |
| P2 | Item-level rights and distribution | Resolve the ICRC and UN source-use terms under the approved project policy | HOLD |

Any canonical edit requires the appropriate bounded authorization, exact proposed diff, independent review and affected tests. No change is authorized by this report.

## 7. Source verification

- United Nations, Charter of the United Nations, official full text: https://www.un.org/en/about-us/un-charter/full-text
- United Nations, Charter Chapter I (Articles 1–2): https://www.un.org/en/about-us/un-charter/chapter-1
- International Committee of the Red Cross, *Handbook on International Rules Governing Military Operations* (2013), official PDF: https://www.icrc.org/sites/default/files/topic/file_plus_list/0431-handbook_on_international_rules_governing_military_operations.pdf
- ICRC publication record: https://www.icrc.org/en/publication/0431-handbook-international-rules-governing-military-operations

The ICRC PDF confirms §2.1.0.1 and §2.1.0.3 on printed p. 45, and §§2.1.0.5–2.1.0.6 on printed p. 46. The PDF introduction states that the Handbook is not a legal textbook and focuses on international law governing military operations. Source access is not a reuse licence; rights clearance remains open.

## 8. Final decision

- Current v2 canonical records fetched: **13/13**.
- Exact identity/version/type: **13/13 MATCH**.
- Claim → EU → Source version edges: **9/9 MATCH**.
- Direct primary-source locators: **3/3 present; substantive fit confirmed subject to Claim scope boundaries**.
- Independent EU locators: **1 direct (A), 1 partial/contextual (B), 1 mismatched (C)**.
- Context/Scope target: **2/2 exact to Claim A v2; no transfer inferred**.
- Canonical changes: **0**.
- INCLUDE: **0**.
- EXCLUDE: **0**.
- Disposition: **13/13 HOLD pending authorized remediation, rights review and independent editorial/legal review**.
