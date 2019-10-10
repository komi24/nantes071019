# -*- coding: utf-8 -*-
from .Feu import Feu
from .Pompier import Pompier
import os
from random import randint as rd
import numpy as np


class Board:
    def __init__(self):
        self.liste_feux = [Feu() for i in range(8)]
        self.liste_pompiers = [Pompier(self) for i in range(3)]
    
    def run(self):
        for pomp in self.liste_pompiers:
            pomp.se_deplacer(self.feu_le_plus_proche(pomp))
        self.display()
    
    def eteindre(self, feu):
        self.liste_feux.remove(feu)
        
    def display(self):
        os.system("clear")
        for i in range(11):
            line = []
            for j in range(11):
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
        
    def feu_le_plus_proche(self, pompier):
        feu_proche = self.liste_feux[0]
        distance_min = self.distance(pompier, feu_proche)
        
        for feu in self.liste_feux:
            distance_cour = self.distance(pompier, feu)
            if distance_cour < distance_min:
                distance_min = distance_cour
                feu_proche = feu
        return feu_proche
    
    def distance(self, pompier, feu):
        return abs(pompier.position[0] - feu.position[0]) + \
            abs(pompier.position[1] - feu.position[1]) 
