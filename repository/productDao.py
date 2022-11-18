# Créer un module repository, avec un fichier 
# productDao.py
# Coder une classe ProductDao qui contiendra des 
# méthodes
# addProduct(self, p)
# getProductById(self, id)
# getAllProducts(self)
# updateProduct(self, p)
# deleteProductById(self, id)
# qui implémentent les fonctionnalités associées pour 
# une table produit et qui a comme propriétés le nom de
# la base, le nom de la table.
# Enfin, elle aura une méthode close() pour fermer la 
# connexion et une méthode init_table() pour créer la 
# table et y mettre des données initiales.
# Les opérations / erreurs seront loggées dans un 
# fichier app.log

import sqlite3
import logging

if __name__ == "__main__":
  import sys
  import os
  SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(os.path.dirname(SCRIPT_DIR))

from myclasses.product import Product


logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    filemode='a',
    format="%(asctime)s - [%(levelname)s]: %(filename)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"
)

class ProductDao:
  DB_NAME = "repository/db.sqlite3"
  TABLE_NAME = "product"
  def __init__(self):
    self.__cnx = None
    try:
      self.__cnx = sqlite3.connect(ProductDao.DB_NAME)
    except sqlite3.DatabaseError as e:
      logging.error(e)
  
  def init_table(self):
    cursor = self.__cnx.cursor()
    logging.info(f"Création de la table {ProductDao.TABLE_NAME} (si elle n'existe pas)")
    try:
      sql = "CREATE TABLE IF NOT EXISTS " + ProductDao.TABLE_NAME
      sql += """ ( 
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      description varchar(50) NOT NULL,
      prix real NOT NULL
      )"""
      cursor.execute(sql)
      # equivalent de truncate (remet le compteur d'id à 0)
      # https://sqlite.org/autoinc.html
      sql = "DELETE FROM " + ProductDao.TABLE_NAME
      cursor.execute(sql)
      sql = "delete from sqlite_sequence where name='" + ProductDao.TABLE_NAME + "'"
      cursor.execute(sql)
      sql = "INSERT INTO " + ProductDao.TABLE_NAME + " (id, description, prix) VALUES (NULL, :description, :prix)"
      p1 = Product(1,"Table",50)
      p2 = Product(2, "Crayon",1.5)
      p3 = Product(3,"PC",2500)
      # p.__dict__ : dictionnaire avec tous les 
      # attributs de l'objet p
      # ne fonctionne pas pour les propriétés
      # cursor.execute(sql, p1.__dict__)
      cursor.execute(sql, {"id" : p1.id, "description" : p1.description, "prix": p1.prix})
      cursor.execute(sql, {"id" : p2.id, "description" : p2.description, "prix": p2.prix})
      cursor.execute(sql, {"id" : p3.id, "description" : p3.description, "prix": p3.prix})
      self.__cnx.commit()
    except sqlite3.Error as e:
      logging.error(e)
    else:
      logging.info(f"Succès de la création de la table {ProductDao.TABLE_NAME} (si elle n'existe pas)")
    finally:
      cursor.close()

  def close(self):
    self.__cnx.close()
  
  # méthode utilisée lorsque la variable est
  # supprimée par le ramasse miettes
  def __del__(self):
    self.close()

  def addProduct(self, p: Product):
    logging.info(f"Ajout du produit {p}")
    cursor = self.__cnx.cursor()
    sql = "INSERT INTO " + ProductDao.TABLE_NAME + " (id, description, prix) VALUES (null, :description, :prix)"
    try:
      cursor.execute(sql, {"id" : p.id, "description" : p.description, "prix": p.prix})
      self.__cnx.commit()
    except sqlite3.Error as e:
      logging.error(e)
    else:
      logging.info(f"Succès de l'ajout du produit {p}")
    finally:
      cursor.close()

  def getProductById(self, id: int) -> Product:
    logging.info(f"Récupération du produit avec l'id {id}")
    sql = f"SELECT * FROM {ProductDao.TABLE_NAME} WHERE id = ?"
    product = None
    try:
      product = self.__cnx.execute(sql,(id,)).fetchall()
    except sqlite3.Error as e:
      logging.error(e)
    else:
      if product:
        # https://sametmarx.com/operateur-splat-ou-etoile-en-python/
        # https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
        product = Product(*product[0])
      logging.info(f"Le produit trouvé : {product}")
    return product

  def getAllProducts(self):
    logging.info(f"Récupération de tous les produits")
    sql = f"SELECT * FROM {ProductDao.TABLE_NAME}"
    try:
      result = self.__cnx.execute(sql).fetchall()
    except sqlite3.Error as e:
      logging.error(e)
    else:
      logging.info(f"Succès de récupération de tous les produits")
      return result
      

  def updateProduct(self, p: Product):
    logging.info(f"Update du produit avec l'id {p.id}")
    sql = "UPDATE " + ProductDao.TABLE_NAME + " SET description=:description, prix=:prix WHERE id=:id"
    cursor = self.__cnx.cursor()
    try:
      cursor.execute(sql, {"id" : p.id, "description" : p.description, "prix": p.prix})
      self.__cnx.commit()
    except sqlite3.Error as e:
      logging.error(e)
    else:
      pass
    finally:
      cursor.close()

  def deleteProductById(self, id: int):
    logging.info(f"Suppression du produit avec l'id {id}")
    sql = f"DELETE FROM {ProductDao.TABLE_NAME} WHERE id = ?"
    product = None
    cursor = self.__cnx.cursor()
    try:
      cursor.execute(sql,(id,))
      self.__cnx.commit()
    except sqlite3.Error as e:
      logging.error(e)
    else:
      logging.info(f"Succès de la suppression du produit avec l'id {id}")
    finally:
      cursor.close()
    return product

if __name__ == "__main__":
  dao = ProductDao()
  print("____init_table____")
  dao.init_table()

  print("____getAllProducts____")
  print(dao.getAllProducts())

  print("____getProductById(2)____")
  print(dao.getProductById(2))

  print("____addProduct(Product(19,'Test', 1999))____")
  product = Product(19,"Test", 1999)
  dao.addProduct(product)
  print(dao.getAllProducts())

  print("____deleteProductById(4)____")
  dao.deleteProductById(4)
  print(dao.getAllProducts())
  
  print("____updateProduct(Product(2,'Edited', 9999))____")
  product = Product(2,"Edited", 9999)
  dao.updateProduct(product)
  print(dao.getAllProducts())

  dao.close()