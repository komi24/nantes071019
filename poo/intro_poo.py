# -*- coding: utf-8 -*-

class NegativeValueException(Exception):
    pass


"""
    1- Rajouter un compte dans la classe personne
    2- Ajouter une méthode transfert(self, autre_personne, montant)
"""
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
        
"""
    Classe Compte qui a en attribut (self.quelquechose) "solde"
    Une methode retrait(self, montant) : qui retire un montant au solde
    Une methode depot(self, montant) : qui ajoute un montant au solde
"""
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

un_compte = Compte(1000)
un_compte.depot(500)
un_compte.retrait(500)

try:
    une_personne = Personne("Marjorie", 32)
    une_personne.dire_bonjour()
    une_deuxieme_personne = Personne("Isabelle", 80)
    une_deuxieme_personne.dire_bonjour()
    
    une_personne.transfert(une_deuxieme_personne, -200)
except NegativeValueException as e:
    print("Une erreur est survenue")
except AssertionError:
    print("Erreur d'assertion")
except:
    print("N'importe quelle erreur")

print(une_personne.nom)
print(une_deuxieme_personne.nom)


#liste_personnes = [Personne() for i in range(10)]

# Créer une liste de personne qui ont 34 ans à partir de la liste de noms
liste_noms = ["Mélanie", "Henri", "Thomas", "Bruna", "Charlie"]
liste_ages = [18, 54, 41, 32, 26]

liste_personnes = []

for i in range(len(liste_noms)):
    liste_personnes.append(Personne(liste_noms[i], liste_ages[i]))

for nom, age in zip(liste_noms, liste_ages):
    liste_personnes.append(Personne(nom, age))    

print(liste_personnes)




















