# -*- coding: utf-8 -*-
#LNG_HELLO = {
#    "FR": dire_bonjour_fr,
#    "EN": dire_bonjour_en,
#    "ES": dire_bonjour_es,
#    "PT": dire_bonjour_pt,
#    "ZH": dire_bonjour_zh,
#}
#
#def dire_bonjour_fr(name):
#    print(f"Bonjour {name}")
#def dire_bonjour_en(name):
#    print(f"Hello {name}")
#def dire_bonjour_es(name):
#    print(f"Hola {name}")
#def dire_bonjour_pt(name):
#    print(f"Bom dia {name}")
#def dire_bonjour_zh(name):
#    print(f"Ni hao {name}")
#
#def dire_bonjour(name, lng="FR"):
#    LNG_HELLO[lng](name)

#LNG_HELLO = {
#    "FR": "Bonjour",
#    "EN": "Hello",
#    "ES": "Hola",
#    "PT": "Bom dia",
#    "ZH": "Ni hao",
#}
#
#def dire_bonjour(name, lng="FR"):
#    print(f"{LNG_HELLO[lng]} {name}")

def dire_bonjour(name, lng="FR"):
    """
        Fonction qui dit bonjour à {name} 
        dans la langue lng
        :param name: Nom de la personne à saluer
        :param lng: Langue dans laquelle saluer
        :type name: type str
        :type lng: type str
    """
    if lng == "FR":
        print(f"Bonjour {name}")
    elif lng == "EN":
        print(f"Hello {name}")
    elif lng == "ES":
        print(f"Hola {name}")
    elif lng == "PT":
        print(f"Bom dia {name}")
    elif lng == "ZH":
        print(f"Ni hao {name}")


if __name__ == "__main__":
    dire_bonjour("Roger", "ZH")
    help(dire_bonjour)















