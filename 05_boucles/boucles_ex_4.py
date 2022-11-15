# Afficher les 20 premiers termes de la suite de 
# fibonacci.
# Elle est définie de la manière suivante : 
# Les premiers termes sont 0 et 1, et les termes suivant 
# sont définis comme étant la somme des deux termes 
# précédents.
# Autrement dit, fibo(0) = 0, fibo(1) = 1, et 
# fibo(n+2) = fibo(n) + fibo(n+1)

fibo_1 = 0
fibo_2 = 1
print(fibo_1)
print(fibo_2)
for i in range(3,21):
  fibo_3 = fibo_1 + fibo_2
  print(fibo_3)
  fibo_1 = fibo_2
  fibo_2 = fibo_3
