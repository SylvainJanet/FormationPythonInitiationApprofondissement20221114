# un ensemble est une collection non ordonnée d'éléments sans doublon
# cette collection supporter les opérations sur les ensembles : l'union, l'intersection, la différence,
# la différence symétrique

panier = {"apple", "orange", "apple", "pear", "banana","orange","kiwi"}
print(panier)

# on ne peut mettre que des éléments de type non mutable dans un ensemble
# test = { 3, [1,2,3], 4} # TypeError: unhashable type: 'list'

variable = {} # dictionnaire vide
print(variable)
print(type(variable))

variable = set()
print(variable)
print(type(variable))

# Par exemple, on peut déterminer les lettres d'une str
s1 = set("abracadabra")
s2 = set("alacazam")

print(f"{s1 = }")
print(f"{s2 = }")

# lettres dans s1 ou dans s2 ou dans les deux (ou inclusif)
print(s1 | s2)
print(s1.union(s2))

# lettres dans s1 et dans s2
print(s1 & s2)
print(s1.intersection(s2))

# lettres dans s1 mais pas dans s2
print(s1 - s2)
print(s1.difference(s2))

# lettres dans s1 ou dans s2 mais pas dans les deux (ou exclusif)
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

print("_____")

# les ensembles en compréhension sont supportés

res = {x for x in 'abracadabra' if x not in 'abc'}
print(res)
