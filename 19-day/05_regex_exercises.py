# 05_regex_exercises.py
# Practical regex tasks

import re

# 1. Extract all numbers
text = "Order IDs: 123, 456, 789"
print("Numbers:", re.findall(r"\d+", text))

# 2. Validate phone number
phone = "9876543210"
if re.fullmatch(r"\d{10}", phone):
    print("Valid phone")
else:
    print("Invalid phone")

# 3. Mask email
email = "user@example.com"
masked = re.sub(r"(.)(.*)(@.*)", r"\1***\3", email)
print("Masked email:", masked)
