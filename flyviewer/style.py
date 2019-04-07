import tkinter as tk
import tkinter.ttk as ttk

viewer_frame = 'Viewer.TFrame'
treeview_frame = 'Treeview.TFrame'
graph_frame = 'Graph.TFrame'

def initialize():
    style = ttk.Style()
    style.configure(viewer_frame, background='red')
    style.configure(treeview_frame, background='DeepPink2')
    style.configure(graph_frame, background='orange')
