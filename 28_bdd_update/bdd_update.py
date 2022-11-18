import sqlite3

cnx = sqlite3.connect("26_bdd_create/database.sqlite3")

curseur = cnx.cursor()

id = 2
new_nom = "Dupond"
new_prenom = "Chloé"
new_age = 37

# sql = "UPDATE personne SET nom = ?, prenom = ?, age = ? WHERE id = ?"
# data = (new_nom,new_prenom,new_age,id)

sql = "UPDATE personne SET nom = :last_name, prenom = :first_name, age = :age WHERE id = :id"
data = {
  "last_name":new_nom,
  "first_name":new_prenom,
  "age":new_age,
  "id":id
}

curseur.execute(sql, data)
cnx.commit()

cnx.close()