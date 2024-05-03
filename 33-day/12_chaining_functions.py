# 12_chaining_functions.py
# Function chaining with lambdas

add = lambda x: x + 5
mul = lambda x: x * 3
sub = lambda x: x - 2

def chain(x):
    return sub(mul(add(x)))

print("Chain result:", chain(10))
