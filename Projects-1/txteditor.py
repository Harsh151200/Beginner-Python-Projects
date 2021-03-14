# GUI Python Program

from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename, asksaveasfilename
import os
from pygments import highlight


root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
root.title("Untitled-TryCatch Text Editor")

file = None
filename = None


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do not do anything")
    button.pack()


def open_file():
    global file
    global filename
    file = askopenfile(mode='r')
    if file is not None:
        content = file.read()
        filename = file.name
        text.insert(INSERT, content)
        filename_only = filename.split("/")[-1]
        root.title(filename_only+"-TryCatch Text Editor")



def save_file():
    global filename
    global file
    if(filename != None and file != None):
        f = open(filename, "r+")
        f.seek(0)
        f.truncate()
        text_data = text.get(1.0, "end-1c")
        f.write(text_data)

    else:
        file = asksaveasfile()
        filename = file.name
        text_data = text.get(1.0, "end-1c")
        f = open(filename, "r+")
        f.write(text_data)
        filename_only = filename.split("/")[-1]
        root.title(filename_only+"-TryCatch Text Editor")



def save_as_file():
    global filename
    global file
    file = asksaveasfile()
    filename = file.name
    text_data = text.get(1.0, "end-1c")
    f = open(filename, "r+")
    f.write(text_data)
    filename_only = filename.split("/")[-1]
    root.title(filename_only+"-TryCatch Text Editor")


def close_file():
    global file
    global filename
    text.delete(1.0,"end-1c")
    root.title("Untitled"+"-TryCatch Text Editor")
    file.close()
    file = None
    filename = None
    
    
    


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as...", command=save_as_file)
filemenu.add_command(label="Close", command=close_file)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


text = Text(root)
text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="aqua", foreground="green")

root.mainloop()

print(filename)
