import sqlite3

with sqlite3.connect("26_bdd_create/database.sqlite3") as cnx:

  curseur = cnx.cursor()

  sql = "DELETE FROM personne WHERE id = ?"
  data = (1,)

  curseur.execute(sql,data)
  
  cnx.commit()
