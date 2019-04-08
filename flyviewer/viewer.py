import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image
from PIL import ImageTk
import cv2
import os
import os.path as op

class Viewer(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        self.fsize = 800
        tk.Canvas.__init__(self, parent, *args, **kwargs, width=self.fsize, height=self.fsize, bg='#424242')
        self.parent = parent

        self.video = None
        self.frame = None
        self.playing = False

    def init_video(self, filename):
        self.cap = cv2.VideoCapture(filename)
        self.current_video = op.basename(filename)
        self.playing = True
        self.update()

    def next_frame(self):
        _, self.frame = self.cap.read()
        img = self.frame.copy()
        img = cv2.resize(img, (self.fsize, self.fsize))
        return img

    def update(self):
        if self.playing:
            frame = self.next_frame()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            self.create_image(0, 0, image = image, anchor = tk.NW)
            self.image = image
