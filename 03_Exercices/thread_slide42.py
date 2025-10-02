from threading import Thread
import queue
import time
import random

class JobWorker(Thread):
    def __init__(self, job_queue: queue.Queue,index: int):
        super().__init__(name=f"Worker-{index}")
        self.job_queue = job_queue
        self.index = index

    def run(self):
        # Boucle jusqu'a ce que la file soit vide
        while True:
            try:
                # Essaye de recuperer un job dans les 3 secondes
                # chaque job est un entier entre  0 et 5 : nombre de secondes "travaille"
                job_duration = self.job_queue.get(timeout=3)

                # log de debut de job
                print(
                    f"{self.name} -> Debut du job : dodo {job_duration}s"
                    f" job restant Avant prise : {self.job_queue.qsize()}"
                )

                # simule le travail
                time.sleep(job_duration)

                # log de fin de job
                print(
                    f"{self.name} -> Fin du job : a dormi {job_duration}s"
                    f" job restant Apres fin : {self.job_queue.qsize()}"
                )

                # Indique a la queue que ce job est fait
                self.job_queue.task_done()
            
            except queue.Empty:
                # Plus de job disponible depuis 3s : on arrete
                print(f"{self.name} aucun job trouvé (timeout) arret du thread")
                break


def main():
    # creation de la file d'attente (file de job)
    job_queue = queue.Queue()

    # genrerer 20 jobs chacun vaut un entier 0 et 5 inclus
    jobs = [random.randint(0,5) for _ in range(20)]
    print(f"MAIN jobs generer dureer en seconde : {jobs}")

    # Alimenter la file
    for job in jobs:
        job_queue.put(job)
    print(f"MAIN {len(jobs)} jobs placee dans la file ")

    # Creer N=5 threads travaileurs
    workers = [JobWorker(job_queue,i) for i in range(5)]

    # Demarre les threads
    print("MAIN demarrage des 5 workers")
    for worker in workers:
        worker.start()

    # Attendre la fin des threads
    for worker in workers:
        worker.join()

    print("MAIN tous les workers on fini. Fin du programme")

if __name__ == "__main__":
    main()