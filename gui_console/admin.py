from myclasses.product import Product
from mytools.userinput import demander_saisie_nombre_borne, demander_saisie_nombre_positif
from repository.productDao import ProductDao

def print_products(dao: ProductDao):
  products = dao.getAllProducts()
  if not products:
    return print("No products in db")
  for id,description,prix in products:
    print(f"{id = }")
    print(f"\t{description = }")
    print(f"\t{prix = }")

def add_product(dao: ProductDao):
  description = input("Description ? ")
  prix = demander_saisie_nombre_positif("Prix ?")
  product = Product(0,description,prix)
  dao.addProduct(product)

def delete_product(dao: ProductDao):
  id_to_delete = demander_saisie_nombre_positif("id to delete ? ")
  dao.deleteProductById(id_to_delete)

def edit_product(dao:ProductDao):
  id_to_update = demander_saisie_nombre_positif("id to update ? ")
  description = input("New description ?")
  prix = demander_saisie_nombre_positif("New price ?")
  product = Product(id_to_update,description,prix)
  dao.updateProduct(product)

def gerer_produit():
  dao = ProductDao()
  while True:
    user_input = demander_saisie_nombre_borne("""__________ Menu __________
1- Afficher la liste des produits.
2- Ajouter un produit
3- Supprimer un produit
4- Editer un produit
5- Quitter
Votre choix ?""",1,5)
    if user_input == 5:
      dao.close()
      break
    if user_input == 1:
      print_products(dao)
    if user_input == 2:
      add_product(dao)
    if user_input == 3:
      delete_product(dao)
    if user_input == 4:
      edit_product(dao)
    input("Press enter")