# 04_list_looping.py
# loop through list

names = ["Ajay", "Kumar", "Suri", "Raj"]

print("Normal loop:")
for n in names:
    print(n)

print("\nIndex loop:")
for i in range(len(names)):
    print(i, "->", names[i])
