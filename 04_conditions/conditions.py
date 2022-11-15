print("_____ Bloc conditionnel _____")

# un bloc conditionnel est un bloc qui ne s'exécute que si une condition est évaluée à True

# un bloc est une section de code marqué par deux points ":" ainsi qu'une indentation sur la ligne suivante
# une indentation : des espaces en début de ligne
# Tant que le code est indenté au moins au même niveau, on est dans le bloc

# il est nécessaire en Python d'être attentif à l'indentation de son code, puisque elle a du sens 

age = 26
if age < 18:
  print("Mineur")
  print("Toujours mineur")
print("Tout âge")

print("_____")

age = 24

if age < 18:
  print("Mineur")
elif age <= 25: # elif : signifie else if
  print("Jeune adulte")
else:
  print("Adulte")

# on peut utiliser n'importe qu'elle expression qui renvoie un bool

if age >= 18 and age <= 25:
  print("Vous avez entre 18 et 25 ans")

# il est possible de réécrire cette condition de manière plus naturelle :
if 18 <= age <= 25:
  print("Vous avez entre 18 et 25 ans")


# un bloc vide n'est pas syntaxiquement valide en Python
# Néanmoins, il est possible de créer un bloc syntaxiquement valide sans rien y faire
# en utilisant le mot clé spécifique : pass
if True:
  # ne compte pas
  pass
print("Fin")

# cadre d'utilisation :

if age < 18:
  # en cours de développement...
  pass
else:
  print("Vous êtes majeur, ok...")
  # en cours de développement...

print("_____")

# opérateur ternaire
age = 20
if age < 18:
  print("mineur")
else:
  print("majeur")

# équivalent en utilisant l'opérateur ternaire :
print("mineur") if age < 18 else print("majeur") 
# on peut aussi affecter des variables
reponse = "mineur" if age < 18 else "majeur"
print(reponse)