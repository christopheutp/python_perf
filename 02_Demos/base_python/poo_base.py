# POO en Python :
# Classe et instance : une classe décrit le comportement, une instance est un objet concret.
# Encapsulation : cacher certains attributs via un underscore (_attribut) ou propriété.
# Héritage : réutiliser du code d’une classe parent (class B(A):).
# Polymorphisme : utiliser un même nom de méthode pour des comportements différents selon la classe.

# data_record.py
class DataRecord:
    def __init__(self, source, value): # constructeur
        self._source = source        # attribut "protégé" (convention)
        self.value = value           # attribut public

    def display(self):
        print(f"{self._source}: {self.value}")

# Héritage simple
class TemperatureRecord(DataRecord):
    def display(self):
        # Polymorphisme : redéfinition de la méthode
        print(f"Température ({self._source}) -> {self.value} °C")

record = DataRecord("capteur générique", 42)
record.display()

temp = TemperatureRecord("sonde T1", 23.5)
temp.display()