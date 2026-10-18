"""Business logic for registering and tracking assets."""

from app.storage import AssetStorage
from app.validation import validate_asset_name, validate_condition


class AssetService:
    def __init__(self, storage: AssetStorage | None = None):
        self.storage = storage or AssetStorage()

    def register_asset(self, name: str, location: str, condition: str = "good") -> dict:
        clean_name = validate_asset_name(name)
        clean_condition = validate_condition(condition)
        if not isinstance(location, str) or not location.strip():
            raise ValueError("Asset location must not be empty.")
        return self.storage.add({
            "name": clean_name,
            "location": location.strip(),
            "condition": clean_condition,
        })

    def list_assets(self) -> list[dict]:
        return self.storage.list_all()

    def update_condition(self, asset_id: int, condition: str) -> dict | None:
        clean_condition = validate_condition(condition)
        return self.storage.update(asset_id, {"condition": clean_condition})
