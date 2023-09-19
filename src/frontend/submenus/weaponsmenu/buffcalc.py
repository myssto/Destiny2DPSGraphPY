import tkinter as tk
from tkinter import ttk

class BuffCalc(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master=master)
        self.master = master
        self.sumaster = master.master
        # self.config(**self.master.frame_style)
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.navname = 'BuffCalc'

        self.__init_menu()

    def __init_menu(self) -> None:
        pass

    def __buffcalc_gui(self) -> None:
        self.vars = {
            'deb_cnst': tk.BooleanVar(),
            'buff_cnst': tk.BooleanVar(),
            'wdmg_cnst': tk.BooleanVar(),
            'total': tk.StringVar()
        }

        self.widgets = {
            'header': [tk.Label(self, text='Buff / Debuff Calculator', **self.master.label_style)],

            'deb': [tk.Label(self, text='Debuff', **self.master.label_style),
                    ttk.Combobox(self, values=self.buff_choices['deb'], **self.master.combo_style)],
            
            'deb_cnst': [tk.Checkbutton(self, variable=self.menu_vars['buffcalc']['deb_cnst'], 
                                        text='Constantly Applied', **self.master.check_button_style)],

            'buff': [tk.Label(self, text='Empower', **self.master.label_style),
                     ttk.Combobox(self, values=self.buff_choices['buff'], **self.master.combo_style)],

            'buff_cnst': [tk.Checkbutton(self, variable=self.menu_vars['buffcalc']['buff_cnst'], 
                                         text='Constantly Applied', **self.master.check_button_style)],

            'wdmg': [tk.Label(self, text='Weapon Damage', **self.master.label_style),
                     ttk.Combobox(self, values=self.buff_choices['wdmg'], **self.master.combo_style)],
            
            'wdmg_cnst': [tk.Checkbutton(self, variable=self.menu_vars['buffcalc']['wdmg_cnst'], 
                                         text='Constantly Applied', **self.master.check_button_style)],

            'misc': [tk.Label(self, text='Misc', **self.master.label_style)],

            'packhunter': [tk.Checkbutton(self, text='Wolfpack Rounds', **self.master.check_button_style)],

            'pad': [],

            'total': [tk.Label(self, text='Total Multiplier', **self.master.label_style),
                      ttk.Entry(self, textvariable=self.menu_vars['buffcalc']['total'], state="readonly")]
        }