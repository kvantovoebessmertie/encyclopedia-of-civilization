"""Эталонная реализация полного машиночитаемого вертикального среза."""

__version__ = "0.1.0"
SCHEMA_VERSION = "0.4"
VALIDATOR_VERSION = "0.2"
PACKAGE_VERSION = "0.1"
SUPPORTED_TYPES = frozenset({
    "record",
    "claim",
    "source",
    "evidence_use",
    "assessment",
    "inference",
    "decision",
    "action",
    "event",
    "result",
    "trust_reputation",
    "authorship_contribution",
    "provenance",
    "scope",
    "context",
    "identity",
    "relation",
    "process",
    "state",
})
