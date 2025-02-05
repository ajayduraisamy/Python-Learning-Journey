# Python Memory Model Demo

a = 10
b = 10

print("a =", a, "id:", id(a))
print("b =", b, "id:", id(b))

print("a is b:", a is b)

# Reassignment creates a new object
a = 20
print("\nAfter reassignment:")
print("a =", a, "id:", id(a))
print("b =", b, "id:", id(b))
