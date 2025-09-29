class Chien:
    """ Représentation d'un chien """

    def __init__(self,nom,age,race):
        self.nom = nom
        self.age = age
        self.race = race

    def aboyer(self):
        print(f"Wouf Wouf {self.nom}")


chien_1 = Chien("REX", 12, "Berger Allemand")

chien_1.aboyer()

print(f"{chien_1} est il a {chien_1.age} ans")