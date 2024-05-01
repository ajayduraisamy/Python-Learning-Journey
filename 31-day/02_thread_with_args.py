# 02_thread_with_args.py
# Thread function with arguments

import threading

def welcome(name):
    print(f"Welcome, {name}!")

t = threading.Thread(target=welcome, args=("Ajay",))
t.start()
t.join()
