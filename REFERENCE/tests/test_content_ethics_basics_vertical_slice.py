import json
from pathlib import Path
SLICE = Path("CONTENT/vertical-slices/ethics-basics")
EXPECTED = {
 "CLM-ETHICS_BASICS-A": "Моральный релятивизм и моральный",
 "CLM-ETHICS_BASICS-B": "Этика добродетели, утилитаризм и",
 "CLM-ETHICS_BASICS-C": "Сборник включает и другие подход"
}
LOCATORS = {
 "EU-ETHICS_BASICS-A": "Chapter 1, On Moral Relativism and Subjectivism, printed p. 7 onward",
 "EU-ETHICS_BASICS-B": "Chapter 3, On Virtue Ethics, p. 28 onward; Chapter 5, Utilitarianism, p. 46 onward; Chapter 6, Kantian Deontology, p. 53 onward",
 "EU-ETHICS_BASICS-C": "Chapters 2, 4, 7 and 8: Divine Command/Natural Law; Egoism/Social Contract; Feminist Ethics; Evolutionary Ethics"
}
def test_content_ethics_basics_vertical_slice():
 records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
 assert len(records)==9
 by_id={r["record_id"]:r for r in records}
 assert all(r["record_version"]=="2" for r in records)
 assert all(r["publication_status"]=="published" and r["completion_status"]=="complete" for r in records)
 src=by_id["SRC-ETHICS_BASICS"]
 assert "CC BY 4.0" in src["content"]["preservation"]
 for rid,prefix in EXPECTED.items():
  assert by_id[rid]["content"]["statement"].startswith(prefix)
  assert by_id[rid]["provenance"]["created_from"]==[{"record_id":src["record_id"],"version":"2"}]
 for rid,locator in LOCATORS.items():
  c=by_id[rid]["content"]
  assert c["material"]["locator"]==locator
  assert c["claim_ref"]["version"]=="2" and c["source_ref"]["version"]=="2"
 assert by_id["CTX-ETHICS_BASICS"]["content"]["target_ref"]["version"]=="2"
 assert by_id["SCP-ETHICS_BASICS"]["content"]["target_ref"]["version"]=="2"
