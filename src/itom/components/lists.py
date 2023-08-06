import ttkbootstrap as tb


class ScrolledList(tb.Frame):  # type: ignore
    """A scrollable list with text buttons. Features a button for
    creating new objects and an optional context menu.
    """

    def __init__(self, master: tb.Frame) -> None:
        super().__init__(master=master)

        self.ttk_key_var: tb.StringVar = tb.StringVar()
        self.ttk_value_var: tb.StringVar = tb.StringVar()

        self._build_gui_components()

    def _build_gui_components(self) -> None:
        """Create the GUI elements inside this component."""
        pass
