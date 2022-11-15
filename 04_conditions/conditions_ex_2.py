# Demander à l'utilisateur un mot. Afficher si ce mot 
# contient la lettre "e" ou non (utiliser l'opérateur 
# in)

mot = input("Entrer un mot ")
if "e" in mot:
  print(f"{mot} contient la lettre e")
else:
  print(f"{mot} ne contient pas la lettre e")