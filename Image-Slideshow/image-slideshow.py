"""
Slide Show - Make an application that shows various pictures in a slide show format.
Optional: Try adding various effects like fade in/out, star wipe and window blinds transitions.
"""

from tkinter import*
from PIL import ImageTk, Image
import time


class Slider:
    def __init__(self, root):
        self.root = root
        self.root.title("TryCatch Image Slideshow")
        self.root.geometry("900x500")
        image = Image.open('Image-Slideshow/lakes.png')
        image = image.resize((700, 400), Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image)
        image = Image.open('Image-Slideshow/mountains.jpg')
        image = image.resize((700, 400), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image)

        Frame_slider = Frame(self.root)
        Frame_slider.place(x=150, y=70, width=600, height=350)
        self.lbl1 = Label(Frame_slider, image=self.image1, bd=0)
        self.lbl1.place(x=0, y=0)
        self.lbl2 = Label(Frame_slider, image=self.image2, bd=0)
        self.lbl2.place(x=1920, y=0)
        self.x = 1920
        self.slider_func()

    def slider_func(self):
        self.x -= 1
        if self.x == 0:
            self.x = 1100
            time.sleep(1)
            self.new_im = self.image1
            self.image1 = self.image2
            self.image2 = self.new_im
            self.lbl1.config(image=self.image1)
            self.lbl2.config(image=self.image2)
        self.lbl2.place(x=self.x, y=0)
        self.lbl2.after(1, self.slider_func)


root = Tk()
obj = Slider(root)
root.configure(bg="powderblue")
photo = PhotoImage(file="Image-Slideshow/gallery.png")
title = Label(root, text="Image Slideshow",
               fg="Black",bg="powderblue" ,font=("Arial", 25, 'bold')).place(x=320, y=10)
root.iconphoto(False, photo)
root.mainloop()
