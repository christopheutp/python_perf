# Démo : conventions de visibilité en Python + name mangling

class Compte:
    def __init__(self, solde_initial: int):
        self.solde = solde_initial      # public : accessible partout
        self._token = "tok_123"         # protégé (convention) : usage interne / sous-classes
        self.__secret = "clé-maître"    # privé (name mangling) : devient _Compte__secret

    # Méthodes avec les mêmes conventions
    def deposer(self, montant: int):    # public
        self.solde += montant

    def _audit(self):                   # protégé (convention)
        print("[AUDIT] solde:", self.solde, "| token:", self._token)

    def __reset_secret(self):           # privé (manglé en _Compte__reset_secret)
        self.__secret = "clé-maître-reset"

c = Compte(100)

# --- Accès public : OK
print("solde public :", c.solde)               # OK

# --- Accès 'protégé' : techniquement accessible, mais déconseillé hors classe/sous-classe
print("token protégé (_token) :", c._token)    # OK (convention de ne pas l'utiliser directement)

# --- Accès 'privé' (double underscore) : l'attribut est renommé par name mangling
#print(c.__secret)  # Provoquerait un AttributeError, car __secret est manglé

# Accès explicite via le nom manglé (possible mais déconseillé) :
print("secret via name mangling :", c._Compte__secret)

# On peut constater le nom réel via dir() (on y verra _Compte__secret)
print("Nom manglé présent ?", any(name.startswith("_Compte__secret") for name in dir(c)))

# Idem pour la méthode 'privée' :
c._Compte__reset_secret()                      # appel via le nom manglé
print("secret après reset :", c._Compte__secret)

# Méthode protégée : accessible techniquement
c._audit()

# Récap rapide (affichages pédagogiques) :
print("\nRÈGLES :")
print("- Public     : nom = 'nom'       -> libre d'accès.")
print("- Protégé    : nom = '_nom'      -> convention : usage interne/sous-classes.")
print("- Privé      : nom = '__nom'     -> manglé en '_NomDeClasse__nom'.")