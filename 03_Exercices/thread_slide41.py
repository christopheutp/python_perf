import random
import queue
import threading
import time

class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for x in range(10):
            number = random.randint(1,1000)
            self.queue.put(number)
            print(f"producteur {number}")
        self.queue.put(0)

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            number = self.queue.get()
            if number == 0:
                break
            print(f"Nombre consommé : {number}")
            self.queue.task_done()

def main():
    q = queue.Queue()
    prod = Producer(q)
    cons = Consumer(q)
    prod.start()
    #time.sleep(2)
    cons.start()
    prod.join()
    cons.join()

main()
