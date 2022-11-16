# documentation vers l'ensemble des méthodes et attributs spéciaux
# https://docs.python.org/3/reference/datamodel.html
class Personnage:
  total_personnage = 0 

  def __init__(self, nom = "John", arme = "Epée", pdv = 100):
    self.nom = nom 
    self.arme = arme
    self.pdv = pdv
    Personnage.total_personnage += 1

  def __del__(self):
    Personnage.total_personnage -= 1
  
  # lorsqu'on fait un print(instance), Python converti l'instance en chaîne de
  # caractères en faisant str(instance)
  # implicitement, on fait à la méthode __str__ de l'instance
  # Par défaut, elle affiche le type de l'objet et son adresse mémoire
  # on peut la redéfinir et modifier son comportement
  # 1 seul argument : self
  # retourne le résultat de la conversion
  def __str__(self):
    return f"Le personnage {self.nom} est armé de {self.arme} et a {self.pdv} pdv"

  # par défaut, la comparaison de deux objets compare les adresses mémoire
  # en utilisant la méthode __eq__, qu'on peut redéfinir
  # elle prend deux arguments (les objets à comparer)
  # renvoie un booléen qui correpond au résultat attendu ==
  def __eq__(self, other):
    return self.nom == other.nom

  def combattre(self, degat = 10):
    self.pdv -= degat
    print(f"Combat terminé. Il reste {self.pdv} pdv au personnage {self.nom}")

  @classmethod
  def afficher_total(cls):
    print(f"Il y a un total de {cls.total_personnage} personnages")

  @staticmethod
  def dire_bonjour():
    print("Bonjour")

  # FIN DU BLOC CLASS

p = Personnage()
print(p)

p2 = Personnage(pdv = 123)
print(p2)

resultat = p == p2
print(resultat)

liste = [
  Personnage(),
  Personnage("Marie","Arc",25),
  Personnage("Cyril","Dague",50),
]

if p in liste: # on cherche à savoir si le personnage dans la variable p appartient
  # à la liste au sens de ==, c'est à dire qu'il cherche à savoir si il existe
  # un element de la liste e tel que p == e
  print(f"{p.nom} est dans la liste")
else:
  print(f"{p.nom} n'est pas dans la liste")


# lorsqu'on créé une classe : 
# - constructeur, attributs
# - __str__, __eq__
# - méthodes