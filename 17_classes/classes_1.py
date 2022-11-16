# Une classe est un type d'objet
# Un objet a 3 particularités, 3 concepts qu'il va falloir définir
# dans une classe. Une classe n'est qu'un descriptif de l'objet
# Lorsqu'on veut parler d'un objet proprement dit, on parle
# d'instance d'une classe.

# la classe : un plan de construction d'un bâtiment
# une instance : l'objet à proprement parler, un bâtiment

# les 3 concepts à définir dans une classe :
# 1) Les propriétés / les champs / les attributs : qui permettent de décrire
# l'objet, de donner son état
# 2) Les méthodes : qui permettent de faire une action avec un objet. Modifier
# son état, ou utiliser son état pour faire un traitement, ...
# 3) Le constructeur : la méthode appelée pour construire les objets

# En Python, tout est objet !

# PascalCase : CeciEstMaClasse - la 1ère lettre de chaque mot en majuscule
class Personnage:
  # Python utilise __init__ pour initialiser les objets
  # un premier paramètre est obligatoire
  # il fait référence à l'objet qui est en train d'être construit
  # souvent on l'appelle self (équivalent de this dans d'autres langages)
  def __init__(self, param_nom = "John", arme = "Epée", pdv = 100):
    self.nom = param_nom # à gauche : attribut
    # à droite : une variable, le paramètre de la fonction
    self.arme = arme
    self.pdv = pdv
  # FIN DU BLOC CLASS

# un peu comme si on faisait Personnage.__init__(p1)
p1 = Personnage()
print(f"Personnage - Nom : {p1.nom} - Arme : {p1.arme} - Pdv : {p1.pdv}")

p2 = Personnage("Maude","Hache",150)
print(f"Personnage - Nom : {p2.nom} - Arme : {p2.arme} - Pdv : {p2.pdv}")

print(p1) # <__main__.Personnage object at 0x00000226A5D26C70>

p3 = Personnage(pdv = 196)
print(f"Personnage - Nom : {p3.nom} - Arme : {p3.arme} - Pdv : {p3.pdv}")