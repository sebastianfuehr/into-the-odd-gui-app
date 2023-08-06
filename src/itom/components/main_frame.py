from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import ttkbootstrap as tb

from itom.components.views import ListFrame

if TYPE_CHECKING:
    pass


class MainFrame(tb.Window):  # type: ignore
    def __init__(self, themename: str) -> None:
        super().__init__(
            title="Into the Odd Manager",
            themename=themename,
        )

        self.mm_key_var = tb.StringVar()

        self.main_menu: Optional[MainMenu] = None
        self.content_frame: ListFrame | None = None

        self._build_gui_components()

    def _build_gui_components(self) -> None:
        """Create the GUI elements inside this component."""
        self.main_menu = MainMenu(self, self.mm_key_var)
        self.main_menu.pack(fill="x")

        self.content_frame = ListFrame(self)
        self.content_frame.pack(expand=True, fill="both")


class MainMenu(tb.Frame):  # type: ignore
    def __init__(self, master: tb.Frame, nav_key_var: tb.StringVar) -> None:
        super().__init__(master=master)
        self.nav_key_var = nav_key_var

        # Button for world selection
        lbl_world = tb.Label(self, text="World Name")
        lbl_world.pack(side="left")

        # Menu items
        lbl_character = tb.Label(self, text="Characters")
        lbl_character.pack(side="left")
