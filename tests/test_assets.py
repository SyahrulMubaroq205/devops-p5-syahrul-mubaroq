"""Unit tests for asset registration and condition updates."""

import pytest
from app.assets import AssetService


def test_register_asset_assigns_id_and_cleans_name():
    service = AssetService()
    asset = service.register_asset("  Projector  ", "Meeting room")
    assert asset["id"] == 1
    assert asset["name"] == "Projector"
    assert asset["condition"] == "good"


def test_register_asset_rejects_blank_name():
    service = AssetService()
    with pytest.raises(ValueError, match="Asset name"):
        service.register_asset("   ", "Meeting room")


def test_register_asset_rejects_invalid_condition():
    service = AssetService()
    with pytest.raises(ValueError, match="Condition"):
        service.register_asset("Chair", "Office", "unknown")


def test_update_condition_for_existing_asset():
    service = AssetService()
    asset = service.register_asset("Chair", "Office")
    updated = service.update_condition(asset["id"], "damaged")
    assert updated["condition"] == "damaged"


def test_update_condition_for_missing_asset_returns_none():
    service = AssetService()
    assert service.update_condition(999, "good") is None
