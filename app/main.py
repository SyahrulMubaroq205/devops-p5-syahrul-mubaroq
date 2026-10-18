"""Command-line entry point for the asset inventory demo."""

from app.assets import AssetService


def main() -> None:
    service = AssetService()
    service.register_asset("Projector", "Meeting room", "good")
    service.register_asset("Standing fan", "Prayer hall", "needs_repair")
    print("Simple Asset Inventory")
    for asset in service.list_assets():
        print(
            f'#{asset["id"]} {asset["name"]} | '
            f'Location: {asset["location"]} | Condition: {asset["condition"]}'
        )


if __name__ == "__main__":
    main()
