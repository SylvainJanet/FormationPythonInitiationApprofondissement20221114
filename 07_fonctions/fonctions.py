# une fonction est une brique de code simple, facile à identifier

# on a déjà utilisé plusieurs fonctions :
# print, input sont des fonctions
# - elles portent un nom simple qui indique bien à quoi elles servent
# - elles prennent des paramètres qui permettent de varier la manière dont elles sont utilisées
# - on n'a pas besoin de savoir comment elles sont écrites, mais juste ce qu'elles vont faire

# sans fonction, le code devient vite long, et il est difficile de s'y repérer
# si un certaine fonctionnalité est utilisée plusieurs fois, on serait obligé de répéter du code plusieurs fois
# à la place, on peut factoriser le code et utiliser une fonction

# pour faciliter la lecture, une bonne pratique est de faire des fonctions relativement courtes
# ~ 20 lignes, pas beaucoup plus

def ma_fonction(): # signature de la fonction
  print("Je suis dans la fonction ma_fonction") # corps de la fonction

ma_fonction()

# tout est objet en Python
# ma_fonction est un objet qui est une fonction
ma_fonction
print(type(ma_fonction))

# pour utiliser la fonction, on utilise son nom suive entre parenthèses des différents paramètres qu'on
# souhaite utiliser (ici ma_fonction est sans paramètres)

# exemple de fonction avec paramètres
def punition(message, nbr_repetition):
  for _ in range(nbr_repetition): # On peut remplacer le nom de la variable dans la boucle for
    # par _ si elle n'est pas utilisée
    print(message)

punition("Je ne dois pas me répéter",3)

mess = "Je dois me répéter"
punition(mess, 1)

# une fonction peut renvoyer une valeur
# un peu comme input qui renvoie ce que l'utilisateur a écrit
# pour faire ça, on utilise le mot clé return
# return valeur

def carre(nombre):
  # ...
  return nombre ** 2

resultat = carre(6)
print(f"Le carré de 6 est {resultat}")

# une fonction qui ne renvoie rien (en apparence) renvoie en réalité None
print(ma_fonction())


# arguments optionnels
# on peut préciser des valeurs par défaut

# il y a un ordre imposé par l'interpréteur Python pour les arguments :
# les arguments obligatoires doivent être placés avant les arguments ayant une valeur par défaut
def f(x, alpha = 15, beta = 19):
  print(x, alpha, beta)

f(1,2,3) # 1 2 3
f(10) # 10 15 19
f(30,40) # 30 40 19

# on peut passer les arguments par leur nom
f(x = 87, beta = 129) # 87 15 129
f(87, beta = 129) # 87 15 129

# Une fonction qui permet de demander à l'utilisateur un nombre et qui renvoie à coup sur un nombre

def demander_saisie_nombre(invite = "Merci d'entrer un nombre"):
  while True:
    user_input = input(invite)
    try:
      result = int(user_input)
      return result
    except ValueError:
      print("Seuls les caractères [0-9] sont autorisés")


# nombre = demander_saisie_nombre()
nombre = 120
print(f"Nombre choisi : {nombre} de type {type(nombre)}") # int

print("_____")

# Une fonction peut retourner plusieurs valeurs
def demander_saisie_deux_nombres():
  nombre1 = demander_saisie_nombre()
  nombre2 = demander_saisie_nombre()
  return nombre1, nombre2 # on renvoie en réalité un tuple

# x = demander_saisie_deux_nombres()
# print(x)
# print(type(x))

# nbr1, nbr2 = demander_saisie_deux_nombres()
# print(f"{nbr1 = }")
# print(f"{nbr2 = }")

# punition("coucou","truc")
punition(True,3)
punition(1,2)
# duck typing : if it quacks like a duck, it's a duck
# ce qui est important ce n'est pas le type des objets, mais ce qu'on peut faire avec

print("_____")

# lower est une méthode sur les str qui renvoie la chaîne en minuscules
chaine = "TRUC"
print(chaine.lower())

# dans ce cas, il n'y a pas d'autocomplétion, ni de code couleur, et on a pas accès à la documentation
# de la méthode lower()
def exemple(chaine):
  print(chaine.lower())

exemple("COUCOU")

# Depuis Python 3.5, le langage propose un moyen d'indiquer aux développeurs et à l'IDE le type attendu des variables
# ou des arguments de fonctions
# Attention : ces indications n'ont aucune incidence sur le code, elles sont ignorées par l'interpréteur
# comme des commentaires

def exemple_with_type_hints(chaine: str) -> None:
  print(chaine.lower())

exemple_with_type_hints("MACHIN")

# http://mypy-lang.org/ # vérification statique des types