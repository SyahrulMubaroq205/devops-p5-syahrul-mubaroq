"""In-memory storage for the demo application."""


class AssetStorage:
    def __init__(self):
        self._assets = {}
        self._next_id = 1

    def add(self, asset: dict) -> dict:
        record = dict(asset)
        record["id"] = self._next_id
        self._assets[self._next_id] = record
        self._next_id += 1
        return dict(record)

    def list_all(self) -> list[dict]:
        return [dict(item) for item in self._assets.values()]

    def get(self, asset_id: int) -> dict | None:
        item = self._assets.get(asset_id)
        return dict(item) if item else None

    def update(self, asset_id: int, changes: dict) -> dict | None:
        if asset_id not in self._assets:
            return None
        self._assets[asset_id].update(changes)
        return dict(self._assets[asset_id])
