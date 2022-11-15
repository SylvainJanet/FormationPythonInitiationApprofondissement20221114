# Faire un programme qui permet d'ajouter ou retirer 
# des produits d'une liste de courses. Lorsque le 
# programme demarre, l'utilisateur a le choix entre:
# 	1- Afficher la liste de courses.
# 	2- Ajouter un produit a la liste de courses (chaine 
#  de caracteres ex: pomme)
# 	3- Retirer un produit de la liste de course 
# 	4- Supprimer toute la liste de courses
# 	5- Quitter le programme
# Tant que l'utilisateur ne saisit pas "quitter", on 
# continue la boucle
# Si l'utilisateur tape 1 : on affiche la liste des 
# produits 
# Si l'utilisateur tape 2 : on lui demande le nom du 
# produit à ajouter et on l'ajoute à la liste de courses
# Si l'utilisateur tape 3 : on lui demande le nom du 
# produit à retirer et on le retire de la liste de
# courses
# Si l'utilisateur tape 4 : on vide la liste
# Si l'utilisateur tape 5: on affiche "Au revoir" et on 
# quitte le programme
if __name__ == "__main__":
  import sys
  import os
  SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(os.path.dirname(SCRIPT_DIR))
  
from mytools.userinput import demander_saisie_nombre_borne

def say_goodbye():
  print("Au revoir")

def print_list_products(list_products):
  if len(list_products) == 0:
    print("La liste est vide")
  else:
    print(f"Produits : {', '.join(list_products)}")

def add_product(list_products):
  while True:
    product_to_add = input("Que voulez-vous ajouter à votre liste de courses ?").lower()
    if product_to_add.isspace() or product_to_add == "":
      print("Merci d'entrer un produit")
      continue
    if (list_products.count(product_to_add.strip())) > 0:
      print(f"Le produit '{product_to_add}' est déja dans votre liste de courses")
    else:
      list_products.append(product_to_add.strip())
      print(f"Le produit '{product_to_add}' a été ajouté à votre liste de courses")
    break

def delete_product(list_products):
  while True:
    product_to_delete = input("Quel produit voulez-vous supprimer ?").lower()
    if product_to_delete.isspace() or product_to_delete == "":
      print("Merci d'entrer un produit")
      continue
    try:
      list_products.remove(product_to_delete.strip())
      print(f"Le produit '{product_to_delete.strip()}' a été supprimé de votre liste de courses")
    except ValueError:
      print(f"Le produit '{product_to_delete.strip()}' n'a pas été trouvé dans votre liste de courses")
    break

def delete_all_products(list_products):
  for product in list_products.copy():
    list_products.remove(product)
  print("Votre liste de course est désormais vide")

list_products = []
while True:
  user_input = demander_saisie_nombre_borne("""__________ Menu __________
1- Afficher la liste de courses.
2- Ajouter un produit a la liste de courses
3- Retirer un produit de la liste de course 
4- Supprimer toute la liste de courses
5- Quitter le programme
Votre choix ?""", 1, 5)
  if user_input == 5:
    say_goodbye()
    break
  if user_input == 1:
    print_list_products(list_products)
  if user_input == 2:
    add_product(list_products)
  if user_input == 3:
    delete_product(list_products)
  if user_input == 4:
    delete_all_products(list_products)
  input("Faites Entrée ")
    