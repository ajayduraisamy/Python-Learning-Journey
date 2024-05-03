# 19_list_comprehension_nested.py
# Nested list comprehension

matrix = [[1,2,3],[4,5,6],[7,8,9]]

flat = [num for row in matrix for num in row]

print("Flattened matrix:", flat)
