import threading, time

# Paramètres pour provoquer la course tout en gardant une exécution rapide
N = 8              # nombre de threads
K = 1_000          # incréments par thread
S = 0.00001        # petite pause pour laisser le CPU changer de thread
ATTENDU = N * K    # valeur attendue si tout s'incrémente correctement

def run(locking: bool):
    compteur = [0]                 # compteur partagé (liste pour être mutable)
    lock = threading.Lock()        # mutex pour protéger la section critique
    start = threading.Barrier(N)   # barrière : tous les threads démarrent ensemble

    def incr():
        # Attendre que tous les threads soient prêts pour créer une vraie concurrence
        start.wait()
        for _ in range(K):
            if locking:
                # SECTION CRITIQUE PROTÉGÉE
                with lock:         # on prend le verrou (mutex)
                    v = compteur[0]      # lecture
                    time.sleep(S)        # simule un travail et laisse un autre thread passer
                    compteur[0] = v + 1  # écriture protégée
            else:
                # SECTION NON PROTÉGÉE (risque de course)
                v = compteur[0]
                time.sleep(S)
                compteur[0] = v + 1

    # Création et lancement des threads
    ts = [threading.Thread(target=incr) for _ in range(N)]
    for t in ts: t.start()
    for t in ts: t.join()

    return compteur[0]

# Test sans lock : résultats généralement faux
print("=== SANS LOCK ===")
print("Obtenu :", run(False), "| Attendu :", ATTENDU)

# Test avec lock : résultats corrects
print("\n=== AVEC LOCK ===")
print("Obtenu :", run(True),  "| Attendu :", ATTENDU)
