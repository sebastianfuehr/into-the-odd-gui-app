import json

from itom.controller.json_controller import ItomJSONDecoder
from itom.model.definitions import Settings
from itom.model.world import World


class WorldController:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def load_world(self, world_name: str) -> World:
        world_path = self.get_world_dir(world_name)
        items, weapons, armor_items, arcana = [], [], [], []

        # Load item-compendium
        path_item_compendium = f"{world_path}/compendia/item-compendium.json"
        with open(path_item_compendium, "r") as f:
            decoded_json = json.load(f, cls=ItomJSONDecoder)
            items = decoded_json["items"]
            weapons = decoded_json["weapons"]
            armor_items = decoded_json["armor_items"]

        # Load gm-compendium
        path_gm_compendium = f"{world_path}/compendia/gm-compendium.json"
        with open(path_gm_compendium, "r") as f:
            decoded_json = json.load(f, cls=ItomJSONDecoder)
            arcana = decoded_json["arcana"]

        return World(
            items=items, weapons=weapons, armor_items=armor_items, arcana=arcana
        )

    def get_world_dir(self, world_name: str) -> str:
        better_name = world_name.lower().replace(" ", "_")
        return f"{self.settings.data_dir}/world_{better_name}"


class FileController:
    pass
