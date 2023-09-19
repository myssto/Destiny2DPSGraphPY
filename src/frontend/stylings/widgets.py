"""Extended Tkinter widgets pre-applied with theme options"""

import tkinter as tk
import tkinter.ttk as ttk

import frontend.stylings.themecontroller as _s

DOCSTRING = """\nCustom themed D2DPSGPY widget"""

# region Default Widgets


class Button(tk.Button):
    __doc__ = tk.Button.__doc__ + DOCSTRING

    def __init__(self, master: tk.Misc | None = None, **kwargs) -> None:
        t_opts = _s.ctrl.get_widget_theme("Button")
        # Using dict.update() allows overriding defualt theme options if one wishes to
        t_opts.update(kwargs)
        super().__init__(master=master, **t_opts)


class Checkbutton(tk.Checkbutton):
    __doc__ = tk.Button.__doc__ + DOCSTRING

    def __init__(self, master: tk.Misc | None = None, **kwargs) -> None:
        t_opts = _s.ctrl.get_widget_theme("Checkbutton")
        # Using dict.update() allows overriding defualt theme options if one wishes to
        t_opts.update(kwargs)
        super().__init__(master=master, **t_opts)


class Combobox(ttk.Combobox):
    __doc__ = ttk.Combobox.__doc__ + DOCSTRING

    def __init__(self, master: tk.Misc | None = None, **kwargs) -> None:
        t_default = {"state": "readonly"}
        t_opts = t_default.update(_s.ctrl.get_widget_theme("Combobox"))
        t_opts.update(kwargs)
        super().__init__(master=master, **t_opts)


class Frame(tk.Frame):
    __doc__ = tk.Frame.__doc__ + DOCSTRING

    def __init__(self, master: tk.Misc | None = None, **kwargs) -> None:
        t_opts = _s.ctrl.get_widget_theme("Frame")
        t_opts.update(kwargs)
        super().__init__(master=master, **t_opts)


class Label(tk.Label):
    __doc__ = tk.Label.__doc__ + DOCSTRING

    def __init__(self, master: tk.Misc | None = None, **kwargs) -> None:
        t_opts = _s.ctrl.get_widget_theme("Label")
        t_opts.update(kwargs)
        super().__init__(master=master, **t_opts)


# endregion

# region Custom Widgets


class Subframe(tk.Frame):
    __doc__ = tk.Frame.__doc__ + DOCSTRING

    def __init__(self, master: tk.Misc | None = None, **kwargs) -> None:
        t_opts = _s.ctrl.get_widget_theme("Subframe")
        t_opts.update(kwargs)
        super().__init__(master=master, **t_opts)


# endregion

# region Utility

# Default grid padding
def padding() -> dict[str, int | str]:
    return {
        "padx": 5,
        "pady": 5,
        "sticky": "NSW"
    }

# endregion
