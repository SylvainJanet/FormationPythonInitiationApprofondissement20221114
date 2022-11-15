# les tuples sont des collections qui sont proches des listes
# les tuples sont des listes non mutables, non modifiables

prenoms = ("Chloé","Nicolas","Marjorie","Nicolas")
print(prenoms)

print("_____")

print(prenoms[0])

print("_____")

for p in prenoms:
  print(p)

print("_____")

nbr = prenoms.count("Nicolas")
print(nbr)

print("_____")

# les tuples ne sont pas modifiables

# prenoms.append("Sergio") # AttributeError: 'tuple' object has no attribute 'append'
# prenoms[1] = "Sergio" # TypeError: 'tuple' object does not support item assignment

# tuples à un élément
nombres = (1) # parenthèses vues comme parenthèses de priorité des opérations
print(nombres)
print(type(nombres))

nombres = (1,)
print(nombres)
print(type(nombres))

# déballage ou unpacking de tuple
prenoms = ("Chloé","Marjorie","Nicolas")

# au lieu d'écrire
# name_0 = prenoms[0]
# name_1 = prenoms[1]
# name_2 = prenoms[2]

# on peut écrire :
name_0, name_1, name_2 = prenoms

print(f"{prenoms = }")
print(f"{name_0 = }")
print(f"{name_1 = }")
print(f"{name_2 = }")

x, y = (5,6)
print(f"{x = }")
print(f"{y = }")

name_0, *reste = prenoms # reste sous forme de liste
print(f"{prenoms = }")
print(f"{name_0 = }")
print(f"{reste = }")
