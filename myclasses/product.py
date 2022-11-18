from myclasses.myexceptions import IdNegatif,PrixNegatif

class Product:
  compteur = 0
  def __init__(self, id, description, prix):
    self.id = id
    self.description = description
    self.prix = prix
    Product.compteur += 1

  def __get_id(self):
    return self.__id
  def __set_id(self, value):
    if value < 0:
      raise IdNegatif("Id negatif !")
    self.__id = value

  def __get_description(self):
    return self.__description
  def __set_description(self, value):
    self.__description = value

  def __get_prix(self):
    return self.__prix
  def __set_prix(self, value):
    if value < 0:
      raise PrixNegatif("Prix negatif !")
    self.__prix = value

  id = property(__get_id,__set_id)
  description = property(__get_description,__set_description)
  prix = property(__get_prix,__set_prix)

  def TVA(self):
    return self.prix * 0.2
  def PrixTTC(self):
    return self.prix + self.TVA()
  def __str__(self):
    return f"id : {self.id} ; description : {self.description} ; prix : {self.prix}"
  def __eq__(self, other):
    return self.id == other.id
  def __del__(self):
    Product.compteur -= 1

if __name__ == "__main__":
  p = Product(1,"PC Dell", 1200)
  print(p)
  p2 = Product(2,"PC HP", 1000)
  print(p2)
  print(f"{p} - prix TVA : {p.TVA()} - prix TTC : {p.PrixTTC()}")
  print(f"{p == p2 = }")
  p.prix = -4