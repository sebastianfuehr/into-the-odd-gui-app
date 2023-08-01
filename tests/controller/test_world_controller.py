from itom.controller.world_controller import WorldController
from itom.model.settings import Settings


def test_load_default_world(default_settings: Settings) -> None:
    world_controller = WorldController(default_settings)
    world = world_controller.load_world("Default")
    assert len(world.armor_items) == 4


def test_get_world_dir(default_settings: Settings) -> None:
    world_controller = WorldController(default_settings)
    dir_path = world_controller.get_world_dir("My World")
    assert dir_path == f"{default_settings.data_dir}/world_my_world"
