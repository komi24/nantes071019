# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Button, Frame, StringVar
from tkinter import LEFT, RIGHT, BOTTOM, TOP

fen = Tk()

#
#button1 = Button(fen, text="Bouton 1")
#button1.pack(side=RIGHT)
#
#button2 = Button(fen, text="Bouton 2")
#button2.pack(side=BOTTOM)
#
#button3 = Button(fen, text="Bouton 3")
#button3.pack(side=LEFT)
#
#button4 = Button(fen, text="Bouton 4")
#button4.pack()

def click_btn(e):
    print("hello", e.widget.cget("text"))
    chaine.set(e.widget.cget("text"))

chaine = StringVar()
chaine.set("0")

label = Label(fen, textvariable=chaine, height=2)
label.pack()

frame = Frame(fen)
frame.pack()
for i in range(3):
    for j in range(3):
        button = Button(frame, text=f"{3*(2-i)+j+1}", width=5, height=2)
        button.grid(column=j, row=i)
        button.bind("<Button-1>", click_btn)

button_zero = Button(fen, text="0", height=2)
button_zero.pack(expand=True, fill="x")

fen.mainloop()


















