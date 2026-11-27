import json
from pathlib import Path
SLICE = Path("CONTENT/vertical-slices/philosophy-basics")
EXPECTED = {
 "CLM-PHILOSOPHY_BASICS-A": "Философия исследует широкие фунд",
 "CLM-PHILOSOPHY_BASICS-B": "Философские аргументы оцениваютс",
 "CLM-PHILOSOPHY_BASICS-C": "Вводная карта философии различае"
}
LOCATORS = {
 "EU-PHILOSOPHY_BASICS-A": "Chapter 1 §1.1, What Is Philosophy?",
 "EU-PHILOSOPHY_BASICS-B": "Chapter 1 §1.2, How Do Philosophers Arrive at Truth?; Sources of Evidence, Logic, Conceptual Analysis",
 "EU-PHILOSOPHY_BASICS-C": "Chapters 5–11: Logic and Reasoning; Metaphysics; Epistemology; Value Theory; Normative Moral Theory; Applied Ethics; Political Philosophy"
}
def test_content_philosophy_basics_vertical_slice():
 records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
 assert len(records)==9
 by_id={r["record_id"]:r for r in records}
 assert all(r["record_version"]=="2" for r in records)
 assert all(r["publication_status"]=="published" and r["completion_status"]=="complete" for r in records)
 src=by_id["SRC-PHILOSOPHY_BASICS"]
 assert "CC BY 4.0" in src["content"]["preservation"]
 for rid,prefix in EXPECTED.items():
  assert by_id[rid]["content"]["statement"].startswith(prefix)
  assert by_id[rid]["provenance"]["created_from"]==[{"record_id":src["record_id"],"version":"2"}]
 for rid,locator in LOCATORS.items():
  c=by_id[rid]["content"]
  assert c["material"]["locator"]==locator
  assert c["claim_ref"]["version"]=="2" and c["source_ref"]["version"]=="2"
 assert by_id["CTX-PHILOSOPHY_BASICS"]["content"]["target_ref"]["version"]=="2"
 assert by_id["SCP-PHILOSOPHY_BASICS"]["content"]["target_ref"]["version"]=="2"
