# 02_kwargs.py
# Functions with **kwargs (keyword arguments)

def print_info(**details):
    for key, value in details.items():
        print(key, ":", value)

print_info(name="Ajay", age=22, city="Chennai")
