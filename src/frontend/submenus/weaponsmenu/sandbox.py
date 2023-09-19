import tkinter as tk
from tkinter import ttk

class SandboxCreation(ttk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.sumaster = master.master
        # self.config(**self.master.frame_style)
        self.pack(side=tk.LEFT, fill=tk.Y)
        self.navname = 'Sandbox Creation'
        
        self.init_menu()

    def init_menu(self):
        pass