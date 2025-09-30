# Démo : Duck Typing en Python

# Pas besoin d'héritage commun : chaque classe définit simplement une méthode __len__

# Je sais que ces objets ont la méthode que je veux utiliser. 
# Peu importe leur type, je me fiche de ce qu'ils sont par ailleurs, je les manipule uniquement via cette méthode.

class Chanson:
    def __init__(self, paroles):
        self.paroles = paroles

    def __len__(self):
        return len(self.paroles.split())  # nb de mots


class Film:
    def __init__(self, minutes):
        self.minutes = minutes

    def __len__(self):
        return self.minutes  # durée en minutes


# --- Utilisation ---
# len() fonctionne sur des types différents, sans héritage ni vérification de type
c = Chanson("La vie en rose")
f = Film(120)

print("len(Chanson) :", len(c))  # applique __len__ de Chanson
print("len(Film)    :", len(f))  # applique __len__ de Film
print("len(str)     :", len("Python"))  # applique __len__ de str intégré
print("len(list)    :", len([1, 2, 3]))  # applique __len__ de list intégré
