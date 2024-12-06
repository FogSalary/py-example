import os
import tkinter as tk


window = tk.Tk()
window.title("Label test window")
window.geometry("500x500")

# text: label name
# font: font(style, size)
# bg/background: background color(label color)
# fg/foreground: foreground color(font color)
# width: label width
# height: label height
# anchor: control label text position, (param: S/W/E/N/SE/SW/NW/NE/CENTER, default: center)
# bitmap: position map
# relief: 3D effect (param: FALT/SUNKEN/RAISED/GROOVE/RIDGE. default: FLAT)
# image: Use with PhotoImage, image only support gif format.
# compound: image and text display together
# padx: setting label text and label border x direction distance
# pady: setting label text and label border y direction distance
# cursor: mouse move above btn, cursor shape, param: arrow/circle/cross/puls ...
# justify: display multi text, set different line align method, param: LEFT/RIGHT/CENTER
# state: btn state, param: NORMAL/ACTIVE/DISABLED, default is NORMAL
# wraplength: set every line text width, unit is screen uint.
# underline: underline, default false; value is underline string index, 0 means first str have underline, and so on



window.mainloop()