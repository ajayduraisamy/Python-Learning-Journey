# 01_basic_process.py
# Creating a simple process

from multiprocessing import Process

def hello():
    print("Hello from a new process!")

p = Process(target=hello)
p.start()
p.join()
