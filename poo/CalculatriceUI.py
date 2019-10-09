# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from tkinter import Tk, Label, Button, Frame, StringVar
from tkinter import LEFT, RIGHT, BOTTOM, TOP

class CalculatriceUI:
    def __init__(self):
        self.fen = Tk()
        self.chaine = StringVar()
        self.chaine.set("")
        
        self.label = Label(self.fen, textvariable=self.chaine, height=2)
        self.label.pack()
        
        self.button_valider = Button(self.fen, text="valider", height=2)
        self.button_valider.pack(side=BOTTOM, expand=True, fill="x")
        self.button_valider.bind("<Button-1>", self.handle_validate)

        self.frame_op = Frame(self.fen)
        self.frame_op.pack(side=RIGHT)
        
        for op in ['+','-','*','/']:
            button = Button(self.frame_op, text=op, width=5, height=2)
            button.bind("<Button-1>", self.handle_op)
            button.pack()
        
        self.frame = Frame(self.fen)
        self.frame.pack()
        for i in range(3):
            for j in range(3):
                button = Button(self.frame, text=f"{3*(2-i)+j+1}", width=5, height=2)
                button.grid(column=j, row=i)
                button.bind("<Button-1>", self.handle_number)
        
        self.button_zero = Button(self.fen, text="0", height=2)
        self.button_zero.pack(expand=True, fill="x")
        self.button_zero.bind("<Button-1>", self.handle_number)
        
        self.fen.mainloop()

    def handle_validate(self, e):
        """
            Gère le click sur le bouton valider
        """
        pass
    def handle_number(self, e):
        """
            Gère le click sur un bouton numérique
        """
        pass
    def handle_op(self, e):
        """
            Gère le click sur un bouton opérateur
        """
        pass

