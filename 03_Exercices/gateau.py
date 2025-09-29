import inspect

class Gateau:
    """Ma Jolie classe Gateau"""

    def __init__(self,nom_gateau: str,temp_cuisson: int,ingredients: list[str],etapes: list[str],createur: str):
        self.nom_gateau = nom_gateau
        self.temps_cuisson = temp_cuisson
        self.ingredients = ingredients
        self.etapes = etapes
        self.createur = createur

    def afficher_ingredients(self):
        print(f"Ingredients de mon gateau : {self.nom_gateau}")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def afficher_etapes(self):
        """Ma methode qui affiche les etapes pour faire mon gateau"""
        print(f"Etapes de mon gateau : {self.nom_gateau}")
        for etape in self.etapes:
            print(f"- {etape}")


# Instanciation du gateau
gateau1 = Gateau("tarte au citron",30,["citron","farine","sucre"],["couper citron","faire le reste"],"toto")
gateau2 = Gateau(
    createur="tata",
    ingredients=["poires","farine","sucre"],
    nom_gateau="tarte au poires",
    temp_cuisson=30,
    etapes=["couper poires","faire le reste"]
    )

# gateau1.afficher_ingredients()
# gateau1.afficher_etapes()
# gateau2.afficher_ingredients()
# gateau2.afficher_etapes()


# help(Gateau)
# print(Gateau.__doc__)
# print(Gateau.afficher_etapes.__doc__)

print(inspect.getdoc(Gateau.afficher_etapes))