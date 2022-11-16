# Attributs d'instance / attributs statiques (ou attributs de classe synonyme)

# Attributs d'instances : chaque instance a sa propre valeur
# Attributs statiques : partagé par toutes les instances

# on souhaite conserver le nombre de personnages instanciés dans 
# l'appli

class Personnage:
  total_personnage = 0 # valeur initialisée lors du chargement
  # de la classe en mémoire
  def __init__(self, nom = "John", arme = "Epée", pdv = 100):
    self.nom = nom 
    self.arme = arme
    self.pdv = pdv
    Personnage.total_personnage += 1

  # les méthodes ou attributs commencant et terminant par des _ _ 
  # sont appelées soit spéciales soit magiques
  # il existe une méthode spéciale, __del__ qui est appelée par le ramasse miettes
  # juste avant de libérer l'espace mémoire associé à un objet
  # 1 argument obligatoire, qui correspond à l'instance qui va être supprimée
  # self
  def __del__(self):
    Personnage.total_personnage -= 1

  # méthode d'instance : méthode qui effectue un traitement avec une instance
  # méthode propre à chaque instance
  # premier argument obligatoire : self. Il correspond à l'instance qui fait
  # appel à la méthode
  def combattre(self, degat = 10):
    self.pdv -= degat
    print(f"Combat terminé. Il reste {self.pdv} pdv au personnage {self.nom}")

  # méthode de classe : méthode partagée par toutes les instances
  # dont le comportement ne dépend pas d'une instance en particulier
  # on utilise un décorateur : 
  # une spécification à la ligne précédent la signature de la méthode
  # un premier argument obligatoire : cls pour référence à la classe
  @classmethod
  def afficher_total(cls): # cls sera Personnage
    print(f"Il y a un total de {cls.total_personnage} personnages")

  # méthode statique : comme une méthode de classe, sauf que l'argument cls
  # est inutile et donc pas d'argument obligatoire
  @staticmethod
  def dire_bonjour():
    print("Bonjour")

  # FIN DU BLOC CLASS

print(f"Il y a un total de {Personnage.total_personnage} personnages")
p1 = Personnage()
print(f"Il y a un total de {Personnage.total_personnage} personnages")
p2 = Personnage("Maude","Hache",150)
print(f"Il y a un total de {Personnage.total_personnage} personnages")
p1 = Personnage("Cyril","Dague",50)
print(f"Il y a un total de {Personnage.total_personnage} personnages")

# John n'est plus référencé par aucune variable : on ne peut plus y avoir accès
# il ne sert plus à rien dans le programme
# un ramasse miettes vient régulièrement libérer l'espace mémoire associé
# aux objets qui ne sont plus référencés

p1.combattre()
p1.combattre(25)

Personnage.afficher_total()
Personnage.dire_bonjour()
