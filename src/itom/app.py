from typing import TYPE_CHECKING, Optional

from components.main_frame import MainFrame
from controller.world_controller import WorldController
from model.definitions import GUIStructure, Settings

if TYPE_CHECKING:
    from ttkbootstrap.style import Style


class App:
    """
    This class doesn't inherit from ttkbootstrap.Window to allow the
    implementation of pop up windows which trigger 'before' the main
    window opens.

    Attributes
        guis(GUIStructure):
        main_frame(MainFrame): The entry point for the application's
            GUI.
        settings(Settings):
        style(ttkbootstrap.style.Style)
        world_controller(WorldController):
    """

    def __init__(self, settings_file_path: Optional[str] = None) -> None:
        """
        Args
            settings_file_path(str): A path string towards an ini file
                with user settings.
        """
        self.settings = Settings(
            app_name="Itom",
            app_author="Sebastian Führ",
            settings_file_path=settings_file_path,
        )
        self.guis = GUIStructure(self.settings)
        self.world_controller = WorldController(self.settings)
        self.world = self.world_controller.load_world("Default")

        self.style: Style = None
        theme = self.settings.config["appearance"]["theme"]
        self.main_frame = MainFrame(app=self, themename=theme)

    def start_gui(self) -> None:
        """Start the application loop and open the GUI."""
        self.main_frame.mainloop()

    def restart(self) -> None:
        """Destroy the current main frame and replace it with a new
        one.
        """
        self.main_frame.destroy()
        self.main_frame = MainFrame(self)

        self.main_frame.mainloop()


if __name__ == "__main__":
    app = App()
    app.start_gui()
