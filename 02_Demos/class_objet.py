# Démo : héritage implicite d'object + dunder methods clés

# 1) TOUTES les classes héritent implicitement de 'object' (même si on ne l'écrit pas).
class A:
    pass

a = A()
print("A hérite d'object :", isinstance(a, object))  # True
# Sans __repr__/__str__, on récupère ceux d'object (représentation par défaut)
print("repr(A()) par défaut :", repr(a))  # ex: <__main__.A object at 0x...>
print("str(A())  par défaut :", str(a))   # idem (str délègue souvent à repr si non redéfini)


# 2) __repr__ vs __str__ :
# - __repr__ : représentation non ambiguë pour dev (debug, console, f"{obj!r}")
# - __str__  : représentation "humaine" (print, f"{obj}")
class User:
    def __init__(self, name: str):
        # __setattr__ sera appelé ici aussi -> penser à super().__setattr__
        self.name = name  # validation + effets dans __setattr__

    def __repr__(self):
        # Représentation détaillée pour le debug
        return f"User(name={self.name!r}, slug={getattr(self, 'slug', None)!r})"

    def __str__(self):
        # Représentation conviviale pour un humain
        return self.name

    # 3) __setattr__ : point de passage unique pour affecter les attributs
    #    - on peut valider, normaliser, créer des attributs dérivés...
    def __setattr__(self, key, value):
        if key == "name":
            if not isinstance(value, str):
                raise TypeError("name doit être une chaîne")
            # stocker l'attribut réel (éviter la récursion en appelant super)
            super().__setattr__("name", value)
            # effet dérivé : générer un slug à chaque changement de name
            super().__setattr__("slug", value.strip().lower().replace(" ", "-"))
        else:
            # pour tout le reste : comportement normal
            super().__setattr__(key, value)

    # 4) __getattr__ : appelé UNIQUEMENT si l'attribut n'existe pas déjà.
    #    On peut fournir des attributs "virtuels" calculés à la volée.
    def __getattr__(self, key):
        if key == "initials":
            parts = [p for p in self.name.strip().split() if p]
            return "".join(p[0].upper() for p in parts)
        # IMPORTANT : si on ne sait pas répondre, relancer une AttributeError
        raise AttributeError(f"{type(self).__name__!s} n'a pas d'attribut '{key}'")


# --- Démonstration ---
u = User("Toto Tata")
print("repr(u) :", repr(u))        # utilise __repr__
print("str(u)  :", str(u))         # utilise __str__
print("slug    :", u.slug)         # créé par __setattr__
print("initials:", u.initials)     # fourni par __getattr__ (virtuel)

# Changer le nom déclenche __setattr__ à nouveau (slug est régénéré)
u.name = "Bob Marley"
print("repr(u) après rename:", repr(u))
print("slug après rename   :", u.slug)

# __getattr__ lève AttributeError si l'attribut n'est pas géré
try:
    print(u.age)  # 'age' n'existe pas -> __getattr__ -> AttributeError
except AttributeError as e:
    print("AttributeError capturée :", e)

# Validation dans __setattr__ (TypeError si name n'est pas une str)
try:
    u.name = 123
except TypeError as e:
    print("TypeError capturée :", e)
