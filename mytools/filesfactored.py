import os
import json
import csv

def get_path_from_string(path_string:str):
  cwd = os.getcwd()
  locations = [s for s in path_string.split("/") if s]
  return os.path.join(cwd, *locations)

def __read_file(path_string,read):
  path = get_path_from_string(path_string)
  with open(path, 'r', encoding="utf-8") as fichier:
    contenu = read(fichier)
  return contenu

def __write_file(path_string, content, write):
  path = get_path_from_string(path_string)
  if not os.path.exists(os.path.dirname(path)):
    os.makedirs(os.path.dirname(path))
  with open(path, 'w', encoding="utf-8", newline="") as fichier:
    write(fichier,content)

def read_file_txt(path_string):
  def read(fichier):
    return fichier.read()
  return __read_file(path_string,read)

def write_file_txt(path_string,content):
  def write(fichier,content):
    fichier.write(content)
  __write_file(path_string,content,write)

def read_file_json(path_string):
  def read(fichier):
    return json.load(fichier)
  return __read_file(path_string,read) 

def write_file_json(path_string, content):
  def write(fichier,content):
    json.dump(content,fichier,indent=2,ensure_ascii=False)
  __write_file(path_string,content,write)

def read_file_csv(path_string, delimiter = ","):
  def read(fichier):
    contenu = []
    reader = csv.reader(fichier, delimiter=delimiter)
    for row in reader:
      if row:
        contenu.append(row)
    return contenu
  return __read_file(path_string,read)

def write_file_csv(path_string, content, delimiter = ","):
  def write(fichier,content):
    writer = csv.writer(fichier,delimiter=delimiter)
    writer.writerows(content)
  __write_file(path_string,content,write)

if __name__ == "__main__":
  print(read_file_txt("/04_files_txt/myfile.txt/"))
  write_file_txt("04_files_txt/myfile2factored.txt","Ceci est un test de la méthode write_file_txt")
  write_file_txt("04_files_txt/newfolder/otherfolder/myfile3factored.txt","Ceci est un test de la méthode write_file_txt")
  print(read_file_json("/05_files_json/sortie.json"))
  donnees = [ 
    {
      'nom' : "Doe", 
      "prenom" : "John"
    }, 
    {
      'nom' : 'Clapton', 
      'prenom' : 'Eric'
    }
  ]
  write_file_json("05_files_json/myfilefactored.json",donnees)
  write_file_json("05_files_json/newfolder/otherfolder/myfile2factored.json",donnees)
  print(read_file_csv("/06_files_csv/myfile.csv"))
  donnees = [ 
    [ "nom","prenom" ],
    [ "Doe", "John" ], 
    [ 'Clapton', 'Eric' ]
  ]
  write_file_csv("06_files_csv/myfile3factored.csv",donnees)
  write_file_csv("06_files_csv/newfolder/otherfolder/myfile4factored.csv",donnees)