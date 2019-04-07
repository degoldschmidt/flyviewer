import tkinter

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        label = tkinter.Label(self,anchor="center",bg="green")
        label.grid(column=1,columnspan=4,rowspan=4,row=0,sticky='NSEW')

        label3 = tkinter.Label(self,anchor="center",bg="red")
        label3.grid(column=0,row=0,rowspan=5,sticky='NSEW')

        label5 = tkinter.Label(self,anchor="center",bg="blue")
        label5.grid(column=1,columnspan=4,row=4,sticky='NSEW')


        for i in range(5):
            self.grid_columnconfigure(i,weight=1)
            self.grid_rowconfigure(i,weight=1)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title("Test App")
    app.mainloop()
