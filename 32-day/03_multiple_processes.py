# 03_multiple_processes.py
# Running multiple processes

from multiprocessing import Process
import time

def worker(id):
    print(f"Process {id} started")
    time.sleep(1)
    print(f"Process {id} finished")

processes = []
for i in range(3):
    p = Process(target=worker, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()
