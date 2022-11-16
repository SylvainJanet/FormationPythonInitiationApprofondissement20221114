# Créer une méthode decimal_to_binary(decimal) qui 
# converti un nombre décimal en un nombre binaire 
# (renvoie une chaine de caractère) 
# Créer une méthode binary_to_decimal(chaine: str) 
# qui converti un nombre binaire (sous forme de 
# chaine de caractères) en un nombre décimal

def decimal_to_binary(decimal):
  if (decimal < 0):
    return "-" + decimal_to_binary(-decimal)
  if (decimal < 2):
    return str(decimal)
  return str(decimal_to_binary(decimal // 2)) +  str(decimal  % 2)
  
print(f"{decimal_to_binary(13)=}")
print(f"{decimal_to_binary(-27)=}")

def check_binary(chaine):
  if chaine[0] == "-":
    if (len(chaine) == 1):
      return False
    start_index = 1
  else:
    start_index = 0
  for char in chaine[start_index:]:
    if (char != "0" and char != "1"):
      return False
  return True

def binary_to_decimal_checked(chaine: str):
  if chaine[0] == "-":
    return -binary_to_decimal_checked(chaine[1:])
  if (len(chaine) == 1):
    return int(chaine[len(chaine)-1]) 
  return int(chaine[len(chaine)-1]) + 2 * binary_to_decimal_checked(chaine[:len(chaine)-1])

def binary_to_decimal(chaine: str):
  if not check_binary(chaine):
    print("Ce n'est pas un nombre binaire")
  else:
    return binary_to_decimal_checked(chaine)

print(f"{binary_to_decimal('1101')=}")
print(f"{binary_to_decimal('-11011')=}")
print(f"{binary_to_decimal('12011')=}")