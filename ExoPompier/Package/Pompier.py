# -*- coding: utf-8 -*-
from random import randint as rd


class Pompier:
    def __init__(self, board):
        self.position = [rd(0,10), rd(0,10)]
        self.occupe = 0
        self.board = board
    def se_deplacer(self, feu):
        """
            si position du pompier en 0 < position du feu en 0
            ajouter un à la position du pompier en 0
            
            si position du pompier en 0 > position du feu en 0
            retirer un à la position du pompier en 0
    
            si position du pompier en 1 < position du feu en 1
            ajouter un à la position du pompier en 1
    
            si position du pompier en 1 > position du feu en 1
            retirer un à la position du pompier en 1
        """
        if self.occupe == 0:
            if self.position[0] < feu.position[0]:
                self.position[0] += 1
            elif self.position[0] > feu.position[0]:
                self.position[0] -= 1
            elif self.position[1] < feu.position[1]:
                self.position[1] += 1
            elif self.position[1] > feu.position[1]:
                self.position[1] -= 1
            else:
                self.occupe = 5
                self.board.eteindre(feu)
        else:
            self.occupe -= 1
            
        
        print(self.position)
        
    def __repr__(self):
        return self.position
    
    
    
    
    
    
    
    
    
    
    
    
    
    