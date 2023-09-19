"""Settings controller"""

import os
from configparser import ConfigParser

_DEFAULT_SETTINGS: dict[str, dict[str, str]] = {
    'Interface': {
        'theme': 'Dark',
        'log_mode': 'App',
        'dmg_steps': 'False',
        'debug_mode': 'False'
    },
    'AutoSave': {
        'enabled': 'False',
        'path': ''
    },
    'Graph': {
        'title': 'DPS Over Time',
        'xlabel': 'Time (seconds)',
        'xlim': '45',
        'ylabel': 'DPS',
        'ylim': '300000',
        'initial_slots': '3',
        'colors': 'random'
    }
}


class Settings(ConfigParser):
    """D2DPSGPY Settings store"""

    def __init__(self) -> None:
        super().__init__()
        self.read_dict(_DEFAULT_SETTINGS)

        self._INI_PATH = os.path.abspath(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '../../settings.ini'))

        if os.path.exists(self._INI_PATH):
            success = self.read(self._INI_PATH)
            if not success:
                print('Error loading configuration file... Creating default')

    def reset_to_defaults(self) -> None:
        """Restores default settings"""
        self.read_dict(_DEFAULT_SETTINGS)
        self.save_settings()

    def save_settings(self) -> None:
        """Writes to predetermined ini file"""
        self.write(self._INI_PATH)

    def lget(self, varname: str) -> str | None:
        """
        Loose get() - Allows search by just option name

        Much more inneficient than get()
        """
        sect = ''
        for sect in self.sections():
            if self.has_option(sect, varname):
                return self.get(sect, varname)

    def lgetboolean(self, varname: str) -> bool | None:
        """
        Loose getboolean() - Allows search by just option name

        Much more inneficient than get()
        """
        sect = ''
        for sect in self.sections():
            if self.has_option(sect, varname):
                return self.getboolean(sect, varname)

    def lgetint(self, varname: str) -> bool | None:
        """
        Loose getint() - Allows search by just option name

        Much more inneficient than get()
        """
        sect = ''
        for sect in self.sections():
            if self.has_option(sect, varname):
                return self.getint(sect, varname)

    def lgetfloat(self, varname: str) -> bool | None:
        """
        Loose getint() - Allows search by just option name

        Much more inneficient than get()
        """
        sect = ''
        for sect in self.sections():
            if self.has_option(sect, varname):
                return self.getfloat(sect, varname)
