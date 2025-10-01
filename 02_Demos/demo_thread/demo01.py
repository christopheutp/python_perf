import time
import random
from threading import Thread

# ============================================================
# MÉTHODE 1 — Thread avec une fonction cible (target=...)
#  1) Créer un objet Thread en passant la fonction à exécuter via target
#     et ses arguments via args=(...,).
#  2) Démarrer le thread avec start().
# ============================================================
def print_vide():
    print("Bonjour !")

def print_avec_texte(texte):
    # Simule un petit travail pour visualiser l'exécution en parallèle
    time.sleep(random.random() * 0.5)
    print("Mon texte:", texte)

def demo_methode_1():
    print("\n=== Méthode 1 : Thread(target=fonction, args=...) ===")

    # Trois threads qui appellent une fonction sans argument
    threads = []
    for _ in range(3):
        t = Thread(target=print_vide)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # attendre la fin des 3 premiers threads

    # Trois threads qui appellent une fonction avec un argument
    threads = []
    for i in range(3):
        t = Thread(target=print_avec_texte, args=(i,))
        t.start()
        threads.append(t)

    print("coucou")

    for t in threads:
        t.join()  # attendre la fin des 3 suivants

    print("[M1] Terminé.")

# ============================================================
# MÉTHODE 2 — Sous-classe de Thread
#  1) Créer une classe qui hérite de Thread, surcharger run().
#  2) Instancier, puis démarrer avec start(), et attendre avec join().
# ============================================================
class MonThread(Thread):
    def __init__(self, texte):
        super().__init__()      # initialise la classe de base Thread
        self.texte = texte

    def run(self):
        # La logique exécutée DANS le thread
        for i in range(6):
            time.sleep(random.random() * 0.5) # petite pause pour illustrer l'entrelacement
            print(self.texte, i) 

def demo_methode_2():
    print("\n=== Méthode 2 : Sous-classe de Thread et run() ===")
    t1 = MonThread("hello")
    t2 = MonThread("bonjour")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("[M2] Terminé.")

# ============================================================
# MÉTHODE 3 — Thread avec méthode d'instance comme cible
#  1) Créer une classe qui implémente la logique métier.
#  2) Instancier la classe.
#  3) Créer un Thread avec target=obj.methode (méthode liée).
#  4) Démarrer et éventuellement join().
# ============================================================

class UnObjet:
    def __init__(self, texte):
        self.texte = texte

    def multi_print(self):
        for i in range(6):
            time.sleep(random.random() * 0.5) 
            print(self.texte, i)

def demo_methode_3():
    print("\n=== Méthode 3 : Thread(target=obj.methode) ===")
    obj1 = UnObjet("hello")
    obj2 = UnObjet("deux")

    t1 = Thread(target=obj1.multi_print)
    t2 = Thread(target=obj2.multi_print)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("[M3] Terminé.")


if __name__ == "__main__":
    #demo_methode_1()
    #demo_methode_2()
    demo_methode_3()