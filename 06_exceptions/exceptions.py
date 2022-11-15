# Il y a 3 types d'erreurs : 
# - les erreurs de compilation : détéctées par Visual Studio Code
# - les exceptions : leurs erreurs qui stoppent l'exécution du programme
# https://docs.python.org/3/library/exceptions.html
# - les erreurs qui n'arrêtent pas l'application : c'est lorsque le programme fonctionne, mais n'a pas
# le comportement désiré
a = "4"
b = "5"
addition = a + b
print(addition) # 45

# erreurs de compilation : détéctées et donc résolues avant que le programme puisse être démarré
# exceptions : doivent être anticipées par le développeur et on a des moyens de les gérer
# erreurs non stoppantes : on peut coder des tests unitaires qui vont de manière automatiser vérifier le
# bon fonctionnement des différentes fonctionnalités
# Tests unitaires -> formation de 2j chez Dawan
# Python Intermédiaire : Multithreading et Tests
# idée : pour toutes les fonctionnalités de notre appli, automatiser un processus qui va :
# * prendre des valeurs en entrée : testons pour a = 10 et b = 5
# * exécuter la fonctionnalité : resultat = addition(a,b)
# * vérifier que le résultat correspond au résultat attendu / plus généralement vérifier que la fonctionnalité
# a le bon comportement
# AssertEquals(15, resultat)

# pour gérer les exceptions, on utilise un bloc try - except
try:  
  print("J'essaye de faire un calcul") 
  1 / 0
  print("J'ai essayé !")
except:
  # ce code est exécuté uniquement si une exception est levée dans le bloc try
  print("La division par 0 n'est pas possible")

# Il existe beaucoup d'exceptions, qui ont des noms différents selon le problème qui se produit
# Elles héritent toutes d'un type d'exception de base, nommé Exception

# On peut spécifier un comportement selon le type d'exception qui a été levé

print("_____")

nombre = input("Saisir un nombre : ")
try:
  nombre = int(nombre)
  result = 5 / nombre
  chaine = "Test"
  # char = chaine[10] # IndexError
  # le mot clé raise permet de soulever soit même une erreur
  # raise FileNotFoundError("Fichier introuvable")
except ZeroDivisionError:
  print("La division par 0 n'est pas possible")
except ValueError:
  print("Vous devez saisir un nombre")
except Exception as erreur: # dans les autres cas, on capture l'exception ici
  print("Erreur !")
  print(erreur)
else: # exécuté uniquement si aucune exception n'a été levée
  print("Super ! Tout s'est bien passé !")
finally: # exécuté dans tous les cas
  print("Peu importe ce qu'il arrive, on passe ici !")


# utilité :
try:
  # ouverture d'un flux (connexion à une bdd, ouverture d'un fichier)
  # traitement
  pass
except:
  # traitement d'erreur
  pass

# ...
# ...

# fermeture du flux

# à comparer à :
try:
  # ouverture d'un flux (connexion à une bdd, ouverture d'un fichier)
  # traitement
  # ...
  pass
except:
  # traitement d'erreur
  pass
finally:
  # fermeture du flux
  pass

# ...

print("Suite de mon programme...")
