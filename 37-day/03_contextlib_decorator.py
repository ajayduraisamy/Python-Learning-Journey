# 03_contextlib_decorator.py
# Using contextlib.contextmanager

from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

with open_file("demo.txt", "w") as f:
    f.write("Written via contextlib!")
