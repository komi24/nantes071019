# -*- coding: utf-8 -*-
from .Feu import Feu
from .Pompier import Pompier

class Board:
    def __init__(self):
        self.liste_feux = [Feu([5,3]), Feu([3,1])]
        self.liste_pompiers = [Pompier([2,0], self)]
    
    def run(self):
        self.liste_pompiers[0].se_deplacer(self.liste_feux[0])
        self.display()
    
    def eteindre(self, feu):
        self.liste_feux.remove(feu)
        
    def display(self):
        for i in range(10):
            line = []
            for j in range(10):
                if self.is_pompier([i,j]):
                    line.append("x")
                elif self.is_feu([i,j]):
                    line.append("o")
                else:
                    line.append(" ")
            print(line)

    def is_pompier(self, position):
        for pomp in self.liste_pompiers:
            if pomp.position == position:
                return True
        return False

    def is_feu(self, position):
        for feu in self.liste_feux:
            if feu.position == position:
                return True
        return False
        
