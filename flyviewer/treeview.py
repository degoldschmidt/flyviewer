import tkinter as tk
import tkinter.ttk as ttk

class TreeView(ttk.Frame):
    def __init__(self, parent, data=None, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs, width=900, height=1000)
        self.parent = parent

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        self.tree = ttk.Treeview(self, height=45, columns=['video', 'condition'], show='headings', style="mystyle.Treeview")
        self.tree.heading('video', text='video')
        self.tree.heading('condition', text='condition(s)')
        self.tree.grid(sticky='nsew')
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.data = data

        self.load_dir()

    def OnDoubleClick(self, event):
        item = self.tree.selection()[0]
        itemtext = self.tree.item(item,"text")
        print("you clicked on", itemtext)
        self.parent.run_video(self.data.get_video(itemtext))


    def load_dir(self):
        list_videos = self.data.videos
        list_conditions = self.data.conditions
        for vid, cond in zip(list_videos, list_conditions):
            self.tree.insert("", tk.END, text=vid, values=(vid, cond))
