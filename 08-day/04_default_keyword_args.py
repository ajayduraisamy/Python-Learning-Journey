# 04_default_keyword_args.py
# Default arguments + keyword arguments

def info(name, age=18, city="Chennai"):
    print(f"Name: {name}, Age: {age}, City: {city}")

info("Ajay")
info("Kumar", age=25)
info(city="Bangalore", name="Suri", age=28)
