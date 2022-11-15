# Variables
# variable : zone mémoire qui permet de stocker une valeur typée
# Il y a plusieurs types de variables en Python
# types numériques : int, float, complex
# types textuel : str
# types booléens : bool
# types collection : range, tuple, list
# types de mapping : dict
# types d'ensembles : set (frozenset)
# (types binaires : memoryview, bytearray, bytes) 

# déclaration : NOM = VALEUR
# règles à respecter dans le nommage des variables
# 1) le nom d'une variable ne peut contenir que des lettres, des chiffres, des underscores ( _ )
# pas d'espace ou de tiret ( - )
# 2) le nom d'une variable ne peut pas commencer par un chiffre
# 3) le nom est sensible à la casse
# age, AGE, Age sont 3 variables différentes
# 4) On ne peut utiliser de mots clé Python pour créer nos variables
# https://www.w3schools.com/python/python_ref_keywords.asp
entier = 15 # Python comprend qu'il s'agit d'un entier
flottant = 3.14159265 # Python comprend qu'il s'agit d'un flottant : . et non ,
complexe = 4 + 2j # j pour le nombre imaginaire
texte = "Bonjour"
# texte = 'Bonjour' # fait exactement la même chose
# nomvariable = nouvellevaleur # permet egalement de modifier la valeur d'une variable
booleen = True # Mots clés : True et False

print(entier)
print(flottant)
print(complexe)
print(texte)
print(booleen)

# Pour inviter l'utilisateur à saisir quelque chose et récupérer le texte dans une variable
# place un curseur juste à côté de ce qui est donné en paramètre
# tant que l'utilisateur n'a pas appuyé sur entré, le programme est figé
saisie = input("Entrez du texte : ")
# print peut être utilisé pour afficher plusieurs choses
# elles seront séparées par des espaces
print("Texte saisi :", saisie)

# PEP 8 (Python Enhancement Proposals)
# https://www.python.org/dev/peps/pep-0008/#naming-conventions
# 1) le nom des variables
# il existe plusieurs case
# - camelCase : tout en minuscules, sauf les initiales en majuscules, à l'exception de la première lettre qui est
# en minuscules
# ceciEstMaVariable
# - PascalCase : tout en minuscules, sauf les initiales
# CeciEstMaVariable
# - snake_case : tout en minuscules, les mots séparés par des underscores
# ceci_est_ma_variable

# En Python : le nom des variables est en snake_case
# 2) le nom des (pseudo-)constantes en snake_case majuscule
# NOM_DE_LA_CONSTANTE

MA_CONSTANTE = 1234
print(MA_CONSTANTE)

# MA_CONSTANTE = "coucou" # techniquement possible, mais le fait que la variable est en majuscule
# indique que c'est pas censé se produire
# print(MA_CONSTANTE)

# Python est dynamiquement fortement typé
# Les types sont implicites et une variable peut changer de type à n'importe quel moment (dynamique)

ma_variable = "du texte"
print(type(ma_variable))
# type est une fonction qui permet d'obtenir le type d'une variable

ma_variable = 15
print(type(ma_variable))

# En Python, tout est objet, la fonction type renvoie un résultat typé, de type 'type'
print(type(type(ma_variable)))

# il n'est pas possible d'effectuer des opérations entre des types incompatibles
# test = 18 + '4' # erreur :
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


