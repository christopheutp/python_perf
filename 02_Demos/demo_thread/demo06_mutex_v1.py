import threading, time, random

solde = 0
verrou = threading.Lock()  # Mutex

def operation(nom, montant):
    global solde
    print(f"[{nom}] DEMARRAGE opération de {'dépôt' if montant>=0 else 'retrait'}: {montant:+}")
    time.sleep(random.uniform(0.05, 0.2))

    # === Partie critique avec acquire() / release() explicites ===
    verrou.acquire()  # prise du verrou
    try:
        avant = solde
        time.sleep(random.uniform(0.05, 0.2))  # simule un calcul ou accès disque
        solde_local = avant + montant
        solde = solde_local
        print(f"[{nom}] EN COURS: avant={avant}, après={solde}")
    finally:
        verrou.release() # libération du verrou, même en cas d’erreur

    print(f"[{nom}] FIN opération")

threads = []
mouvements = [+50, -20, +10, +40, -30, +25, -15, +5, -10, +60]
for i, m in enumerate(mouvements, start=1):
    t = threading.Thread(target=operation, args=(f"T{i}", m))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"[MUTEX ACQUIRE/RELEASE] Solde final attendu={sum(mouvements)}, obtenu={solde}")
