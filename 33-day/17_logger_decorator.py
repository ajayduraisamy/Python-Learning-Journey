# 17_logger_decorator.py
# Decorator that logs function name & time

import time

def profiler(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Running {func.__name__}...")
        result = func(*args, **kwargs)
        print("Time:", time.time() - start)
        return result
    return wrapper

@profiler
def slow_task():
    time.sleep(0.3)
    print("Task complete!")

slow_task()
