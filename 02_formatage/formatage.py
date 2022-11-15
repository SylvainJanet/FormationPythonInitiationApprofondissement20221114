age = 64
prenom = "Chloé"

print("Age :", age, "- Prénom :", prenom)

# on peut utiliser la concaténation des strings
# string1 + string2 retourne une chaîne de caractères composée du contenu de string1 suivi du contenu de string2
# (aucun espace n'est ajouté)

# attention au type : on ne peut concaténer que des str
# -> TypeError: can only concatenate str (not "int") to str
# str(...) permet de convertir un élément en string
message = "Age : " + str(age) + " - Prénom : " + prenom
print(message)

print("Age : " + str(age) + " - Prénom : " + prenom)

# A partir de Python 3 :
print("Age : {} - Prénom : {}".format(age, prenom)) 
# cf https://docs.python.org/fr/3.5/library/string.html#format-specification-mini-language

# Avant python 3
# https://docs.python.org/2/library/stdtypes.html#string-formatting-operations

# A partir de Python 3.6 : fString (format string)
print(f"Age : {age} - Prénom : {prenom}")
# les fstrings permettent aussi ce genre d'écriture :
print(f"{prenom = }") # affiche le nom de la variable et sa valeur
print(f"{5 * 6 = }") # possible avec du code qui renvoie une valeur
