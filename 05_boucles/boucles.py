print("_____ Bloc itératif _____")

# un bloc d'instruction peut être répété un certain nombre de fois.
# Il y a deux types de bloc itératifs :
# - si le nombre de répétitions est connu à l'avance
# on utilise la boucle for, qui répète les instructions au fur et à mesure qu'on avance dans le parcours
# d'une collection d'éléments (une liste, un tuple, un dictionnaire, un set, un str, un range)
# - si le nombre de répétitions n'est pas connu à l'avance mais dépend d'une condition
# on utilise la boucle while, qui répète les instructions tant qu'une condition est évaluée à True

# Afficher les nombres de 0 à 9
nombres = range(10) # collection de nombres de 0 (inclus) à 10 (exclus)
# collection de 10 entiers, de 0 à 9

for nbr in nombres:
  print(nbr)


# Demander un nombre compris entre 1 et 10 à l'utilisateur, et lui redemander tant que le nombre n'est pas
# correct
nombre = 0
while not 1 <= nombre <= 10:
  # nombre = int(input("Saisir un nombre entre 1 et 10 : "))
  nombre = 9

print(f"Ok ! Voilà votre nombre : {nombre}")

print("_____")

# il faut être attentif à la condition de la boucle pour éviter de faire des boucles infinies
# while True:
#   print("Je ne m'arrête pas ! ") # ctrl + c pour forcer l'arrêt du programme

print("_____ Parcourir une chaîne _____")

prenom = "Guillaume"

print(f"{prenom = }")
print(f"Caractère en position 0 : {prenom[0]}") # En Python, les indices commencent à 0
print(f"Caractère en position 1 : {prenom[1]}") 

print("_____ Parcourir une chaîne avec un for _____")

# len() permet de récupérer la taille de la str
for index in range(len(prenom)):
  print(f"{prenom[index]}")

print("_____")

for lettre in prenom:
  print(lettre)

print("_____ Mots clés continue et break _____")

# le mot clé continue permet de forcer le passage à l'itération suivante
# le mot clé break permet de forcer l'arrêt de la boucle

prenom = "Sylvain"
for lettre in prenom:
  if lettre == "y":
    continue
  if lettre == "i":
    break
  print(lettre)
 
# Slva

