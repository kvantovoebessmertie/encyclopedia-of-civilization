DOCUMENTED_FILENAME_ALIASES = {
    "CONTENT/vertical-slices/web-systems-basics/records/CLM-A.json": "CLM-WEB_SYSTEMS_BASICS-A",
    "CONTENT/vertical-slices/web-systems-basics/records/CLM-B.json": "CLM-WEB_SYSTEMS_BASICS-B",
    "CONTENT/vertical-slices/web-systems-basics/records/CLM-C.json": "CLM-WEB_SYSTEMS_BASICS-C",
    "CONTENT/vertical-slices/web-systems-basics/records/EU-A.json": "EU-WEB_SYSTEMS_BASICS-A",
    "CONTENT/vertical-slices/web-systems-basics/records/EU-B.json": "EU-WEB_SYSTEMS_BASICS-B",
    "CONTENT/vertical-slices/web-systems-basics/records/EU-C.json": "EU-WEB_SYSTEMS_BASICS-C",
}


def is_documented_filename_id_alias(relative_path: str, internal_id: str) -> bool:
    return DOCUMENTED_FILENAME_ALIASES.get(relative_path) == internal_id
