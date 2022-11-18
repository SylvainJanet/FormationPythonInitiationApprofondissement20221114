import os
import json
import csv

def read_file_txt(path):
  cwd = os.getcwd()
  file_path = cwd + path
  with open(file_path, 'r', encoding="utf-8") as fichier:
    contenu = fichier.read()
  return contenu

def write_file_txt(path, content):
  cwd = os.getcwd()
  file_path = cwd + path
  with open(file_path, 'w', encoding="utf-8") as fichier:
    fichier.write(content)

def read_file_json(path):
  cwd = os.getcwd()
  file_path = cwd + path
  with open(file_path, 'r', encoding="utf-8") as fichier:
    contenu = json.load(fichier)
  return contenu

def write_file_json(path, content):
  cwd = os.getcwd()
  file_path = cwd + path
  if not os.path.exists(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))
  with open(file_path, 'w', encoding="utf-8") as fichier:
    json.dump(content, fichier, indent=2, ensure_ascii=False)

def read_file_csv(path):
  cwd = os.getcwd()
  file_path = cwd + path
  content = []
  with open(file_path, 'r', encoding="utf-8") as fichier:
    reader = csv.reader(fichier)
    for row in reader:
      if row:
        content.append(row)
  return content

def write_file_csv(path, content):
  cwd = os.getcwd()
  file_path = cwd + path
  if not os.path.exists(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))
  with open(file_path, 'w', encoding="utf-8", newline="") as fichier:
    writer = csv.writer(fichier)
    writer.writerows(content)

if __name__ == "__main__":
  # print(read_file_txt("/26_files_txt/myfile.txt"))
  # write_file_txt("/26_files_txt/myfile2.txt","Ceci est un test de la méthode write_file_txt")
  # print(read_file_json("/27_files_json/sortie.json"))
  # write_file_json("/27_files_json/sortie2.json",[ {'test' : "truc", "test2" : "truc2"}, {'test' : 'chose', 'test2' : 'chose2'}])
  # print(read_file_csv("/29_files_csv/mon_fichier.csv"))
  # write_file_csv("/28_files_csv/mon_fichier.csv",[ ['test', "truc", "test2" , "truc2"], ['test' , 'chose', 'test2' , 'chose2' ]])

  write_file_csv("/log_mars.csv",[['20220225','1','Défaut com'], ['20220305','2','Choc robot'], ['20220325','6','Défaut variateur']])