import threading, time, random

capacite = 2
bornes = threading.Semaphore(capacite)

def tache(nom):
    print(f"[{nom}] prêt à utiliser une borne")
    acquis = bornes.acquire(timeout=5)  # on peut aussi faire bornes.acquire() sans timeout : dans ce cas le thread attendra indefiniment qu'une ressource se libere
    if not acquis:
        print(f"[{nom}] abandon: attente trop longue")
        return
    print(f"[{nom}] a OBTENU une borne → travail...")
    time.sleep(random.uniform(0.5, 1.2))
    print(f"[{nom}] libère la borne")
    bornes.release()

threads = [threading.Thread(target=tache, args=(f"Worker-{i}",)) for i in range(1, 6)]
for t in threads: t.start()
for t in threads: t.join()
print("[SEMAPHORE] Toutes les tâches sont passées par les bornes (2 simultanées max).")