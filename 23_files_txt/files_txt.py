import os

# C:/.../23_files_txt/files_txt.py
print(__file__)

# C:/.../23_files_txt
chemin_dossier = os.path.dirname(os.path.abspath(__file__))

# C:/.../23_files_txt/myfile.txt
chemin_fichier = os.path.join(chemin_dossier,"myfile.txt")

# pour ouvrir un fichier on utilise la fonction open()
# cette fonction prend plusieurs paramètres :
# - le chemin vers le fichier
# - le mode d'ouverture : 
#   'w' pour write
#   'a' pour append
#   'r' pour read

fichier = open(chemin_fichier, 'r', encoding = "utf-8")

contenu = fichier.read()
print(contenu)

# l'ouverture d'un fichier ouvre un flux, une ressource mémoire qui permet d'accéder
# au fichier, qu'il va falloir fermer lorsque le traitement est terminé
# -> sans fermer les flux, on s'expose à des risques de fuite mémoire
fichier.close()

# Context Manager : à la fin du bloc d'instructions, le context manager
# s'occupe de libérer les ressources allouées à l'ouverture du fichier.
with open(chemin_fichier, 'r', encoding="utf-8") as fichier:
  contenu = fichier.read()
  print(contenu)
  # lors de l'ouverture d'un fichier, un curseur est positionné au début
  # du fichier. Lors de la lecture, le curseur avance jusqu'à la fin du fichier
  # une fois terminé, il n'y a plus rien à lire
  fichier.seek(0) # repositionne le curseur en positon 0
  print(f"Contenu de mon fichier : {fichier.read()}")

  # fichier.readline # permet de lire une ligne
  # fichier.readlines # permet de lire tout le fichier mais renvoie une liste de str
  # contenant les lignes

chemin_dossier = os.path.dirname(os.path.abspath(__file__))
chemin_fichier = os.path.join(chemin_dossier,"message.txt")

with open(chemin_fichier, "w", encoding="utf-8") as fichier:
  fichier.write("Salut depuis le code Python !")


# GET Current Work Directory
print("GET Current Work Directory : " + os.getcwd())
chemin_fichier = os.path.join(
  os.getcwd(),
  "23_files_txt",
  "message.txt"
)

with open(chemin_fichier, "a", encoding="utf-8") as fichier:
  fichier.write("\nHello à nouveau !")

chemin_dossier = os.path.join(
  os.getcwd(),
  "23_files_txt",
  "mesfichiers"
)

if not os.path.exists(chemin_dossier):
  os.mkdir(chemin_dossier) # création du dossier, erreur si il existe déjà
else:
  print("Le dossier existe déjà")

chemin_dossier = os.path.join(
  os.getcwd(),
  "23_files_txt",
  "mesautresfichiers",
  "unautredossier",
  "encoreunautredossier"
)

# mkdir ne créé que le dernier repertoire dans le chemin. 
# Ici : FileNotFoundError: [WinError 3] Le chemin d’accès spécifié est introuvable
# os.mkdir(chemin_dossier)

if not os.path.exists(chemin_dossier):
  os.makedirs(chemin_dossier)
else:
  print("Le chemin existe déjà")