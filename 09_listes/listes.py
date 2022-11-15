# les listes sont des collections : elles permettent de regrouper un ensemble de données cohérentes
# liste de prénoms, liste de notes, liste de courses, ...

# liste vide
notes = []
print(notes)

notes = [1,4,9,17]
print(notes)

# il n'y aucune restriction sur le type des éléments d'une liste
liste = [2, 5, 4, "coucou", True, [1,2,3]] # possible
print(liste)

# la cohérence fait plutôt référence à une question d'organisation
# si vous pensez utiliser une lise pour stocker des éléments de nature différente, ce n'est surement pas la manière
# la plus adaptée (dictionnaires, classes seront surement plus adaptés)

print("_____ Atteindre un élément d'une liste _____")

notes = [38, 32, 7, 19, 18]

print(f"Element en position 0 : {notes[0]}")
print(f"Element en position 1 : {notes[1]}")

# notes[100] # IndexError: list index out of range

taille_notes = len(notes)
print(f"Il y a {taille_notes} éléments dans la liste")

print(f"Dernier élément : {notes[taille_notes - 1]}")
print(f"Dernier élément : {notes[-1]}")
# Python autorise les indices négatifs, on part de la fin
print(f"Avant-dernier élément : {notes[-2]}")

# notes[-100] # IndexError: list index out of range

# on peut aussi modifier les éléments d'une liste
print(notes)
notes[1] = 123
print(notes)

print("_____ Parcourir une liste _____")
print("\tAvec un for")

for indice in range(len(notes)):
  print(f"note d'indice {indice} : {notes[indice]}")

print("_____")

for nbr in notes:
  print(nbr)

print("\tAvec un for et l'indice")

for index, nbr in enumerate(notes):
  # enumerate renvoie une liste de tuples
  # (0, notes[0]), (1, notes[1]), ...
  # et donc en déballant les tuples,
  # index va valloir : 0, 1, 2, ...
  # nbr va valloir : notes[0], notes[1], notes[2], ...
  print(f"note d'indice {index} : {nbr}")

print(f"_____ Manipuler une liste _____")

prenoms = ["Anlya","Guillaume", "François", "Laura", "Yassine"]
print(prenoms)

prenoms.append("Sylvain")
print(prenoms)

# une liste est un objet mutable, c'est à dire que son espace mémoire peut être modifié
# ses méthodes renvoient None et modifient la liste

# c'est un comportement à opposer au comportement des str qui sont non mutables
texte = "truc"
print(texte)
texte.upper() # texte n'est pas modifiée
print(texte)
texte = texte.upper()
print(texte)

ma_liste = [4,2,9]
print(ma_liste)
ma_liste.append(16) # ma_liste est modifiée
print(ma_liste)
ma_liste = ma_liste.append(9)
print(ma_liste)

# pop : supprimer des éléments (en utilisant l'indice)
# remove : supprimer des éléments (en utilisant sa valeur)
prenoms.remove("Sylvain")
print(prenoms)
# reverse : inverser l'ordre des éléments de la liste

print("_____ Listes en compréhension _____")

# listes en compréhension, listes en intension, "comprehension lists"

# En Python, on itère beaucoup sur des listes, et souvent on applique un même
# traitement à tous les éléments d'une liste, un par un, et on conserve
# le résultat dans une nouvelle liste

# on peut utiliser une boucle for

sequence = ["a","b","c"]
new_sequence = []
for el in sequence:
  new_sequence.append(el.upper())

print(new_sequence)

# cette opération - prendre une liste, modifier les éléments un par un, conserver
# les résultats - est très commune
# Python possède une manière élégante de faire ça plus vite
sequence = ["a","b","c"]
new_sequence = [el.upper() for el in sequence]
print(new_sequence)

# on peut très réaffecter l'ancienne liste
# même principe que a = a + 2
sequence = [el.upper() for el in sequence]

# une autre opération est également faite très fréquemment : c'est le filtrage
nombres = range(10)
nombres_pairs = []
for nbr in nombres:
  if nbr % 2 == 0:
    nombres_pairs.append(nbr)
print(nombres_pairs)

# on peut aussi faire du filtrage en compréhension
nombres = range(10)
nombres_pairs = [nbr for nbr in nombres if nbr % 2 == 0]
print(nombres_pairs)
# il est tout à fait possible de faire les deux en même temps
nombres = range(10)
double_nombres_pairs = [2*nbr for nbr in nombres if nbr % 2 == 0]
print(double_nombres_pairs)