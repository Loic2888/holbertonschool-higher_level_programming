#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    resultat = {}
    for cle, valeur in a_dictionary.items():
        if isinstance(valeur, (int)):
            resultat[cle] = valeur * 2
        else:
            resultat[cle] = valeur
    return resultat
