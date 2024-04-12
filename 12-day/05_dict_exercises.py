# 05_dict_exercises.py
# Dictionary practice problems

marks = {"math": 88, "science": 92, "english": 75}

# total + average
total = sum(marks.values())
avg = total / len(marks)

print("Total:", total)
print("Average:", avg)

# reverse key-value (value becomes key)
rev = {v: k for k, v in marks.items()}
print("Reversed dict:", rev)
