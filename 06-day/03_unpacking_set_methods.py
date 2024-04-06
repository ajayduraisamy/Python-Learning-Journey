# 03_unpacking_set_methods.py
# Tuple unpacking + Set methods

person = ("Ajay", 22, "Developer")
name, age, job = person
print("Unpacked:", name, age, job)

skills = {"python", "react", "flask"}
skills.add("docker")
skills.discard("react")

print("Updated set:", skills)
