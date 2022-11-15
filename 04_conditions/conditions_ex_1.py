# Demander à l'utilisateur un nombre. Afficher ensuite 
# si ce nombre est pair ou impair

nombre = int(input("Entrer un nombre "))
if (nombre % 2 == 0):
  print(f"{nombre} est pair")
else:
  print(f"{nombre} est impair")
