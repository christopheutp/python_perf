class Chien():
    def __init__(self, nom, age, race):
        self.nom = nom 
        self.age = age 
        self.race = race 
    
    def aboyer(self, texte):
        print(f"{self.nom} aboie la phrase : {texte}")
    
    # il s'agit de ce qu'on appelle une propriété, elle est relative à age ici
    # plus traditionnellement on utilisais la méthode __getattr__ dont la syntaxe est plus complexe
    @property
    def age_humain(self):
        return self.age * 7
    
    #pour définir un attribut avec une méthode particulière, on utilisera le principe de setter
    # plus traditionnellement on utilisais la méthode __setattr__ dont la syntaxe est plus complexe
    @age_humain.setter
    def age_humain(self, value):
        self.age = int(value / 7)


liste_chien = [
    Chien("Rex", 5, "Pit"),
    Chien("Princesse", 2, "Chihuahua") ,
    Chien("Speedy", 2, "Lévrier")
]


for i in range(1,4):
    liste_chien.append(Chien(f"Pif{i}", 0, "Labrador"))

for chien in liste_chien:
    print(chien.nom)
    chien.aboyer("ouaf")

age_double = liste_chien[0].age_humain # il a 5 ans donc *7 -> 35 ans en age humain
print(age_double)

liste_chien[0].age_humain = 30 # il a 30 ans en age humain /7 -> 4 ans
print(liste_chien[0].nom, liste_chien[0].age)

# une instance est mutable, exemple :
princesse = Chien("Princesse", 2, "Chihuahua")
princesse2 = princesse
print(princesse.nom, princesse2.nom)

princesse.nom = "Pepette"
print(princesse.nom, princesse2.nom)