# 09_coroutine_style.py
# Coroutine-style generator (send values)

def accumulator():
    total = 0
    while True:
        x = yield total
        total += x

gen = accumulator()
next(gen)  # prime generator
print(gen.send(10))
print(gen.send(5))
print(gen.send(20))
