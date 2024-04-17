# 02_polymorphism.py
# Method overriding (polymorphism)

class Bird:
    def fly(self):
        return "Bird flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying low"

class Eagle(Bird):
    def fly(self):
        return "Eagle flying high"

for b in (Bird(), Sparrow(), Eagle()):
    print(b.fly())
