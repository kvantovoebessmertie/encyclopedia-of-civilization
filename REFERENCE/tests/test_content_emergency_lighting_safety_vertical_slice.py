import json
from pathlib import Path
from encyclopedia_reference.validator import Validator
from encyclopedia_reference.semantic_rules import validate_semantic_dataset
ROOT=Path(__file__).resolve().parents[2]; CONTENT=ROOT/"CONTENT"/"vertical-slices"/"emergency-lighting-safety"/"records"; SCHEMA=ROOT/"IMPLEMENTATION"/"005-RECORD-SCHEMA.json"
def test_records_validate():
 rs=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]; assert len(rs)==13; v=Validator(SCHEMA)
 for r in rs:
  x=v.validate(r); assert x.passed,(r["record_id"],[(z.code,z.message) for z in x.findings])
 assert validate_semantic_dataset(rs)==[]
def test_lighting_has_exit_and_sleep_boundary():
 rs=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]
 assert any(r["record_id"]=="CLM-LIGHTING-EXTINGUISH" for r in rs)
def test_flashlight_outage_recommendation_uses_shared_cpsc_source():
 import json
 from pathlib import Path
 rs=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(CONTENT.glob("*.json"))]
 by_id={r["record_id"]:r for r in rs}
 eu=by_id["EU-LIGHTING-FLASHLIGHT-OUTAGE-CPSC-2026"]
 assert eu["content"]["claim_ref"] == {"record_id":"CLM-LIGHTING-FLASHLIGHT-OUTAGE","version":"1"}
 assert eu["content"]["source_ref"] == {"record_id":"SRC-CPSC-WINTER-SAFETY-2026","version":"1"}
 shared_path=ROOT/"CONTENT"/"vertical-slices"/"generator-carbon-monoxide-safety"/"records"/"SRC-CPSC-WINTER-SAFETY-2026.json"
 source=json.loads(shared_path.read_text(encoding="utf-8"))
 assert source["content"]["external_ref"]["uri"] == "https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters"
 assert source["content"]["external_ref"]["locator"] == "Generators; Use Flashlights Instead of Candles"
