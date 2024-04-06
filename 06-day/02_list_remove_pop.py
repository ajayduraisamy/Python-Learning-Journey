# 02_list_remove_pop.py
# remove(), pop(), delete items

fruits = ["apple", "banana", "orange", "mango"]

fruits.remove("banana")  # remove by value
popped = fruits.pop(1)   # remove by index

print("List after removal:", fruits)
print("Popped item:", popped)
