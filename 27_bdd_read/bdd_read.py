# CREATE READ UPDATE DELETE : CRUD

import sqlite3

cnx = sqlite3.connect("26_bdd_create/database.sqlite3")

curseur = cnx.cursor()

sql = "SELECT * FROM personne"
curseur.execute(sql)

# le curseur est placé en tête des resultats, et on peut l'utiliser pour parcourir
# les resultats

personnes = curseur.fetchall()
print(personnes) # c'est toujours une liste de tuples

for _,nom,prenom,age in personnes:
  print(f"{nom} {prenom} a {age} ans")

print("_____")

personnes = curseur.fetchall() # le curseur étant en fin de liste,
# si on essaye de récupérer les résultats à nouveau, il ne reste plus rien
print(personnes)

print("_____")

sql = "SELECT nom, prenom FROM personne WHERE id = ?"
data = (2,)

curseur.execute(sql, data)
user = curseur.fetchone()
print(user)

# commit() non nécessaire, puisqu'on a pas modifié les tables

cnx.close()