# un dictionnaire est une collection non ordonnée
# qui fonctionne par association clé / valeur

# - un dictionnaire (physique) : c'est un ensemble de paires clé / valeur
# mot / définition
# - un mot n'apparaît qu'une seule fois dans un dictionnaire, les définitions
# peuvent se répéter

# un dictionnaire (au sens de la collection Python) est un ensemble de paires 
# clé/valeur où les clés sont uniques, pas forcément les valeurs

dictionnaire = { 
  "Python":"langage de programmation", 
  "Dawan":"organisme de formation",
}

print(dictionnaire)

print(dictionnaire["Python"])

# regrouper un ensemble de caractéristiques

utilisateur = {
  "nom":"Doe",
  "prenom":"John",
  "age":15,
}

print(utilisateur['nom'])

# avec une liste, on aurait écrit :
# user = ["Doe","John",15]
# nom = user[0]
# c'est moins clair, les données de la liste ne sont pas homogènes
# pourquoi le nom serait en position 0 ?


# print(dictionnaire["PYTHON"]) # KeyError: 'PYTHON'
# la clé n'existe pas

definition = dictionnaire.get("Python")
print(f"{definition = }")
definition = dictionnaire.get("PYTHON")
print(f"{definition = }")

# if definition != None:
if definition:
  print("La définition existe")
else:
  print("La définition n'existe pas")

print("_____")

dictionnaire["Python"] = "Serpent des forêts tropicales d'Afrique et d'Asie"
print(dictionnaire)

dictionnaire["Java"] = "Langage de programmation"
print(dictionnaire)

# dans les dictionnaires, on peut mettre n'importe quel type d'objet en valeur
# mais on ne peut mettre des objets non mutables en clé (str, int, tuple, ...)

# essai = {
#   [1,2]:"coucou" # TypeError: unhashable type: 'list'
# }

# une valeur peut être elle-même un dictionnaire
utilisateur = {
  "nom":"Doe",
  "prenom":"John",
  "age":15,
  "telephones":["0612345678","0987654321"],
  "adresse": {
    "rue":"1 rue bidon",
    "code_postal":75015,
  },
}

print("_____ Parcourir un dictionnaire _____")

d = {
  "a":1,
  "b":2,
}

for item in d: # parcours uniquement les clés
  print(item)
  print(d[item])

print("_____")

for value in d.values():
  print(value)

print("_____")

for item in d.items():
  print(item)

# en utilisant le déballage de tuples :
for key, value in d.items():
  print(f"{key = } - {value = }")
