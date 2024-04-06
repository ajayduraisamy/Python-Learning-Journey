# 02_tuple_access_set_ops.py
# Tuple access + Set operations

colors = ("red", "blue", "green", "yellow")
print("Tuple first:", colors[0])
print("Tuple slice:", colors[1:3])

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
