import tkinter as tk
import tkinter.ttk as ttk

class TreeView(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs, width=900, height=1000)
        self.parent = parent
        self.tree = ttk.Treeview(self, height=45)
        self.tree.grid(sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
