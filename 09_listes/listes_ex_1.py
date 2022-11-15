# Réduire ces algorithmes à l'aide, des listes en 
# compréhension 
# a)
nombres = [1, 21, 45, 12, 32, 65, 1002, 109, 83]
nombres_pairs = []
for i in nombres:
  if i % 2 == 0:
    nombres_pairs.append(i)
print(nombres_pairs)

nombres_pairs_comprehension = [nbr for nbr in nombres if nbr % 2 == 0]
print(nombres_pairs_comprehension)

# b)
nombres = range(-10, 10)
nombres_positifs = []
for i in nombres:
  if i >= 0:
    nombres_positifs.append(i)
print(nombres_positifs)

nombres_positifs_comprehension = [nbr for nbr in nombres if nbr >= 0]
print(nombres_positifs_comprehension)

# c)
nombres = range(5)
nombres_doubles = []
for i in nombres:
  nombres_doubles.append(i * 2)
print(nombres_doubles)

nombres_double_comprehension = [2*nombre for nombre in nombres]
print(nombres_double_comprehension)

# d)
nombres = range(10)
nombres_inverses = []
for i in nombres:
  if i % 2 == 0:
    nombres_inverses.append(i)
  else:
    nombres_inverses.append(-i)
print(nombres_inverses)

def opposer_nombres_impairs(nbr):
  # if nbr % 2 == 0:
  #   return nbr
  # else:
  #   return -nbr

  # if nbr % 2 == 0:
  #   return nbr
  # return -nbr

  # operateur ternaire
  return nbr if nbr % 2 == 0 else -nbr

nombres_inverses_comprehension = [opposer_nombres_impairs(nbr) for nbr in nombres]

nombres_inverses_comprehension = [(nbr if nbr % 2 == 0 else -nbr) for nbr in nombres]
