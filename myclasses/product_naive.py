class Product:
  compteur = 0
  def __init__(self, id, description, prix):
    self.id = id
    self.description = description
    self.prix = prix
  def TVA(self):
    return self.prix * 0.2
  def PrixTTC(self):
    return self.prix + self.TVA()
  def __str__(self):
    return f"id : {self.id} ; description : {self.description} ; price : {self.prix}"
  def __eq__(self, other):
    return self.id == other.id

if __name__ == "__main__":
  p = Product(1,"PC Dell", 1200)
  print(p)
  p2 = Product(2,"PC HP", 1000)
  print(p2)
  print(f"{p} - TVA : {p.TVA()} - prix TTC : {p.PrixTTC()}")
  print(f"{p == p2 = }")