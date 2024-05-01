# 05_thread_exercises.py
# Practice tasks with threading

import threading
import time

# 1. Print even numbers in thread
def print_even():
    for i in range(0, 11, 2):
        print("Even:", i)
        time.sleep(0.3)

# 2. Print odd numbers in thread
def print_odd():
    for i in range(1, 11, 2):
        print("Odd:", i)
        time.sleep(0.3)

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

t1.start()
t2.start()

t1.join()
t2.join()
