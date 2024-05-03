# 16_closure_example.py
# Closure capturing variable

def make_multiplier(n):
    def inner(x):
        return x * n
    return inner

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 6:", double(6))
print("Triple 6:", triple(6))
