# les modules math et statistics
# fournissent des outils mathématiques et statistiques

import math
import statistics

angle = math.pi / 2

print(f"Le cosinus de {angle} est {math.cos(angle):.1f} et le sinus est {math.sin(angle)}")
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings

sample = [1, 5, 30, 80.7, 2100]
print(f"La moyenne de {sample} est : {statistics.mean(sample)}, son écart type : {statistics.stdev(sample)}")

import requests

r = requests.get("https://www.python.org")
print(r.content)
print("_____")
print(r)