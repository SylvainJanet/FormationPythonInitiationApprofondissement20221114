# Créer un nouveau module dans le projet myclasses
# Y mettre un fichier product.py qui contient une 
# classe Product qui est décrit par un id, une 
# description, un prix, qui a des méthodes pour 
# calculer la TVA d'un produit et le prix TTC 
# (prix tva = 0.2 * prix, 
# et prix ttc = prix + prix tva),
# un compteur du nombre total de produits instanciés, 
# une méthode qui permet de print() correctement un 
# produit, et une méthode qui compare des produits 
# (deux produits sont les mêmes ssi ils ont le même id)

class Product:
  compteur = 0

  def __init__(self, id, description, prix):
    self.id = id
    self.description = description
    self.prix = prix
    Product.compteur += 1

  def TVA(self):
    return self.prix * 0.2
  def PrixTTC(self):
    return self.prix + self.TVA()

  def __str__(self):
    return f"id : {self.id} ; description : {self.description} ; price : {self.prix}"
  def __eq__(self, other):
    return self.id == other.id
  def __del__(self):
    Product.compteur -= 1

if __name__ == "__main__":
  p = Product(1,"PC Dell", 1200)
  print(p)
  p2 = Product(2,"PC HP", 1000)
  print(p2)
  print(f"{p} - TVA : {p.TVA()} - prix TTC : {p.PrixTTC()}")
  print(f"{p == p2 = }")