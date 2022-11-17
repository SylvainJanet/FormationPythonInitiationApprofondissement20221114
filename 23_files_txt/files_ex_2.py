# Créer une méthode write_file_txt(path, content) qui 
# écrit le contenu du string content dans un fichier au 
# chemin path (le créant / l'écrasant éventuellement)

import os

def write_file_txt(path, content):
  cwd = os.getcwd()
  file_path = cwd + path
  with open(file_path, 'w', encoding="utf-8") as fichier:
    fichier.write(content)

if __name__ == "__main__":
  write_file_txt("/23_files_txt/myfile2.txt","Ceci est un test de la méthode write_file_txt")