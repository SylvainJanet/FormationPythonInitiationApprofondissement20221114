# lorsqu'on plusieurs classes partagent certains éléments, certains comportement

# class Chat:
#   def __init__(self, nom, age):
#     self.nom = nom
#     self.age = age
#     # il faudrait encapsuler ces attributs
#   def identite(self):
#     print(f"Je suis un chat et je m'appelle {self.nom}")
#   def cri(self):
#     print("Miaou")
#   def __str__(self):
#     return f"Nom : {self.nom} - age : {self.age}"

# class Chien:
#   def __init__(self, nom, age):
#     self.nom = nom
#     self.age = age
#   def identite(self):
#     print(f"Je suis un chien et je m'appelle {self.nom}")
#   def cri(self):
#     print("Ouaf")
#   def __str__(self):
#     return f"Nom : {self.nom} - age : {self.age}"

# on peut factoriser les éléments communs dans une classe Animal

class Animal:
  def __init__(self, nom, age):
    self.nom = nom
    self.age = age
  def identite(self):
    print(f"Je suis un animal et je m'appelle {self.nom}")
  def __str__(self):
    return f"Nom : {self.nom} - age : {self.age}"

class Chat(Animal): # on dit que la classe Chat hérite de la classe Animal
  # et que la classe Animal est la classe mère de la classe Chat
  def __init__(self, nom, age, couleur):
    # self.nom = nom
    # self.age = age
    super().__init__(nom, age)
    # super() fait référence à la classe mère
    # on peut voir super() comme étant un équivalent de
    # "self vu comme étant une instance de la classe mère"
    self.couleur = couleur
  def cri(self):
    print("Miaou")
  # on peut redéfinir des méthodes existantes dans la classe Animal
  def identite(self):
    print(f"Je suis un chat et je m'appelle {self.nom}")

class Chien(Animal):
  def cri(self):
    print("Ouaf")

cat = Chat("Mistigris",5,"gris")
cat.identite()
print(cat)
cat.cri()

dog = Chien("Médor",10)
dog.identite()
print(dog)
dog.cri()

# quand on écrit 
# class MaClasse
# c'est comme si on écrivait
# class MaClasse(object)
# autrement dit toutes les classes héritent de la classe object
# qui comprend entre autres les comportements par défaut des méthodes __str__ et __eq__

# toutes les types d'exceptions héritent d'un type d'exception de base, nommé Exception
# une bonne pratique est d'implémenter nos propres classes d'exceptions pour chaque type d'erreur dans notre projet
# -> lorsqu'on fait un try-except, on peut avoir un comportement spécifique pour chaque erreur
# -> facilite aussi le débuggage

# En Python, on peut hériter de plusieurs classes
# Néanmoins, cela peut poser des problèmes complexes (Diamond Problem par exemple)
# https://he-arc.github.io/livre-python/super/index.html
# class A(B,C) avec B et C implémentent la même méthode
# laquelle choisir ? A quoi super() fait référence ?
# une possibilité : B apparaît en premier, du coup je prends celle de B
# oui mais et si B hérite de C ?
