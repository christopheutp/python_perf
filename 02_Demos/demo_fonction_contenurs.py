from functools import reduce

# Données de base
nombres = [7, 2, 5, 2, 9, 1, 4]
personnes = [
    {"nom": "Toto", "age": 30},
    {"nom": "Tata", "age": 25},
    {"nom": "Tutu", "age": 35},
    {"nom": "Titi", "age": 25},
    {"nom": "Bob", "age": 13},
    {"nom": "Lea", "age": 13},
]

print("=== sorted ===")
# 1) Tri simple croissant
print(sorted(nombres))  # [1, 2, 2, 4, 5, 7, 9]

# 2) Tri décroissant
print(sorted(nombres, reverse=True))  # [9, 7, 5, 4, 2, 2, 1]

# 3) Tri d'objets par clé
par_age = sorted(personnes, key=lambda p: p["age"])
print(par_age)  # tri par age croissant

# 4) Tri multi-clés: par age puis par nom
par_age_nom = sorted(personnes, key=lambda p: (p["age"], p["nom"]))
print(par_age_nom)

print("\n=== filter ===")
# 1) Garder uniquement les nombres pairs
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(pairs)  # [2, 2, 4]

# 2) Filtrer les personnes de 30 ans et plus
trente_plus = list(filter(lambda p: p["age"]>= 30, personnes))
print(trente_plus)

print("\n=== map ===")
# 1) Appliquer une transformation: carré des nombres
carres = list(map(lambda x: x * x, nombres))
print(carres)

# 2) Mapper des objets: extraire les noms
noms = list(map(lambda p: p["nom"], personnes))
print(noms)  

# 3) Transformation structurée: ajouter une clé "est_majeur"
personnes_maj = list(map(lambda p: {**p, "est_majeur": p["age"] >= 18}, personnes))
print(personnes_maj)

print("\n=== reduce ===")
# 1) Réduire à une somme
somme = reduce(lambda acc, x: acc + x, nombres, 0)
print(somme)

# 2) Réduire à un produit (attention: point de départ 1)
produit = reduce(lambda acc, x: acc * x, nombres, 1)
print(produit)

# 3) Réduire une liste d'objets: compter les âges
compte_ages = reduce(
    lambda acc, p: {**acc, p["age"]: acc.get(p["age"], 0) + 1},
    personnes,
    {}
)
print(compte_ages)  # exemple: {30: 1, 25: 2, 35: 1}

# Remarques:
# - sorted() retourne une nouvelle liste triée (ne modifie pas la liste d'origine).
# - filter() et map() renvoient des itérateurs: utilisez list(...) pour matérialiser.
# - reduce() agrège une séquence en une valeur unique via une fonction binaire et un accumulateur initial.
