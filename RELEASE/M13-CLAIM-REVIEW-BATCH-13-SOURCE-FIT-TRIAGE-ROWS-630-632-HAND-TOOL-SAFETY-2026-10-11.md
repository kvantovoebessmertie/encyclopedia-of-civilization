# M13 Batch 13 — source-fit triage (rows 630–632): hand-tool safety

Date: 2026-10-11  
Branch: `m13-system-wide-depth-audit-2026-10-09`  
Status: **provisional D/E/B assessment; strong support for defective-tool handling and pre-use inspection, but PPE claim needs task/tool-specific scope**

Rubric: D = explanatory depth, E = claim-specific evidence fit, B = boundaries / epistemic discipline (0–3 each). Scores below are provisional triage estimates, not finalized ledger scores. Canonical Claim/Evidence Use/Source JSON remains unchanged.

## Source trail and scope

- CCOHS, *Hand Tools — General Hand Tool Operation*: https://www.ccohs.ca/oshanswers/safety_haz/hand_tools/general.html
- CCOHS, *Powered Hand Tools — Electric Tools — Basic Safety*: https://www.ccohs.ca/oshanswers/safety_haz/power_tools/saf_elec.html
- OSHA, *Hand and Power Tools — Overview*: https://www.osha.gov/hand-power-tools
- OSHA construction standard 29 CFR 1926.301, *Hand tools*: https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.301

The canonical records identify CCOHS as the source for the defective-tool Claim and OSHA as the source for the inspection and PPE Claims. The direct public-source review supports these broad safety messages, but note that the CCOHS “powered hand tools” page is specifically about electric/powered tools, while the Claims use the broader term “ручной инструмент.” The CCOHS general hand-tools page is a better match for inspection and repair of non-powered hand tools. Existing Evidence Use records have concise summaries but do not pinpoint the exact source passage or clearly distinguish tool classes.

## 1. `CLM-TOOL-DEFECTIVE` — provisional **D2 / E3 / B2**

**Claim:** “Неисправный ручной инструмент следует вывести из использования и заменить или отремонтировать до дальнейшего применения.”

**Assessment:** The Claim gives a clear safety action but does not describe tagging, who may repair, or how the tool is isolated from further use (D2). CCOHS explicitly recommends removing a defective powered tool from service, tagging it “Out of service,” replacing damaged equipment, and using a qualified person for repair; its general hand-tools guidance also says to replace or repair defective tools (E3). The claim's broad “ручной инструмент” is supportable via the general hand-tools source, but repair should not be interpreted as permission for an unqualified user to repair a powered tool (B2).

**Disposition:** Retain provisionally. Evidence Use should cite the general hand-tools guidance and, if powered tools are included, the powered-tool section on removing from service and qualified repair.

## 2. `CLM-TOOL-INSPECT` — provisional **D2 / E3 / B2**

**Claim:** “Перед использованием ручной инструмент следует проверять на повреждения и дефекты.”

**Assessment:** This is a useful pre-use safety instruction but does not list the inspection points or distinguish tool types (D2). CCOHS general hand-tools guidance directly says to inspect tools for defects before use; its powered-tools guidance lists damage checks before each use. OSHA standards require tools to be maintained in safe condition, with specific construction hand-tool defects addressed in 29 CFR 1926.301 (E3). The claim is appropriately general, but exact inspection criteria depend on the tool and hazards (B2).

**Disposition:** Retain provisionally. Add pinpoints to CCOHS's “basic tips” for hand tools and the powered-tool “When and how should you inspect” section only where powered tools are within scope.

## 3. `CLM-TOOL-PPE` — provisional **D2 / E2 / B2**

**Claim:** “При работе с инструментом следует использовать соответствующие средства защиты с учётом выполняемой операции и опасностей.”

**Assessment:** The Claim correctly makes PPE dependent on task and hazards but does not identify hazard assessment or examples of protective equipment (D2). OSHA/CCOHS powered-tool guidance supports using appropriate PPE for tool hazards, but the stored OSHA source is described only as a general hand-tool page and does not yet provide a pinpoint showing the full task-specific proposition for all tools (E2). The wording is appropriately conditional and should not be expanded into a blanket requirement for identical PPE for every tool or operation (B2).

**Disposition:** Retain provisionally with an explicit boundary: PPE depends on the tool, workpiece, operation, workplace assessment and applicable requirements. Add the specific OSHA/CCOHS source passage; consider a separate source for hazard-specific PPE if this is intended as cross-tool guidance.

## Batch accounting

- Individual Claims reviewed in this note: **3**.
- New provisional D/E/B assessments recorded: **3**.
- Canonical Evidence Use records with exact claim-specific pinpoints: **0/3**.
- Finalized scored-ledger rows added: **0**.
- Canonical Claim/Evidence Use/Source JSON changed: **0**.
- Batch 13 complete: **NO**.
