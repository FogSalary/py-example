import os
import tkinter as tk
from tkinter import Menu


window = tk.Tk()
window.title("Menu test windos")
window.geometry("500x500")

# property
# bg: background color (menu color)
# fg: foreground color (font color)
# font: font(style, size)
# width: text width
# bd: boder width
# height: text height

# function
# add_cascade: add sub item
# add_command: add command(label param is display content)
# add_separator: add separator
# add_checkbutton: add checkbutton

menubar = Menu(window)

filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="Open File")

filemenu.add_separator()
filemenu.add_command(label="Save")
# add draw menu to menubar
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=editmenu)

menubar.add_checkbutton()

# display menu
window.config(menu=menubar)
window.mainloop()
