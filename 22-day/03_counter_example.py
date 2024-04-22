# 03_counter_example.py
# Counting elements using Counter

from collections import Counter

items = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = Counter(items)
print("Counts:", count)
print("Most common:", count.most_common(1))
