from threading import Thread
from time import sleep
import threading

class MyThread:
    def prepare_tea(self):
        self.task1()
        self.task2()
        self.task3()
        self.task4()

    def task1(self):
        print(f"[{threading.current_thread().name}] Début : faire bouillir l'eau")
        sleep(5)
        print(f"[{threading.current_thread().name}] Fin   : faire bouillir l'eau")

    def task2(self):
        print(f"[{threading.current_thread().name}] Début : ajouter le thé et laisser 3 min")
        sleep(3)
        print(f"[{threading.current_thread().name}] Fin   : ajouter le thé")

    def task3(self):
        print(f"[{threading.current_thread().name}] Début : ajouter le sucre et laisser 2 min")
        sleep(3)
        print(f"[{threading.current_thread().name}] Fin   : ajouter le sucre")

    def task4(self):
        print(f"[{threading.current_thread().name}] Début : filtrer et servir")
        sleep(3)
        print(f"[{threading.current_thread().name}] Fin   : filtrer et servir")

obj = MyThread()
#t = Thread(target=obj.prepare_tea, name="TeaThread")
t = Thread(target=obj.prepare_tea)
t.start()

# thread principal en parallèle
for i in range(10):
    print(f"[{threading.current_thread().name}] Je peux faire autre chose pendant ce temps… {i}")
    sleep(1)
