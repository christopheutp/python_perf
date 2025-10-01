# Une fonction classique pour comparer
def carre(x):
    return x * x

print("Fonction classique :", carre(5))

# --- Fonctions anonymes (lambda) ---
# Syntaxe : lambda paramètres : expression

# Une fonction lambda simple (calcul du carré)
carre_lambda = lambda x: x * x
print("Lambda simple :", carre_lambda(5))

# Lambda avec plusieurs paramètres
addition = lambda a, b: a + b
print("Addition :", addition(3, 7))

# Lambda sans paramètre
bonjour = lambda: "Hello World"
print(bonjour())

# Lambda utilisée directement sans nom (inline)
resultat = (lambda x, y: x * y)(4, 5)
print("Lambda inline :", resultat)

# Exemple concret : utiliser lambda avec sorted
personnes = [
    {"nom": "Alice", "age": 30},
    {"nom": "Bob", "age": 25},
    {"nom": "Charlie", "age": 35},
]
# Tri des personnes par age croissant
personnes_triees = sorted(personnes, key=lambda p: p["age"])
print("\nTri par age :", personnes_triees)
