# Afficher un menu : 
#     Menu
#     1) Convertir minutes en heures
#     2) Quitter
#     Votre choix ?
# Et implémenter les fonctionnalités.
# Par exemple, la conversion transformera 90 minutes 
# en 1 h 30 minutes

while True:
  user_input = input("""Menu
1) Convertir minutes en heures
2) Quitter
Votre choix ? """)
  if (user_input == "2"):
    break
  if (user_input == "1"):
    while True:
      user_input = input("Donner le nombre de minutes ")
      minutes = int(user_input)
      if (minutes >= 0):
        break
      print("Merci d'entrer un nombre positif")
    print(f"{minutes} m = {minutes // 60} h {minutes % 60} m")
    input()