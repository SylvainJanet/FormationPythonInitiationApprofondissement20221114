import json
import os

chemin_fichier = os.path.join(
  os.getcwd(),
  "24_files_json",
  "users.json"
)

with open(chemin_fichier,'r',encoding = "utf-8") as fichier:
  content = json.load(fichier)

print(f"{content = }")
print(type(content))
print(type(content[0]))

for utilisateur in content:
  print(f"Nom : {utilisateur.get('name')}")
  print(f"Rue : {utilisateur.get('address').get('street')}")

chemin_fichier = os.path.join(
  os.getcwd(),
  "24_files_json",
  "sortie.json"
)

data = [
  {
    "Nom":"Doe",
    "Prénom":"John",
  },
  {
    "Nom":"Curie",
    "Prénom":"Marie",
  },
]

with open(chemin_fichier,'w', encoding="utf-8") as fichier:
  json.dump(data, fichier, indent = 2, ensure_ascii=False)