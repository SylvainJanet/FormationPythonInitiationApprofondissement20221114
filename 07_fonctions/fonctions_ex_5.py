# Recoder le jeu où l'on devine un nombre choisi 
# aléatoirement par le programme. Cette fois ci, le 
# programme va demander à l'utilisateur quelles bornes 
# utiliser et lorsqu'il aura deviné un nombre incorrect,
# il lui proposera les choix cohérents 
# Exemple : je choisi 1 et 100 comme bornes. Le 
# programme me demande de saisir un nombre entre 1 et 
# 100. Je choisi 50. Le programme me répond : le nombre
# est plus grand, choisi un nombre entre 51 et 100. 
# Lorsque j'ai trouvé, le programme s'arrête.
# On va cette fois ci utiliser des fonctions.
# - reprendre les fonctions demander_saisie_nombre et 
# demander_saisie_nombre_borne
# - coder decider_bornes() qui renvoie les bornes 
# utilisées pour le jeu
# - coder jouer_un_coup(nombre,minimum,maximum) qui 
# demande à l'utilisateur un entier entre minimum et 
# maximum, et qui renvoie :
# 	* un boolean à vrai uniquement si l'utilisateur a 
#     gagné (il a choisi le paramètre nombre)
# 	* le minimum pour le coup suivant
# 	* le maximum pour le coup suivant
# - coder jouer_une_partie(nombre,minimum,maximum) qui 
# fait une partie du jeu où l'entier à deviner est le 
# paramètre nombre, et où les bornes sont minimum et 
# maximum et qui renvoie le nombre de tentatives du 
# joueur
# - coder une fonction jouer() qui fait tout le jeu : 
# demander à l'utilisateur les bornes du jeu, puis 
# choisi un nombre aléatoirement, puis demande à 
# l'utilisateur de deviner un nombre, en lui disant si 
# le nombre est plus grand ou plus petit, et en lui 
# proposant au fur et à mesure des choix cohérents avec
# ces indications. Lorsque le joueur trouve le nombre, 
# la fonction le félicite, lui donne son nombre de 
# tentatives et s'arrête.

import random

def demander_saisie_nombre(invite):
  while True:
    user_input = input(invite)
    try:
      result = int(user_input)
      return result
    except ValueError:
      print("Seul les caractères [0-9] sont autorisés")

def demander_saisie_nombre_borne(invite,minimum = 1, maximum = 10):
  invite += f" entre {minimum} et {maximum} "
  while True:
    nombre_input = demander_saisie_nombre(invite)
    if minimum <= nombre_input <= maximum:
      return nombre_input

def decider_bornes():
  while True:
    minimum = demander_saisie_nombre("Quelle est la borne minimale ? ")
    maximum = demander_saisie_nombre("Quelle est la borne maximale ? ")
    if minimum < maximum:
      return minimum, maximum
    print("Le minimum doit être plus petit que le maximum !")

def jouer_un_coup(nombre, minimum, maximum):
  essai = demander_saisie_nombre_borne("Devinez le nombre", minimum, maximum)
  if essai < nombre:
    print("Trop petit !")
    return False, essai + 1, maximum
  if essai > nombre:
    print("Trop grand !")
    return False, minimum, essai - 1
  print("Bravo !")
  return True, nombre, nombre

def jouer_une_partie(nombre, minimum, maximum):
  nombre_coup = 0
  while True:
    victoire, minimum, maximum = jouer_un_coup(nombre, minimum, maximum)
    nombre_coup += 1
    if victoire:
      return nombre_coup

def jouer():
  minimum, maximum = decider_bornes()
  nombre = random.randint(minimum,maximum)
  nombre_coup = jouer_une_partie(nombre,minimum,maximum)
  print(f"Vous avez deviné le nombre en {nombre_coup} coups !")

jouer()