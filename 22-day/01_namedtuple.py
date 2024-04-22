# 01_namedtuple.py
# Using namedtuple

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])
p = Person("Ajay", 22, "Chennai")

print(p.name, p.age, p.city)
