from myclasses.myexceptions import IdNegatifException, PrixNegatifException
from typing import List

class Product:
  compteur = 0
  def __init__(self, id, description, prix):
    self.__set_id(id)
    self.__set_description(description)
    self.__set_prix(prix)

  def __get_id(self):
    return self.__id
  def __set_id(self, value):
    if value < 0:
      raise IdNegatifException("Id negatif !")
    self.__id = value

  def __get_description(self):
    return self.__description
  def __set_description(self, value):
    self.__description = value

  def __get_prix(self):
    return self.__prix
  def __set_prix(self, value):
    if value < 0:
      raise PrixNegatifException("Prix negatif !")
    self.__prix = value

  id = property(__get_id,__set_id,None,"""""")
  description = property(__get_description,__set_description,None,"""""")
  prix = property(__get_prix,__set_prix,None,"""""")

  def TVA(self):
    return self.prix * 0.2
  def PrixTTC(self):
    return self.prix + self.TVA()

  def to_dict(self):
    return {
      "id":self.id,
      "description":self.description,
      "prix":self.prix
    }
    
  def to_list_string(self):
    return [str(self.id),self.description,str(self.prix)]

  @staticmethod
  def from_json(dict: dict):
    return Product(int(dict["id"]), dict["description"], float(dict["prix"]))

  @staticmethod
  def from_csv(line: List[str]):
    return Product(int(line[0]),line[1],float(line[2]))


  def __str__(self):
    return f"id : {self.id} ; description : {self.description} ; prix : {self.prix}"
  def __eq__(self, other):
    return self.id == other.id

if __name__ == "__main__":
  p = Product(1,"PC Dell", -1200)
  print(p)
  p2 = Product(2,"PC HP", 1000)
  print(p2)
  print(f"{p} - TVA : {p.TVA()} - prix TTC : {p.PrixTTC()}")
  print(f"{p == p2 = }")
  p.prix = -4