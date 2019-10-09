# -*- coding: utf-8 -*-
from CalculatriceUI import CalculatriceUI


class Calculatrice(CalculatriceUI):
    def __init__(self):
        CalculatriceUI.__init__(self)
        self.operand1 = 0
        self.operand2 = 0
        self.operator = '+'

    def handle_validate(self, e):
        """
            Gère le click sur le bouton valider
            Afficher operand1 + operand2 si self.operator == '+'
            Afficher operand1 - operand2 si self.operator == '-'
            Afficher operand1 * operand2 si self.operator == '*'
            Afficher operand1 / operand2 si self.operator == '/'
        """
        self.operand2 = int(self.chaine.get())
        if self.operator == "+":
            self.chaine.set(str(self.operand1 + self.operand2))
        elif self.operator == "-":
            self.chaine.set(str(self.operand1 - self.operand2))
        elif self.operator == "*":
            self.chaine.set(str(self.operand1 * self.operand2))
        elif self.operator == "/":
            self.chaine.set(str(self.operand1 // self.operand2))

    def handle_number(self, e):
        """
            Gère le click sur un bouton numérique
        """
        self.chaine.set(self.chaine.get() + e.widget.cget("text"))

    def handle_op(self, e):
        """
            Gère le click sur un bouton opérateur
            mettre l'opérateur dans self.operator
            mettre l'affichage courant dans self.operand1
            reset l'affichage : self.chaine...
        """
        self.operator = e.widget.cget("text")
        self.operand1 = int(self.chaine.get())
        self.chaine.set("")






















