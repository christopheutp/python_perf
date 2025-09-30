# Démo : Polymorphisme (override) et appel du parent avec super()

class Personne:
    def jouer(self):
        print("Personne joue calmement.")

class Enfant(Personne):
    # Override : on remplace la méthode du parent
    def jouer(self):
        print("Enfant joue bruyamment.")

class EnfantAvecSuper(Personne):
    # Variante : on réutilise la méthode du parent puis on ajoute un comportement
    def jouer(self):
        super().jouer()  # appel de Personne.jouer(self)
        print("... et l'enfant ajoute de l'énergie au jeu !")

# --- Utilisation polymorphique ---
# Chaque élément a une méthode jouer() adaptée à son type réel.
groupe = [Personne(), Enfant(), EnfantAvecSuper()]

for individu in groupe:
    # Appelle la version "appropriée" de jouer() selon la classe réelle de l'objet
    individu.jouer()
