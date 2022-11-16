# class IdNegatif(Exception):
#   def __init__(self, message):
#     super().__init__(message)

# class PrixNegatif(Exception):
#   def __init__(self, message):
#     super().__init__(message)

class CustomException(Exception):
  def __init__(self,message):
    super().__init__(message)

class IdNegatif(CustomException):
  pass

class PrixNegatif(CustomException):
  pass