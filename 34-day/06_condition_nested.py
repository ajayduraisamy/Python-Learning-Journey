# 06_condition_nested.py
# Nested + conditional comprehension

matrix = [[1,2,3],[4,5,6],[7,8,9]]
even_nums = [n for row in matrix for n in row if n % 2 == 0]
print(even_nums)
