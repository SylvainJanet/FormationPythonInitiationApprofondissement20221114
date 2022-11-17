"""Module de présentation de la documentation

Ce module a été présenté durant la formation Python Initiation
et Approfondissement en novembre 2022 à Dawan"""

import math

# __doc__ : permet d'accéder à la documentation
print(math.__doc__)
print(math.cos.__doc__)

print("_____")

# on peut documenter : modules, fonctions, classes...

print(__doc__)

def ma_fonction():
  """Une fonction à titre d'exemple
  
Une fonction qui sert à illustrer la documentation d'éléments dans un module.
Elle ne fait qu'afficher un message dans la console"""
  print("Coucou")

print(ma_fonction.__doc__)

# générer la documentation à l'aide de pydoc
# py -m pydoc nomdufichier : affichage dans la console
# py -m pydoc -w nomdufichier : dans un fichier html