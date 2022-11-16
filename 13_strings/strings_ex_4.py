# Créer une méthode rot(chaine, number) qui encode une 
# chaine de caractères selon le code de César en 
# utilisant le paramètre number.
# Code de césar : https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage
# Attention aux majuscules/minuscules !
# Pour s'aider : https://fr.wikibooks.org/wiki/Les_ASCII_de_0_%C3%A0_127/La_table_ASCII#Descriptif3
# Exemple : 
# rot("ABCD",3) = "DEFG"
# rot("Message secret",13) = "Zrffntr frperg"
# Pour décoder un message, il suffit d'utiliser 
# rot(message_encode,26-ancien_number) Et donc :
# rot("DEFG",23) = "ABCD"
# rot("Zrffntr frperg",13) = "Message secret"

def rot_ascii_character(code, number, index_min, index_max):
  if (code < index_min or code > index_max):
    return code
  if (code+number>index_max):
    new_number_ascii = index_min + code + number - (index_max + 1)
  else:
    new_number_ascii = code + number
  return new_number_ascii

def rot_ascii_character_improved(code, number, index_min, index_max):
  if (code < index_min or code > index_max):
    return code
  return index_min + (code - index_min + number) % (index_max - index_min +1)

def rot_ascii_majuscule(code, number):
  return rot_ascii_character_improved(code, number, 65, 90)

def rot_ascii_minuscule(code, number):
  return rot_ascii_character_improved(code, number, 97, 122)

def rot(chaine, number):
  result=""
  for char in chaine:
    number_ascii = ord(char)
    if (number_ascii < 65) or (number_ascii > 90 and number_ascii < 97) or (number_ascii > 122):
      result = result+char
    else:
      if number_ascii<=90: # majuscule
        new_number_ascii = rot_ascii_majuscule(number_ascii, number)
      else: #minuscule
        new_number_ascii = rot_ascii_minuscule(number_ascii, number)
      result = result + chr(new_number_ascii)
  return result

def rot11(chaine):
  return rot(chaine,11)

def rot15(chaine):
  return rot(chaine,15)

print(rot("ABCD",3))
print(rot("Message secret",13))
print(rot("DEFG",23))
print(rot("Zrffntr frperg",13))