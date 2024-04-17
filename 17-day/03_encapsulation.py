# 03_encapsulation.py
# Private attributes + getter/setter

class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private

    def deposit(self, amt):
        self.__balance += amt

    def get_balance(self):
        return self.__balance

acc = Bank(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())
