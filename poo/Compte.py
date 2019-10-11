# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:03:11 2019

@author: miguel
"""

"""
    Classe Compte qui a en attribut (self.quelquechose) "solde"
    Une methode retrait(self, montant) : qui retire un montant au solde
    Une methode depot(self, montant) : qui ajoute un montant au solde
"""

class NegativeValueException(Exception):
    pass

class Compte:
    def __init__(self, solde_initial):
        self.solde = solde_initial
    def depot(self, montant):
        if montant < 0:
            raise NegativeValueException()
        self.solde += montant
    def retrait(self, montant):
        assert type(montant) == float or type(montant) == int, "Le montant "
        assert montant > 0, "Le montant doit être positif"
        self.solde -= montant
