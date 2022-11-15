# Ecrire un programme qui demande à l'utilisateur un 
# nombre entre 1 et 10 et qui affiche le double. Si 
# l'utilisateur n'écrit pas un nombre, lui redemander.

while True:
  user_input = input("Entrer un nombre entre 1 et 10 ")
  try:
    number = int(user_input)
  except ValueError:
    print("Ceci n'est pas un nombre")
    continue
  if 1 <= number <= 10:
    break
  print("Nombre invalide")

print(f"Votre nombre : {number} - le double : {2 * number}")