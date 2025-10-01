def presentation(nom, age, *args, **kwargs):
    """
    nom (str)       : nom de la personne
    age (int)       : age de la personne
    *args           : arguments positionnels supplémentaires (non nommes)
    **kwargs        : arguments nommés supplémentaires (sous forme cle=valeur)
    """
    print(f"Nom : {nom}")
    print(f"Âge : {age}")

    # args est un tuple contenant les arguments positionnels supplementaires
    if args:
        print("\nAutres informations (args) :")
        for i, valeur in enumerate(args, start=1):
            print(f"  - info {i} : {valeur}")

    # kwargs est un dictionnaire contenant les arguments nommes supplementaires
    if kwargs:
        print("\nDétails supplementaires (kwargs) :")
        for cle, valeur in kwargs.items():
            print(f"  - {cle} : {valeur}")


# Exemple d'appel
presentation(
    "Tata", 
    30,
    "Developpeuse", "Passionnee de Python",  # -> args
    ville="Lille", hobby="Lecture", github="alice-dev"  # -> kwargs
)
print()
presentation("Toto",45)