from repository.productDao import ProductDao
from myclasses.product import Product


# dao = ProductDao()
# print("____init_table____")
# dao.init_table()

# print("____getAllProducts____")
# print(dao.getAllProducts())

# print("____getProductById(2)____")
# print(dao.getProductById(2))

# print("____addProduct(Product(19,'Test', 1999))____")
# product = Product(19,"Test", 1999)
# dao.addProduct(product)
# print(dao.getAllProducts())

# print("____deleteProductById(4)____")
# dao.deleteProductById(4)
# print(dao.getAllProducts())

# print("____updateProduct(Product(2,'Edited', 9999))____")
# product = Product(2,"Edited", 9999)
# dao.updateProduct(product)
# print(dao.getAllProducts())

# dao.close()

from gui_console.choices import chose_admin_or_user
from gui_console.admin import gerer_produit
from gui_console.user import gerer_panier

def main():
  choice = chose_admin_or_user()
  if not choice:
    return False
  if choice == 'admin':
    gerer_produit()
  if choice == 'user':
    gerer_panier()
  return True

while main():
  pass