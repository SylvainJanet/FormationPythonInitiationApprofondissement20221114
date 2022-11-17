# Créer une méthode read_file_json(path) qui renvoie 
# un string contenant le contenu d'un fichier au 
# chemin path (à partir du dossier de travail actuel)
# la mettre dans le module mytools, dans files.py

import os
import json

def read_file_json(path):
  cwd = os.getcwd()
  file_path = cwd + path
  with open(file_path, 'r', encoding="utf-8") as fichier:
    contenu = json.load(fichier)
  return contenu

if __name__ == "__main__":
  print(read_file_json("/24_files_json/sortie.json"))