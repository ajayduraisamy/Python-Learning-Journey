# 07_dataclass_basic.py
# Basic dataclass example

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Ajay", 22)
print(u)
