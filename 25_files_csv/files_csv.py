import csv
import os

chemin_fichier = os.path.join(
  os.getcwd(),
  "25_files_csv",
  "demo.csv"
)

data = []

with open(chemin_fichier, "r", encoding="utf-8") as fichier:
  reader = csv.reader(fichier,delimiter=",")
  for row in reader: # reader se comporte comme une liste qui contient les lignes
    print(row) # liste de str
    # le contenu de tout le fichier sera une liste de lignes
    # et donc une liste de liste de str
    data.append(row)

print("_____")

print(data)

data = [
  ["nom","prenom"],
  ["Doe","John"],
  ["Curie","Marie"],
]

chemin_fichier = os.path.join(
  os.getcwd(),
  "25_files_csv",
  "myfile.csv"
)

with open(chemin_fichier, "w", encoding= "utf-8") as fichier:
  writer = csv.writer(fichier, delimiter=";")
  writer.writerows(data)

  # on a des lignes supplémentaires présentes dans le fichier final

print("_____")

# première solution : ne lire que les lignes non vides
# pas satisfaisant si on souhaite communiquer le fichier csv
# (l'autre méthode est tellement peu couteuse qu'elle est préférable dans tous les cas)

data = []
with open(chemin_fichier,"r",encoding="utf-8") as fichier:
  reader = csv.reader(fichier, delimiter=";")
  for row in reader :
    if row: # if row != []
      data.append(row)

print(data)

# deuxième solution
# on a deux manières d'écrire les sauts de lignes :
# \n ou \r\n
# on peut préciser lors de l'ouverture du fichier newline = ""

chemin_fichier = os.path.join(
  os.getcwd(),
  "25_files_csv",
  "myfile2.csv"
)

with open(chemin_fichier, "w", encoding="utf-8", newline="") as fichier:
  writer = csv.writer(fichier, delimiter=";")
  writer.writerows(data)
