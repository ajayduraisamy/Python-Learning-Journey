# 01_inheritance.py
# Single inheritance example

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

d = Dog()
print(d.speak())
