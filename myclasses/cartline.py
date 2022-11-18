from myclasses.product import Product
from myclasses.myexceptions import NegativeQuantityException, ZeroQuantityException
from typing import List


class CartLine:
  def __init__(self,product: Product,quantity: int):
    self.__set_product(product)
    self.__set_quantity(quantity)

  def __get_product(self):
    return self.__product
  def __set_product(self, value):
    self.__product = value

  def __get_quantity(self):
    return self.__quantity
  def __set_quantity(self, value):
    if value < 0:
      raise NegativeQuantityException("Can't have a negative amount in Cart")
    if value == 0:
      raise ZeroQuantityException("Can't have zero amount in Cart")
    self.__quantity = value

  product: Product = property(__get_product,__set_product)
  quantity: int = property(__get_quantity,__set_quantity)

  def remove(self, qty:int):
    self.quantity -= qty
  
  def add(self, qty: int):
    self.quantity += qty
  
  def get_price(self):
    p:Product = self.product
    return p.prix * self.quantity

  def to_dict(self):
    return {
      "product":self.product.to_dict(),
      "quantity":self.quantity
    }

  def to_list_string(self):
    resultat = self.product.to_list_string()
    resultat.append(str(self.quantity))
    return resultat

  @staticmethod
  def from_json(dict: dict):
    return CartLine(
        Product.from_json(dict["product"]),
        int(dict["quantity"]))   

  @staticmethod
  def from_csv(line: List[str]):
    return CartLine(
        Product.from_csv(line),
        int(line[3])
      )

  def __str__(self):
    p:Product = self.product
    return f"({p.id}) {p.description} - {self.quantity} x : total {self.get_price()} €"

  def __eq__(cl1, cl2):
    return cl1.product == cl2.product