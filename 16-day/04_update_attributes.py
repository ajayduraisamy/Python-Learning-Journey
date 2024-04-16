# 04_update_attributes.py
# Updating object attributes

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car = Car("BMW", 2020)
print("Before:", car.brand, car.year)

car.year = 2024  # update attribute
print("After:", car.brand, car.year)
