def demander_saisie_nombre(invite):
  while True:
    user_input = input(invite)
    try:
      result = int(user_input)
      return result
    except ValueError:
      print("Seul les caractères [0-9] sont autorisés")

def demander_saisie_nombre_borne(invite,minimum = 1, maximum = 10):
  invite += f" entre {minimum} et {maximum} "
  while True:
    nombre_input = demander_saisie_nombre(invite)
    if minimum <= nombre_input <= maximum:
      return nombre_input

def demander_saisie_nombre_positif(invite):
  invite += " (positif) "
  while True:
    nombre_input = demander_saisie_nombre(invite)
    if nombre_input >= 0:
      return nombre_input

def demander_saisie_chaine_definie(invite):
  while True:
    saisie = input(invite)
    if len(saisie.strip()) != 0:
      return saisie.strip()
    print("Merci d'entrer quelque chose")