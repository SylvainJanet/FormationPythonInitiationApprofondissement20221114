import logging # attention, ne pas appeler ce fichier logging.py
# sinon risque d'import circulaire
import sys

# logging : conserver un journal, des traces du fonctionnement de l'application
# peut servir à plusieurs niveaux :
# - lors du développement, être au courant de l'évolution des fonctionnalités
# qu'on est en train de mettre en place
# - en cas d'erreur, en cas de problème, peut aider à trouver la source du problème

# on peut logger plusieurs niveaux d'informations
# - informations de "debug" : c'est pour le développement
# - informations générales non problématiques "info" : pour indiquer une action
# - informations pour des erreurs :
#     "warning" : problèmes mineurs
#     "error" : pour indiquer un problème
#     "critical" : pour indiquer un problème critique (arrêt de l'application)

# logging.basicConfig(level = logging.DEBUG)
logging.basicConfig(
  level = logging.INFO,
  format = "%(asctime)s - [%(levelname)s]: %(message)s",
  # https://docs.python.org/3/library/logging.html#logrecord-attributes
  datefmt = "%d/%m/%Y - %H:%M",
  # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
  filename = "21_logging/app.log",
  filemode = "w", # mode d'écriture
  # a pour append (par défaut) : écrit à la suite du fichier
  # w pour write : écrase le fichier à chaque fois
  encoding = "utf-8",
)

logging.debug("Ceci est mon message - debug")
logging.info("Ceci est mon message - info")
logging.warning("Ceci est mon message - warning")
logging.error("Ceci est mon message - error")
logging.critical("Ceci est mon message - critical")

# pour configurer le logger c.f l.18, il faut le faire avant de l'utiliser
# si on essaye de modifier sa configuration après l'avoir utilisé, rien
# ne sera pris en compte. De plus, la configuration ne peut être faite qu'une
# seule fois
# voir un loggeur comme une machine qui permet d'écrire des log
# voir logging comme une usine qui fabrique des machines
# à partir du moment où on utilise le logger, ou qu'on essaye de le paramétrer,
# il créé une machine et elle devient sa machine modèle : le logger root

print("_____")

def addition(x,y):
  logging.info("Appel de la fonction addition")
  return x + y

resultat = addition(3,8)
print(resultat)

# on peut créer d'autres loggeurs avec la méthode getLogger(...)
# elle permet d'en créer, mais aussi de récupérer un loggeur particulier
# getLogger() -> récupère le loggeur root
# la configuration de base de ces loggers sera la config du loggeur root
mon_loggeur = logging.getLogger("logger_console")
mon_loggeur.setLevel(logging.WARNING)

# on a des handlers qui sont responsables de gérer l'affichage d'un message
handler_console = logging.StreamHandler(sys.stdout)
mon_loggeur.addHandler(handler_console)

mon_loggeur.debug("Ceci est mon message de mon_loggeur - debug")
mon_loggeur.info("Ceci est mon message de mon_loggeur - info")
mon_loggeur.warning("Ceci est mon message de mon_loggeur - warning")
mon_loggeur.error("Ceci est mon message de mon_loggeur - error")
mon_loggeur.critical("Ceci est mon message de mon_loggeur - critical")