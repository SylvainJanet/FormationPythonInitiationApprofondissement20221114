# Dans les exercices, on a réutilisé des fonctions de fichiers différents, et 
# on les a copier/coller
# on peut éviter ça en utilisant des modules
# on peut importer le module random qui gère l'aléatoire :

# import random
# on peut lui donner un autre nom dans notre fichier
# import random as r

# nombre = r.randint(1,10)
# print(nombre)

# on peut aussi importer des éléments spécifiques d'un module
# from random import randrange
# on peut leur donner un autre nom dans notre fichier
# from random import randrange as r_range
# nombre = r_range(0,11,2)
# print(nombre)

# on peut importer tous les éléments d'un module
# from random import * # on s'expose au risque de conflit de nommage

# un module est une collection de fonctions, de classes, de constantes, ou d'autres variables
# un package est un repertoire qui contient des modules

# pour transformer un repertoire en un package Python, il suffit qu'il
# contienne un fichier __init__.py ( _ _ init _ _ . py sans espace)
# on peut le laisser vide, il est censé contenir la configuration du 
# package

# |_ app.py
# |_ mypackage
#     |_ mymodule.py
#     |_ __init__.py (vide)

# Lorsqu'un module est importé, il est aussi exécuté
import mypackage.mymodule as mymod

print("Module importé")

mymod.ma_fonction()

# on peut vouloir différencier le compotement selon si un module est exécuté
# comme point d'entrée de l'application ou si il est exécuté lors de son
# import

# on peut s'en sortir grâce à la variable __name__ qu'ont tous les modules
# ( _ _ name _ _ sans espace)
# cette variable vaut le nom du module lorsqu'il est importé,
# mais dans le cas où c'est le point d'entrée, elle vaut __main__
# (_ _ main _ _)


# on peut aussi utiliser des packages externes
# un exemple requests : utile pour gérer les requêtes HTTP, par exemple pour récupérer le contenu d'une page web

# On utilise un environnement virtuel pour installer des dépendances.
# Son rôle est d'isoler le projet et d'installer des dépendances uniquement pour le projet en question
# - éviter les conflits de version entre projets
# - éviter de polluer les projets avec des dépendances inutiles

# pour créer un environnement virtuel (une seule fois au début d'un projet)
# dans une console, au niveau du dossier projet
# py -m venv nom-env
# py : executer py.exe
# -m : execute un script
# venv : le nom du script
# nom-env : nom de l'environnement virtuel à créer, peut être ce qu'on veut,
# mais souvent venv

# py -m venv venv

# en cas d'erreur : activer les scripts.
# dans un powershell en mode administrateur : 
# Set-ExecutionPolicy RemoteSigned
# O

# pour activer l'environnement virtuel, il faut exécuter Activate.ps1
#./venv/Script/Activate.ps1

# On voit qu'un environnement virtuel est activé au (venv) en vert au début du 
# prompt de la console

# pour le désactiver : deactivate

# on peut installer des packages externes en utilisant pip
# https://pypi.org/ pour trouver les packages

import requests

# pip install requests

# Lorsqu'on souhaite partager un projet, on ne partage pas le dossier venv
# -> grande quantité de fichiers
# -> ce n'est pas la source de notre travail

# pip list : permet de voir la liste des dépendances avec leur version

# on partage le projet sans le dossier venv, donc sans les dépendances
# mais avec une liste des dépendances
# on récupère un projet avec une liste de dépendances qu'on télécharge

# on ne fait pas ces opérations manuellement
# on peut utiliser des commandes pour le faire

# générer un fichier requirements.txt avec toutes les dépendances
# pip freeze --local > requirements.txt

# pour installer toutes les dépendances listées dans un fichier requirements.txt
# pip install -r requirements.txt