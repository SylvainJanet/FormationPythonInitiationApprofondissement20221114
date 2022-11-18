class CustomException(Exception):
  def __init__(self, message):
    super().__init__(message)
    self.message = message

  def __str__(self):
    return self.message

class IdNegatifException(CustomException):
  """Exception levée lorsqu'on tente de mettre un id négatif"""

class PrixNegatifException(CustomException):
  """Exception levée lorsqu'on tente de mettre un prix négatif"""

class NegativeQuantityException(CustomException):
  pass

class ProductNotInCartException(CustomException):
  pass

class ZeroQuantityException(CustomException):
  pass