"""Custom Exceptions"""

class ThemeNotFoundError(FileNotFoundError):
    pass

class InvalidThemeElementError(ValueError):
    pass