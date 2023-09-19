"""
Oversees all theme related operations

Themes are mainly a tool to assist in development, however the framework does allow
for custom user-generated themes to be created and used. 

A theme is essentially just a dictionary of kwargs that is passed to all 
instances of that specific tk widget upon initialization. Currently there is
no restriction on what arguments of widget.__init__() you can pass through,
but by the same token you are restricted to those only. It is not possible to
theme post-instanciated properties like grid or position.

The theme itself must live in /frontend/stylings/themes/{theme_name}.json and it
must contain valid json for it to be loaded. It is to be a single dictionary formatted

{
    "widgetName": {
        "prop": "value",
        "prop2": "value"
    },
    ...
}

Currently the widgets in theme support are

[Button, Checkbutton, Combobox, Frame, Label, Subframe, Logmenu, Navbar]

All widget names and kwargs _are case and type sensitive_
"""

import json
import os


class ThemeController:
    """Controls all theme and styling related actions"""

    _FALLBACK_THEME = "dark"

    def __init__(self) -> None:
        # Private because we want to manipulate these on input
        self._theme_name = None
        self._theme = None
        # Base dir theme data must live in for the controller to index it
        self._THEME_DIR = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "themes/")
        self._theme_store = dict()

        # Index themes
        for fname in os.listdir(self._THEME_DIR):
            # Skip all non-json files
            if not fname.endswith((".json", ".JSON")):
                continue
            abspath = os.path.join(self._THEME_DIR, fname)
            # Validate the file actually contains json
            with open(abspath, "r") as f:
                if not self._validate_JSON(f):
                    continue
            # If the file is valid, add it to the theme store
            # TODO Implement validation for required elements?
            # feels kind of redundant for a modular theming framework
 
            tname, _ = os.path.splitext(fname)

            self._theme_store.update({
                tname: {
                    "abspath": abspath,
                    "fname": fname,
                }
            })

    def set_theme(self, theme: str) -> None:
        """Sets the current theme by name"""
        # The only case where this would likely happen would be if settings.ini were
        # manually changed to set theme to one that doesnt exist
        if not theme in self.get_theme_choices():
            raise AttributeError(
                "Theme was not found or indexed by the controller")
        # Since json data is only validated at runtime there is a possibility they
        # become invalid _during_ runtime, in which case we will use the fallback
        try:
            with open(self._theme_store[theme]["abspath"], "r") as f:
                dat = json.load(f)
                self._theme = dat
            self._theme_name = theme
        except:
            print(
                f"Error loading theme, falling back to default theme: {self._FALLBACK_THEME}")
            with open(self._theme_store[self._FALLBACK_THEME]["abspath"], "r") as f:
                dat = json.load(f)
                self._theme = dat
            self._theme_name = self._FALLBACK_THEME

    def get_theme(self) -> dict:
        """Returns the entire current theme"""
        return self._theme

    def get_widget_theme(self, widg: str) -> dict:
        """Searches the current theme for settings by widget name\n\n
        Will return an empty dict if it does not exist in the theme"""
        if widg in self._theme:
            return self._theme[widg]
        else:
            return dict()

    def get_theme_choices(self) -> list[str]:
        """Returns a list of theme names"""
        return list(self._theme_store.keys())

    def _validate_JSON(self, dat) -> bool:
        # NOTE Assumes dat is a TextIOWrapper, may want
        # a method that works with raw data or file name
        try:
            json.load(dat)
        except ValueError:
            return False
        return True


# Stores a globally accessible instance of the ThemeController
ctrl: ThemeController

# Avoid setting the variable directly from other modules
def load_controller():
    global ctrl
    ctrl = ThemeController()