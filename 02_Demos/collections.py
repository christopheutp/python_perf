# =========================
# LISTE [ ... ]  (mutable)
# - Indexée de 0 à n-1
# - Accès: l[i]
# - Méthodes: sort(), append(x), extend(lst), pop(i), remove(x), count(x), index(x)
# - Mot-clé del pour supprimer par index ou tranche
# =========================
print("=== LIST ===")
l = [5, 2, 2, 9, 1]
print("Départ       :", l)

# append: ajoute un élément en fin
l.append(7)
print("append(7)    :", l)

# extend: concatène une autre séquence
l.extend([3, 3])
print("extend([3,3]):", l)

# count: nombre d'occurrences d'une valeur
print("count(2)     :", l.count(2))

# index: première position d'une valeur
print("index(9)     :", l.index(9))

# sort: trie sur place (in-place), retourne None
l.sort()
print("sort()       :", l)

# pop(i): retire et renvoie l'élément à l'index donné (dernier si i omis)
x = l.pop(0)
print("pop(0) ->", x, "reste:", l)

# remove(x): retire la première occurrence de x (ValueError si absent)
l.remove(3)
print("remove(3)    :", l)

# del: suppression par index ou tranche
del l[1:3]  # supprime les éléments aux index 1 et 2
print("del l[1:3]   :", l)
print()


# =========================
# TUPLE ( ... , ... )  (immutable)
# - Groupement de valeurs (packing)
# - Décomposition (unpacking)
# - Accès par index comme une liste, mais non modifiable
# =========================
print("=== TUPLE ===")
# Packing
t = (10, 20, 30)
print("tuple        :", t, "t[1] =", t[1])

# Unpacking
a, b = (1, 2)
print("unpacking    :", "a =", a, "b =", b)

# Unpacking avancé: étoile pour récupérer le reste
x, *milieu, y = (1, 2, 3, 4, 5)
print("x, *milieu, y:", x, milieu, y)

# t[0] = 99  # Exemple d'immuabilité: ceci lèverait une erreur si décommenté
print()

# =========================
# SET { ... }  (mutable, éléments uniques, non ordonné)
# - Éléments hashables, pas de doublons
# - Méthodes: add(x), update(itérable), remove(x), discard(x),
#             isdisjoint(s), issubset(s2), issuperset(s2)
# - Opérateurs: union(|), intersection(&), différence(-), diff sym (^)
# =========================

print("=== SET ===")
s = {1, 2, 2, 3}  # les doublons disparaissent automatiquement
print("départ       :", s)  # {1, 2, 3}

s.add(4)  # ajoute un élément
print("add(4)       :", s)  # {1, 2, 3, 4}

s.update([3, 5, 6])  # ajoute plusieurs éléments
print("update([...]):", s)  # {1, 2, 3, 4, 5, 6}

# remove(x): supprime x (erreur si absent)
s.remove(5)
print("remove(5)    :", s)  # {1, 2, 3, 4, 6}

# discard(x): supprime x si présent, sinon ne fait rien
s.discard(999)  # aucun effet
print("discard(999) :", s)

# -----------------------
# Relations d’ensemble
# -----------------------
a = {1, 2}
b = {1, 2, 3}
c = {7, 8}

print("\nRelations densemble :")
print("a.issubset(b)    ->", a.issubset(b),
      " # True si tous les éléments de a sont dans b")
print("b.issuperset(a)  ->", b.issuperset(a),
      " # True si b contient tous les éléments de a")
print("a.isdisjoint(c)  ->", a.isdisjoint(c),
      " # True si a et c nont aucun élément commun")

# -----------------------
# Opérations ensemblistes
# -----------------------
print("\nOpérations ensemblistes :")
print("a | b (union)        ->", a | b,
      " # tous les éléments de a et b sans doublons")
print("a & b (intersection)->", a & b,
      " # éléments présents dans a ET dans b")
print("b - a (différence)  ->", b - a,
      " # éléments de b qui ne sont PAS dans a")
print("a ^ b (différence sym.) ->", a ^ b,
      " # éléments dans a OU b mais pas dans les deux")



# =========================
# DICT { clé: valeur, ... }  (mutable)
# - Couples clé/valeur, clés uniques et immuables
# - Itération sur .keys(), .values(), .items() (ou directement sur les clés)
# =========================
print("=== DICT ===")
d = {"nom": "Alice", "age": 30}
print("départ       :", d)

# Accès et modification
d["ville"] = "Paris"        # ajout
d["age"] = d["age"] + 1     # modification
print("après set     :", d)

# Récupérer avec défaut si absent
print("get('pays','N/A'):", d.get("pays", "N/A"))

# Suppression clé
val = d.pop("ville")        # renvoie la valeur retirée
print("pop('ville')->", val, "reste:", d)

# Itérations
print("clés          :", list(d.keys()))
print("valeurs       :", list(d.values()))
print("items         :", list(d.items()))

# Itération pratique
for k in d:  # équivaut à d.keys()
    print(f"{k} -> {d[k]}")

# Mise à jour depuis un autre dict
d.update({"profession": "Dev", "age": 35})
print("update(...)   :", d)

# Suppression via del
del d["profession"]
print("del d['profession']:", d)
