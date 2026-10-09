from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS_DIR = ROOT / "CONTENT" / "vertical-slices"
RISK_TERMS = {
    "health_medical": r"здоров|медицин|лекарств|дозиров|симптом|инфекц|болезн|травм|кровотеч|реанимац|первая помощь|health|medical|medicine|dose|symptom|infection|disease",
    "emergency_fire_co": r"пожар|угарн|углекисл|эвакуац|чрезвычайн|дым|огнетуш|carbon monoxide|fire|evacuat|emergency",
    "water_food_sanitation": r"питьев.*вод|очистк.*вод|обеззараж|кипячен|санитар|пищев|хранени.*продукт|water treatment|drinking water|sanitation|food safety",
    "electricity_energy": r"электр|напряжен|ток|генератор|аккумулятор|газов.*оборуд|энергоснабж|electric|voltage|generator|battery",
    "construction_tools_materials": r"строитель|фундамент|несущ|кровл|лестниц|инструмент|сварк|бетон|древесин|конструкц|construction|load-bearing|welding",
    "chemicals_hazards": r"химическ|кислот|щелоч|растворител|токсич|ядовит|реагент|chemical|toxic|corrosive",
    "legal_financial": r"закон|юрисдикц|налог|кредит|договор|ответственност|финансов|инвестиц|legal|jurisdiction|tax|loan|contract|financial|investment",
}
GENERIC_EVIDENCE = re.compile(
    r"\b(подтверждает|соответствует|показывает|свидетельствует|объясняет|supports|confirms|shows)\b",
    re.IGNORECASE,
)
ACTIONABLE = re.compile(
    r"\b(должен|необходимо|нельзя|следует|используйте|проверьте|выполните|обеспечьте|"
    r"must|should|do not|never|use|check|ensure|perform)\b",
    re.IGNORECASE,
)


def load_records():
    rows = []
    for path in sorted(RECORDS_DIR.glob("*/records/*.json")):
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            raise RuntimeError(f"Cannot parse {path.relative_to(ROOT)}: {exc}") from exc
        rows.append({"path": path, "slice": path.parent.parent.name, "record": obj})
    return rows


def text_values(value):
    out = []
    if isinstance(value, str):
        out.append(value)
    elif isinstance(value, dict):
        for v in value.values():
            out.extend(text_values(v))
    elif isinstance(value, list):
        for v in value:
            out.extend(text_values(v))
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(ROOT / "RELEASE" / "m13-claim-audit-worksheet"))
    args = parser.parse_args()
    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = load_records()
    records_by_id = defaultdict(list)
    for row in rows:
        r = row["record"]
        records_by_id[str(r.get("record_id", ""))].append(row)

    claims = [row for row in rows if row["record"].get("record_type") == "claim"]
    evidence_by_claim = defaultdict(list)
    for row in rows:
        r = row["record"]
        if r.get("record_type") != "evidence_use":
            continue
        content = r.get("content", {})
        claim_ref = content.get("claim_ref", {}) if isinstance(content, dict) else {}
        claim_id = claim_ref.get("record_id") if isinstance(claim_ref, dict) else None
        if claim_id:
            evidence_by_claim[str(claim_id)].append(row)

    worksheet = []
    for row in claims:
        claim = row["record"]
        cid = str(claim.get("record_id", ""))
        content = claim.get("content", {}) if isinstance(claim.get("content"), dict) else {}
        statement = content.get("statement") or content.get("text") or content.get("description") or ""
        linked = evidence_by_claim.get(cid, [])
        evidence_items = []
        source_ids = []
        evidence_roles = []
        evidence_materials = []
        for evrow in linked:
            ev = evrow["record"]
            ec = ev.get("content", {}) if isinstance(ev.get("content"), dict) else {}
            sr = ec.get("source_ref", {})
            sid = sr.get("record_id") if isinstance(sr, dict) else None
            if sid:
                source_ids.append(str(sid))
            role = ec.get("evidence_role")
            if role:
                evidence_roles.append(str(role))
            material = ec.get("material", {})
            material_text = " ".join(text_values(material))
            evidence_materials.append(material_text)
            source_rows = records_by_id.get(str(sid), []) if sid else []
            source = next((x["record"] for x in source_rows if x["record"].get("record_type") == "source"), {})
            sc = source.get("content", {}) if isinstance(source.get("content"), dict) else {}
            evidence_items.append({
                "evidence_use_id": ev.get("record_id"),
                "evidence_role": role,
                "evidence_material": material_text,
                "source_id": sid,
                "source_identity": sc.get("source_identity"),
                "source_uri": (sc.get("external_ref") or {}).get("uri") if isinstance(sc.get("external_ref"), dict) else None,
                "source_representation": sc.get("representation"),
                "evidence_slice": evrow["slice"],
            })
        combined = " ".join([str(statement)] + evidence_materials)
        risk_domains = [name for name, pattern in RISK_TERMS.items() if re.search(pattern, combined, re.IGNORECASE)]
        flags = []
        if not str(statement).strip():
            flags.append("claim_statement_missing_or_nonstandard_field")
        if len(str(statement).split()) < 8:
            flags.append("very_short_claim_statement_review")
        if not linked:
            flags.append("no_linked_evidence_use")
        if linked and not source_ids:
            flags.append("evidence_use_without_source_ref")
        if linked and not any(str(x).strip() for x in evidence_materials):
            flags.append("evidence_material_empty")
        if linked and any(len(x.split()) < 8 for x in evidence_materials if x.strip()):
            flags.append("short_evidence_material_review")
        if linked and any(GENERIC_EVIDENCE.search(x) and len(x.split()) < 16 for x in evidence_materials if x.strip()):
            flags.append("potentially_generic_evidence_material_review")
        if ACTIONABLE.search(str(statement)):
            flags.append("actionable_or_prescriptive_claim_review")
        if risk_domains:
            flags.append("high_consequence_screen")
        worksheet.append({
            "record_id": cid,
            "record_version": str(claim.get("record_version", "")),
            "slice": row["slice"],
            "file": str(row["path"].relative_to(ROOT)),
            "publication_status": claim.get("publication_status"),
            "completion_status": claim.get("completion_status"),
            "claim_type": content.get("claim_type"),
            "statement": str(statement),
            "evidence_use_count": len(linked),
            "evidence_use_ids": sorted(str(x["record"].get("record_id", "")) for x in linked),
            "source_ids": sorted(set(source_ids)),
            "evidence_roles": sorted(set(evidence_roles)),
            "evidence_items": evidence_items,
            "risk_domains": risk_domains,
            "machine_triage_flags": flags,
            "D_score": None,
            "D_rationale": "",
            "E_score": None,
            "E_rationale": "",
            "B_score": None,
            "B_rationale": "",
            "human_review_status": "NOT_YET_REVIEWED",
        })

    worksheet.sort(key=lambda x: (x["slice"], x["record_id"]))
    json_path = outdir / "M13-CLAIM-AUDIT-WORKSHEET.json"
    csv_path = outdir / "M13-CLAIM-AUDIT-WORKSHEET.csv"
    json_path.write_text(json.dumps({
        "audit": "M13 claim-level depth and epistemic audit worksheet",
        "basis": "Generated from actual record_type and record references; machine flags are triage only, not semantic scores.",
        "source_revision": __import__("subprocess").run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=False
        ).stdout.strip() or "unknown",
        "records_scanned": len(rows),
        "claim_count": len(worksheet),
        "risk_screen_counts": dict(Counter(d for x in worksheet for d in x["risk_domains"])),
        "triage_flag_counts": dict(Counter(f for x in worksheet for f in x["machine_triage_flags"])),
        "claims": worksheet,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    flat = []
    for x in worksheet:
        y = {k: v for k, v in x.items() if k != "evidence_items"}
        y["evidence_items_json"] = json.dumps(x["evidence_items"], ensure_ascii=False)
        for k in ("evidence_use_ids", "source_ids", "evidence_roles", "risk_domains", "machine_triage_flags"):
            y[k] = ";".join(y[k])
        flat.append(y)
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(flat[0].keys()) if flat else [])
        writer.writeheader()
        writer.writerows(flat)

    counts = Counter(f for x in worksheet for f in x["machine_triage_flags"])
    risk_counts = Counter(d for x in worksheet for d in x["risk_domains"])
    print("M13 CLAIM AUDIT WORKSHEET GENERATED")
    print(f"Records scanned: {len(rows)}")
    print(f"Claims inventoried: {len(worksheet)}")
    print(f"Claims with linked Evidence Use: {sum(bool(x['evidence_use_count']) for x in worksheet)}")
    print(f"Claims flagged for machine triage: {sum(bool(x['machine_triage_flags']) for x in worksheet)}")
    print(f"High-consequence claims flagged: {sum('high_consequence_screen' in x['machine_triage_flags'] for x in worksheet)}")
    print("Risk-screen counts: " + json.dumps(dict(sorted(risk_counts.items())), ensure_ascii=False))
    print("Triage-flag counts: " + json.dumps(dict(sorted(counts.items())), ensure_ascii=False))
    print(f"JSON worksheet: {json_path}")
    print(f"CSV worksheet: {csv_path}")


if __name__ == "__main__":
    main()
