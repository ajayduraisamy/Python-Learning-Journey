# 20_lambda_sort.py
# Sorting with lambda key

students = [
    ("Ajay", 22),
    ("Kumar", 25),
    ("Suri", 20)
]

sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by age:", sorted_students)
