from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
SLICE = ROOT / "CONTENT/vertical-slices/human-settlement-systems-basics/records"
README = ROOT / "CONTENT/vertical-slices/human-settlement-systems-basics/README.md"


def test_human_settlement_systems_basics_vertical_slice_is_complete():
    records = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(SLICE.glob("*.json"))]
    assert len(records) == 11
    types = [r["record_type"] for r in records]
    assert types.count("source") == 3
    assert types.count("claim") == 3
    assert types.count("evidence_use") == 3
    assert types.count("context") == 1
    assert types.count("scope") == 1

    by_id = {r["record_id"]: r for r in records}
    sources = {r["record_id"] for r in records if r["record_type"] == "source"}
    claims = [r for r in records if r["record_type"] == "claim"]
    evidence = [r for r in records if r["record_type"] == "evidence_use"]

    assert all(
        r["provenance"]["created_from"][0]["record_id"] in sources
        for r in claims
    )
    assert {e["content"]["claim_ref"]["record_id"] for e in evidence} == {
        c["record_id"] for c in claims
    }
    assert all(e["content"]["source_ref"]["record_id"] in sources for e in evidence)

    # Claim-specific explanatory depth and explicit system dependencies.
    assert "влиять на доступ людей" in by_id["CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_A"]["content"]["statement"]
    assert "взаимозависимую систему" in by_id["CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B"]["content"]["statement"]
    assert "о воде, жилье, транспорте" in by_id["CLM_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C"]["content"]["statement"]

    # Evidence Use must explain both source contribution and source limits.
    assert "функции" in by_id["EU_HUMAN_SETTLEMENT_SYSTEMS_BASICS_A"]["content"]["material"]["description"]
    assert "не доказывает конкретные локальные последствия" in by_id["EU_HUMAN_SETTLEMENT_SYSTEMS_BASICS_B"]["content"]["material"]["description"]
    assert "не заменяет анализ местных условий" in by_id["EU_HUMAN_SETTLEMENT_SYSTEMS_BASICS_C"]["content"]["material"]["description"]

    # Human View: bounded example, traceability, next steps and local boundary.
    readme = README.read_text(encoding="utf-8")
    assert "Иллюстративный пример" in readme
    assert "не проект конкретного поселения" in readme
    assert "местные данные" in readme
    assert "квалифицированных специалистов" in readme
    assert "Что проверить дальше" in readme
    assert "Как проверить основание утверждения" in readme
    assert "records/CLM-HUMAN_SETTLEMENT_SYSTEMS_BASICS-A.json" in readme
    assert "records/CLM-HUMAN_SETTLEMENT_SYSTEMS_BASICS-B.json" in readme
    assert "records/CLM-HUMAN_SETTLEMENT_SYSTEMS_BASICS-C.json" in readme
    assert "records/EU-HUMAN_SETTLEMENT_SYSTEMS_BASICS-A.json" in readme
    assert "records/EU-HUMAN_SETTLEMENT_SYSTEMS_BASICS-B.json" in readme
    assert "records/EU-HUMAN_SETTLEMENT_SYSTEMS_BASICS-C.json" in readme
    assert "records/SRC-HUMAN_SETTLEMENT_SYSTEMS_BASICS.json" in readme
    assert "records/SRC-WB-HUMAN_SETTLEMENT_SYSTEMS_BASICS.json" in readme
    assert "records/SRC-OECD-HUMAN_SETTLEMENT_SYSTEMS_BASICS.json" in readme
    assert "Source → 3 Claims → 3 Evidence Use → Context → Scope" in readme
    assert "Техническая заметка о составе среза" in readme
