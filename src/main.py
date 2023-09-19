import configparser
import os
import sys
import tkinter as tk

import backend.backend as backend
from backend.utility.settings import Settings
import frontend.stylings.themecontroller as themecontroller
from frontend.graphmenu import GraphMenu
from frontend.logemenu import LogMenu
from frontend.navbar import NavBar
from frontend.optionsmenu import OptionsMenu
from frontend.weaponsmenu import WeaponsMenu

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Destiny2DPSGraphPY')
        self.master.resizable(False, False)
        self.pack()

        self.initGUI()

    def load_settings(self):
        # Instance settings
        self.settings = Settings()
        self.default_padding = {'padx': 5, 'pady': 5, 'sticky': 'NSW'}
        self.combo_style = {'width': 17, 'state': 'readonly'}
        themecontroller.theme = self.settings.interface_theme.lower()
        # Access and apply settings
        if self.settings.interface_theme.lower() == 'dark':
            self.configure(bg='#1E1E1E')
            self.master.configure(bg='#1E1E1E', highlightthickness=2, highlightcolor='#000000')
            self.label_style = {'bg': '#1E1E1E', 'fg': '#CCCCCC'}
            self.frame_style = {'bg': '#1E1E1E', 'highlightcolor': '#000000', 'highlightbackground': '#000000', 'highlightthickness': 2}
            self.frame_bg = "#1E1E1E"
            self.check_button_style = {'bg': '#1E1E1E', 'fg': '#CCCCCC', 'selectcolor': '#1E1E1E'}
            self.button_style = {'bg': '#1E1E1E', 'fg': '#CCCCCC', 'height': 1, 'width': 17, 'relief': 'ridge'}
            self.matplotlib_bg = "#1E1E1E"
            self.matplotlib_fg = "#CCCCCC"
            self.listbox_bg = "#808080"
            self.white_text = "#CCCCCC"
            self.navbar_bg = '#1E1E1E'
            self.navbar_fg = '#CCCCCC'
        else:
            # TODO Light mode should always be checked after changes to the ui
            self.configure(bg='#FFFFFF')
            self.master.configure(bg='#FFFFFF', highlightthickness=2, highlightcolor='#000000')
            self.label_style = {'bg': '#FFFFFF', 'fg': '#000000'}
            self.frame_style = {'bg': '#FFFFFF', 'highlightcolor': '#000000', 'highlightbackground': '#FFFFFF', 'highlightthickness': 2}
            self.frame_bg = "#FFFFFF"
            self.check_button_style = {}
            self.button_style = {}
            self.matplotlib_bg = "#FFFFFF"
            self.matplotlib_fg = "#000000"
            self.listbox_bg = "#808080"
            self.white_text = "#000000"
            self.navbar_bg = '#FFFFFF'
            self.navbar_fg = '#000000'

        self.navbar_style = {
            'bg': self.navbar_bg, 
            'fg': self.navbar_fg,
            'height': 5,
            'highlightthickness': 0,
            'borderwidth': 0,
            'highlightcolor': '#000000',
            'selectbackground': self.listbox_bg,
            'selectforeground': '#FFFFFF',
            'selectborderwidth': 0,
            'activestyle': 'none',
            'font': 20,
            'width': 10,
            'exportselection': False
        }

        # Enable window screenshots in debug mode
        if self.settings.debug_mode:
            self.master.bind('<Control-a>', lambda _: self.optionsmenu.debug_testfunc())
            self.master.bind('<Control-s>', lambda e: self.optionsmenu.debug_ssgui(e))

        backend.set_do_dmg_prints(self.settings.do_dmg_prints)

    def initGUI(self):
        # Load settings
        self.load_settings()

        # Load menus
        self.graphmenu = GraphMenu(self)
        self.weaponsmenu = WeaponsMenu(self)
        self.optionsmenu = OptionsMenu(self)
        self.logmenu = LogMenu(self)

        self.navbar = NavBar(self, [
            self.graphmenu,
            self.weaponsmenu,
            self.optionsmenu,
            self.logmenu,
        ])

        # Log mode
        redirect_logs(self.logmenu.log_text, self.settings.log_mode)
        # Auto import
        if firstrun:
            if self.settings.do_auto_save:
                if os.path.exists(self.settings.auto_save_path):
                    self.optionsmenu.import_weps_hdlr(self.settings.auto_save_path)
                else:
                    print(f'Auto Import Error: Expected file at `{self.settings.auto_save_path}` and none existed')
        
        # Initial weaponsmenu
        self.util_update_wep_names(first=True)
        self.weaponsmenu.show_new_weapon()

        # Display navbar and first menu
        self.navbar.pack(side=tk.LEFT, fill=tk.Y)
        self.graphmenu.pack(side=tk.RIGHT, fill=tk.Y)

    def util_update_wep_names(self, first:bool=False):
        self.graphmenu.update_weapons()
        self.weaponsmenu.update_weapons(first=first)

    def util_valfloat(self, char):
        if char in '0123456789.':
            return True
        else:
            return False
        
    def util_valint(self, char):
        if char in '0123456789':
            return True
        else:
            return False

def redirect_logs(text_widget: tk.Widget, log_mode: str):
    def write_to_app(string):
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, string)
        text_widget.see(tk.END)
        text_widget.config(state=tk.DISABLED)

    if log_mode in ['App', 'Both']:
        use_decorator = True if log_mode == 'Both' else False
    else:
        write_to_app('Log Menu will not print logs due to selecting "Console" for Log Mode option' +
                     '\nCheck your console for relevant logs')
        sys.stdout.write = stdoutwrite
        return

    def decorator(func):
        def inner(inpStr):
            try:
                write_to_app(inpStr)
                return func(inpStr)
            except:
                return func(inpStr)
        return inner
    
    if use_decorator:
        sys.stdout.write = decorator(stdoutwrite)
    else:
        sys.stdout.write = write_to_app

def start_gui() -> None:
    global root
    root = tk.Tk()
    # Use PhotoImage to open the PNG file
    img = tk.PhotoImage(file='images/simpleicon-notext.png')
    # Set the window icon
    root.iconphoto(False, img)
    app = GUI(master=root)
    app.mainloop()

def restart_gui() -> None:
    global firstrun
    firstrun = False
    start_gui()

firstrun = True
stdoutwrite = sys.stdout.write
start_gui()