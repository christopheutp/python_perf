class Chien:
    """ Représentation d'un chien """
    instance_chien = 0
    nom_latin = "Canis lupus familiaris"

    def __init__(self,nom,age,race):
        Chien.instance_chien += 1
        self.nom = nom
        self.age = age
        self.race = race

    def aboyer(self):
        print(f"Wouf Wouf {self.nom}")


print(f"Il y a {Chien.instance_chien} instances de chien dont le nom latin est {Chien.nom_latin}")
print("J'instancie 2 chiens !!!!")
chien_1 = Chien("REX", 12, "Berger Allemand")
chien_2 = Chien("Princesse", 4, "Labrador")

print(f"Il y a {Chien.instance_chien} instances de chien dont le nom latin est {Chien.nom_latin}")
Chien.instance_chien = 9
Chien.nom_latin = "Toutou"
print(f"Il y a {Chien.instance_chien} instances de chien dont le nom latin est {Chien.nom_latin}")