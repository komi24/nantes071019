# -*- coding: utf-8 -*-

#from MonPackage import module1
#
#print("Hello world")
#module1.dire_bonjour()

#from MonPackage import module1 as md
#
#print("Hello world")
#md.dire_bonjour()

from MonPackage.module1 import dire_bonjour
from MonPackage import MA_CONSTANTE

#print("Hello world")
#print(MA_CONSTANTE)
#dire_bonjour("Guillemette")
#dire_bonjour("Guillemette", lng="PT")
dire_bonjour()

"""
    Dans module1, créer une fonction dire_bonjour(name, lng...) 
    lng par défaut à "FR" (param optionnel)
    Si lng = "FR" -> Bonjour {name}
    Si lng = "EN" -> Hello {name}
    Si lng = "ES" -> Hola {name}
    Si lng = "PT" -> Bom dia {name}
    Si lng = "ZH" -> Ni hao {name}
"""













