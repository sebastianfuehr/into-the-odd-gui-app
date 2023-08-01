from __future__ import annotations

from typing import TYPE_CHECKING

import ttkbootstrap as tb

if TYPE_CHECKING:
    from itom.app import App


class MainFrame(tb.Window):  # type: ignore
    def __init__(self, app: App) -> None:
        super().__init__(
            title="Into the Odd Manager",
            themename=app.settings.config["appearance"]["theme"],
        )
        self.app = app

        self.main_menu = None
        self.central_frame = None
