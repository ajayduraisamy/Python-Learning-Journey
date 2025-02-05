# Mutable vs Immutable Demo

# Immutable example
x = 5
y = x

y += 1

print("Immutable example:")
print("x =", x, "id:", id(x))
print("y =", y, "id:", id(y))

print("-" * 30)

# Mutable example
list_a = [1, 2, 3]
list_b = list_a

list_b.append(4)

print("Mutable example:")
print("list_a =", list_a, "id:", id(list_a))
print("list_b =", list_b, "id:", id(list_b))
