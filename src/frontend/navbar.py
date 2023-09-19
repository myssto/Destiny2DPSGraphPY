import tkinter as tk

from frontend.stylings.themecontroller import s_Navbar
from frontend.stylings.widgets import Frame


class NavBar(Frame):
    def __init__(self, master, menus: list):
        super().__init__(master=master)
        self.master = master
        self.pack()

        self.menus = menus

        self.init_menu()

    def init_menu(self):
        self.nav_ui()
        self.pack_forget()

    def nav_ui(self):
        # Create navbar and load tabs
        self.nav_listbox = tk.Listbox(self, **s_Navbar())
        self.nav_listbox.pack()
        for idx, menu in enumerate(self.menus):
            self.nav_listbox.insert(idx+1, menu.navname)

        # Set default selection to 'Graph'
        self.nav_listbox.select_set(0)
        # Handle clicks on the navbar
        self.nav_listbox.bind('<<ListboxSelect>>', self.menu_select)

    def menu_select(self, evt):
        # Grab which option was clicked
        index = int(evt.widget.curselection()[0])
        target = self.menus[index]

        if target.winfo_viewable():
            return

        self.menus.remove(target)
        for menu in self.menus:
            menu.pack_forget()
        target.pack(side=tk.RIGHT, fill=tk.Y)
        self.menus.insert(index, target)
