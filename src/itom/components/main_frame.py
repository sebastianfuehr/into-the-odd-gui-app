from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import ttkbootstrap as tb

from itom.components.views import ListFrame

if TYPE_CHECKING:
    from itom.app import App


class MainFrame(tb.Window):  # type: ignore
    """The entrypoint for the application's GUI.

    Attributes
        content_frame(tb.Frame): The central frame of the application
            which will be manipulated by the main menu to show
            different content components.
        main_menu(MainMenu): The main menu GUI component.
        mm_key_var(tb.StringVar): Stores the currently selected main
            menu object.
    """

    def __init__(self, app: "App", themename: str) -> None:
        """
        Forwards the created ttkbootstrap Style object to the
        initiating App object.

        Args
            app(App): An app object to pass on to all child components as a
                controller of app settings and visual structure
                attributes.
            themename(str): A ttkbootstrap theme name.
        """
        super().__init__(
            title="Into the Odd Manager",
            themename=themename,
        )
        self.app = app

        self.app.style = self.style
        self.mm_key_var = tb.StringVar()

        self.main_menu: Optional[MainMenu] = None
        self.content_frame: ListFrame | None = None

        self._build_gui_components()

    def _build_gui_components(self) -> None:
        """Create the GUI elements inside this component."""
        self.main_menu = MainMenu(self, self.app, self.mm_key_var)
        self.main_menu.pack(fill="x")

        self.content_frame = ListFrame(self)
        self.content_frame.pack(expand=True, fill="both")


class MainMenu(tb.Frame):  # type: ignore
    def __init__(self, master: tb.Frame, app: "App", nav_key_var: tb.StringVar) -> None:
        super().__init__(master=master)
        self.app = app
        self.nav_key_var = nav_key_var

        # Button for world selection
        style_lbl_world = self.app.guis.buttons["world_selection"]
        lbl_world = tb.Label(
            self,
            text="World Name",
            font=style_lbl_world["font"],
            background=self.app.style.colors.primary,
        )
        lbl_world.pack(
            side="left", padx=style_lbl_world["padx"], pady=style_lbl_world["pady"]
        )

        # Menu items
        lbl_character = tb.Label(
            self, text="Characters", font=self.app.guis.fonts["Default"]
        )
        lbl_character.pack(side="left")
