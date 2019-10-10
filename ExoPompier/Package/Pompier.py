# -*- coding: utf-8 -*-

class Pompier:
    def __init__(self, position, board):
        self.position = position
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
        else:
            self.occupe -= 1
            if self.occupe == 0:
                """
                    Il faut éteindre le feu
                """
                self.board.eteindre(feu)
            
        
        print(self.position)
        
    def __repr__(self):
        return self.position
    
    
    
    
    
    
    
    
    
    
    
    
    
    