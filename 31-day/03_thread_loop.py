# 03_thread_loop.py
# Thread running a loop

import threading
import time

def show_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(0.5)

t = threading.Thread(target=show_numbers)
t.start()
t.join()
