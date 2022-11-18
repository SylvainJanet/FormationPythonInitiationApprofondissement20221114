# lorsqu'on fait un import Python va chercher le package en interne,
# parmis les packages installés, et aussi dans dans le PATH python.
# Par défaut, ce PATH contient le repertoire contenant le point d'entrée de
# l'application

# ici le path contient le chemin vers 30_retour_imports

# il faut rajouter le chemin vers le dossier global au PATH
if __name__ == "__main__": # si ce fichier est le point d'entrée de l'application
  import os
  import sys

  MAIN_DIR = os.getcwd()
  sys.path.append(MAIN_DIR)

from myclasses.product import Product

p = Product(1,"truc",5)
print(p)
