# encapsulation - idée : protéger les attributs d'un objet lors de l'accès (en lecture, en écriture)
# pour rajouter du contrôle

# on commence par "protéger" les attributs en les rendant pseudo-privés
# on rajoute _ _ devant le nom d'un attribut pour le rendre pseudo-privé
# Il y a obfuscation de nom de l'attribut par Python

# on créé ensuite des accesseurs : GETTERS (en lecture) et SETTERS (en écriture)
# ce sont eux qui font le pont entre l'exterieur et les attributs pseudo-privés

# Enfin, mettre en place le mécanisme de protection en utilisant property

class Rectangle:
  def __init__(self, longueur, largeur):
    # self.__set_longueur(longueur)
    self.longueur_prop = longueur
    self.largeur = largeur

  # GETTERS : accesseurs en lecture
  # un seul argument obligatoire self
  # renvoient la valeur qu'on souhaite lire
  # nom de la méthode : ce qu'on veut
  def __get_longueur(self):
    print("GET LONGUEUR")
    return self.__longueur

  # SETTERS : accesseurs en écriture
  # un argument obligatoire self
  # un deuxième argument obligatoire qui correspond à la valeur qu'on souhaite
  # affecter à l'attribut
  def __set_longueur(self, value):
    print("SET LONGUEUR")
    if value < 0:
      raise ValueError("La longueur ne peut pas être négative")
    self.__longueur = value

  def __get_largeur(self):
    return self.__largeur
  def __set_largeur(self, value):
    if value < 0:
      raise ValueError("La largeur ne peut pas être négative")
    self.__largeur = value

  longueur_prop = property(__get_longueur, __set_longueur)
  largeur = property(__get_largeur, __set_largeur)

  def surface(self):
    return self.__longueur * self.__largeur
  def __str__(self):
    return f"Rectangle de longueur {self.__longueur} et de largeur {self.__largeur}"

rec = Rectangle(10,20)

# print(rec.__longueur) # AttributeError: 'Rectangle' object has no attribute '__longueur'

s = rec.surface()
print(f"{s = }")

# il existe un attribut __dict__ qui permet de voir l'ensemble des attributs d'un objet et leur valeur
# (c'est un dictionnaire attribut:valeur)
print(rec.__dict__)
# print(rec._Rectangle__longueur) # techniquement possible d'accédeur aux attributs pseudo-privés
# faut vraiment le vouloir, et c'est pas une bonne pratique

print("_____")

print(rec.longueur_prop)

print("_____")

rec.longueur_prop = 16
print(rec.longueur_prop)
s = rec.surface()
print(f"{s = }")

print("_____")

# rec.longueur_prop = -12 # ValueError: La longueur ne peut pas être négative

rec2 = Rectangle(-10,29)
s2 = rec2.surface()
print(f"{s2 = }")

# quand on créé une classe, le réflexe est de créer au minimum :
# - le constructeur, les attributs
# - les méthodes __str__, __eq__
# - encapsuler les attributs dans des propriétés (faire des getters et setters et property pour tous les attributs)
# - les méthodes perso