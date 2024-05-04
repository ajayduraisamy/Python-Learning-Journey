# 09_reverse_comprehension.py
# Reverse strings inside a list using comprehension

words = ["python", "ajay", "developer"]
reversed_words = [w[::-1] for w in words]
print(reversed_words)
