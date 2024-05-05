# 04_product.py
# Cartesian product (product)

from itertools import product

a = [1, 2]
b = ["x", "y"]
prod = list(product(a, b))
print("Product a x b:", prod)

# product with repeat (like nested loops)
print("Product with repeat=2:", list(product([0,1], repeat=2)))
