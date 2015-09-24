# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:59:51 2015

@author: nico
"""
#  importer le module sys
import sys
# tester si la longueur de la liste est different de 3
if len(sys.argv) != 3:
    # si c est vrai afficher message erreur
    print("usage: python3 solution.py OP1 OP2")
#  sinon
else:
    #  affecter a avec la position 1 de la liste argv
    a = int(sys.argv[1])
    #  idem
    b = int(sys.argv[2])
    #  afficher le resultat de la somme
    print(a - b)
