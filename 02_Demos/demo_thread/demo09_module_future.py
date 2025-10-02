from concurrent.futures import ThreadPoolExecutor
import time

# Fonction excuter a chaque thread
def task(num):
    print(f"Tache {num} demaree")
    time.sleep(2)
    print(f"Tache {num} fini")
    return f"Resultat de la tache {num} : {num*2}"


def main():
    # Creation du pool de 3 threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Soumission de 5 taches
        futures = [executor.submit(task,i) for i in range(5)]

        # On attend un peu pour voir l'etat des taches
        time.sleep(1)
        print("Etat des taches apres 1 secondes")
        for future in futures:
            print(f"terminé ? {future.done()} En cours ? {future.running()}")

        # Recuperation des resultats
        print("Recuperation des resultats :")
        for future in futures:
            result = future.result() # Bloque jusqu'a ce que la tache soit finie
            print(result)

if __name__ == "__main__":
    main()