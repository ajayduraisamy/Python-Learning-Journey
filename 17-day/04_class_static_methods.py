# 04_class_static_methods.py
# Class methods + static methods

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

    @staticmethod
    def welcome_msg():
        return "Welcome to Python OOP!"

s = Student("Ajay")
print(Student.welcome_msg())
Student.change_school("XYZ School")
print("School:", Student.school)
