import ttkbootstrap as tb

from itom.components.lists import ScrolledList


class ListFrame(tb.Frame):  # type: ignore
    """A split view, featuring an item selection list inside the left
    side panel, and a content frame on the right.
    """

    def __init__(self, master: tb.Frame) -> None:
        super().__init__(master=master)

        self.left_sidebar: ScrolledList | None = None

        self._build_gui_components()

    def _build_gui_components(self) -> None:
        """Create the GUI elements inside this component."""
        self.left_sidebar = ScrolledList(self)
        self.left_sidebar.pack(fill="y")
