import tkinter as tk
import tkinter.ttk as ttk

class Viewer(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        fsize = 800
        tk.Canvas.__init__(self, parent, *args, **kwargs, width=fsize, height=fsize, bg='#424242')
        self.parent = parent

        self.video = '/Users/degoldschmidt/Desktop/tracking_test_data/cam01_2017-11-24T08_26_19.avi'
        self.frame = None
        self.cap = 


    def next_frame(self):
        _, self.frame = self.cap.read()
        img = self.frame.copy()
        img = cv2.resize(img, (fsize, fsize))
        return img

    def update(self):

        self.photo = ImageTk.PhotoImage(image = Image.fromarray())
        self.create_image(0, 0, image = self.photo, anchor = tk.NW)
