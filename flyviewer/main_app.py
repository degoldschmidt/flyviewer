import argparse
import tkinter as tk
import tkinter.ttk as ttk
import os, platform, subprocess
import flyviewer.defaults as defs
from flyviewer.data_object import Data
from flyviewer.graph import Graph
from flyviewer.treeview import TreeView
from flyviewer.viewer import Viewer
#import flyviewer.style as style
viewer_frame = 'Viewer.TFrame'
treeview_frame = 'Treeview.TFrame'
graph_frame = 'Graph.TFrame'

def get_background_of_widget(widget):
    try:
        # We assume first tk widget
        background = widget.cget("background")
    except:
        # Otherwise this is a ttk widget
        style = widget.cget("style")

        if style == "":
            # if there is not style configuration option, default style is the same than widget class
            style = widget.winfo_class()

        background = ttk.Style().lookup(style, 'background')

    return background

def raise_app(root: tk.Tk):
    root.attributes("-topmost", True)
    if platform.system() == 'Darwin':
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
        script = tmpl.format(os.getpid())
        output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
    root.after(0, lambda: root.attributes("-topmost", False))

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

def get_figure():
    fig = Figure(figsize=(5, 1.2), dpi=100)
    fig.add_subplot(111)#.plot(t, 2 * np.sin(2 * np.pi * t))
    #fig.axes.get_yaxis()
    fig.axes[0].spines['right'].set_visible(False)
    fig.axes[0].spines['top'].set_visible(False)

    fig.axes[0].set_xticks([0, 180000, 360000])
    fig.axes[0].set_yticks([-2,0,2])
    x0, x1 = fig.axes[0].get_xticks()[0], fig.axes[0].get_xticks()[-1]
    y0, y1 = fig.axes[0].get_yticks()[0], fig.axes[0].get_yticks()[-1]
    fig.axes[0].spines['left'].set_bounds(y0, y1)
    fig.axes[0].spines['bottom'].set_bounds(x0, x1)
    fig.axes[0].set_ylabel('Global\nmotion')
    fig.tight_layout()
    fig.axes[0].set_xlabel('frames', labelpad=-2)
    return fig

class MainApp(tk.Tk):
    def __init__(self, *args, input=None, **kwargs):
        tk.Tk.__init__(self,None)
        self.title(defs.title)
        self.grid()

        #self.input = input
        style = ttk.Style()
        style.theme_use('default') # select the Unix theme

        self.data = Data()
        self.tree = TreeView(self)
        self.tree.grid(row=0, rowspan=5, column=0, columnspan=3, sticky='nsew')
        self.viewer = Viewer(self)
        self.viewer.grid(row=0, rowspan=4, column=3, columnspan=4, sticky='nsew')
        self.graph = Graph(self)
        self.graph.grid(row=4, column=3, columnspan=4, sticky='nsew')


        raise_app(self)
        for i in range(defs.ncols):
            self.grid_columnconfigure(i,weight=1)
        for i in range(defs.nrows):
            self.grid_rowconfigure(i,weight=1)

        self.update()
        self.mainloop()

    def update(self):
        self.graph.update()
        self.after(1, self.update)

def main():
    parser = argparse.ArgumentParser()
    # add required and optional arguments
    parser.add_argument('input', nargs='?', default=os.getcwd())
    args = parser.parse_args()
    #root = tk.Tk()
    MainApp(input=args.input)

if __name__ == '__main__':
    main()
