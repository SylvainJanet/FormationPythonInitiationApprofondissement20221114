# créer une méthode find_char(chaine, lettre) qui
# affiche "trouvé" ou "aucun résultat" selon si une 
# lettre apparait dans une chaine de caractères

# Solution possible si on oublie l'opérateur "in"
# def find_char_bool(chaine: str, lettre):
#   for char in chaine.lower():
#     if char == lettre:
#       return True
#   return False

# def find_char(chaine,lettre):
#   if (find_char_bool(chaine,lettre)):
#     print("Trouvée")
#   else:
#     print("Aucun résultat")

# def find_char(chaine,lettre):
#   print("Trouvée") if find_char_bool(chaine,lettre) else print("Aucun résultat")

# Avec l'opérateur "in"
# def find_char(chaine, lettre):
#   if lettre.lower() in chaine.lower():
#     print("Trouvée")
#   else:
#     print("Aucun résultat")

def find_char(chaine,lettre):
  print("Trouvée") if lettre.lower() in chaine.lower() else print("Aucun résultat")

print("find_char('Salut','u')")
find_char("Salut","u")
print("find_char('Salut','z')")
find_char("Salut","z")