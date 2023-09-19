"""Container widget for Weapon Creation sub-menus"""

import tkinter as tk
from tkinter import ttk

from frontend.submenus.weaponsmenu.buffcalc import BuffCalc
from frontend.submenus.weaponsmenu.framed import FramedCreation
from frontend.submenus.weaponsmenu.sandbox import SandboxCreation

import backend.backend as backend


class WeaponsMenu(tk.Frame):
    """Container for WeaponsMenu submenus"""

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.config(**self.master.frame_style)
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.navname = 'Weapons'

        self.frame_style = self.master.frame_style.copy()
        self.frame_style['highlightthickness'] = 0

        self.submenus = {
            'framed': FramedCreation(self),
            'sandbox': SandboxCreation(self),
            'buffcalc': BuffCalc(self)
        }

        self.init_menu()

    def init_menu(self):
        self.pack_forget()

    def update_weapons(self, **_):
        pass

    def show_new_weapon(self, **_):
        pass