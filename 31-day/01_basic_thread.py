# 01_basic_thread.py
# Creating a simple thread

import threading

def greet():
    print("Hello from a thread!")

t = threading.Thread(target=greet)
t.start()
t.join()
