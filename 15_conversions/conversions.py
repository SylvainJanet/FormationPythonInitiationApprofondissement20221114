# pour convertir un objet dans un certain type, on utilise une fonction dont
# le nom est le nom du type cible 

str(5) # converti 5 en str
int("19") # converti "19" en int

# Conversions mathématiques
print(round(2.2))
print(round(2.7))
print(round(2.5)) # arrondi à l'inférieur
print(round(2.4567,1))
print(round(2.4567,2))

# conversion booléennes
# les valeurs fausses
print("Conversions booléennes qui renvoient faux")
print(bool(None))
print(bool(0))
print(bool("")) # chaine de caractères vides
print(bool([])) # collections vides

# les valeurs vraies
print("Conversions booléennes qui renvoient vrai")
print(bool(1))
print(bool(-278)) # tous les nombres non nuls
print(bool("Bonjour")) # les chaînes non vides
print(bool([1,2,3])) # les collections non vides

# on peut faire des tests du type
chaine = input("Ecrire quelque chose")
if chaine: # si l'expression ne renvoie pas un booléen, Python fait une conversion
  print("Ok, chaine non vide")
else:
  print("Chaine vide")

# conversion de type
# on a des fonctions 
# bool()
# int()
# float()
# complex()
# str()
# list()
# tuple()
# set()
# dict()
# Si on donne un argument, ces fonctions nous renvoie l'argument converti vers
# le type la fonction si c'est possible
# Si on donne aucun argument, ces fonctions nous renvoient False, 0, chaine
# ou une collection vide