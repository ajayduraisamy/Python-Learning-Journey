# 03_class_methods.py
# Class with methods

class Calculator:
    def add(self, a, b):
        return a + b
    
    def mul(self, a, b):
        return a * b

c = Calculator()
print("Add:", c.add(10, 20))
print("Multiply:", c.mul(5, 6))
