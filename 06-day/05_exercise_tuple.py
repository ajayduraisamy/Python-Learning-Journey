# 05_exercise_tuple.py
# Tuple exercises

# Create a tuple of fruits
fruits = ("apple", "banana", "orange", "mango", "grape")
print(fruits)

# Print first and last fruit
print("First:", fruits[0])
print("Last:", fruits[-1])

# Check if an item exists
print("apple" in fruits)

# Convert tuple to list -> modify -> back to tuple
temp = list(fruits)
temp.append("kiwi")
fruits = tuple(temp)
print("Updated tuple:", fruits)
