# 04_suppress_exceptions.py
# contextlib.suppress example

from contextlib import suppress

# suppress ZeroDivisionError
with suppress(ZeroDivisionError):
    print(10 / 0)

print("No crash!")
