# 03_break_continue.py
# break and continue examples

print("Break example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\nContinue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
