# 04_generator_expression.py
# Generator expression example

gen = (x * x for x in range(5))

for v in gen:
    print(v)
