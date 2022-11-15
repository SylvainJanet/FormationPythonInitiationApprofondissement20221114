# Ecrire une fonction qui transformer une chaine de 
# caracteres en accronyme
# Salut les    geeks -> SLG

import string
def accronyme(chaine: str):
  return ''.join([mot.upper()[0] if len(mot) != 0 else '' for mot in chaine.split(' ')])

def accronyme_v2(chaine: str):
  return ''.join([lettre for lettre in accronyme(chaine) if lettre not in string.punctuation])

print(f"{accronyme('Salut les    geeks             ') = }")
print(f"{accronyme('ceci est une phrase très longue ! ') = }")
print(f"{accronyme('Tout ! Est ! La ! ') = }")

print(f"{accronyme_v2('Salut les    geeks             ') = }")
print(f"{accronyme_v2('ceci est une phrase très longue ! ') = }")
print(f"{accronyme_v2('Tout ! Est ! La ! ') = }")