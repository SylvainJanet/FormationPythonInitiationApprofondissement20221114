# Ecrire une fonction qui permet de demander à 
# l'utilisateur un nombre et qui renvoie à coup sur un 
# nombre.


def demander_saisie_nombre(invite = "Merci d'entrer un nombre"):
  while True:
    user_input = input(invite)
    try:
      result = int(user_input)
      return result
    except ValueError:
      print("Seuls les caractères [0-9] sont autorisés")

def demander_saisie_nombre_borne(invite,minimum = 1, maximum = 10):
  invite = invite + f" entre {minimum} et {maximum} "
  while True:
    nombre_input = demander_saisie_nombre(invite)
    if minimum <= nombre_input <= maximum:
      return nombre_input

nombre = demander_saisie_nombre_borne("Entrer un nombre", 0, 100)
print(f"Nombre choisi {nombre}")

nombre = demander_saisie_nombre_borne("Entrer un nombre")
print(f"Nombre choisi {nombre}")