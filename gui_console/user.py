from json.decoder import JSONDecodeError
from mytools.userinput import demander_saisie_nombre_borne, demander_saisie_nombre_positif
from repository.productDao import ProductDao
from myclasses.cart import Cart
from myclasses.cartline import CartLine
from mytools.files import read_file_json, read_file_csv, write_file_json, write_file_csv

def afficher_liste(panier):
  print(panier)

def ajouter_produit(dao:ProductDao,panier:Cart):
  id_to_add = demander_saisie_nombre_positif("Id ? ")
  p = dao.getProductById(id_to_add)
  if not p:
    print("Produit introuvable")
    return
  quantity_to_add = demander_saisie_nombre_positif("Combien voulez-vous en ajouter ?")
  panier.add_product(p,quantity_to_add)
  print("Le produit a été ajouté à la liste")


def retirer_produit(dao:ProductDao, panier:Cart):
  id_to_delete = demander_saisie_nombre_positif("Id ? ")
  p = dao.getProductById(id_to_delete)
  if (not p) or (not CartLine(p,1) in panier.lines) :
    print("Ce produit n'est pas dans votre panier")
    return
  quantity_to_delete = demander_saisie_nombre_positif("Combien voulez-vous en supprimer ?")
  panier.remove_product(p,quantity_to_delete)
  print("Le produit a été supprimé de la liste")

def supprimer_stock(panier:Cart):
  panier.clear()
  print("Liste de courses supprimée")

def au_revoir():
  print("Au revoir")

def export_json(panier: Cart):
  path = input("Chemin vers le fichier ?")
  write_file_json(path, panier.to_list_dict())

def export_csv(panier: Cart):
  path = input("Chemin vers le fichier")
  write_file_csv(path, panier.to_list_list_string())

def import_json(panier: Cart):
  try:
    path = input("Chemin vers le fichier ?")
    imported = read_file_json(path)
    return Cart.from_json(imported)
  except JSONDecodeError:
    print("Erreur d'import. Format du fichier incorrect")
  except FileNotFoundError:
    print("Fichier introuvable")
  return panier

def import_csv(panier: Cart):
  try:
    path = input("Chemin vers le fichier ?")
    imported = read_file_csv(path)
    return Cart.from_csv(imported)
  except (IndexError, ValueError):
    print("Erreur d'import. Format du fichier incorrect")
  except FileNotFoundError:
    print("Fichier introuvable")
  return panier

def gerer_panier():
  dao = ProductDao()
  panier = Cart([])
  while True:
    for id,description,prix in dao.getAllProducts():
      print(f"{id = }")
      print(f"\t{description = }")
      print(f"\t{prix = }")
    user_input = demander_saisie_nombre_borne("""__________ Menu __________
1- Afficher la liste de courses.
2- Ajouter un produit a la liste de courses
3- Retirer un produit de la liste de course 
4- Supprimer toute la liste de courses
5- Exporter la liste de courses (JSON)
6- Exporter la liste de courses (CSV)
7- Importer la liste de courses (JSON)
8- Importer la liste de courses (CSV)
9- Quitter le programme
Votre choix ?""",1,9)
    if user_input == 9:
      au_revoir()
      break
    if user_input == 1:
      afficher_liste(panier)
    if user_input == 2:
      ajouter_produit(dao,panier)
    if user_input == 3:
      retirer_produit(dao,panier)
    if user_input == 4:
      supprimer_stock(panier)
    if user_input == 5:
      export_json(panier)
    if user_input == 6:
      export_csv(panier)
    if user_input == 7:
      panier = import_json(panier)
    if user_input == 8:
      panier = import_csv(panier)
    input("Appuyer sur entrée")