import json
from pathlib import Path
SLICE = Path("CONTENT/vertical-slices/epidemiology-basics")
def test_content_epidemiology_basics_vertical_slice():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
    assert len(records)==14
    types=[r["record_type"] for r in records]
    assert types.count("source")==3
    assert types.count("claim")==4
    assert types.count("evidence_use")==5
    assert types.count("context")==1
    assert types.count("scope")==1
    sources={r["record_id"] for r in records if r["record_type"]=="source"}
    claims=[r for r in records if r["record_type"]=="claim"]
    evidence=[r for r in records if r["record_type"]=="evidence_use"]
    assert all(r["provenance"]["created_from"][0]["record_id"] in sources for r in claims)
    assert all(r["content"]["source_ref"]["record_id"] in sources for r in evidence)
    assert {r["content"]["claim_ref"]["record_id"] for r in evidence}=={r["record_id"] for r in claims}
    assert any(r["content"]["source_ref"]["record_id"]=="SRC-WHO-EPIDEMIOLOGY-2024" for r in evidence)
def test_who_basic_epidemiology_definition_has_direct_locator():
    records=[json.loads(p.read_text(encoding="utf-8")) for p in (SLICE/"records").glob("*.json")]
    by_id={r["record_id"]:r for r in records}
    source=by_id["SRC-WHO-BASIC-EPIDEMIOLOGY-2E"]
    evidence=by_id["EU-EPIDEMIOLOGY_BASICS-D-WHO-BASIC-EPIDEMIOLOGY"]
    assert source["content"]["external_ref"]["uri"] == "https://iris.who.int/bitstream/handle/10665/43541/9241547073_eng.pdf?sequence=1&isAllowed=y"
    assert source["content"]["external_ref"]["locator"] == "Chapter 1, Box 1.2, Definition of epidemiology, printed page 4"
    assert evidence["content"]["claim_ref"] == {"record_id":"CLM-EPIDEMIOLOGY_BASICS-D","version":"1"}
    assert evidence["content"]["source_ref"] == {"record_id":"SRC-WHO-BASIC-EPIDEMIOLOGY-2E","version":"1"}
