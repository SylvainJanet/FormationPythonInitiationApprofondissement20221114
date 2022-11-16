# (un des) intérêts de la programmation orientée objet (POO ou OOP en anglais)

# pouvoir calculer la surface de rectangles

# exemple sans utiliser les classes :

def surface(longueur,largeur):
  # ...
  return longueur * largeur


longueur_1 = 20
largeur_1 = 10

longueur_2 = 25
largeur_2 = 15

s1 = surface(longueur_1, largeur_1)
s2 = surface(longueur_2, largeur_2)

print(f"{s1 = }")
print(f"{s2 = }")

# plusieurs problèmes :
# la fonction surface peut être appelée avec n'importe quel nombre
# pas forcément avec des longueurs ou des largeurs de rectangles

nbr_personnages = 10
surface(nbr_personnages,nbr_personnages)
surface(longueur_1, largeur_2)

# les variables sont totalement décorrélées
# la seule raison qui fait qu'on a compris qu'il s'agissait du calcul de deux
# rectangles différents, c'est le _1 et _2 à la fin du nom, le retour à la ligne
# pour mieux visualiser

# le code concernant les traitements appliqués aux rectangles n'est pas centralisé
# en cas de modification de traitement des rectangles, on doit retenir l'emplacement
# des toutes les fonctions qui traitent des rectangles, et toutes les modifier

# rien ne nous empêche de mettre des valeurs absurdes
longueur_3 = -8
largeur_3 = 9

s3 = surface(longueur_3, largeur_3)

print(f"{s3 = }")

# équivalent en objet :
# on ajoute de la structure et du sens à notre code

class Rectangle:
  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur
  def surface(self):
    return self.longueur * self.largeur
  def __str__(self):
    return f"Rectangle de longueur {self.longueur} et de largeur {self.largeur}"

rec1 = Rectangle(20,10)
rec2 = Rectangle(25,15)

print(rec1)
print(rec2)

s1 = rec1.surface()
s2 = rec2.surface()

print(f"{s1 = }")
print(f"{s2 = }")

# pour l'instant, on peut encore utiliser des valeurs absurdes

rec3 = Rectangle(-8,9)

s3 = rec3.surface()

print(f"{s3 = }")