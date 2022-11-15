# - Coder convertir_heures_en_minutes(heures,minutes) 
# qui renvoie la conversion d'une heure en minutes. Par
# exemple convertir_heures_en_minutes(1,30) renvoie 90
# - Coder convertir_minutes_en_heures(minutes) qui 
# renvoie la conversion de minutes en heures. Par 
# exemple convertir_minutes_en_heures(90) renvoie 1, 30
# - reprendre la fonction demander_saisie_nombre
# - coder demander_saisie_nombre_positif(invite) qui 
# renvoie un nombre positif entré par l'utilisateur
# - on souhaite afficher un menu
# 	Menu
# 	1) Convertir minutes en heures
# 	2) Convertir heures en minutes
# 	3) Quitter
# 	Votre choix ?
# Implémenter les fonctionnalités.

def convertir_heures_en_minutes(heures,minutes):
  return heures * 60 + minutes

def convertir_minutes_en_heures(minutes):
  return minutes // 60 , minutes % 60

def demander_saisie_nombre(invite):
  while True:
    user_input = input(invite)
    try:
      result = int(user_input)
      return result
    except ValueError:
      print("Seul les caractères [0-9] sont autorisés")

def demander_saisie_nombre_positif(invite):
  invite += " (positif) "
  while True:
    nombre_input = demander_saisie_nombre(invite)
    if nombre_input >= 0:
      return nombre_input

def choix_1():
  minutes_input = demander_saisie_nombre_positif("Entrer le nombre de minutes")
  heures, minutes = convertir_minutes_en_heures(minutes_input)
  print(f"{minutes_input} m = {heures} h {minutes} m")
  input()

def choix_2():
  heures = demander_saisie_nombre_positif("Entrer le nombre d'heures")
  minutes_input = demander_saisie_nombre_positif("Entrer le nombre de minutes")
  minutes = convertir_heures_en_minutes(heures, minutes_input)
  print(f"{heures} h {minutes_input} m = {minutes} m")
  input()

while True:
  user_input = input("""Menu
1) Convertir minutes en heures
2) Convertir heures en minutes
3) Quitter
Votre choix ? """)
  if (user_input == "3"):
    break
  if (user_input == "1"):
    choix_1()
  if (user_input == "2"):
    choix_2()