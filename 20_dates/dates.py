# Pour créer des dates, on va utiliser le package datetime
# on va utiliser 3 classes : date, datetime et timedelta
# date : date sans heures
# datetime : dates avec heures (minutes, secondes, microsecondes)
# timedelta : durées

from datetime import date, datetime, timedelta

# Créer des dates
today = date.today()
before = date(2022,9,14) # 14 septembre 2022

# Afficher des dates
print(f"Aujourd'hui nous sommes le {today}")
print(f"Aujourd'hui nous sommes le {today.day}/{today.month}/{today.year}")
print(f"Aujourd'hui nous sommes le {before.day}/{before.month}/{before.year}")
# on peut afficher une date en utilisant un formattage plus formalisé
# Voir https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
print(f"Aujourd'hui nous sommes le (formaté) {before:%d/%m/%Y}")
# chaine = before:%d/%m/%Y # ne fonctionne pas : ce formatage est propre au fString
chaine = before.strftime("%d/%m/%Y")
print(chaine)

# datetime
now = datetime.now()
then = datetime(2022,11,14,hour=9, minute=30)

print(now)
print(then)

print(then.strftime("%d/%m/%Y - %Hh%M"))

# on peut faire le contraire en convertissant une chaine de caractère en datetime
chaine = "18/11/2022 - 17h00"
end = datetime.strptime(chaine, "%d/%m/%Y - %Hh%M")
print(end)
print(type(end))


# timedelta
now = datetime.now()
then = datetime(2022,11,14,9,30)

interval = now - then
print(interval)

interval = timedelta(days=1, hours=2, minutes=29)
future = now + interval
print(future)