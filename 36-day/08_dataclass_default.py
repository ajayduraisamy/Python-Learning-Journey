# 08_dataclass_default.py
# Dataclass with default values

from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float = 100.0
    tags: list = field(default_factory=list)

p = Product("Laptop")
print(p)
