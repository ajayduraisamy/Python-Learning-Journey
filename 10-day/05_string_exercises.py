# 05_string_exercises.py
# String practice

# 1. Count vowels
text = "programming"
vowels = 0
for c in text:
    if c in "aeiou":
        vowels += 1
print("Vowel count:", vowels)

# 2. Reverse string
rev = text[::-1]
print("Reversed:", rev)

# 3. Check palindrome
word = "madam"
print("Palindrome?" , word == word[::-1])
