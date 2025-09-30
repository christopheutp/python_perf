# Rappel
# en Python, l’indentation définit les blocs de code (pas d’accolades)

# 1. Variables et affichage
name = "Alice"
age = 30
print(f"Bonjour {name}, tu as {age} ans.")

# 2. Types et conversions
# Python est dynamiquement typés, mais conversions possibles int("5")
num_str = "42"
num = int(num_str)
print(num + 8)  # 50

# 3. Conditions et boucles
if age > 18:
    print("Adulte")
else:
    print("Mineur")

for i in range(3):
    print("Compteur:", i)

# 4. Listes et slicing / mutables, supportent slicing mylist[1:3]
# Tuples : immuables.
fruits = ["pomme", "banane", "cerise"]
print(fruits[0], fruits[1:])
fruits.append("orange")
print(fruits)

# 5. Dictionnaires : paires clé-valeur.
person = {"nom": "Bob", "ville": "Paris"}
print(person["nom"])
person["age"] = 25
for k, v in person.items():
    print(k, ":", v)

# 6. Fonctions : def, paramètres, return, valeurs par défaut
def carre(x):
    return x * x

print("Carré de 5 =", carre(5))