# Ecrire un programme qui choisit un nombre 
# aléatoirement entre 0 et 100 et qui demande à 
# l'utilisateur de deviner ce nombre. Après chaque 
# proposition, le programme indique si la valeur est 
# plus grande ou plus petite que la proposition. Le 
# programme gèrera le cas où l'utilisateur n'entre pas 
# un nombre. Lorsque l'utilisateur a trouvé, lui
# donner son nombre de tentatives. Si l'utilisateur
# dépasse un certain nombre de coups, il a perdu.
# Indication : pour choisir un nombre aléatoire, 
# utiliser :
import random # importe le module qui contient toutes 
              # les fonctions permettant de gérer 
              # l'aléatoire
nombre = random.randint(0,100)  # génère un nombre 
                                # aléatoire entre 0 et 
                                # 100
nbr_tentatives = 0
nbr_tentatives_max = 6
while True:
  user_input = input("Devine mon nombre entre 0 et 100 ")
  try:
    guess = int(user_input)
    nbr_tentatives+=1
    if guess == nombre:
      print(f"C'est bien ça, mon nombre était {nombre}")
      print(f"Tu as trouvé en {nbr_tentatives} tentatives !")
      break
    if nbr_tentatives == nbr_tentatives_max:
      print("Perdu !")
      break
    if guess <= nombre:
      print("Plus grand !")
    else:
      print("Plus petit !")
  except ValueError:
    print("Essaye de deviner un nombre !")

print("Fin du programme...")