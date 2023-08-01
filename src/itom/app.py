from typing import Optional

from controller.world_controller import WorldController
from model.settings import Settings


class App:
    def __init__(self, settings_file_path: Optional[str] = None) -> None:
        self.settings = Settings(
            app_name="Itom",
            app_author="Sebastian Führ",
            settings_file_path=settings_file_path,
        )
        self.world_controller = WorldController(self.settings)
        self.world = self.world_controller.load_world("Default")


if __name__ == "__main__":
    App()
