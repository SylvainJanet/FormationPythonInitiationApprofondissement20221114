# Créer une méthode write_file_json(path, content) qui 
# écrit le contenu du dictionnaire content dans un 
# fichier au chemin path (le créant / l'écrasant 
# éventuellement)
# la mettre dans le module mytools, dans files.py

import os
import json

def write_file_json(path, content):
  cwd = os.getcwd()
  file_path = cwd + path
  with open(file_path, 'w', encoding="utf-8") as fichier:
    json.dump(content, fichier, indent=2, ensure_ascii=False)

if __name__ == "__main__":
  write_file_json("/24_files_json/sortie2.json",[ {'test' : "truc", "test2" : "truc2"}, {'test' : 'chose', 'test2' : 'chose2'}])