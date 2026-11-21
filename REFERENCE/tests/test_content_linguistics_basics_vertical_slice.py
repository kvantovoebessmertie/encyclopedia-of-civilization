import json
from pathlib import Path
SLICE = Path("CONTENT/vertical-slices/linguistics-basics")
EXPECTED = {
 "CLM-LINGUISTICS_BASICS-A": "Научное изучение языка опирается",
 "CLM-LINGUISTICS_BASICS-B": "Фонетика описывает физические св",
 "CLM-LINGUISTICS_BASICS-C": "Лингвистический анализ включает "
}
LOCATORS = {
 "EU-LINGUISTICS_BASICS-A": "§§1.2–1.4, printed pp. 10–21",
 "EU-LINGUISTICS_BASICS-B": "Chapter 3 §§3.2–3.6, pp. 72–120; Chapter 4 §§4.1–4.5, pp. 165–185",
 "EU-LINGUISTICS_BASICS-C": "Chapter 5 §§5.1–5.7, pp. 209–239; Chapter 6 §§6.1–6.5, pp. 259–287; Chapter 7 §§7.1–7.5, pp. 389–416"
}
def test_content_linguistics_basics_vertical_slice():
 records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
 assert len(records)==9
 by_id={r["record_id"]:r for r in records}
 assert all(r["record_version"]=="2" for r in records)
 assert all(r["publication_status"]=="published" and r["completion_status"]=="complete" for r in records)
 src=by_id["SRC-LINGUISTICS_BASICS"]
 assert "CC BY-NC-SA 4.0" in src["content"]["preservation"]
 for rid,prefix in EXPECTED.items():
  assert by_id[rid]["content"]["statement"].startswith(prefix)
  assert by_id[rid]["provenance"]["created_from"]==[{"record_id":src["record_id"],"version":"2"}]
 for rid,locator in LOCATORS.items():
  c=by_id[rid]["content"]
  assert c["material"]["locator"]==locator
  assert c["claim_ref"]["version"]=="2" and c["source_ref"]["version"]=="2"
 assert by_id["CTX-LINGUISTICS_BASICS"]["content"]["target_ref"]["version"]=="2"
 assert by_id["SCP-LINGUISTICS_BASICS"]["content"]["target_ref"]["version"]=="2"
