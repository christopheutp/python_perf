class Canid:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("La canidé fait du bruit !")


# Si l'on voit que l'on a des attributs / méthodes en commun entre plusieurs classes,
# il n'y a pas besoin de les réécrire, il suffit d'hériter de la classe pour les récupérer automatiquement
class Chien(Canid):
    # Si aucun constructeur dans chien, on aura le constructeur de la classe mère
    
    # Si je définit un constructeur, il remplacera celui de la classe mère
    # On pourra ajouter des attributs et des instructions suplémentaires
    def __init__(self, name, age, race):
        super().__init__(name, age) # on appelle le constructructeur du parent avec ses paramètres
        self.race = race

    # ici, on remplace le make_sound() du parent, on appelle ça la surcharge (override)
    def make_sound(self):
        # super().make_sound() # cette ligne reproduit le comportement du parent
        print("Le chien fait 'OUAF!'")



if __name__ == "__main__":
    canide1 = Canid("Ed", 10)
    chien1 = Chien("Pepette", 2, "Doberman") # ne pas oublier le paramètre de constructeur race qu'on a ajouté

    print(canide1.age)
    # print(canide1.race) # ne fonctionne pas car les canidés n'on pas d'attribut race 
    print(type(canide1))
    print(chien1.age)
    print(chien1.race)
    print(type(chien1))

    canide1.make_sound()
    chien1.make_sound()

    print("-"*80)

    liste_canid = [
        canide1,
        chien1,
        Chien("Princesse", 2, "Chiwawa")
    ]

    for canid in liste_canid:
        canid.make_sound()