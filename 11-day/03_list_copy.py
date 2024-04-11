# 03_list_copy.py
# Copy vs assignment

a = [1, 2, 3]
b = a          # reference (same list)
c = a.copy()   # copy (new list)

a.append(4)

print("Original:", a)
print("Reference b:", b)
print("Copy c:", c)
