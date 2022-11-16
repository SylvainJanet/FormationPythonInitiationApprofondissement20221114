# Fonctions de base de Python utilisables sur les itérables
# (listes, tuples, dictionnaires, set, ...)

iterable1 = [0, 1, 0, 1, 1]
iterable2 = [0, 0, 0, 0, 0]
iterable3 = [1, 1, 1, 1, 1]
iterable4 = [True, False, True, True]
iterable5 = ["a", "b", "c", "d", "e"]

# vérifier si toutes les valeurs sont "vraies"
print(all(iterable1))
print(all(iterable3))
print(all(iterable4))

print("_____")

# vérifier qu'au moins une valeur est "vraie"
print(any(iterable1))
print(any(iterable2))
print(any(iterable4))

print("_____")

# renvoie la longueur de l'itérable
print(len(iterable5))

print("_____")

# calculer la somme des éléments (l'itérable doit contenir des nombres)
print(sum(iterable1))
# print(sum(iterable5)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# raison : pour faire la somme, il commence à 0 puis additionne les éléments
# uns par uns.

print("_____")

# trouver la valeur minimale / maximale des éléments
print(min(iterable1))
print(max(iterable3))