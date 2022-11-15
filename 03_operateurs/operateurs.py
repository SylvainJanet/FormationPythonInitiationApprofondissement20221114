# une expression est une série d'instructions qui renvoie une valeur
# que l'on pourrait mettre dans une variable ou utiliser comme argument d'une
# fonction

a = 15 # 15 est une expression
b = a # a est une expression
print(f"{a = }")
print(f"{b = }") 

non_defini = None # valeur spéciale considére comme "pas de valeur"
print(f"{non_defini = }")

# les opérateurs permettent d'écrire des expressions, et de faire des transformations
# entre plusieurs expressions

print("_____ Opérateurs arithmétiques _____")
# caractère d'échapement : \ permet d'afficher des caractères spéciaux
# \t : tabulation
# \n : retour à la ligne
print("\t\"Addition\"")

a = 2
b = 3
c = a + b
print(f"{a = }")
print(f"{b = }")
print(f"c = {a} + {b} = {c}")

c += 2 # raccourci pour c = c + 2
print(f"après c += 2, {c = }")

# input renvoie toujours une str
# a = input("Entrez un nombre ")
# b = input("Entrez un deuxième nombre ")
a = "5"
b = "8"
c = a + b # ici + fait la concaténation
print(f"{a} + {b} = {c}")
c = int(a) + int(b) # ici on fait la conversion en int puis + sur des int : addition
print(f"{a} + {b} = {c}")
print(type(a)) # int(...) fait la conversion, renvoie le résultat mais ne modifie pas
# les variables en entrée

print("\tSoustraction")

a = 5
b = 3
c = a - b
print(f"{a = }")
print(f"{b = }")
print(f"c = {a} - {b} = {c}")

c -= 2 # raccourci pour c = c - 2
print(f"après c -= 2, {c = }")

a = "5"
b = "8"
# c = a - b # TypeError: unsupported operand type(s) for -: 'str' and 'str'

print("\tMultiplication")

a = 5
b = 3
c = a * b
print(f"{a = }")
print(f"{b = }")
print(f"c = {a} * {b} = {c}")

c *= 2 # raccourci pour c = c * 2
print(f"après c *= 2, {c = }")

print("\tDivision")

a = 4
b = 5
c = a / b
print(f"{a = }")
print(f"{b = }")
print(f"c = {a} / {b} = {c}")

c /= 2 # raccourci pour c = c / 2
print(f"après c /= 2, {c = }")

print("\tPuissance")

a = 2
b = 3
c = a ** b
print(f"{a = }")
print(f"{b = }")
print(f"c = {a} ** {b} = {c}")

c **= 2 # raccourci pour c = c ** 2
print(f"après c **= 2, {c = }")

print("\tDivision entière")

a = 11
b = 2
c = a // b
print(f"{a = }")
print(f"{b = }")
print(f"c = {a} // {b} = {c}")

c //= 2 # raccourci pour c = c // 2
print(f"après c //= 2, {c = }")


print("\tModulo")

a = 14
b = 5
c = a % b
print(f"{a = }")
print(f"{b = }")
print(f"c = {a} % {b} = {c}")

c %= 2 # raccourci pour c = c % 2
print(f"après c %= 2, {c = }")

print("_____ Opérateurs de comparaison _____")

# < : strictement plus petit que
# <= : inférieur ou égal
# > : strictement plus grand que
# >= : supérieur ou égal

x = 5
y = 9
resultat = x > y # booleen
print(resultat)

# == : égal à
# != : différent de

resultat = x != y
print(resultat)

resultat = x == y
print(resultat)

print("_____")

# il existe d'autres opérateurs :
# des opérateurs logiques : or, and, not
# des opérateurs logiques par bit : |, &, ~
# idée : on fait une conversion en binaire, 
# on voit les 0 comme False et les 1 comme True, et on fait des opération logiques
# bit par bit

# 5 | 7 -> 101 | 111 -> 111 -> 7
print(5 | 7)
# 5 & 7 -> 101 | 111 -> 101 -> 5
print(5 & 7)

# is, in, ...