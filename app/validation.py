"""Input validation helpers for asset records."""


def validate_asset_name(name: str) -> str:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Asset name must not be empty.")
    return name.strip()


def validate_condition(condition: str) -> str:
    allowed = {"good", "needs_repair", "damaged"}
    if condition not in allowed:
        raise ValueError(f"Condition must be one of: {', '.join(sorted(allowed))}.")
    return condition
