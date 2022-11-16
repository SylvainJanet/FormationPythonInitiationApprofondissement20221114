# utilisation des méthodes proposées par les chaînes de caractères

texte = "     Ceci   est UN    ExEMPle    "

print(texte.upper())
print(texte.lower())
print("est" in texte)
print(texte.endswith("MPle"))
print(texte.strip())
print("\"" + texte.strip() + "\"") # enlève les espaces au début et en fin de chaîne

# les str sont des objets non mutables : les méthodes ne transforment pas la chaîne, elles renvoient une copie
# modifiée

texte = "mon.fichier.txt"

split_string = texte.split(".")
print(split_string)

# on peut faire l'opération inverse en utilisant join
print("////".join(split_string))
print("".join(split_string))

print("_____")

# En Python, les chaînes sont encodées en utilisant l'unicode
# Chaque caractère est positionné dans une table et dispose d'une position dans la table, nommé ordinal
# Par exemple, 'A' a pour ordinal 65, et l'ordinal 97 a pour ordinal 'a' 

print(ord('A'))
print(chr(97))

liste = ["banane","Abricot","elephant","Python"]
print(liste)
liste.sort()
print(liste)

# tri par ordre alphabétique : utilise l'ordre lexicographique (compare les premières lettres, et si c'est la 
# deuxième, sinon on a la réponse, ...) et utilise l'ordinal pour comparer les caractères.

resultat = liste.sort()
print(resultat)
print(liste.sort()) # les listes sont mutables, sort() modifie la liste et ne renvoie rien (None)

import string # ne pas appeler ce fichier string.py pour éviter les imports circulaires

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

saisie = input("Entrez un caractère : ")
if saisie in string.punctuation:
  print("c'est de la ponctuation")
else:
  print("ce n'est pas de la ponctuation")