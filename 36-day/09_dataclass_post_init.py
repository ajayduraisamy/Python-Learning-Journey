# 09_dataclass_post_init.py
# Dataclass __post_init__ usage

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: int

    def __post_init__(self):
        if self.salary < 0:
            self.salary = 0  # fix negative salary

emp = Employee("Kumar", -4000)
print(emp)
