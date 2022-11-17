# Créer une méthode read_file_txt(path) qui renvoie 
# un string contenant le contenu d'un fichier au 
# chemin path (à partir du dossier de travail actuel)

import os

def read_file_txt(path):
  cwd = os.getcwd()
  file_path = cwd + path
  with open(file_path, 'r', encoding="utf-8") as fichier:
    contenu = fichier.read()
  return contenu

if __name__ == "__main__":
  print(read_file_txt("/23_files_txt/myfile.txt"))