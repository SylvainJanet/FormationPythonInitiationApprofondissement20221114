# Ecrire une fonction qui affiche la table de 
# multiplication d'un nombre ou le premier et le dernier 
# multiples sont paramétrés

def table_multiplication(number,first_multiple, last_multiple):
  for i in range(first_multiple, last_multiple +1):
    print(f"{i} x {number} = {i*number}")

print("Table de multiplication de 13 : ")
table_multiplication(13,0,10)