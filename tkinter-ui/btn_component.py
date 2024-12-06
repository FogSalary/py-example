import os
import tkinter as tk


window = tk.Tk()
window.title("Btn test window")
window.geometry("500x500")

# parameter
# text: btn text content
# font: font(style, size)
# bg/background: background color(btn color)
# fg/foreground: foreground color(font color)
# width: btn width
# height: btn height
# command: slot func, when btn click, run slot func
# padx: setting btn text and btn border x direction distance
# pady: setting btn text and btn border y direction distance
# bd/borderwidth: btn border width
# anchor: btn text location (param: S/W/E/N/SE/SW/NW/NE/CENTER, default: center)
# image: Use with PhotoImage, image only support gif format.
# relief: 3D effect (param: FALT/SUNKEN/RAISED/GROOVE/RIDGE. default: FLAT)
# bitmap: position image
# compound: image and text display together
# cursor: mouse move above btn, cursor shape, param: arrow/circle/cross/puls ...
# justify: display multi text, set different line align method, param: LEFT/RIGHT/CENTER
# state: btn state, param: NORMAL/ACTIVE/DISABLED, default is NORMAL
# wraplength: set every line text width, unit is screen uint.
# underline: underline, default false; value is underline string index, 0 means first str have underline, and so on

btn1 = tk.Button(window, text="btn1", bg="red", fg="blue")
btn1.pack()

btn2 = tk.Button(window, text="btn2", padx=20, pady=20)
btn2.pack()

window.mainloop()