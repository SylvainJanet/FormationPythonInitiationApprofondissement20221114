# Créer une méthode anagramme(mot1: str, mot2: str)
# qui permet de vérifier si deux mots sont des 
# anagrammes

# def anagramme(mot1: str, mot2: str):
#   if len(mot1) != len(mot2):
#     return "Pas un anagramme"
#   for c in mot1:
#     if mot1.count(c) != mot2.count(c):
#       return "Pas un anagramme"
#   return "Ce sont des anagrammes"

# Solution alternative :
# def anagramme(mot1: str, mot2: str):
#   liste1, liste2 = list(mot1), list(mot2)
#   liste1.sort()
#   liste2.sort()
#   return liste1 == liste2

def anagramme(mot1: str, mot2: str):
  return sorted(mot1) == sorted(mot2)

print(f"{anagramme('parisien','aspirine')=}")
print(f"{anagramme('parisien','aspirines')=}")