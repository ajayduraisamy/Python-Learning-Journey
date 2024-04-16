# 05_oop_exercises.py
# OOP practice problems

# 1. Animal class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return self.name + " makes a sound."

a = Animal("Dog")
print(a.sound())

# 2. Bank account class
class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def get_balance(self):
        return self.balance

acc = Account(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())
