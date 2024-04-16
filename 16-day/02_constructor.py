# 02_constructor.py
# Using __init__ constructor

class Student:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

s = Student("Ajay", "CSE")
print(s.name, "-", s.dept)
