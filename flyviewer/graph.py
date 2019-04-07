import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler, MouseEvent
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

def create_figure():
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

class Graph(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs, width=800, height=200, bg='#ffffff')
        self.parent = parent
        optionList = ('train', 'plane', 'boat')
        self.v = tk.StringVar()
        self.v.set(optionList[0])
        self.om = tk.OptionMenu(self, self.v, *optionList)
        self.om.grid(row=0, column=0, sticky='nsew')

        self.fig = create_figure()
        self.update()
        self.canvas.get_tk_widget().grid(row=0, column=1, sticky='nsew')

        for i in range(2):
            self.grid_columnconfigure(i,weight=1)
        for i in range(1):
            self.grid_rowconfigure(i,weight=1)


    def update(self):
        print('Change to', self.v.get())
        self.fig.axes[0].set_ylabel(self.v.get())
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)  # A tk.DrawingArea.
        self.canvas.draw()
