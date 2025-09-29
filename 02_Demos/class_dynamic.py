# Definition d'une fonction classique qui sera utilisee comme methode
# Elle attendra un parametre self 
def sensor_read(self):
    return f"{self.name}"

# Creation dynamique d'une classe avec "type"
# Syntaxe : type(nom_de_la_classe,classe_parents,dictionnaire_attributs)
DynamicSensor = type(
    "DynamicSensor", # nom de la classe
    (), # Pas de parents
    {"read": sensor_read} 
)

# Instanciation de la classe dynamique
ds = DynamicSensor()

# Ajout d'un attribut name
ds.name = "Mon jolie Capteur"

# Appel de la methone read
print(ds.read())

