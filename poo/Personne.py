# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:03:38 2019

@author: miguel
"""
from Compte import Compte

class Personne:
    def __init__(self, firstname, age_initial=34, solde=1000):
        self.nom = firstname
        self.age = age_initial
        self.compte = Compte(solde)
    def dire_bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}")
    def dire_bonjour_a(self, autre_personne):
        print(f"Bonjour {autre_personne.nom}, je m'appelle {self.nom}")
    def transfert(self, autre_personne, montant):
        self.compte.retrait(montant)
        autre_personne.compte.depot(montant)
    def __repr__(self):
        return f"Je m'appelle : {self.nom}."
    
    def __lt__(self, autre):
#        return self.age < autre.age
        return self.compte.solde < autre.compte.solde

    def __eq__(self, autre):
#        return self.age == autre.age
        return self.compte.solde == autre.compte.solde
        
