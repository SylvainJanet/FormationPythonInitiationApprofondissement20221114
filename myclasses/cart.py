from myclasses.product import Product
from typing import List
from myclasses.cartline import CartLine
from myclasses.myexceptions import ProductNotInCartException

class Cart:
  def __init__(self,lines: List[CartLine]):
    self.__set_lines(lines)

  def __get_lines(self):
    return self.__lines
  def __set_lines(self, value):
    self.__lines = value

  lines: List[CartLine] = property(__get_lines,__set_lines)

  def get_total_price(self):
    return sum([line.get_price() for line in self.lines])

  def add_product(self,p:Product, qty: int):
    if not CartLine(p,1) in self.lines:
      self.lines.append(CartLine(p,qty))
    else:
      index = self.lines.index(CartLine(p,1))
      self.lines[index].add(qty)

  def remove_product(self,p:Product, qty: int):
    if not CartLine(p,1) in self.lines:
      raise ProductNotInCartException("Product not found")
    else:
      index = self.lines.index(CartLine(p,1))
      if qty >= self.lines[index].quantity:
        self.lines.pop(index)
      else:
        self.lines[index].remove(qty)
    
  def clear(self):
    self.lines.clear()

  def to_list_dict(self):
    return [line.to_dict() for line in self.lines]

  def to_list_list_string(self):
    return [line.to_list_string() for line in self.lines]
  
  @staticmethod
  def from_json(liste: List[dict]):
    lines = [CartLine.from_json(l) for l in liste]
    return Cart(lines)

  @staticmethod
  def from_csv(liste: List[List[str]]):
    lines = [CartLine.from_csv(l) for l in liste]
    return Cart(lines)

  def __str__(self):
    if self.lines:
      return "\n".join([str(line) for line in self.__lines])+f"\nTotal : {self.get_total_price()} €"
    return "Empty cart"