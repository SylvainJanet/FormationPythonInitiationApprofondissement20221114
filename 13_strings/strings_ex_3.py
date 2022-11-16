# Créer une méthode 
# palindrome(mot, space_included = False) 
# qui permet de vérifier si une chaine de caractères 
# est un palindrome.
# Le paramètre space_included permet d'inclure ou 
# non les espaces
# palindrome('kayak') = True
# palindrome('Esope reste ici et se repose') = False
# palindrome('Esope reste ici et se repose', True) = True
# palindrome('chien') = False

def remove_spaces(s: str) -> str:
  return "".join([x for x in s.split(" ") if len(x) > 0])

def inverser(mot: str) -> str:
  liste = list(mot)
  liste.reverse()
  return "".join(liste)

def is_reverse(mot1: str, mot2: str, space_ignored = False):
  if (space_ignored):
    mot1 = remove_spaces(mot1)
    mot2 = remove_spaces(mot2)
    mot1 = mot1.lower()
    mot2 = mot2.lower()
  return mot1 == inverser(mot2)

def palindrome(mot: str, space_ignored = False):
  return is_reverse(mot, mot, space_ignored)
  
print(f"{palindrome('kayak')=}")
print(f"{palindrome('Esope reste ici et se repose')=}")
print(f"{palindrome('Esope reste ici et se repose', True)=}")
print(f"{palindrome('kayaak')=}")