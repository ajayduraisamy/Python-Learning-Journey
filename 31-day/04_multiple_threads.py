# 04_multiple_threads.py
# Running multiple threads

import threading
import time

def worker(id):
    print(f"Thread {id} started")
    time.sleep(1)
    print(f"Thread {id} done")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
