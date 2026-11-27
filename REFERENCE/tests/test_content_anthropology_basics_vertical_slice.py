import json
from pathlib import Path
SLICE = Path("CONTENT/vertical-slices/anthropology-basics")
EXPECTED = {
 "CLM-ANTHROPOLOGY_BASICS-A": "Антропология в данном учебном из",
 "CLM-ANTHROPOLOGY_BASICS-B": "Этнография и включённое наблюден",
 "CLM-ANTHROPOLOGY_BASICS-C": "Холизм, межкультурное сравнение,"
}
LOCATORS = {
 "EU-ANTHROPOLOGY_BASICS-A": "§1.2, printed pp. 14–18",
 "EU-ANTHROPOLOGY_BASICS-B": "§§2.3–2.5, printed pp. 48–55",
 "EU-ANTHROPOLOGY_BASICS-C": "§§1.5–1.7, printed pp. 25–31"
}
def test_content_anthropology_basics_vertical_slice():
 records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
 assert len(records)==9
 by_id={r["record_id"]:r for r in records}
 assert all(r["record_version"]=="2" for r in records)
 assert all(r["publication_status"]=="published" and r["completion_status"]=="complete" for r in records)
 src=by_id["SRC-ANTHROPOLOGY_BASICS"]
 assert "CC BY-NC-SA 4.0" in src["content"]["preservation"]
 for rid,prefix in EXPECTED.items():
  assert by_id[rid]["content"]["statement"].startswith(prefix)
  assert by_id[rid]["provenance"]["created_from"]==[{"record_id":src["record_id"],"version":"2"}]
 for rid,locator in LOCATORS.items():
  c=by_id[rid]["content"]
  assert c["material"]["locator"]==locator
  assert c["claim_ref"]["version"]=="2" and c["source_ref"]["version"]=="2"
 assert by_id["CTX-ANTHROPOLOGY_BASICS"]["content"]["target_ref"]["version"]=="2"
 assert by_id["SCP-ANTHROPOLOGY_BASICS"]["content"]["target_ref"]["version"]=="2"
