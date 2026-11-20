from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT" / "vertical-slices" / "infrastructure-resilience-basics" / "records"

def test_infrastructure_resilience_basics_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    assert len(records) >= 9
    assert {"source", "claim", "evidence_use", "context", "scope"} <= {r["record_type"] for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = {r["record_id"] for r in records if r["record_type"] == "claim"}
    assert len(sources) >= 1
    assert len(claims) >= 3
    for claim in [r for r in records if r["record_type"] == "claim"]:
        assert claim["provenance"]["created_from"][0]["record_id"] in sources
        assert any(e["content"]["claim_ref"]["record_id"] == claim["record_id"] and e["content"]["source_ref"]["record_id"] in sources for e in records if e["record_type"] == "evidence_use")

def test_historical_fema_source_v1_is_preserved_alongside_cisa_v2():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in SLICE.glob("*.json")]
    sources = {
        (r["record_id"], r["record_version"]): r
        for r in records
        if r["record_type"] == "source"
    }
    historical = sources[("SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025", "1")]
    current = sources[("SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025", "2")]

    assert historical["content"]["source_identity"] == "FEMA — Infrastructure Dependency Primer"
    assert historical["content"]["external_ref"]["uri"] == (
        "https://www.fema.gov/emergency-managers/practitioners/recovery-resilience-resource-library/infrastructure-dependency"
    )
    assert current["content"]["source_identity"].startswith("Cybersecurity and Infrastructure Security Agency (CISA)")
    assert current["content"]["external_ref"]["uri"].startswith("https://www.cisa.gov/")

    corpus_records = [
        json.loads(p.read_text(encoding="utf-8"))
        for p in (ROOT / "CONTENT" / "vertical-slices").glob("*/records/*.json")
    ]
    historical_reference_records = set()
    for record in corpus_records:
        if record["record_type"] == "evidence_use":
            refs = [record["content"].get("source_ref", {})]
            refs += record.get("provenance", {}).get("created_from", [])
        else:
            refs = record.get("provenance", {}).get("created_from", [])
        if any(
            ref.get("record_id") == "SRC-FEMA-INFRASTRUCTURE-DEPENDENCY-2025"
            and ref.get("version") == "1"
            for ref in refs
        ):
            historical_reference_records.add(record["record_id"])

    assert {
        "EU-INFRASTRUCTURE_RESILIENCE-A-2",
        "EU-INFRASTRUCTURE_RESILIENCE-B-2",
        "EU-INFRASTRUCTURE_RESILIENCE-C-2",
        "REL_M3_EMERGENCY_INFRASTRUCTURE",
        "CTX-REL_M3_EMERGENCY_INFRASTRUCTURE",
    } <= historical_reference_records
