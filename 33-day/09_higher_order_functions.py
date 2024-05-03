# 09_higher_order_functions.py
# Higher-order functions (functions returning functions)

def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)
cube = power(3)

print("Square 5:", square(5))
print("Cube 5:", cube(5))
