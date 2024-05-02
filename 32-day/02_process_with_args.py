# 02_process_with_args.py
# Process with arguments

from multiprocessing import Process

def greet(name):
    print(f"Welcome, {name}!")

p = Process(target=greet, args=("Ajay",))
p.start()
p.join()
