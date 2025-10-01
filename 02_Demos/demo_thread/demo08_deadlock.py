import threading, time

lock_A = threading.Lock()
lock_B = threading.Lock()

def t1():
    print("[T1] acquire(lock_A)")
    lock_A.acquire()
    print("[T1] lock_A acquis")
    time.sleep(0.1)  # laisse T2 prendre lock_B
    print("[T1] tente acquire(lock_B) → deadlock attendu...")
    lock_B.acquire()  # ← ne reviendra jamais (T2 tient lock_B et attend lock_A)
    print("[T1] lock_B acquis (n'arrivera pas)")
    lock_B.release()
    lock_A.release()

def t2():
    print("[T2] acquire(lock_B)")
    lock_B.acquire()
    print("[T2] lock_B acquis")
    time.sleep(0.1)  # laisse T1 prendre lock_A
    print("[T2] tente acquire(lock_A) → deadlock attendu...")
    lock_A.acquire()  # ← ne reviendra jamais (T1 tient lock_A et attend lock_B)
    print("[T2] lock_A acquis (n'arrivera pas)")
    lock_A.release()
    lock_B.release()

a = threading.Thread(target=t1, name="T1")
b = threading.Thread(target=t2, name="T2")
a.start(); b.start()

# Ces join ne serviront jamais à cause du blocage circulaire
a.join(); b.join()
