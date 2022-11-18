# une base de donnée relationnelle est une base de données (un ensemble de tables) avec
# des éventuelles relations entre les tables. 
# Les relations peuvent être de plusieurs types :
# - relation 1 à 1 (un objet de type A est associé à un seul objet de type B et inversement)
# par exemple : Cerveau est lié à un Crâne
# - relation 1 à plusieurs / plusieurs à 1 : par exemple un employé fait partie d'une
# entreprise, mais une entreprise peut avoir plusieurs employés
# - relation plusieurs à plusieurs : un utilisateur est lié à une liste de produit
# (la liste de produits dans son panier) mais un produit peut être dans le panier de
# plusieurs utilisateurs

# pour effectuer ses relations, mais aussi pour identifier chaque élément d'une
# table de manière, on utilise une clé primaire : un id (identifiant)
# pour les relations on peut aussi utiliser d'autres clés pour symboliser ces
# relations, cf cours de SQL

# Pour communiquer avec une base de données, on utilise le SQL (structured query language)
# Pourquoi structuré ? Toutes les lignes d'un table ont forcément les même colonnes
# (potentiellement None). 
# Quand on utilise une base de donnée creuse (avec beaucoup de None), ce n'est pas forcément
# le cas, et on peut utiliser des base de données non structurées et d'autres langages

# Objectif : savoir comment envoyer des requêtes SQL à une base de données en Python
# et comment recevoir des résultats
# Le but n'est pas d'apprendre le SQL ou la gestion de BDD

# Il existe plusieurs SGBD (système de gestion de base de données) mySql, SqlServer,
# postgreSql, ...
# On va utiliser SQLite. Sa particularité est de ne pas fonctionner en terme de client/serveur
# mais d'être intégré au programme. L'intégralité de la base de données (tables, données, ...)
# est stocké dans un fichier.

# Il existe une API unifiée, où les mêmes opérations se font avec les mêmes fonctions quelle
# que soit la base de donnée relationnelle SQL à laquelle on accède.

import sqlite3

# Pour SQLite, la méthode connect ne prend qu'un seul paramètre, le nom du fichier
# SQLite est une base données embarquée sans sécurité, on a pas besoin de mot de passe
# Si on souhaite se connecter à une autre base de données (pas forcément SQLite) la
# seule chose qui va changer c'est cette connexion

# Si la base existe, on se connecte. Sinon, on créé le fichier.
cnx = sqlite3.connect("26_bdd_create/database.sqlite3")

# un curseur, dans une base de données, représente un endroit où on se trouve dans la base,
# notamment lorsqu'on récupère des données
# c'est ce curseur qui sert à exécuter des requêtes SQL, et qu'on utilise pour parcourir
# les résultats, quand il y en a
curseur = cnx.cursor()

# ici, on créé une nouvelle table dans notre base de données
# """ en Python : pour la documentation mais aussi pour pouvoir faire des chaînes de
# caractères sur plusieurs lignes
sql = """
CREATE TABLE IF NOT EXISTS personne (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nom VARCHAR(30) NOT NULL,
  prenom VARCHAR(20) NOT NULL,
  age INTEGER UNSIGNED NOT NULL,
  CONSTRAINT unique_names UNIQUE (nom,prenom)
)
"""

# INTEGER : int, entier
# PRIMARY KEY : clé primaire
# AUTOINCREMENT : la base qui s'occupe de générer l'id au fur et à mesure qu'on ajoute
# des données dans la base
# sinon, on devrait manuellement s'assurer que l'id n'existe pas déjà dans la table
# NOT NULL : équivalent de NOT NONE
# VARCHAR : une chaine de caractères
# UNSIGNED : nombre positif
# CONSTRAINT unique_names UNIQUE (nom,prenom) : contrainte sur la table
# qu'on appelle unique_names : pas d'homonyme

curseur.execute(sql)

# SQLite browser
# https://sqlitebrowser.org/

# on va ajouter des données à la base

# Concept de transaction :
# Problème : exemple d'une appli de banque
# Je veux vous faire un virement. 2 requêtes sont faites :
# 1) la première pour me retirer la somme sur mon compte
# 2) la seconde pour vous donner la somme sur le votre
# Qu'est ce qu'il se passe si un problème se produit entre les deux requêtes ?
# L'argent serait retiré de mon compte, mais vous ne recevrez rien
# une transaction : un ensemble d'instructions envoyé à une base de données
# qui ne sera réellement effectués que si aucune erreur ne se produit, et tous les
# changements seront appliqués en même temps
# si il y a un problème : on fait un rollback de transaction (retour en arrière : tout
# est annulé)
# si tout se passe bien : on fait un commit de transaction (on applique réellement toutes
# les modifications)

# avec sqlite3, on a pas besoin d'explicitement démarrer une transaction
# par contre il faut soit commit, soit rollback

try:
  # requête SQL pour insérer des données :
  # sql = "INSERT INTO personne (nom, prenom, age) VALUES ('Doe','John',56)"
  # ne jamais faire d'envoi de données comme ça
  # problème de sécurité potentiel : injection SQL
  # encore pire : 
  # sql = f"INSERT INTO personne (nom, prenom, age) VALUES ('{nom}', '{prenom}', {age})"
  # à proscrire, pour des raisons de sécurité, ne jamais faire les choses comme ça

  # imaginons qu'on demande à l'utilisateur son nom, son prenom, son age
  # nom = input("...")
  # prenom = input("...")
  # age = int(input("..."))
  # et qu'on fasse la requête :
  # sql = f"INSERT INTO personne (nom, prenom, age) VALUES ('{nom}', '{prenom}', {age})"

  # un utilisateur malveillant pourrait renseigner les informations suivantes :
  # nom : X','bidule',20) DELETE FROM personne INSERT INTO personne (nom, prenom, age) VALUES ('Philippe 
  # prenom : hahaha
  # age : 34

  # la requête envoyée à la base sera : 
  # INSERT INTO personne (nom, prenom, age) VALUES ('X','bidule',20) 
  # DELETE FROM personne 
  # INSERT INTO personne (nom, prenom, age) VALUES ('Philippe', 'hahaha', 34)

  # autre exemple plus pratique :
  # https://www.youtube.com/watch?v=ciNHn38EyRc

  # mécanisme protégé contre les injections : 
  sql = "INSERT INTO personne (nom, prenom, age) VALUES (?,?,?)"
  data = ("Dupont","Marjorie",29)
  curseur.execute(sql, data)

  cnx.commit()
except sqlite3.IntegrityError:
  # Si on essaye d'ajouter la même personne (ou un homonyme) :
  # sqlite3.IntegrityError: UNIQUE constraint failed: personne.nom, personne.prenom
  cnx.rollback()

# une connection est une ressource qu'il faut fermer pour éviter les fuites mémoire
# comme pour les fichiers, on peut utiliser le Context Manager
cnx.close()

# En pratique, on utilise souvent des ORM (object realtion mapping) comme Pewee,
# SqlAlchemy, ... qui permettent de faire le pont entre le modèle objet (les classes)
# et la base de données (les tables)

# par exemple : en partant d'une base de données, générer le code des classes
# ou en partant du code des classes, générer la base de données

# Avantages :
# - lier le code et la base de données : centralise le modèle objet
# - d'autres langages de requêtes sont utilisés, qui permettent de profiter de la structure
# des objets.
# Quand on a des relations entre les tables, les requêtes qui utilisent ces relations peuvent
# être plus complexes à écrire (des jointures)
# on pourra faire des choses du types :
# request.table(Personne).insert(Personne('truc','bidule',95))

# Inconvénients : 
# - le SQL pur est meilleur en terme de performance : en définitive, les ORMs communiquent
# en SQL avec la base
# - certaines fonctionnalités SQL ne sont parfois pas implémentés dans les autres
# langages de requêtes propres aux ORMs